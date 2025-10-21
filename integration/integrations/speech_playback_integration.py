"""
SpeechPlaybackIntegration — интеграция модуля последовательного воспроизведения с EventBus

Слушает gRPC-ответы (`grpc.response.audio`, `grpc.request_completed|failed`) и проигрывает аудио-чанки.
Поддерживает отмену через `keyboard.short_press`/`interrupt.request`.
"""

import asyncio
import logging
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any

import numpy as np

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

from modules.speech_playback.core.player import SequentialSpeechPlayer, PlayerConfig
from modules.speech_playback.core.state import PlaybackState

# ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ АУДИО
from config.unified_config_loader import unified_config

logger = logging.getLogger(__name__)


class SpeechPlaybackIntegration:
    """Интеграция SequentialSpeechPlayer с EventBus"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        
        # ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ - единый источник истины
        self.config = unified_config.get_speech_playback_config()

        self._player: Optional[SequentialSpeechPlayer] = None
        self._initialized = False
        self._running = False
        self._had_audio_for_session: Dict[Any, bool] = {}
        self._finalized_sessions: Dict[Any, bool] = {}
        self._last_audio_ts: float = 0.0
        self._silence_task: Optional[asyncio.Task] = None
        # Пометка завершённых сервером сессий (получен grpc.request_completed/failed)
        self._grpc_done_sessions: Dict[Any, bool] = {}
        # Текущая активная сессия воспроизведения (последняя)
        self._current_session_id: Optional[Any] = None
        # Пометки отменённых сессий для фильтрации поздних чанков
        self._cancelled_sessions: set = set()
        # Защита от WAV: пометка, что заголовок уже отброшен для сессии
        self._wav_header_skipped: Dict[Any, bool] = {}
        # Основной event loop, используется для публикации из фоновых потоков
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        # Флаг необходимости пересинхронизации выхода после записи
        self._needs_output_resync: bool = False
        self._pending_resync_task: Optional[asyncio.Task] = None

    async def initialize(self) -> bool:
        try:
            # Ленивая инициализация плеера с централизованной конфигурацией
            pc = PlayerConfig(
                sample_rate=self.config['sample_rate'],
                channels=self.config['channels'],
                dtype=self.config['dtype'],
                buffer_size=self.config['buffer_size'],
                max_memory_mb=self.config['max_memory_mb'],
                auto_device_selection=self.config['auto_device_selection'],
            )
            self._player = SequentialSpeechPlayer(pc)
            
            # НАСТРАИВАЕМ EventBus в SequentialSpeechPlayer для получения событий выбора устройств
            if hasattr(self._player, 'set_event_bus'):
                self._player.set_event_bus(self.event_bus)
                logger.debug("🔍 [AUDIO_DEBUG] EventBus настроен в SequentialSpeechPlayer")
            else:
                logger.warning("⚠️ [AUDIO_DEBUG] SequentialSpeechPlayer не поддерживает set_event_bus")
            
            # Коллбек завершения воспроизведения — сигнализируем в EventBus
            try:
                self._player.set_callbacks(on_playback_completed=self._on_player_completed)
            except Exception:
                pass

            # Подписки
            await self.event_bus.subscribe("grpc.response.audio", self._on_audio_chunk, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH)
            # ✅ Новый обработчик для сырых аудио данных
            await self.event_bus.subscribe("playback.raw_audio", self._on_raw_audio, EventPriority.HIGH)
            # Сигналы (короткие тоны) через EventBus
            await self.event_bus.subscribe("playback.signal", self._on_playback_signal, EventPriority.HIGH)
            await self.event_bus.subscribe("grpc.request_cancel", self._on_grpc_cancel, EventPriority.CRITICAL)
            
            # ЕДИНЫЙ канал прерываний - только playback.cancelled
            await self.event_bus.subscribe("playback.cancelled", self._on_unified_interrupt, EventPriority.CRITICAL)
            await self.event_bus.subscribe("voice.mic_closed", self._on_voice_mic_closed, EventPriority.HIGH)
            
            # Устаревшие прямые прерывания (для обратной совместимости, но перенаправляем в единый канал)
            # УБРАНО: keyboard.short_press - прерывания только при переходе в LISTENING
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
            # Сохраняем текущий event loop для последующих thread-safe публикаций
            try:
                self._loop = asyncio.get_running_loop()
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
        self._running = True
        return True

    async def stop(self) -> bool:
        try:
            if self._player:
                try:
                    self._player.stop_playback()
                    self._player.shutdown()
                except Exception:
                    pass
            self._running = False
            return True
        except Exception as e:
            await self._handle_error(e, where="speech.stop", severity="warning")
            return False

    # -------- Event Handlers --------
    async def _on_audio_chunk(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            # Фильтрация поздних чанков после отмены
            if sid is not None and (sid in self._cancelled_sessions):
                logger.debug(f"Ignoring audio chunk for cancelled sid={sid}")
                return
            if sid is not None:
                self._current_session_id = sid
            audio_bytes: bytes = data.get("bytes") or b""
            dtype: str = (data.get("dtype") or 'int16').lower()
            shape = data.get("shape") or []
            src_sample_rate: Optional[int] = data.get("sample_rate")
            src_channels: Optional[int] = data.get("channels")
            if not audio_bytes:
                logger.debug(f"🔇 Пустой аудио чанк для сессии {sid}")
                return
            
            logger.info(f"🔊 Получен аудио чанк: {len(audio_bytes)} bytes, dtype={dtype}, shape={shape}, sr={src_sample_rate}, ch={src_channels} для сессии {sid}")

            # Инициализация плеера при первом чанке
            if self._player and not self._player.state_manager.is_playing and not self._player.state_manager.is_paused:
                if not self._player.initialize():
                    await self._handle_error(Exception("player_init_failed"), where="speech.player_init")
                    return

            # Декодирование в numpy + диагностика формата
            try:
                audio_bytes_in = audio_bytes
                # Если пришёл WAV (RIFF) — на первом чанке отбросим заголовок до data
                try:
                    if sid is not None and not self._wav_header_skipped.get(sid):
                        b = audio_bytes
                        if len(b) >= 12 and b[:4] == b'RIFF' and b[8:12] == b'WAVE':
                            i = 12
                            data_offset = None
                            while i + 8 <= len(b):
                                chunk_id = b[i:i+4]
                                chunk_size = int.from_bytes(b[i+4:i+8], 'little', signed=False)
                                i += 8
                                if chunk_id == b'data':
                                    data_offset = i
                                    break
                                i += chunk_size
                            if data_offset is not None:
                                audio_bytes_in = b[data_offset:]
                                self._wav_header_skipped[sid] = True
                        else:
                            self._wav_header_skipped[sid] = True
                except Exception:
                    pass
                # Определяем dtype с учётом возможной эндИанности
                dt: Any
                if dtype in ('float32', 'float'):
                    dt = np.float32
                elif dtype in ('int16_be', 'pcm_s16be'):
                    dt = np.dtype('>i2')
                elif dtype in ('int16_le', 'pcm_s16le'):
                    dt = np.dtype('<i2')
                elif dtype in ('int16', 'short'):
                    # По умолчанию считаем little-endian, но проверим byteswap эвристикой
                    dt = np.dtype('<i2')
                else:
                    dt = np.dtype('<i2')

                arr = np.frombuffer(audio_bytes_in, dtype=dt)
                # Если тип int16 без явной эндИанности — эвристика byteswap по пику сигнала
                try:
                    if dt.kind == 'i' and dt.itemsize == 2 and dtype in ('int16', 'short'):
                        peak = float(np.max(np.abs(arr))) if arr.size else 0.0
                        swapped = arr.byteswap().newbyteorder()
                        peak_sw = float(np.max(np.abs(swapped))) if swapped.size else 0.0
                        if peak_sw > peak * 1.8:
                            arr = swapped
                except Exception:
                    pass

                # Доп. эвристика: если dtype не указан/"int16", а данные выглядят как float32 PCM
                # (длина кратна 4, а пик у int16-представления слишком мал),
                # попробуем интерпретировать как float32 и передать в модуль для конвертации.
                try:
                    if dtype in ('int16', 'short') and (len(audio_bytes_in) % 4 == 0):
                        peak_i16 = float(np.max(np.abs(arr))) if arr.size else 0.0
                        arr_f32 = np.frombuffer(audio_bytes_in, dtype=np.float32)
                        peak_f32 = float(np.max(np.abs(arr_f32))) if arr_f32.size else 0.0
                        # Считаем «правдоподобным» float32, если значения в пределах [-1,1]
                        looks_like_f32 = (peak_f32 > 0 and peak_f32 <= 1.2)
                        looks_like_bad_i16 = (peak_i16 > 0 and peak_i16 < 256)
                        if looks_like_f32 and looks_like_bad_i16:
                            # ✅ ПРАВИЛЬНО: Передаем float32 в модуль, не конвертируем здесь
                            arr = arr_f32
                            dtype = 'float32'  # для логов ниже
                except Exception:
                    pass
                if shape and len(shape) > 0:
                    try:
                        arr = arr.reshape(shape)
                    except Exception:
                        pass
                # ✅ ПРАВИЛЬНО: Не конвертируем здесь - передаем сырые данные в модуль
                # Модуль speech_playback сам выполнит конвертацию float32 → int16
                # Прочее приведение формата (ресемплинг/каналы) выполняет плеер на основе metadata

                # Диагностика: логируем основы формата (без спамма)
                try:
                    _min = float(arr.min()) if arr.size else 0.0
                    _max = float(arr.max()) if arr.size else 0.0
                    logger.info(
                        f"🔍 audio_chunk: sid={sid}, in_dtype='{(data.get('dtype') or 'auto')}', dec_dtype={arr.dtype}, shape={getattr(arr,'shape',())}, min={_min:.3f}, max={_max:.3f}, bytes={len(audio_bytes_in)}"
                    )
                except Exception:
                    pass
            except Exception as e:
                await self._handle_error(e, where="speech.decode_audio", severity="warning")
                return

            # ✅ КРИТИЧНО: start_playback ПЕРЕД add_audio_data для lazy start
            try:
                if self._player:
                    player_state = None
                    try:
                        player_state = self._player.state_manager.get_state()
                    except Exception:
                        player_state = None

                    if self._needs_output_resync or player_state not in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                        try:
                            changed = self._player.resync_output_device()
                            if changed:
                                logger.info("SpeechPlayback: выходной маршрут обновлён перед воспроизведением")
                        except Exception as sync_err:
                            logger.debug(f"SpeechPlayback: не удалось пересинхронизировать выход перед воспроизведением: {sync_err}")
                        finally:
                            self._needs_output_resync = False
                        try:
                            player_state = self._player.state_manager.get_state()
                        except Exception:
                            player_state = None

                    # Определяем текущее состояние плеера и корректно управляем
                    state = player_state or self._player.state_manager.get_state()
                    if state == PlaybackState.PAUSED:
                        # Если пауза — резюмируем
                        self._player.resume_playback()
                    elif state != PlaybackState.PLAYING:
                        # IDLE/ERROR/STOPPING — пытаемся запустить воспроизведение
                        # Повторная/идемпотентная инициализация безопасна
                        if not self._player.initialize():
                            await self._handle_error(Exception("player_init_failed"), where="speech.player_init")
                            return
                        if not self._player.start_playback():
                            await self._handle_error(Exception("start_failed"), where="speech.start_playback")
                            return
                        await self.event_bus.publish("playback.started", {"session_id": sid})

                    # Добавляем чанк ПОСЛЕ создания потока
                    self._player.add_audio_data(
                        arr,
                        priority=0,
                        metadata={
                            "session_id": sid,
                            "sample_rate": src_sample_rate,
                            "channels": src_channels,
                            "original_dtype": dtype,  # ✅ Передаем оригинальный тип для диагностики
                            "original_bytes": len(audio_bytes),  # ✅ Для диагностики
                        },
                    )

                self._had_audio_for_session[sid] = True

                # Обновляем метку времени последнего аудио (НЕ запускаем таймер тишины при каждом чанке)
                try:
                    self._last_audio_ts = asyncio.get_event_loop().time()
                    # Таймер тишины запускается только после завершения gRPC потока
                except Exception:
                    pass
            except Exception as e:
                await self._handle_error(e, where="speech.add_chunk")

        except Exception as e:
                await self._handle_error(e, where="speech.on_audio_chunk", severity="warning")

    async def _on_voice_mic_closed(self, event):
        """Фиксирует завершение записи и готовит пересинхронизацию вывода."""
        try:
            self._needs_output_resync = True

            if self._pending_resync_task and not self._pending_resync_task.done():
                self._pending_resync_task.cancel()

            async def _delayed_resync():
                try:
                    await asyncio.sleep(0.2)
                    if self._player:
                        changed = self._player.resync_output_device()
                        if changed:
                            logger.info("SpeechPlayback: выходной маршрут обновлён после закрытия микрофона")
                except asyncio.CancelledError:
                    return
                except Exception as sync_err:
                    logger.debug(f"SpeechPlayback: ошибка пересинхронизации после закрытия микрофона: {sync_err}")
                finally:
                    self._pending_resync_task = None

            self._pending_resync_task = asyncio.create_task(_delayed_resync())
        except Exception as e:
            await self._handle_error(e, where="speech.on_voice_mic_closed", severity="warning")

    async def _on_grpc_completed(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            logger.info(f"SpeechPlayback: получено grpc.request_completed для сессии {sid}")
            if sid is not None:
                self._grpc_done_sessions[sid] = True
                logger.info(f"SpeechPlayback: установлен флаг _grpc_done_sessions[{sid}] = True")
            # Запускаем таймер тишины для завершения воспроизведения
            if self._silence_task and not self._silence_task.done():
                self._silence_task.cancel()
            self._silence_task = asyncio.create_task(self._finalize_on_silence(sid, timeout=3.0))
        except Exception as e:
            await self._handle_error(e, where="speech.on_grpc_completed", severity="warning")

    async def _on_grpc_failed(self, event):
        try:
            data = (event or {}).get("data", {})
            sid = data.get("session_id")
            err = (data.get("error") or "").lower()
            if sid is not None:
                self._grpc_done_sessions[sid] = True
                if err == 'cancelled':
                    self._cancelled_sessions.add(sid)
            if self._player:
                try:
                    state = getattr(self._player.state_manager, "current_state", None)
                    if state in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                        self._player.stop_playback()
                except Exception:
                    pass
            if sid is not None:
                self._finalized_sessions[sid] = True
            if err == 'cancelled':
                logger.info("SpeechPlayback: gRPC cancelled — пропускаем playback.failed")
                return
            await self.event_bus.publish("playback.failed", {"session_id": sid, "error": data.get("error")})
            try:
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.SLEEPING,
                    "source": "speech_playback"
                })
            except Exception:
                pass
        except Exception as e:
            await self._handle_error(e, where="speech.on_grpc_failed", severity="warning")

    async def _on_unified_interrupt(self, event):
        """ЕДИНЫЙ обработчик прерывания воспроизведения"""
        try:
            data = event.get("data", {})
            source = data.get("source", "unknown")
            reason = data.get("reason", "interrupt")
            
            logger.info(f"SpeechPlayback: ЕДИНЫЙ канал прерывания, source={source}, reason={reason}")
            
            # Помечаем текущую сессию как отменённую (если есть)
            if self._current_session_id is not None:
                self._cancelled_sessions.add(self._current_session_id)
                
            # Отменяем таймер тишины, если активен
            try:
                if self._silence_task and not self._silence_task.done():
                    self._silence_task.cancel()
            except Exception:
                pass
            
            # Останавливаем воспроизведение только если реально играем/на паузе
            if self._player and self._player.state_manager.current_state in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                self._player.stop_playback()
            
            # Очищаем все сессии
            self._finalized_sessions.clear()
            
            logger.info("SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал")
            
        except Exception as e:
            await self._handle_error(e, where="speech.on_unified_interrupt", severity="warning")
    
    async def _on_legacy_interrupt(self, event):
        """Обработчик устаревших прерываний (перенаправляет в единый канал)"""
        try:
            event_type = event.get("type", "unknown")
            data = event.get("data", {})
            
            logger.info(f"SpeechPlayback: получено устаревшее прерывание {event_type}, перенаправляем в ЕДИНЫЙ канал")
            
            # Перенаправляем в единый канал прерывания
            await self.event_bus.publish("playback.cancelled", {
                "session_id": data.get("session_id"),
                "reason": "legacy_interrupt",
                "source": f"legacy_{event_type}",
                "original_event": event_type
            })
            
        except Exception as e:
            await self._handle_error(e, where="speech.on_legacy_interrupt", severity="warning")

    async def _on_raw_audio(self, event: Dict[str, Any]):
        """✅ ПРАВИЛЬНО: Приём сырых аудио данных (numpy array) для воспроизведения."""
        try:
            if not self._player:
                return
            data = (event or {}).get("data", {})
            audio_data = data.get("audio_data")
            if audio_data is None:
                return
            
            # Извлекаем метаданные
            sample_rate = data.get("sample_rate", 48000)
            channels = data.get("channels", 1)
            priority = int(data.get("priority", 10))
            pattern = data.get("pattern", "raw_audio")
            session_id = data.get("session_id")

            logger.info(
                f"🔔 playback.raw_audio: pattern={pattern}, dtype={audio_data.dtype}, shape={audio_data.shape}, "
                f"sr={sample_rate}, ch={channels}, prio={priority}"
            )

            # Проверяем sample rate — должен совпадать с плеером
            target_sr = int(self.config['sample_rate'])
            if sample_rate != target_sr:
                logger.debug(f"Raw audio SR mismatch: got={sample_rate}, player={target_sr} — skipping")
                return

            # Назначаем технический session_id для «сырых» сценариев без реальной сессии (например, welcome tone).
            raw_session = False
            if session_id is None:
                session_id = f"raw:{pattern}:{int(time.time() * 1000)}"
                raw_session = True

            self._current_session_id = session_id
            self._had_audio_for_session[session_id] = True
            if raw_session:
                self._grpc_done_sessions[session_id] = True
            else:
                self._grpc_done_sessions.setdefault(session_id, False)
            self._finalized_sessions.pop(session_id, None)
            self._cancelled_sessions.discard(session_id)

            # ✅ ПРАВИЛЬНО: Передаем numpy массив напрямую в плеер
            # Плеер сам выполнит необходимую конвертацию
            try:
                if (not self._player.state_manager.is_playing
                        and not self._player.state_manager.is_paused):
                    if not self._player.initialize():
                        await self._handle_error(Exception("player_init_failed"), where="speech.raw_audio.init")
                        return

                meta = {
                    "kind": "raw_audio",
                    "pattern": pattern,
                    "sample_rate": sample_rate,
                    "channels": channels
                }

                # ✅ КРИТИЧНО: start_playback ПЕРЕД add_audio_data для lazy start
                # Поток должен быть создан до добавления данных, чтобы _ensure_stream_started() мог его запустить
                state = self._player.state_manager.get_state()
                if state == PlaybackState.PAUSED:
                    self._player.resume_playback()
                elif state != PlaybackState.PLAYING:
                    if not self._player.start_playback():
                        await self._handle_error(Exception("start_failed"), where="speech.raw_audio.start")
                        return
                    await self.event_bus.publish("playback.started", {"session_id": session_id, "pattern": pattern})

                # Добавляем данные ПОСЛЕ создания потока
                self._player.add_audio_data(audio_data, priority=priority, metadata=meta)

                # Обновляем отметку времени последнего аудио и планируем корректный shutdown
                try:
                    self._last_audio_ts = asyncio.get_event_loop().time()
                except Exception:
                    pass

                if raw_session:
                    if self._silence_task and not self._silence_task.done():
                        self._silence_task.cancel()
                    self._silence_task = asyncio.create_task(self._finalize_on_silence(session_id, timeout=1.0))

            except Exception as e:
                await self._handle_error(e, where="speech.raw_audio", severity="warning")

        except Exception as e:
            await self._handle_error(e, where="speech.on_raw_audio", severity="warning")

    async def _on_app_shutdown(self, event):
        await self.stop()

    async def _on_playback_signal(self, event: Dict[str, Any]):
        """Приём коротких сигналов (PCM s16le mono) для немедленного воспроизведения."""
        try:
            if not self._player:
                return
            data = (event or {}).get("data", {})
            pcm = data.get("pcm")
            if not pcm:
                return
            sr = int(data.get("sample_rate", 0))
            ch = int(data.get("channels", 1))
            gain = float(data.get("gain", 1.0))
            priority = int(data.get("priority", 10))
            pattern = data.get("pattern")

            logger.info(f"🔔 playback.signal: pattern={pattern}, bytes={len(pcm)}, sr={sr}, ch={ch}, gain={gain}, prio={priority}")

            # Проверяем sample rate — должен совпадать с плеером
            target_sr = int(self.config['sample_rate'])
            if sr != target_sr:
                logger.debug(f"Signal SR mismatch: got={sr}, player={target_sr} — skipping")
                return

            # Декодируем PCM s16le mono
            try:
                arr = np.frombuffer(pcm, dtype=np.int16)
            except Exception:
                return

            # Применяем gain (осторожно с переполнением)
            try:
                if gain != 1.0:
                    a = arr.astype(np.float32) * max(0.0, min(1.0, gain))
                    a = np.clip(a, -32768.0, 32767.0).astype(np.int16)
                else:
                    a = arr
            except Exception:
                a = arr

            # ✅ КРИТИЧНО: start_playback ПЕРЕД add_audio_data для lazy start
            try:
                meta = {"kind": "signal", "pattern": pattern}

                # Запускаем воспроизведение ПЕРЕД добавлением данных
                state = self._player.state_manager.get_state()
                if state == PlaybackState.PAUSED:
                    self._player.resume_playback()
                elif state != PlaybackState.PLAYING:
                    if not self._player.initialize():
                        await self._handle_error(Exception("player_init_failed"), where="speech.signal.player_init")
                        return
                    if not self._player.start_playback():
                        await self._handle_error(Exception("start_failed"), where="speech.signal.start_playback")
                        return
                    await self.event_bus.publish("playback.started", {"signal": True})

                # Добавляем данные ПОСЛЕ создания потока
                self._player.add_audio_data(a, priority=priority, metadata=meta)
            except Exception as e:
                await self._handle_error(e, where="speech.signal.add_chunk")
        except Exception as e:
            await self._handle_error(e, where="speech.on_playback_signal", severity="warning")

    async def _on_grpc_cancel(self, event: Dict[str, Any]):
        """Отмена активного воспроизведения по запросу gRPC."""
        try:
            if not self._player:
                return
            logger.info("SpeechPlayback: получен grpc.request_cancel — очищаем буфер")
            try:
                if hasattr(self._player, "chunk_buffer") and self._player.chunk_buffer:
                    self._player.chunk_buffer.clear_all()
            except Exception:
                pass
            try:
                self._player.stop_playback()
            except Exception:
                pass
            await self.event_bus.publish("playback.cancelled", {
                "session_id": self._current_session_id,
                "source": "grpc_cancel"
            })
        except Exception as e:
            await self._handle_error(e, where="speech.on_grpc_cancel", severity="warning")

    # -------- Utils --------
    async def _finalize_on_silence(self, sid, timeout: float = 3.0):
        """Фолбэк: если после последнего чанка наступила тишина и плеер остановился — завершаем PROCESSING."""
        try:
            logger.info(f"SpeechPlayback: запуск _finalize_on_silence для сессии {sid}, timeout={timeout}s")
            start = self._last_audio_ts
            await asyncio.sleep(timeout)
            logger.info(f"SpeechPlayback: _finalize_on_silence завершен для сессии {sid}")
            
            # Если не было новых чанков
            if self._last_audio_ts == start and self._player:
                # Если буфер пуст — завершаем воспроизведение и сессию
                buf_empty = (getattr(self._player, 'chunk_buffer', None) and self._player.chunk_buffer.is_empty)
                grpc_done = self._grpc_done_sessions.get(sid, False)
                finalized = self._finalized_sessions.get(sid, False)
                
                logger.info(f"SpeechPlayback: _finalize_on_silence проверка для сессии {sid}: grpc_done={grpc_done}, buf_empty={buf_empty}, finalized={finalized}")
                
                # Финализируем ТОЛЬКО если сервер закончил поток (grpc_done), буфер пуст, и сессия ещё не финализирована
                if grpc_done and buf_empty and not finalized:
                    logger.info(f"SpeechPlayback: _finalize_on_silence завершаем сессию {sid}")
                    # Небольшая задержка для дренажа устройства
                    try:
                        drain_sec = max(0.05, min(0.25, (self.config['buffer_size'] / self.config['sample_rate']) * 4.0))
                        await asyncio.sleep(drain_sec)
                    except Exception:
                        pass
                    # Корректно останавливаем воспроизведение и завершаем
                    try:
                        if self._player:
                            self._player.stop_playback()
                    except Exception:
                        pass
                    await self.event_bus.publish("playback.completed", {"session_id": sid})
                    self._finalized_sessions[sid] = True
                    try:
                        await self.event_bus.publish("mode.request", {
                            "target": AppMode.SLEEPING,
                            "source": "speech_playback"
                        })
                    except Exception:
                        pass
                elif grpc_done and not finalized:
                    # Дополнительная проверка: если gRPC завершен, но буфер не пуст,
                    # принудительно завершаем через небольшую задержку
                    logger.info(f"SpeechPlayback: _finalize_on_silence принудительное завершение для сессии {sid} (gRPC завершен, но буфер не пуст)")
                    try:
                        # Даем время для завершения воспроизведения
                        await asyncio.sleep(0.5)
                        # Проверяем еще раз
                        buf_empty_retry = (getattr(self._player, 'chunk_buffer', None) and self._player.chunk_buffer.is_empty)
                        if buf_empty_retry or not self._player or not self._player.state_manager.is_playing:
                            logger.info(f"SpeechPlayback: _finalize_on_silence принудительно завершаем сессию {sid}")
                            try:
                                if self._player:
                                    self._player.stop_playback()
                            except Exception:
                                pass
                            await self.event_bus.publish("playback.completed", {"session_id": sid})
                            self._finalized_sessions[sid] = True
                            try:
                                await self.event_bus.publish("mode.request", {
                                    "target": AppMode.SLEEPING,
                                    "source": "speech_playback"
                                })
                            except Exception:
                                pass
                        else:
                            # Для raw-сессий (welcome, signals) просто ждем пока доиграют естественным образом
                            # НЕТ ЛИМИТОВ - играем до конца
                            logger.info(f"SpeechPlayback: ожидаем естественного завершения воспроизведения для {sid}")
                            while True:
                                await asyncio.sleep(0.5)  # проверяем каждые 500мс
                                # Проверяем завершилось ли естественным образом
                                buf_check = (getattr(self._player, 'chunk_buffer', None) and self._player.chunk_buffer.is_empty)
                                if buf_check or not self._player or not self._player.state_manager.is_playing:
                                    logger.info(f"SpeechPlayback: воспроизведение завершено естественным образом")
                                    break
                            
                            await self.event_bus.publish("playback.completed", {"session_id": sid})
                            self._finalized_sessions[sid] = True
                            try:
                                await self.event_bus.publish("mode.request", {
                                    "target": AppMode.SLEEPING,
                                    "source": "speech_playback"
                                })
                            except Exception:
                                pass
                    except Exception as e:
                        logger.error(f"SpeechPlayback: ошибка при принудительном завершении для сессии {sid}: {e}")
                else:
                    logger.info(f"SpeechPlayback: _finalize_on_silence пропускаем завершение для сессии {sid}")
        except asyncio.CancelledError:
            logger.info(f"SpeechPlayback: _finalize_on_silence отменен для сессии {sid}")
            return
        except Exception as e:
            logger.error(f"SpeechPlayback: ошибка в _finalize_on_silence для сессии {sid}: {e}")
            # Тихо игнорируем ошибки фолбэка
            pass

    def _on_player_completed(self):
        """Коллбек плеера: воспроизведение завершено (буфер пуст, поток завершён)."""
        try:
            sid = self._current_session_id
            if sid is None:
                logger.debug("SpeechPlayback: _on_player_completed вызван, но session_id=None")
                return
            
            grpc_done = self._grpc_done_sessions.get(sid, False)
            finalized = self._finalized_sessions.get(sid, False)
            
            logger.info(f"SpeechPlayback: _on_player_completed для сессии {sid}, grpc_done={grpc_done}, finalized={finalized}")
            
            # Завершаем только если сервер завершил поток и мы еще не финализировали
            if grpc_done and not finalized:
                logger.info(f"SpeechPlayback: завершаем воспроизведение для сессии {sid}")
                # На всякий случай — остановим воспроизведение, если ещё не остановлено
                try:
                    if self._player:
                        state = getattr(self._player.state_manager, "current_state", None)
                        if state in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                            self._player.stop_playback()
                except Exception:
                    pass
                loop = self._loop
                if loop and not loop.is_closed():
                    asyncio.run_coroutine_threadsafe(
                        self.event_bus.publish("playback.completed", {"session_id": sid}),
                        loop,
                    )
                self._finalized_sessions[sid] = True
                if loop and not loop.is_closed():
                    asyncio.run_coroutine_threadsafe(
                        self.event_bus.publish("mode.request", {
                            "target": AppMode.SLEEPING,
                            "source": "speech_playback"
                        }),
                        loop,
                    )
            else:
                logger.debug(f"SpeechPlayback: пропускаем завершение для сессии {sid} (grpc_done={grpc_done}, finalized={finalized})")
        except Exception as e:
            logger.error(f"SpeechPlayback: ошибка в _on_player_completed: {e}")
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
            "player": (self._player.get_status() if self._player else {}),
        }
