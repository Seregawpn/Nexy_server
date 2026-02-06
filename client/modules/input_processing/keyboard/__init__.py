"""
Keyboard module - обработка клавиатуры
"""

from .keyboard_monitor import KeyboardMonitor
from .types import KeyboardConfig, KeyEvent, KeyEventType, KeyType

__all__ = [
    'KeyboardMonitor',
    'KeyEvent',
    'KeyEventType',
    'KeyType',
    'KeyboardConfig'
]
