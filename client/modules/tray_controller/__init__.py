"""
Tray Controller Module для macOS
Управление иконкой в меню-баре и отображение статуса приложения
"""

from .core.config import TrayConfigManager
from .core.tray_controller import TrayController
from .core.tray_types import TrayConfig, TrayIcon, TrayMenu, TrayStatus

__all__ = [
    'TrayController',
    'TrayIcon', 
    'TrayMenu',
    'TrayStatus',
    'TrayConfig',
    'TrayConfigManager'
]

__version__ = "1.6.1.13"
__author__ = "Nexy Team"








