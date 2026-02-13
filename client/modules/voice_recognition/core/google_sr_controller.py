"""
GoogleSRController - Speech Recognition controller using speech_recognition.Microphone.

Based on working prototype from test_mvp13b_sr.py.
Designed for integration with EventBus via callbacks.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
import threading
from typing import Any, Callable

import speech_recognition as sr

from .audio_route_monitor import AudioRouteMonitor

logger = logging.getLogger(__name__)


@dataclass
class GoogleSRResult:
    """Result of speech recognition."""

    text: str
    confidence: float
    language: str
    error: str | None = None


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
        phrase_time_limit: float | None = None,
        device_index: int | None = None,
        on_started: Callable[[], None] | None = None,
        on_completed: Callable[[GoogleSRResult], None] | None = None,
        on_failed: Callable[[str], None] | None = None,
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
        self._thread: threading.Thread | None = None

        # Device monitoring
        self._route_monitor = AudioRouteMonitor(on_device_change=self._on_device_change)

        # Metrics
        self.utterances = 0
        self.successful = 0
        self.failed = 0
        self.last_text: str = ""
        self.last_error: str | None = None

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

        # Если ранее был cancel/stop — очищаем флаг, чтобы старт был полноценным
        if self._stop.is_set():
            self._stop.clear()

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

    def stop_listening(self) -> GoogleSRResult | None:
        """
        Stop listening and return result.
        Мгновенно возвращает управление — поток завершится асинхронно.
        """
        logger.info("🛑 Stop listening requested")
        self._listening.clear()
        self._stop.set()  # Немедленно сигнализируем потоку остановиться

        # НЕ ждём поток — возвращаем управление мгновенно
        # Поток завершится асинхронно когда текущий listen() закончится

        if self.last_text:
            return GoogleSRResult(
                text=self.last_text, confidence=0.9, language=self._lang, error=None
            )
        elif self.last_error:
            return GoogleSRResult(
                text="", confidence=0.0, language=self._lang, error=self.last_error
            )
        return None

    def cancel_listening(self) -> None:
        """Cancel listening without waiting for result."""
        self._listening.clear()
        self._stop.set()
        logger.info("❌ Listening cancelled")

    def is_listening(self) -> bool:
        """Public read-only state for listening lifecycle."""
        return self._listening.is_set()

    def _on_device_change(self, new_device_name: str) -> None:
        """Callback when audio device changes."""
        logger.info("🎧 Device changed to: %s", new_device_name)

    def _capture_and_recognize(self) -> None:
        """
        Capture audio via sr.Microphone and recognize with Google.

        БЕСШОВНЫЙ РЕЖИМ: микрофон остаётся открытым на протяжении всего
        удержания PTT. Аудио-чанки отправляются на распознавание в фоновых
        потоках, в то время как запись продолжается без перерывов.
        """
        self.utterances += 1
        self.last_text = ""
        self.last_error = None

        try:
            mic = sr.Microphone(device_index=self._device_index)

            with mic as source:
                logger.info("🔊 Adjusting for ambient noise...")
                self._recognizer.adjust_for_ambient_noise(source, duration=0.3)

                # БЕСШОВНЫЙ ЦИКЛ: слушаем пока _listening активен
                while self._listening.is_set() and not self._stop.is_set():
                    if self._phrase_limit is not None:
                        logger.info("🎙️ Listening... (phrase_limit=%.1fs)", self._phrase_limit)
                    else:
                        logger.info("🎙️ Listening... (no phrase limit, will stop on silence)")

                    try:
                        # Проверяем _stop перед блокирующим вызовом
                        if self._stop.is_set():
                            # Stop-path must not emit terminal no_speech immediately.
                            # VoiceRecognitionIntegration owns delayed fallback terminal
                            # to avoid racing with final chunk recognition completion.
                            logger.info("🛑 Stop flag detected, breaking loop")
                            break

                        current_limit = self._phrase_limit  # None is allowed

                        # КРИТИЧНО: Используем ОЧЕНЬ короткий timeout для мгновенного реагирования на _stop
                        # 0.3с — минимум для захвата аудио, но позволяет проверять _stop ~3 раза/сек
                        timeout = 0.3

                        audio = self._recognizer.listen(
                            source, timeout=timeout, phrase_time_limit=current_limit
                        )

                        # КРИТИЧНО: Если _stop установлен, всё равно обрабатываем захваченный аудио!
                        # Это последний фрагмент речи пользователя — нельзя его терять.
                        if self._stop.is_set():
                            logger.info(
                                "🛑 Stop requested, processing FINAL audio chunk before exit"
                            )
                            if len(audio.frame_data) > 0:
                                threading.Thread(
                                    target=self._recognize_audio_chunk,
                                    args=(audio,),
                                    daemon=True,
                                    name="GoogleSR-FinalRecognize",
                                ).start()
                            break

                        logger.info("📊 Audio captured: %d bytes", len(audio.frame_data))

                        # КРИТИЧНО: Отправляем на распознавание В ФОНЕ
                        # Это позволяет продолжить слушание без ожидания результата
                        threading.Thread(
                            target=self._recognize_audio_chunk,
                            args=(audio,),
                            daemon=True,
                            name="GoogleSR-Recognize",
                        ).start()

                    except sr.WaitTimeoutError:
                        if self._stop.is_set():
                            # Stop-path: do not emit immediate no_speech here.
                            # Integration fallback will publish terminal no_speech
                            # only if no completion arrives in the grace window.
                            logger.info("🛑 Stop requested while waiting for speech")
                            break
                        # Timeout ожидания речи — продолжаем слушать
                        logger.debug("⏳ No speech detected, continuing...")
                        continue

                logger.info(
                    "🎙️ Listening loop ended (listening=%s, stop=%s)",
                    self._listening.is_set(),
                    self._stop.is_set(),
                )

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
                self._listening.clear()
                self._on_failed(self.last_error)
        except Exception as e:
            logger.error("❌ Capture error: %s", e)
            self.last_error = f"capture_error: {e}"
            self.failed += 1
            if self._on_failed:
                self._listening.clear()
                self._on_failed(self.last_error)
        finally:
            # Разрешаем последующий start_listening после завершения сессии
            self._listening.clear()

    def _recognize_audio_chunk(self, audio) -> None:
        """
        Распознать аудио-чанк в фоновом потоке.

        Этот метод вызывается в отдельном потоке для каждого захваченного
        аудио-фрагмента, чтобы не блокировать основной цикл слушания.
        """
        try:
            logger.info("🌐 Recognizing with Google...")
            text = self._recognizer.recognize_google(audio, language=self._lang)  # type: ignore[reportAttributeAccessIssue]
            text = text.strip()

            if text:
                self.last_text = text
                self.successful += 1
                logger.info("✅ STT: %s", text)

                result = GoogleSRResult(text=text, confidence=0.9, language=self._lang)

                if self._on_completed:
                    self._on_completed(result)
            else:
                self.last_error = "empty_result"
                self.failed += 1
                if self._on_failed:
                    self._on_failed("empty_result")

        except sr.UnknownValueError:
            logger.info("⚠️ Google could not understand audio")
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

    def get_current_device(self) -> str | None:
        """Get current input device name."""
        return self._route_monitor.get_current_input()

    def get_metrics(self) -> dict[str, Any]:
        """Get recognition metrics."""
        return {
            "utterances": self.utterances,
            "successful": self.successful,
            "failed": self.failed,
            "last_text": self.last_text,
            "last_error": self.last_error,
            "device": self.get_current_device(),
        }
