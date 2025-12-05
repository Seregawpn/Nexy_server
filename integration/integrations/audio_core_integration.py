"""
AudioCoreIntegration - Интеграция новой аудиосистемы с EventBus

Согласно AUDIO_SYSTEM_ARCHITECTURE_IMPL.md:
- Инициализирует CoreAudioDeviceBus, DeviceStateCache, CoreAudioDeviceManager
- Запускает мониторинг устройств (INPUT и OUTPUT)
- Настраивает DevicePollingWatcher как fallback
- Предоставляет InputStreamManager и OutputStreamManager для использования другими интеграциями
"""

import logging
from typing import Optional
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler, ErrorSeverity, ErrorCategory

logger = logging.getLogger(__name__)

# Импорт компонентов новой аудиосистемы
try:
    from modules.audio_core import (
        CoreAudioDeviceBus,
        DeviceStateCache,
        CoreAudioDeviceManager,
        InputStreamManager,
        OutputStreamManager,
        DevicePollingWatcher
    )
    AUDIO_CORE_AVAILABLE = True
except ImportError as e:
    AUDIO_CORE_AVAILABLE = False
    logger.warning(f"⚠️ AudioCore модуль недоступен: {e}")


class AudioCoreIntegration:
    """
    Интеграция новой аудиосистемы
    
    Ответственность:
    - Инициализация и запуск мониторинга устройств
    - Предоставление InputStreamManager и OutputStreamManager
    - Координация работы CoreAudioDeviceManager и DevicePollingWatcher
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        """
        Инициализация интеграции
        
        Args:
            event_bus: Шина событий
            state_manager: Менеджер состояний
            error_handler: Обработчик ошибок
        """
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        
        # Компоненты аудиосистемы
        self._bus: Optional[CoreAudioDeviceBus] = None
        self._cache: Optional[DeviceStateCache] = None
        self._manager: Optional[CoreAudioDeviceManager] = None
        self._polling_watcher: Optional[DevicePollingWatcher] = None
        self._input_stream_manager: Optional[InputStreamManager] = None
        self._output_stream_manager: Optional[OutputStreamManager] = None
        
        self._initialized = False
        self._running = False
        
        logger.info("🔧 AudioCoreIntegration создан")
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            if not AUDIO_CORE_AVAILABLE:
                logger.warning("⚠️ AudioCore модуль недоступен, интеграция отключена")
                return False
            
            # Создаём компоненты
            self._bus = CoreAudioDeviceBus()
            self._cache = DeviceStateCache()
            logger.info(f"✅ [AUDIO_CORE] DeviceStateCache создан: id={id(self._cache)}")
            self._manager = CoreAudioDeviceManager(
                bus=self._bus,
                cache=self._cache,
                event_bus=self.event_bus
            )
            # ✅ УМЕНЬШЕН ИНТЕРВАЛ: 5.0 → 2.0 сек для быстрого обнаружения AirPods
            self._polling_watcher = DevicePollingWatcher(
                bus=self._bus,
                cache=self._cache,
                manager=self._manager,
                poll_interval=2.0  # Быстрее обнаружение подключения устройств
            )
            logger.info("✅ DevicePollingWatcher создан с интервалом 2.0 сек")
            # Передаём кэш в stream managers для доступа к устройствам
            self._input_stream_manager = InputStreamManager(device_cache=self._cache)
            self._output_stream_manager = OutputStreamManager(device_cache=self._cache)
            
            # Устанавливаем polling watcher в manager
            self._manager.set_polling_watcher(self._polling_watcher)
            
            self._initialized = True
            logger.info("✅ AudioCoreIntegration инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации AudioCoreIntegration: {e}", exc_info=True)
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.INITIALIZATION,
                message=f"Ошибка инициализации AudioCoreIntegration: {e}",
                context={"where": "audio_core_integration.initialize"}
            )
            return False
    
    async def start(self) -> bool:
        """Запуск мониторинга устройств"""
        try:
            if not self._initialized or not self._manager:
                logger.warning("⚠️ AudioCoreIntegration не инициализирован")
                return False
            
            # Убеждаемся, что polling watcher установлен (на случай, если не был установлен в initialize)
            if self._polling_watcher and not self._manager._polling_watcher:
                self._manager.set_polling_watcher(self._polling_watcher)
            
            # Запускаем мониторинг INPUT и OUTPUT устройств
            # start_monitoring всегда возвращает True (использует polling fallback если CoreAudio недоступен)
            success = self._manager.start_monitoring(
                monitor_input=True,
                monitor_output=True
            )
            
            if success:
                self._running = True
                if self.is_core_audio_available():
                    logger.info("✅ AudioCoreIntegration запущен (CoreAudio нотификации активны)")
                else:
                    logger.info("✅ AudioCoreIntegration запущен (polling fallback активен)")
            else:
                logger.warning("⚠️ Не удалось запустить мониторинг устройств")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска AudioCoreIntegration: {e}", exc_info=True)
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка запуска AudioCoreIntegration: {e}",
                context={"where": "audio_core_integration.start"}
            )
            return False
    
    async def stop(self) -> bool:
        """Остановка мониторинга устройств"""
        try:
            if not self._running:
                return True
            
            if self._manager:
                self._manager.stop_monitoring()
            
            if self._polling_watcher:
                self._polling_watcher.stop()
            
            if self._input_stream_manager:
                self._input_stream_manager.close()
            
            if self._output_stream_manager:
                self._output_stream_manager.close()
            
            if self._bus:
                self._bus.cleanup()
            
            self._running = False
            logger.info("✅ AudioCoreIntegration остановлен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки AudioCoreIntegration: {e}", exc_info=True)
            return False
    
    def get_input_stream_manager(self) -> Optional[InputStreamManager]:
        """Получает InputStreamManager для использования другими интеграциями"""
        return self._input_stream_manager
    
    def get_output_stream_manager(self) -> Optional[OutputStreamManager]:
        """Получает OutputStreamManager для использования другими интеграциями"""
        return self._output_stream_manager
    
    def get_device_cache(self) -> Optional[DeviceStateCache]:
        """Получает DeviceStateCache для использования другими интеграциями"""
        return self._cache
    
    def is_core_audio_available(self) -> bool:
        """Проверяет, доступны ли Core Audio нотификации"""
        if self._bus:
            return self._bus.is_available()
        return False

