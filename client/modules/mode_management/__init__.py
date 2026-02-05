"""
Mode Management - Модуль управления режимами
"""

from .core.mode_controller import ModeController
from .core.types import (
    AppMode,
    ModeConfig,
    ModeEvent,
    ModeMetrics,
    ModeStatus,
    ModeTransition,
    ModeTransitionType,
)
from .modes.listening_mode import ListeningMode
from .modes.sleeping_mode import SleepingMode

__all__ = [
    'ModeController',
    'AppMode',
    'ModeTransition',
    'ModeTransitionType',
    'ModeStatus',
    'ModeEvent',
    'ModeConfig',
    'ModeMetrics',
    'SleepingMode',
    'ListeningMode'
]

__version__ = "1.6.1.11"
__author__ = "Nexy Team"
