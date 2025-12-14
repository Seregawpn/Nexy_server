"""
Типы данных для AVFoundation Audio Engine
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, Any


class AudioState(Enum):
    """Состояние аудио потока"""
    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    ERROR = "error"
    RECONNECTING = "reconnecting"


@dataclass
class AudioFormat:
    """Формат аудио"""
    sample_rate: int
    channels: int
    bit_depth: Optional[int] = None  # Опционально, обычно 16 для int16


@dataclass
class AudioDeviceInfo:
    """Информация об аудио устройстве"""
    name: str
    is_input: bool
    uid: Optional[str] = None


@dataclass
class AudioInputResult:
    """Результат записи аудио"""
    data: bytes
    sample_rate: int
    channels: int
    duration_ms: float
    frames_recorded: int
    device_info: Optional[AudioDeviceInfo] = None
    input_format: Optional[AudioFormat] = None
    diagnostics: Optional[Dict[str, Any]] = None
