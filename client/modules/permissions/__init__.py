"""
Permissions Module для macOS
Управление разрешениями системы
"""


from .core.permissions_queue import PermissionsQueue
from .core.types import (
    PermissionType, PermissionStatus, PermissionInfo, PermissionResult,
    PermissionEvent, PermissionConfig, PermissionManagerState
)
from .core.config import PermissionConfigManager

__all__ = [
    'PermissionType',
    'PermissionStatus', 
    'PermissionInfo',
    'PermissionResult',
    'PermissionEvent',
    'PermissionConfig',
    'PermissionManagerState',
    'PermissionsQueue',
    'PermissionConfigManager'
]

__version__ = "1.0.2"
__author__ = "Nexy Team"
