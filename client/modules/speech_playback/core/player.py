"""
Sequential Speech Player - Основной плеер для последовательного воспроизведения

ОСНОВНЫЕ ПРИНЦИПЫ:
1. Последовательное воспроизведение - один чанк за раз
2. Без лимитов размера - накопление всех данных
3. Thread-safety - безопасная работа в многопоточной среде
4. macOS совместимость - для PKG упаковки
5. Простота и надежность - минимальная сложность
"""

import logging
import threading
import time
import asyncio
import sounddevice as sd
import numpy as np
from typing import Optional, Callable, Dict, Any
from dataclasses import dataclass

from .state import StateManager, PlaybackState, ChunkState
from .buffer import ChunkBuffer, ChunkInfo
from ..utils.audio_utils import resample_audio, convert_channels
# Воспроизведение использует системные дефолтные устройства macOS, отдельный менеджер не требуется
from ..macos.core_audio import CoreAudioManager
from ..macos.performance import PerformanceMonitor

# ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ АУДИО
from config.unified_config_loader import unified_config

logger = logging.getLogger(__name__)

@dataclass
class PlayerConfig:
    """
    Конфигурация плеера

    ВАЖНО: Используйте from_centralized_config() для загрузки из unified_config.yaml
    Хардкод значения ниже - только fallback на случай ошибки загрузки конфигурации.
    """
    sample_rate: int = 48000  # Fallback - загружается из централизованной конфигурации
    channels: int = 1         # Fallback - загружается из централизованной конфигурации
    dtype: str = 'int16'      # Fallback - загружается из централизованной конфигурации
    buffer_size: int = 512    # Fallback - загружается из централизованной конфигурации
    max_memory_mb: int = 1024 # Fallback - загружается из централизованной конфигурации
    device_id: Optional[int] = None
    auto_device_selection: bool = True
    auto_output_device_switch: bool = True  # Автоматическое переключение output устройства
    
    @classmethod
    def from_centralized_config(cls) -> 'PlayerConfig':
        """
        Создать PlayerConfig из централизованной конфигурации
        
        Returns:
            PlayerConfig: Конфигурация из unified_config.yaml
        """
        try:
            audio_config = unified_config.get_audio_config()
            config_dict = audio_config.get_speech_playback_config()
            
            return cls(
                sample_rate=config_dict['sample_rate'],
                channels=config_dict['channels'],
                dtype=config_dict['dtype'],
                buffer_size=config_dict['buffer_size'],
                max_memory_mb=config_dict['max_memory_mb'],
                auto_device_selection=config_dict['auto_device_selection'],
                auto_output_device_switch=config_dict.get('auto_output_device_switch', True),
                device_id=None  # Определяется автоматически
            )
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки централизованной конфигурации: {e}")
            logger.info("🔄 Используем конфигурацию по умолчанию")
            return cls()  # Fallback к defaults

class SequentialSpeechPlayer:
    """Плеер для последовательного воспроизведения речи"""
    
    def __init__(self, config: Optional[PlayerConfig] = None):
        """
        Инициализация плеера
        
        Args:
            config: Конфигурация плеера (если None, загружается из централизованной конфигурации)
        """
        # Используем централизованную конфигурацию по умолчанию
        if config is None:
            try:
                self.config = PlayerConfig.from_centralized_config()
                logger.info("✅ PlayerConfig загружен из централизованной конфигурации")
            except Exception as e:
                logger.warning(f"⚠️ Ошибка загрузки централизованной конфигурации: {e}")
                logger.info("🔄 Используем fallback конфигурацию")
                self.config = PlayerConfig()
        else:
            self.config = config
        self.state_manager = StateManager()
        # Выбираем dtype буфера под конфиг (унифицировано на int16)
        buf_dtype = np.int16 if str(self.config.dtype).lower() in ('int16', 'short') else np.int16  # Всегда int16
        self.chunk_buffer = ChunkBuffer(sample_rate=self.config.sample_rate, channels=self.config.channels, dtype=str(buf_dtype))
        
        # Потоки и синхронизация
        self._playback_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._pause_event.set()  # Начинаем с разблокированной паузы
        
        # Аудио поток (lazy start для снижения нагрузки)
        self._audio_stream: Optional[sd.OutputStream] = None
        self._stream_lock = threading.RLock()
        self._stream_started = False  # Флаг для lazy start
        
        # macOS компоненты
        self._core_audio_manager = CoreAudioManager()
        self._performance_monitor = PerformanceMonitor()

        # Output device tracking (для автоматического переключения устройств)
        self.output_device_name: Optional[str] = None  # PRIMARY: имя для сравнения
        self._current_playback_session_id: Optional[Any] = None  # Текущая сессия воспроизведения
        self._current_device_id: Optional[int] = None  # Текущий device ID для отслеживания изменений
        
        # 🔧 РЕФАКТОРИНГ: Разделение device_sample_rate и content_sample_rate
        # config.sample_rate = целевой rate контента/движка (например 24000 по умолчанию)
        # _device_sample_rate = реальный rate устройства (например 48000)
        # _actual_sample_rate = rate текущего контента из metadata (например 24000)
        self._device_sample_rate: Optional[int] = None  # Sample rate устройства (из _probe_output_format)
        self._actual_sample_rate: Optional[int] = None  # Реальный sample_rate из аудио данных (content rate)
        self._stream_sample_rate: Optional[int] = None  # Sample rate текущего потока (для сравнения)
        
        # 🔧 РЕФАКТОРИНГ: Защита от re-entrancy при пересоздании потока
        self._recreating_stream: bool = False  # Флаг пересоздания потока (защита от гонок)
        self._recreating_stream_start_time: Optional[float] = None  # Время начала пересоздания (для защиты от залипания)
        
        # 🔧 РЕФАКТОРИНГ: Метрики для диагностики
        self._stream_recreate_count: int = 0  # Счетчик пересозданий потока
        self._stream_recreate_reasons: list = []  # Причины пересозданий (для диагностики)
        
        # 🔧 ФИНАЛЬНЫЕ ФИКСЫ: Generation counter для защиты от устаревших callback'ов
        self._stream_gen: int = 0  # Generation counter - увеличивается при каждом recreate
        self._current_stream_gen: int = 0  # Generation текущего активного stream (для callback)
        
        # 🔧 ФИНАЛЬНЫЙ ФИКС: Импорт функции ресемплинга
        try:
            from modules.speech_playback.utils.device_utils import resample_audio
            self._resample_audio_func = resample_audio
        except ImportError:
            logger.warning("⚠️ [RESAMPLE] Не удалось импортировать resample_audio, ресемплинг недоступен")
            self._resample_audio_func = None
        
        # 🔧 PRODUCTION ФИКС #1: Кэш для np.arange(n) по длине входа (оптимизация ресемплинга)
        self._interp_x_cache: dict[int, np.ndarray] = {}  # Кэш: n -> np.arange(n, dtype=np.float32)
        self._max_interp_cache_size: int = 100  # Максимум записей в кэше
        
        # 🔧 ФИНАЛЬНЫЕ ФИКСЫ: Cooldown на device query
        self._last_device_query_ts: float = 0.0  # Время последнего device query
        self._device_query_cooldown_sec: float = 0.5  # Cooldown 500ms между запросами
        
        # 🔧 ФИНАЛЬНЫЕ ФИКСЫ: Защита от playback без ресемплинга
        self._needs_resample: bool = False  # Требуется ли ресемплинг
        self._resample_warning_logged: bool = False  # Логировали ли предупреждение о ресемплинге
        
        # 🔧 PRODUCTION: Кэш последнего успешного device (для failure-path)
        self._last_valid_device_id: Optional[int] = None  # Последний валидный device_id
        self._last_valid_device_sr: Optional[int] = None  # Последний валидный device_sr
        
        # 🔧 PRODUCTION: Tripwires (счётчики и таймеры)
        self._callback_underrun_count: int = 0  # Счётчик underrun в callback
        self._callback_gen_mismatch_count: int = 0  # Счётчик несовпадений generation
        self._callback_shape_mismatch_count: int = 0  # Счётчик нарушений shape инварианта
        self._callback_error_count: int = 0  # Счётчик ошибок в callback
        self._resample_error_count: int = 0  # Счётчик ошибок ресемплинга
        self._device_query_failure_count: int = 0  # Счётчик неудачных device queries
        self._stream_open_fail_count: int = 0  # Счётчик неудачных открытий stream
        
        # Таймеры (rolling avg / max)
        self._recreate_total_ms_history: list = []  # История времени recreate (для avg/max)
        self._callback_resample_ms_history: list = []  # История времени ресемплинга (для avg/max)
        self._max_recreate_history: int = 100  # Максимум записей в истории

        # Callbacks
        self._on_chunk_started: Optional[Callable[[ChunkInfo], None]] = None
        self._on_chunk_completed: Optional[Callable[[ChunkInfo], None]] = None
        self._on_playback_completed: Optional[Callable[[], None]] = None
        self._on_error: Optional[Callable[[Exception], None]] = None

        logger.info("🔧 SequentialSpeechPlayer инициализирован")

    def initialize(self) -> bool:
        """Инициализация плеера"""
        try:
            logger.info("🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...")
            # Инициализация macOS компонентов
            logger.debug(f"🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...")
            # 🔧 FIX: Проверяем наличие метода initialize() перед вызовом
            if hasattr(self._core_audio_manager, 'initialize'):
                if not self._core_audio_manager.initialize():
                    logger.error("❌ [AUDIO_ERROR] Ошибка инициализации Core Audio")
                    return False
                logger.info("✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован")
            else:
                logger.debug("🔍 [AUDIO_DEBUG] Core Audio Manager не требует инициализации (метод initialize отсутствует)")

            # Подстраиваемся под актуальный выходной маршрут
            self._sync_output_format()
            
            # Используем системное устройство по умолчанию от macOS
            if self.config.auto_device_selection:
                logger.info("🎯 Используем системное устройство по умолчанию от macOS")
                # Синхронизируем буфер под новое число каналов
                # 🔧 FIX: Проверяем наличие метода set_channels() перед вызовом
                if hasattr(self.chunk_buffer, 'set_channels'):
                    try:
                        self.chunk_buffer.set_channels(self.config.channels)
                    except Exception as e:
                        logger.debug(f"⚠️ Не удалось обновить каналы буфера: {e}")
                else:
                    logger.debug("🔍 [AUDIO_DEBUG] ChunkBuffer не поддерживает set_channels()")
            
            # Логируем конфигурацию плеера для отладки
            logger.info(f"📊 [AUDIO_STATS] Конфигурация плеера: sample_rate={self.config.sample_rate}Hz, channels={self.config.channels}, dtype={self.config.dtype}")
            
            # Инициализация мониторинга производительности
            # 🔧 FIX: Проверяем наличие метода start() перед вызовом
            if hasattr(self._performance_monitor, 'start'):
                self._performance_monitor.start()
            else:
                logger.debug("🔍 [AUDIO_DEBUG] Performance Monitor не требует запуска (метод start отсутствует)")
            
            logger.info("✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка инициализации плеера: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            return False
    
    def add_audio_data(self, audio_data: np.ndarray, priority: int = 0, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Добавить аудио данные для воспроизведения

        Args:
            audio_data: Аудио данные
            priority: Приоритет чанка
            metadata: Дополнительные метаданные

        Returns:
            ID чанка
        """
        try:
            # Извлекаем metadata ВНЕ lock (быстрые операции)
            session_id = metadata.get('session_id') if metadata else None
            incoming_sr = None
            if metadata and 'sample_rate' in metadata:
                incoming_sr = int(metadata['sample_rate'])

            # 🔧 РЕФАКТОРИНГ: Минимизируем время под lock - только критичные операции
            # Выполняем медленные операции (_query_default_output_device) ВНЕ lock
            device_id = None
            device_sr = None
            if session_id != self._current_playback_session_id or not self._stream_started:
                logger.debug(f"🔍 [OUTPUT] Новая сессия или первый запуск (session={session_id})")
            # 🔧 ФИНАЛЬНЫЙ ФИКС: Cooldown только на failure-path (успешные запросы обрабатываются сразу)
            current_time = time.time()
            device_changed, detected_device_id, detected_device_sr = None, None, None

            # Всегда проверяем device change (для быстрой реакции на переключение)
            device_changed, detected_device_id, detected_device_sr = self._detect_output_device_change()

            if device_changed:
                # Устройство изменилось - обрабатываем сразу (игнорируем cooldown)
                device_id = detected_device_id
                device_sr = detected_device_sr
                logger.debug(f"🔍 [OUTPUT] Обнаружено изменение устройства: device_id={device_id}, device_sr={device_sr}Hz")
            elif detected_device_id is None or detected_device_sr is None:
                # Device не найден - применяем cooldown (failure-path)
                if current_time - self._last_device_query_ts >= self._device_query_cooldown_sec:
                    self._last_device_query_ts = current_time
                    # Используем обнаруженные значения (даже если None)
                    device_id = detected_device_id
                    device_sr = detected_device_sr
                else:
                    # Cooldown активен - используем кэш
                    logger.debug(f"🔍 [OUTPUT] Device query в cooldown (device не найден), используем кэш")
            else:
                # Device найден, но не изменился - обновляем timestamp
                self._last_device_query_ts = current_time

            # 🔧 РЕФАКТОРИНГ: Вся логика пересоздания потока под единым lock (минимальное время)
            need_device_query = False
            with self._stream_lock:
                # 1) Обновляем _actual_sample_rate если изменился
                if incoming_sr is not None:
                    if self._actual_sample_rate is None or self._actual_sample_rate != incoming_sr:
                        old_sr = self._actual_sample_rate
                        self._actual_sample_rate = incoming_sr
                        logger.info(f"🔧 [SAMPLE_RATE] Обновлен реальный sample_rate: {old_sr}Hz → {incoming_sr}Hz (config: {self.config.sample_rate}Hz)")
                
                # 2) Обновляем сессию и device info (если обнаружено изменение)
                if session_id != self._current_playback_session_id:
                    self._current_playback_session_id = session_id
                
                if device_id is not None:
                    self._current_device_id = device_id
                if device_sr is not None:
                    self._device_sample_rate = device_sr
                
                # 3) Единый механизм пересоздания потока (атомарно)
                reason = f"add_audio_data (session={session_id}, thread={threading.current_thread().name})"
                recreated, need_device = self._recreate_stream_if_needed_locked(
                    reason=reason, 
                    device_id=device_id, 
                    incoming_sr=incoming_sr,
                    device_sr=device_sr
                )
                
                if need_device:
                    # Требуется device_id - выходим из lock, получаем device, снова lock
                    need_device_query = True
                
                # 4) Если поток не существует и не требуется device query, создаем его
                if self._audio_stream is None and not need_device_query:
                    if device_id is None:
                        need_device_query = True
                    else:
                        # Создаем поток синхронно (для простоты, можно оптимизировать позже)
                        pass  # Будет создан через recreate или отдельно
            
            # 🔧 Если требуется device query - выполняем ВНЕ lock
            if need_device_query:
                current_time = time.time()
                current_device = self._query_default_output_device()
                device_id = current_device.get('index') if current_device else None
                device_info = current_device if current_device else {}
                device_sr = device_info.get('default_samplerate')
                if device_sr:
                    try:
                        device_sr = int(device_sr)
                    except:
                        device_sr = None
                
                # 🔧 ФИНАЛЬНЫЙ ФИКС: Cooldown только на failure-path
                if device_id is None:
                    # Device не найден - применяем cooldown
                    self._device_query_failure_count += 1
                    if current_time - self._last_device_query_ts >= self._device_query_cooldown_sec:
                        self._last_device_query_ts = current_time
                        # 🔧 PRODUCTION ФИКС #4: Используем кэш последнего успешного device
                        if self._last_valid_device_id is not None:
                            device_id = self._last_valid_device_id
                            device_sr = self._last_valid_device_sr
                            logger.debug(f"🔍 [DEVICE] Используем кэш последнего успешного device: id={device_id}, sr={device_sr}Hz")
                        # Логируем раз в 5 секунд
                        if not hasattr(self, '_device_not_found_last_log') or (current_time - getattr(self, '_device_not_found_last_log', 0)) >= 5.0:
                            logger.warning(f"⚠️ [DEVICE] Device не найден (failure_count={self._device_query_failure_count}), продолжаем буферизацию. Чанки не потеряются.")
                            self._device_not_found_last_log = current_time
                    else:
                        # Cooldown активен - пропускаем query, используем кэш
                        if self._last_valid_device_id is not None:
                            device_id = self._last_valid_device_id
                            device_sr = self._last_valid_device_sr
                        logger.debug(f"🔍 [DEVICE] Device query в cooldown (device не найден), используем кэш")
                        need_device_query = False  # Не пытаемся recreate без device_id
                else:
                    # Device найден - обновляем timestamp и кэш (успешный запрос)
                    self._last_device_query_ts = current_time
                    # 🔧 PRODUCTION ФИКС #4: Кэшируем успешный device
                    self._last_valid_device_id = device_id
                    self._last_valid_device_sr = device_sr
                
                # Снова под lock - обновляем и пересоздаем
                with self._stream_lock:
                    if device_id is not None:
                        self._current_device_id = device_id
                    if device_sr is not None:
                        self._device_sample_rate = device_sr
                    
                    recreated, _ = self._recreate_stream_if_needed_locked(
                        reason=reason,
                        device_id=device_id,
                        incoming_sr=incoming_sr,
                        device_sr=device_sr
                    )
                    
                    if self._audio_stream is None and device_id is not None:
                        # Создаем поток если все еще не существует
                        new_stream = self._create_audio_stream_unlocked(
                            device_id=device_id,
                            content_sr=incoming_sr or self._actual_sample_rate or self.config.sample_rate,
                            device_sr=device_sr or self._device_sample_rate
                        )
                        if new_stream:
                            self._audio_stream = new_stream
                            self._stream_started = False
                            self._stream_sample_rate = device_sr or incoming_sr or self.config.sample_rate
                            self._current_device_id = device_id
                
                # ✅ КРИТИЧНО: Чанк добавляется в буфер ДАЖЕ если recreate был пропущен
                # Это гарантирует что аудио не потеряется

            # ✅ ПРАВИЛЬНО: ЕДИНСТВЕННАЯ конвертация в модуле плеера
            # Только dtype конвертация - все остальные конвертации убраны
            
            # Проверяем и конвертируем dtype если необходимо
            if audio_data.dtype == np.float32 or audio_data.dtype == np.float64:
                # float32/float64 → int16
                audio_data = np.clip(audio_data, -1.0, 1.0)
                audio_data = (audio_data * 32767.0).astype(np.int16)
                logger.debug(f"🔄 Конвертация: {audio_data.dtype} → int16")
            elif audio_data.dtype != np.int16:
                # другие типы → int16
                audio_data = audio_data.astype(np.int16)
                logger.debug(f"🔄 Конвертация: {audio_data.dtype} → int16")
            # Если уже int16 - оставляем как есть
            
            # Убеждаемся, что данные в правильной форме [samples, channels]
            if audio_data.ndim == 1:
                # 1D → 2D [samples, 1] для моно
                audio_data = audio_data.reshape(-1, 1)
                current_channels = 1
            elif audio_data.ndim > 2:
                # 3D+ → 2D
                audio_data = audio_data.reshape(audio_data.shape[0], -1)
                current_channels = audio_data.shape[1]
            else:
                current_channels = audio_data.shape[1]

            # ✅ ИСПРАВЛЕНИЕ: Упрощенная логика каналов
            # Оставляем данные как есть - sounddevice сам разберется с конвертацией
            target_channels = int(self.config.channels)
            
            # Только базовая конвертация если действительно необходимо
            if current_channels != target_channels:
                if current_channels == 1 and target_channels == 1:
                    # Моно → Моно: оставляем как есть
                    pass
                elif current_channels == 1 and target_channels > 1:
                    # Моно → Стерео: НЕ дублируем, пусть sounddevice разберется
                    logger.debug(f"🔄 Моно аудио будет воспроизведено на {target_channels} каналах")
                elif current_channels > 1 and target_channels == 1:
                    # Стерео → Моно: берем первый канал
                    audio_data = audio_data[:, :1]
                    logger.debug(f"🔄 Стерео → Моно: взят первый канал")
                # Остальные случаи оставляем как есть

            # 🔍 ДИАГНОСТИКА: Вычисляем ожидаемую длительность (ВНЕ lock)
            if incoming_sr is not None and len(audio_data) > 0:
                expected_duration = len(audio_data) / float(incoming_sr)
                logger.info(f"🔍 [SAMPLE_RATE_DIAG] Аудио: {len(audio_data)} samples, expected_duration={expected_duration:.3f}s at {incoming_sr}Hz")
                if self.config.sample_rate != incoming_sr:
                    wrong_duration = len(audio_data) / float(self.config.sample_rate)
                    speed_factor = incoming_sr / float(self.config.sample_rate)
                    logger.warning(f"⚠️ [SAMPLE_RATE_DIAG] При {self.config.sample_rate}Hz: duration={wrong_duration:.3f}s, speed_factor={speed_factor:.2f}x")

            # Добавляем в буфер (priority передаем в metadata)
            if metadata is None:
                metadata = {}
            metadata['priority'] = priority
            chunk_id = self.chunk_buffer.add_chunk(audio_data, metadata)

            # Lazy start: стартуем поток при появлении первого чанка
            self._ensure_stream_started()

            logger.info(f"✅ Аудио данные добавлены: {chunk_id} (size: {len(audio_data)})")

            return chunk_id
            
        except Exception as e:
            logger.error(f"❌ Ошибка добавления аудио данных: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            raise
    
    def start_playback(self) -> bool:
        """Запуск воспроизведения"""
        try:
            # Проверяем, что можем запустить воспроизведение
            if self.state_manager.current_state not in [PlaybackState.IDLE, PlaybackState.PAUSED]:
                logger.warning("⚠️ Невозможно запустить воспроизведение в текущем состоянии")
                return False
            
            # Переходим в состояние PLAYING
            self.state_manager.set_state(PlaybackState.PLAYING)
            
            # НЕ очищаем данные - они уже добавлены в буфер
            
            # Запускаем аудио поток
            if not self._start_audio_stream():
                self.state_manager.set_state(PlaybackState.ERROR)
                return False
            
            # ✅ FIX: Стартуем поток сразу при start_playback (не lazy start)
            # Это гарантирует, что поток готов к воспроизведению
            self._ensure_stream_started()
            
            # Запускаем поток воспроизведения
            self._stop_event.clear()
            self._pause_event.set()
            
            self._playback_thread = threading.Thread(target=self._playback_loop, daemon=True)
            self._playback_thread.start()
            
            logger.info("🎵 Воспроизведение запущено")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска воспроизведения: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            return False
    
    def stop_playback(self) -> bool:
        """Остановка воспроизведения"""
        try:
            # Проверяем, что можем остановить воспроизведение
            if self.state_manager.current_state not in [PlaybackState.PLAYING, PlaybackState.PAUSED]:
                logger.warning("⚠️ Невозможно остановить воспроизведение в текущем состоянии")
                return False
            
            # Переходим в состояние STOPPING
            self.state_manager.set_state(PlaybackState.STOPPING)
            
            # Останавливаем поток воспроизведения
            self._stop_event.set()
            
            # МГНОВЕННО прерываем аудио: очищаем буферы и останавливаем поток до ожидания join
            try:
                self.chunk_buffer.clear_all()
            except Exception:
                pass
            self._stop_audio_stream()
            
            # Ждем завершения потока
            if self._playback_thread and self._playback_thread.is_alive():
                self._playback_thread.join(timeout=1.0)
            
            # Переходим в состояние STOPPED
            self.state_manager.set_state(PlaybackState.IDLE)
            
            logger.info("🛑 Воспроизведение остановлено")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки воспроизведения: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            return False
    
    def pause_playback(self) -> bool:
        """Приостановка воспроизведения"""
        try:
            # Проверяем, что можем поставить на паузу
            if self.state_manager.current_state != PlaybackState.PLAYING:
                logger.warning("⚠️ Невозможно приостановить воспроизведение в текущем состоянии")
                return False
            
            self._pause_event.clear()
            self.state_manager.set_state(PlaybackState.PAUSED)
            
            logger.info("⏸️ Воспроизведение приостановлено")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка приостановки воспроизведения: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            return False
    
    def resume_playback(self) -> bool:
        """Возобновление воспроизведения"""
        try:
            # Проверяем, что можем возобновить воспроизведение
            if self.state_manager.current_state != PlaybackState.PAUSED:
                logger.warning("⚠️ Невозможно возобновить воспроизведение в текущем состоянии")
                return False
            
            self._pause_event.set()
            self.state_manager.set_state(PlaybackState.PLAYING)
            
            logger.info("▶️ Воспроизведение возобновлено")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка возобновления воспроизведения: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
            return False
    
    def _start_audio_stream(self, *, sync_output: bool = True, device_id: int = None) -> bool:
        """
        Запуск аудио потока с lazy start (публичный метод, берет lock)

        Args:
            sync_output: Синхронизировать формат с устройством
            device_id: ID устройства (None = использовать дефолтное)
        """
        with self._stream_lock:
            return self._start_audio_stream_locked(sync_output=sync_output, device_id=device_id)
    
    def _start_audio_stream_locked(self, *, sync_output: bool = True, device_id: int = None) -> bool:
        """
        Запуск аудио потока с lazy start (locked-версия, вызывается когда lock уже взят)
        
        🔧 РЕФАКТОРИНГ: Использует _create_audio_stream_unlocked для создания потока ВНЕ lock.

        Args:
            sync_output: Синхронизировать формат с устройством
            device_id: ID устройства (None = использовать дефолтное)
        """
        if self._audio_stream is not None:
            logger.warning("⚠️ Аудио поток уже создан")
            return True

        # Перед созданием потока уточняем параметры текущего устройства
        if sync_output:
            # 🔧 РЕФАКТОРИНГ: _sync_output_format_locked не меняет config.sample_rate
            self._sync_output_format_locked(restart_stream=False)

        # Получаем параметры для создания потока
        content_sr = self._actual_sample_rate if self._actual_sample_rate is not None else self.config.sample_rate
        device_sr = self._device_sample_rate
        
        # 🔧 ФИНАЛЬНЫЙ ФИКС: Получаем generation ПЕРЕД выходом из lock
        self._stream_gen += 1
        new_stream_gen = self._stream_gen
        
        # Выходим из lock для создания потока (тяжелая I/O операция)
        # (lock будет взят снова при финализации)
        
        # Создаем поток ВНЕ lock (с generation из closure)
        try:
            new_stream = self._create_audio_stream_unlocked(
                device_id=device_id,
                content_sr=content_sr,
                device_sr=device_sr,
                stream_gen=new_stream_gen  # Передаем generation
            )
            
            if new_stream is None:
                logger.error("❌ Не удалось создать аудио поток")
                with self._stream_lock:
                    # Откатываем generation если не удалось создать
                    self._stream_gen -= 1
                return False
            
            # Снова под lock - финализация
            with self._stream_lock:
                self._audio_stream = new_stream
                self._stream_started = False  # Stream создан, но ещё не стартован
                actual_stream_sr = device_sr if device_sr and device_sr != content_sr else content_sr
                self._stream_sample_rate = actual_stream_sr
                
                # 🔧 PRODUCTION ФИКС #1: Обновляем generation СТРОГО ПОСЛЕ активации stream
                # Порядок: 1) stream создан, 2) stream стартован (lazy start), 3) generation обновлен
                # Пока stream не стартован - generation не обновляем (защита от раннего mute)
                # Generation будет обновлен в _ensure_stream_started() после старта
                
                # 🔧 ФИНАЛЬНЫЙ ФИКС: Проверяем нужен ли ресемплинг
                content_sr_actual = self._actual_sample_rate or self.config.sample_rate
                if actual_stream_sr != content_sr_actual:
                    # Ресемплинг нужен - проверяем доступность функции
                    if self._resample_audio_func is not None:
                        self._needs_resample = True
                        logger.info(
                            f"✅ [RESAMPLE] Stream создан с sr={actual_stream_sr}Hz, content_sr={content_sr_actual}Hz. "
                            f"Ресемплинг будет выполняться в callback."
                        )
                    else:
                        # Ресемплер недоступен - это fallback scenario, логируем предупреждение
                        self._needs_resample = True
                        if not self._resample_warning_logged:
                            logger.warning(
                                f"⚠️ [RESAMPLE] Stream создан с sr={actual_stream_sr}Hz (fallback), но content_sr={content_sr_actual}Hz. "
                                f"Ресемплер недоступен - playback будет пропущен. Требуется реализация ресемплинга."
                            )
                            self._resample_warning_logged = True
                else:
                    self._needs_resample = False
                    self._resample_warning_logged = False
                
                logger.info(
                    f"🔧 Аудио поток создан (device_id={device_id}, sr={self._stream_sample_rate}Hz, "
                    f"channels: {self.config.channels}, gen={new_stream_gen}, needs_resample={self._needs_resample})"
                )
                logger.debug("💡 Поток будет стартован при появлении первого чанка (lazy start)")
                return True

        except Exception as e:
            logger.error(f"❌ Ошибка создания аудио потока: {e}")
            with self._stream_lock:
                # Откатываем generation при ошибке
                self._stream_gen -= 1
            return False

    def _ensure_stream_started(self):
        """Убеждаемся что поток стартован (для lazy start)"""
        with self._stream_lock:
            if self._audio_stream is not None and not self._stream_started:
                try:
                    # 🔍 ДИАГНОСТИКА: Проверяем состояние перед стартом
                    logger.info(f"🔍 [OUTPUT] Стартуем поток: stream exists={self._audio_stream is not None}, started={self._stream_started}")

                    self._audio_stream.start()
                    self._stream_started = True
                    
                    # 🔧 PRODUCTION ФИКС #1: Обновляем generation СТРОГО ПОСЛЕ активации stream
                    # Порядок: 1) stream создан, 2) stream стартован, 3) generation обновлен
                    # Это защищает от раннего mute старого callback'а
                    if self._stream_gen > 0:
                        self._current_stream_gen = self._stream_gen
                        logger.info(f"✅ [STREAM] Поток активирован, generation обновлён: gen={self._current_stream_gen}")
                    
                    logger.info("▶️ Аудио поток стартован (lazy start)")

                    # 🔍 ДИАГНОСТИКА: Проверяем состояние после старта
                    stream_active = self._audio_stream.active if self._audio_stream else False
                    logger.info(f"🔍 [OUTPUT] Поток стартован: active={stream_active}")
                    
                    # ✅ КРИТИЧЕСКАЯ ПРОВЕРКА: Убеждаемся что поток действительно активен
                    if not stream_active:
                        logger.error("❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: Поток не активен после старта!")
                    else:
                        logger.info("✅ [OUTPUT] Поток активен, callback должен вызываться")
                except Exception as e:
                    logger.error(f"❌ Ошибка старта аудио потока: {e}")
            elif self._audio_stream is None:
                logger.error(f"❌ [OUTPUT] НЕ МОГУ СТАРТОВАТЬ: stream is None!")
            elif self._stream_started:
                logger.debug(f"✅ [OUTPUT] Поток уже стартован")
    
    def _stop_audio_stream(self):
        """Остановка аудио потока (публичный метод, берет lock)"""
        with self._stream_lock:
            self._stop_audio_stream_locked()
    
    def _stop_audio_stream_locked(self):
        """Остановка аудио потока (locked-версия, вызывается когда lock уже взят)"""
        try:
                if self._audio_stream is not None:
                    if self._stream_started:
                        self._audio_stream.stop()
                    self._audio_stream.close()
                    self._audio_stream = None
                    self._stream_started = False
                self._stream_sample_rate = None
                logger.info("🛑 Аудио поток остановлен")

        except Exception as e:
            logger.error(f"❌ Ошибка остановки аудио потока: {e}")
    
    @staticmethod
    def _is_bluetooth_device(name: str) -> bool:
        lowered = (name or "").lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpods", "beats", "headset", "earbud"))

    def _query_default_output_device(self):
        """Возвращает информацию о текущем системном выходном устройстве."""
        try:
            default_setting = sd.default.device
            logger.debug(f"🔍 [OUTPUT] sd.default.device = {default_setting}")

            output_device = None
            if hasattr(default_setting, '__getitem__'):
                try:
                    output_device = default_setting[1]
                    logger.debug(f"🔍 [OUTPUT] output_device ID = {output_device}")
                except IndexError:
                    output_device = None
                    logger.warning(f"⚠️ [OUTPUT] IndexError при получении output device из {default_setting}")

            device_info = sd.query_devices(output_device, 'output')
            logger.debug(f"🔍 [OUTPUT] device_info = {device_info}")
            return device_info
        except Exception as e:
            logger.error(f"❌ [OUTPUT] Не удалось определить выходное устройство: {e}")
            return None

    def _probe_output_format(self):
        """Определяет желаемые sample_rate и channels для текущего выхода."""
        if not self.config.auto_device_selection:
            return None, None, None

        device_info = self._query_default_output_device()
        if not device_info:
            return None, None, None

        device_name = device_info.get('name', 'unknown')

        raw_sample_rate = device_info.get('default_samplerate') or self.config.sample_rate
        try:
            sample_rate = int(raw_sample_rate)
        except Exception:
            sample_rate = self.config.sample_rate
        if sample_rate <= 0:
            sample_rate = self.config.sample_rate

        raw_channels = device_info.get('max_output_channels') or self.config.channels
        try:
            channels = int(raw_channels)
        except Exception:
            channels = self.config.channels
        if channels <= 0:
            channels = self.config.channels

        adjusted_channels = 1 if channels <= 1 else min(2, channels)
        effective_rate = sample_rate if sample_rate > 0 else self.config.sample_rate
        if self._is_bluetooth_device(device_name) and effective_rate <= 24000:
            adjusted_channels = 1

        return sample_rate, adjusted_channels, device_name

    def _sync_output_format(self, restart_stream: bool = False) -> bool:
        """Подстраивает sample_rate и channels под текущее выходное устройство (публичный метод)."""
        with self._stream_lock:
            return self._sync_output_format_locked(restart_stream=restart_stream)
    
    def _sync_output_format_locked(self, restart_stream: bool = False) -> bool:
        """
        Подстраивает sample_rate и channels под текущее выходное устройство (locked-версия).
        
        🔧 РЕФАКТОРИНГ: НЕ изменяет config.sample_rate (это content rate).
        Обновляет только _device_sample_rate и config.channels.
        """
        if not self.config.auto_device_selection:
            return False

        sample_rate, adjusted_channels, device_name = self._probe_output_format()
        if sample_rate is None and adjusted_channels is None:
            return False

        device_sr_changed = False
        channel_changed = False

        # 🔧 РЕФАКТОРИНГ: Обновляем _device_sample_rate, НЕ config.sample_rate
        if sample_rate is not None and sample_rate > 0 and sample_rate != self._device_sample_rate:
            logger.info(
                "🎛 Обновляем device_sample_rate: %s → %s (device=%s)",
                self._device_sample_rate,
                sample_rate,
                device_name or "unknown",
            )
            self._device_sample_rate = sample_rate
            device_sr_changed = True

        if adjusted_channels is not None and adjusted_channels > 0 and adjusted_channels != self.config.channels:
            logger.info(
                "🎛 Обновляем channels плеера: %s → %s (device=%s)",
                self.config.channels,
                adjusted_channels,
                device_name or "unknown",
            )
            self.config.channels = adjusted_channels
            channel_changed = True
            # 🔧 FIX: Проверяем наличие метода set_channels() перед вызовом
            if hasattr(self.chunk_buffer, 'set_channels'):
                try:
                    self.chunk_buffer.set_channels(adjusted_channels)
                except Exception as channel_err:
                    logger.debug(f"⚠️ Не удалось обновить каналы буфера: {channel_err}")
            else:
                logger.debug("🔍 [AUDIO_DEBUG] ChunkBuffer не поддерживает set_channels()")

        # 🔧 РЕФАКТОРИНГ: Пересоздание потока через единый механизм
        if restart_stream and (device_sr_changed or channel_changed) and self._audio_stream is not None:
            was_active = self.state_manager.is_playing or self.state_manager.is_paused
            reason = f"device_sr_changed={device_sr_changed}, channel_changed={channel_changed}"
            self._recreate_stream_if_needed_locked(reason=reason, device_id=None, incoming_sr=None)
            if was_active:
                self._ensure_stream_started()

        return device_sr_changed or channel_changed

    def resync_output_device(self) -> bool:
        """Переопределяет формат вывода и перезапускает поток при необходимости."""
        with self._stream_lock:
            # 🔧 РЕФАКТОРИНГ: Идемпотентная проверка - если device_id тот же и поток корректен, просто return False
            current_device = self._query_default_output_device()
            current_device_id = current_device.get('index') if current_device else None
            
            if (self._audio_stream is not None and 
                self._current_device_id == current_device_id and 
                self._stream_sample_rate == (self._actual_sample_rate or self.config.sample_rate)):
                logger.debug("🔍 [RESYNC] Устройство и sample_rate не изменились, пересоздание не требуется")
                return False
            
            return self._sync_output_format_locked(restart_stream=True)
    
    def _recreate_stream_if_needed_locked(self, reason: str, device_id: Optional[int], incoming_sr: Optional[int], device_sr: Optional[int] = None) -> tuple[bool, bool]:
        """
        Единый метод пересоздания потока (locked-версия).
        
        🔧 ПРАВИЛО: НЕ делает I/O, не ходит в CoreAudio/PortAudio, не читает "default device".
        Все device queries должны быть выполнены ВНЕ lock.
        
        Вызывается из:
        - add_audio_data (под lock)
        - resync_output_device (под lock)
        
        Args:
            reason: Причина пересоздания (для логирования)
            device_id: ID устройства (ОБЯЗАТЕЛЬНО передан извне, не None если нужен)
            incoming_sr: Sample rate входящего контента (None = использовать текущий)
            device_sr: Sample rate устройства (опционально, для fallback)
        
        Returns:
            (recreated: bool, need_device: bool)
            - recreated: True если поток был пересоздан, False если не требовалось
            - need_device: True если требуется device_id для пересоздания (выполнить ВНЕ lock)
        """
        # 🔧 ЗАЩИТА ОТ ЗАЛИПАНИЯ: Проверяем таймаут пересоздания
        if self._recreating_stream:
            if self._recreating_stream_start_time is not None:
                elapsed = time.time() - self._recreating_stream_start_time
                if elapsed > 5.0:  # 5 секунд - критический таймаут
                    logger.error(
                        f"❌ [RECREATE] КРИТИЧЕСКАЯ ОШИБКА: _recreating_stream залипло на {elapsed:.1f}s! "
                        f"Принудительно сбрасываем флаг. Возможна проблема с драйвером/PortAudio."
                    )
                    self._recreating_stream = False
                    self._recreating_stream_start_time = None
                else:
                    logger.debug(
                        f"🔍 [RECREATE] Поток уже пересоздается другим потоком (elapsed={elapsed:.1f}s), "
                        f"пропускаем (reason={reason}, thread={threading.current_thread().name})"
                    )
                    return (False, False)
            else:
                # Флаг True, но нет времени старта - сбрасываем
                logger.warning("⚠️ [RECREATE] _recreating_stream=True без _recreating_stream_start_time, сбрасываем")
                self._recreating_stream = False
        
        # Вычисляем нужные условия (БЕЗ I/O операций!)
        need_recreate = False
        recreate_reason = ""
        need_device = False
        
        # 1) Проверка sample_rate mismatch
        # 🔧 FIX: Сравниваем incoming_sr с content rate, а не с stream rate
        # Если ресемплинг включен, stream rate (device) != content rate - это нормально
        if incoming_sr is not None:
            current_content_sr = self._actual_sample_rate if self._actual_sample_rate is not None else self.config.sample_rate
            # Пересоздаем только если изменился content rate, а не если content != device
            if self._audio_stream is not None and current_content_sr != incoming_sr:
                need_recreate = True
                recreate_reason = f"sample_rate_mismatch (content={current_content_sr}Hz, incoming={incoming_sr}Hz)"
        
        # 2) Проверка device changed
        # 🔧 КРИТИЧНО: НЕ вызываем _query_default_output_device() здесь!
        if device_id is None:
            # Если device_id не передан, но нужно проверить device change - требуем device_id
            if self._audio_stream is None or self._current_device_id is None:
                need_recreate = True
                recreate_reason = "stream_not_exists_or_device_unknown"
                need_device = True  # Требуем device_id для пересоздания
        elif device_id != self._current_device_id:
            need_recreate = True
            recreate_reason = f"device_changed (old={self._current_device_id}, new={device_id})"
        
        # 3) Проверка: поток не существует
        if self._audio_stream is None and not need_device:
            need_recreate = True
            recreate_reason = "stream_not_exists"
        
        if not need_recreate:
            return (False, False)
        
        if need_device:
            # Требуется device_id, но он не передан - возвращаем флаг
            logger.debug(f"🔍 [RECREATE] Требуется device_id для пересоздания (reason={recreate_reason})")
            return (False, True)
        
        # 🔧 ДВУХФАЗНОЕ ПЕРЕСОЗДАНИЕ: Под lock только решение и флаги, I/O операции ВНЕ lock
        prev_device_id = self._current_device_id
        prev_stream_sr = self._stream_sample_rate
        thread_name = threading.current_thread().name
        
        # Фаза 1: Под lock - решение, флаги, отсоединение ссылки
        old_stream = self._audio_stream
        was_started = self._stream_started  # Сохраняем состояние ПЕРЕД отсоединением
        old_stream_gen = self._current_stream_gen  # Сохраняем generation старого stream
        
        # 🔧 ФИНАЛЬНЫЙ ФИКС: Увеличиваем generation ПЕРЕД отсоединением
        self._stream_gen += 1
        new_stream_gen = self._stream_gen
        
        self._audio_stream = None  # Отсоединяем ссылку сразу (другие потоки видят None)
        self._stream_started = False
        self._stream_sample_rate = None
        
        self._recreating_stream = True
        self._recreating_stream_start_time = time.time()
        
        # Сохраняем параметры для фазы 2 (ВНЕ lock)
        recreate_params = {
            'reason': reason,
            'recreate_reason': recreate_reason,
            'device_id': device_id,
            'incoming_sr': incoming_sr,
            'device_sr': device_sr or self._device_sample_rate,
            'prev_device_id': prev_device_id,
            'prev_stream_sr': prev_stream_sr,
            'thread_name': thread_name,
            'old_stream_gen': old_stream_gen,
            'new_stream_gen': new_stream_gen
        }
        
        # 🔍 ДЕТАЛЬНОЕ ЛОГИРОВАНИЕ
        logger.info(
            f"🔄 [RECREATE] Начало пересоздания потока: {recreate_reason} | "
            f"reason={reason} | thread={thread_name} | "
            f"prev_device={prev_device_id}→new={device_id} | "
            f"prev_stream_sr={prev_stream_sr}Hz→incoming={incoming_sr}Hz | "
            f"content_sr={self._actual_sample_rate or self.config.sample_rate}Hz | "
            f"device_sr={device_sr or self._device_sample_rate}Hz | "
            f"stream_gen={old_stream_gen}→{new_stream_gen}"
        )
        
        # Выходим из lock для тяжелых операций
        # (lock будет взят снова в _finish_recreate_locked)
        
        # Фаза 2: ВНЕ lock - тяжелые I/O операции
        try:
            # Останавливаем старый поток (может быть медленным)
            # was_started уже сохранен выше (перед отсоединением)
            if old_stream is not None:
                try:
                    if was_started:
                        old_stream.stop()
                    old_stream.close()
                except Exception as e:
                    logger.warning(f"⚠️ [RECREATE] Ошибка при остановке старого потока: {e}")
            
            # Создаем новый поток (может быть медленным)
            # 🔧 ФИНАЛЬНЫЙ ФИКС: Передаем generation как параметр (уже увеличен под lock выше)
            new_stream = self._create_audio_stream_unlocked(
                device_id=device_id,
                content_sr=incoming_sr or self._actual_sample_rate or self.config.sample_rate,
                device_sr=device_sr or self._device_sample_rate,
                stream_gen=new_stream_gen  # Передаем generation из recreate_params
            )
            
            # Фаза 3: Снова под lock - финализация
            with self._stream_lock:
                return self._finish_recreate_locked(new_stream, recreate_params)
                
        except Exception as e:
            logger.error(f"❌ [RECREATE] Ошибка пересоздания потока: {e}", exc_info=True)
            with self._stream_lock:
                self._recreating_stream = False
                self._recreating_stream_start_time = None
            return (False, False)
    
    def _finish_recreate_locked(self, new_stream: Optional[sd.OutputStream], recreate_params: dict) -> tuple[bool, bool]:
        """Финальная фаза пересоздания потока (под lock)"""
        try:
            if new_stream is None:
                logger.error(f"❌ [RECREATE] Не удалось создать новый поток")
                self._recreating_stream = False
                self._recreating_stream_start_time = None
                return (False, False)
            
            # Подставляем новый stream
            self._audio_stream = new_stream
            self._stream_started = False  # Stream создан, но ещё не стартован
            actual_stream_sr = recreate_params.get('device_sr') or recreate_params.get('incoming_sr') or self.config.sample_rate
            self._stream_sample_rate = actual_stream_sr
            if recreate_params.get('device_id') is not None:
                self._current_device_id = recreate_params['device_id']
                # 🔧 PRODUCTION ФИКС #4: Кэшируем последний успешный device
                self._last_valid_device_id = recreate_params['device_id']
                self._last_valid_device_sr = actual_stream_sr
            
            # 🔧 PRODUCTION ФИКС #1: Generation будет обновлён в _ensure_stream_started() после старта
            # Порядок: 1) stream создан, 2) stream стартован, 3) generation обновлен
            new_stream_gen = recreate_params.get('new_stream_gen', self._stream_gen)
            # НЕ обновляем _current_stream_gen здесь - только после активации stream
            
            # 🔧 ФИНАЛЬНЫЙ ФИКС: Проверяем нужен ли ресемплинг
            content_sr_actual = recreate_params.get('incoming_sr') or self._actual_sample_rate or self.config.sample_rate
            if actual_stream_sr != content_sr_actual:
                # Ресемплинг нужен - проверяем доступность функции
                if self._resample_audio_func is not None:
                    self._needs_resample = True
                    logger.info(
                        f"✅ [RESAMPLE] Stream создан с sr={actual_stream_sr}Hz, content_sr={content_sr_actual}Hz. "
                        f"Ресемплинг будет выполняться в callback."
                    )
                else:
                    # Ресемплер недоступен - это fallback scenario, логируем предупреждение
                    self._needs_resample = True
                    if not self._resample_warning_logged:
                        logger.warning(
                            f"⚠️ [RESAMPLE] Stream создан с sr={actual_stream_sr}Hz (fallback), но content_sr={content_sr_actual}Hz. "
                            f"Ресемплер недоступен - playback будет пропущен. Требуется реализация ресемплинга."
                        )
                        self._resample_warning_logged = True
            else:
                self._needs_resample = False
                self._resample_warning_logged = False
            
            # Обновляем метрики
            self._stream_recreate_count += 1
            reason_entry = (
                f"{recreate_params['recreate_reason']} | reason={recreate_params['reason']} | "
                f"thread={recreate_params['thread_name']} | "
                f"prev_device={recreate_params['prev_device_id']}→new={recreate_params['device_id']} | "
                f"prev_sr={recreate_params['prev_stream_sr']}Hz→new={self._stream_sample_rate}Hz | "
                f"gen={recreate_params.get('old_stream_gen', '?')}→{new_stream_gen}"
            )
            self._stream_recreate_reasons.append(reason_entry)
            if len(self._stream_recreate_reasons) > 10:
                self._stream_recreate_reasons.pop(0)
            
            elapsed = time.time() - self._recreating_stream_start_time
            elapsed_ms = elapsed * 1000
            
            # 🔧 PRODUCTION ФИКС #5: Метрика времени recreate
            self._recreate_total_ms_history.append(elapsed_ms)
            if len(self._recreate_total_ms_history) > self._max_recreate_history:
                self._recreate_total_ms_history.pop(0)
            
            logger.info(
                f"✅ [RECREATE] Поток пересоздан успешно (count={self._stream_recreate_count}, "
                f"elapsed={elapsed:.3f}s ({elapsed_ms:.1f}ms), new_device={recreate_params['device_id']}, new_sr={self._stream_sample_rate}Hz, "
                f"gen={new_stream_gen}, needs_resample={self._needs_resample})"
            )
            
            return (True, False)
            
        except Exception as e:
            logger.error(f"❌ [RECREATE] Ошибка финализации пересоздания: {e}", exc_info=True)
            return (False, False)
        finally:
            self._recreating_stream = False
            self._recreating_stream_start_time = None
    
    def _make_audio_callback(self, stream_gen: int, stream_sr: int, content_sr: int):
        """
        🔧 ФИНАЛЬНЫЙ ФИКС: Создает callback с closure, захватывающим generation и sample rates.
        
        Это делает generation "per-callback", а не "per-object", защищая от перекрёстной порчи.
        
        Args:
            stream_gen: Generation этого конкретного stream
            stream_sr: Sample rate потока
            content_sr: Sample rate контента (для ресемплинга)
        """
        needs_resample = (stream_sr != content_sr) and (self._resample_audio_func is not None)
        
        def audio_callback(outdata, frames, time_info, status):
            """
            Callback для воспроизведения аудио с per-callback generation guard.
            """
            try:
                # 🔧 PRODUCTION ФИКС #5: Tripwires - проверка status (только счётчики, логи вне callback)
                if status:
                    # Проверяем underflow (только счётчик, логирование вне callback)
                    if hasattr(status, 'output_underflow') and status.output_underflow:
                        self._callback_underrun_count += 1
                        # Логирование вынесено вне callback (rate-limited в основном коде)

                # 🔧 ФИНАЛЬНЫЙ ФИКС: Проверяем generation через closure (per-callback, не per-object)
                # Читаем current_gen БЕЗ lock (быстрое чтение int, атомарно на Python)
                current_gen = self._current_stream_gen
                if stream_gen != current_gen:
                    # Stream был пересоздан - этот callback устарел
                    self._callback_gen_mismatch_count += 1
                    outdata[:] = 0
                    if not hasattr(self, '_callback_stale_warning_logged') or not self._callback_stale_warning_logged:
                        logger.debug(f"🔍 [CALLBACK] Устаревший callback (gen={stream_gen} != current={current_gen}), пропускаем")
                        self._callback_stale_warning_logged = True
                    return

                # Получаем данные из буфера (может быть 1D или 2D, dtype: int16)
                data = self.chunk_buffer.get_playback_data(frames)
                
                # 🔧 PRODUCTION ФИКС #3: Проверка формы данных и dtype
                if len(data) > 0:
                    # 🔧 PRODUCTION ФИКС #1: Нормализуем dtype: int16 → float32 (симметрично)
                    if data.dtype == np.int16:
                        # Используем 32768.0 для симметрии (int16: -32768..32767)
                        data = data.astype(np.float32) / 32768.0  # Нормализация [-1.0, 1.0]
                    elif data.dtype not in [np.float32, np.float64]:
                        data = data.astype(np.float32)
                    
                    # Нормализуем форму: всегда 2D
                    if data.ndim == 1:
                        data = data.reshape(-1, 1)
                
                # 🔧 ФИНАЛЬНЫЙ ФИКС: Ресемплинг если нужен (с кэшированием коэффициентов)
                if needs_resample and len(data) > 0:
                    resample_start = time.time()
                    try:
                        # Ресемплим каждый канал отдельно
                        if data.ndim == 1:
                            # 1D → ресемплим напрямую
                            data_1d = self._resample_audio_func(data, content_sr, stream_sr)
                            # Проверяем результат
                            if data_1d.ndim == 1:
                                data = data_1d.reshape(-1, 1)
                            else:
                                data = data_1d
                        else:
                            # 2D → ресемплим каждый канал отдельно
                            resampled_channels = []
                            for ch in range(data.shape[1]):
                                channel_data = data[:, ch]
                                resampled_ch = self._resample_audio_func(channel_data, content_sr, stream_sr)
                                resampled_channels.append(resampled_ch)
                            
                            # Объединяем каналы (все должны быть одинаковой длины после ресемплинга)
                            if resampled_channels:
                                # Берем длину первого канала (все должны быть одинаковыми)
                                target_len = len(resampled_channels[0])
                                # Создаем 2D массив
                                data = np.zeros((target_len, len(resampled_channels)), dtype=data.dtype)
                                for ch_idx, resampled_ch in enumerate(resampled_channels):
                                    actual_len = min(target_len, len(resampled_ch))
                                    data[:actual_len, ch_idx] = resampled_ch[:actual_len]
                        
                        # 🔧 PRODUCTION ФИКС #2: Метрика времени ресемплинга
                        resample_ms = (time.time() - resample_start) * 1000
                        self._callback_resample_ms_history.append(resample_ms)
                        if len(self._callback_resample_ms_history) > self._max_recreate_history:
                            self._callback_resample_ms_history.pop(0)
                        
                    except Exception as e:
                        # 🔧 PRODUCTION: Только счётчик в callback, логирование вне callback
                        # Ошибка ресемплинга - критично, но логируем вне callback
                        if not hasattr(self, '_resample_error_count'):
                            self._resample_error_count = 0
                        self._resample_error_count += 1
                        outdata[:] = 0
                        return
                
                # 🔧 PRODUCTION ФИКС #4: Всегда обнуляем outdata сначала (убирает мусор/предыдущие значения)
                outdata[:] = 0
                
                # Формируем выходные данные (ожидаем 2D)
                if len(data) == 0:
                    # Данных нет - outdata уже обнулён
                    return
                
                # ✅ ИСПРАВЛЕНИЕ: Проверяем и нормализуем форму данных
                if data.ndim == 1:
                    # 1D → 2D: (frames,) → (frames, 1)
                    data = data.reshape(-1, 1)
                
                # 🔧 PRODUCTION ФИКС #2: Preallocated buffer вместо np.vstack (быстрее, без лишних аллокаций)
                data_ch = data.shape[1]
                out_ch = self.config.channels
                data_frames = data.shape[0]
                
                # Создаём буфер нужного размера заранее (1 аллокация вместо 2+копий)
                if data_frames < frames:
                    # Нужно добить нулями - создаём буфер frames x channels
                    out = np.zeros((frames, out_ch), dtype=np.float32)
                    n = min(data_frames, frames)
                    # Копируем данные в начало буфера
                    if data_ch == 1 and out_ch >= 2:
                        # Моно → стерео: дублируем канал
                        out[:n, 0] = data[:n, 0]
                        out[:n, 1] = data[:n, 0]
                    elif data_ch >= 2 and out_ch == 1:
                        # Стерео → моно: среднее (L+R)/2
                        out[:n, 0] = 0.5 * (data[:n, 0] + data[:n, 1])
                    else:
                        # Одинаковое количество каналов или просто копируем
                        n_ch = min(data_ch, out_ch)
                        out[:n, :n_ch] = data[:n, :n_ch]
                    data = out
                elif data_frames > frames:
                    # Нужно обрезать - создаём буфер frames x channels
                    out = np.zeros((frames, out_ch), dtype=np.float32)
                    if data_ch == 1 and out_ch >= 2:
                        # Моно → стерео: дублируем канал
                        out[:, 0] = data[:frames, 0]
                        out[:, 1] = data[:frames, 0]
                    elif data_ch >= 2 and out_ch == 1:
                        # Стерео → моно: среднее (L+R)/2
                        out[:, 0] = 0.5 * (data[:frames, 0] + data[:frames, 1])
                    else:
                        # Одинаковое количество каналов или просто копируем
                        n_ch = min(data_ch, out_ch)
                        out[:, :n_ch] = data[:frames, :n_ch]
                    data = out
                else:
                    # data_frames == frames - просто конвертируем каналы
                    out = np.zeros((frames, out_ch), dtype=np.float32)
                    if data_ch == 1 and out_ch >= 2:
                        # Моно → стерео: дублируем канал
                        out[:, 0] = data[:, 0]
                        out[:, 1] = data[:, 0]
                    elif data_ch >= 2 and out_ch == 1:
                        # Стерео → моно: среднее (L+R)/2
                        out[:, 0] = 0.5 * (data[:, 0] + data[:, 1])
                    else:
                        # Одинаковое количество каналов или просто копируем
                        n_ch = min(data_ch, out_ch)
                        out[:, :n_ch] = data[:, :n_ch]
                    data = out
                
                # 🔧 PRODUCTION ФИКС #1: Конвертируем обратно в int16 если нужно (симметрично)
                if outdata.dtype == np.int16:
                    # Симметричная конвертация: избегаем микроклиппинга
                    data = np.clip(data, -1.0, 1.0 - (1.0/32768.0))
                    data = (data * 32768.0).astype(np.int16)
                elif data.dtype != outdata.dtype:
                    data = data.astype(outdata.dtype)
                
                # 🔧 PRODUCTION ФИКС #3: Soft guard вместо assert (безопасно в production)
                if data.shape[0] != frames:
                    # Инвариант нарушен - только счётчик, логирование вне callback
                    if not hasattr(self, '_callback_shape_mismatch_count'):
                        self._callback_shape_mismatch_count = 0
                    self._callback_shape_mismatch_count += 1
                    outdata[:] = 0
                    return
                
                # Заполняем outdata (data.shape[0] == frames гарантированно)
                outdata[:, :] = data[:, :]
                
            except Exception as e:
                # 🔧 PRODUCTION: Только счётчик в callback, логирование вне callback
                # Критическая ошибка - но логируем вне callback для безопасности
                if not hasattr(self, '_callback_error_count'):
                    self._callback_error_count = 0
                self._callback_error_count += 1
                outdata[:] = 0
        
        return audio_callback
    
    def _create_audio_stream_unlocked(self, device_id: Optional[int], content_sr: int, device_sr: Optional[int], stream_gen: int) -> Optional[sd.OutputStream]:
        """
        Создание аудио потока ВНЕ lock (тяжелая I/O операция).
        
        🔧 FALLBACK: Пробуем content_sr, если не получается - пробуем device_sr.
        🔧 ФИНАЛЬНЫЙ ФИКС: Используем closure для per-callback generation guard.
        
        Args:
            device_id: ID устройства
            content_sr: Sample rate контента
            device_sr: Sample rate устройства
            stream_gen: Generation для этого stream (передается извне, под lock)
        """
        
        # Пробуем content_sr сначала (ПРЕДПОЧТИТЕЛЬНО - всегда открываем на content_sr)
        playback_sample_rate = content_sr
        
        # Если device_sr известен и отличается - предупреждаем
        if device_sr is not None and device_sr != content_sr:
            logger.info(
                f"🔍 [STREAM_RATE] Content rate ({content_sr}Hz) != Device rate ({device_sr}Hz). "
                f"Пробуем создать поток с content_rate, при ошибке будет fallback на device_rate с ресемплингом."
            )
        
        # Попытка 1: content_sr (ПРЕДПОЧТИТЕЛЬНО)
        try:
            # 🔧 ФИНАЛЬНЫЙ ФИКС: Создаем callback через closure с захваченным gen
            callback = self._make_audio_callback(stream_gen, playback_sample_rate, content_sr)
            
            stream_config = {
                'device': device_id,
                'channels': self.config.channels,
                'dtype': self.config.dtype,
                'samplerate': playback_sample_rate,
                'blocksize': self.config.buffer_size,
                'callback': callback  # ✅ Closure с per-callback generation
            }
            
            logger.info(f"🔧 [STREAM_CREATE] Пробуем создать поток: device={device_id}, sr={playback_sample_rate}Hz, gen={stream_gen}")
            stream = sd.OutputStream(**stream_config)
            logger.info(f"✅ [STREAM_CREATE] Поток создан с content_rate={playback_sample_rate}Hz")
            return stream
            
        except Exception as e:
            logger.warning(f"⚠️ [STREAM_CREATE] Не удалось создать поток с content_rate={playback_sample_rate}Hz: {e}")
            # 🔧 PRODUCTION ФИКС #5: Метрика неудачных открытий
            self._stream_open_fail_count += 1
            
            # Попытка 2: device_sr (fallback) - ТОЛЬКО если content_sr не работает
            if device_sr is not None and device_sr != content_sr:
                try:
                    playback_sample_rate = device_sr
                    
                    # 🔧 ФИНАЛЬНЫЙ ФИКС: Создаем callback с ресемплингом для fallback
                    callback = self._make_audio_callback(stream_gen, playback_sample_rate, content_sr)
                    
                    stream_config['samplerate'] = playback_sample_rate
                    stream_config['callback'] = callback
                    
                    logger.info(f"🔧 [STREAM_CREATE] Fallback: пробуем device_rate={playback_sample_rate}Hz с ресемплингом")
                    stream = sd.OutputStream(**stream_config)
                    logger.info(
                        f"✅ [STREAM_CREATE] Поток создан с device_rate={playback_sample_rate}Hz (fallback). "
                        f"Ресемплинг {content_sr}Hz → {device_sr}Hz будет выполняться в callback."
                    )
                    return stream
                except Exception as e2:
                    logger.error(f"❌ [STREAM_CREATE] Не удалось создать поток даже с device_rate={playback_sample_rate}Hz: {e2}")
                    return None
            else:
                logger.error(f"❌ [STREAM_CREATE] device_sr не известен, fallback невозможен")
                return None

    def _detect_output_device_change(self) -> tuple[bool, Optional[int], Optional[int]]:
        """
        🔧 PURE функция: Обнаруживает изменение output устройства БЕЗ мутации shared state.

        Использует NAME-based сравнение (аналогично INPUT логике).

        Returns:
            (changed: bool, device_id: Optional[int], device_sr: Optional[int])
            - changed: True если устройство изменилось (или первый запуск)
            - device_id: ID текущего устройства (если обнаружено)
            - device_sr: Sample rate устройства (если обнаружено)
        """
        if not self.config.auto_output_device_switch:
            logger.debug("🔍 [OUTPUT] Автопереключение отключено (auto_output_device_switch=False)")
            return (False, None, None)

        try:
            logger.debug("🔍 [OUTPUT] Проверка смены устройства...")

            # Получаем текущее default output устройство
            current_device_info = self._query_default_output_device()
            if not current_device_info:
                logger.debug("⚠️ [OUTPUT] Не удалось получить текущее устройство")
                return (False, None, None)

            current_device_name = current_device_info.get('name')
            if not current_device_name:
                logger.debug("⚠️ [OUTPUT] У устройства нет имени")
                return (False, None, None)

            # 🔧 PURE: Читаем shared state БЕЗ мутации (только для сравнения)
            # В идеале это должно быть через snapshot, но для простоты оставляем так
            old_device_name = self.output_device_name

            # Извлекаем device_id и device_sr
            device_id = current_device_info.get('index')
            device_sr = current_device_info.get('default_samplerate')
            if device_sr:
                try:
                    device_sr = int(device_sr)
                except:
                    device_sr = None

            # Проверяем изменилось ли
            if old_device_name is None:
                # Первый запуск
                logger.info(f"🔊 [OUTPUT] Начальное устройство: \"{current_device_name}\" (ID={device_id}, SR={device_sr}Hz)")
                return (True, device_id, device_sr)

            if current_device_name != old_device_name:
                # Устройство изменилось
                logger.info(
                    f"🔄 [OUTPUT] Смена устройства: \"{old_device_name}\" → \"{current_device_name}\" "
                    f"(ID={device_id}, SR={device_sr}Hz)"
                )
                return (True, device_id, device_sr)

            # Устройство не изменилось
            logger.debug(f"✅ [OUTPUT] Устройство не изменилось: \"{current_device_name}\"")
            return (False, device_id, device_sr)

        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка проверки устройства: {e}")
            return (False, None, None)
    
    def _check_and_update_output_device(self) -> bool:
        """
        Устаревший метод (для обратной совместимости).
        Использует _detect_output_device_change() и обновляет shared state под lock.
        """
        changed, device_id, device_sr = self._detect_output_device_change()
        if changed:
            with self._stream_lock:
                if device_id is not None:
                    self._current_device_id = device_id
                if device_sr is not None:
                    self._device_sample_rate = device_sr
                # Обновляем имя устройства
                current_device = self._query_default_output_device()
                if current_device:
                    self.output_device_name = current_device.get('name')
        return changed

    def _audio_callback(self, outdata, frames, time_info, status):
        """
        УСТАРЕВШИЙ метод callback (для обратной совместимости).
        
        🔧 ФИНАЛЬНЫЙ ФИКС: Теперь используется _make_audio_callback() с closure для per-callback generation.
        Этот метод больше не используется при создании новых stream'ов.
        """
        try:
            if status:
                logger.warning(f"⚠️ Статус аудио потока: {status}")

            # 🔧 ФИНАЛЬНЫЙ ФИКС: Проверяем generation - если stream был пересоздан, не пишем данные
            # Читаем generation БЕЗ lock (быстрое чтение int, атомарно на Python)
            current_gen = self._current_stream_gen
            callback_stream_gen = getattr(self, '_callback_stream_gen', None)
            
            if callback_stream_gen is None:
                # Первый вызов - сохраняем generation
                callback_stream_gen = current_gen
                self._callback_stream_gen = callback_stream_gen
            elif callback_stream_gen != current_gen:
                # Stream был пересоздан - этот callback устарел
                # Заполняем нулями и выходим (не пишем в устаревший stream)
                outdata[:] = 0
                if not hasattr(self, '_callback_stale_warning_logged') or not self._callback_stale_warning_logged:
                    logger.debug(f"🔍 [CALLBACK] Устаревший callback (gen={callback_stream_gen} != current={current_gen}), пропускаем")
                    self._callback_stale_warning_logged = True
                return

            # 🔍 ДИАГНОСТИКА: Логируем time_info для проверки реального sample_rate
            if not hasattr(self, '_callback_first_logged'):
                # ИСПРАВЛЕНО: time_info - это cdata структура PortAudio, не словарь
                # Обращаемся к полям напрямую через getattr
                current_time = getattr(time_info, 'current_time', 0.0) if time_info else 0.0
                logger.info(f"🔍 [CALLBACK_DIAG] Первый callback: stream_sr={self._audio_stream.samplerate if self._audio_stream else 'N/A'}, actual_sr={self._actual_sample_rate}, config_sr={self.config.sample_rate}, current_time={current_time}, gen={callback_stream_gen}")
                self._callback_first_logged = True
                self._callback_start_time = current_time
                self._callback_total_frames = 0

            # 🔧 ФИНАЛЬНЫЙ ФИКС: Если нужен ресемплинг, но его нет - не воспроизводим (только буферизуем)
            if self._needs_resample:
                # Ресемплинг не реализован - не воспроизводим, только буферизуем
                outdata[:] = 0
                if not hasattr(self, '_resample_playback_skipped_logged') or not self._resample_playback_skipped_logged:
                    logger.warning(
                        f"⚠️ [RESAMPLE] Пропуск playback: требуется ресемплинг (stream_sr={self._stream_sample_rate}Hz != content_sr={self._actual_sample_rate or self.config.sample_rate}Hz), "
                        f"но ресемплер не реализован. Данные буферизуются, но не воспроизводятся."
                    )
                    self._resample_playback_skipped_logged = True
                return

            # Получаем данные из буфера (2D: frames x channels)
            data = self.chunk_buffer.get_playback_data(frames)
            
            # 🔍 КРИТИЧЕСКАЯ ДИАГНОСТИКА: Всегда логируем первые 20 вызовов
            if not hasattr(self, '_callback_debug_count'):
                self._callback_debug_count = 0
            if self._callback_debug_count < 20:
                buffer_size = self.chunk_buffer.buffer_size
                queue_size = self.chunk_buffer.queue_size
                has_data = len(data) > 0
                # ИСПРАВЛЕНО: time_info - это cdata структура PortAudio, не словарь
                current_time = getattr(time_info, 'current_time', 0.0) if time_info else 0.0
                if hasattr(self, '_callback_start_time'):
                    elapsed = current_time - self._callback_start_time
                else:
                    elapsed = 0.0
                self._callback_total_frames = getattr(self, '_callback_total_frames', 0) + frames
                
                # 🔍 ДИАГНОСТИКА: Проверяем реальный sample_rate потока
                stream_sr = self._audio_stream.samplerate if self._audio_stream else None
                logger.info(
                    f"🎵 [CALLBACK #{self._callback_debug_count}] frames={frames}, data_shape={data.shape if has_data else 'EMPTY'}, "
                    f"buffer_size={buffer_size}, queue_size={queue_size}, channels={self.config.channels}, "
                    f"stream_sr={stream_sr}, actual_sr={self._actual_sample_rate}, config_sr={self.config.sample_rate}, "
                    f"elapsed={elapsed:.3f}s, total_frames={self._callback_total_frames}"
                )
                self._callback_debug_count += 1
            elif self._callback_debug_count == 20:
                logger.info(f"🔇 [CALLBACK] Дальнейшее логирование callback отключено (работает нормально)")
                self._callback_debug_count += 1
            
            # Формируем выходные данные (ожидаем 2D)
            if len(data) == 0:
                outdata[:] = 0
            else:
                # ✅ ИСПРАВЛЕНИЕ: Проверяем и нормализуем форму данных
                if data.ndim == 1:
                    # 1D → 2D: (frames,) → (frames, 1)
                    data = data.reshape(-1, 1)
                
                # Нормализуем каналы
                if data.shape[1] != self.config.channels:
                    if data.shape[1] == 1 and self.config.channels > 1:
                        # Моно → стерео: дублируем канал
                        data = np.repeat(data, self.config.channels, axis=1)
                    elif data.shape[1] > 1 and self.config.channels == 1:
                        # Стерео → моно: берем первый канал
                        data = data[:, :1]
                
                # Копируем данные в outdata
                out_frames = min(frames, data.shape[0])
                out_channels = min(self.config.channels, data.shape[1])
                
                # Заполняем outdata
                outdata[:out_frames, :out_channels] = data[:out_frames, :out_channels]
                
                # Если каналов меньше - дублируем последний
                if out_channels < self.config.channels:
                    for ch in range(out_channels, self.config.channels):
                        outdata[:out_frames, ch] = data[:out_frames, out_channels - 1]
                
                # Заполняем остаток нулями
                if out_frames < frames:
                    outdata[out_frames:, :] = 0
                
        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}")
            outdata[:] = 0

    def reconfigure_channels(self, new_channels: int) -> bool:
        """Безопасно переинициализировать аудиовывод под новое число каналов (1..2)"""
        try:
            new_ch = 1 if new_channels <= 1 else 2
            if new_ch == self.config.channels:
                return True
            # Останавливаем текущий поток
            self._stop_audio_stream()
            # Обновляем конфиг и буфер
            self.config.channels = new_ch
            # 🔧 FIX: Проверяем наличие метода set_channels() перед вызовом
            if hasattr(self.chunk_buffer, 'set_channels'):
                try:
                    self.chunk_buffer.set_channels(new_ch)
                except Exception as e:
                    logger.debug(f"⚠️ Не удалось обновить каналы буфера: {e}")
            else:
                logger.debug("🔍 [AUDIO_DEBUG] ChunkBuffer не поддерживает set_channels()")
            # Запускаем заново если были в состоянии PLAYING
            if self.state_manager.is_playing or self.state_manager.is_paused:
                return self._start_audio_stream()
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка reconfigure_channels: {e}")
            return False
    
    def _playback_loop(self):
        """Основной цикл воспроизведения - упрощенная версия
        
        ВАЖНО: Этот цикл используется только для координации, реальное воспроизведение
        происходит через audio callback, который читает данные напрямую из буфера через get_playback_data().
        """
        try:
            logger.info("🔄 Playback loop запущен")
            logger.info(f"🔍 [PLAYBACK_LOOP] Начальное состояние: queue_size={self.chunk_buffer.queue_size}, buffer_size={self.chunk_buffer.buffer_size}")
            
            # 🔍 ИСПРАВЛЕНО: Упрощенная версия - callback сам читает данные через get_playback_data()
            # Этот цикл только ждет завершения воспроизведения всех чанков
            while not self._stop_event.is_set():
                # Проверяем паузу
                self._pause_event.wait()
                
                # 🔍 ИСПРАВЛЕНО: Не используем get_next_chunk() - его нет в ChunkBuffer
                # Вместо этого просто проверяем, есть ли данные в буфере
                queue_size_before = self.chunk_buffer.queue_size
                has_data = self.chunk_buffer.has_data
                queue_size_after = self.chunk_buffer.queue_size
                
                # 🔍 ИСПРАВЛЕНО: Callback сам читает данные через get_playback_data()
                # Этот цикл только ждет, пока все данные будут воспроизведены
                if has_data:
                    # Есть данные - callback их обработает
                    # Просто ждем небольшое время и проверяем снова
                    time.sleep(0.01)
                else:
                    # Нет чанков - проверяем нужно ли остановить поток (lazy stop)
                    if self.chunk_buffer.queue_size == 0 and self.chunk_buffer.buffer_size == 0:
                        # Очередь пустая - останавливаем поток для снижения нагрузки
                        with self._stream_lock:
                            if self._stream_started:
                                try:
                                    self._audio_stream.stop()
                                    self._stream_started = False
                                    logger.info("⏸️ Аудио поток остановлен (очередь пуста, lazy stop)")
                                except Exception as e:
                                    logger.error(f"❌ Ошибка остановки потока: {e}")
                    time.sleep(0.01)
            
            logger.info("🔄 Playback loop завершен")
            # Устанавливаем состояние IDLE после естественного завершения
            try:
                self.state_manager.set_state(PlaybackState.IDLE)
            except Exception:
                pass
            # Коллбек завершения воспроизведения (если задан)
            try:
                if self._on_playback_completed:
                    self._on_playback_completed()
            except Exception:
                pass
            
        except Exception as e:
            logger.error(f"❌ Ошибка в playback loop: {e}")
            self.state_manager.set_state(PlaybackState.ERROR)
    
    def _wait_for_chunk_completion(self, chunk_info: ChunkInfo, timeout: float = 30.0):
        """Ждать завершения воспроизведения чанка"""
        start_time = time.time()
        
        # Ожидаем, пока буфер воспроизведения не будет пустым
        # Это означает, что весь чанк был воспроизведен
        while time.time() - start_time < timeout:
            # Немедленный выход при запросе остановки
            if self._stop_event.is_set():
                logger.info(f"⏹️ Прерывание чанка {chunk_info.chunk_id} по stop_event")
                return
            if not self.chunk_buffer.has_data:
                logger.info(f"✅ Чанк {chunk_info.chunk_id} полностью воспроизведен")
                return
            
            time.sleep(0.01)
        
        logger.warning(f"⚠️ Таймаут ожидания завершения чанка {chunk_info.chunk_id}")
    
    def wait_for_completion(self, timeout: float = None) -> bool:
        """Ждать завершения воспроизведения всех чанков (без таймаута)"""
        return self.chunk_buffer.wait_for_completion(timeout)
    
    def set_callbacks(self, 
                     on_chunk_started: Optional[Callable[[ChunkInfo], None]] = None,
                     on_chunk_completed: Optional[Callable[[ChunkInfo], None]] = None,
                     on_playback_completed: Optional[Callable[[], None]] = None,
                     on_error: Optional[Callable[[Exception], None]] = None):
        """Установить callbacks"""
        self._on_chunk_started = on_chunk_started
        self._on_chunk_completed = on_chunk_completed
        self._on_playback_completed = on_playback_completed
        self._on_error = on_error
    
    def get_stats(self) -> Dict[str, Any]:
        """Получить статистику плеера"""
        return {
            'state': self.state_manager.current_state.value,
            'is_playing': self.state_manager.is_playing,
            'is_paused': self.state_manager.is_paused,
            'has_error': self.state_manager.has_error,
            'buffer_stats': self.chunk_buffer.get_stats(),
            'performance_stats': self._performance_monitor.get_stats()
        }
    
    def shutdown(self):
        """Завершение работы плеера"""
        try:
            # Останавливаем воспроизведение
            self.stop_playback()

            # Останавливаем мониторинг производительности
            self._performance_monitor.stop()

            # Очищаем буферы
            self.chunk_buffer.clear_all()

            # Очищаем кэш устройств (при завершении плеера)
            self.output_device_name = None
            self._current_playback_session_id = None
            logger.debug("🔍 [OUTPUT] Кэш устройств очищен при shutdown")

            logger.info("🛑 Плеер завершил работу")

        except Exception as e:
            logger.error(f"❌ Ошибка завершения работы плеера: {e}")












































    def get_status(self) -> Dict[str, Any]:
        """
        Получает статус плеера
        
        Returns:
            Dict с информацией о статусе
        """
        return {
            "state": self.state_manager.current_state.value,
            "chunk_count": self.chunk_buffer.queue_size,
            "buffer_size": self.chunk_buffer.buffer_size,
            "is_playing": self.state_manager.current_state == PlaybackState.PLAYING,
            "is_paused": self.state_manager.current_state == PlaybackState.PAUSED,
            "device_id": None,  # Используем системный дефолт
            "sample_rate": self.config.sample_rate,
            "channels": self.config.channels
        }
