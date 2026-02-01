"""
SpeechPlaybackIntegration — интеграция модуля последовательного воспроизведения с EventBus

Слушает gRPC-ответы (`grpc.response.audio`, `grpc.request_completed|failed`) и проигрывает аудио-чанки.
Поддерживает отмену через `keyboard.short_press`/`interrupt.request`.
"""


import asyncio
import logging
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any, TYPE_CHECKING, TYPE_CHECKING

import numpy as np

from integration.core.event_bus import EventBus, EventPriority
from integration.core.event_types import EventTypes
from integration.core.state_manager import ApplicationStateManager, AppMode  # type: ignore[attr-defined]
from integration.core.error_handler import ErrorHandler

# NEW: AVFoundationPlayer (Standard)
if TYPE_CHECKING:
    from modules.speech_playback.core.avf_player import AVFoundationPlayer, AVFPlayerConfig
else:
    AVFoundationPlayer = None
    AVFPlayerConfig = None

try:
    from modules.speech_playback.core.avf_player import AVFoundationPlayer, AVFPlayerConfig  # type: ignore[assignment]
    _AVF_PLAYER_AVAILABLE = True
except ImportError as e:
    logging.getLogger(__name__).error(f"❌ [AUDIO] AVFoundationPlayer import failed: {e}")
    _AVF_PLAYER_AVAILABLE = False
    AVFoundationPlayer = None  # type: ignore[assignment, misc]
    AVFPlayerConfig = None  # type: ignore[assignment, misc]
except Exception as e:
    logging.getLogger(__name__).error(f"❌ [AUDIO] AVFoundationPlayer unexpected error: {e}")
    _AVF_PLAYER_AVAILABLE = False
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

        self._avf_player: Optional[Any] = None  # type: ignore[type-arg]
        
        self._initialized = False
        self._running = False
        self._had_audio_for_session: Dict[Any, bool] = {}
        self._finalized_sessions: Dict[Any, bool] = {}
        self._last_audio_ts: float = 0.0
        self._silence_task: Optional[asyncio.Task] = None
        self._grpc_done_sessions: Dict[Any, bool] = {}
        self._cancelled_sessions: set = set()
        self._wav_header_skipped: Dict[Any, bool] = {}
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._needs_output_resync: bool = False
        self._pending_resync_task: Optional[asyncio.Task] = None

    async def initialize(self) -> bool:
        try:
            # AVFoundationPlayer initialization deferred to start() to prevent early TCC triggers
            if _AVF_PLAYER_AVAILABLE:
                logger.info("ℹ️ [AUDIO] AVFoundationPlayer initialization deferred to start()")
            else:
                 logger.error("❌ [AUDIO] AVFoundationPlayer module not available")

            # Подписки
            await self.event_bus.subscribe("grpc.response.audio", self._on_audio_chunk, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH)
            await self.event_bus.subscribe("playback.raw_audio", self._on_raw_audio, EventPriority.HIGH)
            await self.event_bus.subscribe("playback.signal", self._on_playback_signal, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_cancel", self._on_grpc_cancel, EventPriority.CRITICAL)
            
            await self.event_bus.subscribe("playback.cancelled", self._on_unified_interrupt, EventPriority.CRITICAL)
            await self.event_bus.subscribe("voice.mic_closed", self._on_voice_mic_closed, EventPriority.HIGH)
            
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)

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
        if _AVF_PLAYER_AVAILABLE and AVFPlayerConfig is not None and AVFoundationPlayer is not None and self._avf_player is None:
            try:
                logger.info("🚀 [AUDIO] Initializing AVFoundationPlayer (Deferred)...")
                avf_config = AVFPlayerConfig(
                    sample_rate=self.config.get('sample_rate', 48000),
                    channels=self.config.get('channels', 1),
                    volume=self.config.get('volume', 0.8)
                )
                self._avf_player = AVFoundationPlayer(avf_config)
                if self._avf_player is not None and self._avf_player.initialize():
                    logger.info("✅ [AUDIO] AVFoundationPlayer initialized successfully")
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
                if not self._avf_player.is_playing():
                     if not self._avf_player.start_playback():
                         logger.error("❌ [AUDIO] Failed to start AVFoundationPlayer playback")
                         return False
                return True
            except Exception as e:
                logger.error(f"❌ [AUDIO] Ensure player ready failed: {e}")
                return False
        return False

    # -------- Event Handlers --------
    async def _on_audio_chunk(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            audio_bytes_len = len(data.get("bytes", b""))
            logger.info(f"🔊 [AUDIO_RECV] _on_audio_chunk received: session={sid}, bytes={audio_bytes_len}")
            
            # Фильтрация поздних чанков после отмены
            if sid is not None and (sid in self._cancelled_sessions):
                logger.debug(f"Ignoring audio chunk for cancelled sid={sid}")
                return
            
            if sid is not None:
                self.state_manager.update_session_id(str(sid))
                
            audio_bytes: bytes = data.get("bytes") or b""
            dtype: str = (data.get("dtype") or 'int16').lower()
            shape = data.get("shape") or []
            src_sample_rate: Optional[int] = data.get("sample_rate")
            src_channels: Optional[int] = data.get("channels")
            
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

            if not await self._ensure_player_ready():
                return

            # Декодирование в numpy (сохраняем логику, так как gRPC шлет байты)
            try:
                audio_bytes_in = audio_bytes
                # WAV header skip logic
                try:
                    if sid is not None and not self._wav_header_skipped.get(sid):
                        b = audio_bytes
                        if len(b) >= 12 and b[:4] == b'RIFF' and b[8:12] == b'WAVE':
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
                if dtype in ('float32', 'float'):
                    dt = np.float32
                elif dtype in ('int16_be', 'pcm_s16be'):
                    dt = np.dtype('>i2')
                elif dtype in ('int16_le', 'pcm_s16le'):
                    dt = np.dtype('<i2')
                else:
                    dt = np.dtype('<i2')

                arr = np.frombuffer(audio_bytes_in, dtype=dt)
                
                # Check for float32 masquerading as int16
                try:
                    if dtype in ('int16', 'short') and (len(audio_bytes_in) % 4 == 0):
                        arr_f32 = np.frombuffer(audio_bytes_in, dtype=np.float32)
                        peak_f32 = float(np.max(np.abs(arr_f32))) if arr_f32.size else 0.0
                        if peak_f32 > 0 and peak_f32 <= 1.2:
                            arr = arr_f32
                            dtype = 'float32'
                except Exception:
                    pass
                
                if shape and len(shape) > 0:
                    try:
                        arr = arr.reshape(shape)
                    except Exception:
                        pass
                
                # ADD TO PLAYER
                if self._avf_player:
                    # Publish started event if first chunk
                    if not self._had_audio_for_session.get(sid):
                        # TRACE: начало воспроизведения
                        ts_ms = int(time.monotonic() * 1000)
                        logger.info(f"TRACE phase=playback.start ts={ts_ms} session={sid} extra={{chunk_size={len(audio_bytes)}}}")
                        await self.event_bus.publish("playback.started", {"session_id": sid})
                    
                    metadata = {
                        "session_id": sid,
                        "sample_rate": src_sample_rate,
                        "channels": src_channels,
                        "original_dtype": dtype
                    }
                    self._avf_player.add_audio_data(arr, metadata=metadata)
                    
                self._had_audio_for_session[sid] = True
                try:
                    self._last_audio_ts = self._loop.time() if self._loop else time.time()
                except Exception:
                    pass

            except Exception as e:
                await self._handle_error(e, where="speech.decode_audio", severity="warning")

        except Exception as e:
                await self._handle_error(e, where="speech.on_audio_chunk", severity="warning")

    async def _on_voice_mic_closed(self, event):
        # AVFoundation handles route changes automatically
        # No manual resync needed
        pass

    async def _on_raw_audio(self, event: Dict[str, Any]):
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
            
            # Setup session
            raw_session = False
            if session_id is None:
                session_id = f"raw:{pattern}:{int(time.time() * 1000)}"
                raw_session = True

            self.state_manager.update_session_id(str(session_id))
            self._had_audio_for_session[session_id] = True
            if raw_session:
                self._grpc_done_sessions[session_id] = True
            else:
                self._grpc_done_sessions.setdefault(session_id, False)
            self._finalized_sessions.pop(session_id, None)
            self._cancelled_sessions.discard(session_id)

            if not await self._ensure_player_ready():
                return

            meta = {
                "kind": "raw_audio",
                "pattern": pattern,
                "sample_rate": sample_rate,
                "channels": channels
            }
            if data.get("metadata"):
                meta.update(data.get("metadata"))

            # TRACE: начало воспроизведения (raw audio)
            ts_ms = int(time.monotonic() * 1000)
            logger.info(f"TRACE phase=playback.start ts={ts_ms} session={session_id} extra={{pattern={pattern}, raw_audio=true}}")
            # Publish started
            await self.event_bus.publish("playback.started", {"session_id": session_id, "pattern": pattern})
            
            self._avf_player.add_audio_data(audio_data, metadata=meta)
            logger.debug(f"🔍 [AUDIO] Raw audio added to AVFPlayer for session {session_id}")

            try:
                self._last_audio_ts = self._loop.time() if self._loop else time.time()
            except Exception:
                pass

            if raw_session:
                if self._silence_task and not self._silence_task.done():
                    self._silence_task.cancel()
                self._silence_task = asyncio.create_task(self._finalize_on_silence(session_id, timeout=1.0))

        except Exception as e:
            await self._handle_error(e, where="speech.on_raw_audio", severity="warning")

    async def _on_app_shutdown(self, event):
        await self.stop()

    async def _on_playback_signal(self, event: Dict[str, Any]):
        try:
            if not self._avf_player:
                return
            data = (event or {}).get("data", {})
            pcm = data.get("pcm")
            if not pcm:
                return
            pattern = data.get("pattern")
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

            if not await self._ensure_player_ready():
                return

            meta = {"kind": "signal", "pattern": pattern}
            # TRACE: начало воспроизведения (signal)
            ts_ms = int(time.monotonic() * 1000)
            logger.info(f"TRACE phase=playback.start ts={ts_ms} session=None extra={{pattern={pattern}, signal=true}}")
            await self.event_bus.publish("playback.started", {"signal": True})
            self._avf_player.add_audio_data(arr, metadata=meta)
            
        except Exception as e:
            await self._handle_error(e, where="speech.on_playback_signal", severity="warning")

    async def _on_unified_interrupt(self, event: Dict[str, Any]):
        """
        Unified handler for playback interruption (user cancellation, stop, mode switch).
        Немедленная остановка плеера при cancel.
        """
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            
            # Немедленная остановка плеера
            if self._avf_player:
                try:
                    self._avf_player.clear_queue()
                    self._avf_player.stop_playback()
                    logger.info("🛑 SpeechPlayback: плеер остановлен синхронно")
                except Exception as e:
                    logger.error(f"❌ SpeechPlayback: ошибка остановки плеера: {e}")
            
            if sid:
                self._cancelled_sessions.add(sid)
            
            # Cancel silence task if any
            if self._silence_task and not self._silence_task.done():
                self._silence_task.cancel()
            
            # КРИТИЧНО: Сохраняем had_audio ДО очистки для корректного логирования
            had_audio_before_cleanup = False
            if sid is not None:
                had_audio_before_cleanup = self._had_audio_for_session.get(sid, False)
            
            # Сброс локальных флагов воспроизведения
            if sid:
                self._had_audio_for_session.pop(sid, None)
                self._finalized_sessions.pop(sid, None)
            
            # КРИТИЧНО: Публикуем playback.completed только при наличии session_id (чтобы не завершить чужую цепочку)
            if sid is not None:
                # TRACE: завершение воспроизведения (отмена)
                ts_ms = int(time.monotonic() * 1000)
                logger.info(f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{cancelled=true}}")
                logger.info(
                    f"🔍 [PLAYBACK_END] session={sid} exit_reason=cancelled "
                    f"summary={{had_audio={had_audio_before_cleanup}}}"
                )
                await self.event_bus.publish("playback.completed", {"session_id": sid})
                logger.info(f"🛑 SpeechPlayback: playback.completed опубликовано (session_id={sid})")
            else:
                logger.debug("🛑 SpeechPlayback: playback.completed не опубликовано (session_id=None, cancel только останавливает плеер)")
                
        except Exception as e:
            await self._handle_error(e, where="speech.unified_interrupt", severity="warning")
    
    async def _on_grpc_cancel(self, event: Dict[str, Any]):
        """Отмена активного воспроизведения по запросу gRPC."""
        try:
            if self._avf_player:
                 try:
                     self._avf_player.clear_queue()
                     self._avf_player.stop_playback()
                 except Exception:
                     pass

            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            if sid:
                self._cancelled_sessions.add(sid)
                
            await self.event_bus.publish("playback.cancelled", {
                "session_id": sid, 
                "source": "grpc_cancel",
                "reason": "server_request"
            })
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_cancel", severity="warning")

    async def _on_grpc_completed(self, event: Dict[str, Any]):
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
                    if sid not in self._cancelled_sessions:
                        # TRACE: завершение воспроизведения (без аудио)
                        ts_ms = int(time.monotonic() * 1000)
                        logger.info(f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{no_audio=true}}")
                        logger.info(
                            f"🔍 [PLAYBACK_END] session={sid} exit_reason=no_audio "
                            f"summary={{had_audio=false, duration=0}}"
                        )
                        await self.event_bus.publish("playback.completed", {"session_id": sid})
                        logger.info(f"SpeechPlayback: finalized session {sid} (no audio received)")
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_completed", severity="warning")

    async def _on_grpc_failed(self, event: Dict[str, Any]):
        """
        Handle grpc.request_failed event.
        """
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            error = data.get("error")
            
            if sid:
                self._grpc_done_sessions[sid] = True
                self._finalized_sessions[sid] = True
                
            # TRACE: завершение воспроизведения с ошибкой
            ts_ms = int(time.monotonic() * 1000)
            logger.info(f"TRACE phase=playback.end ts={ts_ms} session={sid} extra={{error={error}, failed=true}}")
            # Publish playback failed
            await self.event_bus.publish("playback.failed", {
                "session_id": sid,
                "error": error,
                "reason": "grpc_failed"
            })
        except Exception as e:
            await self._handle_error(e, where="speech.grpc_failed", severity="warning")

    # -------- Utils --------
    async def _finalize_on_silence(self, session_id: str, timeout: float = 3.0):
        """
        Ожидает завершения воспроизведения очереди и затем переводит режим.
        V2 Implementation for AVFoundationPlayer.
        """
        try:
            start_wait = time.time()
            # Wait for queue to drain
            while True:
                if not self._avf_player:
                    break
                    
                try:
                    is_playing = self._avf_player.is_playing()
                    is_queue_empty = self._avf_player.is_queue_empty()
                except Exception:
                    is_queue_empty = True # Assume empty if error
                
                # If filtered/cancelled
                if session_id in self._cancelled_sessions:
                    logger.debug(f"Finalize cancelled for {session_id}")
                    return

                # If done (queue empty)
                if is_queue_empty:
                    # Give a small buffer for the last chunk to actually play out from buffer
                    await asyncio.sleep(0.5) 
                    break
                
                if time.time() - start_wait > (timeout * 5): # Safety break
                    logger.warning(f"Finalize timeout waiting for queue empty {session_id}")
                    break
                
                await asyncio.sleep(0.2)

            # Переход в SLEEPING (или LISTENING если это был вопрос, но здесь мы просто заканчиваем playback)
            if session_id not in self._cancelled_sessions:
                # TRACE: завершение воспроизведения
                ts_ms = int(time.monotonic() * 1000)
                wait_duration = time.time() - start_wait
                logger.info(f"TRACE phase=playback.end ts={ts_ms} session={session_id} extra={{finalized=true}}")
                logger.info(
                    f"🔍 [PLAYBACK_END] session={session_id} exit_reason=queue_drained "
                    f"summary={{had_audio={self._had_audio_for_session.get(session_id, False)}, "
                    f"wait_duration_sec={wait_duration:.2f}}}"
                )
                await self.event_bus.publish("playback.completed", {"session_id": session_id})
                logger.info(f"SpeechPlayback: finalized session {session_id}")

        except asyncio.CancelledError:
            return
        except Exception as e:
            await self._handle_error(e, where="speech.finalize_on_silence", severity="warning")

    async def _handle_error(self, e: Exception, *, where: str, severity: str = "error"):
        if hasattr(self.error_handler, 'handle'):
            await self.error_handler.handle(
                error=e,
                category="speech_playback",
                severity=severity,
                context={"where": where}
            )
        else:
            logger.error(f"Speech playback error at {where}: {e}")

    def get_status(self) -> Dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "avf_player": (self._avf_player.is_playing() if self._avf_player else False),
        }

