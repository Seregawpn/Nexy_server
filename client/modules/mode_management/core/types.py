"""
Типы данных для управления режимами
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable


class AppMode(Enum):
    """Режимы приложения"""

    SLEEPING = "sleeping"  # Спящий режим
    LISTENING = "listening"  # Прослушивание
    PROCESSING = "processing"  # Обработка команды


class ModeTransitionType(Enum):
    """Типы переходов между режимами"""

    AUTOMATIC = "automatic"  # Автоматический переход
    MANUAL = "manual"  # Ручной переход
    INTERRUPT = "interrupt"  # Переход по прерыванию


class ModeStatus(Enum):
    """Статусы режима"""

    ACTIVE = "active"
    INACTIVE = "inactive"
    TRANSITIONING = "transitioning"


@dataclass
class ModeTransition:
    """Переход между режимами"""

    from_mode: AppMode
    to_mode: AppMode
    transition_type: ModeTransitionType
    condition: Callable[..., Any] | None = None
    action: Callable[..., Any] | None = None
    priority: int = 1
    timeout: float = 5.0
    data: dict[str, Any] | None = None


@dataclass
class ModeEvent:
    """Событие режима"""

    mode: AppMode
    status: ModeStatus
    timestamp: float
    transition_type: ModeTransitionType | None = None
    data: dict[str, Any] | None = None
    error: str | None = None


@dataclass
class ModeConfig:
    """Конфигурация режимов"""

    default_mode: AppMode = AppMode.SLEEPING
    enable_automatic_transitions: bool = True
    transition_timeout: float = 5.0
    max_transition_attempts: int = 3
    enable_logging: bool = True
    enable_metrics: bool = True


@dataclass
class ModeMetrics:
    """Метрики режимов"""

    total_transitions: int = 0
    successful_transitions: int = 0
    failed_transitions: int = 0
    time_in_modes: dict[AppMode, float] | None = None
    transitions_by_type: dict[ModeTransitionType, int] | None = None
    average_transition_time: float = 0.0

    def __post_init__(self):
        if self.time_in_modes is None:
            self.time_in_modes = {mode: 0.0 for mode in AppMode}
        if self.transitions_by_type is None:
            self.transitions_by_type = {t: 0 for t in ModeTransitionType}
