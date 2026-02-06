"""
Конфигурация для распознавания речи

ВАЖНО: Аудио параметры загружаются из централизованной конфигурации.
Используйте get_config() для получения актуальной конфигурации.
"""

from typing import Any

from config.unified_config_loader import unified_config

from ..core.types import RecognitionConfig


def _get_base_config() -> dict[str, Any]:
    """Получить базовые параметры из централизованной конфигурации"""
    try:
        raw_config = unified_config.get_stt_config()
    except Exception:
        raw_config = {}
        
    return {
        'sample_rate': raw_config.get('sample_rate') or raw_config.get('target_sample_rate') or 16000,
        'channels': raw_config.get('channels') or raw_config.get('target_channels') or 1,
        'chunk_size': raw_config.get('chunk_size') or 2048,
        'language': raw_config.get('language') or "en-US",
    }

def _create_default_config(base: dict[str, Any]) -> RecognitionConfig:
    return RecognitionConfig(
        language=base['language'],
        sample_rate=base['sample_rate'],
        chunk_size=base['chunk_size'],
        channels=base['channels'],
        dtype='int16',
        
        energy_threshold=100,
        dynamic_energy_threshold=True,
        pause_threshold=0.5,
        phrase_threshold=0.3,
        non_speaking_duration=0.3,
        max_duration=30.0,
        
        timeout=5.0,
        phrase_timeout=0.3,
        max_alternatives=1,
        show_all=False,
        
        enable_logging=True,
        enable_metrics=True,
        auto_start=True,
        enable_audio_recovery=False
    )

def _create_high_quality_config(base: dict[str, Any]) -> RecognitionConfig:
    return RecognitionConfig(
        language=base['language'],
        sample_rate=base['sample_rate'],
        chunk_size=max(2048, base['chunk_size']),
        channels=base['channels'],
        dtype='int16',
        
        energy_threshold=50,
        dynamic_energy_threshold=True,
        pause_threshold=0.8,
        phrase_threshold=0.5,
        non_speaking_duration=0.5,
        max_duration=60.0,
        
        timeout=10.0,
        phrase_timeout=0.5,
        max_alternatives=3,
        show_all=True,
        
        enable_logging=True,
        enable_metrics=True,
        auto_start=True,
        enable_audio_recovery=False
    )

def _create_fast_config(base: dict[str, Any]) -> RecognitionConfig:
    return RecognitionConfig(
        language=base['language'],
        sample_rate=base['sample_rate'],
        chunk_size=max(1024, base['chunk_size'] // 2),
        channels=base['channels'],
        dtype='int16',
        
        energy_threshold=200,
        dynamic_energy_threshold=False,
        pause_threshold=0.3,
        phrase_threshold=0.2,
        non_speaking_duration=0.2,
        max_duration=15.0,
        
        timeout=3.0,
        phrase_timeout=0.2,
        max_alternatives=1,
        show_all=False,
        
        enable_logging=True,
        enable_metrics=True,
        auto_start=True,
        enable_audio_recovery=False
    )

def get_config(preset: str = "default") -> RecognitionConfig:
    """Возвращает актуальную конфигурацию по имени пресета"""
    base = _get_base_config()
    
    if preset == "high_quality":
        return _create_high_quality_config(base)
    elif preset == "fast":
        return _create_fast_config(base)
    else:
        return _create_default_config(base)

def create_custom_config(**kwargs) -> RecognitionConfig:
    """Создает пользовательскую конфигурацию"""
    return RecognitionConfig(**kwargs)

# For backward compatibility / static access if absolutely needed (DEPRECATED)
DEFAULT_RECOGNITION_CONFIG = get_config("default")
