"""
Voice Recognition Module - Speech to Text using Google Cloud Speech-to-Text (V2)

ARCHITECTURE:
- core/google_sr_controller.py - Standard Google SR controller (compliant with architecture)
- core/audio_route_monitor.py - Audio device monitoring
"""

from .core.audio_route_monitor import AudioRouteMonitor
from .core.google_sr_controller import GoogleSRController, GoogleSRResult

__version__ = "1.6.1.28"
__author__ = "Nexy AI Voice Assistant Team"

# Export main classes
__all__ = ["GoogleSRController", "GoogleSRResult", "AudioRouteMonitor"]
