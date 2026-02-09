"""
SignalIntegration — интеграция сигналов (аудио/визуальные cues) через EventBus.

Подписывается на ключевые события приложения и публикует `playback.signal`
с короткими PCM-тонами через EventBusAudioSink. Генерация и политика (cooldown)
реализованы в `modules.signals`.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
import time
from typing import Any

from integration.core import selectors
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

from integration.adapters.signals_event_sink import EventBusAudioSink
from modules.signals.channels.audio_tone import AudioToneChannel
from modules.signals.config.types import PatternConfig
from modules.signals.core.interfaces import SignalKind, SignalPattern, SignalRequest
from modules.signals.core.service import CooldownPolicy, SimpleSignalService

logger = logging.getLogger(__name__)


@dataclass
class SignalsIntegrationConfig:
    enabled: bool = True
    sample_rate: int = 48_000
    default_volume: float = 0.2
    patterns: dict[str, PatternConfig] | None = None


class SignalIntegration:
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: SignalsIntegrationConfig | None = None,
    ) -> None:
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or SignalsIntegrationConfig()

        # Build signals service (audio channel only for now)
        sink = EventBusAudioSink(self.event_bus)
        audio_ch = AudioToneChannel(
            sink,
            sample_rate=self.config.sample_rate,
            default_volume=self.config.default_volume,
        )

        cooldowns: dict[SignalPattern, CooldownPolicy] = {}
        # If pattern configs provided, derive cooldowns
        if self.config.patterns:
            for name, p in self.config.patterns.items():
                try:
                    sp = SignalPattern(name)
                    cooldowns[sp] = CooldownPolicy(cooldown_ms=getattr(p, "cooldown_ms", 300))
                except Exception:
                    # Ignore unknown names to keep robust
                    pass
        else:
            # sensible defaults tuned for deterministic UX cues on mode transitions
            cooldowns = {
                SignalPattern.LISTEN_START: CooldownPolicy(250),
                SignalPattern.DONE: CooldownPolicy(400),
                SignalPattern.ERROR: CooldownPolicy(150),
                SignalPattern.CANCEL: CooldownPolicy(200),
            }

        self._service = SimpleSignalService(
            channels=[audio_ch],
            cooldowns=cooldowns,
            enabled=self.config.enabled,
        )

        self._initialized = False
        self._running = False
        # УБРАНО: Защита от дублей через session_id - теперь полагаемся только на cooldown в _service.emit()
        # Это предотвращает ложные подавления сигнала при одинаковых session_id между активациями
        self._last_cancel_ts: float = 0.0
        self._cancel_cooldown_sec: float = 0.5
        self._last_mode: AppMode | None = None
        self._last_error_ts: float = 0.0
        self._error_to_done_suppress_sec: float = 1.0

    async def initialize(self) -> bool:
        try:
            # Source of truth for UX cues is app.mode_changed (centralized mode coordinator).
            await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed, EventPriority.HIGH)
            # Short-press reset should always produce cancel cue.
            await self.event_bus.subscribe("keyboard.short_press", self._on_interrupt, EventPriority.CRITICAL)
            await self.event_bus.subscribe("playback.completed", self._on_playback_completed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_cancelled, EventPriority.MEDIUM)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            await self.event_bus.subscribe("grpc.request_failed", self._on_error_like, EventPriority.MEDIUM)
            await self.event_bus.subscribe("voice.recognition_failed", self._on_error_like, EventPriority.MEDIUM)
            self._last_mode = selectors.get_current_mode(self.state_manager)
            self._initialized = True
            logger.info("SignalIntegration initialized")
            return True
        except Exception as e:
            logger.error(f"SignalIntegration init error: {e}")
            return False

    async def start(self) -> bool:
        self._running = True
        logger.info("SignalIntegration started")
        return True

    async def stop(self) -> bool:
        self._running = False
        logger.info("SignalIntegration stopped")
        return True

    # Handlers
    async def _on_mode_changed(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            mode_raw = data.get("mode")
            mode = self._normalize_mode(mode_raw)
            prev_mode = self._last_mode
            self._last_mode = mode
            if mode is None:
                return

            if mode == AppMode.LISTENING:
                logger.info("Signals: LISTEN_START (app.mode_changed)")
                await self._service.emit(
                    SignalRequest(pattern=SignalPattern.LISTEN_START, kind=SignalKind.AUDIO)
                )
                return

            if mode == AppMode.SLEEPING and prev_mode is not None and prev_mode != AppMode.SLEEPING:
                # Emit DONE on real transition to sleeping.
                # Protect from false "DONE right after ERROR".
                now = time.monotonic()
                if (now - self._last_error_ts) < self._error_to_done_suppress_sec:
                    logger.debug("Signals: DONE skipped (recent error)")
                    return
                logger.info("Signals: DONE (app.mode_changed -> sleeping)")
                await self._service.emit(
                    SignalRequest(pattern=SignalPattern.DONE, kind=SignalKind.AUDIO)
                )
        except Exception:
            pass

    @staticmethod
    def _normalize_mode(mode_raw: Any) -> AppMode | None:
        if isinstance(mode_raw, AppMode):
            return mode_raw
        if mode_raw is None:
            return None
        try:
            return AppMode(str(mode_raw))
        except Exception:
            return None

    async def _on_voice_mic_opened(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            # КРИТИЧНО: Убрана проверка на одинаковый session_id - полагаемся только на cooldown в _service.emit()
            # Это предотвращает ложные подавления сигнала при одинаковых session_id между активациями
            # Cooldown (600ms) уже настроен в _service и предотвращает дребезг
            logger.info(f"Signals: LISTEN_START (voice.mic_opened, session={sid})")
            await self._service.emit(SignalRequest(pattern=SignalPattern.LISTEN_START, kind=SignalKind.AUDIO))
        except Exception as e:
            logger.debug(f"SignalIntegration _on_voice_mic_opened error: {e}")

    async def _on_playback_completed(self, event: dict[str, Any]):
        try:
            # DONE is emitted from app.mode_changed -> sleeping to keep a single source.
            logger.debug("Signals: DONE skipped (playback.completed; source=mode_changed)")
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_completed error: {e}")

    async def _on_playback_cancelled(self, event: dict[str, Any]):
        try:
            now = time.monotonic()
            if (now - self._last_cancel_ts) < self._cancel_cooldown_sec:
                logger.debug("Signals: CANCEL skipped (cooldown)")
                return

            raw_event = event or {}
            payload = raw_event.get("data")
            if not isinstance(payload, dict):
                payload = raw_event if isinstance(raw_event, dict) else {}

            logger.info("Signals: CANCEL (playback.cancelled)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.CANCEL, kind=SignalKind.AUDIO))
            self._last_cancel_ts = now
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_cancelled error: {e}")

    async def _on_interrupt(self, event: dict[str, Any]):
        try:
            now = time.monotonic()
            if (now - self._last_cancel_ts) < self._cancel_cooldown_sec:
                logger.debug("Signals: CANCEL skipped (interrupt cooldown)")
                return
            logger.info("Signals: CANCEL (keyboard.short_press)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.CANCEL, kind=SignalKind.AUDIO))
            self._last_cancel_ts = now
        except Exception as e:
            logger.debug(f"SignalIntegration _on_interrupt error: {e}")

    async def _on_error_like(self, event: dict[str, Any]):
        try:
            current_mode = selectors.get_current_mode(self.state_manager)
            if current_mode == AppMode.SLEEPING:
                logger.debug("Signals: ERROR skipped (already sleeping)")
                return
            logger.info("Signals: ERROR (failure event)")
            await self._service.emit(SignalRequest(pattern=SignalPattern.ERROR, kind=SignalKind.AUDIO))
            self._last_error_ts = time.monotonic()
        except Exception as e:
            logger.debug(f"SignalIntegration _on_error_like error: {e}")

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "enabled": self.config.enabled,
        }
