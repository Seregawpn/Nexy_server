"""
DeviceChangePublisherIntegration - Интеграция DeviceChangePublisher с EventBus

✅ ЦИКЛ 1: Интеграция единого монитора устройств в систему
"""

import logging
from typing import Optional

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

logger = logging.getLogger(__name__)

# Попытка импорта DeviceChangePublisher
try:
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    from modules.audio_core.device_change_publisher import DeviceChangePublisher
    DEVICE_CHANGE_PUBLISHER_AVAILABLE = True
except ImportError as e:
    DEVICE_CHANGE_PUBLISHER_AVAILABLE = False
    DeviceChangePublisher = None
    logger.warning(f"⚠️ DeviceChangePublisher недоступен: {e}")


class DeviceChangePublisherIntegration:
    """
    Интеграция DeviceChangePublisher с EventBus
    
    Ответственность:
    - Инициализация и запуск DeviceChangePublisher
    - Координация мониторинга INPUT/OUTPUT устройств
    - Публикация событий device.default_*_changed в EventBus
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        
        self._publisher: Optional[DeviceChangePublisher] = None
        self._initialized = False
        self._running = False
        
        logger.info("🔧 DeviceChangePublisherIntegration создан")
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            if not DEVICE_CHANGE_PUBLISHER_AVAILABLE:
                logger.warning("⚠️ DeviceChangePublisher недоступен, интеграция отключена")
                return False
            
            self._publisher = DeviceChangePublisher(self.event_bus)
            self._initialized = True
            
            logger.info("✅ DeviceChangePublisherIntegration инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации DeviceChangePublisherIntegration: {e}", exc_info=True)
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.INITIALIZATION,
                message=f"Ошибка инициализации DeviceChangePublisherIntegration: {e}",
                context={"where": "device_change_publisher_integration.initialize"}
            )
            return False
    
    async def start(self) -> bool:
        """Запуск мониторинга устройств"""
        try:
            if not self._initialized or not self._publisher:
                logger.warning("⚠️ DeviceChangePublisherIntegration не инициализирован")
                return False
            
            # Запускаем мониторинг INPUT и OUTPUT устройств
            success = await self._publisher.start_monitoring(
                monitor_input=True,
                monitor_output=True
            )
            
            if success:
                self._running = True
                logger.info("✅ DeviceChangePublisherIntegration запущен (мониторинг INPUT и OUTPUT)")
            else:
                logger.warning("⚠️ Не удалось запустить мониторинг устройств")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска DeviceChangePublisherIntegration: {e}", exc_info=True)
            await self.error_handler.handle_error(
                severity=ErrorSeverity.MEDIUM,
                category=ErrorCategory.RUNTIME,
                message=f"Ошибка запуска DeviceChangePublisherIntegration: {e}",
                context={"where": "device_change_publisher_integration.start"}
            )
            return False
    
    async def stop(self) -> bool:
        """Остановка мониторинга устройств"""
        try:
            if not self._running or not self._publisher:
                return True
            
            await self._publisher.stop_monitoring()
            self._running = False
            
            logger.info("✅ DeviceChangePublisherIntegration остановлен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки DeviceChangePublisherIntegration: {e}", exc_info=True)
            return False
    
    def get_current_input_device(self):
        """Получить текущее INPUT устройство"""
        if self._publisher:
            return self._publisher.get_current_input_device()
        return None
    
    def get_current_output_device(self):
        """Получить текущее OUTPUT устройство"""
        if self._publisher:
            return self._publisher.get_current_output_device()
        return None
    
    def is_core_audio_available(self) -> bool:
        """Проверяет, доступны ли Core Audio нотификации"""
        if self._publisher:
            return self._publisher.is_core_audio_available()
        return False

