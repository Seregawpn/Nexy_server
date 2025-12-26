"""
AVFoundationPlayer - Audio playback using AVAudioEngine (AVFoundation).

Replaces sounddevice-based SequentialSpeechPlayer.
Plays raw PCM audio data from server.
"""

from __future__ import annotations

import threading
import logging
import queue
from typing import Optional, Dict, Any
from dataclasses import dataclass

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class AVFPlayerConfig:
    """Configuration for AVFoundation player."""
    sample_rate: int = 24000
    channels: int = 1
    buffer_size: int = 512
    volume: float = 0.8


class AVFoundationPlayer:
    """
    Audio player using AVAudioEngine (AVFoundation).
    
    Features:
    - Plays raw PCM audio data (int16 or float32)
    - Device-aware (follows system default)
    - Queue-based for sequential playback
    - Recreates engine on device change
    """
    
    def __init__(self, config: Optional[AVFPlayerConfig] = None):
        self.config = config or AVFPlayerConfig()
        
        self._engine = None
        self._player_node = None
        self._lock = threading.Lock()
        self._audio_queue: queue.Queue = queue.Queue()
        self._playing = False
        self._initialized = False
        
        # Device monitoring
        self._current_output_device: Optional[str] = None
        self._obs_token = None
        
        # Thread tracking
        self._playback_thread: Optional[threading.Thread] = None

    def initialize(self) -> bool:
        """Initialize AVAudioEngine and player node."""
        try:
            from AVFoundation import (
                AVAudioEngine, AVAudioPlayerNode, AVAudioFormat,
                AVAudioSession, AVAudioSessionCategoryPlayback
            )
            
            # Activate audio session for playback
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
                
                # Set volume
                mixer.setOutputVolume_(self.config.volume)
                
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

        logger.info("🛑 AVFoundationPlayer shutdown")

    def add_audio_data(self, audio_data: np.ndarray, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Add audio data to playback queue.
        
        Args:
            audio_data: NumPy array (int16 or float32)
            metadata: Optional metadata
            
        Returns:
            Chunk ID
        """
        # Diagnostic: check for silent audio
        if audio_data.size > 0:
            peak = float(np.max(np.abs(audio_data)))
            if peak == 0:
                logger.debug("⚠️ Added totally silent audio chunk")
            elif peak < 0.0001:
                logger.debug(f"⚠️ Added very quiet audio chunk (peak: {peak:.6f})")

        chunk_id = f"chunk_{id(audio_data)}"
        
        # Convert int16 to float32 if needed
        if audio_data.dtype == np.int16:
            audio_float = audio_data.astype(np.float32) / 32768.0
        else:
            audio_float = audio_data.astype(np.float32)
        
        self._audio_queue.put({
            "id": chunk_id,
            "data": audio_float,
            "metadata": metadata
        })
        
        logger.debug(f"📊 Added chunk {chunk_id}: {len(audio_data)} samples")
        return chunk_id

    def start_playback(self) -> bool:
        """Start playback."""
        if not self._initialized:
            logger.error("❌ Player not initialized")
            return False
        
        with self._lock:
            try:
                # Set volumes to maximum for player and mixer
                self._player_node.setVolume_(1.0)
                mixer = self._engine.mainMixerNode()
                mixer.setOutputVolume_(1.0)
                
                # Start engine if not running
                # Note: mainMixerNode -> outputNode connection is AUTOMATIC in AVAudioEngine
                if not self._engine.isRunning():
                    success, error = self._engine.startAndReturnError_(None)
                    if success:
                        logger.info("🔊 AVAudioEngine started successfully")
                    else:
                        logger.error(f"❌ Failed to start AVAudioEngine: {error}")
                        return False
                else:
                    logger.debug("🔊 AVAudioEngine already running")
                
                # Start the player node
                self._player_node.play()
                self._playing = True
                logger.info("▶️ Playback started")
                
                # Start playback thread
                self._playback_thread = threading.Thread(target=self._playback_loop, daemon=True, name="AVFPlaybackLoop")
                self._playback_thread.start()
                logger.info(f"▶️ Playback thread started: {self._playback_thread.name}, is_alive={self._playback_thread.is_alive()}")
                
                return True
            except Exception as e:
                logger.error(f"❌ Start playback failed: {e}")
                return False

    def _ensure_engine_running(self) -> bool:
        """
        Ensure AVAudioEngine is running.
        Restarts the engine if it stopped (e.g., due to route change or interruption).
        Also reconnects playerNode to mixer if needed.
        
        Returns:
            True if engine is running, False otherwise
        """
        from AVFoundation import AVAudioFormat
        
        if not self._engine:
            return False
            
        try:
            if not self._engine.isRunning():
                logger.warning("⚠️ AVAudioEngine stopped, attempting to restart...")
                
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
                    
                    # Set volumes
                    self._player_node.setVolume_(1.0)
                    mixer = self._engine.mainMixerNode()
                    mixer.setOutputVolume_(1.0)
                    
                    # Ensure player node is playing
                    if self._player_node and not self._player_node.isPlaying():
                        self._player_node.play()
                        logger.info("▶️ PlayerNode restarted")
                    return True
                else:
                    logger.error(f"❌ Failed to restart AVAudioEngine: {error}")
                    return False
            return True
        except Exception as e:
            logger.error(f"❌ Error ensuring engine running: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False

    def stop_playback(self) -> None:
        """Stop playback."""
        with self._lock:
            self._playing = False
            try:
                if self._player_node:
                    self._player_node.stop()
            except Exception as e:
                logger.warning(f"⚠️ Stop error: {e}")
            logger.info("⏹️ Playback stopped")

    def is_playing(self) -> bool:
        """Check if currently playing."""
        thread_alive = self._playback_thread.is_alive() if self._playback_thread else False
        engine_running = self._engine.isRunning() if self._engine else False
        player_playing = False
        try:
            player_playing = self._player_node.isPlaying() if self._player_node else False
        except Exception:
            pass
        logger.debug(f"🔍 is_playing check: _playing={self._playing}, thread_alive={thread_alive}, engine_running={engine_running}, player_playing={player_playing}")
        # Возвращаем True только если флаг True И поток жив
        return self._playing and thread_alive

    def is_queue_empty(self) -> bool:
        """Check if audio queue is empty."""
        return self._audio_queue.empty()

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
        from AVFoundation import AVAudioPCMBuffer, AVAudioFormat
        
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
                break
            
            try:
                audio_data = chunk["data"]
                frame_count = len(audio_data)
                
                if frame_count == 0:
                    continue

                # Create buffer
                buffer = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(fmt, frame_count)
                buffer.setFrameLength_(frame_count)
                
                # Get the pointer to the first channel's data
                float_channel_data = buffer.floatChannelData()
                if float_channel_data is None:
                    logger.error("❌ floatChannelData() returned None")
                    continue
                
                ptr = float_channel_data[0]
                
                # SAFE: Element-wise copy - guaranteed to work with PyObjC
                # This is slower but doesn't cause segfaults
                for i in range(frame_count):
                    ptr[i] = float(audio_data[i])
                
                # Ensure engine is running before scheduling buffer
                if not self._ensure_engine_running():
                    logger.error("❌ Cannot schedule buffer - engine not running")
                    continue
                
                # Schedule buffer for playback
                self._player_node.scheduleBuffer_completionHandler_(buffer, None)
                
                # ДИАГНОСТИКА: проверяем состояние engine и player
                try:
                    engine_running = self._engine.isRunning() if self._engine else False
                    player_playing = self._player_node.isPlaying() if self._player_node else False
                    
                    # Check buffer amplitude
                    peak = max(abs(ptr[i]) for i in range(min(100, frame_count)))
                    
                    # Check output format (only first time)
                    if frame_count > 0 and not hasattr(self, '_format_logged'):
                        try:
                            out_fmt = self._engine.outputNode().outputFormatForBus_(0)
                            logger.info(f"🔊 Output format: {out_fmt.sampleRate()}Hz, {out_fmt.channelCount()}ch")
                            self._format_logged = True
                        except Exception:
                            pass
                    
                    logger.debug(f"▶️ Scheduled chunk: {frame_count} frames | peak={peak:.4f} | engine={engine_running}, player={player_playing}")
                except Exception as diag_e:
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
            from Foundation import NSNotificationCenter
            from AVFoundation import AVAudioSessionRouteChangeNotification
            
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
                from Foundation import NSNotificationCenter
                NSNotificationCenter.defaultCenter().removeObserver_(self._obs_token)
            except Exception:
                pass
            self._obs_token = None

    def _on_route_change(self, notification) -> None:
        """Handle audio route change."""
        logger.info("🔄 Output route changed, recreating player...")
        # Recreate in background thread to avoid blocking
        thread = threading.Thread(target=self.recreate, daemon=True)
        thread.start()
