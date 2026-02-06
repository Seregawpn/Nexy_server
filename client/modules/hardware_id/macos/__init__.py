"""
macOS компоненты модуля hardware_id
"""

from .hardware_detector import HardwareDetector
from .system_profiler import SystemProfilerBridge

__all__ = [
    'SystemProfilerBridge',
    'HardwareDetector'
]
