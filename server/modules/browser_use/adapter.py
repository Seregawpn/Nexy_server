"""
Browser Use Module Adapter - адаптер для BrowserUseModule

Feature ID: F-2025-015-browser-use
"""

import logging
from typing import Dict, Any, AsyncIterator

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState
from modules.browser_use.constants import FEATURE_ID
from modules.browser_use.module import BrowserUseModule

logger = logging.getLogger(__name__)


class BrowserUseModuleAdapter(UniversalModuleInterface):
    """
    Адаптер для BrowserUseModule
    
    Обеспечивает интеграцию BrowserUseModule с UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="browser_use")
        self._module = BrowserUseModule()
        self._status = ModuleStatus(state=ModuleState.INIT)
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация адаптера
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        try:
            await self._module.initialize(config)
            self._status = ModuleStatus(state=ModuleState.READY, health="ok")
            logger.info(f"[{FEATURE_ID}] BrowserUseModuleAdapter initialized")
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"[{FEATURE_ID}] Ошибка инициализации: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> AsyncIterator[Dict[str, Any]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на выполнение browser-use задачи
                - args: Dict[str, Any] - аргументы команды (task, config_preset)
                - session_id: str - идентификатор сессии
                - hardware_id: str - идентификатор оборудования
                - feature_id: str - идентификатор фичи
        
        Yields:
            События прогресса browser-use задачи
        """
        async for progress in self._module.process(request):
            yield progress
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов модуля
        
        Вызывается при остановке сервера или перезагрузке модуля.
        """
        await self._module.cleanup()
        self._status = ModuleStatus(state=ModuleState.STOPPED, health="ok")
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса модуля
        
        Returns:
            ModuleStatus с текущим состоянием модуля
        """
        return self._module.status()
    
    def set_interrupt_workflow(self, interrupt_workflow):
        """Установка InterruptWorkflowIntegration"""
        self._module.set_interrupt_workflow(interrupt_workflow)