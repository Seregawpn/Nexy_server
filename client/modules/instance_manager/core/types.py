"""
Типы данных для модуля управления экземплярами.
"""

from dataclasses import dataclass
from enum import Enum


class InstanceStatus(Enum):
    """Статус экземпляра приложения."""

    SINGLE = "single"  # Единственный экземпляр
    DUPLICATE = "duplicate"  # Обнаружено дублирование
    ERROR = "error"  # Ошибка проверки


@dataclass
class LockInfo:
    """Информация о блокировке экземпляра."""

    pid: int
    timestamp: float
    lock_file: str
    process_name: str
    bundle_id: str


@dataclass
class InstanceManagerConfig:
    """Конфигурация модуля управления экземплярами."""

    enabled: bool = True
    lock_file: str = "~/Library/Application Support/Nexy/nexy.lock"
    timeout_seconds: int = 30
    lock_grace_ms: int = 1500
    cleanup_on_startup: bool = True
    show_duplicate_message: bool = True
    pid_check: bool = True  # Проверка PID процесса
