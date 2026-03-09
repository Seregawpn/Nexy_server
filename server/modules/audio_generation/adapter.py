"""
Адаптер для AudioProcessor - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.audio_generation.core.audio_processor import AudioProcessor

logger = logging.getLogger(__name__)


class AudioGenerationAdapter(UniversalModuleInterface):
    """
    Адаптер для AudioProcessor
    
    Временный адаптер для использования существующего AudioProcessor
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="audio_generation")
        self._processor: AudioProcessor = None
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
            
            # Создаем процессор
            self._processor = AudioProcessor(config)
            
            # Инициализируем процессор
            if await self._processor.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать AudioProcessor")
                
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
            request: Запрос на генерацию аудио
                - text: str - текст для генерации
                - voice: str (опционально) - голос
                - rate: float (опционально) - скорость
        
        Returns:
            Результат обработки (может быть AsyncIterator для streaming)
        
        Raises:
            Exception: Если обработка не удалась
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            text = request.get("text", "")
            if not text:
                raise ValueError("Текст для генерации аудио не указан")
            
            # Используем метод генерации аудио из процессора
            async def stream_audio():
                async for audio_chunk in self._processor.generate_speech_streaming(text):
                    yield {"audio": audio_chunk, "type": "audio_chunk"}
            
            return stream_audio()
                
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
            
            if self._processor and hasattr(self._processor, 'cleanup'):
                await self._processor.cleanup()
            
            self._processor = None
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
    
    def get_processor(self) -> AudioProcessor:
        """
        Получение внутреннего процессора (для совместимости)
        
        Returns:
            Экземпляр AudioProcessor
        """
        return self._processor

