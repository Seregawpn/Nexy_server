"\"\"\"DeviceChangePublisherIntegration - обёртка над DeviceChangePublisher\"\"\""

import logging
from typing import Optional

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from modules.audio_core.device_change_publisher import DeviceChangePublisher
from integration.integrations.audio_core_integration import AudioCoreIntegration

logger = logging.getLogger(__name__)


class DeviceChangePublisherIntegration:
    """Интеграция для DeviceChangePublisher"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        audio_core_integration: Optional[AudioCoreIntegration] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self._publisher = DeviceChangePublisher(
            event_bus=self.event_bus,
            core_integration=audio_core_integration
        )
        self._initialized = False

        logger.info("DeviceChangePublisherIntegration создан")

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        result = await self._publisher.initialize()
        self._initialized = result
        logger.info(f"DeviceChangePublisherIntegration.initialize -> {result}")
        return result

    async def start(self) -> bool:
        """Запуск мониторинга устройств"""
        if not self._initialized:
            logger.warning("⚠️ DeviceChangePublisherIntegration не инициализирована")
            return False
        return await self._publisher.start_monitoring(monitor_input=True, monitor_output=True)

    async def stop(self) -> bool:
        """Остановка мониторинга"""
        return await self._publisher.stop_monitoring()

    def get_current_input_device(self):
        return self._publisher.get_current_input_device()

    def get_current_output_device(self):
        return self._publisher.get_current_output_device()

    def is_core_audio_available(self) -> bool:
        return self._publisher.is_core_audio_available()

