"""
Конфигурация модуля Audio Generation
Использует централизованную конфигурацию
"""

from typing import Dict, Any, Optional

from config.unified_config import get_config

class AudioGenerationConfig:
    """Конфигурация модуля генерации аудио"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация конфигурации из централизованной системы
        
        Args:
            config: Словарь с конфигурацией (опционально, переопределяет централизованную)
        """
        # Получаем централизованную конфигурацию
        unified_config = get_config()
        self.config = config or {}
        
        # Используем централизованные настройки с возможностью переопределения
        # Edge TTS настройки
        self.edge_tts_voice_name = self.config.get('edge_tts_voice_name', unified_config.audio.edge_tts_voice_name)
        self.edge_tts_rate = self.config.get('edge_tts_rate', unified_config.audio.edge_tts_rate)
        self.edge_tts_volume = self.config.get('edge_tts_volume', unified_config.audio.edge_tts_volume)
        self.edge_tts_pitch = self.config.get('edge_tts_pitch', unified_config.audio.edge_tts_pitch)
        
        # Настройки аудио формата
        self.audio_format = self.config.get('audio_format', unified_config.audio.audio_format)
        self.sample_rate = self.config.get('sample_rate', unified_config.audio.sample_rate)
        self.channels = self.config.get('channels', unified_config.audio.channels)
        self.bits_per_sample = self.config.get('bits_per_sample', unified_config.audio.bits_per_sample)
        
        # Настройки производительности
        self.max_concurrent_requests = self.config.get('max_concurrent_requests', unified_config.text_processing.max_concurrent_requests)
        self.request_timeout = self.config.get('request_timeout', unified_config.text_processing.request_timeout)
        self.connection_timeout = self.config.get('connection_timeout', 30)
        
        # Настройки streaming
        self.streaming_chunk_size = self.config.get('streaming_chunk_size', unified_config.audio.streaming_chunk_size)
        self.streaming_enabled = self.config.get('streaming_enabled', unified_config.audio.streaming_enabled)
        
        # Настройки конвертации
        self.convert_to_pcm = self.config.get('convert_to_pcm', True)
        
        # Настройки логирования
        self.log_level = self.config.get('log_level', unified_config.logging.level)
        self.log_requests = self.config.get('log_requests', unified_config.logging.log_requests)
        self.log_responses = self.config.get('log_responses', unified_config.logging.log_responses)
    
    def get_edge_tts_config(self) -> Dict[str, Any]:
        """
        Получение конфигурации Edge TTS
        
        Returns:
            Словарь с конфигурацией Edge TTS
        """
        return {
            'voice_name': self.edge_tts_voice_name,
            'rate': self.edge_tts_rate,
            'volume': self.edge_tts_volume,
            'pitch': self.edge_tts_pitch,
            'audio_format': self.audio_format,
            'sample_rate': self.sample_rate,
            'channels': self.channels,
            'bits_per_sample': self.bits_per_sample,
            'streaming_chunk_size': self.streaming_chunk_size,
            'timeout': self.request_timeout,
            'connection_timeout': self.connection_timeout,
            'convert_to_pcm': self.convert_to_pcm
        }
    
    def get_streaming_config(self) -> Dict[str, Any]:
        """
        Получение конфигурации streaming
        
        Returns:
            Словарь с конфигурацией streaming
        """
        return {
            'chunk_size': self.streaming_chunk_size,
            'enabled': self.streaming_enabled,
            'sample_rate': self.sample_rate,
            'channels': self.channels,
            'bits_per_sample': self.bits_per_sample
        }
    
    def validate(self) -> bool:
        """
        Валидация конфигурации
        
        Returns:
            True если конфигурация валидна, False иначе
        """
        # Edge TTS не требует ключей, только проверяем параметры
        
        # Проверяем корректность аудио параметров
        if self.sample_rate not in [8000, 16000, 22050, 24000, 44100, 48000]:
            print("❌ sample_rate должен быть одним из: 8000, 16000, 22050, 24000, 44100, 48000")
            return False
            
        if self.channels not in [1, 2]:
            print("❌ channels должен быть 1 (моно) или 2 (стерео)")
            return False
            
        if self.bits_per_sample not in [8, 16, 24, 32]:
            print("❌ bits_per_sample должен быть одним из: 8, 16, 24, 32")
            return False
            
        if self.request_timeout <= 0:
            print("❌ request_timeout должен быть положительным")
            return False
            
        if self.streaming_chunk_size <= 0:
            print("❌ streaming_chunk_size должен быть положительным")
            return False
        
        # Проверяем формат rate/volume/pitch (Edge TTS использует строки типа "+0%", "-20Hz")
        if not isinstance(self.edge_tts_rate, str):
            print("⚠️ edge_tts_rate должен быть строкой (например, '+0%', '-20%')")
        
        if not isinstance(self.edge_tts_volume, str):
            print("⚠️ edge_tts_volume должен быть строкой (например, '+0%', '-20%')")
        
        if not isinstance(self.edge_tts_pitch, str):
            print("⚠️ edge_tts_pitch должен быть строкой (например, '+0Hz', '-20Hz')")
        
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса конфигурации
        
        Returns:
            Словарь со статусом конфигурации
        """
        return {
            'edge_tts_voice_name': self.edge_tts_voice_name,
            'edge_tts_rate': self.edge_tts_rate,
            'edge_tts_volume': self.edge_tts_volume,
            'edge_tts_pitch': self.edge_tts_pitch,
            'audio_format': self.audio_format,
            'sample_rate': self.sample_rate,
            'channels': self.channels,
            'bits_per_sample': self.bits_per_sample,
            'max_concurrent_requests': self.max_concurrent_requests,
            'request_timeout': self.request_timeout,
            'connection_timeout': self.connection_timeout,
            'streaming_chunk_size': self.streaming_chunk_size,
            'streaming_enabled': self.streaming_enabled,
            'convert_to_pcm': self.convert_to_pcm,
            'log_level': self.log_level,
            'log_requests': self.log_requests,
            'log_responses': self.log_responses
        }
    
    def get_voice_options(self) -> Dict[str, list]:
        """
        Получение доступных опций голоса
        
        Returns:
            Словарь с доступными опциями
        """
        return {
            'voice_names': [
                'en-US-AriaNeural',
                'en-US-DavisNeural',
                'en-US-JennyNeural',
                'en-US-GuyNeural',
                'en-US-JaneNeural',
                'en-US-JasonNeural',
                'en-US-NancyNeural',
                'en-US-TonyNeural',
                'en-US-MichelleNeural',
                'en-US-ChristopherNeural',
                'ru-RU-SvetlanaNeural',
                'ru-RU-DmitryNeural',
                'ru-RU-EkaterinaNeural'
            ],
            'rate_options': ['+0%', '-20%', '-50%', '+20%', '+50%'],
            'volume_options': ['+0%', '-20%', '-50%', '+20%', '+50%'],
            'pitch_options': ['+0Hz', '-20Hz', '-50Hz', '+20Hz', '+50Hz'],
            'audio_formats': [
                'pcm',
                'mp3'
            ]
        }
