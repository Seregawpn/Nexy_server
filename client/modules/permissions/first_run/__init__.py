"""
First Run Permissions - модуль для запроса разрешений при первом запуске.
"""

from .status_checker import (
    PermissionStatus,
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    check_all_permissions,
)

from .activator import (
    activate_microphone,
    activate_accessibility,
    activate_screen_capture,
    activate_all_permissions,
)

__all__ = [
    "PermissionStatus",
    "check_microphone_status",
    "check_accessibility_status",
    "check_screen_capture_status",
    "check_all_permissions",
    "activate_microphone",
    "activate_accessibility",
    "activate_screen_capture",
    "activate_all_permissions",
]
