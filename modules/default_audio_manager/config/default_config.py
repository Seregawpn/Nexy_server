"""
Конфигурация по умолчанию для DefaultAudioManager
"""

from typing import Dict, Any, Optional
from ..core.types import DefaultAudioConfig

class DefaultAudioConfigLoader:
    """Загрузчик конфигурации для DefaultAudioManager"""
    
    @staticmethod
    def load_from_unified_config(unified_config: Dict[str, Any]) -> DefaultAudioConfig:
        """
        Загрузка конфигурации из unified_config.yaml
        
        Args:
            unified_config: Словарь конфигурации
            
        Returns:
            DefaultAudioConfig: Конфигурация для DefaultAudioManager
        """
        # Получаем секцию default_audio
        default_audio_config = unified_config.get('default_audio', {})
        
        # Создаем конфигурацию с значениями по умолчанию
        config = DefaultAudioConfig()
        
        # Обновляем параметры из конфигурации
        if 'input_sample_rate' in default_audio_config:
            config.input_sample_rate = default_audio_config['input_sample_rate']
        
        if 'output_sample_rate' in default_audio_config:
            config.output_sample_rate = default_audio_config['output_sample_rate']
        
        if 'input_channels' in default_audio_config:
            config.input_channels = default_audio_config['input_channels']
        
        if 'output_channels' in default_audio_config:
            config.output_channels = default_audio_config['output_channels']
        
        if 'dtype' in default_audio_config:
            config.dtype = default_audio_config['dtype']
        
        if 'chunk_size' in default_audio_config:
            config.chunk_size = default_audio_config['chunk_size']
        
        # Health check параметры
        if 'health_check_interval' in default_audio_config:
            config.health_check_interval = default_audio_config['health_check_interval']
        
        if 'health_check_duration' in default_audio_config:
            config.health_check_duration = default_audio_config['health_check_duration']
        
        if 'rms_threshold' in default_audio_config:
            config.rms_threshold = default_audio_config['rms_threshold']
        
        if 'silent_threshold' in default_audio_config:
            config.silent_threshold = default_audio_config['silent_threshold']
        
        # Обработка ошибок
        if 'auto_reopen_on_error' in default_audio_config:
            config.auto_reopen_on_error = default_audio_config['auto_reopen_on_error']
        
        if 'max_retry_attempts' in default_audio_config:
            config.max_retry_attempts = default_audio_config['max_retry_attempts']
        
        if 'retry_delay' in default_audio_config:
            config.retry_delay = default_audio_config['retry_delay']
        
        if 'error_cooldown' in default_audio_config:
            config.error_cooldown = default_audio_config['error_cooldown']
        
        # Логирование
        if 'enable_debug_logging' in default_audio_config:
            config.enable_debug_logging = default_audio_config['enable_debug_logging']
        
        if 'log_health_checks' in default_audio_config:
            config.log_health_checks = default_audio_config['log_health_checks']
        
        if 'log_stream_events' in default_audio_config:
            config.log_stream_events = default_audio_config['log_stream_events']
        
        return config
    
    @staticmethod
    def create_default_config() -> DefaultAudioConfig:
        """
        Создание конфигурации по умолчанию
        
        Returns:
            DefaultAudioConfig: Конфигурация по умолчанию
        """
        return DefaultAudioConfig()
    
    @staticmethod
    def create_optimized_config() -> DefaultAudioConfig:
        """
        Создание оптимизированной конфигурации для production
        
        Returns:
            DefaultAudioConfig: Оптимизированная конфигурация
        """
        config = DefaultAudioConfig()
        
        # Оптимизированные параметры
        config.health_check_interval = 2.0  # Реже проверяем
        config.health_check_duration = 0.2  # Быстрее проверяем
        config.auto_reopen_on_error = True
        config.max_retry_attempts = 2
        config.retry_delay = 1.0
        config.error_cooldown = 5.0
        
        # Меньше логирования
        config.enable_debug_logging = False
        config.log_health_checks = False
        config.log_stream_events = True
        
        return config
    
    @staticmethod
    def create_debug_config() -> DefaultAudioConfig:
        """
        Создание конфигурации для отладки
        
        Returns:
            DefaultAudioConfig: Отладочная конфигурация
        """
        config = DefaultAudioConfig()
        
        # Отладочные параметры
        config.health_check_interval = 0.5  # Чаще проверяем
        config.health_check_duration = 0.5  # Дольше проверяем
        config.auto_reopen_on_error = True
        config.max_retry_attempts = 5
        config.retry_delay = 0.2
        config.error_cooldown = 1.0
        
        # Больше логирования
        config.enable_debug_logging = True
        config.log_health_checks = True
        config.log_stream_events = True
        
        return config
