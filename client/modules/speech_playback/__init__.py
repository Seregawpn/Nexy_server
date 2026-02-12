"""
Speech Playback Module - Audio playback using AVFoundation (V2)

ARCHITECUTRE:
- core/avf_player.py - AVFoundation player implementation
- macos/ - Helper utilities for macOS
"""

from .core.avf_player import AVFoundationPlayer, AVFPlayerConfig

__version__ = "1.6.1.30"
__author__ = "Nexy AI Voice Assistant Team"

# Export main classes
__all__ = ["AVFoundationPlayer", "AVFPlayerConfig"]
