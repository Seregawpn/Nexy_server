"""
CoreAudioDeviceManager - Менеджер устройств

Получает события от Bus, нормализует в DeviceDescriptor, обновляет DeviceStateCache,
публикует DeviceChangeEvent.
"""

import asyncio
import logging
import threading
import time
from typing import Optional, Dict, Any
from integration.core.event_bus import EventBus
from .core_audio_device_bus import CoreAudioDeviceBus
from .device_state_cache import DeviceStateCache
from .types import DeviceDescriptor, DeviceChangeEvent

logger = logging.getLogger(__name__)


class CoreAudioDeviceManager:
    """
    Менеджер устройств CoreAudio
    
    Алгоритм:
    1. Подписывается на bus.subscribe_raw_events(callback)
    2. При callback: преобразует raw → DeviceDescriptor, обновляет DeviceStateCache, публикует DeviceChangeEvent
    3. Если нотификации не пришли 1.5 сек (проверка timer), запускает DevicePollingWatcher
    4. После первого успешного notification отключает watcher
    """
    
    def __init__(
        self,
        bus: CoreAudioDeviceBus,
        cache: DeviceStateCache,
        event_bus: EventBus
    ):
        """
        Инициализация менеджера
        
        Args:
            bus: Шина устройств CoreAudio
            cache: Кэш состояний устройств
            event_bus: Шина событий
        """
        self._bus = bus
        self._cache = cache
        self._event_bus = event_bus
        
        self._notification_received = {
            'input': False,
            'output': False
        }
        self._notification_lock = threading.Lock()
        self._polling_watcher: Optional[Any] = None  # Будет установлен извне
        self._polling_timer: Optional[threading.Timer] = None
        
        logger.info("CoreAudioDeviceManager создан")
    
    def start_monitoring(self, monitor_input: bool = True, monitor_output: bool = True) -> bool:
        """
        Запускает мониторинг устройств
        
        Args:
            monitor_input: Мониторить INPUT устройства
            monitor_output: Мониторить OUTPUT устройства
        
        Returns:
            True если запуск успешен (или доступен polling fallback)
        """
        # Инициализируем начальное состояние устройств
        self._initialize_initial_devices(monitor_input, monitor_output)
        
        core_audio_success = True
        
        # Пытаемся подписаться на CoreAudio нотификации
        if monitor_input:
            if not self._subscribe_direction("input"):
                core_audio_success = False
        
        if monitor_output:
            if not self._subscribe_direction("output"):
                core_audio_success = False
        
        # ✅ ИСПРАВЛЕНИЕ: Запускаем polling всегда (даже если CoreAudio работает)
        # Это гарантирует обнаружение изменений устройств (например, подключение AirPods)
        # даже если CoreAudio notifications не срабатывают для некоторых устройств
        if self._polling_watcher:
            logger.info("✅ [MANAGER] Запускаем polling watcher для отслеживания изменений устройств")
            self._polling_watcher.start()
        else:
            logger.warning("⚠️ [MANAGER] Polling watcher не установлен")
        
        # Если CoreAudio недоступен, логируем это
        if not core_audio_success:
            logger.info("ℹ️ CoreAudio нотификации недоступны, используем только polling fallback")
        
        # Запускаем таймер для проверки нотификаций (1.5 сек) только если CoreAudio доступен
        if core_audio_success:
            self._start_notification_timer()
        
        # Всегда возвращаем True - polling fallback обеспечит работу
        return True
    
    def _initialize_initial_devices(self, monitor_input: bool, monitor_output: bool):
        """
        Инициализирует начальное состояние устройств в кэше
        
        Args:
            monitor_input: Инициализировать INPUT устройство
            monitor_output: Инициализировать OUTPUT устройство
        """
        try:
            if monitor_input:
                input_info = self._bus.get_default_device("input")
                if input_info:
                    descriptor = self._normalize_device(input_info, "input")
                    if descriptor:
                        self._cache.update_default_input(descriptor)
                        logger.info(f"✅ Начальное INPUT устройство инициализировано: {descriptor.name}")
            
            if monitor_output:
                output_info = self._bus.get_default_device("output")
                if output_info:
                    descriptor = self._normalize_device(output_info, "output")
                    if descriptor:
                        logger.info(
                            f"✅ [INIT] Начальное OUTPUT устройство инициализировано: \"{descriptor.name}\" "
                            f"(uid: {descriptor.uid}, device_id: {descriptor.device_id}, is_bluetooth: {descriptor.is_bluetooth})"
                        )
                        self._cache.update_default_output(descriptor)
                        
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации начальных устройств: {e}", exc_info=True)
    
    def _subscribe_direction(self, direction: str) -> bool:
        """
        Подписывается на нотификации для направления
        
        Args:
            direction: Направление ("input" или "output")
            
        Returns:
            True если подписка успешна
        """
        def callback(raw_data: Dict[str, Any]):
            """Callback для обработки сырых данных"""
            try:
                # Преобразуем raw → DeviceDescriptor
                descriptor = self._normalize_device(raw_data, direction)
                if not descriptor:
                    logger.warning(f"⚠️ Не удалось нормализовать устройство {direction}")
                    return
                
                # Получаем старое устройство из кэша
                old_descriptor = None
                try:
                    if direction == "input":
                        old_descriptor = self._cache.get_default_input() if self._cache.has_input() else None
                    else:
                        old_descriptor = self._cache.get_default_output() if self._cache.has_output() else None
                except RuntimeError:
                    pass  # Устройство ещё не инициализировано
                
                # Обновляем кэш
                if direction == "input":
                    self._cache.update_default_input(descriptor)
                else:
                    # ✅ ДИАГНОСТИКА: Логируем обновление OUTPUT устройства
                    logger.info(
                        f"📝 [CACHE_UPDATE] Обновление OUTPUT устройства в cache: "
                        f"uid=\"{descriptor.uid}\", name=\"{descriptor.name}\", "
                        f"device_id={descriptor.device_id}, is_bluetooth={descriptor.is_bluetooth}"
                    )
                    self._cache.update_default_output(descriptor)
                    logger.info(
                        f"✅ [CACHE_UPDATE] OUTPUT устройство успешно обновлено в cache: \"{descriptor.name}\""
                    )
                
                # Публикуем событие
                event = DeviceChangeEvent(
                    direction=direction,
                    old=old_descriptor,
                    new=descriptor,
                    source="sys",
                    timestamp=time.time()
                )
                
                self.publish_device_change_event(event)
                
                # Отмечаем, что нотификация получена
                with self._notification_lock:
                    self._notification_received[direction] = True
                    # Отключаем polling watcher после первого успешного notification
                    if self._polling_watcher and all(self._notification_received.values()):
                        logger.info("✅ Нотификации получены, отключаем polling watcher")
                        self._stop_polling_watcher()
                        self._cancel_notification_timer()
                
            except Exception as e:
                logger.error(f"❌ Ошибка в callback обработки устройства ({direction}): {e}", exc_info=True)
        
        return self._bus.subscribe_raw_events(callback, direction)
    
    def _normalize_device(self, raw_data: Dict[str, Any], direction: str) -> Optional[DeviceDescriptor]:
        """
        Нормализует сырые данные в DeviceDescriptor
        
        Args:
            raw_data: Сырые данные устройства
            direction: Направление ("input" или "output")
        
        Returns:
            DeviceDescriptor или None
        """
        try:
            return DeviceDescriptor(
                uid=raw_data.get('uid', 'unknown'),
                name=raw_data.get('name', 'Unknown'),
                latency=raw_data.get('latency', 0.0),
                blocksize=raw_data.get('blocksize', 0),
                sample_rate=raw_data.get('sample_rate', 48000.0),
                is_bluetooth=raw_data.get('is_bluetooth', False),
                is_input=(direction == "input"),
                device_id=raw_data.get('device_id')
            )
        except Exception as e:
            logger.error(f"❌ Ошибка нормализации устройства: {e}", exc_info=True)
            return None
    
    def publish_device_change_event(self, event: DeviceChangeEvent):
        """
        Публикует событие в EventBus (публичный метод для использования извне)
        
        Формат события совместим с существующими интеграциями:
        - device_name, device_id, is_bluetooth, source
        - old_device_name, old_device_id
        
        Args:
            event: Событие смены устройства
        """
        try:
            event_name = f"device.default_{event.direction}_changed"
            
            # ✅ ДИАГНОСТИКА: Логируем публикацию события
            old_name = event.old.name if event.old else None
            logger.info(
                f"📢 [MANAGER] Публикуем событие {event_name}: "
                f"\"{old_name}\" → \"{event.new.name}\" "
                f"(ID: {event.old.device_id if event.old else None} → {event.new.device_id}, "
                f"BT: {event.new.is_bluetooth}, source: {event.source})"
            )
            
            # Формат для обратной совместимости с существующими интеграциями
            payload = {
                # Основные поля (обязательные для обратной совместимости)
                'device_name': event.new.name,
                'device_id': event.new.device_id,
                'is_bluetooth': event.new.is_bluetooth,
                'source': 'CORE_AUDIO' if event.source == 'sys' else 'POLLING',
                'old_device_name': event.old.name if event.old else None,
                'old_device_id': event.old.device_id if event.old else None,
                
                # Расширенные поля (для будущего использования)
                'uid': event.new.uid,
                'sample_rate': event.new.sample_rate,
                'latency': event.new.latency,
                'blocksize': event.new.blocksize,
                'old_uid': event.old.uid if event.old else None,
                'old_sample_rate': event.old.sample_rate if event.old else None,
                'direction': event.direction,
                'timestamp': event.timestamp,
            }
            
            # ✅ ИСПРАВЛЕНИЕ: EventBus.publish - async метод, нужно вызывать через create_task
            # Получаем event loop и создаем задачу для публикации
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # Event loop уже запущен - создаем задачу
                    loop.create_task(self._event_bus.publish(event_name, payload))
                    logger.info(f"📢 Событие опубликовано (async): {event_name} ({event.new.name})")
                else:
                    # Event loop не запущен - запускаем синхронно
                    loop.run_until_complete(self._event_bus.publish(event_name, payload))
                    logger.info(f"📢 Событие опубликовано (sync): {event_name} ({event.new.name})")
            except RuntimeError:
                # Нет event loop - создаем новый в отдельном потоке
                import threading
                def publish_in_thread():
                    new_loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(new_loop)
                    try:
                        new_loop.run_until_complete(self._event_bus.publish(event_name, payload))
                    finally:
                        new_loop.close()
                
                thread = threading.Thread(target=publish_in_thread, daemon=True)
                thread.start()
                logger.info(f"📢 Событие опубликовано (thread): {event_name} ({event.new.name})")
            
        except Exception as e:
            logger.error(f"❌ Ошибка публикации события: {e}", exc_info=True)
    
    def _start_notification_timer(self):
        """Запускает таймер для проверки нотификаций (1.5 сек)"""
        def check_notifications():
            """Проверка, пришли ли нотификации"""
            with self._notification_lock:
                if not all(self._notification_received.values()):
                    logger.warning("⚠️ Нотификации не пришли за 1.5 сек, запускаем polling watcher")
                    # Polling watcher будет запущен извне через set_polling_watcher
                    if self._polling_watcher:
                        logger.info("✅ [MANAGER] Запускаем polling watcher (нотификации не пришли)")
                        self._polling_watcher.start()
                    else:
                        logger.warning("⚠️ [MANAGER] Polling watcher не установлен, не можем запустить fallback")
        
        self._polling_timer = threading.Timer(1.5, check_notifications)
        self._polling_timer.start()
    
    def _cancel_notification_timer(self):
        """Отменяет таймер проверки нотификаций"""
        if self._polling_timer:
            self._polling_timer.cancel()
            self._polling_timer = None
    
    def _stop_polling_watcher(self):
        """Останавливает polling watcher"""
        if self._polling_watcher:
            try:
                self._polling_watcher.stop()
            except Exception as e:
                logger.error(f"❌ Ошибка остановки polling watcher: {e}", exc_info=True)
    
    def set_polling_watcher(self, watcher):
        """
        Устанавливает polling watcher
        
        Args:
            watcher: Экземпляр DevicePollingWatcher
        """
        self._polling_watcher = watcher
    
    def stop_monitoring(self):
        """Останавливает мониторинг устройств"""
        self._cancel_notification_timer()
        self._stop_polling_watcher()
        # Отписка от нотификаций делается через bus.cleanup()
        logger.info("✅ Мониторинг устройств остановлен")

