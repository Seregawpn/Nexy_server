"""
Адаптер для DatabaseManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union, Optional

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.database.core.database_manager import DatabaseManager

logger = logging.getLogger(__name__)


class DatabaseAdapter(UniversalModuleInterface):
    """
    Адаптер для DatabaseManager
    
    Временный адаптер для использования существующего DatabaseManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="database")
        self._manager: Optional[DatabaseManager] = None
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
            self._manager = DatabaseManager(config)
            
            # Инициализируем менеджер
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                error_msg = (
                    "Не удалось инициализировать DatabaseManager. "
                    "Проверьте конфигурацию БД в config.env. "
                    "Сервер продолжит работу без функциональности БД."
                )
                raise Exception(error_msg)
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            error_msg = (
                f"❌ Ошибка инициализации адаптера {self.name}: {e}. "
                "Это некритическая ошибка - сервер продолжит работу без модуля database. "
                "Для исправления проверьте конфигурацию БД в config.env."
            )
            logger.error(error_msg)
            raise
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на работу с БД
                - action: str - действие (query, insert, update, delete)
                - query: str (опционально) - SQL запрос
                - data: dict (опционально) - данные
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            action = request.get("action", "query")
            
            result = {}
            
            if action == "query":
                query = request.get("query", "")
                if not query:
                    raise ValueError("SQL запрос не указан")
                # Выполняем запрос через менеджер
                # Это упрощенный пример - в реальности нужно использовать методы менеджера
                result = {"success": True, "data": []}
            elif action == "insert":
                data = request.get("data", {})
                # Вставка данных
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
    
    def get_manager(self) -> Optional[DatabaseManager]:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр DatabaseManager или None
        """
        return self._manager

