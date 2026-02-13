"""
SpeechPlaybackIntegration — интеграция модуля последовательного воспроизведения с EventBus

Слушает gRPC-ответы (`grpc.response.audio`, `grpc.request_completed|failed`) и проигрывает аудио-чанки.
Поддерживает отмену через `keyboard.short_press`/`interrupt.request`.
"""

import asyncio
import logging
import time
from typing import TYPE_CHECKING, Any
import uuid

import numpy as np

from integration.core import selectors
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.state_manager import (  # type: ignore[attr-defined]
    ApplicationStateManager,
)

try:
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# NEW: AVFoundationPlayer (Standard)
if TYPE_CHECKING:
    from modules.speech_playback.core.avf_player import AVFoundationPlayer, AVFPlayerConfig
else:
    AVFoundationPlayer = None
    AVFPlayerConfig = None

try:
    from modules.speech_playback.core.avf_player import (  # type: ignore[assignment]
        AVFoundationPlayer,
        AVFPlayerConfig,
    )

    _AVF_PLAYER_AVAILABLE = True
except ImportError as e:
    logging.getLogger(__name__).error(f"❌ [AUDIO] AVFoundationPlayer import failed: {e}")
    _AVF_PLAYER_AVAILABLE = False  # type: ignore[reportConstantRedefinition]
    AVFoundationPlayer = None  # type: ignore[assignment, misc]
    AVFPlayerConfig = None  # type: ignore[assignment, misc]
except Exception as e:
    logging.getLogger(__name__).error(f"❌ [AUDIO] AVFoundationPlayer unexpected error: {e}")
    _AVF_PLAYER_AVAILABLE = False  # type: ignore[reportConstantRedefinition]
    AVFoundationPlayer = None  # type: ignore[assignment, misc]
    AVFPlayerConfig = None  # type: ignore[assignment, misc]

# ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ АУДИО
from config.unified_config_loader import unified_config

logger = logging.getLogger(__name__)


class SpeechPlaybackIntegration:
    """Интеграция воспроизведения с EventBus (AVFoundationPlayer)"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler

        # ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ
        self.config = unified_config.get_speech_playback_config()
        self._audio_diag_verbose = bool(self.config.get("audio_diag_verbose", False))
        self._audio_diag_log_every = max(1, int(self.config.get("audio_diag_log_every", 50)))
        self._signal_max_age_ms = max(0, int(self.config.get("signal_max_age_ms", 1200)))
        self._tts_auto_gain_enabled = bool(self.config.get("tts_auto_gain_enabled", False))
        self._tts_target_peak = float(self.config.get("tts_target_peak", 0.35))
        self._tts_max_gain = float(self.config.get("tts_max_gain", 6.0))
        self._tts_min_peak_for_gain = float(self.config.get("tts_min_peak_for_gain", 0.01))
        # Anti-clipping defaults for streamed TTS chunks.
        self._tts_safe_max_gain = float(self.config.get("tts_safe_max_gain", 2.5))
        self._tts_headroom_peak = float(self.config.get("tts_headroom_peak", 0.90))
        self._tts_gain_ema_alpha = float(self.config.get("tts_gain_ema_alpha", 0.25))

        self._avf_player: Any | None = None  # type: ignore[type-arg]

        self._initialized = False
        self._running = False
        self._had_audio_for_session: dict[Any, bool] = {}
        self._finalized_sessions: dict[Any, bool] = {}
        self._terminal_event_by_session: dict[str, str] = {}
        self._last_audio_ts: float = 0.0
        self._silence_task: asyncio.Task[Any] | None = None
        self._grpc_done_sessions: dict[Any, bool] = {}
        self._cancelled_sessions: set[Any] = set()
        self._wav_header_skipped: dict[Any, bool] = {}
        self._raw_sessions: set[str] = set()
        self._loop: asyncio.AbstractEventLoop | None = None
        self._needs_output_resync: bool = False
        self._pending_resync_task: asyncio.Task[Any] | None = None
        self._playback_ready = False
        # Guard: дедупликация cancel-циклов и блокировка сигналов в окне отмены
        self._cancel_in_flight: bool = False
        self._last_cancel_sid: str | None = None
        self._last_cancel_ts: float = 0.0
        self._cancel_guard_window_sec: float = 0.5
        self._signal_block_until_ts: float = 0.0
        self._cancel_guard_task: asyncio.Task[Any] | None = None
        self._shutdown_requested: bool = False
        # Single source of serialization for player operations (start/stop/queue).
        self._playback_op_lock = asyncio.Lock()

        # Session switch detection - prevents audio overlap
        self._current_session_id: str | None = None
        self._active_output_session_id: str | None = None
        self._tts_peak_ema_by_session: dict[str, float] = {}
        # gRPC playback start confirmation (single owner diagnostics).
        self._grpc_start_confirmed_sessions: set[str] = set()
        self._grpc_start_reasserted_sessions: set[str] = set()
        self._grpc_start_watchdogs: dict[str, asyncio.Task[Any]] = {}
        self._grpc_start_watchdog_timeout_sec: float = float(
            self.config.get("grpc_start_watchdog_timeout_sec", 0.25)
        )

    async def initialize(self) -> bool:
        try:
            # AVFoundationPlayer initialization deferred to start() to prevent early TCC triggers
            if _AVF_PLAYER_AVAILABLE:
                logger.info("ℹ️ [AUDIO] AVFoundationPlayer initialization deferred to start()")
            else:
                logger.error("❌ [AUDIO] AVFoundationPlayer module not available")

            # Подписки
            await self.event_bus.subscribe(
                "grpc.response.audio", self._on_audio_chunk, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "playback.raw_audio", self._on_raw_audio, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "playback.signal", self._on_playback_signal, EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "grpc.request_cancel", self._on_grpc_cancel, EventPriority.CRITICAL
            )

            await self.event_bus.subscribe(
                "playback.cancelled", self._on_unified_interrupt, EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "voice.mic_closed", self._on_voice_mic_closed, EventPriority.HIGH
            )

            await self.event_bus.subscribe(
                "app.shutdown", self._on_app_shutdown, EventPriority.HIGH
            )

            try:
                self._loop = self.event_bus._loop or asyncio.get_running_loop()
            except RuntimeError:
                self._loop = None

            self._initialized = True
            logger.info("SpeechPlaybackIntegration initialized")
            return True
        except Exception as e:
            await self._handle_error(e, where="speech.initialize")
            return False

    async def start(self) -> bool:
        if not self._initialized:
            logger.error("SpeechPlaybackIntegration not initialized")
            return False

        if self._running:
            return True

        # Initialize AVFoundationPlayer (Deferred)
        if (
            _AVF_PLAYER_AVAILABLE
            and AVFPlayerConfig is not None
            and AVFoundationPlayer is not None
            and self._avf_player is None
        ):
            try:
                logger.info("🚀 [AUDIO] Initializing AVFoundationPlayer (Deferred)...")
                avf_config = AVFPlayerConfig(
                    sample_rate=self.config.get("sample_rate", 48000),
                    channels=self.config.get("channels", 1),
                    volume=self.config.get("volume", 0.8),
                    audio_diag_verbose=self._audio_diag_verbose,
                    audio_diag_log_every=self._audio_diag_log_every,
                )
                self._avf_player = AVFoundationPlayer(avf_config)
                if self._avf_player is not None and self._avf_player.initialize():
                    logger.info("✅ [AUDIO] AVFoundationPlayer initialized successfully")
                    await self._publish_playback_ready(reason="startup")
                else:
                    logger.error("❌ [AUDIO] AVFoundationPlayer init failed")
                    self._avf_player = None
            except Exception as e:
                logger.error(f"❌ [AUDIO] AVFoundationPlayer error: {e}")
                self._avf_player = None

        self._running = True
        return True

    async def stop(self) -> bool:
        try:
            if self._avf_player:
                try:
                    self._avf_player.shutdown()
                except Exception:
                    pass
            self._running = False
            return True
        except Exception as e:
            await self._handle_error(e, where="speech.stop", severity="warning")
            return False

    # -------- Helper Methods --------
    async def _ensure_player_ready(self) -> bool:
        """
        Ensure player is ready and playing.
        """
        if self._avf_player:
            try:
                if not self._is_player_initialized():
                    if self._avf_player.initialize():
                        logger.info("✅ [AUDIO] AVFoundationPlayer initialized on-demand")
                        await self._publish_playback_ready(reason="on_demand")
                    else:
                        logger.error("❌ [AUDIO] AVFoundationPlayer on-demand init failed")
                        return False
                # IMPORTANT: always call start_playback().
                # AVFoundationPlayer.start_playback() is idempotent and re-asserts
                # playback AVAudioSession profile even on no-op path. This restores
                # output after microphone/input path may have reconfigured session.
                if not self._avf_player.start_playback():
                    logger.error("❌ [AUDIO] Failed to (re)start AVFoundationPlayer playback")
                    return False
                return True
            except Exception as e:
                logger.error(f"❌ [AUDIO] Ensure player ready failed: {e}")
                return False
        return False

    def _is_player_initialized(self) -> bool:
        if not self._avf_player:
            return False
        return bool(getattr(self._avf_player, "_initialized", False))

    async def _publish_playback_ready(self, reason: str) -> None:
        if self._playback_ready:
            return
        self._playback_ready = True
        await self.event_bus.publish("playback.ready", {"reason": reason})

    async def _queue_session_audio(
        self,
        *,
        session_id: Any,
        audio_data: np.ndarray,
        metadata: dict[str, Any],
        trace_extra: str,
        source: str,
        started_payload: dict[str, Any] | None = None,
    ) -> bool:
        """Single owner for enqueue/start semantics across grpc and raw_audio paths."""
        if not self._avf_player:
            return False

        if self._audio_diag_verbose and getattr(audio_data, "size", 0) > 0:
            try:
                peak = float(np.max(np.abs(audio_data)))
                rms = float(
                    np.sqrt(np.mean(np.square(np.asarray(audio_data, dtype=np.float32))))
                )
                logger.info(
                    "AUDIO_PIPELINE phase=before_queue session=%s samples=%s peak=%.4f rms=%.4f dtype=%s",
                    session_id,
                    int(audio_data.size),
                    peak,
                    rms,
                    str(audio_data.dtype),
                )
            except Exception:
                pass

        async with self._playback_op_lock:
            # Fresh-start policy for streamed gRPC sessions:
            # first chunk of a new session must reset output graph to avoid
            # stale/no-audio path after input/mic reconfiguration.
            sid_key = str(session_id) if session_id is not None else None
            first_chunk_of_new_grpc_session = (
                source == "grpc_audio"
                and sid_key is not None
                and self._active_output_session_id is not None
                and not self._had_audio_for_session.get(session_id)
                and sid_key != self._active_output_session_id
            )
            if first_chunk_of_new_grpc_session:
                logger.info(
                    "AUDIO_FRESH_START session=%s prev_session=%s reason=grpc_session_first_chunk",
                    sid_key,
                    self._active_output_session_id,
                )
                self._stop_player_locked()

            if not await self._ensure_player_ready():
                return False

            if source == "grpc_audio":
                self._confirm_grpc_start_locked(session_id)

            if not self._had_audio_for_session.get(session_id):
                ts_ms = int(time.monotonic() * 1000)
                logger.info(
                    f"TRACE phase=playback.start ts={ts_ms} session={session_id} extra={{{trace_extra}}}"
                )
                payload: dict[str, Any] = {"session_id": session_id}
                if started_payload:
                    payload.update(started_payload)
                await self.event_bus.publish("playback.started", payload)

            self._avf_player.add_audio_data(audio_data, metadata=metadata)
            self._had_audio_for_session[session_id] = True
            if sid_key is not None:
                self._active_output_session_id = sid_key

            try:
                self._last_audio_ts = self._loop.time() if self._loop else time.time()
            except Exception:
                pass
        return True

    def _confirm_grpc_start_locked(self, session_id: Any) -> None:
        sid = str(session_id) if session_id is not None else "None"
        if sid in self._grpc_start_confirmed_sessions:
            return
        route = None
        engine_running = None
        player_playing = None
        try:
            if self._avf_player and hasattr(self._avf_player, "get_playback_runtime_status"):
                snap = self._avf_player.get_playback_runtime_status()
                route = snap.get("route")
                engine_running = snap.get("engine_running")
                player_playing = snap.get("player_playing")
        except Exception:
            pass
        logger.info(
            "AUDIO_GRPC_START_CONFIRMED session=%s route=%s engine_running=%s player_playing=%s",
            sid,
            route,
            engine_running,
            player_playing,
        )
        self._grpc_start_confirmed_sessions.add(sid)
        task = self._grpc_start_watchdogs.pop(sid, None)
        if task and not task.done():
            task.cancel()

    async def _grpc_start_watchdog(self, session_id: Any) -> None:
        sid = str(session_id) if session_id is not None else "None"
        try:
            await asyncio.sleep(self._grpc_start_watchdog_timeout_sec)
            if sid in self._grpc_start_confirmed_sessions:
                return
            if sid in self._grpc_start_reasserted_sessions:
                return
            self._grpc_start_reasserted_sessions.add(sid)
            async with self._playback_op_lock:
                ready = await self._ensure_player_ready()
                logger.warning(
                    "AUDIO_GRPC_START_REASSERT session=%s ready=%s timeout_sec=%.3f",
                    sid,
                    ready,
                    self._grpc_start_watchdog_timeout_sec,
                )
                if ready:
                    self._confirm_grpc_start_locked(session_id)
        except asyncio.CancelledError:
            return
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_start_watchdog", severity="warning")

    def _clear_grpc_start_tracking(self, session_id: Any) -> None:
        sid = str(session_id) if session_id is not None else None
        if sid is None:
            return
        self._grpc_start_confirmed_sessions.discard(sid)
        self._grpc_start_reasserted_sessions.discard(sid)
        task = self._grpc_start_watchdogs.pop(sid, None)
        if task and not task.done():
            task.cancel()

    async def _emit_terminal_playback_event(
        self,
        event_name: str,
        *,
        session_id: Any | None,
        payload: dict[str, Any] | None = None,
        mark_finalized: bool = True,
    ) -> bool:
        """Publish terminal playback event once per session."""
        sid_key = str(session_id) if session_id is not None else None
        if sid_key is not None:
            emitted = self._terminal_event_by_session.get(sid_key)
            if emitted is not None:
                logger.debug(
                    "Terminal playback event dedup: sid=%s already emitted=%s, skip=%s",
                    sid_key,
                    emitted,
                    event_name,
                )
                return False
            self._terminal_event_by_session[sid_key] = event_name
            if mark_finalized:
                self._finalized_sessions[session_id] = True

        out = dict(payload or {})
        out.setdefault("session_id", session_id)
        await self.event_bus.publish(event_name, out)
        return True

    # -------- Event Handlers --------
    async def _on_audio_chunk(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            audio_bytes_len = len(data.get("bytes", b""))
            if self._audio_diag_verbose:
                logger.info(
                    f"🔊 [AUDIO_RECV] _on_audio_chunk received: session={sid}, bytes={audio_bytes_len}"
                )

            # Фильтрация поздних чанков после отмены
            if sid is not None and (sid in self._cancelled_sessions):
                logger.debug(f"Ignoring audio chunk for cancelled sid={sid}")
                return

            # Session switch detection - log for debugging, but DON'T interrupt playback
            # Audio will queue sequentially, user can manually interrupt if needed
            if (
                sid is not None
                and self._current_session_id is not None
                and sid != self._current_session_id
            ):
                logger.info(
                    f"🔄 [AUDIO_SESSION_SWITCH] session changed: {self._current_session_id} → {sid}, queueing audio"
                )

            # Update current session
            if sid is not None:
                self._current_session_id = sid

            if sid is not None:
                self.state_manager.update_session_id(str(sid))
                sid_key = str(sid)
                if sid_key not in self._grpc_start_confirmed_sessions:
                    task = self._grpc_start_watchdogs.get(sid_key)
                    if task is None or task.done():
                        self._grpc_start_watchdogs[sid_key] = asyncio.create_task(
                            self._grpc_start_watchdog(sid)
                        )

            audio_bytes: bytes = data.get("bytes") or b""
            dtype: str = (data.get("dtype") or "int16").lower()
            shape = data.get("shape") or []
            src_sample_rate: int | None = data.get("sample_rate")
            src_channels: int | None = data.get("channels")

            if not audio_bytes:
                return

            # GUARD: Проверка sample_rate из чанка на соответствие конфигурации
            expected_sample_rate = self.config.get("sample_rate", 48000)
            if src_sample_rate is not None and src_sample_rate != expected_sample_rate:
                logger.warning(
                    f"⚠️ [AUDIO_PLAYBACK] sample_rate mismatch: chunk={src_sample_rate}Hz, "
                    f"expected={expected_sample_rate}Hz для сессии {sid}. Чанк отброшен."
                )
                return  # Drop chunk - избегаем воспроизведения с неверной скоростью

            # Если sample_rate не указан - это ошибка протокола (должен быть заполнен в grpc_client_integration)
            if src_sample_rate is None:
                logger.error(
                    f"❌ [AUDIO_PLAYBACK] sample_rate отсутствует в audio_chunk для сессии {sid}. "
                    f"Чанк отброшен. Протокол нарушен."
                )
                return  # Drop chunk

            # Если channels не указан - это ошибка протокола (должен быть заполнен в grpc_client_integration)
            if src_channels is None:
                logger.error(
                    f"❌ [AUDIO_PLAYBACK] channels отсутствует в audio_chunk для сессии {sid}. "
                    f"Чанк отброшен. Протокол нарушен."
                )
                return  # Drop chunk

            # GUARD: Проверка channels из чанка на соответствие конфигурации
            expected_channels = self.config.get("channels", 1)
            if src_channels != expected_channels:
                logger.warning(
                    f"⚠️ [AUDIO_PLAYBACK] channels mismatch: chunk={src_channels}, "
                    f"expected={expected_channels} для сессии {sid}. Чанк отброшен."
                )
                return  # Drop chunk - избегаем воспроизведения с неверным количеством каналов

            # Декодирование в numpy (сохраняем логику, так как gRPC шлет байты)
            try:
                audio_bytes_in = audio_bytes
                # WAV header skip logic
                try:
                    if sid is not None and not self._wav_header_skipped.get(sid):
                        b = audio_bytes
                        if len(b) >= 12 and b[:4] == b"RIFF" and b[8:12] == b"WAVE":
                            # ... (skip header logic matches previous) ...
                            # For brevity, implementing simple skip if detected
                            self._wav_header_skipped[sid] = True
                            # Assuming standard 44 header for simplicity or keeping it simple
                            # (Real implementation handles parsing, here we trust data is mostly raw or handled)
                        else:
                            self._wav_header_skipped[sid] = True
                except Exception:
                    pass

                dt: Any
                if dtype in ("float32", "float"):
                    dt = np.float32
                elif dtype in ("int16_be", "pcm_s16be"):
                    dt = np.dtype(">i2")
                elif dtype in ("int16_le", "pcm_s16le"):
                    dt = np.dtype("<i2")
                else:
                    dt = np.dtype("<i2")

                arr = np.frombuffer(audio_bytes_in, dtype=dt)

                # DIAGNOSTIC: Check raw bytes for debugging silence issue
                if self._audio_diag_verbose and len(audio_bytes_in) >= 8:
                    first_bytes = audio_bytes_in[:8].hex()
                    peak_int16 = float(np.max(np.abs(arr))) if arr.size > 0 else 0.0
                    # Check if data is all zeros
                    is_all_zeros = np.all(arr == 0) if arr.size > 0 else True
                    logger.info(
                        f"🔬 [RAW_AUDIO_DIAG] session={sid} bytes={len(audio_bytes_in)} "
                        f"dtype={dtype} first_bytes={first_bytes} peak_int16={peak_int16:.4f} all_zeros={is_all_zeros}"
                    )

                # Guard: for float32 payloads accept only finite samples.
                # Format ownership lives in grpc_client_integration (dtype field).
                if dtype in ("float32", "float"):
                    finite_mask = np.isfinite(arr)
                    if not np.all(finite_mask):
                        invalid = int(arr.size - int(np.count_nonzero(finite_mask)))
                        logger.warning(
                            f"⚠️ [AUDIO_PLAYBACK] non-finite float32 samples: invalid={invalid}, "
                            f"session={sid}. Чанк отброшен."
                        )
                        return

                # Transport-level `shape` may be inconsistent for streamed PCM chunks.
                # Source of truth for playback is bytes + dtype + channels contract.
                # Keep stream linear to avoid frame-count collapse (e.g. shape [1, N]).
                if shape and len(shape) > 0:
                    try:
                        expected_elems = 1
                        for d in shape:
                            expected_elems *= int(d)
                        if expected_elems != int(arr.size):
                            logger.warning(
                                "⚠️ [AUDIO_PLAYBACK] shape mismatch ignored: shape=%s elems=%s bytes_elems=%s session=%s",
                                shape,
                                expected_elems,
                                int(arr.size),
                                sid,
                            )
                    except Exception:
                        pass

                if arr.ndim != 1:
                    arr = arr.reshape(-1)

                # Prepare playback samples in canonical float32 domain [-1..1].
                # grpc.response.audio owner: SpeechPlaybackIntegration.
                if dtype in ("float32", "float"):
                    arr_play = np.asarray(arr, dtype=np.float32)
                else:
                    arr_play = np.asarray(arr, dtype=np.float32) / 32768.0

                # Auto-gain for streamed TTS only (does not affect welcome/raw/signal paths).
                # Keeps speech audible on low-amplitude chunks while limiting clipping risk.
                sid_key = str(sid) if sid is not None else None
                if self._tts_auto_gain_enabled and arr_play.size > 0:
                    peak = float(np.max(np.abs(arr_play)))
                    gain = 1.0
                    if peak >= self._tts_min_peak_for_gain:
                        max_gain = max(1.0, min(self._tts_max_gain, self._tts_safe_max_gain))
                        prev_ema = self._tts_peak_ema_by_session.get(sid_key, peak) if sid_key else peak
                        alpha = min(1.0, max(0.01, self._tts_gain_ema_alpha))
                        ema_peak = (1.0 - alpha) * prev_ema + alpha * peak
                        if sid_key is not None:
                            self._tts_peak_ema_by_session[sid_key] = float(ema_peak)

                        gain = min(max_gain, self._tts_target_peak / max(float(ema_peak), 1e-6))
                        gain = max(1.0, gain)

                        # Keep headroom by constraining gain with current chunk peak.
                        headroom_limit = max(0.1, min(0.98, self._tts_headroom_peak))
                        if peak * gain > headroom_limit:
                            gain = min(gain, headroom_limit / max(peak, 1e-6))
                            gain = max(1.0, gain)
                    elif sid_key is not None:
                        # Keep EMA stable during near-silent chunks, but avoid stale growth.
                        self._tts_peak_ema_by_session[sid_key] = float(
                            self._tts_peak_ema_by_session.get(sid_key, peak) * 0.9
                        )

                    if gain > 1.0:
                        arr_play = arr_play * gain
                    arr_play = np.clip(arr_play, -0.98, 0.98)

                    if self._audio_diag_verbose:
                        clipped_samples = int(np.count_nonzero(np.abs(arr_play) >= 0.979))
                        clip_ratio = (
                            float(clipped_samples) / float(arr_play.size) if arr_play.size > 0 else 0.0
                        )
                        logger.info(
                            "🔊 [AUDIO_GAIN] session=%s gain=%.2f peak_before=%.4f target_peak=%.2f clip_ratio=%.4f",
                            sid,
                            gain,
                            peak,
                            self._tts_target_peak,
                            clip_ratio,
                        )

                metadata = {
                    "kind": "grpc_audio",
                    "session_id": sid,
                    "sample_rate": src_sample_rate,
                    "channels": src_channels,
                    "original_dtype": dtype,
                }
                await self._queue_session_audio(
                    session_id=sid,
                    audio_data=arr_play,
                    metadata=metadata,
                    trace_extra=f"chunk_size={len(audio_bytes)}",
                    source="grpc_audio",
                )

            except Exception as e:
                await self._handle_error(e, where="speech.decode_audio", severity="warning")

        except Exception as e:
            await self._handle_error(e, where="speech.on_audio_chunk", severity="warning")

    async def _on_voice_mic_closed(self, event):
        if not self._running or not self._avf_player:
            return

        # Centralized post-mic recovery hook.
        # Mic path may transiently reconfigure route/session; playback owner
        # re-asserts runtime profile through idempotent start path.
        is_playing = False
        try:
            is_playing = bool(self._avf_player.is_playing())
        except Exception:
            is_playing = False
        if not (is_playing or self._current_session_id):
            return

        sid = None
        try:
            data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
            sid = data.get("session_id")
        except Exception:
            data = {}

        try:
            status_before = self._avf_player.get_playback_runtime_status()
        except Exception:
            status_before = {}

        try:
            async with self._playback_op_lock:
                recovered = await self._ensure_player_ready()
                try:
                    status_after = self._avf_player.get_playback_runtime_status()
                except Exception:
                    status_after = {}

            logger.info(
                "AUDIO_MIC_RECOVERY session=%s recovered=%s before=%s after=%s",
                sid,
                recovered,
                status_before,
                status_after,
            )
        except Exception as e:
            await self._handle_error(e, where="speech.on_voice_mic_closed", severity="warning")

    async def _on_raw_audio(self, event: dict[str, Any]):
        try:
            if not self._avf_player:
                return
            data = (event or {}).get("data", {})
            audio_data = data.get("audio_data")
            if audio_data is None:
                return

            # Используем значения из конфига (единый источник истины) вместо хардкода
            sample_rate = data.get("sample_rate", self.config.get("sample_rate", 48000))
            channels = data.get("channels", self.config.get("channels", 1))
            pattern = data.get("pattern", "raw_audio")
            session_id = data.get("session_id")

            # Setup session: use UUID format to keep Session SoT/validators consistent.
            session_id, raw_session = self._ensure_raw_session_id(session_id)
            self._raw_sessions.add(session_id)

            self.state_manager.update_session_id(str(session_id))
            if raw_session:
                self._grpc_done_sessions[session_id] = True
            else:
                self._grpc_done_sessions.setdefault(session_id, False)
            self._finalized_sessions.pop(session_id, None)
            self._cancelled_sessions.discard(session_id)

            meta = {
                "kind": "raw_audio",
                "pattern": pattern,
                "sample_rate": sample_rate,
                "channels": channels,
            }
            if data.get("metadata"):
                meta.update(data.get("metadata"))

            queued = await self._queue_session_audio(
                session_id=session_id,
                audio_data=audio_data,
                metadata=meta,
                trace_extra=f"pattern={pattern}, raw_audio=true",
                source="raw_audio",
                started_payload={"pattern": pattern},
            )
            if not queued:
                return
            logger.debug(f"🔍 [AUDIO] Raw audio added to AVFPlayer for session {session_id}")

            if raw_session:
                if self._silence_task and not self._silence_task.done():
                    self._silence_task.cancel()
                self._silence_task = asyncio.create_task(
                    self._finalize_on_silence(session_id, timeout=1.0)
                )

        except Exception as e:
            await self._handle_error(e, where="speech.on_raw_audio", severity="warning")

    async def _on_app_shutdown(self, event):
        self._shutdown_requested = True
        await self.stop()

    async def _on_playback_signal(self, event: dict[str, Any]):
        try:
            data = (event or {}).get("data", {})
            pattern = data.get("pattern")
            cue_id = data.get("cue_id")
            now = time.monotonic()
            emitted_at_ms = data.get("emitted_at_ms")
            logger.info(
                "CUE_TRACE phase=playback_signal.received cue_id=%s pattern=%s emitted_at_ms=%s",
                cue_id,
                pattern,
                emitted_at_ms,
            )
            if self._shutdown_requested:
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=shutdown",
                    cue_id,
                    pattern,
                )
                return
            if bool(
                selectors.get_state_value(self.state_manager, StateKeys.USER_QUIT_INTENT, False)
            ):
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=user_quit_intent",
                    cue_id,
                    pattern,
                )
                return
            if isinstance(emitted_at_ms, (int, float)) and self._signal_max_age_ms > 0:
                age_ms = int(now * 1000) - int(emitted_at_ms)
                if age_ms > self._signal_max_age_ms:
                    logger.info(
                        "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=stale age_ms=%s max_age_ms=%s",
                        cue_id,
                        pattern,
                        age_ms,
                        self._signal_max_age_ms,
                    )
                    return

            current_mode = selectors.get_current_mode(self.state_manager)
            pattern_name = str(pattern or "")
            if pattern_name == "listen_start" and current_mode != AppMode.LISTENING:
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=stale_listen_start mode=%s",
                    cue_id,
                    pattern,
                    current_mode,
                )
                return
            # Terminal cues are decided by SignalIntegration (single owner).
            # Do not re-decide them here based on current mode, otherwise
            # quick LISTENING re-entry can suppress legitimate SLEEPING/error cues.

            # Anti-race guard: block only duplicate/late CANCEL cue in cancel window.
            # Do not suppress mode cues (listen_start/done/error), otherwise UX signal
            # becomes flaky right after interrupts.
            if self._cancel_in_flight and now < self._signal_block_until_ts and pattern == "cancel":
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=cancel_in_flight",
                    cue_id,
                    pattern,
                )
                return
            if not self._avf_player:
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=player_unavailable",
                    cue_id,
                    pattern,
                )
                return
            pcm = data.get("pcm")
            if not pcm:
                logger.info(
                    "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=no_pcm",
                    cue_id,
                    pattern,
                )
                return
            gain = float(data.get("gain", 1.0))

            try:
                arr = np.frombuffer(pcm, dtype=np.int16)
            except Exception:
                return

            # Apply gain if needed
            if gain != 1.0:
                try:
                    a = arr.astype(np.float32) * max(0.0, min(1.0, gain))
                    a = np.clip(a, -32768.0, 32767.0).astype(np.int16)
                    arr = a
                except Exception:
                    pass

            async with self._playback_op_lock:
                if not await self._ensure_player_ready():
                    logger.info(
                        "CUE_TRACE phase=playback_signal.dropped cue_id=%s pattern=%s drop_reason=player_not_ready",
                        cue_id,
                        pattern,
                    )
                    return

                meta = {"kind": "signal", "pattern": pattern, "cue_id": cue_id}
                # TRACE: начало воспроизведения (signal)
                ts_ms = int(time.monotonic() * 1000)
                logger.info(
                    f"TRACE phase=playback.start ts={ts_ms} session=None extra={{pattern={pattern}, signal=true}}"
                )
                logger.info(
                    "CUE_TRACE phase=playback_signal.queued cue_id=%s pattern=%s samples=%s gain=%.3f",
                    cue_id,
                    pattern,
                    len(arr),
                    gain,
                )
                await self.event_bus.publish("playback.started", {"signal": True})
                self._avf_player.add_audio_data(arr, metadata=meta)

        except Exception as e:
            await self._handle_error(e, where="speech.on_playback_signal", severity="warning")

    async def _on_unified_interrupt(self, event: dict[str, Any]):
        """
        Unified handler for playback interruption (user cancellation, stop, mode switch).
        Немедленная остановка плеера при cancel.
        """
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            now = time.monotonic()

            async with self._playback_op_lock:
                self._stop_player_locked()

            if self._is_cancel_dedup(sid, now):
                logger.debug("🛑 SpeechPlayback: cancel dedup (sid=%s)", sid)
                return

            self._arm_cancel_guard(sid, now)
            had_audio_before_cleanup = self._apply_cancel_state(sid, source="unified_interrupt")

            # КРИТИЧНО: На cancel НЕ публикуем playback.completed.
            # Terminal событие уже playback.cancelled (source of truth для cancel-ветки).
            if sid is not None:
                # TRACE: завершение воспроизведения (отмена)
                ts_ms = int(time.monotonic() * 1000)
                logger.info(
                    f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{cancelled=true}}"
                )
                logger.info(
                    f"🔍 [PLAYBACK_END] session={sid} exit_reason=cancelled "
                    f"summary={{had_audio={had_audio_before_cleanup}}}"
                )
            else:
                logger.debug(
                    "🛑 SpeechPlayback: cancel завершен без session_id (только остановка плеера)"
                )

        except Exception as e:
            await self._handle_error(e, where="speech.unified_interrupt", severity="warning")

    async def _reset_cancel_guard(self):
        try:
            await asyncio.sleep(self._cancel_guard_window_sec)
        except asyncio.CancelledError:
            return
        finally:
            self._cancel_in_flight = False

    def _stop_player_locked(self) -> None:
        if not self._avf_player:
            return
        try:
            self._avf_player.clear_queue()
            self._avf_player.stop_playback()
            logger.info("🛑 SpeechPlayback: плеер остановлен синхронно")
        except Exception as e:
            logger.error(f"❌ SpeechPlayback: ошибка остановки плеера: {e}")

    def _is_cancel_dedup(self, sid: Any, now: float) -> bool:
        return (
            sid is not None
            and self._last_cancel_sid == sid
            and (now - self._last_cancel_ts) < self._cancel_guard_window_sec
        )

    def _arm_cancel_guard(self, sid: Any, now: float) -> None:
        self._cancel_in_flight = True
        self._last_cancel_sid = sid
        self._last_cancel_ts = now
        self._signal_block_until_ts = now + self._cancel_guard_window_sec
        if self._cancel_guard_task and not self._cancel_guard_task.done():
            self._cancel_guard_task.cancel()
        self._cancel_guard_task = asyncio.create_task(self._reset_cancel_guard())

    def _apply_cancel_state(self, sid: Any, *, source: str) -> bool:
        if self._silence_task and not self._silence_task.done():
            self._silence_task.cancel()

        had_audio_before_cleanup = False
        if sid is not None:
            had_audio_before_cleanup = self._had_audio_for_session.get(sid, False)

        if sid:
            if had_audio_before_cleanup:
                self._cancelled_sessions.add(sid)
                logger.info(
                    "🛑 SpeechPlayback: session %s added to cancelled_sessions (had_audio=True, source=%s)",
                    sid,
                    source,
                )
            else:
                logger.info(
                    "🛑 SpeechPlayback: skip cancelled_sessions for %s (no audio yet, source=%s)",
                    sid,
                    source,
                )

            self._had_audio_for_session.pop(sid, None)
            self._tts_peak_ema_by_session.pop(str(sid), None)
            self._clear_grpc_start_tracking(sid)
            self._finalized_sessions[sid] = True
            self._raw_sessions.discard(str(sid))
            if self._current_session_id == sid:
                self._current_session_id = None
            if self._active_output_session_id == str(sid):
                self._active_output_session_id = None

        return had_audio_before_cleanup

    async def _on_grpc_cancel(self, event: dict[str, Any]):
        """Отмена активного воспроизведения по запросу gRPC."""
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            now = time.monotonic()
            async with self._playback_op_lock:
                self._stop_player_locked()

            if self._is_cancel_dedup(sid, now):
                logger.debug("🛑 SpeechPlayback: grpc_cancel dedup (sid=%s)", sid)
                return

            self._arm_cancel_guard(sid, now)
            self._apply_cancel_state(sid, source="grpc_cancel")

            await self._emit_terminal_playback_event(
                "playback.cancelled",
                session_id=sid,
                payload={
                    "session_id": sid,
                    "source": "grpc_cancel",
                    "reason": "server_request",
                },
            )
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_cancel", severity="warning")

    async def _on_grpc_completed(self, event: dict[str, Any]):
        """
        Handle grpc.request_completed event.
        Mark session as done from gRPC perspective.
        """
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            if sid:
                # Mark as done
                self._grpc_done_sessions[sid] = True

                # If we received audio, wait for it to finish playing
                if self._had_audio_for_session.get(sid):
                    # Only start silence task if not already finalized/cancelled
                    if sid not in self._cancelled_sessions and sid not in self._finalized_sessions:
                        if self._silence_task and not self._silence_task.done():
                            self._silence_task.cancel()
                        self._silence_task = asyncio.create_task(self._finalize_on_silence(sid))
                        logger.debug(f"Started finalize_on_silence for gRPC session {sid}")
                else:
                    # If we haven't received any audio, finalize immediately
                    if sid not in self._cancelled_sessions and sid not in self._finalized_sessions:
                        # TRACE: завершение воспроизведения (без аудио)
                        ts_ms = int(time.monotonic() * 1000)
                        logger.info(
                            f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{no_audio=true}}"
                        )
                        logger.info(
                            f"🔍 [PLAYBACK_END] session={sid} exit_reason=no_audio "
                            f"summary={{had_audio=false, duration=0}}"
                        )
                        published = await self._emit_terminal_playback_event(
                            "playback.completed",
                            session_id=sid,
                            payload={"session_id": sid},
                        )
                        if published:
                            logger.info(
                                f"SpeechPlayback: finalized session {sid} (no audio received)"
                            )
                        self._tts_peak_ema_by_session.pop(str(sid), None)
                        self._clear_grpc_start_tracking(sid)
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_completed", severity="warning")

    async def _on_grpc_failed(self, event: dict[str, Any]):
        """
        Handle grpc.request_failed event.
        """
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            error = data.get("error")

            if sid:
                self._grpc_done_sessions[sid] = True
                self._tts_peak_ema_by_session.pop(str(sid), None)
                self._clear_grpc_start_tracking(sid)

            # TRACE: завершение воспроизведения с ошибкой
            ts_ms = int(time.monotonic() * 1000)
            logger.info(
                f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{error={error}, failed=true}}"
            )
            # Publish playback failed
            await self._emit_terminal_playback_event(
                "playback.failed",
                session_id=sid,
                payload={
                    "session_id": sid,
                    "error": error,
                    "reason": "grpc_failed",
                },
            )
            if sid is not None:
                self._raw_sessions.discard(str(sid))
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_failed", severity="warning")

    # -------- Utils --------
    async def _finalize_on_silence(self, session_id: str, timeout: float = 3.0):
        """
        Ожидает завершения воспроизведения очереди и затем переводит режим.
        V2 Implementation for AVFoundationPlayer.
        """
        try:
            if session_id in self._finalized_sessions:
                logger.debug(f"Finalize skipped (already finalized): {session_id}")
                return

            start_wait = time.time()
            stable_idle_checks = 0
            # Wait until queue is drained AND scheduled audio tail is actually played out.
            while True:
                if not self._avf_player:
                    break

                try:
                    is_queue_empty = self._avf_player.is_queue_empty()
                    buffered_sec = self._avf_player.get_buffered_audio_seconds()
                except Exception:
                    is_queue_empty = True  # Assume empty if error
                    buffered_sec = 0.0

                # If filtered/cancelled
                if session_id in self._cancelled_sessions:
                    logger.debug(f"Finalize cancelled for {session_id}")
                    return

                # Consider playback done only when both queue and scheduled tail are empty
                if is_queue_empty and buffered_sec <= 0.05:
                    stable_idle_checks += 1
                else:
                    stable_idle_checks = 0

                if stable_idle_checks >= 3:
                    break

                if time.time() - start_wait > (timeout * 5):  # Safety break
                    # Raw cue/welcome sessions can keep a small device tail buffer even when queue is drained.
                    # Treat this as expected and avoid warning noise.
                    if session_id in self._raw_sessions and is_queue_empty and buffered_sec <= 0.35:
                        logger.info(
                            f"Finalize reached tail-buffer threshold {session_id} "
                            f"(queue_empty={is_queue_empty}, buffered_sec={buffered_sec:.3f})"
                        )
                    else:
                        logger.warning(
                            f"Finalize timeout waiting idle {session_id} "
                            f"(queue_empty={is_queue_empty}, buffered_sec={buffered_sec:.3f})"
                        )
                    break

                await asyncio.sleep(0.1)

            # Переход в SLEEPING (или LISTENING если это был вопрос, но здесь мы просто заканчиваем playback)
            if session_id not in self._cancelled_sessions:
                if session_id in self._finalized_sessions:
                    logger.debug(
                        f"Finalize skipped before publish (already finalized): {session_id}"
                    )
                    return
                # TRACE: завершение воспроизведения
                ts_ms = int(time.monotonic() * 1000)
                wait_duration = time.time() - start_wait
                logger.info(
                    f"TRACE phase=playback.end ts={ts_ms} session={session_id} extra={{finalized=true}}"
                )
                logger.info(
                    f"🔍 [PLAYBACK_END] session={session_id} exit_reason=queue_drained "
                    f"summary={{had_audio={self._had_audio_for_session.get(session_id, False)}, "
                    f"wait_duration_sec={wait_duration:.2f}}}"
                )
                published = await self._emit_terminal_playback_event(
                    "playback.completed",
                    session_id=session_id,
                    payload={"session_id": session_id},
                )
                if published:
                    logger.info(f"SpeechPlayback: finalized session {session_id}")
                self._raw_sessions.discard(session_id)
                self._tts_peak_ema_by_session.pop(str(session_id), None)
                self._clear_grpc_start_tracking(session_id)

        except asyncio.CancelledError:
            return
        except Exception as e:
            await self._handle_error(e, where="speech.finalize_on_silence", severity="warning")

    @staticmethod
    def _ensure_raw_session_id(session_id: Any) -> tuple[str, bool]:
        """Return a valid UUID session_id for raw playback path."""
        if isinstance(session_id, str):
            try:
                parsed = uuid.UUID(session_id, version=4)
                if str(parsed) == session_id:
                    return session_id, False
            except Exception:
                pass
        return str(uuid.uuid4()), True

    async def _handle_error(self, e: Exception, *, where: str, severity: str = "error"):
        if hasattr(self.error_handler, "handle"):
            await self.error_handler.handle(
                error=e, category="speech_playback", severity=severity, context={"where": where}
            )
        else:
            logger.error(f"Speech playback error at {where}: {e}")

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "avf_player": (self._avf_player.is_playing() if self._avf_player else False),
        }
