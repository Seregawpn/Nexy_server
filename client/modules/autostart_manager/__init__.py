"""
Autostart Manager Module

Модуль для управления автозапуском приложения.
"""

from .core.autostart_manager import AutostartManager
from .core.types import AutostartConfig, AutostartStatus

Config = AutostartConfig

__all__ = [
    'AutostartManager',
    'AutostartStatus',
    'AutostartConfig', 
    'Config'
]
