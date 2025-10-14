"""
Типы данных для DefaultAudioManager
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Callable, Dict, Any, List
import time

class AudioStreamState(Enum):
    """Состояния аудио потока"""
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    ERROR = "error"

class HealthStatus(Enum):
    """Статус здоровья микрофона"""
    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    SILENT = "silent"
    ERROR = "error"

@dataclass
class StreamError:
    """Информация об ошибке потока"""
    error_type: str
    error_message: str
    timestamp: float = field(default_factory=time.time)
    device_info: Optional[Dict[str, Any]] = None
    retry_count: int = 0

@dataclass
class AudioMetrics:
    """Метрики аудио"""
    rms_value: float = 0.0
    peak_value: float = 0.0
    sample_count: int = 0
    error_count: int = 0
    last_health_check: float = field(default_factory=time.time)
    stream_uptime: float = 0.0

@dataclass
class DefaultAudioConfig:
    """Конфигурация DefaultAudioManager"""
    
    # Параметры аудио
    input_sample_rate: int = 16000
    output_sample_rate: int = 48000
    input_channels: int = 1
    output_channels: int = 1
    dtype: str = "int16"
    chunk_size: int = 1024
    
    # Health check параметры
    health_check_interval: float = 1.0
    health_check_duration: float = 0.3
    rms_threshold: float = 1e-4
    silent_threshold: float = 1e-6
    
    # Обработка ошибок
    auto_reopen_on_error: bool = True
    max_retry_attempts: int = 3
    retry_delay: float = 0.5
    error_cooldown: float = 2.0
    
    # Логирование
    enable_debug_logging: bool = False
    log_health_checks: bool = True
    log_stream_events: bool = True
    
    # Callbacks
    on_stream_state_change: Optional[Callable[[AudioStreamState], None]] = None
    on_health_status_change: Optional[Callable[[HealthStatus], None]] = None
    on_error: Optional[Callable[[StreamError], None]] = None
    on_metrics_update: Optional[Callable[[AudioMetrics], None]] = None

# Callback типы для совместимости
StreamStateCallback = Callable[[AudioStreamState], None]
HealthStatusCallback = Callable[[HealthStatus], None]
ErrorCallback = Callable[[StreamError], None]
MetricsCallback = Callable[[AudioMetrics], None]
