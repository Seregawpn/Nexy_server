"""
Instance Manager Module

Модуль для управления экземплярами приложения и предотвращения дублирования.
"""

from .core.instance_manager import InstanceManager
from .core.runtime_helpers import make_probe_config, resolve_lock_file_path
from .core.types import InstanceManagerConfig, InstanceStatus, LockInfo

__all__ = [
    "InstanceManager",
    "InstanceStatus",
    "LockInfo",
    "InstanceManagerConfig",
    "resolve_lock_file_path",
    "make_probe_config",
]
