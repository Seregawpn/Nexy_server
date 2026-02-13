"""
Update Module - Система управления обновлениями

Модуль предоставляет функциональность для:
- HTTP сервера обновлений (порт 8081)
- Управления манифестами версий
- Обработки артефактов обновлений (DMG/PKG)
- Поддержки Sparkle автообновлений для macOS
- Безопасности (SHA256, Ed25519 подписи)

Совместим с существующим update_server.py
"""

from .core.update_manager import UpdateManager
from .config import UpdateConfig
from .._version import get_module_version

__all__ = ['UpdateManager', 'UpdateConfig']
__version__ = get_module_version()


