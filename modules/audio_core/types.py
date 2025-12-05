"""
Типы данных для аудиосистемы Nexy
"""

import enum
import time
import threading
from dataclasses import dataclass, field
from typing import Literal, Optional
import sounddevice as sd


@dataclass(frozen=True)
class DeviceDescriptor:
    """Дескриптор аудиоустройства"""
    uid: str
    name: str
    latency: float
    blocksize: int
    sample_rate: float
    is_bluetooth: bool
    is_input: bool
    device_id: Optional[int] = None  # PortAudio device index (может быть None для BT)


@dataclass(frozen=True)
class DeviceChangeEvent:
    """Событие смены устройства"""
    direction: Literal["input", "output"]
    old: Optional[DeviceDescriptor]
    new: DeviceDescriptor
    source: Literal["sys", "polling"] = "sys"
    timestamp: float = field(default_factory=time.time)


class StreamState(enum.Enum):
    """Состояние потока"""
    IDLE = "idle"
    OPENING = "opening"
    ACTIVE = "active"
    CLOSING = "closing"
    ERROR_RETRYING = "error_retrying"


@dataclass
class StreamContext:
    """Контекст потока"""
    state: StreamState = StreamState.IDLE
    current_device: Optional[DeviceDescriptor] = None
    stream: Optional[sd.InputStream | sd.OutputStream] = None
    pending_device: Optional[DeviceDescriptor] = None
    lock: threading.Lock = field(default_factory=threading.Lock)
    
    def transition(self, target: StreamState):
        """Переход в новое состояние"""
        self.state = target

