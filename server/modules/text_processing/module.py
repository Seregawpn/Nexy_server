"""
TextProcessingModule - модуль обработки текста, реализующий UniversalModuleInterface
Пример приведения модуля к стандарту PR-2
"""

import logging
from typing import Dict, Any, AsyncIterator, Union

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.text_processing.core.text_processor import TextProcessor
from modules.text_processing.config import TextProcessingConfig

logger = logging.getLogger(__name__)


class TextProcessingModule(UniversalModuleInterface):
    """
    Модуль обработки текста
    
    Реализует UniversalModuleInterface для единообразного взаимодействия
    через координатор модулей.
    
    Использует существующий TextProcessor внутри, но предоставляет
    стандартизированный интерфейс.
    """
    
    def __init__(self):
        """Инициализация модуля"""
        super().__init__(name="text_processing")
        self._processor: TextProcessor = None
        self._config: TextProcessingConfig = None
        self._status = ModuleStatus(state=ModuleState.INIT)
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация модуля
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        try:
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            logger.info(f"Инициализация модуля {self.name}...")
            
            # Создаем конфигурацию из unified_config
            self._config = TextProcessingConfig(config)
            
            # Создаем процессор
            self._processor = TextProcessor(config)
            
            # Инициализируем процессор
            if await self._processor.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Модуль {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать TextProcessor")
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации модуля {self.name}: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на обработку текста
                - text: str - текст для обработки
                - image_data: bytes (опционально) - изображение в формате JPEG
                - use_search: bool (опционально) - использовать Google Search
        
        Returns:
            Результат обработки (может быть AsyncIterator для streaming)
        
        Raises:
            Exception: Если обработка не удалась
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            text = request.get("text", "")
            image_data = request.get("image_data")
            use_search = request.get("use_search", False)
            
            if not text:
                raise ValueError("Текст для обработки не указан")
            
            # Если есть изображение, используем метод с изображением
            if image_data:
                async def stream_with_image():
                    async for chunk in self._processor.process_text_streaming(
                        text, image_data
                    ):
                        yield {"text": chunk, "type": "text_chunk"}
                return stream_with_image()
            else:
                # Обычная обработка текста
                async def stream_text():
                    async for chunk in self._processor.process_text_streaming(text):
                        yield {"text": chunk, "type": "text_chunk"}
                return stream_text()
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка обработки в модуле {self.name}: {e}")
            raise
        finally:
            # Возвращаем статус в READY после обработки
            if self._status.state == ModuleState.PROCESSING:
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов модуля
        
        Вызывается при остановке сервера или перезагрузке модуля.
        """
        try:
            logger.info(f"Очистка модуля {self.name}...")
            
            if self._processor:
                await self._processor.cleanup()
            
            self._processor = None
            self._config = None
            self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
            
            logger.info(f"✅ Модуль {self.name} очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки модуля {self.name}: {e}")
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса модуля
        
        Returns:
            ModuleStatus с текущим состоянием модуля
        """
        return self._status
    
    def get_processor(self) -> TextProcessor:
        """
        Получение внутреннего процессора (для совместимости)
        
        Returns:
            Экземпляр TextProcessor
        """
        return self._processor

