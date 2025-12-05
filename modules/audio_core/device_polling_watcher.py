"""
DevicePollingWatcher - Polling fallback

В режиме «нет уведомлений» делает bus.list_devices() каждые 5 сек,
сравнивает default UID с кешем и воспроизводит тоже событие.
"""

import logging
import threading
import time
from typing import Optional
from .core_audio_device_bus import CoreAudioDeviceBus
from .device_state_cache import DeviceStateCache
from .core_audio_device_manager import CoreAudioDeviceManager

logger = logging.getLogger(__name__)


class DevicePollingWatcher:
    """
    Watcher для polling fallback
    
    Опрашивает bus.list_devices() каждые 5 сек и сравнивает default UID с кешем.
    """
    
    def __init__(
        self,
        bus: CoreAudioDeviceBus,
        cache: DeviceStateCache,
        manager: CoreAudioDeviceManager,
        poll_interval: float = 5.0
    ):
        """
        Инициализация watcher
        
        Args:
            bus: Шина устройств CoreAudio
            cache: Кэш состояний устройств
            manager: Менеджер устройств (для публикации событий)
            poll_interval: Интервал опроса в секундах (по умолчанию 5.0)
        """
        self._bus = bus
        self._cache = cache
        self._manager = manager
        self._poll_interval = poll_interval
        
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        
        logger.info(f"DevicePollingWatcher создан (интервал: {poll_interval} сек)")
    
    def start(self):
        """Запускает polling watcher"""
        if self._running:
            logger.warning("⚠️ DevicePollingWatcher уже запущен")
            return
        
        self._running = True
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._polling_loop, daemon=True)
        self._thread.start()
        logger.info("✅ DevicePollingWatcher запущен")
    
    def stop(self):
        """Останавливает polling watcher"""
        if not self._running:
            return
        
        self._running = False
        self._stop_event.set()
        
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2.0)
        
        logger.info("✅ DevicePollingWatcher остановлен")
    
    def _polling_loop(self):
        """Основной цикл polling"""
        logger.info("🔄 Polling loop запущен")
        
        while self._running and not self._stop_event.is_set():
            try:
                # Проверяем INPUT устройства
                self._check_direction("input")
                
                # Проверяем OUTPUT устройства
                self._check_direction("output")
                
                # Ждём до следующего опроса
                if self._stop_event.wait(self._poll_interval):
                    break  # Получен сигнал остановки
                    
            except Exception as e:
                logger.error(f"❌ Ошибка в polling loop: {e}", exc_info=True)
                # Продолжаем работу даже при ошибке
                if self._stop_event.wait(1.0):
                    break
        
        logger.info("🔄 Polling loop завершён")
    
    def _check_direction(self, direction: str):
        """
        Проверяет изменение устройства для направления
        
        Args:
            direction: Направление ("input" или "output")
        """
        try:
            # Получаем текущее дефолтное устройство
            current_info = self._bus.get_default_device(direction)
            if not current_info:
                logger.debug(f"🔍 [POLLING] {direction.upper()}: текущее устройство не найдено")
                return
            
            current_name = current_info.get('name', 'Unknown')
            current_uid = current_info.get('uid')
            
            # Получаем устройство из кэша
            try:
                if direction == "input":
                    cached_device = self._cache.get_default_input() if self._cache.has_input() else None
                else:
                    cached_device = self._cache.get_default_output() if self._cache.has_output() else None
            except RuntimeError:
                cached_device = None
            
            # Сравниваем UID и имя (для обнаружения изменений)
            cached_uid = cached_device.uid if cached_device else None
            cached_name = cached_device.name if cached_device else None
            
            # ✅ ДИАГНОСТИКА: Логируем каждую проверку для отладки
            logger.debug(
                f"🔍 [POLLING] {direction.upper()}: текущее=\"{current_name}\" (uid={current_uid}), "
                f"кэш=\"{cached_name}\" (uid={cached_uid})"
            )
            
            # ✅ ИСПРАВЛЕНИЕ: Публикуем событие если:
            # 1. Устройство найдено впервые (cached_device is None)
            # 2. UID изменился
            # 3. Имя изменилось (для случаев, когда UID может совпадать, но устройство другое)
            if cached_device is None or current_uid != cached_uid or current_name != cached_name:
                # Устройство изменилось или найдено впервые
                if cached_device is None:
                    logger.info(f"✅ [POLLING] Found default {direction} (первое обнаружение): \"{current_info.get('name', 'Unknown')}\" (uid: {current_uid})")
                else:
                    logger.info(f"🔄 [{direction.upper()}] Обнаружено изменение устройства через polling: {cached_uid} -> {current_uid}")
                
                # Нормализуем устройство
                from .types import DeviceDescriptor
                new_descriptor = DeviceDescriptor(
                    uid=current_info.get('uid', 'unknown'),
                    name=current_info.get('name', 'Unknown'),
                    latency=current_info.get('latency', 0.0),
                    blocksize=current_info.get('blocksize', 0),
                    sample_rate=current_info.get('sample_rate', 48000.0),
                    is_bluetooth=current_info.get('is_bluetooth', False),
                    is_input=(direction == "input"),
                    device_id=current_info.get('device_id')
                )
                
                # Обновляем кэш
                if direction == "input":
                    self._cache.update_default_input(new_descriptor)
                else:
                    # ✅ ДИАГНОСТИКА: Логируем найденное OUTPUT устройство через polling
                    logger.info(
                        f"📡 [POLLING] Found default output: \"{new_descriptor.name}\" "
                        f"(uid: {new_descriptor.uid}, device_id: {new_descriptor.device_id}, "
                        f"is_bluetooth: {new_descriptor.is_bluetooth})"
                    )
                    self._cache.update_default_output(new_descriptor)
                
                # Публикуем событие через manager
                from .types import DeviceChangeEvent
                event = DeviceChangeEvent(
                    direction=direction,
                    old=cached_device,
                    new=new_descriptor,
                    source="polling",
                    timestamp=time.time()
                )
                
                # Используем публичный метод manager для публикации
                self._manager.publish_device_change_event(event)
                
        except Exception as e:
            logger.error(f"❌ Ошибка проверки направления {direction}: {e}", exc_info=True)

