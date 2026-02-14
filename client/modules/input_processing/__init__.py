"""
Input Processing - Модуль обработки ввода
Объединяет обработку клавиатуры и речи
"""

# from .speech.speech_recognizer import SpeechRecognizer  # Временно отключено
# from .speech.types import SpeechEvent, SpeechEventType, SpeechState, SpeechConfig  # Временно отключено
from .config.input_config import DEFAULT_INPUT_CONFIG, InputConfig
from .keyboard.keyboard_monitor import KeyboardMonitor
from .keyboard.types import KeyboardConfig, KeyEvent, KeyEventType

__all__ = [
    'KeyboardMonitor',
    'KeyEvent',
    'KeyEventType', 
    'KeyboardConfig',
    # 'SpeechRecognizer',  # Временно отключено
    # 'SpeechEvent',  # Временно отключено
    # 'SpeechEventType',  # Временно отключено
    # 'SpeechState',  # Временно отключено
    # 'SpeechConfig',  # Временно отключено
    'InputConfig',
    'DEFAULT_INPUT_CONFIG'
]

__version__ = "1.6.1.36"
__author__ = "Nexy Team"
