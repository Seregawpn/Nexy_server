"""
Autostart Manager Module

Модуль для управления автозапуском приложения.
"""

from .core.autostart_manager import AutostartManager
from .core.config import AutostartConfig as Config
from .core.types import AutostartConfig, AutostartStatus

__all__ = ["AutostartManager", "AutostartStatus", "AutostartConfig", "Config"]
