"""
Адаптер для InterruptManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union, Optional

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.interrupt_handling.core.interrupt_manager import InterruptManager

logger = logging.getLogger(__name__)


class InterruptHandlingAdapter(UniversalModuleInterface):
    """
    Адаптер для InterruptManager
    
    Временный адаптер для использования существующего InterruptManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    
    Примечание: InterruptManager уже наследует UniversalModuleInterface,
    но использует старый интерфейс. Этот адаптер оборачивает его для
    использования через новый ModuleCoordinator.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="interrupt_handling")
        self._manager: Optional[InterruptManager] = None
        self._config: Dict[str, Any] = {}
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
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            logger.info(f"Инициализация адаптера {self.name}...")
            
            self._config = config
            
            # Создаем менеджер
            from modules.interrupt_handling.config import InterruptHandlingConfig
            interrupt_config = InterruptHandlingConfig()
            self._manager = InterruptManager(interrupt_config)
            
            # Инициализируем менеджер (используем старый метод)
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать InterruptManager")
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации адаптера {self.name}: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на обработку прерывания
                - action: str - действие (interrupt_session, check_interrupt, clear_interrupt)
                - session_id: str - идентификатор сессии
                - hardware_id: str (опционально) - идентификатор устройства
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            if self._manager is None:
                raise Exception("InterruptManager not initialized")
            
            action = request.get("action", "check_interrupt")
            session_id = request.get("session_id")
            hardware_id = request.get("hardware_id")
            
            result = {}
            
            if action == "interrupt_session":
                target = hardware_id or session_id
                if not target:
                    raise ValueError("hardware_id или session_id не указан")
                interrupt_result = await self._manager.interrupt_session(target)
                result = {"success": interrupt_result.get("success", False), **interrupt_result}
            elif action in ("check_interrupt", "check_hardware_interrupt"):
                if not hardware_id:
                    raise ValueError("hardware_id не указан")
                is_interrupted = self._manager.should_interrupt(hardware_id)
                result = {"interrupted": is_interrupted, "success": True}
            elif action == "register_module":
                module_name = request.get("module_name")
                module_instance = request.get("module_instance")
                if not module_name or not module_instance:
                    raise ValueError("module_name и module_instance обязательны")
                success = await self._manager.register_module(module_name, module_instance)
                result = {"success": success}
            elif action == "register_callback":
                callback = request.get("callback")
                if callback is None:
                    raise ValueError("callback обязателен для register_callback")
                success = await self._manager.register_callback(callback)
                result = {"success": success}
            elif action == "clear_interrupt":
                if hasattr(self._manager, "_reset_interrupt_flags"):
                    self._manager._reset_interrupt_flags()
                result = {"success": True}
            else:
                raise ValueError(f"Неизвестное действие: {action}")
            
            return result
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка обработки в адаптере {self.name}: {e}")
            raise
        finally:
            # Возвращаем статус в READY после обработки
            if self._status.state == ModuleState.PROCESSING:
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов адаптера
        """
        try:
            logger.info(f"Очистка адаптера {self.name}...")
            
            if self._manager and hasattr(self._manager, 'cleanup'):
                await self._manager.cleanup()
            
            self._manager = None
            self._config = {}
            self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
            
            logger.info(f"✅ Адаптер {self.name} очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки адаптера {self.name}: {e}")
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса адаптера
        
        Returns:
            ModuleStatus с текущим состоянием
        """
        return self._status
    
    def get_manager(self) -> Optional[InterruptManager]:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр InterruptManager или None
        """
        return self._manager
