"""
Interrupt Management - Модуль управления прерываниями
"""

from .config.interrupt_config import DEFAULT_INTERRUPT_CONFIG, InterruptModuleConfig
from .core.interrupt_coordinator import InterruptCoordinator, InterruptDependencies
from .core.types import (
    InterruptConfig,
    InterruptEvent,
    InterruptMetrics,
    InterruptPriority,
    InterruptStatus,
    InterruptType,
)
from .handlers.recording_interrupt import RecordingInterruptHandler
from .handlers.speech_interrupt import SpeechInterruptHandler

__all__ = [
    "InterruptCoordinator",
    "InterruptDependencies",
    "InterruptEvent",
    "InterruptType",
    "InterruptPriority",
    "InterruptStatus",
    "InterruptConfig",
    "InterruptMetrics",
    "SpeechInterruptHandler",
    "RecordingInterruptHandler",
    "InterruptModuleConfig",
    "DEFAULT_INTERRUPT_CONFIG",
]

__version__ = "1.6.1.30"
__author__ = "Nexy Team"
