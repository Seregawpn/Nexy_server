"""
Welcome Message Module — серверная генерация приветственного сообщения при запуске приложения.
"""

from .core.welcome_player import WelcomePlayer
from .core.types import WelcomeConfig, WelcomeState, WelcomeResult

__version__ = "1.6.0.24"
__all__ = ["WelcomePlayer", "WelcomeConfig", "WelcomeState", "WelcomeResult"]
