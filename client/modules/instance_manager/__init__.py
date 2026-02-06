"""
Instance Manager Module

Модуль для управления экземплярами приложения и предотвращения дублирования.
"""

from .core.instance_manager import InstanceManager
from .core.types import InstanceManagerConfig, InstanceStatus, LockInfo

__all__ = [
    'InstanceManager',
    'InstanceStatus', 
    'LockInfo',
    'InstanceManagerConfig'
]

