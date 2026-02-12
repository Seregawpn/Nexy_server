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


def _clamp_volume(value: float) -> float:
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


@dataclass
class SignalsIntegrationConfig:
    enabled: bool = True
    sample_rate: int = 48_000
    default_volume: float = 0.2
    patterns: dict[str, PatternConfig] | None = None
    suppress_listen_start_for_ptt: bool = False
    suppress_cancel_for_keyboard_interrupt: bool = False


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
        self._shutdown_requested: bool = False
        self._ptt_listening_sessions: set[str] = set()
        # Pattern-specific audio profile (single source for UX audibility).
        self._audio_profile = self._build_audio_profile()

    async def initialize(self) -> bool:
        try:
            # Source of truth for UX cues is app.mode_changed (centralized mode coordinator).
            await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed, EventPriority.HIGH)
            await self.event_bus.subscribe("mode.request", self._on_mode_request, EventPriority.MEDIUM)
            await self.event_bus.subscribe("processing.terminal", self._on_processing_terminal, EventPriority.HIGH)
            await self.event_bus.subscribe("signal.play", self._on_signal_play, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.completed", self._on_playback_completed, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_cancelled, EventPriority.MEDIUM)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
            # playback.cancelled payload is source-of-truth for CANCEL suppression decisions.
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
            if self._shutdown_requested:
                return
            data = (event or {}).get("data", {})
            mode_raw = data.get("mode")
            mode = self._normalize_mode(mode_raw)
            if mode is None:
                return
            old_mode = self._normalize_mode(data.get("old_mode"))
            sid = data.get("session_id")
            sid_key = str(sid) if sid is not None else None

            if mode == AppMode.LISTENING:
                if (
                    self.config.suppress_listen_start_for_ptt
                    and sid_key is not None
                    and sid_key in self._ptt_listening_sessions
                ):
                    logger.info("Signals: LISTEN_START suppressed for PTT session=%s", sid_key)
                    self._ptt_listening_sessions.discard(sid_key)
                    return
                logger.info("Signals: LISTEN_START (app.mode_changed)")
                await self._emit_audio_pattern(
                    SignalPattern.LISTEN_START,
                    session_id=sid_key,
                    reason="mode_listening",
                )
                if sid_key is not None:
                    self._ptt_listening_sessions.discard(sid_key)
                return

            if mode == AppMode.SLEEPING and old_mode in {AppMode.LISTENING, AppMode.PROCESSING}:
                logger.info("Signals: SLEEP cue (app.mode_changed, old=%s)", old_mode.value)
                await self._emit_audio_pattern(
                    SignalPattern.DONE,
                    session_id=sid_key,
                    reason="mode_sleeping",
                )
                return
        except Exception:
            pass

    async def _on_mode_request(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            target = self._normalize_mode(data.get("target"))
            if target != AppMode.LISTENING:
                return
            source = str(data.get("source") or "")
            sid = data.get("session_id")
            sid_key = str(sid) if sid is not None else None
            if sid_key is None:
                return
            if source == "input_processing":
                self._ptt_listening_sessions.add(sid_key)
        except Exception:
            pass

    async def _on_processing_terminal(self, event: dict[str, Any]):
        try:
            # Single Source of Truth for SLEEP cue is app.mode_changed.
            # processing.terminal stays as a lifecycle event and must not emit terminal tones.
            if self._shutdown_requested:
                return
            data = (event or {}).get("data", {})
            result = str(data.get("result") or "").lower()
            reason = str(data.get("reason") or "")
            logger.debug("Signals: terminal cue skipped (owner=app.mode_changed, result=%s, reason=%s)", result, reason)
        except Exception as e:
            logger.debug(f"SignalIntegration _on_processing_terminal error: {e}")

    async def _on_signal_play(self, event: dict[str, Any]):
        """
        Backward-compatible entry point for integrations that request an explicit cue.
        Owner of actual cue emission remains SignalIntegration.
        """
        try:
            if self._shutdown_requested:
                return
            data = (event or {}).get("data", {})
            raw_pattern = str(data.get("pattern") or "").strip().lower()
            sid = data.get("session_id")
            sid_key = str(sid) if sid is not None else None
            reason = str(data.get("reason") or "signal_play")

            pattern = self._resolve_external_pattern(raw_pattern)
            if pattern is None:
                logger.debug("Signals: signal.play skipped (unknown pattern=%s)", raw_pattern)
                return

            logger.info("Signals: explicit play (%s)", raw_pattern)
            await self._emit_audio_pattern(pattern, session_id=sid_key, reason=reason)
        except Exception as e:
            logger.debug(f"SignalIntegration _on_signal_play error: {e}")

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

    async def _on_playback_completed(self, event: dict[str, Any]):
        try:
            # DONE is emitted from app.mode_changed -> sleeping to keep a single source.
            logger.debug("Signals: DONE skipped (playback.completed; source=mode_changed)")
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_completed error: {e}")

    async def _on_playback_cancelled(self, event: dict[str, Any]):
        try:
            if self._shutdown_requested:
                return
            now = time.monotonic()
            if (now - self._last_cancel_ts) < self._cancel_cooldown_sec:
                logger.debug("Signals: CANCEL skipped (cooldown)")
                return

            raw_event = event or {}
            payload = raw_event.get("data")
            if not isinstance(payload, dict):
                payload = raw_event if isinstance(raw_event, dict) else {}
            sid = payload.get("session_id")
            sid_key = str(sid) if sid is not None else None
            cancel_source = str(payload.get("source") or "")
            cancel_initiator = str(payload.get("initiator") or "")

            if self.config.suppress_cancel_for_keyboard_interrupt:
                if cancel_initiator == "keyboard" or cancel_source.startswith("keyboard."):
                    logger.info(
                        "Signals: CANCEL suppressed for keyboard interrupt (session=%s, source=%s, initiator=%s)",
                        sid_key,
                        cancel_source or "unknown",
                        cancel_initiator or "unknown",
                    )
                    return

            logger.info("Signals: CANCEL (playback.cancelled)")
            await self._emit_audio_pattern(
                SignalPattern.CANCEL,
                session_id=sid_key,
                reason="playback_cancelled",
            )
            self._last_cancel_ts = now
        except Exception as e:
            logger.debug(f"SignalIntegration _on_playback_cancelled error: {e}")

    async def _on_app_shutdown(self, event: dict[str, Any]):
        try:
            self._shutdown_requested = True
            logger.debug("Signals: shutdown requested, suppressing further cues")
        except Exception:
            pass

    async def _emit_audio_pattern(
        self,
        pattern: SignalPattern,
        *,
        session_id: str | None = None,
        reason: str = "",
    ) -> None:
        profile = self._audio_profile.get(pattern, {})
        cue_id = self._build_cue_id(pattern, session_id)
        logger.info(
            "CUE_TRACE phase=signal.emit cue_id=%s sid=%s pattern=%s reason=%s profile=%s",
            cue_id,
            session_id,
            pattern.value,
            reason,
            {
                "tone_hz": int(profile.get("tone_hz", 880)),
                "duration_ms": int(profile.get("duration_ms", 120)),
                "volume": float(profile.get("volume", 0.2)),
            },
        )
        req = SignalRequest(
            pattern=pattern,
            kind=SignalKind.AUDIO,
            tone_hz=int(profile.get("tone_hz", 880)),
            duration_ms=int(profile.get("duration_ms", 120)),
            volume=float(profile.get("volume", 0.2)),
            session_id=session_id,
            cue_id=cue_id,
        )
        await self._service.emit(req)

    def _build_audio_profile(self) -> dict[SignalPattern, dict[str, float | int]]:
        # Audible defaults for UX cues.
        # Previous defaults were often too subtle right after TTS playback on Bluetooth routes.
        defaults: dict[SignalPattern, dict[str, float | int]] = {
            SignalPattern.LISTEN_START: {"tone_hz": 1200, "duration_ms": 220, "volume": 0.65},
            SignalPattern.DONE: {"tone_hz": 1000, "duration_ms": 220, "volume": 0.62},
            SignalPattern.ERROR: {"tone_hz": 740, "duration_ms": 240, "volume": 0.68},
            SignalPattern.CANCEL: {"tone_hz": 660, "duration_ms": 220, "volume": 0.62},
        }

        cfg = self.config.patterns or {}
        result = dict(defaults)
        for pattern in list(defaults.keys()):
            cfg_item = cfg.get(pattern.value)
            if not isinstance(cfg_item, PatternConfig):
                continue
            default_item = defaults.get(pattern, {})
            min_duration = int(default_item.get("duration_ms", 120))
            min_volume = float(default_item.get("volume", 0.2))
            result[pattern] = {
                "tone_hz": int(cfg_item.tone_hz),
                # Audibility floor: avoid too-short/too-quiet cues from config overrides.
                "duration_ms": max(min_duration, int(cfg_item.duration_ms)),
                "volume": _clamp_volume(max(min_volume, float(cfg_item.volume))),
            }
        return result

    @staticmethod
    def _resolve_external_pattern(raw_pattern: str) -> SignalPattern | None:
        """
        Map external pattern names to canonical SignalPattern.
        Keeps one owner for cue emission while allowing legacy callers.
        """
        mapping = {
            "listen_start": SignalPattern.LISTEN_START,
            "processing_start": SignalPattern.PROCESSING_START,
            "done": SignalPattern.DONE,
            "error": SignalPattern.ERROR,
            "cancel": SignalPattern.CANCEL,
            # Update-specific aliases collapse to canonical cues.
            "update_start": SignalPattern.PROCESSING_START,
            "update_progress": SignalPattern.PROCESSING_START,
            "update_success": SignalPattern.DONE,
            "update_error": SignalPattern.ERROR,
        }
        return mapping.get(raw_pattern)

    @staticmethod
    def _build_cue_id(pattern: SignalPattern, session_id: str | None) -> str:
        sid = session_id or "none"
        return f"{sid}:{pattern.value}:{int(time.monotonic() * 1000)}"

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "enabled": self.config.enabled,
        }
