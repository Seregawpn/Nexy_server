"""
Утилиты для работы с качеством изображений
"""

from .types import ScreenshotQuality

# Маппинг качества WebP (0-100)
WEBP_QUALITY_MAP: dict[str, int] = {"low": 50, "medium": 80, "high": 85, "maximum": 95}

# Маппинг качества JPEG (0.0-1.0 для NSBitmapImageRep)
JPEG_QUALITY_MAP: dict[str, float] = {"low": 0.5, "medium": 0.75, "high": 0.85, "maximum": 0.95}


def get_webp_quality(config_quality: ScreenshotQuality, default: int = 80) -> int:
    """Получает качество WebP (0-100) из конфигурации"""
    quality_str = (
        str(config_quality.value) if hasattr(config_quality, "value") else str(config_quality)
    )
    return WEBP_QUALITY_MAP.get(quality_str.lower(), default)


def get_jpeg_quality(config_quality: ScreenshotQuality, default: float = 0.75) -> float:
    """Получает качество JPEG (0.0-1.0) из конфигурации"""
    quality_str = (
        str(config_quality.value) if hasattr(config_quality, "value") else str(config_quality)
    )
    return JPEG_QUALITY_MAP.get(quality_str.lower(), default)
