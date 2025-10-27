"""
Permission restart module.

Provides detection and scheduling logic that decides when the application
should relaunch automatically after the user grants critical macOS
permissions (microphone, accessibility, input monitoring, screen capture).
"""

from .core.config import PermissionRestartConfig, load_permission_restart_config
from .core.permission_change_detector import PermissionChangeDetector
from .core.restart_scheduler import RestartScheduler

__all__ = [
    "PermissionRestartConfig",
    "PermissionChangeDetector",
    "RestartScheduler",
    "load_permission_restart_config",
]
