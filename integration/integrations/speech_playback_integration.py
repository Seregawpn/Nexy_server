"""
SpeechPlaybackIntegration — интеграция модуля последовательного воспроизведения с EventBus

Слушает gRPC-ответы (`grpc.response.audio`, `grpc.request_completed|failed`) и проигрывает аудио-чанки.
Поддерживает отмену через `keyboard.short_press`/`interrupt.request`.
"""

import asyncio
import json
import logging
import threading
import time
from dataclasses import dataclass
from typing import Optional, Dict, Any, List

import numpy as np

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

from modules.speech_playback.core.player import SequentialSpeechPlayer, PlayerConfig
from modules.speech_playback.core.state import PlaybackState

# ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ АУДИО
from config.unified_config_loader import unified_config

# ✅ AVFoundation аудиосистема (Этап 3-4)
# ✅ КРИТИЧНО: Логируем попытку импорта ДО создания logger
import logging
_logger_temp = logging.getLogger(__name__)
_logger_temp.info("🔍 [AVF] Попытка импорта AVFAudioEngine из modules.audio_avf...")

try:
    from modules.audio_avf import AVFAudioEngine
    from config.audio_config import AudioConfig
    from config.unified_config_loader import UnifiedConfigLoader
    _AVF_AVAILABLE = True
    _logger_temp.info("✅ [AVF] AVFAudioEngine импортирован успешно")
except ImportError as e:
    _logger_temp.error(f"❌ [AVF] Не удалось импортировать AVFAudioEngine: {e}")
    _logger_temp.exception("❌ [AVF] Детали ImportError при импорте AVFAudioEngine")
    _AVF_AVAILABLE = False
    AVFAudioEngine = None
except Exception as e:
    _logger_temp.error(f"❌ [AVF] Неожиданная ошибка при импорте AVFAudioEngine: {e}")
    _logger_temp.exception("❌ [AVF] Детали исключения при импорте AVFAudioEngine")
    _AVF_AVAILABLE = False
    AVFAudioEngine = None

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
        # ✅ ИСПРАВЛЕНИЕ: Таймеры тишины для каждой сессии отдельно (предотвращение race conditions)
        self._silence_tasks: Dict[Any, asyncio.Task] = {}
        # Пометка завершённых сервером сессий (получен grpc.request_completed/failed)
        self._grpc_done_sessions: Dict[Any, bool] = {}
        # КРИТИЧНО: _current_session_id удален - используем только state_manager.get_current_session_id()
        # Пометки отменённых сессий для фильтрации поздних чанков
        self._cancelled_sessions: set = set()
        # Защита от WAV: пометка, что заголовок уже отброшен для сессии
        self._wav_header_skipped: Dict[Any, bool] = {}
        # Основной event loop, используется для публикации из фоновых потоков
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        # Флаг необходимости пересинхронизации выхода после записи
        self._needs_output_resync: bool = False
        self._pending_resync_task: Optional[asyncio.Task] = None
        
        # ✅ AVFoundation аудиосистема (Этап 3-4)
        self._avf_engine: Optional[AVFAudioEngine] = None
        
        # ✅ НОВОЕ: Отслеживание активных чанков для предотвращения одновременного воспроизведения
        # Ключ: session_id, значение: информация о текущем воспроизводимом чанке
        self._active_chunks: Dict[Any, Dict[str, Any]] = {}
        # ✅ КРИТИЧНО: Lock для синхронизации доступа к _active_chunks (предотвращение race conditions)
        self._active_chunks_lock = asyncio.Lock()
        self._use_avf: bool = False
        self._output_stream_manager = None  # Legacy, для обратной совместимости
        
        # ✅ AVFoundation буферизация (Этап 4): Буфер для чанков и очередь воспроизведения
        self._avf_chunk_buffer: Dict[str, List[Dict[str, Any]]] = {}  # session_id -> список чанков
        self._avf_playback_task: Optional[asyncio.Task] = None  # Фоновый процесс воспроизведения
        self._avf_is_playing: Dict[str, bool] = {}  # session_id -> is_playing
        
        # ✅ ОПТИМИЗАЦИЯ: Event для мгновенного пробуждения worker вместо polling
        self._chunk_completed_event: asyncio.Event = asyncio.Event()
        self._new_chunk_event: asyncio.Event = asyncio.Event()

    def _ensure_avf_engine(self, reason: str = "unknown") -> bool:
        """Создаёт AVFAudioEngine, если он ещё не создан."""
        if self._avf_engine is not None:
            return True

        if not _AVF_AVAILABLE:
            logger.error("❌ [AVF] Попытка создать AVFAudioEngine, но модуль недоступен (reason=%s)", reason)
            return False

        try:
            loader = UnifiedConfigLoader()
            audio_config = loader.get_audio_config_object()
            self._avf_engine = AVFAudioEngine(audio_config, event_bus=self.event_bus)
            self._use_avf = True
            logger.info("✅ [AVF] Создан локальный AVFAudioEngine (reason=%s)", reason)

            loop = getattr(self.event_bus, "_loop", None)
            if loop and loop.is_running():
                try:
                    self._avf_engine.attach_event_loop(loop)
                    logger.info("✅ [AVF] Event loop прикреплён к локальному AVFAudioEngine (reason=%s)", reason)
                except Exception:
                    logger.warning("⚠️ [AVF] Не удалось прикрепить loop к AVFAudioEngine (reason=%s)", reason, exc_info=True)
            else:
                logger.warning("⚠️ [AVF] Event loop недоступен при создании AVFAudioEngine (reason=%s)", reason)
            return True
        except Exception:
            logger.error("❌ [AVF] Ошибка создания локального AVFAudioEngine (reason=%s)", reason, exc_info=True)
            self._avf_engine = None
            return False

    async def initialize(self, output_stream_manager=None, avf_engine=None) -> bool:
        """
        Инициализация интеграции
        
        Args:
            output_stream_manager: OutputStreamManager из AudioSystemIntegration (legacy, опционально)
            avf_engine: AVFAudioEngine из AudioSystemIntegration (новая аудиосистема, опционально)
        """
        try:
            # ✅ ДИАГНОСТИКА: Логируем параметры инициализации
            logger.info(f"🔍 [AVF] SpeechPlaybackIntegration.initialize вызван: avf_engine={avf_engine is not None}, _AVF_AVAILABLE={_AVF_AVAILABLE}")
            
            # ✅ AVFoundation аудиосистема (Этап 3-4): Можно вызывать повторно для установки avf_engine
            if avf_engine is not None and _AVF_AVAILABLE:
                self._avf_engine = avf_engine
                self._use_avf = True
                logger.info(f"✅ [AVF] SpeechPlaybackIntegration получил AVFAudioEngine: {type(avf_engine).__name__}")
            else:
                if avf_engine is None:
                    logger.warning("⚠️ [AVF] SpeechPlaybackIntegration.initialize вызван с avf_engine=None")
                if not _AVF_AVAILABLE:
                    logger.error("❌ [AVF] AVFoundation недоступен (импорт не удался)")
                try:
                    loader = UnifiedConfigLoader()
                    avf_config = loader.get_audio_avf_config()
                    avf_enabled = avf_config.get("avf", {}).get("enabled", False)
                    ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
                    import os
                    disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"

                    self._use_avf = avf_enabled and not ks_avf_enabled and not disable_avf_env

                    if self._use_avf:
                        logger.info("✅ [AVF] SpeechPlaybackIntegration использует AVFAudioEngine (feature flag включен)")
                    else:
                        reason = []
                        if not avf_enabled:
                            reason.append("feature flag disabled")
                        if ks_avf_enabled:
                            reason.append("kill-switch enabled")
                        if disable_avf_env:
                            reason.append("env variable disabled")
                        logger.warning(
                            f"⚠️ [AVF] Feature flag отключен: {', '.join(reason)}, но AVF будет использован принудительно (PortAudio удалён)"
                        )
                        self._use_avf = True
                        logger.info("✅ [AVF] AVF принудительно включен (PortAudio недоступен)")

                    if self._avf_engine is None:
                        logger.warning("⚠️ [AVF] AVFAudioEngine не передан, создаём локальный экземпляр")
                        # ✅ КРИТИЧНО: Создаём AVFAudioEngine локально, если он не передан
                        if _AVF_AVAILABLE:
                            if self._ensure_avf_engine(reason="initialize_fallback"):
                                logger.info("✅ [AVF] Локальный AVFAudioEngine создан успешно")
                            else:
                                logger.error("❌ [AVF] Не удалось создать локальный AVFAudioEngine")
                        else:
                            logger.error("❌ [AVF] AVFoundation недоступен (импорт не удался)")
                except Exception as e:
                    logger.warning(f"⚠️ [AVF] Ошибка проверки feature flag: {e}")
                    if self._avf_engine is None:
                        logger.warning("⚠️ [AVF] AVFAudioEngine не передан, создаём локальный экземпляр (fallback)")
                        # ✅ КРИТИЧНО: Создаём AVFAudioEngine локально, если он не передан
                        if _AVF_AVAILABLE:
                            if self._ensure_avf_engine(reason="initialize_fallback_exception"):
                                logger.info("✅ [AVF] Локальный AVFAudioEngine создан успешно (после исключения)")
                            else:
                                logger.error("❌ [AVF] Не удалось создать локальный AVFAudioEngine (после исключения)")
                        else:
                            logger.error("❌ [AVF] AVFoundation недоступен (импорт не удался)")
            
            # ✅ Legacy: Получаем OutputStreamManager из AudioSystemIntegration (для обратной совместимости)
            if output_stream_manager is not None:
                self._output_stream_manager = output_stream_manager
            
            # ✅ КРИТИЧНО: Legacy player больше не создаётся - PortAudio удалён
            # Если AVF доступен, используем его принудительно
            logger.info(f"🔍 [AVF] Финальная проверка: _avf_engine={self._avf_engine is not None}, _use_avf={self._use_avf}")
            
            if self._avf_engine is not None:
                logger.info("✅ [AVF] AVFAudioEngine доступен, legacy player НЕ создаётся (PortAudio удалён)")
                self._player = None
            else:
                # AVF недоступен - это критическая ошибка, так как PortAudio тоже удалён
                logger.error("❌ [AVF] AVFAudioEngine недоступен, а PortAudio удалён. Воспроизведение невозможно.")
                logger.error(f"❌ [AVF] Диагностика: avf_engine параметр={avf_engine is not None}, _AVF_AVAILABLE={_AVF_AVAILABLE}")
                self._player = None
                # Не создаём legacy player, так как он не может работать без PortAudio
            if output_stream_manager:
                self._output_stream_manager = output_stream_manager
                logger.info("✅ [AUDIO_SYSTEM] OutputStreamManager передан в SpeechPlaybackIntegration")
            
            # ✅ Устанавливаем callback для уведомления о переключении на встроенное устройство
            async def on_device_fallback(from_device: str, to_device: str, reason: str):
                """Callback для уведомления о переключении на встроенное устройство"""
                try:
                    logger.error(
                        f"⚠️ [AUDIO_SYSTEM] ⚠️ КРИТИЧНО: Bluetooth устройство '{from_device}' не отвечает — "
                        f"переключились на встроенное устройство '{to_device}'"
                    )
                    # Публикуем событие для других интеграций (например, tray)
                    await self.event_bus.publish("audio.device.fallback", {
                        "from_device": from_device,
                        "to_device": to_device,
                        "reason": reason
                    })
                except Exception as e:
                    logger.error(f"❌ [AUDIO_SYSTEM] Ошибка обработки device_fallback callback: {e}", exc_info=True)
            
            # Устанавливаем callback (синхронная обертка для async callback)
            def sync_callback(from_device: str, to_device: str, reason: str):
                """Синхронная обертка для async callback"""
                try:
                    loop = self._loop
                    if loop and loop.is_running():
                        asyncio.run_coroutine_threadsafe(
                            on_device_fallback(from_device, to_device, reason),
                            loop
                        )
                except Exception as e:
                    logger.debug(f"⚠️ [AUDIO_SYSTEM] Ошибка вызова async callback: {e}")
            
            # ✅ AVFoundation аудиосистема (Этап 4): Настраиваем legacy player ТОЛЬКО если он создан
            if self._player is not None:
                self._player._on_device_fallback = sync_callback
                logger.debug("✅ [AUDIO_SYSTEM] Callback device_fallback установлен в player")
                
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
            else:
                logger.debug("✅ [AVF] Legacy player не создан, пропускаем настройку callbacks")

            # Подписки (только если ещё не инициализирован, чтобы избежать дублирования)
            if not self._initialized:
                await self.event_bus.subscribe("grpc.response.audio", self._on_audio_chunk, EventPriority.HIGH)
                await self.event_bus.subscribe("grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH)
                await self.event_bus.subscribe("grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH)
                # ✅ Новый обработчик для сырых аудио данных
                await self.event_bus.subscribe("playback.raw_audio", self._on_raw_audio, EventPriority.HIGH)
                # Сигналы (короткие тоны) через EventBus
                await self.event_bus.subscribe("playback.signal", self._on_playback_signal, EventPriority.HIGH)
                await self.event_bus.subscribe("grpc.request_cancel", self._on_grpc_cancel, EventPriority.CRITICAL)
                
                # ✅ НОВАЯ АУДИОСИСТЕМА: Подписка на события смены устройств
                await self.event_bus.subscribe("audio.device.output_changed", self._on_output_device_changed, EventPriority.HIGH)
                await self.event_bus.subscribe("audio.device.both_changed", self._on_output_device_changed, EventPriority.HIGH)
                await self.event_bus.subscribe("audio.device.fallback", self._on_audio_device_fallback, EventPriority.HIGH)
                
                # ✅ КРИТИЧНО: Подписка на события завершения воспроизведения от AVFAudioEngine
                await self.event_bus.subscribe("audio.playback.completed", self._on_avf_playback_completed, EventPriority.HIGH)
                await self.event_bus.subscribe("audio.playback.interrupted", self._on_avf_playback_interrupted, EventPriority.HIGH)
                await self.event_bus.subscribe("audio.device.output_resync_required", self._on_avf_output_resync_required, EventPriority.HIGH)
                
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
            # КРИТИЧНО: Используем state_manager для синхронизации session_id (единый источник истины)
            if sid is not None:
                # Синхронизируем session_id с state_manager БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(str(sid))
            audio_bytes: bytes = data.get("bytes") or b""
            dtype: str = (data.get("dtype") or 'int16').lower()
            shape = data.get("shape") or []
            # ✅ ИСПРАВЛЕНИЕ: gRPC данные всегда 48kHz, если не указано иное
            # Это критично для правильного ресемплинга на BT устройства (24kHz)
            src_sample_rate: Optional[int] = data.get("sample_rate") or 48000
            src_channels: Optional[int] = data.get("channels") or 1
            if not audio_bytes:
                logger.debug(f"🔇 Пустой аудио чанк для сессии {sid}")
                return
            
            logger.info(f"🔊 Получен аудио чанк: {len(audio_bytes)} bytes, dtype={dtype}, shape={shape}, sr={src_sample_rate}, ch={src_channels} для сессии {sid}")

            # ✅ КРИТИЧНО: Принудительно используем AVFAudioEngine если он доступен
            # PortAudio (sounddevice) удалён, поэтому legacy fallback не может работать
            if self._avf_engine is not None:
                try:
                    # Декодируем в numpy для буферизации
                    # (используем ту же логику что и для legacy player)
                    audio_bytes_in = audio_bytes
                    # WAV header skip (если нужно)
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
                    
                    # Определяем dtype
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
                    
                    # Конвертируем в int16 если нужно
                    if arr.dtype != np.int16:
                        if arr.dtype == np.float32:
                            arr = (arr * 32767).astype(np.int16)
                        else:
                            arr = arr.astype(np.int16)
                    
                    # Добавляем в буфер
                    if sid not in self._avf_chunk_buffer:
                        self._avf_chunk_buffer[sid] = []
                        self._avf_is_playing[sid] = False
                    
                    self._avf_chunk_buffer[sid].append({
                        "data": arr,
                        "sample_rate": src_sample_rate,
                        "channels": src_channels,
                        "timestamp": time.time()
                    })
                    
                    logger.debug(f"✅ [AVF] Чанк добавлен в буфер для сессии {sid}: {len(arr)} samples, буфер={len(self._avf_chunk_buffer[sid])} чанков")
                    
                    # Запускаем фоновый процесс воспроизведения если ещё не запущен
                    if self._avf_playback_task is None or self._avf_playback_task.done():
                        self._avf_playback_task = asyncio.create_task(self._avf_playback_worker())
                        logger.info("✅ [AVF] Фоновый процесс воспроизведения запущен")
                    
                    # ✅ ОПТИМИЗАЦИЯ: Пробуждаем worker мгновенно вместо polling
                    self._new_chunk_event.set()
                    
                    # Публикуем событие начала воспроизведения (если первый чанк)
                    if not self._avf_is_playing.get(sid, False):
                        self._avf_is_playing[sid] = True
                        await self.event_bus.publish("playback.started", {"session_id": sid})
                    
                    # Обновляем timestamp последнего аудио
                    self._last_audio_ts = asyncio.get_event_loop().time()
                    
                    return  # Пропускаем legacy player
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка буферизации чанка: {e}", exc_info=True)
                    # ✅ КРИТИЧНО: НЕ используем legacy fallback - PortAudio удалён
                    logger.error("❌ [AVF] Legacy fallback недоступен (PortAudio удалён). Воспроизведение невозможно.")
                    await self._handle_error(Exception("avf_buffering_failed_no_fallback"), where="speech.grpc_response.avf")
                    return
            
            # ✅ КРИТИЧНО: Legacy player больше не используется - PortAudio удалён
            # Если AVF недоступен, воспроизведение невозможно
            if self._avf_engine is None:
                logger.error("❌ [AVF] AVFAudioEngine недоступен, а PortAudio удалён. Воспроизведение невозможно.")
                await self._handle_error(Exception("no_audio_engine_available"), where="speech.grpc_response.no_engine")
                return
            
            # Legacy: Используем старый player (только если AVF недоступен, но это не должно происходить)
            if not self._player:
                logger.error("❌ [LEGACY] SequentialSpeechPlayer недоступен (PortAudio удалён). Воспроизведение невозможно.")
                await self._handle_error(Exception("legacy_player_unavailable"), where="speech.grpc_response.legacy")
                return
            
            # Legacy: Инициализация плеера при первом чанке (не должно выполняться)
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

                    # ✅ КРИТИЧНО: Синхронизируем output device ДО добавления данных
                    # Это гарантирует, что self.config.sample_rate обновлен до правильного значения (24kHz для BT)
                    # и ресемплинг в add_audio_data будет выполнен с правильными параметрами
                    if self._needs_output_resync or player_state not in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                        try:
                            changed = self._player.resync_output_device()
                            if changed:
                                logger.info("SpeechPlayback: выходной маршрут обновлён перед воспроизведением")
                                # ✅ После обновления sample_rate убеждаемся, что metadata содержит актуальный sample_rate
                                # Если src_sample_rate не был передан, используем обновленный sample_rate из конфига
                                if src_sample_rate is None or src_sample_rate == 48000:
                                    # Используем актуальный sample_rate из конфига плеера для правильного ресемплинга
                                    actual_player_sr = getattr(self._player.config, 'sample_rate', 48000)
                                    if actual_player_sr != 48000:
                                        logger.debug(f"🔄 Обновляем src_sample_rate: {src_sample_rate} → {actual_player_sr} (из конфига плеера)")
                                        src_sample_rate = actual_player_sr
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
            # ✅ ИСПРАВЛЕНИЕ: Запускаем таймер тишины с увеличенным таймаутом (10 секунд вместо 3)
            # Это предотвращает преждевременное завершение для длинных аудио
            # ✅ ИСПРАВЛЕНИЕ: Таймер для каждой сессии отдельно (предотвращение race conditions)
            if sid in self._silence_tasks:
                old_task = self._silence_tasks[sid]
                if not old_task.done():
                    old_task.cancel()
                    logger.debug(f"SpeechPlayback: отменён предыдущий _finalize_on_silence для сессии {sid}")
            # ✅ УВЕЛИЧЕН ТАЙМАУТ: 10 секунд вместо 3 для длинных аудио
            self._silence_tasks[sid] = asyncio.create_task(self._finalize_on_silence(sid, timeout=10.0))
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
            
            # ✅ КРИТИЧНО: Ищем session_id из state_manager или из AVF буферов
            # state_manager может сбросить session_id при grpc.request_completed, но воспроизведение ещё активно
            current_session_id = self.state_manager.get_current_session_id()
            
            # ✅ ИСПРАВЛЕНИЕ: Если session_id не найден в state_manager, ищем в AVF буферах
            if current_session_id is None:
                # Ищем активные сессии в AVF буферах
                active_sessions = [
                    sid for sid, chunks in self._avf_chunk_buffer.items()
                    if len(chunks) > 0 or self._avf_is_playing.get(sid, False)
                ]
                if active_sessions:
                    current_session_id = active_sessions[0]
                    logger.info(f"SpeechPlayback: session_id не найден в state_manager, использован из AVF буфера: {current_session_id}")
            
            # Помечаем текущую сессию как отменённую (если есть)
            if current_session_id is not None:
                self._cancelled_sessions.add(current_session_id)
                logger.info(f"SpeechPlayback: сессия {current_session_id} помечена как отменённая")
            
            # ✅ ИСПРАВЛЕНИЕ: Отменяем таймеры тишины для всех сессий при прерывании
            try:
                for task_sid, task in list(self._silence_tasks.items()):
                    if not task.done():
                        task.cancel()
                    self._silence_tasks.pop(task_sid, None)
            except Exception:
                pass
            
            # ✅ КРИТИЧНО: Останавливаем AVF engine и очищаем AVF буфер при прерывании
            if self._avf_engine is not None:
                try:
                    # Останавливаем воспроизведение
                    logger.info(f"SpeechPlayback: останавливаем AVF engine при прерывании")
                    await self._avf_engine.stop_output()
                    
                    # Очищаем буферы для текущей сессии
                    if current_session_id is not None:
                        self._avf_chunk_buffer.pop(current_session_id, None)
                        self._avf_is_playing.pop(current_session_id, None)
                        logger.info(f"SpeechPlayback: очищен AVF буфер для сессии {current_session_id}")
                    
                    # Очищаем активные чанки
                    async with self._active_chunks_lock:
                        self._active_chunks.clear()
                        logger.info(f"SpeechPlayback: очищены активные чанки")
                    
                    # Очищаем все буферы (на случай, если session_id не найден или есть другие сессии)
                    self._avf_chunk_buffer.clear()
                    self._avf_is_playing.clear()
                    logger.info(f"SpeechPlayback: очищены все AVF буферы")
                except Exception as e:
                    logger.error(f"SpeechPlayback: ошибка остановки AVF engine при прерывании: {e}", exc_info=True)
            
            # КРИТИЧНО: Останавливаем воспроизведение, если legacy плеер существует
            # Проверяем состояние, но останавливаем даже если состояние не обновлено (кроме IDLE/STOPPED)
            if self._player:
                try:
                    current_state = self._player.state_manager.current_state
                    if current_state in (PlaybackState.PLAYING, PlaybackState.PAUSED):
                        logger.info(f"SpeechPlayback: останавливаем воспроизведение (state={current_state})")
                        self._player.stop_playback()
                    elif current_state not in (PlaybackState.IDLE, PlaybackState.STOPPING):
                        # КРИТИЧНО: Останавливаем даже если состояние не PLAYING/PAUSED (может быть не обновлено)
                        # Но пропускаем IDLE и STOPPING, чтобы избежать избыточных вызовов
                        logger.warning(f"SpeechPlayback: принудительно останавливаем воспроизведение (state={current_state}, может быть не обновлено)")
                        self._player.stop_playback()
                    else:
                        logger.debug(f"SpeechPlayback: воспроизведение уже остановлено (state={current_state})")
                except Exception as e:
                    # КРИТИЧНО: Останавливаем даже при ошибке проверки состояния (безопасно, метод идемпотентный)
                    logger.warning(f"SpeechPlayback: ошибка проверки состояния, принудительно останавливаем: {e}")
                    try:
                        self._player.stop_playback()
                    except Exception:
                        pass
            
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
            logger.info(f"🔔 [AVF] _on_raw_audio вызван! event keys: {list(event.keys()) if event else 'None'}")
            data = (event or {}).get("data", {})
            logger.debug(f"🔍 [AVF] data keys: {list(data.keys()) if data else 'None'}")
            audio_data = data.get("audio_data")
            if audio_data is None:
                logger.warning("⚠️ [AVF] audio_data is None в _on_raw_audio")
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
            
            # ✅ ДИАГНОСТИКА: Логируем состояние движков перед выбором
            logger.debug(
                f"🔍 [AVF] Диагностика движков: _avf_engine={self._avf_engine is not None}, "
                f"_use_avf={self._use_avf}, _player={self._player is not None}"
            )

            if self._avf_engine is None:
                logger.warning("⚠️ [AVF] AVFAudioEngine недоступен перед воспроизведением, пытаемся создать локально")
                logger.info(f"🔍 [AVF] _AVF_AVAILABLE={_AVF_AVAILABLE}, вызываем _ensure_avf_engine(reason='on_raw_audio_fallback')")
                # ✅ КРИТИЧНО: Создаём AVFAudioEngine при первом использовании, если он не был создан в initialize()
                if _AVF_AVAILABLE:
                    logger.info("🔍 [AVF] _AVF_AVAILABLE=True, вызываем _ensure_avf_engine()")
                    if self._ensure_avf_engine(reason="on_raw_audio_fallback"):
                        logger.info("✅ [AVF] Локальный AVFAudioEngine создан при первом использовании")
                        # ✅ КРИТИЧНО: Проверяем, что _avf_engine действительно создан
                        if self._avf_engine is None:
                            logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: _ensure_avf_engine() вернул True, но _avf_engine всё ещё None")
                            await self._handle_error(RuntimeError("avf_engine_unavailable"), where="speech.play_audio")
                            return
                    else:
                        logger.error("❌ [AVF] Не удалось создать локальный AVFAudioEngine при первом использовании (_ensure_avf_engine вернул False)")
                        await self._handle_error(RuntimeError("avf_engine_unavailable"), where="speech.play_audio")
                        return
                else:
                    logger.error("❌ [AVF] AVFoundation недоступен (импорт не удался, _AVF_AVAILABLE=False)")
                    await self._handle_error(RuntimeError("avf_engine_unavailable"), where="speech.play_audio")
                    return

            # ✅ КРИТИЧНО: Принудительно используем AVFAudioEngine если он доступен
            # PortAudio (sounddevice) удалён, поэтому legacy fallback не может работать
            # Если AVF доступен, используем его независимо от feature flag
            if self._avf_engine is not None:
                # Проверяем feature flag только для логирования
                if not self._use_avf:
                    logger.warning("⚠️ [AVF] AVFAudioEngine доступен, но feature flag отключен. Используем AVF принудительно (PortAudio удалён)")
                try:
                    # Конвертируем numpy array в bytes
                    if isinstance(audio_data, np.ndarray):
                        # Убеждаемся, что это int16
                        if audio_data.dtype != np.int16:
                            if audio_data.dtype == np.float32:
                                # Конвертируем float32 [-1, 1] в int16
                                audio_data = (audio_data * 32767).astype(np.int16)
                            else:
                                audio_data = audio_data.astype(np.int16)
                        audio_bytes = audio_data.tobytes()
                    else:
                        audio_bytes = audio_data
                    
                    logger.info(f"✅ [AVF] Воспроизведение через AVFAudioEngine: {len(audio_bytes)} bytes, {sample_rate}Hz, {channels}ch")
                    
                    # Воспроизводим через AVFAudioEngine
                    success = await self._avf_engine.play_audio(audio_bytes, sample_rate, channels)
                    
                    if success:
                        # Публикуем события для совместимости
                        if session_id:
                            self.state_manager.update_session_id(str(session_id))
                        await self.event_bus.publish("playback.started", {"session_id": session_id, "pattern": pattern})
                        
                        # ✅ КРИТИЧНО: Для welcome_message и других raw-сессий добавляем чанк в _active_chunks
                        # Это необходимо для корректной обработки completion callback в _on_avf_playback_completed
                        if pattern in ("welcome_message", "signal") and session_id:
                            import time
                            async with self._active_chunks_lock:
                                self._active_chunks[str(session_id)] = {
                                    "chunk": {"data": audio_data, "sample_rate": sample_rate, "channels": channels},
                                    "start_time": time.time(),
                                    "duration_sec": len(audio_bytes) / (sample_rate * channels * 2),
                                    "session_id": str(session_id)
                                }
                                logger.debug(f"✅ [AVF] Добавлен чанк в _active_chunks для сессии {session_id} (pattern={pattern})")
                        
                        # ✅ ИСПРАВЛЕНИЕ: Проверяем состояние воспроизведения вместо простого ожидания
                        # Это необходимо для обнаружения прерывания из-за конфигурационных событий (например, переключение режимов AirPods)
                        duration_sec = len(audio_bytes) / (sample_rate * channels * 2)  # 2 bytes per sample (int16)
                        
                        # ✅ КРИТИЧНО: Ждём завершения воспроизведения с проверкой состояния
                        start_time = time.time()
                        start_wait = time.time()  # Для логов
                        check_interval = 0.1  # Проверяем каждые 100ms
                        max_wait_time = duration_sec + 0.5  # Максимальное время ожидания с запасом
                        playback_interrupted = False
                        
                        while (time.time() - start_time) < max_wait_time:
                            await asyncio.sleep(check_interval)
                            
                            # ✅ КРИТИЧНО: Проверяем, не было ли воспроизведение прервано
                            if not self._avf_engine.is_output_active:
                                # Воспроизведение остановлено (возможно, из-за конфигурационного события)
                                elapsed = time.time() - start_time
                                logger.warning(
                                    f"⚠️ [AVF] Воспроизведение прервано через {elapsed:.2f}s "
                                    f"(ожидалось {duration_sec:.2f}s) - возможно, из-за конфигурационного события"
                                )
                                playback_interrupted = True
                                
                                # ✅ КРИТИЧНО: Используем точный расчёт через get_samples_played() из AVFAudioEngine
                                # Это гарантирует корректный расчёт остатка даже при прерываниях и переподключениях
                                bytes_per_sample = 2 * max(1, channels)
                                samples_played = self._avf_engine.get_samples_played()
                                bytes_played = samples_played * bytes_per_sample
                                
                                # ✅ КРИТИЧНО: Проверяем что bytes_played не превышает размер буфера
                                if bytes_played > len(audio_bytes):
                                    logger.warning(
                                        f"⚠️ [AVF] samples_played ({samples_played}) даёт bytes_played ({bytes_played}) "
                                        f"больше размера буфера ({len(audio_bytes)}), используем размер буфера"
                                    )
                                    bytes_played = len(audio_bytes)
                                
                                remaining_bytes = audio_bytes[bytes_played:]
                                
                                logger.debug(
                                    f"🔍 [AVF] Расчёт остатка: samples_played={samples_played}, "
                                    f"bytes_played={bytes_played}, remaining={len(remaining_bytes)} bytes"
                                )
                                
                                if len(remaining_bytes) > 0:
                                    logger.info(
                                        f"🔄 [AVF] Пытаемся возобновить воспроизведение: "
                                        f"{len(remaining_bytes)} bytes из {len(audio_bytes)}"
                                    )
                                    
                                    # Небольшая задержка для завершения переподключения
                                    await asyncio.sleep(0.2)
                                    
                                    # Пытаемся воспроизвести оставшиеся данные
                                    retry_success = await self._avf_engine.play_audio(remaining_bytes, sample_rate, channels)
                                    
                                    if retry_success:
                                        logger.info("✅ [AVF] Воспроизведение возобновлено после прерывания")
                                        # Ждём завершения оставшейся части
                                        remaining_duration = len(remaining_bytes) / (sample_rate * channels * 2)
                                        await asyncio.sleep(remaining_duration + 0.1)
                                        
                                        # ✅ КРИТИЧНО: Проверяем состояние после ожидания завершения возобновлённого воспроизведения
                                        # Проверяем, завершилось ли воспроизведение
                                        is_output_active_after_resume = self._avf_engine.is_output_active if self._avf_engine else False
                                        engine_running_after_resume = self._avf_engine._engine.isRunning() if (self._avf_engine and self._avf_engine._engine) else False
                                        
                                        if not is_output_active_after_resume or not engine_running_after_resume:
                                            # Воспроизведение завершилось - публикуем completed
                                            logger.info("✅ [AVF] Воспроизведение завершилось после возобновления, публикуем playback.completed")
                                            await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                            logger.info(f"✅ [AVF] Воспроизведение завершено после возобновления: {pattern}")
                                            return
                                        else:
                                            # Воспроизведение всё ещё активно - ждём ещё немного или принудительно завершаем
                                            logger.warning(f"⚠️ [AVF] Воспроизведение всё ещё активно после ожидания {remaining_duration:.2f}s, ждём дополнительно 0.5s")
                                            await asyncio.sleep(0.5)
                                            
                                            # Финальная проверка
                                            is_output_active_final = self._avf_engine.is_output_active if self._avf_engine else False
                                            engine_running_final = self._avf_engine._engine.isRunning() if (self._avf_engine and self._avf_engine._engine) else False
                                            
                                            if not is_output_active_final or not engine_running_final:
                                                logger.info("✅ [AVF] Воспроизведение завершилось после дополнительного ожидания, публикуем playback.completed")
                                                await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                                logger.info(f"✅ [AVF] Воспроизведение завершено после возобновления: {pattern}")
                                                return
                                            else:
                                                # Воспроизведение всё ещё активно - принудительно завершаем (completion callback не пришёл)
                                                logger.warning(f"⚠️ [AVF] Воспроизведение всё ещё активно после дополнительного ожидания, принудительно публикуем playback.completed (completion callback не пришёл)")
                                                await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                                logger.info(f"✅ [AVF] Воспроизведение завершено принудительно после возобновления: {pattern}")
                                                return
                                    else:
                                        logger.error("❌ [AVF] Не удалось возобновить воспроизведение после прерывания")
                                        # Публикуем событие о прерывании
                                        await self.event_bus.publish("playback.interrupted", {
                                            "session_id": session_id,
                                            "pattern": pattern,
                                            "reason": "device_configuration_change",
                                            "elapsed_sec": elapsed,
                                            "expected_duration_sec": duration_sec,
                                            "retry_failed": True
                                        })
                                        return
                                else:
                                    # Данные уже проиграны, просто логируем
                                    logger.debug("🔍 [AVF] Все данные уже проиграны до прерывания")
                                
                                break
                            
                            # Проверяем, завершилось ли воспроизведение естественным образом
                            if (time.time() - start_time) >= duration_sec:
                                # Воспроизведение должно было завершиться
                                break
                        
                        # ✅ КРИТИЧНО: Финальная проверка перед публикацией completed
                        if not playback_interrupted:
                            # Дополнительная проверка: убеждаемся, что воспроизведение действительно завершилось
                            if self._avf_engine.is_output_active:
                                logger.warning(
                                    f"⚠️ [AVF] Воспроизведение всё ещё активно после ожидания {duration_sec:.2f}s"
                                )
                                # ✅ ИСПРАВЛЕНИЕ: Проверяем, не остановлен ли engine системой
                                # Если engine остановлен, но состояние RUNNING - это означает, что буфер потерян
                                # В этом случае публикуем playback.completed, чтобы не зависнуть
                                if self._avf_engine._engine and not self._avf_engine._engine.isRunning():
                                    logger.warning(
                                        f"⚠️ [AVF] Engine остановлен системой, но состояние RUNNING. "
                                        f"Буфер потерян, публикуем playback.completed для предотвращения зависания"
                                    )
                                    await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                    logger.info(f"✅ [AVF] Воспроизведение завершено (принудительно, engine остановлен): {pattern}")
                                    return
                                # Не публикуем completed, так как воспроизведение не завершилось
                                return
                            
                            await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                            logger.info(f"✅ [AVF] Воспроизведение завершено: {pattern}")
                        else:
                            # Воспроизведение было прервано, но мы его возобновили
                            # Проверяем финальное состояние
                            # ✅ ИСПРАВЛЕНИЕ: Проверяем не только is_output_active, но и реальное состояние engine
                            is_output_active = self._avf_engine.is_output_active
                            engine_running = self._avf_engine._engine.isRunning() if self._avf_engine._engine else False
                            
                            if not is_output_active or not engine_running:
                                # Воспроизведение не активно или engine остановлен - публикуем completed
                                if not engine_running:
                                    logger.warning(f"⚠️ [AVF] Engine остановлен после возобновления, публикуем playback.completed")
                                await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                logger.info(f"✅ [AVF] Воспроизведение завершено после возобновления: {pattern}")
                            else:
                                logger.warning(f"⚠️ [AVF] Воспроизведение всё ещё активно после возобновления (is_output_active={is_output_active}, engine_running={engine_running})")
                                
                                # ✅ ИСПРАВЛЕНИЕ: Если воспроизведение всё ещё активно после возобновления,
                                # но completion callback не пришёл - принудительно публикуем playback.completed
                                # Это предотвращает зависание приветствия
                                logger.warning(f"⚠️ [AVF] Принудительно публикуем playback.completed (completion callback не пришёл после возобновления)")
                                await self.event_bus.publish("playback.completed", {"session_id": session_id, "pattern": pattern})
                                logger.info(f"✅ [AVF] Воспроизведение завершено принудительно: {pattern}")
                    else:
                        logger.error(f"❌ [AVF] Не удалось начать воспроизведение: {pattern}")
                        await self._handle_error(Exception("avf_playback_failed"), where="speech.raw_audio.avf")
                    
                    return
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка воспроизведения через AVFAudioEngine: {e}", exc_info=True)
                    # ✅ КРИТИЧНО: НЕ используем legacy fallback - PortAudio удалён
                    logger.error("❌ [AVF] Legacy fallback недоступен (PortAudio удалён). Воспроизведение невозможно.")
                    await self._handle_error(Exception("avf_playback_failed_no_fallback"), where="speech.raw_audio.avf")
                    return
            
            # ✅ КРИТИЧНО: Legacy player больше не используется - PortAudio удалён
            # Если AVF недоступен, воспроизведение невозможно
            if self._avf_engine is None:
                logger.error("❌ [AVF] AVFAudioEngine недоступен, а PortAudio удалён. Воспроизведение невозможно.")
                await self._handle_error(Exception("no_audio_engine_available"), where="speech.raw_audio.no_engine")
                return
            
            # ✅ КРИТИЧНО: Legacy код удалён - PortAudio недоступен
            # Если код дошёл до этой точки, значит AVF путь не сработал, но AVF доступен
            # Это не должно происходить, но на всякий случай логируем ошибку
            logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: AVF путь не сработал, но AVF доступен. Это не должно происходить.")
            await self._handle_error(Exception("avf_path_failed_unexpectedly"), where="speech.raw_audio.avf_unexpected_failure")
            return

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
            # КРИТИЧНО: Используем state_manager для получения session_id
            sid = self.state_manager.get_current_session_id()
            logger.info(f"SpeechPlayback: получен grpc.request_cancel для сессии {sid} — очищаем буфер")
            
            # ✅ AVFoundation аудиосистема (Этап 4): Очищаем AVFoundation буфер
            if self._avf_engine is not None:
                try:
                    if sid:
                        self._avf_chunk_buffer.pop(sid, None)
                        self._avf_is_playing.pop(sid, None)
                    await self._avf_engine.stop_output()
                except Exception:
                    pass
            
            # Legacy: Очищаем legacy player буфер
            if self._player:
                try:
                    if hasattr(self._player, "chunk_buffer") and self._player.chunk_buffer:
                        self._player.chunk_buffer.clear_all()
                except Exception:
                    pass
                try:
                    self._player.stop_playback()
                except Exception:
                    pass
            # КРИТИЧНО: Используем state_manager для получения session_id (единый источник истины)
            current_session_id = self.state_manager.get_current_session_id()
            await self.event_bus.publish("playback.cancelled", {
                "session_id": current_session_id,
                "source": "grpc_cancel"
            })
        except Exception as e:
            await self._handle_error(e, where="speech.on_grpc_cancel", severity="warning")

    # -------- Utils --------
    async def _finalize_on_silence(self, sid, timeout: float = 10.0):
        """Фолбэк: если после последнего чанка наступила тишина и плеер остановился — завершаем PROCESSING.
        
        ✅ ИСПРАВЛЕНИЕ: Увеличен таймаут до 10 секунд для длинных аудио.
        ✅ ИСПРАВЛЕНИЕ: Проверяет is_output_active перед принудительной остановкой.
        ✅ ИСПРАВЛЕНИЕ: Отменяется при получении completion callback.
        """
        try:
            logger.info(f"SpeechPlayback: запуск _finalize_on_silence для сессии {sid}, timeout={timeout}s")
            start = self._last_audio_ts
            await asyncio.sleep(timeout)
            logger.info(f"SpeechPlayback: _finalize_on_silence завершен для сессии {sid}")
            
            # ✅ КРИТИЧНО: Проверяем, не была ли сессия уже завершена через completion callback
            if self._finalized_sessions.get(sid, False):
                logger.info(f"SpeechPlayback: _finalize_on_silence пропускаем завершение для сессии {sid} (уже финализирована через completion callback)")
                return
            
            # Если не было новых чанков
            # ✅ КРИТИЧНО: Проверяем AVFoundation буфер (принудительно используем AVF)
            if self._avf_engine is not None:
                buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0
                grpc_done = self._grpc_done_sessions.get(sid, False)
                finalized = self._finalized_sessions.get(sid, False)
                # ✅ КРИТИЧНО: Проверяем, активно ли воспроизведение
                is_output_active = self._avf_engine.is_output_active
            elif self._player:
                # Legacy: Проверяем legacy player буфер
                buf_empty = (getattr(self._player, 'chunk_buffer', None) and self._player.chunk_buffer.is_empty)
                grpc_done = self._grpc_done_sessions.get(sid, False)
                finalized = self._finalized_sessions.get(sid, False)
                is_output_active = False  # Legacy player не имеет is_output_active
            else:
                # Нет ни AVFoundation, ни legacy player
                return
                
            logger.info(f"SpeechPlayback: _finalize_on_silence проверка для сессии {sid}: grpc_done={grpc_done}, buf_empty={buf_empty}, finalized={finalized}, is_output_active={is_output_active}")
            
            # ✅ ИСПРАВЛЕНИЕ: Финализируем ТОЛЬКО если сервер закончил поток (grpc_done), буфер пуст,
            # сессия ещё не финализирована, И воспроизведение не активно, И нет активных чанков
            # ✅ КРИТИЧНО: Проверяем _active_chunks для этой сессии
            has_active_chunk = False
            async with self._active_chunks_lock:
                has_active_chunk = sid in self._active_chunks
            
            if grpc_done and buf_empty and not finalized and not is_output_active and not has_active_chunk:
                logger.info(f"SpeechPlayback: _finalize_on_silence завершаем сессию {sid} (воспроизведение не активно, буфер пуст)")
                # ✅ ИСПРАВЛЕНИЕ: Не останавливаем воспроизведение принудительно, так как оно уже не активно
                # Просто публикуем playback.completed
                self._avf_is_playing[sid] = False
                await self.event_bus.publish("playback.completed", {"session_id": sid})
                self._finalized_sessions[sid] = True
                # ✅ ИСПРАВЛЕНИЕ: Очищаем таймер для этой сессии
                self._silence_tasks.pop(sid, None)
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
                    
                    # ✅ ИСПРАВЛЕНИЕ: Для AVF проверяем is_output_active и _active_chunks
                    if self._avf_engine is not None:
                        # Проверяем, активно ли воспроизведение и есть ли активные чанки
                        is_output_active_retry = self._avf_engine.is_output_active
                        has_active_chunk_retry = False
                        async with self._active_chunks_lock:
                            has_active_chunk_retry = sid in self._active_chunks
                        
                        # ✅ КРИТИЧНО: Не завершаем, если воспроизведение активно или есть активные чанки
                        # ✅ ИСПРАВЛЕНИЕ: Перезапускаем таймер, чтобы не потерять fallback защиту
                        if is_output_active_retry or has_active_chunk_retry:
                            logger.info(f"SpeechPlayback: _finalize_on_silence пропускаем завершение для сессии {sid} (воспроизведение активно или есть активные чанки), перезапускаем таймер")
                            # ✅ КРИТИЧНО: Отменяем текущий таймер и создаём новый с тем же таймаутом для продолжения fallback защиты
                            # Это гарантирует, что если completion callback не придёт, fallback всё равно сработает
                            if sid in self._silence_tasks:
                                old_task = self._silence_tasks[sid]
                                if not old_task.done():
                                    old_task.cancel()
                                self._silence_tasks.pop(sid, None)
                            self._silence_tasks[sid] = asyncio.create_task(self._finalize_on_silence(sid, timeout=10.0))
                            return
                        
                        # Буфер должен быть пуст для AVF
                        buf_empty_retry = len(self._avf_chunk_buffer.get(sid, [])) == 0
                        if buf_empty_retry:
                            logger.info(f"SpeechPlayback: _finalize_on_silence завершаем сессию {sid} (AVF: буфер пуст, воспроизведение не активно)")
                            self._avf_is_playing[sid] = False
                            await self.event_bus.publish("playback.completed", {"session_id": sid})
                            self._finalized_sessions[sid] = True
                            self._silence_tasks.pop(sid, None)
                            try:
                                await self.event_bus.publish("mode.request", {
                                    "target": AppMode.SLEEPING,
                                    "source": "speech_playback"
                                })
                            except Exception:
                                pass
                        return
                    
                    # Legacy: Проверяем legacy player буфер
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
                        self._silence_tasks.pop(sid, None)
                        try:
                            await self.event_bus.publish("mode.request", {
                                "target": AppMode.SLEEPING,
                                "source": "speech_playback"
                            })
                        except Exception:
                            pass
                except Exception as e:
                    logger.error(f"SpeechPlayback: ошибка при принудительном завершении для сессии {sid}: {e}")
                    # ✅ ИСПРАВЛЕНИЕ: Удаляем таймер при ошибке
                    self._silence_tasks.pop(sid, None)
            else:
                logger.info(f"SpeechPlayback: _finalize_on_silence пропускаем завершение для сессии {sid}")
        except asyncio.CancelledError:
            logger.info(f"SpeechPlayback: _finalize_on_silence отменен для сессии {sid}")
            return
        except Exception as e:
            logger.error(f"SpeechPlayback: ошибка в _finalize_on_silence для сессии {sid}: {e}")
            # Тихо игнорируем ошибки фолбэка
            pass

    async def _avf_playback_worker(self):
        """✅ AVFoundation аудиосистема (Этап 4): Фоновый процесс воспроизведения чанков из буфера"""
        logger.info("✅ [AVF] Фоновый процесс воспроизведения запущен")
        
        while True:
            try:
                # Ищем сессию с чанками в буфере
                active_sessions = [
                    sid for sid, chunks in self._avf_chunk_buffer.items()
                    if len(chunks) > 0 and self._avf_is_playing.get(sid, False)
                ]
                
                if not active_sessions:
                    # ✅ ОПТИМИЗАЦИЯ: Ждём событие вместо polling (0.1s)
                    # Событие будет установлено при добавлении нового чанка или завершении воспроизведения
                    self._new_chunk_event.clear()
                    try:
                        await asyncio.wait_for(self._new_chunk_event.wait(), timeout=0.5)
                    except asyncio.TimeoutError:
                        pass  # Timeout - просто проверяем снова
                    continue
                
                # Обрабатываем первую активную сессию
                sid = active_sessions[0]
                
                # ✅ КРИТИЧНО: Проверяем, не была ли сессия отменена при прерывании
                if sid in self._cancelled_sessions:
                    logger.info(f"SpeechPlayback: сессия {sid} отменена, пропускаем обработку чанков")
                    # Очищаем буфер для отменённой сессии
                    self._avf_chunk_buffer.pop(sid, None)
                    self._avf_is_playing.pop(sid, None)
                    continue
                
                chunks = self._avf_chunk_buffer[sid]
                
                if len(chunks) == 0:
                    continue
                
                # ✅ КРИТИЧНО: Проверяем, не воспроизводится ли уже чанк для этой сессии
                # Если чанк активен - ждём completion callback
                # ✅ ИСПРАВЛЕНИЕ: Используем Lock для синхронизации доступа
                async with self._active_chunks_lock:
                    if sid in self._active_chunks:
                        # ✅ ОПТИМИЗАЦИЯ: Ждём completion callback через Event вместо polling
                        pass  # Выходим из lock и ждём ниже
                    else:
                        pass  # Можем продолжить
                
                # Проверяем ещё раз после выхода из lock
                if sid in self._active_chunks:
                    # Чанк воспроизводится, ждём completion callback через Event
                    self._chunk_completed_event.clear()
                    try:
                        await asyncio.wait_for(self._chunk_completed_event.wait(), timeout=0.5)
                    except asyncio.TimeoutError:
                        pass  # Timeout - просто проверяем снова
                    continue
                
                # ✅ ИСПРАВЛЕНИЕ: Воспроизводим чанки ПОСЛЕДОВАТЕЛЬНО, а не все сразу
                # Это предотвращает ошибку "Воспроизведение уже активно"
                chunk = chunks.pop(0)  # Берём первый чанк
                audio_data = chunk["data"]
                sample_rate = chunk["sample_rate"]
                channels = chunk["channels"]
                audio_bytes = audio_data.tobytes()
                
                # ✅ ИСПРАВЛЕНИЕ: Проверяем активные чанки перед принудительной остановкой
                # Если есть активный чанк для этой сессии - ждём completion callback вместо принудительной остановки
                async with self._active_chunks_lock:
                    if sid in self._active_chunks:
                        # Чанк уже воспроизводится, ждём completion callback через Event
                        logger.debug(f"🔍 [AVF] Чанк уже воспроизводится для сессии {sid}, ждём completion callback")
                
                if sid in self._active_chunks:
                    self._chunk_completed_event.clear()
                    try:
                        await asyncio.wait_for(self._chunk_completed_event.wait(), timeout=0.5)
                    except asyncio.TimeoutError:
                        pass
                    continue
                
                # ✅ КРИТИЧНО: Проверяем и принудительно сбрасываем состояние перед новым чанком
                # ✅ ИСПРАВЛЕНИЕ: Проверяем ВСЕ активные чанки, а не только для текущего sid
                # Это предотвращает прерывание воспроизведения другой сессии
                if self._avf_engine.is_output_active:
                    # Проверяем, есть ли активные чанки для ЛЮБОЙ сессии
                    has_any_active_chunks = False
                    async with self._active_chunks_lock:
                        has_any_active_chunks = len(self._active_chunks) > 0
                    
                    if has_any_active_chunks:
                        # Есть активные чанки для другой сессии - ждём их завершения
                        logger.debug(f"🔍 [AVF] Воспроизведение активно для другой сессии, ждём завершения перед новым чанком для сессии {sid}")
                        await asyncio.sleep(0.1)
                        continue
                    
                    # Нет активных чанков ни для одной сессии - можно безопасно остановить
                    logger.warning(f"⚠️ [AVF] Воспроизведение активно перед новым чанком для сессии {sid} (но нет активных чанков), принудительно останавливаем")
                    # Принудительно останавливаем воспроизведение
                    stop_success = await self._avf_engine.stop_output()
                    if not stop_success:
                        logger.error(f"❌ [AVF] Не удалось остановить воспроизведение перед новым чанком для сессии {sid}")
                        # Возвращаем чанк в начало буфера для повторной попытки
                        chunks.insert(0, chunk)
                        await asyncio.sleep(0.1)
                        continue
                    # Небольшая задержка для гарантированного сброса состояния
                    await asyncio.sleep(0.1)
                    logger.info(f"✅ [AVF] Воспроизведение остановлено, готовы к новому чанку для сессии {sid}")
                
                # Воспроизводим чанк
                logger.info(f"✅ [AVF] Воспроизведение чанка для сессии {sid}: {len(audio_bytes)} bytes, {sample_rate}Hz, {channels}ch")
                success = await self._avf_engine.play_audio(audio_bytes, sample_rate, channels)
                
                if not success:
                    logger.error(f"❌ [AVF] play_audio вернул False для сессии {sid}, проверяем состояние")
                    # Проверяем состояние для диагностики
                    if self._avf_engine.is_output_active:
                        logger.warning(f"⚠️ [AVF] Состояние всё ещё активно после неудачного play_audio, принудительно останавливаем")
                        await self._avf_engine.stop_output()
                        await asyncio.sleep(0.1)
                
                if success:
                    # ✅ НОВОЕ: Сохраняем информацию о текущем чанке для completion callback
                    # ✅ КРИТИЧНО: Сохраняем session_id в active_chunks, так как state_manager может сбросить его
                    # ✅ ИСПРАВЛЕНИЕ: Используем Lock для синхронизации доступа
                    async with self._active_chunks_lock:
                        self._active_chunks[sid] = {
                            "chunk": chunk,
                            "start_time": time.time(),
                            "duration_sec": len(audio_bytes) / (sample_rate * channels * 2),
                            "session_id": sid  # ✅ КРИТИЧНО: Сохраняем session_id для использования в completion callback
                        }
                    logger.debug(f"✅ [AVF] Чанк начал воспроизведение для сессии {sid}, ожидаем completion callback")
                    # ✅ УБРАНО: await asyncio.sleep() - полагаемся ТОЛЬКО на completion callback
                    # ✅ УБРАНО: await self._avf_engine.stop_output() - остановка через completion callback
                    # Worker продолжит работу и возьмёт следующий чанк после получения completion callback
                else:
                    logger.error(f"❌ [AVF] Ошибка воспроизведения чанка для сессии {sid}")
                    # ✅ ИСПРАВЛЕНИЕ: Используем Lock для синхронизации доступа
                    async with self._active_chunks_lock:
                        self._active_chunks.pop(sid, None)
                    # Возвращаем чанк в начало буфера для повторной попытки
                    chunks.insert(0, chunk)
                    await asyncio.sleep(0.1)
                    continue
                
                # ✅ КРИТИЧНО: НЕ проверяем завершение сессии здесь
                # Проверка выполняется в _on_avf_playback_completed после completion callback
                # Worker просто продолжит работу и возьмёт следующий чанк, если он есть
                
            except asyncio.CancelledError:
                logger.info("✅ [AVF] Фоновый процесс воспроизведения отменён")
                break
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка в фоновом процессе воспроизведения: {e}", exc_info=True)
                await asyncio.sleep(0.1)
    
    def _on_player_completed(self):
        """Коллбек плеера: воспроизведение завершено (буфер пуст, поток завершён)."""
        try:
            # КРИТИЧНО: Используем state_manager для получения session_id (единый источник истины)
            sid = self.state_manager.get_current_session_id()
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
    
    async def _on_audio_device_fallback(self, event: Dict[str, Any]):
        """
        ✅ Обработчик события переключения на встроенное устройство (E_BT_FALLBACK)
        
        Args:
            event: Событие audio.device.fallback
        """
        try:
            data = event.get('data', {})
            from_device = data.get('from_device', 'unknown')
            to_device = data.get('to_device', 'unknown')
            reason = data.get('reason', 'BT device repeatedly failing')
            
            logger.error(
                f"⚠️ [AUDIO_SYSTEM] ⚠️ КРИТИЧНО: Bluetooth устройство '{from_device}' не отвечает — "
                f"переключились на встроенное устройство '{to_device}'"
            )
            
            # Публикуем уведомление для tray (если нужно)
            # TrayControllerIntegration может подписаться на это событие и показать уведомление
            await self.event_bus.publish("tray.notification", {
                "type": "warning",
                "title": "Bluetooth устройство недоступно",
                "message": f"Переключились на встроенное устройство '{to_device}'",
                "duration": 5.0
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_SYSTEM] Ошибка обработки события fallback: {e}", exc_info=True)

    async def _on_avf_playback_completed(self, event: Dict[str, Any]):
        """Обработчик события завершения воспроизведения от AVFAudioEngine

        ✅ КРИТИЧНО: Обрабатывает completion callback и проверяет, был ли это последний чанк.
        Если последний - публикует playback.completed. Если нет - worker продолжит воспроизведение следующего.
        """
        try:
            data = event.get("data", {})
            source = data.get("source", "AVF")
            finished = data.get("finished", True)

            logger.info(f"✅ [AVF] Получено audio.playback.completed от AVFAudioEngine: source={source}, finished={finished}")
            logger.info(f"🔍 [AVF] _on_avf_playback_completed: event={event}, active_chunks={list(self._active_chunks.keys())}, _avf_chunk_buffer={list(self._avf_chunk_buffer.keys())}")

            # ✅ КРИТИЧНО: Ищем session_id в active_chunks, так как state_manager может сбросить его
            # до завершения воспроизведения всех чанков (при grpc.request_completed)
            # state_manager сбрасывает session_id при grpc.request_completed, но воспроизведение ещё не завершено
            # ✅ ИСПРАВЛЕНИЕ: Используем Lock для синхронизации доступа
            sid = None
            active_chunk_info = None
            
            async with self._active_chunks_lock:
                # Ищем активный чанк по всем сессиям (обычно будет только один)
                logger.info(f"🔍 [AVF] Поиск session_id в active_chunks: {list(self._active_chunks.keys())}")
                for session_id_key, chunk_info in list(self._active_chunks.items()):
                    # Проверяем, что это действительно активный чанк (не старый, начат менее 30 секунд назад)
                    chunk_start_time = chunk_info.get("start_time", 0)
                    time_since_start = time.time() - chunk_start_time if chunk_start_time else None
                    logger.debug(f"🔍 [AVF] Проверка сессии {session_id_key}: chunk_start_time={chunk_start_time}, time_since_start={time_since_start}")
                    # ✅ КРИТИЧНО: Для welcome_message и signal не проверяем время (они могут быть старыми, но это последний чанк)
                    if "welcome_message" in str(session_id_key) or "signal" in str(session_id_key):
                        sid = session_id_key
                        active_chunk_info = self._active_chunks.pop(sid, None)
                        logger.info(f"✅ [AVF] Найден raw-сессия {sid} в active_chunks (без проверки времени)")
                        break
                    elif chunk_start_time and (time.time() - chunk_start_time) < 30.0:
                        sid = session_id_key
                        active_chunk_info = self._active_chunks.pop(sid, None)
                        logger.info(f"✅ [AVF] Найден активный чанк для сессии {sid} в active_chunks (time_since_start={time_since_start:.2f}s)")
                        break
                
                if sid is None:
                    # Fallback: пытаемся получить из state_manager (если он ещё не сброшен)
                    session_id = self.state_manager.get_current_session_id()
                    if session_id is not None:
                        sid = str(session_id)
                        active_chunk_info = self._active_chunks.pop(sid, None)
                        logger.debug(f"🔍 [AVF] Использован session_id из state_manager: {sid}")
                    else:
                        # ✅ КРИТИЧНО: Если session_id не найден, ищем по всем сессиям с активным воспроизведением
                        # Это может произойти, если state_manager сбросил session_id, но воспроизведение ещё активно
                        for session_id_key in list(self._avf_chunk_buffer.keys()):
                            if session_id_key in self._active_chunks:
                                sid = session_id_key
                                active_chunk_info = self._active_chunks.pop(sid, None)
                                logger.warning(f"⚠️ [AVF] session_id не найден в state_manager, использован из _avf_chunk_buffer: {sid}")
                                break
                        
                        if sid is None:
                            logger.error("❌ [AVF] completion callback получен, но session_id не найден ни в active_chunks, ни в state_manager, ни в _avf_chunk_buffer")
                            logger.error(f"❌ [AVF] active_chunks={list(self._active_chunks.keys())}, state_manager.session_id={self.state_manager.get_current_session_id()}, _avf_chunk_buffer={list(self._avf_chunk_buffer.keys())}")
                            # ✅ КРИТИЧНО: Для welcome_message и signal пытаемся найти по паттерну в active_chunks
                            for session_id_key in list(self._active_chunks.keys()):
                                if "welcome_message" in str(session_id_key) or "signal" in str(session_id_key):
                                    sid = session_id_key
                                    active_chunk_info = self._active_chunks.pop(sid, None)
                                    logger.warning(f"⚠️ [AVF] Найден session_id по паттерну: {sid}")
                                    break
                            if sid is None:
                                logger.error("❌ [AVF] session_id не найден даже по паттерну, пропускаем публикацию playback.completed")
                                return
            
            # ✅ КРИТИЧНО: Удаляем из active_chunks (чанк завершён)
            if active_chunk_info:
                elapsed = time.time() - active_chunk_info["start_time"]
                expected_duration = active_chunk_info["duration_sec"]
                logger.info(f"✅ [AVF] Чанк завершён для сессии {sid} через {elapsed:.2f}s (ожидалось {expected_duration:.2f}s)")
            else:
                logger.warning(f"⚠️ [AVF] completion callback получен для сессии {sid}, но чанк не найден в active_chunks")
            
            # ✅ КРИТИЧНО: Проверяем, был ли это последний чанк
            grpc_done = self._grpc_done_sessions.get(sid, False)
            buf_empty = len(self._avf_chunk_buffer.get(sid, [])) == 0
            
            # ✅ ИСПРАВЛЕНИЕ: Для welcome_message и других raw-сессий считаем, что это последний чанк
            # (они не используют gRPC и буферизацию, поэтому grpc_done=False и buf_empty=True)
            # Проверяем, является ли это raw-сессией (welcome_message, signal) по session_id или по отсутствию в буфере
            is_raw_session = False
            if sid and ("welcome_message" in str(sid) or "signal" in str(sid)):
                # ✅ КРИТИЧНО: Для welcome_message и signal всегда считаем raw-сессией
                is_raw_session = True
                logger.info(f"✅ [AVF] Определена raw-сессия для {sid} (по паттерну в session_id)")
            elif active_chunk_info:
                # Если чанк был в active_chunks, но не в буфере (buf_empty=True) и не gRPC (grpc_done=False)
                # - это raw-сессия (welcome_message, signal)
                if buf_empty and not grpc_done:
                    # Проверяем session_id на наличие паттернов raw-сессий
                    if sid and ("welcome_message" in str(sid) or "signal" in str(sid)):
                        is_raw_session = True
                        logger.debug(f"🔍 [AVF] Определена raw-сессия для {sid} (buf_empty=True, grpc_done=False)")
            
            # ✅ ИСПРАВЛЕНИЕ: Проверяем, не была ли сессия уже финализирована
            if self._finalized_sessions.get(sid, False):
                logger.debug(f"🔍 [AVF] Сессия {sid} уже финализирована, пропускаем публикацию playback.completed")
                return
            
            # ✅ КРИТИЧНО: Управление таймером в зависимости от того, последний ли чанк
            # ✅ ИСПРАВЛЕНИЕ: Для raw-сессий (welcome_message, signal) считаем, что это последний чанк
            is_last_chunk = (grpc_done and buf_empty) or is_raw_session
            
            if is_last_chunk:
                # ✅ ПОСЛЕДНИЙ ЧАНК - отменяем таймер (больше не нужен)
                if sid in self._silence_tasks:
                    silence_task = self._silence_tasks[sid]
                    if not silence_task.done():
                        silence_task.cancel()
                        logger.debug(f"✅ [AVF] Отменён _finalize_on_silence для сессии {sid} (последний чанк завершён)")
                    self._silence_tasks.pop(sid, None)
            else:
                # ✅ НЕ ПОСЛЕДНИЙ ЧАНК - перезапускаем таймер для продолжения fallback защиты
                # Это гарантирует, что если completion callback для следующего чанка не придёт, fallback всё равно сработает
                if sid in self._silence_tasks:
                    old_task = self._silence_tasks[sid]
                    if not old_task.done():
                        old_task.cancel()
                        logger.debug(f"✅ [AVF] Перезапускаем _finalize_on_silence для сессии {sid} (не последний чанк, продолжаем fallback защиту)")
                    self._silence_tasks.pop(sid, None)
                # Перезапускаем таймер с тем же таймаутом
                self._silence_tasks[sid] = asyncio.create_task(self._finalize_on_silence(sid, timeout=10.0))
            
            if is_last_chunk:
                # ✅ ПОСЛЕДНИЙ ЧАНК ЗАВЕРШЁН - публикуем playback.completed
                logger.info(f"✅ [AVF] Последний чанк завершён для сессии {sid}, публикуем playback.completed")
                logger.info(f"🔍 [AVF] is_last_chunk=True: grpc_done={grpc_done}, buf_empty={buf_empty}, is_raw_session={is_raw_session}")
                self._avf_is_playing.pop(sid, None)
                self._finalized_sessions[sid] = True
                
                # Очищаем буфер (если был)
                self._avf_chunk_buffer.pop(sid, None)
                # ✅ ИСПРАВЛЕНИЕ: Используем Lock для синхронизации доступа
                async with self._active_chunks_lock:
                    self._active_chunks.pop(sid, None)
                
                # Определяем pattern для события
                # Для raw-сессий (welcome_message, signal) используем pattern из session_id
                event_pattern = "avf_playback"
                if is_raw_session and sid:
                    if "welcome_message" in str(sid):
                        event_pattern = "welcome_message"
                    elif "signal" in str(sid):
                        event_pattern = "signal"
                
                # Публикуем playback.completed
                logger.info(f"🔍 [AVF] Публикуем playback.completed для сессии {sid}, pattern={event_pattern}")
                await self.event_bus.publish("playback.completed", {
                    "session_id": sid,
                    "pattern": event_pattern,
                    "source": source,
                    "finished": finished
                })
                logger.info(f"✅ [AVF] playback.completed опубликовано для сессии {sid}, pattern={event_pattern}")
                logger.info(f"✅ [AVF] playback.completed опубликовано для сессии {sid} (последний чанк, pattern={event_pattern})")
                
                # Переход в SLEEPING
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.SLEEPING,
                    "source": "speech_playback_avf"
                })
            else:
                # ✅ НЕ ПОСЛЕДНИЙ ЧАНК - worker продолжит воспроизведение следующего
                logger.debug(f"🔍 [AVF] Чанк завершён, но не последний (grpc_done={grpc_done}, buf_empty={buf_empty}), worker продолжит")
                # Worker автоматически возьмёт следующий чанк из буфера, так как active_chunks[sid] удалён
            
            # ✅ ОПТИМИЗАЦИЯ: Пробуждаем worker мгновенно вместо polling (0.1s ожидания)
            self._chunk_completed_event.set()
                
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка обработки audio.playback.completed: {e}", exc_info=True)
    
    async def _on_avf_playback_interrupted(self, event: Dict[str, Any]):
        """Обработчик события прерывания воспроизведения от AVFAudioEngine
        
        ✅ КРИТИЧНО: Обрабатывает audio.playback.interrupted для завершения воспроизведения
        когда engine остановлен системой во время воспроизведения (буфер потерян)
        """
        try:
            data = event.get("data", {})
            reason = data.get("reason", "unknown")
            device_name = data.get("device_name", "unknown")
            source = data.get("source", "AVF")
            
            logger.warning(f"⚠️ [AVF] Получено audio.playback.interrupted: reason={reason}, device={device_name}, source={source}")
            
            # ✅ КРИТИЧНО: Ищем session_id из state_manager или из AVF буферов
            current_session_id = self.state_manager.get_current_session_id()
            
            # ✅ ИСПРАВЛЕНИЕ: Если session_id не найден в state_manager, ищем в AVF буферах
            if current_session_id is None:
                # Ищем активные сессии в AVF буферах
                active_sessions = [
                    sid for sid, chunks in self._avf_chunk_buffer.items()
                    if len(chunks) > 0 or self._avf_is_playing.get(sid, False)
                ]
                if active_sessions:
                    current_session_id = active_sessions[0]
                    logger.info(f"⚠️ [AVF] session_id не найден в state_manager, использован из AVF буфера: {current_session_id}")
            
            # ✅ КРИТИЧНО: Если session_id найден, публикуем playback.completed для предотвращения зависания
            if current_session_id is not None:
                logger.warning(f"⚠️ [AVF] Публикуем playback.completed для сессии {current_session_id} (воспроизведение прервано из-за остановки engine)")
                # Очищаем активные чанки для этой сессии
                async with self._active_chunks_lock:
                    self._active_chunks.pop(str(current_session_id), None)
                # Публикуем playback.completed
                await self.event_bus.publish("playback.completed", {
                    "session_id": current_session_id,
                    "pattern": "avf_playback",
                    "source": source,
                    "interrupted": True,
                    "reason": reason
                })
                logger.info(f"✅ [AVF] playback.completed опубликовано для сессии {current_session_id} (прервано: {reason})")
            else:
                logger.warning("⚠️ [AVF] session_id не найден, не можем опубликовать playback.completed")
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка обработки audio.playback.interrupted: {e}", exc_info=True)
    
    async def _on_avf_output_resync_required(self, event: Dict[str, Any]):
        """Обработчик события необходимости ресинхронизации выхода от AVFAudioEngine
        
        ✅ КРИТИЧНО: Обрабатывает audio.device.output_resync_required для возобновления
        воспроизведения после конфигурационных событий (например, переключение режимов AirPods)
        """
        try:
            data = event.get("data", {})
            device_name = data.get("device_name", "unknown")
            
            logger.info(f"🔄 [AVF] Получено audio.device.output_resync_required: device={device_name}")
            
            # ✅ КРИТИЧНО: Если воспроизведение было прервано, пытаемся возобновить
            # Логика возобновления уже реализована в _on_raw_audio(), здесь только логируем
            if self._avf_engine and self._avf_engine.is_output_active:
                logger.debug("🔍 [AVF] Воспроизведение активно, ресинхронизация не требуется")
            else:
                logger.debug("🔍 [AVF] Воспроизведение не активно, ресинхронизация будет выполнена при следующем чанке")
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка обработки audio.device.output_resync_required: {e}", exc_info=True)
    
    async def _on_output_device_changed(self, event: Dict[str, Any]):
        """
        ✅ НОВАЯ АУДИОСИСТЕМА: Обработчик события смены OUTPUT устройства

        Args:
            event: Событие audio.device.output_changed или audio.device.both_changed
        """
        try:
            # Формат события от DeviceMonitor: data содержит отдельные поля, не объект device
            data = event.get('data', {})
            
            # Проверяем формат события (может быть device объект или отдельные поля)
            if 'device' in data:
                # Новый формат: объект device
                device_data = data.get('device')
                if hasattr(device_data, 'name'):
                    # Это DeviceDescriptor
                    device_name = device_data.name
                    device_id = device_data.device_id
                    uid = device_data.uid
                    is_bluetooth = device_data.is_bluetooth
                    sample_rate = device_data.sample_rate
                    channels = device_data.channels
                    blocksize = device_data.blocksize
                    latency = device_data.latency
                else:
                    # Это словарь
                    device_name = device_data.get('name', '')
                    device_id = device_data.get('device_id')
                    uid = device_data.get('uid', '')
                    is_bluetooth = device_data.get('is_bluetooth', False)
                    sample_rate = device_data.get('sample_rate', 48000)
                    channels = device_data.get('channels', 2)
                    blocksize = device_data.get('blocksize')
                    latency = device_data.get('latency')
            else:
                # Старый формат: отдельные поля в data
                device_name = data.get('device_name', '')
                device_id = data.get('device_id')
                uid = data.get('uid', '')
                is_bluetooth = data.get('is_bluetooth', False)
                sample_rate = data.get('sample_rate', 48000)
                channels = data.get('channels', 2)
                blocksize = data.get('blocksize')
                latency = data.get('latency')
            
            is_new_device = data.get('is_new_device', False)
            
            if not device_name:
                logger.warning("⚠️ [AUDIO_SYSTEM] Событие смены устройства без имени")
                return
            
            logger.info(f"🔄 [AUDIO_SYSTEM] Получено событие смены OUTPUT устройства: {device_name} (новое: {is_new_device})")
            
            # Переключаем устройство в плеере через OutputStreamManager
            if self._output_stream_manager and self._player:
                from modules.audio_core.types import DeviceDescriptor
                
                # Создаём DeviceDescriptor из данных события
                new_device = DeviceDescriptor(
                    uid=uid or f"device_{device_id}" if device_id else f"device_{device_name}",
                    name=device_name,
                    device_id=device_id,
                    sample_rate=sample_rate,
                    channels=channels,
                    is_bluetooth=is_bluetooth,
                    is_input=False,  # OUTPUT устройство
                    blocksize=blocksize,
                    latency=latency
                )
                
                # ✅ КРИТИЧНО: Используем resync_output_device для переключения устройства
                # Это гарантирует правильную синхронизацию формата и пересоздание потока
                # resync_output_device вызывает _sync_output_format(restart_stream=True), который:
                # 1. Определяет параметры нового устройства через _probe_output_format
                # 2. Обновляет config.sample_rate/channels
                # 3. Останавливает старый поток (если есть) и создает новый с правильными параметрами
                # ✅ НОВОЕ: Если потока нет - создает новый для автоматического подключения
                logger.info(f"🔄 [AUDIO_SYSTEM] Переключаем устройство через resync_output_device: {device_name} (новое устройство: {is_new_device})")
                device_changed = self._player.resync_output_device()
                if device_changed:
                    logger.info(f"✅ [AUDIO_SYSTEM] Устройство переключено: {device_name} (rate={self._player.config.sample_rate}Hz, ch={self._player.config.channels})")
                else:
                    # ✅ НОВОЕ: Даже если параметры не изменились, но это новое устройство - создаем поток
                    if is_new_device:
                        logger.info(f"🔄 [AUDIO_SYSTEM] Новое устройство обнаружено, создаем поток даже если параметры не изменились: {device_name}")
                        # Принудительно создаем поток для нового устройства
                        self._player._sync_output_format(restart_stream=True)
                        logger.info(f"✅ [AUDIO_SYSTEM] Поток создан для нового устройства: {device_name}")
                    else:
                        logger.debug(f"🔍 [AUDIO_SYSTEM] Параметры устройства не изменились: {device_name}")
            else:
                logger.warning("⚠️ [AUDIO_SYSTEM] OutputStreamManager или Player недоступен для переключения устройства")
                    
        except Exception as e:
            logger.error(f"❌ [AUDIO_SYSTEM] Ошибка обработки события смены устройства: {e}", exc_info=True)
    
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
