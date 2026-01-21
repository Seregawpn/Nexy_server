"""
DeviceChangePublisher - Единый монитор устройств INPUT/OUTPUT

✅ ЦИКЛ 1: Единый компонент для мониторинга устройств
- Подписка на Core Audio нотификации (приоритет 1)
- Fallback на polling при недоступности Core Audio
- Публикация событий в EventBus: device.default_input_changed / device.default_output_changed
- Debounce для rapid device switch
- Логирование источника (CoreAudio vs polling)
"""

import logging
import platform
import threading
import time
import subprocess
import json
import shutil
from typing import Optional, Dict, Any, Callable, Literal
from dataclasses import dataclass
from enum import Enum

# Для проверки feature flag
try:
    from config.unified_config_loader import unified_config
except ImportError:
    unified_config = None
    logger = logging.getLogger(__name__)
    logger.warning("⚠️ unified_config недоступен, feature flag device_switch_v2 не будет работать")

logger = logging.getLogger(__name__)

# Попытка импорта CoreAudioManager
try:
    # Используем относительный импорт через sys.path
    import sys
    import os
    # Получаем корень проекта (два уровня вверх от этого файла)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    from modules.speech_playback.macos.core_audio import CoreAudioManager
    CORE_AUDIO_MANAGER_AVAILABLE = True
except ImportError as e:
    CORE_AUDIO_MANAGER_AVAILABLE = False
    CoreAudioManager = None
    logger.debug(f"⚠️ CoreAudioManager недоступен: {e}")


class DeviceChangeSource(Enum):
    """Источник события смены устройства"""
    CORE_AUDIO = "core_audio"  # Core Audio нотификации
    POLLING = "polling"  # Polling fallback


@dataclass
class DeviceInfo:
    """Информация об устройстве"""
    name: str
    device_id: Optional[int]
    is_bluetooth: bool
    source: DeviceChangeSource


class DeviceChangePublisher:
    """
    Единый монитор устройств INPUT/OUTPUT
    
    Функции:
    - Подписка на Core Audio нотификации (приоритет 1)
    - Fallback на polling при недоступности Core Audio
    - Публикация событий в EventBus
    - Debounce для rapid device switch
    - Логирование источника (CoreAudio vs polling)
    """
    
    def __init__(self, event_bus):
        """
        Инициализация издателя
        
        Args:
            event_bus: EventBus для публикации событий
        """
        self.event_bus = event_bus
        self._is_macos = platform.system() == "Darwin"
        
        # Core Audio менеджер
        self._core_audio_manager: Optional[CoreAudioManager] = None
        self._core_audio_available = False
        
        # Состояние мониторинга
        self._monitoring_input = False
        self._monitoring_output = False
        self._monitoring_lock = threading.Lock()
        
        # Текущие устройства
        self._current_input_device: Optional[DeviceInfo] = None
        self._current_output_device: Optional[DeviceInfo] = None
        
        # Polling fallback
        self._polling_thread: Optional[threading.Thread] = None
        self._stop_polling = threading.Event()
        self._polling_interval_input = 1.0  # секунд для обычных устройств
        self._polling_interval_output = 1.0  # секунд для обычных устройств
        self._polling_interval_bt = 5.0  # секунд для BT устройств
        
        # Debounce
        self._debounce_delay = 0.3  # секунд
        self._debounce_timers: Dict[str, threading.Timer] = {}
        self._debounce_lock = threading.Lock()
        
        # Кэш для уменьшения вызовов SwitchAudioSource
        self._device_name_cache: Dict[str, tuple[str, float]] = {}  # device_type -> (name, timestamp)
        self._cache_ttl = 0.5  # секунд - время жизни кэша
        self._cache_lock = threading.Lock()
        
        # Инициализация Core Audio менеджера
        if self._is_macos and CORE_AUDIO_MANAGER_AVAILABLE:
            try:
                self._core_audio_manager = CoreAudioManager()
                if self._core_audio_manager.initialize():
                    self._core_audio_available = self._core_audio_manager.is_notifications_available()
                    logger.info(f"✅ CoreAudioManager инициализирован (notifications: {self._core_audio_available})")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось инициализировать CoreAudioManager: {e}")
                self._core_audio_available = False
        
        logger.info(f"🔧 DeviceChangePublisher создан (macOS: {self._is_macos}, CoreAudio: {self._core_audio_available})")
    
    async def start_monitoring(self, monitor_input: bool = True, monitor_output: bool = True) -> bool:
        """
        Запуск мониторинга устройств
        
        Args:
            monitor_input: Мониторить INPUT устройства
            monitor_output: Мониторить OUTPUT устройства
        
        Returns:
            True если мониторинг запущен успешно
        """
        try:
            with self._monitoring_lock:
                if (self._monitoring_input and monitor_input) or (self._monitoring_output and monitor_output):
                    logger.warning("⚠️ Мониторинг уже запущен для запрошенных устройств")
                    return True
                
                self._monitoring_input = monitor_input or self._monitoring_input
                self._monitoring_output = monitor_output or self._monitoring_output
                
                # Инициализация текущих устройств
                if monitor_input:
                    input_info = self._get_current_input_device()
                    if input_info:
                        self._current_input_device = input_info
                        logger.info(f"🎤 Текущий INPUT: \"{input_info.name}\" (ID={input_info.device_id}, BT={input_info.is_bluetooth})")
                
                if monitor_output:
                    output_info = self._get_current_output_device()
                    if output_info:
                        self._current_output_device = output_info
                        logger.info(f"🔊 Текущий OUTPUT: \"{output_info.name}\" (ID={output_info.device_id}, BT={output_info.is_bluetooth})")
                
                # Попытка использовать Core Audio нотификации (приоритет 1)
                core_audio_success = False
                if self._core_audio_available:
                    # Подписка на INPUT нотификации
                    if monitor_input:
                        if self._core_audio_manager.start_device_notifications(
                            self._on_input_device_changed_core_audio,
                            device_type="input"
                        ):
                            logger.info("✅ [INPUT] Core Audio нотификации активированы (событийная реакция)")
                            core_audio_success = True
                        else:
                            logger.warning("⚠️ [INPUT] Не удалось подписаться на Core Audio нотификации, используем polling")
                    
                    # Подписка на OUTPUT нотификации
                    if monitor_output:
                        if self._core_audio_manager.start_device_notifications(
                            self._on_output_device_changed_core_audio,
                            device_type="output"
                        ):
                            logger.info("✅ [OUTPUT] Core Audio нотификации активированы (событийная реакция)")
                            core_audio_success = True
                        else:
                            logger.warning("⚠️ [OUTPUT] Не удалось подписаться на Core Audio нотификации, используем polling")
                    
                    # Если хотя бы одна подписка успешна, публикуем событие
                    if core_audio_success:
                        await self.event_bus.publish("device.monitoring_started", {
                            "source": DeviceChangeSource.CORE_AUDIO.value,
                            "monitor_input": monitor_input,
                            "monitor_output": monitor_output
                        })
                        # Если обе подписки успешны, не запускаем polling
                        if (not monitor_input or self._core_audio_manager._notification_listener_id_input) and \
                           (not monitor_output or self._core_audio_manager._notification_listener_id_output):
                            return True
                
                # Fallback на polling
                if not self._polling_thread or not self._polling_thread.is_alive():
                    self._stop_polling.clear()
                    self._polling_thread = threading.Thread(
                        target=self._polling_loop,
                        name="DeviceChangePublisher-Polling",
                        daemon=True
                    )
                    self._polling_thread.start()
                    logger.info(f"🚀 [POLLING] Запуск polling мониторинга (INPUT: {monitor_input}, OUTPUT: {monitor_output})")
                    
                    # Публикуем событие о запуске мониторинга
                    await self.event_bus.publish("device.monitoring_started", {
                        "source": DeviceChangeSource.POLLING.value,
                        "monitor_input": monitor_input,
                        "monitor_output": monitor_output
                    })
                
                return True
                
        except Exception as e:
            logger.error(f"❌ Ошибка запуска мониторинга: {e}", exc_info=True)
            return False
    
    async def stop_monitoring(self):
        """Остановка мониторинга устройств"""
        try:
            with self._monitoring_lock:
                self._monitoring_input = False
                self._monitoring_output = False
                
                # Остановка Core Audio нотификаций
                if self._core_audio_manager:
                    # Останавливаем все нотификации (если device_type=None)
                    self._core_audio_manager.stop_device_notifications(device_type=None)
                
                # Остановка polling
                if self._polling_thread and self._polling_thread.is_alive():
                    self._stop_polling.set()
                    self._polling_thread.join(timeout=2.0)
                    self._polling_thread = None
                
                # Отмена debounce таймеров
                with self._debounce_lock:
                    for timer in self._debounce_timers.values():
                        timer.cancel()
                    self._debounce_timers.clear()
                
                logger.info("🛑 Мониторинг устройств остановлен")
                
                # Публикуем событие об остановке мониторинга
                await self.event_bus.publish("device.monitoring_stopped", {})
                
        except Exception as e:
            logger.error(f"❌ Ошибка остановки мониторинга: {e}", exc_info=True)
    
    def get_current_input_device(self) -> Optional[DeviceInfo]:
        """Получить текущее INPUT устройство"""
        return self._current_input_device
    
    def get_current_output_device(self) -> Optional[DeviceInfo]:
        """Получить текущее OUTPUT устройство"""
        return self._current_output_device
    
    def is_core_audio_available(self) -> bool:
        """Проверяет, доступны ли Core Audio нотификации"""
        return self._core_audio_available
    
    # === Core Audio callbacks ===
    
    def _on_input_device_changed_core_audio(self):
        """
        Callback для Core Audio нотификаций о смене INPUT устройства
        
        ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Выполняем в отдельном потоке для предотвращения блокировки
        """
        # Запускаем в отдельном потоке, чтобы не блокировать Core Audio callback
        def _async_get_device():
            try:
                logger.info("🔔 [INPUT] Core Audio нотификация: default input устройство изменилось")
                new_device = self._get_current_input_device()
                if new_device:
                    self._handle_device_change("input", new_device, DeviceChangeSource.CORE_AUDIO)
            except Exception as e:
                logger.error(f"❌ Ошибка в Core Audio INPUT callback: {e}", exc_info=True)
        
        # Запускаем в отдельном потоке
        thread = threading.Thread(target=_async_get_device, name="DeviceChange-Input", daemon=True)
        thread.start()
    
    def _on_output_device_changed_core_audio(self):
        """
        Callback для Core Audio нотификаций о смене OUTPUT устройства
        
        ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Выполняем в отдельном потоке для предотвращения блокировки
        """
        # Запускаем в отдельном потоке, чтобы не блокировать Core Audio callback
        def _async_get_device():
            try:
                logger.info("🔔 [OUTPUT] Core Audio нотификация: default output устройство изменилось")
                new_device = self._get_current_output_device()
                if new_device:
                    self._handle_device_change("output", new_device, DeviceChangeSource.CORE_AUDIO)
            except Exception as e:
                logger.error(f"❌ Ошибка в Core Audio OUTPUT callback: {e}", exc_info=True)
        
        # Запускаем в отдельном потоке
        thread = threading.Thread(target=_async_get_device, name="DeviceChange-Output", daemon=True)
        thread.start()
    
    # === Polling fallback ===
    
    def _polling_loop(self):
        """Основной цикл polling мониторинга"""
        logger.info("🔄 [POLLING] Запуск polling цикла мониторинга устройств")
        
        while not self._stop_polling.is_set():
            try:
                # Проверка INPUT устройства
                if self._monitoring_input:
                    new_input = self._get_current_input_device()
                    if new_input and self._current_input_device:
                        # ✅ ФАЗА 1: Улучшенное сравнение устройств
                        # При включенном feature flag сравниваем по device_id (более надежно)
                        # При выключенном - по имени (старая логика)
                        device_changed = False
                        if unified_config:
                            try:
                                feature_config = unified_config._load_config().get("features", {}).get("device_switch_v2", {})
                                if feature_config.get("enabled", False):
                                    # Новая логика: сравниваем по device_id
                                    device_changed = (
                                        new_input.device_id != self._current_input_device.device_id or
                                        new_input.name != self._current_input_device.name
                                    )
                                else:
                                    # Старая логика: сравниваем по имени
                                    device_changed = new_input.name != self._current_input_device.name
                            except Exception:
                                # Fallback на сравнение по имени при ошибке проверки флага
                                device_changed = new_input.name != self._current_input_device.name
                        else:
                            # Fallback на сравнение по имени если unified_config недоступен
                            device_changed = new_input.name != self._current_input_device.name
                        
                        if device_changed:
                            self._handle_device_change("input", new_input, DeviceChangeSource.POLLING)
                    elif new_input and not self._current_input_device:
                        # Первая инициализация
                        self._current_input_device = new_input
                
                # Проверка OUTPUT устройства
                if self._monitoring_output:
                    new_output = self._get_current_output_device()
                    if new_output and self._current_output_device:
                        # ✅ ФАЗА 1: Улучшенное сравнение устройств
                        # При включенном feature flag сравниваем по device_id (более надежно)
                        # При выключенном - по имени (старая логика)
                        device_changed = False
                        if unified_config:
                            try:
                                feature_config = unified_config._load_config().get("features", {}).get("device_switch_v2", {})
                                if feature_config.get("enabled", False):
                                    # Новая логика: сравниваем по device_id
                                    device_changed = (
                                        new_output.device_id != self._current_output_device.device_id or
                                        new_output.name != self._current_output_device.name
                                    )
                                else:
                                    # Старая логика: сравниваем по имени
                                    device_changed = new_output.name != self._current_output_device.name
                            except Exception:
                                # Fallback на сравнение по имени при ошибке проверки флага
                                device_changed = new_output.name != self._current_output_device.name
                        else:
                            # Fallback на сравнение по имени если unified_config недоступен
                            device_changed = new_output.name != self._current_output_device.name
                        
                        if device_changed:
                            self._handle_device_change("output", new_output, DeviceChangeSource.POLLING)
                    elif new_output and not self._current_output_device:
                        # Первая инициализация
                        self._current_output_device = new_output
                
                # Адаптивный интервал: больше для BT устройств
                interval = self._polling_interval_bt if (
                    (self._current_input_device and self._current_input_device.is_bluetooth) or
                    (self._current_output_device and self._current_output_device.is_bluetooth)
                ) else max(self._polling_interval_input, self._polling_interval_output)
                
                self._stop_polling.wait(interval)
                
            except Exception as e:
                logger.error(f"❌ Ошибка в polling цикле: {e}", exc_info=True)
                self._stop_polling.wait(1.0)  # Пауза при ошибке
    
    # === Обработка смены устройства ===
    
    def _handle_device_change(self, device_type: Literal["input", "output"], new_device: DeviceInfo, source: DeviceChangeSource):
        """
        Обработка смены устройства с debounce
        
        Args:
            device_type: Тип устройства (input/output)
            new_device: Новое устройство
            source: Источник события (CoreAudio/polling)
        """
        try:
            # Отменяем предыдущий debounce таймер для этого типа устройства
            with self._debounce_lock:
                timer_key = f"{device_type}_device_change"
                if timer_key in self._debounce_timers:
                    self._debounce_timers[timer_key].cancel()
                    del self._debounce_timers[timer_key]
                
                # Создаем новый debounce таймер
                def publish_change():
                    try:
                        old_device = self._current_input_device if device_type == "input" else self._current_output_device
                        
                        # Обновляем текущее устройство
                        if device_type == "input":
                            self._current_input_device = new_device
                        else:
                            self._current_output_device = new_device
                        
                        # Публикуем событие
                        event_name = f"device.default_{device_type}_changed"
                        event_data = {
                            "device_name": new_device.name,
                            "device_id": new_device.device_id,
                            "is_bluetooth": new_device.is_bluetooth,
                            "source": source.value,
                            "old_device_name": old_device.name if old_device else None,
                            "old_device_id": old_device.device_id if old_device else None
                        }
                        
                        # Публикуем через EventBus (синхронно, так как мы в отдельном потоке)
                        import asyncio
                        loop = self.event_bus._loop
                        if loop and loop.is_running():
                            asyncio.run_coroutine_threadsafe(
                                self.event_bus.publish(event_name, event_data),
                                loop
                            )
                        else:
                            logger.warning(f"⚠️ EventBus loop не доступен, событие не опубликовано")
                        
                        logger.info(
                            f"🔔 [{device_type.upper()}] Смена устройства: "
                            f"\"{old_device.name if old_device else 'None'}\" → "
                            f"\"{new_device.name}\" (source: {source.value})"
                        )
                        
                        # Удаляем таймер из словаря
                        with self._debounce_lock:
                            if timer_key in self._debounce_timers:
                                del self._debounce_timers[timer_key]
                                
                    except Exception as e:
                        logger.error(f"❌ Ошибка публикации события смены устройства: {e}", exc_info=True)
                
                timer = threading.Timer(self._debounce_delay, publish_change)
                timer.start()
                self._debounce_timers[timer_key] = timer
                
        except Exception as e:
            logger.error(f"❌ Ошибка обработки смены устройства: {e}", exc_info=True)
    
    # === Определение устройств ===
    
    def _get_current_input_device(self) -> Optional[DeviceInfo]:
        """
        Получить текущее INPUT устройство.
        
        ✅ ФАЗА 1, ШАГ 1.2: Упрощенная логика "следуем за системным дефолтом"
        - Если feature flag device_switch_v2 включен: использует sd.default.device[0] напрямую
        - Если feature flag выключен: использует старую логику через SwitchAudioSource (fallback)
        """
        try:
            # ✅ ФАЗА 1: Проверка feature flag
            use_v2_logic = False
            if unified_config:
                try:
                    feature_config = unified_config._load_config().get("features", {}).get("device_switch_v2", {})
                    use_v2_logic = feature_config.get("enabled", False)
                except Exception as e:
                    logger.debug(f"⚠️ Ошибка проверки feature flag device_switch_v2: {e}")
            
            if use_v2_logic:
                # ✅ НОВАЯ ЛОГИКА: Используем системный дефолт PortAudio напрямую
                logger.debug("🔍 [INPUT][V2] Используем системный дефолт PortAudio напрямую")
                try:
                    import sounddevice as sd
                    default_setting = sd.default.device
                    if hasattr(default_setting, '__getitem__'):
                        input_device_id = default_setting[0]  # INPUT устройство (индекс 0)
                        
                        if input_device_id is not None:
                            # Получаем информацию об устройстве
                            try:
                                device_info = sd.query_devices(input_device_id, 'input')
                                if device_info and device_info.get('max_input_channels', 0) > 0:
                                    device_name = device_info.get('name', 'Unknown')
                                    is_bluetooth = self._is_bluetooth_device(device_name)
                                    
                                    logger.debug(
                                        f"✅ [INPUT][V2] Системный дефолт PortAudio: "
                                        f"name=\"{device_name}\", id={input_device_id}, BT={is_bluetooth}"
                                    )
                                    
                                    return DeviceInfo(
                                        name=device_name,
                                        device_id=input_device_id if not is_bluetooth else None,  # BT устройства используют device_id=None
                                        is_bluetooth=is_bluetooth,
                                        source=DeviceChangeSource.POLLING
                                    )
                                else:
                                    logger.warning(f"⚠️ [INPUT][V2] Устройство ID {input_device_id} не является INPUT устройством")
                                    return None
                            except Exception as e:
                                logger.warning(f"⚠️ [INPUT][V2] Ошибка получения информации об устройстве ID {input_device_id}: {e}")
                                return None
                        else:
                            logger.warning("⚠️ [INPUT][V2] sd.default.device[0] вернул None")
                            return None
                    else:
                        logger.warning("⚠️ [INPUT][V2] sd.default.device не поддерживает индексацию")
                        return None
                except Exception as e:
                    logger.warning(f"⚠️ [INPUT][V2] Ошибка получения системного дефолта PortAudio: {e}")
                    return None
            
            # ✅ СТАРАЯ ЛОГИКА (fallback если feature flag выключен)
            logger.debug("🔍 [INPUT][LEGACY] Используем старую логику через SwitchAudioSource")
            device_name = self._get_device_name_via_macos_api("input")
            if not device_name:
                return None
            
            is_bluetooth = self._is_bluetooth_device(device_name)
            device_id = None
            
            # Для обычных устройств пытаемся найти ID в PortAudio
            if not is_bluetooth:
                device_id = self._find_device_id_by_name(device_name, device_type="input")
            
            return DeviceInfo(
                name=device_name,
                device_id=device_id,
                is_bluetooth=is_bluetooth,
                source=DeviceChangeSource.POLLING  # Будет обновлено при публикации события
            )
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения INPUT устройства: {e}")
            return None
    
    def _get_current_output_device(self) -> Optional[DeviceInfo]:
        """
        Получить текущее OUTPUT устройство.
        
        ✅ ФАЗА 1, ШАГ 1.2: Упрощенная логика "следуем за системным дефолтом"
        - Если feature flag device_switch_v2 включен: использует sd.default.device[1] напрямую
        - Если feature flag выключен: использует старую логику через SwitchAudioSource (fallback)
        """
        try:
            # ✅ ФАЗА 1: Проверка feature flag
            use_v2_logic = False
            if unified_config:
                try:
                    feature_config = unified_config._load_config().get("features", {}).get("device_switch_v2", {})
                    use_v2_logic = feature_config.get("enabled", False)
                except Exception as e:
                    logger.debug(f"⚠️ Ошибка проверки feature flag device_switch_v2: {e}")
            
            if use_v2_logic:
                # ✅ НОВАЯ ЛОГИКА: Используем системный дефолт PortAudio напрямую
                logger.debug("🔍 [OUTPUT][V2] Используем системный дефолт PortAudio напрямую")
                try:
                    import sounddevice as sd
                    default_setting = sd.default.device
                    if hasattr(default_setting, '__getitem__'):
                        output_device_id = default_setting[1]  # OUTPUT устройство (индекс 1)
                        
                        if output_device_id is not None:
                            # Получаем информацию об устройстве
                            try:
                                device_info = sd.query_devices(output_device_id, 'output')
                                if device_info and device_info.get('max_output_channels', 0) > 0:
                                    device_name = device_info.get('name', 'Unknown')
                                    is_bluetooth = self._is_bluetooth_device(device_name)
                                    
                                    logger.debug(
                                        f"✅ [OUTPUT][V2] Системный дефолт PortAudio: "
                                        f"name=\"{device_name}\", id={output_device_id}, BT={is_bluetooth}"
                                    )
                                    
                                    return DeviceInfo(
                                        name=device_name,
                                        device_id=output_device_id if not is_bluetooth else None,  # BT устройства используют device_id=None
                                        is_bluetooth=is_bluetooth,
                                        source=DeviceChangeSource.POLLING
                                    )
                                else:
                                    logger.warning(f"⚠️ [OUTPUT][V2] Устройство ID {output_device_id} не является OUTPUT устройством")
                                    return None
                            except Exception as e:
                                logger.warning(f"⚠️ [OUTPUT][V2] Ошибка получения информации об устройстве ID {output_device_id}: {e}")
                                return None
                        else:
                            logger.warning("⚠️ [OUTPUT][V2] sd.default.device[1] вернул None")
                            return None
                    else:
                        logger.warning("⚠️ [OUTPUT][V2] sd.default.device не поддерживает индексацию")
                        return None
                except Exception as e:
                    logger.warning(f"⚠️ [OUTPUT][V2] Ошибка получения системного дефолта PortAudio: {e}")
                    return None
            
            # ✅ СТАРАЯ ЛОГИКА (fallback если feature flag выключен)
            logger.debug("🔍 [OUTPUT][LEGACY] Используем старую логику через SwitchAudioSource")
            device_name = self._get_device_name_via_macos_api("output")
            if not device_name:
                return None
            
            is_bluetooth = self._is_bluetooth_device(device_name)
            device_id = None
            
            # Для обычных устройств пытаемся найти ID в PortAudio
            if not is_bluetooth:
                device_id = self._find_device_id_by_name(device_name, device_type="output")
            
            return DeviceInfo(
                name=device_name,
                device_id=device_id,
                is_bluetooth=is_bluetooth,
                source=DeviceChangeSource.POLLING  # Будет обновлено при публикации события
            )
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения OUTPUT устройства: {e}")
            return None
    
    def _get_device_name_via_macos_api(self, device_type: Literal["input", "output"]) -> Optional[str]:
        """
        Получает имя текущего default устройства через macOS API (SwitchAudioSource)
        
        ⚠️ DEPRECATED: Используется только для fallback диагностики при выключенном feature flag device_switch_v2
        ✅ ФАЗА 1, ШАГ 1.2: Этот метод будет удален в Фазе 2
        
        Args:
            device_type: Тип устройства (input/output)
        
        Returns:
            Имя устройства или None если не удалось получить
        """
        # Проверяем кэш
        current_time = time.time()
        with self._cache_lock:
            if device_type in self._device_name_cache:
                cached_name, cached_time = self._device_name_cache[device_type]
                if current_time - cached_time < self._cache_ttl:
                    logger.debug(f"✅ [{device_type.upper()}] Используем кэш: \"{cached_name}\"")
                    return cached_name
        
        # Кэш устарел или отсутствует - делаем вызов
        try:
            switch_audio_source_path = shutil.which('SwitchAudioSource')
            if not switch_audio_source_path:
                logger.debug(f"⚠️ [{device_type.upper()}] SwitchAudioSource не найден в PATH")
                return None
            
            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Уменьшен таймаут с 5 до 1 секунды для быстрой реакции
            result = subprocess.run(
                [switch_audio_source_path, '-c', '-t', device_type, '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=1  # Уменьшен с 5 до 1 секунды
            )
            
            if result.returncode == 0:
                try:
                    device_info = json.loads(result.stdout.strip())
                    device_name = device_info.get('name', '')
                    if device_name:
                        logger.debug(f"✅ [{device_type.upper()}] macOS default (через SwitchAudioSource): \"{device_name}\"")
                        # Обновляем кэш
                        with self._cache_lock:
                            self._device_name_cache[device_type] = (device_name, current_time)
                        return device_name
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ [{device_type.upper()}] Ошибка парсинга JSON от SwitchAudioSource: {e}")
            else:
                logger.warning(f"⚠️ [{device_type.upper()}] SwitchAudioSource вернул код ошибки {result.returncode}")
                
        except subprocess.TimeoutExpired:
            logger.warning(f"⚠️ [{device_type.upper()}] SwitchAudioSource timeout (1s) - используем кэш если доступен")
            # Пытаемся использовать кэш даже если он устарел
            with self._cache_lock:
                if device_type in self._device_name_cache:
                    cached_name, _ = self._device_name_cache[device_type]
                    logger.debug(f"⚠️ [{device_type.upper()}] Используем устаревший кэш: \"{cached_name}\"")
                    return cached_name
        except Exception as e:
            logger.warning(f"⚠️ [{device_type.upper()}] Ошибка получения имени через SwitchAudioSource: {e}")
            # Пытаемся использовать кэш при ошибке
            with self._cache_lock:
                if device_type in self._device_name_cache:
                    cached_name, _ = self._device_name_cache[device_type]
                    logger.debug(f"⚠️ [{device_type.upper()}] Используем кэш при ошибке: \"{cached_name}\"")
                    return cached_name
        
        return None
    
    def _is_bluetooth_device(self, name: str) -> bool:
        """Проверяет, является ли устройство Bluetooth по имени"""
        if not name:
            return False
        lowered = name.lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpods", "airpod", "beats", "headset", "earbud"))
    
    def _find_device_id_by_name(self, device_name: str, device_type: Literal["input", "output"]) -> Optional[int]:
        """
        Находит PortAudio ID устройства по имени
        
        Args:
            device_name: Имя устройства
            device_type: Тип устройства (input/output)
        
        Returns:
            PortAudio ID устройства или None если не найдено
        """
        try:
            import sounddevice as sd
            all_devices = sd.query_devices()
            
            if device_type == "output":
                filtered_devices = [
                    d for d in all_devices
                    if isinstance(d, dict) and d.get('max_output_channels', 0) > 0
                ]
            else:
                filtered_devices = [
                    d for d in all_devices
                    if isinstance(d, dict) and d.get('max_input_channels', 0) > 0
                ]
            
            for device in filtered_devices:
                if device.get('name') == device_name:
                    return device.get('index')
            
            return None
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка поиска ID устройства '{device_name}': {e}")
            return None

