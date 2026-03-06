"""
Основной AudioProcessor - координатор модуля генерации аудио
"""

import sys
import os
from pathlib import Path

# Добавляем путь к корню проекта для корректных импортов
if __name__ == "__main__":
    # Определяем корневую директорию проекта (server/)
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent.parent.parent  # server/
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

import logging
from typing import Dict, Any, Optional, AsyncGenerator
from modules.audio_generation.config import AudioGenerationConfig
from modules.audio_generation.providers.edge_tts_provider import EdgeTTSProvider

logger = logging.getLogger(__name__)

class AudioProcessor:
    """
    Основной процессор аудио
    
    Координирует работу Edge TTS провайдера и обеспечивает
    единый интерфейс для генерации речи из текста.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация процессора аудио
        
        Args:
            config: Конфигурация модуля
        """
        self.config = AudioGenerationConfig(config)
        self.provider = None
        self.is_initialized = False
        
        logger.info("AudioProcessor initialized")
    
    async def initialize(self) -> bool:
        """
        Инициализация процессора аудио
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Initializing AudioProcessor...")
            
            # Валидируем конфигурацию
            if not self.config.validate():
                logger.error("Audio generation configuration validation failed")
                return False
            
            # Создаем провайдер
            await self._create_provider()
            
            # Инициализируем провайдер
            if not self.provider:
                logger.error("Failed to create Edge TTS provider")
                return False
            
            if not await self.provider.initialize():
                logger.error("Failed to initialize Edge TTS provider")
                return False
            
            self.is_initialized = True
            logger.info("AudioProcessor initialized successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize AudioProcessor: {e}")
            return False
    
    async def _create_provider(self):
        """Создание провайдера аудио"""
        try:
            # Edge TTS Provider (единственный провайдер)
            edge_tts_config = self.config.get_edge_tts_config()
            self.provider = EdgeTTSProvider(edge_tts_config)
            
            logger.info("Created Edge TTS provider")
            
        except Exception as e:
            logger.error(f"Error creating provider: {e}")
            raise e
    
    async def generate_speech(self, text: str) -> AsyncGenerator[bytes, None]:
        """
        Генерация речи из текста
        
        Args:
            text: Текст для преобразования в речь
            
        Yields:
            Chunks аудио данных
        """
        try:
            if not self.is_initialized:
                raise Exception("AudioProcessor not initialized")
            
            logger.debug(f"Generating speech for text: {text[:100]}...")
            
            if not self.provider:
                raise Exception("AudioProcessor provider not initialized")
            
            async for audio_chunk in self.provider.process(text):
                yield audio_chunk
                
        except Exception as e:
            logger.error(f"Error generating speech: {e}")
            raise e
    
    async def generate_speech_streaming(self, text: str) -> AsyncGenerator[bytes, None]:
        """
        Потоковая генерация речи из текста
        
        Args:
            text: Текст для преобразования в речь
            
        Yields:
            Chunks аудио данных в реальном времени
        """
        try:
            if not self.is_initialized:
                raise Exception("AudioProcessor not initialized")
            
            logger.debug(f"Streaming speech generation for text: {text[:100]}...")
            
            # Получаем streaming конфигурацию
            streaming_config = self.config.get_streaming_config()
            
            if not streaming_config['enabled']:
                logger.warning("Streaming is disabled, falling back to regular generation")
                async for chunk in self.generate_speech(text):
                    yield chunk
                return
            
            # Потоковая генерация через провайдер
            if not self.provider:
                raise Exception("AudioProcessor provider not initialized")
            
            async for audio_chunk in self.provider.process(text):
                if not audio_chunk:
                    continue
                logger.info(
                    "AudioProcessor → emit sentence audio bytes=%s", len(audio_chunk)
                )
                yield audio_chunk
                
        except Exception as e:
            logger.error(f"Error in streaming speech generation: {e}")
            raise e
    
    async def cleanup(self) -> bool:
        """
        Очистка ресурсов процессора
        
        Returns:
            True если очистка успешна, False иначе
        """
        try:
            logger.info("Cleaning up AudioProcessor...")
            
            # Очищаем провайдер
            if self.provider:
                await self.provider.cleanup()
            
            self.is_initialized = False
            logger.info("AudioProcessor cleaned up successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error cleaning up AudioProcessor: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса процессора
        
        Returns:
            Словарь со статусом процессора
        """
        status = {
            "is_initialized": self.is_initialized,
            "config_status": self.config.get_status(),
            "provider": None
        }
        
        # Добавляем статус провайдера
        if self.provider:
            status["provider"] = self.provider.get_status()
        
        return status
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Получение метрик процессора
        
        Returns:
            Словарь с метриками процессора
        """
        metrics = {
            "is_initialized": self.is_initialized,
            "provider": None
        }
        
        # Добавляем метрики провайдера
        if self.provider:
            metrics["provider"] = self.provider.get_metrics()
        
        return metrics
    
    def get_audio_info(self) -> Dict[str, Any]:
        """
        Получение информации об аудио формате
        
        Returns:
            Словарь с информацией об аудио
        """
        if self.provider:
            return self.provider.get_audio_info()
        else:
            return {
                "format": self.config.audio_format,
                "sample_rate": self.config.sample_rate,
                "channels": self.config.channels,
                "bits_per_sample": self.config.bits_per_sample,
                "voice_name": self.config.edge_tts_voice_name,
                "rate": self.config.edge_tts_rate,
                "pitch": self.config.edge_tts_pitch,
                "volume": self.config.edge_tts_volume
            }
    
    def get_voice_options(self) -> Dict[str, list]:
        """
        Получение доступных опций голоса
        
        Returns:
            Словарь с доступными опциями
        """
        return self.config.get_voice_options()
    
    def update_voice_settings(self, voice_settings: Dict[str, Any]) -> bool:
        """
        Обновление настроек голоса
        
        Args:
            voice_settings: Новые настройки голоса
            
        Returns:
            True если настройки обновлены, False иначе
        """
        try:
            if not self.is_initialized or not self.provider:
                logger.warning("Cannot update voice settings - processor not initialized")
                return False
            
            # Обновляем настройки в конфигурации
            if 'voice_name' in voice_settings:
                self.config.edge_tts_voice_name = voice_settings['voice_name']
            if 'rate' in voice_settings:
                self.config.edge_tts_rate = voice_settings['rate']
            if 'pitch' in voice_settings:
                self.config.edge_tts_pitch = voice_settings['pitch']
            if 'volume' in voice_settings:
                self.config.edge_tts_volume = voice_settings['volume']
            
            # Обновляем настройки в провайдере
            if hasattr(self.provider, 'voice_name'):
                self.provider.voice_name = self.config.edge_tts_voice_name
            if hasattr(self.provider, 'rate'):
                self.provider.rate = self.config.edge_tts_rate
            if hasattr(self.provider, 'pitch'):
                self.provider.pitch = self.config.edge_tts_pitch
            if hasattr(self.provider, 'volume'):
                self.provider.volume = self.config.edge_tts_volume
            
            logger.info(f"Voice settings updated: {voice_settings}")
            return True
            
        except Exception as e:
            logger.error(f"Error updating voice settings: {e}")
            return False
    
    def reset_metrics(self):
        """Сброс метрик процессора"""
        if self.provider:
            self.provider.reset_metrics()
        logger.info("AudioProcessor metrics reset")
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Получение краткой сводки по процессору
        
        Returns:
            Словарь со сводкой
        """
        summary = {
            "is_initialized": self.is_initialized,
            "provider_name": "edge_tts",
            "provider_available": self.provider.is_available if self.provider else False,
            "config_valid": self.config.validate(),
            "audio_info": self.get_audio_info()
        }
        
        return summary
    
    def __str__(self) -> str:
        """Строковое представление процессора"""
        return f"AudioProcessor(initialized={self.is_initialized}, provider={'edge_tts' if self.provider else 'none'})"
    
    def __repr__(self) -> str:
        """Представление процессора для отладки"""
        return (
            f"AudioProcessor("
            f"initialized={self.is_initialized}, "
            f"provider={'edge_tts' if self.provider else 'none'}, "
            f"available={self.provider.is_available if self.provider else False}"
            f")"
        )


# Блок для прямого запуска файла (тестирование)
if __name__ == "__main__":
    import asyncio
    
    async def test_audio_processor():
        """Простой тест AudioProcessor"""
        print("="*60)
        print("ТЕСТИРОВАНИЕ AudioProcessor")
        print("="*60)
        
        # Настройка логирования
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        try:
            # Создаем процессор
            processor = AudioProcessor()
            print("\n1. AudioProcessor создан")
            
            # Инициализируем
            init_result = await processor.initialize()
            if not init_result:
                print("❌ Инициализация не удалась")
                return
            
            print("✅ AudioProcessor инициализирован")
            
            # Проверяем статус
            status = processor.get_status()
            print(f"\n2. Статус:")
            print(f"   Инициализирован: {status.get('is_initialized', False)}")
            print(f"   Провайдер: {status.get('provider_name', 'N/A')}")
            print(f"   Провайдер доступен: {status.get('provider_available', False)}")
            
            # Тест генерации аудио
            test_text = "Hello, this is a test of AudioProcessor."
            print(f"\n3. Генерация аудио для текста: '{test_text}'")
            
            chunks = []
            total_bytes = 0
            async for chunk in processor.generate_speech_streaming(test_text):
                chunks.append(chunk)
                total_bytes += len(chunk)
            
            print(f"✅ Аудио сгенерировано:")
            print(f"   Чанков: {len(chunks)}")
            print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
            
            # Информация об аудио
            audio_info = processor.get_audio_info()
            print(f"\n4. Информация об аудио:")
            print(f"   Формат: {audio_info.get('format', 'N/A')}")
            print(f"   Sample rate: {audio_info.get('sample_rate', 'N/A')} Hz")
            print(f"   Channels: {audio_info.get('channels', 'N/A')}")
            print(f"   Bits per sample: {audio_info.get('bits_per_sample', 'N/A')}")
            print(f"   Voice: {audio_info.get('voice_name', 'N/A')}")
            
            # Cleanup
            await processor.cleanup()
            print("\n✅ Тест завершен успешно!")
            
        except Exception as e:
            print(f"\n❌ Ошибка: {e}")
            import traceback
            traceback.print_exc()
    
    # Запускаем тест
    asyncio.run(test_audio_processor())
