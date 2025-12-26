"""
GoogleSRController - Speech Recognition controller using speech_recognition.Microphone.

Based on working prototype from test_mvp13b_sr.py.
Designed for integration with EventBus via callbacks.
"""

from __future__ import annotations

import threading
import time
import logging
from typing import Optional, Callable, Any
from dataclasses import dataclass

import speech_recognition as sr

from .audio_route_monitor import AudioRouteMonitor

logger = logging.getLogger(__name__)


@dataclass
class GoogleSRResult:
    """Result of speech recognition."""
    text: str
    confidence: float
    language: str
    error: Optional[str] = None


class GoogleSRController:
    """
    Speech Recognition controller using speech_recognition.Microphone.
    
    Features:
    - Uses sr.Microphone for input (compliant with architecture)
    - Integrates with AudioRouteMonitor for device changes
    - Provides callbacks for EventBus integration
    """
    
    def __init__(
        self,
        language_code: str = "ru-RU",
        phrase_time_limit: float = 12.0,
        device_index: Optional[int] = None,
        on_started: Optional[Callable[[], None]] = None,
        on_completed: Optional[Callable[[GoogleSRResult], None]] = None,
        on_failed: Optional[Callable[[str], None]] = None,
    ):
        self._lang = language_code
        self._phrase_limit = phrase_time_limit
        self._device_index = device_index  # None = system default
        
        # Callbacks for EventBus integration
        self._on_started = on_started
        self._on_completed = on_completed
        self._on_failed = on_failed
        
        self._recognizer = sr.Recognizer()
        self._stop = threading.Event()
        self._listening = threading.Event()
        self._thread: Optional[threading.Thread] = None
        
        # Device monitoring
        self._route_monitor = AudioRouteMonitor(
            on_device_change=self._on_device_change
        )
        
        # Metrics
        self.utterances = 0
        self.successful = 0
        self.failed = 0
        self.last_text: str = ""
        self.last_error: Optional[str] = None
        
        self._initialized = False

    def initialize(self) -> bool:
        """Initialize the controller."""
        try:
            self._route_monitor.start()
            self._initialized = True
            logger.info("✅ GoogleSRController initialized")
            return True
        except Exception as e:
            logger.error("❌ GoogleSRController init failed: %s", e)
            return False

    def shutdown(self) -> None:
        """Shutdown the controller."""
        self._stop.set()
        self._listening.clear()
        self._route_monitor.stop()
        if self._thread:
            self._thread.join(timeout=2.0)
        logger.info("🛑 GoogleSRController shutdown")

    def start_listening(self) -> bool:
        """Start listening for speech. Returns immediately, recognition runs in background."""
        if not self._initialized:
            logger.error("❌ Controller not initialized")
            return False
            
        if self._listening.is_set():
            logger.warning("⚠️ Already listening")
            return True
        
        self._listening.set()
        self._thread = threading.Thread(target=self._capture_and_recognize, daemon=True)
        self._thread.start()
        
        if self._on_started:
            try:
                self._on_started()
            except Exception as e:
                logger.warning("⚠️ on_started callback error: %s", e)
        
        logger.info("🎙️ Started listening")
        return True

    def stop_listening(self) -> Optional[GoogleSRResult]:
        """
        Stop listening and return result.
        Note: This signals to stop, but recognition continues until phrase ends.
        """
        self._listening.clear()
        logger.info("🛑 Stop listening requested")
        
        # Wait for thread to finish
        if self._thread:
            self._thread.join(timeout=self._phrase_limit + 5.0)
        
        if self.last_text:
            return GoogleSRResult(
                text=self.last_text,
                confidence=0.9,
                language=self._lang,
                error=None
            )
        elif self.last_error:
            return GoogleSRResult(
                text="",
                confidence=0.0,
                language=self._lang,
                error=self.last_error
            )
        return None

    def cancel_listening(self) -> None:
        """Cancel listening without waiting for result."""
        self._listening.clear()
        self._stop.set()
        logger.info("❌ Listening cancelled")

    def _on_device_change(self, new_device_name: str) -> None:
        """Callback when audio device changes."""
        logger.info("🎧 Device changed to: %s", new_device_name)

    def _capture_and_recognize(self) -> None:
        """Capture audio via sr.Microphone and recognize with Google."""
        self.utterances += 1
        self.last_text = ""
        self.last_error = None
        
        try:
            # Note: PyAudio is reinitialized by AudioRouteMonitor when device changes
            mic = sr.Microphone(device_index=self._device_index)
            
            with mic as source:
                logger.info("🔊 Adjusting for ambient noise...")
                self._recognizer.adjust_for_ambient_noise(source, duration=0.3)
                
                logger.info("🎙️ Listening... (phrase_limit=%.1fs)", self._phrase_limit)
                
                try:
                    audio = self._recognizer.listen(
                        source,
                        timeout=5.0,  # Wait max 5s for speech to start
                        phrase_time_limit=self._phrase_limit
                    )
                except sr.WaitTimeoutError:
                    logger.warning("⚠️ No speech detected (timeout)")
                    self.last_error = "no_speech"
                    self.failed += 1
                    if self._on_failed:
                        self._on_failed("no_speech")
                    return
                
                logger.info("📊 Audio captured: %d bytes", len(audio.frame_data))
            
            # Recognize with Google
            logger.info("🌐 Recognizing with Google...")
            try:
                text = self._recognizer.recognize_google(audio, language=self._lang)
                text = text.strip()
                
                if text:
                    self.last_text = text
                    self.successful += 1
                    logger.info("✅ STT: %s", text)
                    
                    result = GoogleSRResult(
                        text=text,
                        confidence=0.9,
                        language=self._lang
                    )
                    
                    if self._on_completed:
                        self._on_completed(result)
                else:
                    self.last_error = "empty_result"
                    self.failed += 1
                    if self._on_failed:
                        self._on_failed("empty_result")
                        
            except sr.UnknownValueError:
                logger.warning("⚠️ Google could not understand audio")
                self.last_error = "unknown_value"
                self.failed += 1
                if self._on_failed:
                    self._on_failed("unknown_value")
            except sr.RequestError as e:
                logger.error("❌ Google SR request error: %s", e)
                self.last_error = f"request_error: {e}"
                self.failed += 1
                if self._on_failed:
                    self._on_failed(f"request_error: {e}")
                    
        except OSError as e:
            error_str = str(e).lower()
            if "busy" in error_str or "in use" in error_str:
                logger.error("❌ Microphone is busy (used by another app)")
                self.last_error = "mic_busy"
            else:
                logger.error("❌ Microphone error: %s", e)
                self.last_error = f"mic_error: {e}"
            self.failed += 1
            if self._on_failed:
                self._on_failed(self.last_error)
        except Exception as e:
            logger.error("❌ Capture error: %s", e)
            self.last_error = f"capture_error: {e}"
            self.failed += 1
            if self._on_failed:
                self._on_failed(self.last_error)

    def get_current_device(self) -> Optional[str]:
        """Get current input device name."""
        return self._route_monitor.get_current_input()

    def get_metrics(self) -> dict:
        """Get recognition metrics."""
        return {
            "utterances": self.utterances,
            "successful": self.successful,
            "failed": self.failed,
            "last_text": self.last_text,
            "last_error": self.last_error,
            "device": self.get_current_device(),
        }
