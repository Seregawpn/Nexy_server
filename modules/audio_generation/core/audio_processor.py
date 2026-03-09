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
from modules.audio_generation.core.audio_processor_bridge import (
    apply_voice_settings_to_config,
    apply_voice_settings_to_provider,
    build_audio_info_from_config,
    build_not_ready_reason,
    build_processor_metrics,
    build_processor_status,
    build_processor_summary,
    build_provider_name,
    is_processor_ready,
)
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
            if not is_processor_ready(self.is_initialized, self.provider):
                raise Exception(build_not_ready_reason(self.is_initialized, self.provider))
            
            logger.debug(f"Generating speech for text: {text[:100]}...")
            
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
            if not is_processor_ready(self.is_initialized, self.provider):
                raise Exception(build_not_ready_reason(self.is_initialized, self.provider))
            
            logger.debug(f"Streaming speech generation for text: {text[:100]}...")
            
            # Получаем streaming конфигурацию
            streaming_config = self.config.get_streaming_config()
            
            if not streaming_config['enabled']:
                logger.warning("Streaming is disabled, falling back to regular generation")
                async for chunk in self.generate_speech(text):
                    yield chunk
                return
            
            # Потоковая генерация через провайдер
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
        return build_processor_status(
            is_initialized=self.is_initialized,
            config_status=self.config.get_status(),
            provider=self.provider,
        )
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Получение метрик процессора
        
        Returns:
            Словарь с метриками процессора
        """
        return build_processor_metrics(
            is_initialized=self.is_initialized,
            provider=self.provider,
        )
    
    def get_audio_info(self) -> Dict[str, Any]:
        """
        Получение информации об аудио формате
        
        Returns:
            Словарь с информацией об аудио
        """
        if self.provider:
            return self.provider.get_audio_info()
        return build_audio_info_from_config(self.config)
    
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
            if not is_processor_ready(self.is_initialized, self.provider):
                logger.warning("Cannot update voice settings - processor not initialized")
                return False
            
            apply_voice_settings_to_config(self.config, voice_settings)
            apply_voice_settings_to_provider(self.provider, self.config)
            
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
        return build_processor_summary(
            is_initialized=self.is_initialized,
            provider=self.provider,
            config_valid=self.config.validate(),
            audio_info=self.get_audio_info(),
        )
    
    def __str__(self) -> str:
        """Строковое представление процессора"""
        return (
            f"AudioProcessor("
            f"initialized={self.is_initialized}, "
            f"provider={build_provider_name(self.provider)}"
            f")"
        )
    
    def __repr__(self) -> str:
        """Представление процессора для отладки"""
        return (
            f"AudioProcessor("
            f"initialized={self.is_initialized}, "
            f"provider={build_provider_name(self.provider)}, "
            f"available={self.provider.is_available if self.provider else False}"
            f")"
        )
