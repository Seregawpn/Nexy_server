"""
AVFoundationPlayer - Audio playback using AVAudioEngine (AVFoundation).

Replaces sounddevice-based SequentialSpeechPlayer.
Plays raw PCM audio data from server.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
import queue
import threading
import time
from typing import Any

import numpy as np

logger = logging.getLogger(__name__)

try:
    import AVFoundation as _AVFoundation
except Exception:
    _AVFoundation = None

try:
    import Foundation as _Foundation
except Exception:
    _Foundation = None

AVAudioEngine = getattr(_AVFoundation, "AVAudioEngine", None)
AVAudioFormat = getattr(_AVFoundation, "AVAudioFormat", None)
AVAudioPCMBuffer = getattr(_AVFoundation, "AVAudioPCMBuffer", None)
AVAudioPlayerNode = getattr(_AVFoundation, "AVAudioPlayerNode", None)
AVAudioSession = getattr(_AVFoundation, "AVAudioSession", None)
AVAudioSessionCategoryPlayback = getattr(_AVFoundation, "AVAudioSessionCategoryPlayback", None)
AVAudioSessionModeDefault = getattr(_AVFoundation, "AVAudioSessionModeDefault", None)
AVAudioSessionRouteChangeNotification = getattr(
    _AVFoundation, "AVAudioSessionRouteChangeNotification", None
)
AVAudioSessionCategoryOptionAllowBluetoothA2DP = getattr(
    _AVFoundation, "AVAudioSessionCategoryOptionAllowBluetoothA2DP", 0
)
AVAudioSessionCategoryPlayAndRecord = getattr(
    _AVFoundation, "AVAudioSessionCategoryPlayAndRecord", None
)
AVAudioSessionCategoryOptionDefaultToSpeaker = getattr(
    _AVFoundation, "AVAudioSessionCategoryOptionDefaultToSpeaker", 0
)
NSNotificationCenter = getattr(_Foundation, "NSNotificationCenter", None)


@dataclass
class AVFPlayerConfig:
    """Configuration for AVFoundation player."""

    sample_rate: int = 48000  # CHANGED: Default to 48k to match server
    channels: int = 1
    buffer_size: int = 512
    volume: float = 0.8
    audio_diag_verbose: bool = False
    audio_diag_log_every: int = 50


class AVFoundationPlayer:
    """
    Audio player using AVAudioEngine (AVFoundation).
    """

    def __init__(self, config: AVFPlayerConfig | None = None):
        self.config = config or AVFPlayerConfig()
        self._audio_diag_verbose = bool(self.config.audio_diag_verbose)
        self._audio_diag_log_every = max(1, int(self.config.audio_diag_log_every))
        self._diag_chunk_counter = 0

        self._engine = None
        self._player_node = None
        self._lock = threading.Lock()
        self._audio_queue: queue.Queue[dict[str, Any] | None] = queue.Queue()
        self._playing = False
        self._initialized = False
        # Approximate "audio still scheduled in AVAudioPlayerNode" horizon.
        self._scheduled_audio_until = 0.0

        self._current_output_device: str | None = None
        self._obs_token = None
        self._playback_thread: threading.Thread | None = None
        self._recreate_threads: list[threading.Thread] = []
        self._last_audio_session_signature: tuple[str | None, str | None, int, str | None] | None = (
            None
        )
        self._audio_session_unavailable_logged = False
        self._last_render_heal_ts = 0.0
        self._write_mismatch_streak = 0
        self._add_audio_warn_cooldown_sec = 5.0
        self._last_silent_warn_ts = 0.0
        self._last_quiet_warn_ts = 0.0
        self._silent_warn_suppressed = 0
        self._quiet_warn_suppressed = 0
        # Route-change recreate guard: prevents recreate storms and overlapping
        # engine rebuilds when system audio/VoiceOver rapidly toggles routes.
        self._route_recreate_in_flight = False
        self._last_route_recreate_ts = 0.0
        self._route_recreate_min_interval_sec = 1.0

    def initialize(self) -> bool:
        """Initialize AVAudioEngine and player node."""
        try:
            if not (AVAudioEngine and AVAudioFormat and AVAudioPlayerNode):
                raise RuntimeError("AVFoundation audio symbols unavailable")

            self._ensure_playback_audio_session(reason="initialize")

            with self._lock:
                # Create engine
                self._engine = AVAudioEngine.alloc().init()

                # Create player node
                self._player_node = AVAudioPlayerNode.alloc().init()

                # Attach player to engine
                self._engine.attachNode_(self._player_node)

                # Create format for our audio (PCM, 24kHz, mono, float32)
                fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                    1,  # AVAudioPCMFormatFloat32
                    self.config.sample_rate,
                    self.config.channels,
                    False,  # Non-interleaved
                )

                # Connect player to main mixer
                mixer = self._engine.mainMixerNode()
                self._engine.connect_to_format_(self._player_node, mixer, fmt)

                # КРИТИЧНО: Устанавливаем volume=1.0 для гарантии слышимого вывода
                # Это важно для приветствия и других важных сообщений
                mixer.setOutputVolume_(1.0)
                self._player_node.setVolume_(1.0)
                logger.info(f"🔊 [AVF_PLAYER] Volume set to 1.0 (mixer and player_node)")

                # Prepare engine
                self._engine.prepare()

                self._initialized = True
                self._diag_tone_played = False
                logger.info("✅ AVFoundationPlayer initialized (AVAudioEngine)")

                # Register for route change notifications
                self._register_for_route_changes()

                return True

        except Exception as e:
            logger.error(f"❌ AVFoundationPlayer init failed: {e}")
            return False

    def shutdown(self) -> None:
        """Shutdown the player."""
        with self._lock:
            self._playing = False
            try:
                if self._player_node:
                    self._player_node.stop()
                if self._engine:
                    self._engine.stop()
            except Exception as e:
                logger.warning(f"⚠️ Shutdown engine error: {e}")

            self._unregister_route_changes()
            self._initialized = False

        # Wait for playback thread to finish (outside lock to avoid deadlock)
        if self._playback_thread and self._playback_thread.is_alive():
            try:
                self._playback_thread.join(timeout=1.0)
                logger.debug("🧵 Playback thread joined")
            except Exception as e:
                logger.warning(f"⚠️ Could not join playback thread: {e}")

        # Wait for recreate threads
        with self._lock:
            threads_to_join = list(self._recreate_threads)
            self._recreate_threads.clear()

        for t in threads_to_join:
            if t.is_alive():
                try:
                    t.join(timeout=1.0)
                    logger.debug(f"🧵 Recreate thread {t.name} joined")
                except Exception as e:
                    logger.warning(f"⚠️ Could not join recreate thread: {e}")

        logger.info("🛑 AVFoundationPlayer shutdown")

    def add_audio_data(self, audio_data: np.ndarray, metadata: dict[str, Any] | None = None) -> str:
        """
        Add audio data to playback queue.

        Args:
            audio_data: NumPy array (int16 or float32)
            metadata: Optional metadata

        Returns:
            Chunk ID
        """
        if self._audio_diag_verbose:
            logger.info(
                f"📊 [ADD_AUDIO] Incoming: shape={audio_data.shape}, dtype={audio_data.dtype}, size={audio_data.size}"
            )

        # Diagnostic: check for silent audio on INPUT
        if audio_data.size > 0:
            peak = float(np.max(np.abs(audio_data)))
            min_val = float(np.min(audio_data))
            max_val = float(np.max(audio_data))
            if self._audio_diag_verbose:
                logger.info(
                    f"📊 [ADD_AUDIO] INPUT peak={peak:.4f}, min={min_val:.4f}, max={max_val:.4f}"
                )
            if peak == 0:
                self._log_add_audio_level_warning(silent=True, peak=peak)
            elif peak < 0.0001:
                self._log_add_audio_level_warning(silent=False, peak=peak)

        chunk_id = f"chunk_{id(audio_data)}"

        # Convert int16 to float32 if needed
        if audio_data.dtype == np.int16:
            if self._audio_diag_verbose:
                logger.info(f"📊 [ADD_AUDIO] Converting int16 -> float32 (dividing by 32768.0)")
            audio_float = audio_data.astype(np.float32) / 32768.0
            float_peak = float(np.max(np.abs(audio_float)))
            if self._audio_diag_verbose:
                logger.info(f"📊 [ADD_AUDIO] AFTER conversion: peak={float_peak:.6f}")
        else:
            audio_float = audio_data.astype(np.float32)
            float_peak = float(np.max(np.abs(audio_float)))
            if self._audio_diag_verbose:
                logger.info(f"📊 [ADD_AUDIO] Already float: peak={float_peak:.6f}")

        # CRITICAL FIX: Make an explicit copy to prevent race condition
        # The original numpy array might be reused/modified by the caller
        audio_copy = np.ascontiguousarray(audio_float, dtype=np.float32).copy()
        if self._audio_diag_verbose:
            logger.debug(
                f"📊 [ADD_AUDIO] Made copy: peak after copy={float(np.max(np.abs(audio_copy))):.6f}"
            )

        self._audio_queue.put({"id": chunk_id, "data": audio_copy, "metadata": metadata})
        if isinstance(metadata, dict) and metadata.get("kind") == "signal":
            logger.info(
                "CUE_TRACE phase=avf.queue_push cue_id=%s pattern=%s chunk_id=%s samples=%s queue_size=%s",
                metadata.get("cue_id"),
                metadata.get("pattern"),
                chunk_id,
                len(audio_data),
                self._audio_queue.qsize(),
            )

        if self._audio_diag_verbose:
            logger.info(
                f"📊 [ADD_AUDIO] Queued chunk {chunk_id}: {len(audio_data)} samples, queue_size={self._audio_queue.qsize()}"
            )
        return chunk_id

    def _log_add_audio_level_warning(self, silent: bool, peak: float) -> None:
        """Rate-limit verbose input-level warnings to avoid log spam."""
        if not self._audio_diag_verbose:
            return

        now = time.monotonic()
        cooldown = self._add_audio_warn_cooldown_sec
        if silent:
            suppressed = self._silent_warn_suppressed
            if (now - self._last_silent_warn_ts) < cooldown:
                self._silent_warn_suppressed = suppressed + 1
                return
            extra = (
                f" (suppressed {suppressed} similar in {cooldown:.1f}s)"
                if suppressed > 0
                else ""
            )
            logger.warning("⚠️ [ADD_AUDIO] Incoming audio is TOTALLY SILENT%s", extra)
            self._last_silent_warn_ts = now
            self._silent_warn_suppressed = 0
            return

        suppressed = self._quiet_warn_suppressed
        if (now - self._last_quiet_warn_ts) < cooldown:
            self._quiet_warn_suppressed = suppressed + 1
            return
        extra = (
            f" (suppressed {suppressed} similar in {cooldown:.1f}s)"
            if suppressed > 0
            else ""
        )
        logger.warning("⚠️ [ADD_AUDIO] Incoming audio is very quiet (peak: %.6f)%s", peak, extra)
        self._last_quiet_warn_ts = now
        self._quiet_warn_suppressed = 0

    def start_playback(self) -> bool:
        """Start playback."""
        if not self._initialized:
            logger.error("❌ Player not initialized")
            return False

        with self._lock:
            try:
                engine = self._engine
                player_node = self._player_node
                if engine is None or player_node is None:
                    logger.error("❌ Player internals unavailable")
                    return False

                # Always re-assert playback audio session profile, even if playback
                # fast-path returns no-op. Mic/STT path may have changed session state.
                self._ensure_playback_audio_session(reason="start_playback")

                # Idempotent fast-path: avoid spawning duplicate playback threads.
                thread_alive = self._playback_thread.is_alive() if self._playback_thread else False
                if (
                    self._playing
                    and thread_alive
                    and engine.isRunning()
                    and player_node.isPlaying()
                ):
                    # Keep output chain unmuted even on no-op path.
                    # Route/mic interactions can leave node or mixer volume altered
                    # while playback state still looks healthy.
                    try:
                        player_node.setVolume_(1.0)
                        mixer = engine.mainMixerNode()
                        mixer.setOutputVolume_(1.0)
                    except Exception:
                        pass
                    try:
                        if AVAudioSession:
                            snap = self._capture_audio_session_runtime(AVAudioSession.sharedInstance())
                            logger.info(
                                "AUDIO_SESSION_RUNTIME reason=start_playback_noop snapshot=%s",
                                snap,
                            )
                    except Exception:
                        pass
                    logger.debug("▶️ Playback already active, start_playback is a no-op")
                    return True

                # КРИТИЧНО: Устанавливаем volume=1.0 для гарантии слышимого вывода
                player_node.setVolume_(1.0)
                mixer = engine.mainMixerNode()
                mixer.setOutputVolume_(1.0)
                logger.info(
                    f"🔊 [AVF_PLAYER] Volume set to 1.0 at playback start (mixer and player_node)"
                )

                # Start engine if not running
                # Note: mainMixerNode -> outputNode connection is AUTOMATIC in AVAudioEngine
                if not engine.isRunning():
                    # CRITICAL FIX: When engine was stopped (e.g. by macOS audio
                    # interruption from microphone/PyAudio), the player_node→mixer
                    # connection can become invalid. Re-attach and reconnect the
                    # player node to the engine graph before restarting.
                    try:
                        fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                            1,  # AVAudioPCMFormatFloat32
                            self.config.sample_rate,
                            self.config.channels,
                            False,
                        )
                        # Disconnect any stale connections first
                        engine.disconnectNodeOutput_(player_node)
                        # Re-connect player → mixer
                        mixer_node = engine.mainMixerNode()
                        engine.connect_to_format_(player_node, mixer_node, fmt)
                        mixer_node.setOutputVolume_(1.0)
                        player_node.setVolume_(1.0)
                        engine.prepare()
                        logger.info(
                            "🔄 [AVF_PLAYER] Re-connected player→mixer after engine stop"
                        )
                    except Exception as reconnect_err:
                        logger.warning(
                            "⚠️ [AVF_PLAYER] Failed to reconnect player node: %s",
                            reconnect_err,
                        )

                    success, error = engine.startAndReturnError_(None)
                    if success:
                        logger.info("🔊 AVAudioEngine started successfully")
                    else:
                        logger.error(f"❌ Failed to start AVAudioEngine: {error}")
                        return False
                else:
                    logger.debug("🔊 AVAudioEngine already running")

                # Route snapshot on every playback start to diagnose "audio scheduled but not audible".
                self._log_output_route_snapshot()
                try:
                    if AVAudioSession:
                        snap = self._capture_audio_session_runtime(AVAudioSession.sharedInstance())
                        logger.info("AUDIO_SESSION_RUNTIME reason=start_playback snapshot=%s", snap)
                except Exception:
                    pass

                # Start the player node
                player_node.play()
                self._playing = True
                logger.info("▶️ Playback started")

                # Start playback thread
                if not thread_alive:
                    self._playback_thread = threading.Thread(
                        target=self._playback_loop, daemon=True, name="AVFPlaybackLoop"
                    )
                    self._playback_thread.start()
                    logger.info(
                        f"▶️ Playback thread started: {self._playback_thread.name}, is_alive={self._playback_thread.is_alive()}"
                    )
                else:
                    logger.debug("▶️ Playback thread already alive, skipping thread restart")

                return True
            except Exception as e:
                logger.error(f"❌ Start playback failed: {e}")
                return False

    def get_playback_runtime_status(self) -> dict[str, Any]:
        """Return runtime playback status for integration-level diagnostics."""
        with self._lock:
            engine = self._engine
            player_node = self._player_node
            status: dict[str, Any] = {
                "playing_flag": bool(self._playing),
                "thread_alive": bool(self._playback_thread and self._playback_thread.is_alive()),
                "engine_running": bool(engine and engine.isRunning()),
                "player_playing": bool(player_node and player_node.isPlaying()),
                "route": None,
                "session_snapshot": None,
            }
            try:
                if AVAudioSession:
                    session = AVAudioSession.sharedInstance()
                    status["route"] = self._current_route_signature(session)
                    status["session_snapshot"] = self._capture_audio_session_runtime(session)
            except Exception:
                pass
            return status

    def _log_output_route_snapshot(self) -> None:
        """Log current output format/device each time playback starts."""
        try:
            engine = self._engine
            if engine is None:
                return
            output_node = engine.outputNode()
            output_format = output_node.outputFormatForBus_(0)
            logger.info(
                f"🔊 [AVF_PLAYER] Output snapshot: {output_format.sampleRate()}Hz, "
                f"{output_format.channelCount()}ch, format={output_format.commonFormat()}"
            )
            if AVAudioSession:
                try:
                    session = AVAudioSession.sharedInstance()
                    current_route = session.currentRoute()
                    if current_route:
                        outputs = current_route.outputs()
                        if outputs and len(outputs) > 0:
                            output = outputs[0]
                            device_name = (
                                output.portName() if hasattr(output, "portName") else "unknown"
                            )
                            port_type = (
                                output.portType() if hasattr(output, "portType") else "unknown"
                            )
                            logger.info(
                                f"🔊 [AVF_PLAYER] Output route snapshot: {device_name} (type: {port_type})"
                            )
                except Exception as device_e:
                    logger.debug(f"⚠️ [AVF_PLAYER] Could not get output route snapshot: {device_e}")
        except Exception as format_e:
            logger.warning(f"⚠️ [AVF_PLAYER] Could not get output snapshot: {format_e}")

    def _current_route_signature(self, session) -> str | None:
        try:
            current_route = session.currentRoute()
            if not current_route:
                return None
            outputs = current_route.outputs()
            if not outputs or len(outputs) == 0:
                return None
            output = outputs[0]
            device_name = output.portName() if hasattr(output, "portName") else "unknown"
            port_type = output.portType() if hasattr(output, "portType") else "unknown"
            return f"{device_name}:{port_type}"
        except Exception:
            return None

    def _capture_audio_session_runtime(self, session) -> dict[str, Any]:
        snap: dict[str, Any] = {}
        try:
            if hasattr(session, "category"):
                snap["category"] = str(session.category())
            if hasattr(session, "mode"):
                snap["mode"] = str(session.mode())
            if hasattr(session, "otherAudioPlaying"):
                snap["other_audio_playing"] = bool(session.otherAudioPlaying())
            if hasattr(session, "secondaryAudioShouldBeSilencedHint"):
                snap["secondary_should_be_silenced"] = bool(
                    session.secondaryAudioShouldBeSilencedHint()
                )
            if hasattr(session, "outputVolume"):
                snap["output_volume"] = float(session.outputVolume())
        except Exception:
            pass
        snap["route"] = self._current_route_signature(session)
        return snap

    def _ensure_playback_audio_session(self, *, reason: str) -> None:
        """Centralized owner for playback audio session profile."""
        if not AVAudioSession or AVAudioSessionCategoryPlayback is None:
            if not self._audio_session_unavailable_logged:
                logger.warning(
                    "AUDIO_SESSION_PROFILE reason=%s applied=false unavailable=true has_session=%s has_playback_category=%s",
                    reason,
                    bool(AVAudioSession),
                    bool(AVAudioSessionCategoryPlayback is not None),
                )
                self._audio_session_unavailable_logged = True
            return
        try:
            session = AVAudioSession.sharedInstance()
            route_sig = self._current_route_signature(session)

            # Detect Bluetooth output — use PlayAndRecord to avoid A2DP/HFP conflict
            is_bluetooth = route_sig and "Bluetooth" in route_sig
            if is_bluetooth and AVAudioSessionCategoryPlayAndRecord is not None:
                chosen_category_obj = AVAudioSessionCategoryPlayAndRecord
                target_category = str(AVAudioSessionCategoryPlayAndRecord)
                target_options = (
                    int(AVAudioSessionCategoryOptionAllowBluetoothA2DP or 0)
                    | int(AVAudioSessionCategoryOptionDefaultToSpeaker or 0)
                )
            else:
                chosen_category_obj = AVAudioSessionCategoryPlayback
                target_category = str(AVAudioSessionCategoryPlayback)
                target_options = int(AVAudioSessionCategoryOptionAllowBluetoothA2DP or 0)

            target_mode = str(AVAudioSessionModeDefault) if AVAudioSessionModeDefault else None
            target_signature = (target_category, target_mode, target_options, route_sig)
            before = self._capture_audio_session_runtime(session)
            current_category = None
            current_mode = None
            try:
                if hasattr(session, "category"):
                    current_category = str(session.category())
                if hasattr(session, "mode"):
                    current_mode = str(session.mode())
            except Exception:
                pass
            already_on_target = current_category == target_category and (
                target_mode is None or current_mode == target_mode
            )

            if self._last_audio_session_signature == target_signature and already_on_target:
                logger.debug(
                    "AUDIO_SESSION_PROFILE reason=%s applied=false dedup=true category=%s mode=%s options=%s route=%s",
                    reason,
                    target_category,
                    target_mode,
                    target_options,
                    route_sig,
                )
                return

            if is_bluetooth:
                logger.info(
                    "🎧 Bluetooth output detected, using PlayAndRecord category for route=%s",
                    route_sig,
                )

            if (
                target_mode is not None
                and hasattr(session, "setCategory_mode_options_error_")
            ):
                session.setCategory_mode_options_error_(
                    chosen_category_obj,
                    AVAudioSessionModeDefault,
                    target_options,
                    None,
                )
            elif hasattr(session, "setCategory_withOptions_error_"):
                session.setCategory_withOptions_error_(
                    chosen_category_obj, target_options, None
                )
            else:
                session.setCategory_error_(chosen_category_obj, None)
            session.setActive_error_(True, None)
            self._last_audio_session_signature = target_signature
            after = self._capture_audio_session_runtime(session)
            logger.info(
                "AUDIO_SESSION_PROFILE reason=%s applied=true category=%s mode=%s options=%s route=%s before=%s after=%s",
                reason,
                target_category,
                target_mode,
                target_options,
                route_sig,
                before,
                after,
            )
        except Exception as e:
            logger.warning(
                "⚠️ [AVF_PLAYER] Failed to apply playback audio session profile (%s): %s",
                reason,
                e,
            )

    def _ensure_engine_running(self) -> bool:
        """
        Ensure AVAudioEngine is running.
        Restarts the engine if it stopped (e.g., due to route change or interruption).
        Also reconnects playerNode to mixer if needed.

        Returns:
            True if engine is running, False otherwise
        """
        if not self._engine or AVAudioFormat is None:
            return False

        try:
            if not self._engine.isRunning():
                now = time.time()
                if getattr(self, "_engine_restart_in_progress", False):
                    return False
                last_attempt = getattr(self, "_engine_restart_last_attempt", 0.0)
                backoff = getattr(self, "_engine_restart_backoff", 1.0)
                if now - last_attempt < backoff:
                    return False
                self._engine_restart_in_progress = True
                self._engine_restart_last_attempt = now
                self._engine_restart_backoff = min(backoff * 2, 8.0)

                last_warn = getattr(self, "_engine_restart_last_warn", 0.0)
                if now - last_warn >= 5.0:
                    logger.warning("⚠️ AVAudioEngine stopped, attempting to restart...")
                    self._engine_restart_last_warn = now

                # CRITICAL: Reconnect playerNode to mixer before starting
                # Connection may be lost when engine stops.
                # Must disconnect first to clear stale connections that silently
                # swallow scheduled buffers without rendering them.
                try:
                    mixer = self._engine.mainMixerNode()
                    fmt = (
                        AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                            1,  # AVAudioPCMFormatFloat32
                            self.config.sample_rate,
                            self.config.channels,
                            False,
                        )
                    )
                    # Disconnect stale output first
                    try:
                        self._engine.disconnectNodeOutput_(self._player_node)
                    except Exception:
                        pass
                    self._engine.connect_to_format_(self._player_node, mixer, fmt)
                    logger.info("🔗 Reconnected playerNode to mixer (with disconnect)")
                except Exception as conn_e:
                    logger.warning(f"⚠️ Connection warning (may already exist): {conn_e}")

                # Prepare and start engine
                self._engine.prepare()
                success, error = self._engine.startAndReturnError_(None)
                if success:
                    logger.info("🔊 AVAudioEngine restarted successfully")
                    self._engine_restart_backoff = 1.0
                    self._engine_restart_in_progress = False

                    # Set volumes
                    player_node = self._player_node
                    if player_node is None:
                        logger.error("❌ Player node unavailable after restart")
                        return False
                    player_node.setVolume_(1.0)
                    mixer = self._engine.mainMixerNode()
                    mixer.setOutputVolume_(1.0)

                    # Ensure player node is playing
                    if not player_node.isPlaying():
                        player_node.play()
                        logger.info("▶️ PlayerNode restarted")
                    return True
                else:
                    logger.error(f"❌ Failed to restart AVAudioEngine: {error}")
                    self._engine_restart_in_progress = False
                    return False
            return True
        except Exception as e:
            logger.error(f"❌ Error ensuring engine running: {e}")
            import traceback

            logger.error(traceback.format_exc())
            if getattr(self, "_engine_restart_in_progress", False):
                self._engine_restart_in_progress = False
            return False

    def _maybe_recreate_for_render_stall(self, *, reason: str) -> bool:
        """
        Best-effort self-heal for runtime render stalls.
        Rate-limited to avoid recreate storms.
        """
        now = time.monotonic()
        if (now - self._last_render_heal_ts) < 2.0:
            return False
        self._last_render_heal_ts = now
        try:
            logger.warning("⚠️ Render stall detected (%s), recreating AVF player", reason)
            self.recreate()
            return True
        except Exception as e:
            logger.error(f"❌ Render self-heal failed ({reason}): {e}")
            return False

    def stop_playback(self) -> None:
        """Stop playback."""
        playback_thread: threading.Thread | None = None
        with self._lock:
            self._playing = False
            self._scheduled_audio_until = 0.0
            playback_thread = self._playback_thread
            try:
                if self._player_node:
                    self._player_node.stop()
            except Exception as e:
                logger.warning(f"⚠️ Stop error: {e}")
            # Wake playback loop promptly so it does not linger across next start_playback.
            try:
                self._audio_queue.put_nowait(None)
            except Exception:
                pass
            logger.info("⏹️ Playback stopped")
        # Avoid long blocking in caller thread, but give worker a short window to exit.
        try:
            if playback_thread and playback_thread.is_alive():
                playback_thread.join(timeout=0.25)
                if playback_thread.is_alive():
                    logger.debug("⏹️ Playback thread still stopping in background")
        except Exception:
            pass

    def is_playing(self) -> bool:
        """Check if currently playing."""
        thread_alive = self._playback_thread.is_alive() if self._playback_thread else False
        player_playing = False
        try:
            player_playing = self._player_node.isPlaying() if self._player_node else False
        except Exception:
            pass
        buffered_sec = self.get_buffered_audio_seconds()
        queue_non_empty = not self._audio_queue.empty()
        engine_running = self._engine.isRunning() if self._engine else False
        if self._audio_diag_verbose:
            logger.debug(
                f"🔍 is_playing check: _playing={self._playing}, thread_alive={thread_alive}, engine_running={engine_running}, player_playing={player_playing}"
            )
        # Consider active only when render path is actually alive.
        # This prevents false-ready state where chunks are queued but player node is not rendering.
        return (
            self._playing
            and thread_alive
            and engine_running
            and player_playing
            and (queue_non_empty or buffered_sec > 0.02)
        )

    def is_queue_empty(self) -> bool:
        """Check if audio queue is empty."""
        return self._audio_queue.empty()

    def get_buffered_audio_seconds(self) -> float:
        """
        Approximate amount of audio already scheduled to AVAudioPlayerNode.
        """
        with self._lock:
            remaining = self._scheduled_audio_until - time.monotonic()
        return remaining if remaining > 0.0 else 0.0

    def clear_queue(self) -> None:
        """Clear playback queue."""
        with self._lock:
            while not self._audio_queue.empty():
                try:
                    self._audio_queue.get_nowait()
                except queue.Empty:
                    break
        logger.debug("🗑️ Audio queue cleared")

    def _playback_loop(self) -> None:
        """Background thread for processing audio queue."""
        if AVAudioFormat is None or AVAudioPCMBuffer is None:
            logger.error("❌ AVFoundation buffer/format symbols unavailable")
            return

        # Pre-create the format to avoid allocation in the loop if possible
        fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
            1,  # AVAudioPCMFormatFloat32
            self.config.sample_rate,
            self.config.channels,
            False,  # Non-interleaved
        )

        while self._playing:
            try:
                chunk = self._audio_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            if chunk is None:
                # Stop sentinel from previous stop can be observed after a new start.
                # Exit only when playback is actually stopped; otherwise ignore stale sentinel.
                if not self._playing:
                    break
                continue

            try:
                audio_data = chunk["data"]
                frame_count = len(audio_data)
                metadata = chunk.get("metadata") if isinstance(chunk, dict) else None
                cue_id = metadata.get("cue_id") if isinstance(metadata, dict) else None
                cue_pattern = metadata.get("pattern") if isinstance(metadata, dict) else None
                chunk_kind = metadata.get("kind") if isinstance(metadata, dict) else None
                self._diag_chunk_counter += 1

                # CRITICAL DIAGNOSTIC: Check data immediately after extracting from queue
                if self._audio_diag_verbose and audio_data.size > 0:
                    queue_peak = float(np.max(np.abs(audio_data)))
                    first_10 = audio_data[: min(10, len(audio_data))]
                    logger.info(
                        f"📊 [QUEUE_EXTRACT] peak={queue_peak:.6f}, first_10={first_10[:5]}"
                    )
                    if queue_peak == 0:
                        # Zero-valued chunks are expected on silence tails in streaming TTS.
                        # Keep this as debug telemetry to avoid noisy false-positive errors.
                        logger.debug(
                            "🔇 [QUEUE_EXTRACT] Audio data is ZERO after extraction from queue"
                        )

                if frame_count == 0:
                    continue

                # Track approximate "scheduled but not yet rendered" duration.
                chunk_duration_sec = frame_count / float(self.config.sample_rate)
                with self._lock:
                    now = time.monotonic()
                    base = self._scheduled_audio_until if self._scheduled_audio_until > now else now
                    self._scheduled_audio_until = base + chunk_duration_sec

                # Create buffer
                buffer = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(fmt, frame_count)
                buffer.setFrameLength_(frame_count)

                # Get the pointer to the first channel's data
                float_channel_data = buffer.floatChannelData()
                if float_channel_data is None:
                    logger.error("❌ floatChannelData() returned None")
                    continue

                ptr = float_channel_data[0]

                # Log pre-copy peak for diagnostics (use full array, not just first 100)
                pre_peak = float(np.max(np.abs(audio_data)))
                write_peak = pre_peak
                if self._audio_diag_verbose and (chunk_kind == "grpc_audio" or (self._diag_chunk_counter % self._audio_diag_log_every) == 0):
                    try:
                        pre_rms = float(np.sqrt(np.mean(np.square(audio_data.astype(np.float32)))))
                    except Exception:
                        pre_rms = 0.0
                    logger.info(
                        "AUDIO_PIPELINE phase=before_schedule kind=%s chunk=%s frames=%s peak=%.4f rms=%.4f",
                        chunk_kind or "unknown",
                        self._diag_chunk_counter,
                        frame_count,
                        pre_peak,
                        pre_rms,
                    )
                if self._audio_diag_verbose:
                    logger.debug(f"📊 Pre-copy peak (FULL): {pre_peak:.4f}, samples={frame_count}")

                # Write float32 samples directly into AVAudioPCMBuffer channel memory.
                # objc.varlist supports `as_buffer(count)` which exposes writable memoryview.
                try:
                    audio_contiguous = np.ascontiguousarray(audio_data, dtype=np.float32)
                    raw = ptr.as_buffer(frame_count)
                    dst = np.frombuffer(raw, dtype=np.float32, count=frame_count)
                    dst[:] = audio_contiguous
                    write_peak = float(np.max(np.abs(dst))) if dst.size else 0.0

                    if self._audio_diag_verbose:
                        test_idx = 0
                        for i in range(min(1000, frame_count)):
                            if abs(audio_contiguous[i]) > 0.01:
                                test_idx = i
                                break
                        read_back = float(ptr[test_idx])
                        logger.debug(
                            "📊 Buffer write check: idx=%s wrote=%.6f read=%.6f",
                            test_idx,
                            float(audio_contiguous[test_idx]),
                            read_back,
                        )

                    # Guard against silent/corrupted writes with non-silent source.
                    if pre_peak > 0.02 and write_peak < (pre_peak * 0.15):
                        self._write_mismatch_streak += 1
                        logger.warning(
                            "⚠️ Buffer write mismatch: src_peak=%.4f write_peak=%.4f streak=%s",
                            pre_peak,
                            write_peak,
                            self._write_mismatch_streak,
                        )
                    else:
                        self._write_mismatch_streak = 0

                except Exception as copy_e:
                    logger.error(f"❌ Buffer memory write failed: {copy_e}")
                    logger.error("❌ AUDIO MAY BE SILENT - unable to write AVAudioPCMBuffer memory")

                # Ensure engine is running before scheduling buffer
                if not self._ensure_engine_running():
                    logger.warning("⚠️ Engine not running, waiting before retry...")
                    # Do not drop chunk on transient engine outage.
                    self._audio_queue.put(chunk)
                    time.sleep(0.2)  # Prevent tight loop when engine is down
                    continue

                player_node = self._player_node
                if player_node is None:
                    logger.error("❌ Cannot schedule buffer - player node unavailable")
                    # Preserve chunk and try recovery.
                    self._audio_queue.put(chunk)
                    self._maybe_recreate_for_render_stall(reason="player_node_unavailable")
                    continue

                # Guard against a stale node state: engine may run while node is paused/stopped.
                try:
                    if not player_node.isPlaying():
                        player_node.play()
                        logger.warning("⚠️ Player node was not playing; resumed before scheduling chunk")
                    if not player_node.isPlaying():
                        logger.error("❌ Player node still not playing after resume")
                        self._audio_queue.put(chunk)
                        if self._maybe_recreate_for_render_stall(reason="player_not_playing"):
                            time.sleep(0.1)
                        continue
                except Exception as play_e:
                    logger.warning(f"⚠️ Could not resume player node: {play_e}")
                    self._audio_queue.put(chunk)
                    if self._maybe_recreate_for_render_stall(reason="player_resume_exception"):
                        time.sleep(0.1)
                    continue

                # Schedule buffer for playback
                def _on_buffer_consumed(chunk_num=self._diag_chunk_counter, fc=frame_count):
                    logger.info(f"✅ [BUFFER_CONSUMED] chunk={chunk_num} frames={fc} — engine rendered this buffer")

                player_node.scheduleBuffer_completionHandler_(buffer, _on_buffer_consumed)
                if self._write_mismatch_streak >= 3:
                    logger.error("❌ Repeated buffer write mismatches, attempting self-heal recreate")
                    self._write_mismatch_streak = 0
                    if self._maybe_recreate_for_render_stall(reason="write_peak_mismatch"):
                        time.sleep(0.1)
                        continue
                if cue_id is not None:
                    logger.info(
                        "CUE_TRACE phase=avf.render_start cue_id=%s pattern=%s frames=%s",
                        cue_id,
                        cue_pattern,
                        frame_count,
                    )

                # ДИАГНОСТИКА: проверяем состояние engine и player
                try:
                    engine_running = self._engine.isRunning() if self._engine else False
                    player_playing = player_node.isPlaying() if player_node else False

                    # Check output format (only first time)
                    if frame_count > 0 and not hasattr(self, "_format_logged"):
                        try:
                            engine = self._engine
                            if engine is None:
                                raise RuntimeError("Engine unavailable")
                            out_fmt = engine.outputNode().outputFormatForBus_(0)
                            logger.info(
                                f"🔊 Output format: {out_fmt.sampleRate()}Hz, {out_fmt.channelCount()}ch"
                            )
                            self._format_logged = True
                        except Exception:
                            pass

                    if self._audio_diag_verbose:
                        logger.debug(
                            "▶️ Scheduled chunk: %s frames | src_peak=%.4f written_peak=%.4f | engine=%s, player=%s",
                            frame_count,
                            pre_peak,
                            write_peak,
                            engine_running,
                            player_playing,
                        )
                    elif (self._diag_chunk_counter % self._audio_diag_log_every) == 0:
                        logger.debug(
                            "▶️ Scheduled chunk progress: chunks=%s engine=%s player=%s",
                            self._diag_chunk_counter,
                            engine_running,
                            player_playing,
                        )
                except Exception as diag_e:
                    if self._audio_diag_verbose:
                        logger.debug(
                            f"▶️ Scheduled chunk: {frame_count} frames | diag_error={diag_e}"
                        )

            except Exception as e:
                logger.error(f"❌ Playback loop error: {e}")
                import traceback

                logger.error(traceback.format_exc())

        # Выход из цикла
        logger.info(f"🛑 _playback_loop exited. _playing={self._playing}")

    def _play_diagnostic_tone(self, engine, player_node) -> None:
        """Play a short diagnostic beep through the RUNNING engine to verify output works."""
        import math
        sr = self.config.sample_rate
        duration = 0.3  # 300ms beep
        freq = 880.0  # A5 — clearly audible
        frame_count = int(sr * duration)
        t = np.arange(frame_count, dtype=np.float32) / sr
        tone = (0.3 * np.sin(2.0 * math.pi * freq * t)).astype(np.float32)

        fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
            1, sr, self.config.channels, False
        )
        buf = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(fmt, frame_count)
        buf.setFrameLength_(frame_count)
        ptr = buf.floatChannelData()[0]
        raw = ptr.as_buffer(frame_count)
        dst = np.frombuffer(raw, dtype=np.float32, count=frame_count)
        dst[:] = tone

        peak = float(np.max(np.abs(dst)))
        out_fmt = engine.outputNode().outputFormatForBus_(0)
        logger.info(
            "🔔 [DIAG_TONE] Playing 300ms test tone: freq=%sHz, peak=%.4f, "
            "output=%sHz/%sch, engine=%s, player=%s",
            freq, peak, out_fmt.sampleRate(), out_fmt.channelCount(),
            engine.isRunning(), player_node.isPlaying(),
        )

        def _on_diag_done():
            logger.info("✅ [DIAG_TONE] Diagnostic tone buffer was consumed by engine")

        player_node.scheduleBuffer_completionHandler_(buf, _on_diag_done)
        logger.info("🔔 [DIAG_TONE] Scheduled — if you hear a beep, engine works!")

    def recreate(self) -> None:
        """Recreate engine for new output device."""
        with self._lock:
            was_playing = self._playing

            try:
                if self._player_node:
                    self._player_node.stop()
                if self._engine:
                    self._engine.stop()
            except Exception:
                pass

            self._engine = None
            self._player_node = None

        # Reset audio session cache so category is re-evaluated for new device type
        self._last_audio_session_signature = None

        # Reinitialize
        if self.initialize() and was_playing:
            self.start_playback()

        logger.info("🔄 AVFoundationPlayer recreated for new device")

    def _register_for_route_changes(self) -> None:
        """Register for audio route change notifications."""
        try:
            if AVAudioSessionRouteChangeNotification is None or NSNotificationCenter is None:
                return

            nc = NSNotificationCenter.defaultCenter()
            self._obs_token = nc.addObserverForName_object_queue_usingBlock_(
                AVAudioSessionRouteChangeNotification,
                None,
                None,
                self._on_route_change,
            )
            logger.debug("🔔 Registered for output route changes")
        except Exception as e:
            logger.warning(f"⚠️ Could not register for route changes: {e}")

    def _unregister_route_changes(self) -> None:
        """Unregister from notifications."""
        if self._obs_token:
            try:
                if NSNotificationCenter is not None:
                    NSNotificationCenter.defaultCenter().removeObserver_(self._obs_token)
            except Exception:
                pass
            self._obs_token = None

    def _on_route_change(self, notification) -> None:
        """Handle audio route change."""
        now = time.monotonic()
        with self._lock:
            if self._route_recreate_in_flight:
                logger.debug("🔄 Route change ignored: recreate already in flight")
                return
            if (now - self._last_route_recreate_ts) < self._route_recreate_min_interval_sec:
                logger.debug(
                    "🔄 Route change ignored: debounce %.3fs",
                    self._route_recreate_min_interval_sec,
                )
                return
            self._route_recreate_in_flight = True
            self._last_route_recreate_ts = now

        logger.info("🔄 Output route changed, recreating player...")

        def _recreate_with_guard() -> None:
            try:
                self.recreate()
            finally:
                with self._lock:
                    self._route_recreate_in_flight = False

        # Recreate in background thread to avoid blocking main thread (likely AppKit event loop)
        thread = threading.Thread(target=_recreate_with_guard, daemon=True, name="AVFRecreate")
        with self._lock:
            # Clean up finished threads
            self._recreate_threads = [t for t in self._recreate_threads if t.is_alive()]
            self._recreate_threads.append(thread)
        thread.start()
