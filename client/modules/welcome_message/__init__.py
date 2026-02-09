"""
Welcome Message Module — серверная генерация приветственного сообщения при запуске приложения.
"""

from .core.types import WelcomeConfig, WelcomeResult, WelcomeState
from .core.welcome_player import WelcomePlayer

__version__ = "1.6.1.24"
__all__ = ["WelcomePlayer", "WelcomeConfig", "WelcomeState", "WelcomeResult"]
