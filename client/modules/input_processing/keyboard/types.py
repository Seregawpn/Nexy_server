"""
Типы данных для обработки клавиатуры
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, Any

class KeyEventType(Enum):
    """Типы событий клавиатуры"""
    PRESS = "press"
    RELEASE = "release"
    HOLD = "hold"
    SHORT_PRESS = "short_press"  # < 0.6s
    LONG_PRESS = "long_press"    # >= 0.6s

class KeyType(Enum):
    """Типы клавиш"""
    SPACE = "space"
    CTRL = "ctrl"
    ALT = "alt"
    SHIFT = "shift"
    ENTER = "enter"
    ESC = "esc"

@dataclass
class KeyEvent:
    """Событие клавиатуры"""
    key: str
    event_type: KeyEventType
    timestamp: float
    duration: Optional[float] = None
    data: Optional[Dict[str, Any]] = None

@dataclass
class KeyboardConfig:
    """Конфигурация клавиатуры - все значения загружаются из unified_config.yaml"""
    key_to_monitor: str
    short_press_threshold: float
    long_press_threshold: float
    event_cooldown: float
    hold_check_interval: float
    debounce_time: float
    combo_timeout_sec: float = 10.0  # Максимальное время активной комбинации (защита от залипания)
    key_state_timeout_sec: float = 5.0  # Максимальное время удержания отдельной клавиши (защита от залипания)
