"""
Модуль системы обновлений Nexy
HTTP-система обновлений без пароля с миграцией в ~/Applications
"""

from .config import UpdaterConfig
from .dmg import find_app_in_dmg, mount_dmg, unmount_dmg
from .net import UpdateHTTPClient
from .pkg import install_pkg, verify_pkg_signature
from .replace import atomic_replace_app
from .updater import Updater
from .verify import sha256_checksum, verify_app_signature, verify_ed25519_signature

__all__ = [
    'UpdaterConfig',
    'UpdateHTTPClient', 
    'sha256_checksum',
    'verify_ed25519_signature',
    'verify_app_signature',
    'mount_dmg',
    'unmount_dmg',
    'find_app_in_dmg',
    'install_pkg',
    'verify_pkg_signature',
    'atomic_replace_app',
    'Updater'
]
