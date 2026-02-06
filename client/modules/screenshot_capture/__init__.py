"""
Модуль захвата скриншотов для macOS
"""

from .core.config import get_screenshot_config
from .core.screenshot_capture import ScreenshotCapture
from .core.types import (
    ScreenInfo,
    ScreenshotCaptureError,
    ScreenshotConfig,
    ScreenshotData,
    ScreenshotError,
    ScreenshotFormat,
    ScreenshotFormatError,
    ScreenshotPermissionError,
    ScreenshotQuality,
    ScreenshotRegion,
    ScreenshotResult,
    ScreenshotTimeoutError,
)

__all__ = [
    # Основные классы
    'ScreenshotCapture',
    # глобальные синглтоны удалены
    
    # Типы данных
    'ScreenshotConfig',
    'ScreenshotData',
    'ScreenshotResult',
    'ScreenshotFormat',
    'ScreenshotQuality',
    'ScreenshotRegion',
    'ScreenInfo',
    
    # Исключения
    'ScreenshotError',
    'ScreenshotPermissionError',
    'ScreenshotCaptureError',
    'ScreenshotFormatError',
    'ScreenshotTimeoutError',
    
    # Конфигурация
    'get_screenshot_config'
]

# Версия модуля
__version__ = "1.6.1.16"
__author__ = "Nexy Development Team"
__description__ = "Модуль захвата скриншотов для macOS с поддержкой JPEG"
