"""
Адаптер для MemoryManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.memory_management.core.memory_manager import MemoryManager

logger = logging.getLogger(__name__)


class MemoryManagementAdapter(UniversalModuleInterface):
    """
    Адаптер для MemoryManager
    
    Временный адаптер для использования существующего MemoryManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="memory_management")
        self._manager: MemoryManager = None
        self._config: Dict[str, Any] = {}
        self._status = ModuleStatus(state=ModuleState.INIT)
        self._db_manager = None  # Для установки после инициализации database
    
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
            
            # Создаем менеджер (db_manager будет установлен позже)
            self._manager = MemoryManager(db_manager=self._db_manager)
            
            # Инициализируем менеджер
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать MemoryManager")
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации адаптера {self.name}: {e}")
            raise
    
    def set_database_manager(self, db_manager):
        """
        Установка DatabaseManager (для совместимости)
        
        Args:
            db_manager: Экземпляр DatabaseManager
        """
        self._db_manager = db_manager
        if self._manager and hasattr(self._manager, 'set_database_manager'):
            self._manager.set_database_manager(db_manager)
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на работу с памятью
                - action: str - действие (get_memory, update_memory, analyze)
                - session_id: str - идентификатор сессии
                - prompt: str (опционально) - промпт
                - response: str (опционально) - ответ
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            action = request.get("action", "get_memory")
            session_id = request.get("session_id")
            
            if not session_id:
                raise ValueError("session_id не указан")
            
            result = {}
            
            if action == "get_memory":
                # Получаем память для сессии
                memory = await self._manager.get_memory_context(session_id)
                result = {"memory": memory}
            elif action == "update_memory":
                # Обновляем память
                prompt = request.get("prompt", "")
                response = request.get("response", "")
                await self._manager.update_memory(session_id, prompt, response)
                result = {"success": True}
            elif action == "analyze":
                # Анализируем память
                prompt = request.get("prompt", "")
                response = request.get("response", "")
                analysis = await self._manager.analyze_memory(prompt, response)
                result = {"analysis": analysis}
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
    
    def get_manager(self) -> MemoryManager:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр MemoryManager
        """
        return self._manager

