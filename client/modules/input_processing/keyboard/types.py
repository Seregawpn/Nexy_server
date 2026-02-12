"""
Типы данных для обработки клавиатуры
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class KeyEventType(Enum):
    """Типы событий клавиатуры"""

    PRESS = "press"
    RELEASE = "release"
    HOLD = "hold"
    SHORT_PRESS = "short_press"  # < 0.6s
    LONG_PRESS = "long_press"  # >= 0.6s


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
    duration: float | None = None
    data: dict[str, Any] | None = None


@dataclass
class KeyboardConfig:
    """Конфигурация клавиатуры - все значения загружаются из unified_config.yaml"""

    key_to_monitor: str
    short_press_threshold: float
    long_press_threshold: float
    event_cooldown: float
    hold_check_interval: float
    debounce_time: float
    combo_timeout_sec: float = (
        120.0  # Максимальное время активной комбинации (2 мин для длинных записей)
    )
    key_state_timeout_sec: float = 60.0  # Максимальное время удержания отдельной клавиши (1 мин)
