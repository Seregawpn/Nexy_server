"""
Универсальный интерфейс для взаимодействия модулей
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, AsyncIterator, Union

from .module_status import ModuleStatus, ModuleState

logger = logging.getLogger(__name__)


class UniversalModuleInterface(ABC):
    """
    Универсальный интерфейс для всех модулей
    
    Обеспечивает стандартный способ взаимодействия между модулями
    без знания о конкретной реализации.
    
    Все модули должны реализовывать этот интерфейс для единообразного
    взаимодействия через координатор модулей.
    """
    
    def __init__(self, name: str):
        """
        Инициализация модуля
        
        Args:
            name: Имя модуля
        """
        self.name = name
        self._status = ModuleStatus(state=ModuleState.INIT)
        logger.info(f"Module {self.name} created")
    
    @abstractmethod
    async def initialize(self, config: dict) -> None:
        """
        Инициализация модуля
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        pass
    
    @abstractmethod
    async def process(self, request: Any) -> Union[Any, AsyncIterator[Any]]:
        """
        Основная обработка запроса
        
        Args:
            request: Входной запрос (тип зависит от модуля)
            
        Returns:
            Результат обработки (может быть обычным значением или AsyncIterator для streaming)
            
        Raises:
            Exception: Если обработка не удалась
        """
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """
        Очистка ресурсов модуля
        
        Вызывается при остановке сервера или перезагрузке модуля.
        """
        pass
    
    @abstractmethod
    def status(self) -> ModuleStatus:
        """
        Получение статуса модуля
        
        Returns:
            ModuleStatus с текущим состоянием модуля
        """
        pass
    
    def get_status_dict(self) -> Dict[str, Any]:
        """
        Получение статуса модуля в виде словаря
        
        Returns:
            Словарь со статусом модуля
        """
        status_dict = self.status().to_dict()
        status_dict["name"] = self.name
        return status_dict
    
    def __str__(self) -> str:
        """Строковое представление модуля"""
        return f"Module({self.name}, state={self.status().state.value})"
    
    def __repr__(self) -> str:
        """Представление модуля для отладки"""
        return (
            f"UniversalModuleInterface("
            f"name='{self.name}', "
            f"state='{self.status().state.value}'"
            f")"
        )
