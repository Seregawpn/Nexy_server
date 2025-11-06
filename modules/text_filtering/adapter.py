"""
Адаптер для TextFilterManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.text_filtering.core.text_filter_manager import TextFilterManager

logger = logging.getLogger(__name__)


class TextFilteringAdapter(UniversalModuleInterface):
    """
    Адаптер для TextFilterManager
    
    Временный адаптер для использования существующего TextFilterManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    
    Примечание: TextFilterManager уже наследует UniversalModuleInterface,
    но использует старый интерфейс. Этот адаптер оборачивает его для
    использования через новый ModuleCoordinator.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="text_filtering")
        self._manager: TextFilterManager = None
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
            from modules.text_filtering.config import TextFilteringConfig
            filter_config = TextFilteringConfig()
            self._manager = TextFilterManager(filter_config)
            
            # Инициализируем менеджер (используем старый метод)
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать TextFilterManager")
                
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
            request: Запрос на фильтрацию текста
                - text: str - текст для фильтрации
                - action: str (опционально) - действие (filter, clean, validate)
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            text = request.get("text", "")
            action = request.get("action", "filter")
            
            if not text:
                raise ValueError("Текст для фильтрации не указан")
            
            result = {}
            
            if action == "filter":
                # Фильтруем текст
                filtered_text = await self._manager.filter_text(text)
                result = {"filtered_text": filtered_text, "success": True}
            elif action == "clean":
                # Очищаем текст
                cleaned_text = await self._manager.clean_text(text)
                result = {"cleaned_text": cleaned_text, "success": True}
            elif action == "validate":
                # Валидируем текст
                is_valid = await self._manager.validate_text(text)
                result = {"is_valid": is_valid, "success": True}
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
    
    def get_manager(self) -> TextFilterManager:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр TextFilterManager
        """
        return self._manager

