"""
Speech Recognition - Модуль распознавания речи
"""

from .core.speech_recognizer import SpeechRecognizer
from .core.types import (
    RecognitionConfig, RecognitionResult, RecognitionState, 
    RecognitionEvent, RecognitionEventType, RecognitionEngine, RecognitionMetrics
)
from .config.default_config import (
    DEFAULT_RECOGNITION_CONFIG, HIGH_QUALITY_CONFIG, 
    FAST_CONFIG, get_config, create_custom_config
)
from .utils.audio_utils import (
    normalize_audio, resample_audio, convert_channels,
    detect_silence, trim_silence, get_audio_info
)

__all__ = [
    'SpeechRecognizer',
    'RecognitionConfig',
    'RecognitionResult', 
    'RecognitionState',
    'RecognitionEvent',
    'RecognitionEventType',
    'RecognitionMetrics',
    'DEFAULT_RECOGNITION_CONFIG',
    'HIGH_QUALITY_CONFIG',
    'FAST_CONFIG',
    'get_config',
    'create_custom_config',
    'normalize_audio',
    'resample_audio',
    'convert_channels',
    'detect_silence',
    'trim_silence',
    'get_audio_info'
]

__version__ = "1.0.2"
__author__ = "Nexy Team"
