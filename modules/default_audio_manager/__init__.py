"""
Модуль управления аудио через системные дефолты macOS

Этот модуль предоставляет:
- Использование системных дефолтов macOS для аудио
- Автоматическое следование настройкам пользователя
- Мониторинг здоровья микрофона
- Простое управление аудио потоками
- Обработку ошибок и переоткрытие потоков
"""

from .core.default_audio_manager import DefaultAudioManager
from .core.types import (
    DefaultAudioConfig, AudioStreamState, HealthStatus,
    StreamError, AudioMetrics
)
from .core.health_checker import HealthChecker

# Версия модуля
__version__ = "1.0.0"

# Экспортируемые классы и функции
__all__ = [
    # Основные классы
    "DefaultAudioManager",
    "HealthChecker",
    
    # Типы данных
    "DefaultAudioConfig",
    "AudioStreamState", 
    "HealthStatus",
    "StreamError",
    "AudioMetrics",
    
    # Версия
    "__version__"
]


def create_default_audio_manager(config: dict = None) -> DefaultAudioManager:
    """
    Создает экземпляр DefaultAudioManager с конфигурацией
    
    Args:
        config: Словарь конфигурации (опционально)
        
    Returns:
        DefaultAudioManager: Экземпляр менеджера аудио
    """
    from .core.types import DefaultAudioConfig
    
    if config:
        manager_config = DefaultAudioConfig(**config)
    else:
        manager_config = DefaultAudioConfig()
    
    return DefaultAudioManager(manager_config)


def create_default_audio_manager_with_config(config: DefaultAudioConfig) -> DefaultAudioManager:
    """
    Создает DefaultAudioManager с готовой конфигурацией
    
    Args:
        config: Конфигурация DefaultAudioConfig
        
    Returns:
        DefaultAudioManager: Экземпляр менеджера аудио
    """
    return DefaultAudioManager(config)
