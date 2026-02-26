"""
Адаптер для SessionManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union, Optional

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.session_management.core.session_manager import SessionManager

logger = logging.getLogger(__name__)


class SessionManagementAdapter(UniversalModuleInterface):
    """
    Адаптер для SessionManager
    
    Временный адаптер для использования существующего SessionManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="session_management")
        self._manager: Optional[SessionManager] = None
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
            self._manager = SessionManager(config)
            
            # Инициализируем менеджер
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать SessionManager")
                
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
            request: Запрос на работу с сессиями
                - action: str - действие (create_session, get_session, update_session)
                - hardware_id: str - идентификатор устройства
                - session_id: str (опционально) - идентификатор сессии
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            action = request.get("action", "create_session")
            hardware_id = request.get("hardware_id")
            
            result = {}
            
            if self._manager is None:
                raise Exception("SessionManager not initialized")
            
            if action == "create_session":
                if not hardware_id:
                    raise ValueError("hardware_id не указан")
                # Создаем сессию (передаем hardware_id через context, так как create_session не принимает его напрямую)
                user_agent = request.get("user_agent")
                ip_address = request.get("ip_address")
                context = request.get("context", {})
                if hardware_id:
                    context["hardware_id"] = hardware_id
                session_data = await self._manager.create_session(user_agent, ip_address, context)
                result = {"session_id": session_data.get("session_id"), "success": True}
            elif action == "get_session":
                session_id = request.get("session_id")
                if not session_id:
                    raise ValueError("session_id не указан")
                # Получаем статус сессии
                session = await self._manager.get_session_status(session_id)
                result = {"session": session, "success": True}
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
    
    def get_manager(self) -> Optional[SessionManager]:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр SessionManager или None
        """
        return self._manager

