"""
AVFoundationPlayer - Audio playback using AVAudioEngine (AVFoundation).

Replaces sounddevice-based SequentialSpeechPlayer.
Plays raw PCM audio data from server.
"""

from __future__ import annotations

import ctypes
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
AVAudioSessionRouteChangeNotification = getattr(_AVFoundation, "AVAudioSessionRouteChangeNotification", None)
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
        self._session_enqueue_count: dict[str, int] = {}
        
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

    def initialize(self) -> bool:
        """Initialize AVAudioEngine and player node."""
        try:
            if not (AVAudioEngine and AVAudioFormat and AVAudioPlayerNode):
                raise RuntimeError("AVFoundation audio symbols unavailable")
            
            # Activate audio session for playback
            if AVAudioSession and AVAudioSessionCategoryPlayback is not None:
                try:
                    session = AVAudioSession.sharedInstance()
                    session.setCategory_error_(AVAudioSessionCategoryPlayback, None)
                    session.setActive_error_(True, None)
                    logger.info("🔊 AVAudioSession activated for playback")
                except Exception as e:
                    logger.warning(f"⚠️ Could not activate AVAudioSession: {e}")

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
                    False # Non-interleaved
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
            logger.info(f"📊 [ADD_AUDIO] Incoming: shape={audio_data.shape}, dtype={audio_data.dtype}, size={audio_data.size}")
        
        # Diagnostic: check for silent audio on INPUT
        if audio_data.size > 0:
            peak = float(np.max(np.abs(audio_data)))
            min_val = float(np.min(audio_data))
            max_val = float(np.max(audio_data))
            if self._audio_diag_verbose:
                logger.info(f"📊 [ADD_AUDIO] INPUT peak={peak:.4f}, min={min_val:.4f}, max={max_val:.4f}")
            if peak == 0:
                if self._audio_diag_verbose:
                    logger.warning("⚠️ [ADD_AUDIO] Incoming audio is TOTALLY SILENT")
            elif peak < 0.0001:
                if self._audio_diag_verbose:
                    logger.warning(f"⚠️ [ADD_AUDIO] Incoming audio is very quiet (peak: {peak:.6f})")

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
            logger.debug(f"📊 [ADD_AUDIO] Made copy: peak after copy={float(np.max(np.abs(audio_copy))):.6f}")
        
        self._audio_queue.put({
            "id": chunk_id,
            "data": audio_copy,
            "metadata": metadata
        })
        if isinstance(metadata, dict):
            sid = metadata.get("session_id")
            kind = str(metadata.get("kind") or "grpc")
            sid_key = str(sid) if sid is not None else ""
            if sid_key:
                count = self._session_enqueue_count.get(sid_key, 0) + 1
                self._session_enqueue_count[sid_key] = count
                should_log = count <= 3 or (count % self._audio_diag_log_every) == 0
            else:
                count = 0
                should_log = kind == "signal"
            if should_log and audio_copy.size > 0:
                abs_arr = np.abs(audio_copy)
                peak_f = float(np.max(abs_arr))
                rms_f = float(np.sqrt(np.mean(np.square(abs_arr))))
                logger.info(
                    "ROOTCAUSE[AVF_ENQUEUE] kind=%s session=%s count=%s samples=%s peak_f=%.5f rms_f=%.5f queue=%s",
                    kind,
                    sid,
                    count,
                    int(audio_copy.size),
                    peak_f,
                    rms_f,
                    self._audio_queue.qsize(),
                )
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
            logger.info(f"📊 [ADD_AUDIO] Queued chunk {chunk_id}: {len(audio_data)} samples, queue_size={self._audio_queue.qsize()}")
        return chunk_id


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

                # Idempotent fast-path: avoid spawning duplicate playback threads.
                thread_alive = self._playback_thread.is_alive() if self._playback_thread else False
                if self._playing and thread_alive and engine.isRunning() and player_node.isPlaying():
                    logger.info(
                        "ROOTCAUSE[START_NOOP] queue_empty=%s buffered_sec=%.3f thread_alive=%s engine=%s player=%s",
                        self._audio_queue.empty(),
                        self.get_buffered_audio_seconds(),
                        thread_alive,
                        engine.isRunning(),
                        player_node.isPlaying(),
                    )
                    return True

                # КРИТИЧНО: Устанавливаем volume=1.0 для гарантии слышимого вывода
                player_node.setVolume_(1.0)
                mixer = engine.mainMixerNode()
                mixer.setOutputVolume_(1.0)
                logger.info(f"🔊 [AVF_PLAYER] Volume set to 1.0 at playback start (mixer and player_node)")
                
                # Ensure Audio Session is active
                if AVAudioSession:
                    try:
                        session = AVAudioSession.sharedInstance()
                        session.setActive_error_(True, None)
                        logger.debug("🔊 [AVF_PLAYER] AVAudioSession activated in start_playback")
                    except Exception as e:
                        logger.warning(f"⚠️ [AVF_PLAYER] Failed to activate AVAudioSession in start_playback: {e}")
                
                # Start engine if not running
                # Note: mainMixerNode -> outputNode connection is AUTOMATIC in AVAudioEngine
                if not engine.isRunning():
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
                
                # Start the player node
                player_node.play()
                self._playing = True
                logger.info("▶️ Playback started")
                
                # Start playback thread
                if not thread_alive:
                    self._playback_thread = threading.Thread(target=self._playback_loop, daemon=True, name="AVFPlaybackLoop")
                    self._playback_thread.start()
                    logger.info(f"▶️ Playback thread started: {self._playback_thread.name}, is_alive={self._playback_thread.is_alive()}")
                else:
                    logger.debug("▶️ Playback thread already alive, skipping thread restart")
                
                return True
            except Exception as e:
                logger.error(f"❌ Start playback failed: {e}")
                return False

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
                            device_name = output.portName() if hasattr(output, "portName") else "unknown"
                            port_type = output.portType() if hasattr(output, "portType") else "unknown"
                            logger.info(
                                f"🔊 [AVF_PLAYER] Output route snapshot: {device_name} (type: {port_type})"
                            )
                except Exception as device_e:
                    logger.debug(f"⚠️ [AVF_PLAYER] Could not get output route snapshot: {device_e}")
        except Exception as format_e:
            logger.warning(f"⚠️ [AVF_PLAYER] Could not get output snapshot: {format_e}")

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
                # Connection may be lost when engine stops
                try:
                    mixer = self._engine.mainMixerNode()
                    fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                        1,  # AVAudioPCMFormatFloat32
                        self.config.sample_rate,
                        self.config.channels,
                        False
                    )
                    self._engine.connect_to_format_(self._player_node, mixer, fmt)
                    logger.info("🔗 Reconnected playerNode to mixer")
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
            logger.debug(f"🔍 is_playing check: _playing={self._playing}, thread_alive={thread_alive}, engine_running={engine_running}, player_playing={player_playing}")
        # Consider active only when there is queued/scheduled audio.
        return self._playing and thread_alive and (queue_non_empty or buffered_sec > 0.02)

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
            False # Non-interleaved
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
                self._diag_chunk_counter += 1
                
                # CRITICAL DIAGNOSTIC: Check data immediately after extracting from queue
                if self._audio_diag_verbose and audio_data.size > 0:
                    queue_peak = float(np.max(np.abs(audio_data)))
                    first_10 = audio_data[:min(10, len(audio_data))]
                    logger.info(f"📊 [QUEUE_EXTRACT] peak={queue_peak:.6f}, first_10={first_10[:5]}")
                    if queue_peak == 0:
                        logger.error("❌ [QUEUE_EXTRACT] Audio data is ZERO after extraction from queue!")
                
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
                if self._audio_diag_verbose:
                    logger.debug(f"📊 Pre-copy peak (FULL): {pre_peak:.4f}, samples={frame_count}")
                
                # Copy float32 samples into AVAudioPCMBuffer channel-0 memory.
                # Single owner for this conversion is AVFoundationPlayer.
                copy_ok = False
                audio_contiguous = np.ascontiguousarray(audio_data, dtype=np.float32)
                try:
                    buffer_ptr = getattr(ptr, "__pyobjc_object__", None)
                    if isinstance(buffer_ptr, int) and buffer_ptr != 0:
                        ctypes.memmove(
                            buffer_ptr,
                            audio_contiguous.ctypes.data,
                            frame_count * ctypes.sizeof(ctypes.c_float),
                        )
                        copy_ok = True
                        if self._audio_diag_verbose:
                            logger.debug(f"📊 memmove completed: {frame_count} samples")
                except Exception as copy_e:
                    if self._audio_diag_verbose:
                        logger.warning(f"⚠️ memmove copy failed: {copy_e}")

                if not copy_ok:
                    try:
                        for i in range(frame_count):
                            ptr[i] = float(audio_contiguous[i])
                        copy_ok = True
                        if self._audio_diag_verbose:
                            logger.debug(f"📊 indexed copy completed: {frame_count} samples")
                    except Exception as copy_e:
                        logger.error(f"❌ Failed to copy samples into AVAudioPCMBuffer: {copy_e}")
                        logger.error("❌ AUDIO WILL BE SILENT - unable to write to AVAudioPCMBuffer")
                        continue
                
                # Ensure engine is running before scheduling buffer
                if not self._ensure_engine_running():
                    logger.warning("⚠️ Engine not running, waiting before retry...")
                    time.sleep(0.2)  # Prevent tight loop when engine is down
                    continue

                player_node = self._player_node
                if player_node is None:
                    logger.error("❌ Cannot schedule buffer - player node unavailable")
                    continue
                
                # Schedule buffer for playback
                player_node.scheduleBuffer_completionHandler_(buffer, None)
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
                    
                    # Check buffer amplitude - use middle of buffer since beginning may be silent
                    mid = frame_count // 2
                    start = max(0, mid - 50)
                    end = min(frame_count, mid + 50)
                    peak = max(abs(ptr[i]) for i in range(start, end)) if end > start else 0.0
                    
                    # Check output format (only first time)
                    if frame_count > 0 and not hasattr(self, '_format_logged'):
                        try:
                            engine = self._engine
                            if engine is None:
                                raise RuntimeError("Engine unavailable")
                            out_fmt = engine.outputNode().outputFormatForBus_(0)
                            logger.info(f"🔊 Output format: {out_fmt.sampleRate()}Hz, {out_fmt.channelCount()}ch")
                            self._format_logged = True
                        except Exception:
                            pass
                    
                    if self._audio_diag_verbose:
                        logger.debug(f"▶️ Scheduled chunk: {frame_count} frames | peak={peak:.4f} | engine={engine_running}, player={player_playing}")
                    elif (self._diag_chunk_counter % self._audio_diag_log_every) == 0:
                        logger.debug(
                            "▶️ Scheduled chunk progress: chunks=%s engine=%s player=%s",
                            self._diag_chunk_counter,
                            engine_running,
                            player_playing,
                        )
                    if cue_id is not None or (self._diag_chunk_counter % self._audio_diag_log_every) == 0:
                        logger.info(
                            "ROOTCAUSE[AVF_RENDER] cue_id=%s pattern=%s frames=%s mid_peak_f=%.5f engine=%s player=%s",
                            cue_id,
                            cue_pattern,
                            frame_count,
                            float(peak),
                            engine_running,
                            player_playing,
                        )
                except Exception as diag_e:
                    if self._audio_diag_verbose:
                        logger.debug(f"▶️ Scheduled chunk: {frame_count} frames | diag_error={diag_e}")
                
            except Exception as e:
                logger.error(f"❌ Playback loop error: {e}")
                import traceback
                logger.error(traceback.format_exc())
        
        # Выход из цикла
        logger.info(f"🛑 _playback_loop exited. _playing={self._playing}")

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
        logger.info("🔄 Output route changed, recreating player...")
        # Recreate in background thread to avoid blocking main thread (likely AppKit event loop)
        thread = threading.Thread(target=self.recreate, daemon=True, name="AVFRecreate")
        with self._lock:
            # Clean up finished threads
            self._recreate_threads = [t for t in self._recreate_threads if t.is_alive()]
            self._recreate_threads.append(thread)
        thread.start()
