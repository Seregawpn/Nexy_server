"""
AudioRouteMonitor - Monitors audio device changes via AVFoundation + polling.

Based on working prototype from test_mvp13b_sr.py.
Provides automatic device detection and PyAudio reinitialization for Google SR.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
import threading
import time
from typing import Callable

logger = logging.getLogger(__name__)


def refresh_pyaudio_devices() -> None:
    """Reinitialize PyAudio to pick up device changes (Bluetooth, USB)."""
    try:
        import pyaudio
        pa = pyaudio.PyAudio()
        pa.terminate()
    except Exception:
        pass


@dataclass
class DeviceSnapshot:
    """Current audio device state."""
    input_name: str
    input_uid: str
    timestamp: float


class AudioRouteMonitor:
    """
    Monitors audio device changes via AVFoundation + polling.
    
    Features:
    - Listens to AVAudioSessionRouteChangeNotification (event-driven)
    - Polls every 2 seconds (fallback)
    - Reinitializes PyAudio when devices change
    """
    
    def __init__(self, on_device_change: Callable[[str], None] | None = None):
        self._on_change = on_device_change
        self._last_snapshot: DeviceSnapshot | None = None
        self._stop = threading.Event()
        self._poll_thread: threading.Thread | None = None
        self._obs_token = None
        self._lock = threading.Lock()
    
    def start(self) -> None:
        """Start monitoring audio device changes."""
        # Initial snapshot
        self._last_snapshot = self._get_snapshot()
        if self._last_snapshot:
            logger.info("🎧 Initial input device: %s", self._last_snapshot.input_name)
        
        # Register for route change notifications (AVFoundation)
        try:
            from AVFoundation import AVAudioSessionRouteChangeNotification  # type: ignore
            from Foundation import NSNotificationCenter  # type: ignore
            
            nc = NSNotificationCenter.defaultCenter()
            self._obs_token = nc.addObserverForName_object_queue_usingBlock_(
                AVAudioSessionRouteChangeNotification,
                None,
                None,
                self._on_route_change_notification,
            )
            logger.info("🔔 Registered for AVAudioSession route change notifications")
        except Exception as e:
            logger.warning("⚠️ Could not register for notifications: %s", e)
        
        # Start polling thread
        self._stop.clear()
        self._poll_thread = threading.Thread(target=self._poll_loop, name="device_poll", daemon=True)
        self._poll_thread.start()
        logger.info("🔄 Device polling started (every 2s)")
    
    def stop(self) -> None:
        """Stop monitoring."""
        self._stop.set()
        if self._poll_thread:
            self._poll_thread.join(timeout=3.0)
        if self._obs_token:
            try:
                from Foundation import NSNotificationCenter  # type: ignore
                NSNotificationCenter.defaultCenter().removeObserver_(self._obs_token)
            except Exception:
                pass
        logger.info("🛑 AudioRouteMonitor stopped")
    
    def get_current_input(self) -> str | None:
        """Get current input device name."""
        with self._lock:
            return self._last_snapshot.input_name if self._last_snapshot else None
    
    def _get_snapshot(self) -> DeviceSnapshot | None:
        """Get current audio route snapshot."""
        try:
            from AVFoundation import AVAudioSession  # type: ignore
            
            session = AVAudioSession.sharedInstance()
            route = session.currentRoute()
            inputs = route.inputs() if route else []
            
            if inputs and len(inputs) > 0:
                port = inputs[0]
                name = str(port.portName()) if hasattr(port, 'portName') else "Unknown"
                uid = str(port.UID()) if hasattr(port, 'UID') else name
                return DeviceSnapshot(input_name=name, input_uid=uid, timestamp=time.time())
            
            return None
        except Exception as e:
            logger.warning("⚠️ Could not get audio route: %s", e)
            return None
    
    def _check_for_changes(self, reason: str) -> None:
        """Check if device changed and trigger callback."""
        new_snapshot = self._get_snapshot()
        
        with self._lock:
            old_snapshot = self._last_snapshot
            
            if new_snapshot is None:
                return
            
            changed = (
                old_snapshot is None or
                old_snapshot.input_uid != new_snapshot.input_uid
            )
            
            if changed:
                old_name = old_snapshot.input_name if old_snapshot else "(none)"
                logger.info("🔄 Device changed (%s): %s → %s", reason, old_name, new_snapshot.input_name)
                
                # Reinitialize PyAudio to pick up new device
                refresh_pyaudio_devices()
                logger.info("🔄 PyAudio reinitialized for new device")
                
                self._last_snapshot = new_snapshot
                
                if self._on_change:
                    try:
                        self._on_change(new_snapshot.input_name)
                    except Exception as e:
                        logger.warning("⚠️ on_device_change callback error: %s", e)
            else:
                self._last_snapshot = new_snapshot
    
    def _on_route_change_notification(self, notification) -> None:
        """Handle AVAudioSession route change notification."""
        self._check_for_changes("notification")
    
    def _poll_loop(self) -> None:
        """Poll for device changes every 2 seconds."""
        while not self._stop.is_set():
            self._stop.wait(2.0)
            if not self._stop.is_set():
                self._check_for_changes("poll")
