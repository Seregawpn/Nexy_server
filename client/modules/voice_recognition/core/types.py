"""
Типы данных для распознавания речи
"""

from dataclasses import dataclass
from enum import Enum
import time
from typing import Any


class RecognitionEngine(Enum):
    """Доступные движки распознавания"""

    GOOGLE = "google"


class RecognitionState(Enum):
    """Состояния распознавания"""

    IDLE = "idle"
    LISTENING = "listening"
    PROCESSING = "processing"
    RECOGNIZING = "recognizing"
    COMPLETED = "completed"
    ERROR = "error"


class AudioStreamState(Enum):
    """Состояния аудио-потока (state machine для предотвращения гонок)"""

    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"


class RecognitionEventType(Enum):
    """Типы событий распознавания"""

    LISTENING_START = "listening_start"
    LISTENING_STOP = "listening_stop"
    RECOGNITION_START = "recognition_start"
    RECOGNITION_COMPLETE = "recognition_complete"
    RECOGNITION_ERROR = "recognition_error"
    TIMEOUT = "timeout"


@dataclass
class RecognitionConfig:
    """
    Конфигурация распознавания речи

    ВАЖНО: sample_rate, channels, chunk_size загружаются из централизованной
    конфигурации при создании объекта через default_config.py
    """

    # Основные настройки
    language: str = "en-US"  # Только английский
    sample_rate: int = 16000  # Будет перезаписано из централизованной конфигурации
    chunk_size: int = 1024  # Будет перезаписано из централизованной конфигурации
    channels: int = 1  # Будет перезаписано из централизованной конфигурации
    dtype: str = "int16"  # STT всегда int16

    # Настройки микрофона
    energy_threshold: int = 100
    dynamic_energy_threshold: bool = True
    pause_threshold: float = 0.5
    phrase_threshold: float = 0.3
    non_speaking_duration: float = 0.3
    max_duration: float = 30.0

    # Настройки распознавания
    timeout: float = 5.0
    phrase_timeout: float = 0.3
    max_alternatives: int = 1
    show_all: bool = False

    # Дополнительные настройки
    enable_logging: bool = True
    enable_metrics: bool = True
    auto_start: bool = True
    enable_audio_recovery: bool = True


@dataclass
class RecognitionResult:
    """Результат распознавания речи"""

    text: str
    confidence: float | None = None
    alternatives: list[str] | None = None
    language: str = "en-US"  # Только английский
    duration: float = 0.0
    timestamp: float = 0.0
    error: str | None = None

    def __post_init__(self):
        if self.timestamp == 0.0:
            self.timestamp = time.time()
        if self.alternatives is None:
            self.alternatives = []


@dataclass
class RecognitionEvent:
    """Событие распознавания"""

    event_type: RecognitionEventType
    state: RecognitionState
    timestamp: float
    result: RecognitionResult | None = None
    error: str | None = None
    data: dict[str, Any] | None = None


@dataclass
class RecognitionMetrics:
    """Метрики распознавания"""

    total_recognitions: int = 0
    successful_recognitions: int = 0
    failed_recognitions: int = 0
    average_confidence: float = 0.0
    average_duration: float = 0.0
    recognitions_by_language: dict[str, int] | None = None

    def __post_init__(self):
        if self.recognitions_by_language is None:
            self.recognitions_by_language = {"en-US": 0}
