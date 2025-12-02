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
# ✅ ФАЗА 3: Stream Config Resolver
from .stream_config_resolver import StreamConfigResolver

# ЦЕНТРАЛИЗОВАННАЯ КОНФИГУРАЦИЯ АУДИО
from config.unified_config_loader import unified_config

# ✅ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ УСТРОЙСТВ
from modules.audio_core import DeviceParamsNormalizer, OutputParams

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
        self.chunk_buffer = ChunkBuffer(max_memory_mb=self.config.max_memory_mb, channels=self.config.channels, dtype=buf_dtype)
        
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
        self._current_output_device_id: Optional[int] = None  # PortAudio ID текущего устройства
        self._current_playback_session_id: Optional[Any] = None  # Текущая сессия воспроизведения
        self._last_device_check_time: float = 0.0  # Время последней проверки устройства
        self._device_check_interval: float = 1.0  # Интервал проверки устройства (секунды)
        self._is_current_device_bluetooth: bool = False  # Флаг для определения BT устройства
        # ✅ FIX: Блокировка для защиты device tracking переменных от race conditions
        self._device_tracking_lock = threading.RLock()
        
        # Фоновый мониторинг output устройства
        self._output_monitor_thread: Optional[threading.Thread] = None
        self._stop_device_monitor = threading.Event()
        self._output_monitor_lock = threading.RLock()
        
        # ✅ КЭШ ОШИБОК: Хранит "плохие" конфигурации по имени устройства
        # Формат: {device_name: {'error_code': -10851, 'safe_config': {...}, 'timestamp': ...}}
        # Используется для предотвращения повторных ошибок при переподключении устройств
        # ⚠️ ВАЖНО: Должен быть создан ПЕРЕД StreamConfigResolver
        self._device_error_cache: Dict[str, Dict[str, Any]] = {}
        self._error_cache_lock = threading.RLock()
        
        # ✅ ФАЗА 3: Stream Config Resolver (создается ПОСЛЕ кэша ошибок)
        self._stream_config_resolver = StreamConfigResolver(
            default_sample_rate=self.config.sample_rate,
            default_channels=self.config.channels,
            default_dtype=self.config.dtype,
            default_buffer_size=self.config.buffer_size
        )
        # Устанавливаем ссылку на кэш ошибок
        self._stream_config_resolver.set_error_cache(self._device_error_cache, self._error_cache_lock)

        # ✅ ИТЕРАЦИЯ 2: Инициализация нормализатора параметров устройств (пока не используется)
        try:
            audio_config = unified_config.get_audio_config()
            normalizer_config = audio_config.get('normalization', {})
            if normalizer_config:
                self._params_normalizer = DeviceParamsNormalizer(normalizer_config)
                self._normalized_params: Optional[OutputParams] = None
                logger.debug("✅ DeviceParamsNormalizer инициализирован (готов к использованию)")
            else:
                logger.warning("⚠️ Конфигурация нормализации не найдена, используем fallback")
                self._params_normalizer = None
                self._normalized_params = None
        except Exception as e:
            logger.warning(f"⚠️ Ошибка инициализации нормализатора: {e}")
            self._params_normalizer = None
            self._normalized_params = None

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
            if not self._core_audio_manager.initialize():
                logger.error("❌ [AUDIO_ERROR] Ошибка инициализации Core Audio")
                return False
            logger.info("✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован")

            # Подстраиваемся под актуальный выходной маршрут
            self._sync_output_format()
            
            # Используем системное устройство по умолчанию от macOS
            if self.config.auto_device_selection:
                logger.info("🎯 Используем системное устройство по умолчанию от macOS")
                # Синхронизируем буфер под новое число каналов
                try:
                    self.chunk_buffer.set_channels(self.config.channels)
                except Exception:
                    pass
            
            # Логируем конфигурацию плеера для отладки
            logger.info(f"📊 [AUDIO_STATS] Конфигурация плеера: sample_rate={self.config.sample_rate}Hz, channels={self.config.channels}, dtype={self.config.dtype}")
            
            # Инициализация мониторинга производительности
            self._performance_monitor.start()
            
            # Запускаем фоновый мониторинг output устройства
            if self.config.auto_output_device_switch:
                self._start_output_monitoring()
            
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
            # ✅ НОВАЯ ЛОГИКА: Проверка смены output устройства
            session_id = metadata.get('session_id') if metadata else None
            import time
            current_time = time.time()
            
            # ✅ FIX: Проверяем смену устройства в следующих случаях:
            # 1. Новая сессия
            # 2. Первый запуск (поток ещё не стартован)
            # 3. Прошло достаточно времени с последней проверки (для обнаружения подключения устройств во время воспроизведения)
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств увеличиваем интервал проверки (они редко меняются)
            with self._device_tracking_lock:
                # Для BT устройств используем больший интервал (5 секунд вместо 1)
                check_interval = 5.0 if self._is_current_device_bluetooth else self._device_check_interval
                should_check_device = (
                    session_id != self._current_playback_session_id or 
                    not self._stream_started or
                    (current_time - self._last_device_check_time) >= check_interval
                )
            
            if should_check_device:
                with self._device_tracking_lock:
                    logger.debug(f"🔍 [OUTPUT] Проверка устройства: session={session_id}, started={self._stream_started}, time_since_check={current_time - self._last_device_check_time:.2f}s")

                # ✅ Проверяем И обновляем output устройство (атомарная операция)
                # НО! БЕЗ sd._terminate() внутри - это уничтожит потоки!
                device_changed = self._check_and_update_output_device()
                self._last_device_check_time = current_time  # Обновляем время последней проверки

                if device_changed:
                    # Устройство изменилось (или первый запуск)
                    logger.info("🔄 [OUTPUT] Устройство изменилось - пересоздаём поток")

                    # 1. Останавливаем старый поток если он существует
                    if self._audio_stream is not None:
                        logger.debug("🔄 [OUTPUT] Останавливаем старый поток")
                        self._stop_audio_stream()

                    # 2. ✅ НЕ ВЫЗЫВАЕМ sd._terminate() / sd._initialize()!
                    # Это может вызвать segfault/crash в многопоточной среде

                    # 3. Получаем ID текущего дефолтного OUTPUT устройства
                    current_device = self._query_default_output_device()
                    device_id = current_device.get('index') if current_device else None
                    logger.info(f"🔍 [OUTPUT] Текущее OUTPUT устройство ID: {device_id}")

                    # 4. Создаём новый поток для конкретного устройства
                    logger.info("🔄 [OUTPUT] Создаём новый поток для нового устройства")
                    if not self._start_audio_stream(device_id=device_id):
                        logger.error("❌ [OUTPUT] Не удалось создать поток для нового устройства")
                        # Продолжаем с существующим потоком или без потока

                # Обновляем текущую сессию
                with self._device_tracking_lock:
                    if session_id != self._current_playback_session_id:
                        self._current_playback_session_id = session_id
                        logger.debug(f"🔍 [OUTPUT] Обновлена сессия: {session_id}")

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

            # Добавляем в буфер
            chunk_id = self.chunk_buffer.add_chunk(audio_data, priority, metadata)

            # ✅ ИСПРАВЛЕНИЕ: Если поток не существует (например, был остановлен lazy stop),
            # создаём новый перед попыткой старта
            if self._audio_stream is None:
                logger.debug("🔍 [OUTPUT] Поток не существует, создаём новый...")
                # Получаем текущее устройство
                current_device = self._query_default_output_device()
                device_id = current_device.get('index') if current_device else None
                self._start_audio_stream(device_id=device_id)

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
            # ✅ FIX: Если состояние ERROR, сбрасываем в IDLE для повторной попытки
            if self.state_manager.current_state == PlaybackState.ERROR:
                logger.warning("⚠️ Состояние ERROR, сбрасываем в IDLE для повторной попытки")
                self.state_manager.set_state(PlaybackState.IDLE)
            
            # Проверяем, что можем запустить воспроизведение
            if self.state_manager.current_state not in [PlaybackState.IDLE, PlaybackState.PAUSED]:
                logger.warning(f"⚠️ Невозможно запустить воспроизведение в текущем состоянии: {self.state_manager.current_state}")
                # ✅ FIX: Если поток не создан, создаём его и пробуем запустить
                if self._audio_stream is None:
                    logger.info("🔄 Поток не создан, создаём и пробуем запустить...")
                    current_device = self._query_default_output_device()
                    device_id = current_device.get('index') if current_device else None
                    if self._start_audio_stream(device_id=device_id):
                        self._ensure_stream_started()
                        self.state_manager.set_state(PlaybackState.PLAYING)
                        return True
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
        Запуск аудио потока с lazy start (создаём без старта)

        Args:
            sync_output: Синхронизировать формат с устройством
            device_id: ID устройства (None = использовать дефолтное)
        """
        try:
            logger.info(f"🔍 [OUTPUT] _start_audio_stream вызван: sync_output={sync_output}, device_id={device_id}")
            
            with self._stream_lock:
                # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Убеждаемся, что старый поток полностью закрыт перед созданием нового
                if self._audio_stream is not None:
                    logger.warning("⚠️ [OUTPUT] Обнаружен существующий поток при создании нового, закрываем...")
                    stream_ref = self._audio_stream  # Сохраняем ссылку
                    
                    try:
                        # Проверяем состояние потока
                        is_active = stream_ref.active if hasattr(stream_ref, 'active') else False
                        logger.warning(f"⚠️ [OUTPUT] Существующий поток: active={is_active}, started={self._stream_started}")
                        
                        # Если поток активен, закрываем его
                        if is_active or self._stream_started:
                            logger.info("🔄 [OUTPUT] Закрываем существующий активный поток перед созданием нового...")
                            try:
                                if self._stream_started:
                                    stream_ref.stop()
                                    self._stream_started = False
                            except Exception as e:
                                logger.warning(f"⚠️ [OUTPUT] Ошибка при остановке существующего потока: {e}")
                            
                            try:
                                stream_ref.close()
                            except Exception as e:
                                logger.warning(f"⚠️ [OUTPUT] Ошибка при закрытии существующего потока: {e}")
                        else:
                            # Поток существует, но не активен - просто закрываем
                            logger.debug("🔄 [OUTPUT] Закрываем неактивный поток...")
                            try:
                                stream_ref.close()
                            except Exception:
                                pass
                        
                        # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Дожидаемся реального освобождения устройства
                        max_wait_time = 1.0  # Максимальное время ожидания
                        wait_interval = 0.02  # Интервал проверки (20ms)
                        waited_time = 0.0
                        
                        while waited_time < max_wait_time:
                            try:
                                if hasattr(stream_ref, 'active'):
                                    if not stream_ref.active:
                                        logger.debug(f"✅ [OUTPUT] Старый поток полностью освобожден (active=False, ожидание: {waited_time:.3f}с)")
                                        break
                                    else:
                                        logger.debug(f"⏳ [OUTPUT] Старый поток еще активен (active=True), ожидание: {waited_time:.3f}с...")
                                else:
                                    logger.debug("💡 [OUTPUT] Поток не имеет атрибута active, считаем закрытым")
                                    break
                            except (AttributeError, RuntimeError) as e:
                                logger.debug(f"✅ [OUTPUT] Поток уже закрыт/удален: {e}")
                                break
                            
                            time.sleep(wait_interval)
                            waited_time += wait_interval
                        
                        if waited_time >= max_wait_time:
                            logger.warning(f"⚠️ [OUTPUT] Превышено время ожидания освобождения старого потока ({max_wait_time}с), продолжаем...")
                        
                        self._audio_stream = None
                        self._stream_started = False
                        logger.info(f"✅ [OUTPUT] Старый поток закрыт и освобожден (ожидание: {waited_time:.3f}с)")
                        
                        # Дополнительная задержка для гарантии освобождения устройства
                        time.sleep(0.1)
                        
                    except Exception as e:
                        logger.warning(f"⚠️ [OUTPUT] Ошибка при проверке/закрытии существующего потока: {e}", exc_info=True)
                        # Принудительно очищаем ссылку
                        self._audio_stream = None
                        self._stream_started = False
                        time.sleep(0.2)  # Увеличенная задержка при ошибке
                
                # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Финальная проверка перед созданием нового потока
                if self._audio_stream is not None:
                    logger.error("❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: Поток все еще существует после закрытия!")
                    self._audio_stream = None
                    self._stream_started = False
                    time.sleep(0.5)  # Большая задержка при критической ошибке

                logger.info(f"🔍 [OUTPUT] Текущая конфигурация: rate={self.config.sample_rate}Hz, channels={self.config.channels}, dtype={self.config.dtype}, buffer_size={self.config.buffer_size}")

                # Перед созданием потока уточняем параметры текущего устройства
                if sync_output:
                    logger.debug("🔍 [OUTPUT] Синхронизируем формат с устройством...")
                    self._sync_output_format(restart_stream=False)
                    logger.info(f"🔍 [OUTPUT] После синхронизации: rate={self.config.sample_rate}Hz, channels={self.config.channels}")

                # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Сначала используем device_id, переданный вызовом
                # Только если device_id не передан, обращаемся к SwitchAudioSource
                device_info = None
                device_name = "Unknown"
                is_bluetooth = False
                
                if device_id is not None:
                    # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Используем переданный device_id
                    logger.info(f"✅ [OUTPUT] Используем переданный device_id={device_id} (пропускаем запрос к SwitchAudioSource)")
                    try:
                        device_info = sd.query_devices(device_id, 'output')
                        if device_info:
                            device_name = device_info.get('name', 'Unknown')
                            logger.info(f"✅ [OUTPUT] Устройство по device_id={device_id}: \"{device_name}\"")
                            # Определяем, является ли устройство BT
                            if device_name != "Unknown":
                                if self._params_normalizer:
                                    is_bluetooth = self._params_normalizer.is_bluetooth_device(device_name)
                                else:
                                    lowered = device_name.lower()
                                    is_bluetooth = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
                        else:
                            logger.warning(f"⚠️ [OUTPUT] device_id={device_id} не найден в PortAudio, fallback на SwitchAudioSource")
                            device_id = None  # Fallback на SwitchAudioSource
                    except Exception as e:
                        logger.warning(f"⚠️ [OUTPUT] Ошибка получения устройства по device_id={device_id}: {e}, fallback на SwitchAudioSource")
                        device_id = None  # Fallback на SwitchAudioSource
                
                if device_id is None:
                    # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Только если device_id не передан, обращаемся к SwitchAudioSource
                    logger.debug("🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...")
                    logger.info(f"✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)")
                    current_device = self._query_default_output_device()
                    if current_device:
                        device_name = current_device.get('name', 'Unknown')
                        device_id_from_macos = current_device.get('index', None)
                        logger.info(f"✅ [OUTPUT] macOS API (источник истины): \"{device_name}\" (ID={device_id_from_macos})")
                    
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем тип устройства ДО принятия решения о device_id
                    is_bluetooth = False
                    if device_name != "Unknown":
                        if self._params_normalizer:
                            is_bluetooth = self._params_normalizer.is_bluetooth_device(device_name)
                        else:
                            # ✅ FALLBACK: Если _params_normalizer недоступен, проверяем имя устройства напрямую
                            lowered = device_name.lower()
                            is_bluetooth = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
                            if is_bluetooth:
                                logger.debug(f"🔍 [OUTPUT] BT устройство определено через fallback: \"{device_name}\"")
                    
                    if is_bluetooth:
                        # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Для BT устройств ВСЕГДА используем device=None
                        # Не ищем ID в PortAudio - пусть macOS сам выберет правильное устройство
                        logger.info(f"🔧 [OUTPUT] BT устройство обнаружено: \"{device_name}\"")
                        logger.info(f"💡 [OUTPUT] SwitchAudioSource → device=None для BT (macOS управляет параметрами)")
                        device_id = None  # ВСЕГДА None для BT устройств
                        device_info = {}  # Не получаем информацию из PortAudio для BT
                    elif device_id_from_macos is not None:
                        # Для обычных устройств используем ID из macOS API (только если он есть)
                        device_id = device_id_from_macos
                        device_info = current_device
                        logger.debug(f"🔍 [OUTPUT] Обычное устройство: используем ID={device_id}")
                    else:
                        # macOS API вернул устройство, но без ID (PortAudio не видит его)
                        # Это может быть временная проблема - используем device=None как fallback
                        logger.warning(f"⚠️ [OUTPUT] macOS API вернул устройство \"{device_name}\", но PortAudio не видит его (ID=None)")
                        logger.info(f"💡 [OUTPUT] Используем device=None (системный дефолт) как fallback")
                        device_id = None
                        device_info = current_device
                else:
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: SwitchAudioSource - единственный источник истины
                    # Нет fallback на PortAudio или sd.default.device
                    # Если SwitchAudioSource не вернул устройство, используем device=None (системный дефолт)
                    logger.warning("⚠️ [OUTPUT] SwitchAudioSource не вернул устройство (единственный источник истины)")
                    logger.warning("⚠️ [OUTPUT] Пропускаем получение информации об устройстве - используем device=None (системный дефолт)")
                    device_info = {}
                
                # ✅ ИТЕРАЦИЯ 3: Нормализуем параметры устройства (только для обычных устройств)
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств полностью доверяем macOS параметрам
                # DeviceParamsNormalizer используется только для обычных устройств
                is_bluetooth_precheck = False
                if device_name and device_name != "Unknown":
                    if self._params_normalizer:
                        is_bluetooth_precheck = self._params_normalizer.is_bluetooth_device(device_name)
                    else:
                        lowered = device_name.lower()
                        is_bluetooth_precheck = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
                
                if device_info and self._params_normalizer and not is_bluetooth_precheck:
                    # Только для обычных устройств используем DeviceParamsNormalizer
                    try:
                        normalized = self._params_normalizer.select_output_params(device_info)
                        self._normalized_params = normalized
                        
                        # Обновляем конфиг с нормализованными параметрами
                        original_rate = self.config.sample_rate
                        original_channels = self.config.channels
                        
                        self.config.sample_rate = normalized.sample_rate
                        self.config.channels = normalized.channels
                        
                        logger.info(f"✅ [OUTPUT] Нормализованные параметры для \"{device_name}\":")
                        logger.info(f"   Sample Rate: {normalized.device_rate or 'N/A'} → {normalized.sample_rate} Hz")
                        logger.info(f"   Channels: {normalized.channels}")
                        if original_rate != normalized.sample_rate or original_channels != normalized.channels:
                            logger.info(f"   ⚠️ Параметры изменены: {original_rate}Hz/{original_channels}ch → {normalized.sample_rate}Hz/{normalized.channels}ch")
                    except Exception as e:
                        logger.warning(f"⚠️ Ошибка нормализации параметров: {e}, используем конфиг")
                else:
                    if is_bluetooth_precheck:
                        logger.debug(f"💡 [OUTPUT] BT устройство \"{device_name}\" - пропускаем DeviceParamsNormalizer, доверяем macOS параметрам")
                    elif not self._params_normalizer:
                        logger.debug("⚠️ Нормализатор недоступен, используем конфиг")
                    else:
                        logger.debug("⚠️ Информация об устройстве недоступна, используем конфиг")

                # ✅ ИСПРАВЛЕНИЕ: Используем явный device_id
                # sounddevice.OutputStream принимает device как:
                # - None: использовать системный дефолт
                # - int: конкретный device ID
                # - (input_id, output_id): для duplex streams
                # У нас output-only stream, поэтому передаём просто int или None

                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем тип устройства для правильной конфигурации
                # Определяем тип устройства ПОСЛЕ получения device_name из macOS API
                # Используем уже определенный is_bluetooth из блока выше (если был определен)
                # Если не был определен, определяем здесь
                if 'is_bluetooth' not in locals():
                    is_bluetooth = False
                    if device_name and device_name != "Unknown":
                        if self._params_normalizer:
                            is_bluetooth = self._params_normalizer.is_bluetooth_device(device_name)
                        else:
                            # ✅ FALLBACK: Если _params_normalizer недоступен, проверяем имя устройства напрямую
                            lowered = device_name.lower()
                            is_bluetooth = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
                            if is_bluetooth:
                                logger.debug(f"🔍 [OUTPUT] BT устройство определено через fallback: \"{device_name}\"")
                
                # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Для BT устройств ВСЕГДА используем device=None
                # НИКОГДА не используем PortAudio ID для BT устройств - сразу device=None
                if is_bluetooth:
                    logger.info(f"💡 [OUTPUT] SwitchAudioSource → \"{device_name}\" (BT устройство)")
                    logger.info(f"✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)")
                    device_id = None  # ВСЕГДА None для BT устройств, НЕ используем PortAudio ID
                
                # ✅ КЭШ ОШИБОК: Получаем безопасную конфигурацию с учетом истории ошибок
                # Если устройство уже вызывало ошибки в прошлом, сразу используем безопасную конфигурацию
                stream_config = self._get_safe_stream_config(device_name, is_bluetooth, device_id)
                
                if is_bluetooth:
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Для BT устройств НЕ задаем blocksize, latency
                    # channels обязателен, но blocksize/latency не задаем - пусть macOS/PortAudio выберут сами
                    logger.info(f"🔧 [OUTPUT] BT устройство: используем channels={stream_config.get('channels')} (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)")
                else:
                    logger.debug(f"🔧 [OUTPUT] Обычное устройство: используем все параметры (device={stream_config.get('device')}, channels={stream_config.get('channels')}, blocksize={stream_config.get('blocksize', 'N/A')})")
                
                logger.info(f"🔍 [OUTPUT] Конфигурация потока:")
                logger.info(f"   device: {stream_config.get('device')}")
                logger.info(f"   channels: {stream_config.get('channels', 'N/A')}")
                logger.info(f"   dtype: {stream_config.get('dtype')}")
                logger.info(f"   samplerate: {stream_config.get('samplerate')} Hz")
                if 'blocksize' in stream_config:
                    logger.info(f"   blocksize: {stream_config['blocksize']}")
                else:
                    logger.info(f"   blocksize: N/A (не задан, пусть PortAudio выберет)")
                if 'latency' in stream_config:
                    logger.info(f"   latency: {stream_config['latency']}s")
                else:
                    logger.info(f"   latency: N/A (не задан, пусть PortAudio выберет)")

                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: device_name и device_id уже получены выше из macOS API
                # Логируем финальную конфигурацию
                device_id_actual = device_id if device_id is not None else 'System Default'
                logger.info(f"🔍 [OUTPUT] Создаём поток для устройства: {device_name} (ID={device_id_actual})")

                # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Для BT устройств НИКОГДА не проверяем доступность через PortAudio ID
                # BT устройства всегда используют device=None, проверка доступности не нужна
                if not is_bluetooth and device_id is not None and device_id_actual != 'System Default':
                    logger.info(f"🔍 [OUTPUT] Проверяем доступность устройства ID {device_id_actual}...")
                    try:
                        device_available = self._check_device_available(device_id)  # Используем оригинальный device_id (int)
                        logger.debug(f"🔍 [OUTPUT] Результат проверки доступности: {device_available}")
                    except Exception as check_error:
                        logger.error(f"❌ [OUTPUT] Исключение при проверке доступности устройства ID {device_id_actual}: {check_error}", exc_info=True)
                        device_available = False
                    
                    if not device_available:
                        logger.warning(f"⚠️ [OUTPUT] Устройство {device_name} (ID={device_id_actual}) недоступно, пробуем с задержкой...")
                        time.sleep(0.2)  # Небольшая задержка для инициализации устройства
                        logger.debug(f"🔍 [OUTPUT] Задержка завершена, повторная проверка...")
                        
                        # Повторная проверка
                        if not self._check_device_available(device_id):  # Используем оригинальный device_id (int)
                            logger.error(f"❌ [OUTPUT] Устройство {device_name} (ID={device_id_actual}) всё ещё недоступно")
                            # ✅ FIX: Пробуем использовать None (системный дефолт) как fallback
                            logger.info("🔄 [OUTPUT] Пробуем использовать системный дефолт (device=None)")
                            stream_config['device'] = None
                            device_id_actual = 'System Default'
                            logger.info(f"🔍 [OUTPUT] Обновлённая конфигурация: device={stream_config['device']}")
                    else:
                        logger.info(f"✅ [OUTPUT] Устройство {device_name} (ID={device_id_actual}) доступно")
                else:
                    logger.info(f"🔍 [OUTPUT] Пропускаем проверку доступности (device_id={device_id}, device_id_actual={device_id_actual})")

                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Экспоненциальный backoff для создания потока
                # Для BT устройств требуется больше времени на инициализацию CoreAudio pipeline
                max_retries = 5  # Увеличено до 5 для BT устройств
                base_delay = 0.3
                last_error = None
                
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств применяем увеличенную предстартовую задержку
                # BT устройствам нужно 2-3 секунды для полной инициализации CoreAudio pipeline
                bt_prestart_delay = 0.0
                if is_bluetooth:
                    bt_prestart_delay = 2.0  # Увеличено до 2 секунд для полной инициализации
                    logger.info(f"⏳ [OUTPUT] Bluetooth устройство обнаружено, ожидание готовности CoreAudio pipeline ({bt_prestart_delay}с)...")
                    time.sleep(bt_prestart_delay)
                
                # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Финальная проверка перед началом retry-цикла
                # Убеждаемся, что старый поток действительно закрыт
                if self._audio_stream is not None:
                    logger.error("❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: Поток все еще существует перед retry-циклом!")
                    logger.error("❌ [OUTPUT] Принудительно очищаем поток и ждем освобождения устройства...")
                    try:
                        if hasattr(self._audio_stream, 'active') and self._audio_stream.active:
                            self._audio_stream.stop()
                        self._audio_stream.close()
                    except Exception:
                        pass
                    self._audio_stream = None
                    self._stream_started = False
                    # Увеличенная задержка для гарантии освобождения устройства
                    wait_time = 1.0 if is_bluetooth else 0.5
                    logger.info(f"⏳ [OUTPUT] Ожидание освобождения устройства: {wait_time}с...")
                    time.sleep(wait_time)
                
                logger.info(f"🔍 [OUTPUT] Начинаем создание потока (max_retries={max_retries}, base_delay={base_delay}s, BT={is_bluetooth})...")
                logger.info(f"✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)")
                
                stream_start_time = time.time()
                for attempt in range(max_retries):
                    # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Перед каждой попыткой проверяем, что старый поток закрыт
                    # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Используем is_bluetooth из текущей попытки, а не из self._current_device_name
                    if self._audio_stream is not None:
                        logger.warning(f"⚠️ [OUTPUT] Попытка {attempt + 1}: обнаружен незакрытый поток, закрываем...")
                        logger.info(f"✅ [OUTPUT] Используем is_bluetooth={is_bluetooth} из текущей попытки (устройство: \"{device_name}\")")
                        # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Передаем is_bluetooth из текущей попытки напрямую
                        self._stop_audio_stream(is_bluetooth=is_bluetooth)
                        
                        # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Дополнительная проверка после _stop_audio_stream()
                        # Убеждаемся, что поток действительно None и не активен
                        max_verify_time = 1.0 if is_bluetooth else 0.5
                        verify_interval = 0.02
                        verify_time = 0.0
                        
                        while verify_time < max_verify_time:
                            if self._audio_stream is None:
                                logger.debug(f"✅ [OUTPUT] Поток подтвержден как None (проверка: {verify_time:.3f}с)")
                                break
                            time.sleep(verify_interval)
                            verify_time += verify_interval
                        
                        if self._audio_stream is not None:
                            logger.error(f"❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: Поток все еще существует после _stop_audio_stream()!")
                            # Принудительно очищаем
                            try:
                                if hasattr(self._audio_stream, 'active') and self._audio_stream.active:
                                    self._audio_stream.stop()
                                self._audio_stream.close()
                            except Exception:
                                pass
                            self._audio_stream = None
                            self._stream_started = False
                            time.sleep(0.5)  # Дополнительная задержка
                    
                    # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Финальная проверка перед созданием потока
                    if self._audio_stream is not None:
                        logger.error(f"❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: Поток все еще существует перед созданием нового!")
                        raise RuntimeError("Старый поток не был закрыт перед созданием нового")
                    
                        logger.info(f"🔍 [OUTPUT] Попытка {attempt + 1}/{max_retries} создания потока...")
                    
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Логируем подтверждение, что старый поток закрыт → создаём новый stream
                    if self._audio_stream is None:
                        logger.info(f"✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream")
                        logger.info(f"   Устройство: {device_name} (ID={device_id_actual}, BT={is_bluetooth})")
                        logger.info(f"   Параметры: device={stream_config.get('device')}, channels={stream_config.get('channels', 'N/A')}, "
                                   f"samplerate={stream_config.get('samplerate')}, blocksize={stream_config.get('blocksize', 'N/A')}, "
                                   f"latency={stream_config.get('latency', 'N/A')}")
                        if is_bluetooth:
                            logger.info(f"   SwitchAudioSource → device=None для BT (macOS управляет параметрами)")
                    else:
                        logger.error(f"❌ [OUTPUT] КРИТИЧЕСКАЯ ОШИБКА: _audio_stream не None перед созданием потока!")
                        raise RuntimeError("Старый поток не был закрыт перед созданием нового")
                    
                        logger.debug(f"🔍 [OUTPUT] Параметры потока: {stream_config}")

                host_error_code = self._get_last_host_error_code()
                if host_error_code is not None:
                    logger.debug(f"🔍 [OUTPUT] Последний host error code: {host_error_code}")

                try:
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Создаем поток только после подтверждения, что старый закрыт
                    # Создаем поток БЕЗ старта (lazy start для снижения нагрузки)
                    logger.info(f"🔍 [OUTPUT] Создаем новый поток: device={stream_config.get('device')}, BT={is_bluetooth}")
                    self._audio_stream = sd.OutputStream(**stream_config)
                    self._stream_started = False

                    elapsed = time.time() - stream_start_time
                    if attempt > 0:
                        logger.info(f"✅ [OUTPUT] Аудио поток создан успешно на попытке {attempt + 1}! (время создания: {elapsed:.2f}с)")
                    else:
                        logger.info(f"✅ [OUTPUT] Аудио поток создан успешно! (время создания: {elapsed:.2f}с)")
                    # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Логируем "new stream device=None" для BT устройств
                    if is_bluetooth:
                        logger.info(f"✅ [OUTPUT] new stream device=None (BT устройство)")
                    # ✅ РАСШИРЕННОЕ ЛОГИРОВАНИЕ: Фиксируем все параметры успешного создания
                    logger.info(f"   Устройство: {device_name} (ID={device_id_actual}, BT={is_bluetooth})")
                    logger.info(f"   Параметры: channels={stream_config.get('channels')}, samplerate={stream_config.get('samplerate')}Hz, "
                               f"dtype={stream_config.get('dtype')}, blocksize={stream_config.get('blocksize', 'N/A')}, "
                               f"latency={stream_config.get('latency', 'N/A')}")
                    logger.info(f"   Задержки: prestart={bt_prestart_delay if is_bluetooth else 0}с, "
                               f"backoff={base_delay * (2 ** attempt) if attempt > 0 else 0}с")

                    # ✅ КЭШ ОШИБОК: Если поток создан успешно после ошибок, сохраняем безопасную конфигурацию
                    # Это позволит при следующем подключении сразу использовать рабочую конфигурацию
                    if attempt > 0:
                        # Поток создан после ошибок - сохраняем безопасную конфигурацию
                        # Используем -10851 как общий код для "конфигурационных ошибок"
                        self._cache_error_config(device_name, -10851, stream_config)
                        logger.info(f"💾 [OUTPUT] Сохранена безопасная конфигурация после успешного создания потока (попытка {attempt + 1})")

                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Сохраняем имя текущего устройства для использования в _stop_audio_stream()
                    self._current_device_name = device_name
                    logger.debug("💡 Поток будет стартован при появлении первого чанка (lazy start)")
                    return True
                except Exception as e:
                        last_error = e
                        elapsed = time.time() - stream_start_time
                        error_msg = str(e)
                        
                        # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Специальная обработка ошибок для BT устройств
                        is_error_9986 = "-9986" in error_msg or "Internal PortAudio error" in error_msg
                        is_error_10851 = (
                            "-10851" in error_msg
                            or "Invalid Property Value" in error_msg
                            or host_error_code == -10851
                        )
                        
                        # ✅ КЭШ ОШИБОК: При ошибке -10851 (конфигурационная ошибка) сохраняем текущую конфигурацию
                        # для будущего использования безопасной конфигурации
                        if is_error_10851:
                            logger.warning(f"⚠️ [OUTPUT] Обнаружена ошибка -10851 (Invalid Property Value) - сохраняем конфигурацию для кэша")
                            # Сохраняем текущую конфигурацию как "плохую" (будет заменена на безопасную при успешном создании)
                            # Это позволит при следующей попытке сразу использовать безопасную конфигурацию
                        
                        # ✅ РАСШИРЕННОЕ ЛОГИРОВАНИЕ: Фиксируем все параметры и ошибки
                        logger.error(f"❌ [OUTPUT] Попытка {attempt + 1}/{max_retries} создания потока не удалась (время: {elapsed:.2f}с)")
                        logger.error(f"   Устройство: {device_name} (ID={device_id_actual}, BT={is_bluetooth})")
                        logger.error(f"   Параметры: device={stream_config.get('device')}, channels={stream_config.get('channels')}, "
                                   f"samplerate={stream_config.get('samplerate')}, blocksize={stream_config.get('blocksize', 'N/A')}, "
                                   f"latency={stream_config.get('latency', 'N/A')}")
                        logger.error(f"   Ошибка: {type(e).__name__}: {e}")
                        logger.error(f"   is_error_9986={is_error_9986}, is_error_10851={is_error_10851}")
                        
                        # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Ошибка -10851 указывает на несовместимые параметры для BT
                        if is_error_10851 and is_bluetooth:
                            logger.warning("⚠️ [OUTPUT] Обнаружена ошибка -10851 (Invalid Property Value) для BT устройства")
                            logger.info("💡 [OUTPUT] Переключаемся на системный дефолт (device=None) БЕЗ параметров буферизации")
                            # Для BT устройств пробуем использовать системный дефолт БЕЗ параметров буферизации
                            stream_config['device'] = None
                            device_id_actual = 'System Default'
                            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Убираем ВСЕ параметры буферизации для BT
                            if 'blocksize' in stream_config:
                                del stream_config['blocksize']
                            if 'latency' in stream_config:
                                del stream_config['latency']
                            if stream_config.get('channels', self.config.channels) > 1:
                                stream_config['channels'] = 1
                                logger.info("🔧 [OUTPUT] Для BT устройства понижены каналы до моно (1)")
                            logger.info(f"🔧 [OUTPUT] Для BT устройства убраны все параметры буферизации (пусть PortAudio выберет сам)")
                            logger.debug(f"🔍 [OUTPUT] Обновлённая конфигурация для BT: {stream_config}")
                        
                        if is_error_9986:
                            logger.warning("⚠️ [OUTPUT] Обнаружена ошибка -9986 (Internal PortAudio error) - устройство может быть занято")
                            logger.info("💡 [OUTPUT] Рекомендация: убедитесь, что старый поток полностью закрыт")
                        logger.debug(f"   Детали ошибки:", exc_info=True)
                        
                        # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: При ошибке -9986/-10851 сначала _stop_audio_stream(), time.sleep(1.0), затем device=None
                        # Убираем старую обработку ошибок, которая просто увеличивает backoff
                        # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Используем is_bluetooth из текущей попытки, а не из self._current_device_name
                        if is_error_9986 or is_error_10851:
                            logger.warning(f"⚠️ [OUTPUT] Ошибка {'-9986' if is_error_9986 else '-10851'}: устройство может быть занято старым потоком")
                            logger.info("🔄 [OUTPUT] Вызываем _stop_audio_stream() для гарантированного освобождения устройства...")
                            logger.info(f"✅ [OUTPUT] Используем is_bluetooth={is_bluetooth} из текущей попытки (устройство: \"{device_name}\")")
                            
                            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Передаем is_bluetooth из текущей попытки напрямую
                            # НЕ используем self._current_device_name, который обновляется только после успешного создания потока
                            self._stop_audio_stream(is_bluetooth=is_bluetooth)
                            
                            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Затем time.sleep(1.0)
                            logger.info(f"⏳ [OUTPUT] Задержка для освобождения устройства после ошибки: 1.0с...")
                            time.sleep(1.0)
                            
                            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Затем device=None для BT устройств
                            if is_bluetooth:
                                logger.info("🔄 [OUTPUT] Для BT устройства создаем stream с device=None (macOS управляет параметрами)")
                                stream_config['device'] = None
                                device_id_actual = 'System Default'
                                # Убираем только blocksize и latency для BT
                                if 'blocksize' in stream_config:
                                    del stream_config['blocksize']
                                if 'latency' in stream_config:
                                    del stream_config['latency']
                                # Убеждаемся, что channels есть (обязателен для sd.OutputStream)
                                if 'channels' not in stream_config:
                                    stream_config['channels'] = self.config.channels
                                logger.info(f"🔧 [OUTPUT] Для BT устройства: device=None, channels={stream_config.get('channels')}, без blocksize/latency")
                            else:
                                # Для обычных устройств пробуем device=None как fallback
                                if stream_config.get('device') is not None:
                                    logger.info("🔄 [OUTPUT] Для обычного устройства пробуем device=None как fallback")
                                    stream_config['device'] = None
                                    device_id_actual = 'System Default'
                            
                            logger.info(f"✅ [OUTPUT] Устройство должно быть освобождено после ошибки {'-9986' if is_error_9986 else '-10851'}")
                            
                            # ✅ КЭШ ОШИБОК: При ошибке -10851 после применения безопасной конфигурации
                            # сохраняем её для будущего использования
                            if is_error_10851:
                                # Сохраняем безопасную конфигурацию (device=None, без blocksize/latency для BT)
                                safe_config_for_cache = stream_config.copy()
                                if 'callback' in safe_config_for_cache:
                                    del safe_config_for_cache['callback']
                                self._cache_error_config(device_name, -10851, safe_config_for_cache)
                                logger.info(f"💾 [OUTPUT] Сохранена безопасная конфигурация для \"{device_name}\" после ошибки -10851")
                        
                        if attempt < max_retries - 1:
                            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Новый backoff после обработки ошибки
                            if is_bluetooth or is_error_9986 or is_error_10851:
                                delay = base_delay * (2 ** attempt) * 2.0 * 1.5  # Увеличенная задержка ×1.5 для повторных ошибок
                            else:
                                delay = base_delay * (2 ** attempt)
                            logger.info(f"⏳ [OUTPUT] Повторная попытка через {delay:.2f}с (экспоненциальный backoff ×1.5, попытка {attempt + 1}/{max_retries})...")
                            time.sleep(delay)
                            
                            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Логируем, что старый поток закрыт → создаём новый stream
                            logger.info(f"✅ [OUTPUT] Старый поток закрыт → создаём новый stream (попытка {attempt + 1}/{max_retries})")
                        else:
                            logger.error(f"❌ [OUTPUT] Все {max_retries} попытки создания потока не удались")
                            
                            # Если все попытки не удались, пробуем с device=None и моно как последний шанс
                            if stream_config.get('device') is not None or (is_bluetooth and stream_config.get('channels', 2) == 2):
                                logger.info("🔄 [OUTPUT] Последняя попытка: используем системный дефолт (device=None) и моно (1 канал)")
                                stream_config['device'] = None
                                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств пробуем моно (1 канал) вместо стерео
                                if is_bluetooth and stream_config.get('channels', 2) == 2:
                                    stream_config['channels'] = 1
                                    logger.info(f"🔧 [OUTPUT] Для BT устройства пробуем моно (1 канал) вместо стерео (2 канала)")
                                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств убираем ВСЕ параметры буферизации
                                if is_bluetooth:
                                    if 'blocksize' in stream_config:
                                        del stream_config['blocksize']
                                    if 'latency' in stream_config:
                                        del stream_config['latency']
                                    logger.info(f"🔧 [OUTPUT] Для BT устройства убраны все параметры буферизации (пусть PortAudio выберет сам)")
                                try:
                                    self._audio_stream = sd.OutputStream(**stream_config)
                                    self._stream_started = False
                                    logger.info(f"✅ [OUTPUT] Поток создан с системным дефолтом и моно")
                                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Сохраняем имя текущего устройства
                                    self._current_device_name = device_name
                                    return True
                                except Exception as e:
                                    logger.error(f"❌ [OUTPUT] Последняя попытка также не удалась: {e}")
                
                raise last_error if last_error else Exception("Не удалось создать аудио поток")

        except Exception as e:
            logger.error(f"❌ Ошибка создания аудио потока: {e}")
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
                    logger.info("▶️ Аудио поток стартован (lazy start)")

                    # 🔍 ДИАГНОСТИКА: Проверяем состояние после старта
                    logger.info(f"🔍 [OUTPUT] Поток стартован: active={self._audio_stream.active if self._audio_stream else 'N/A'}")
                except Exception as e:
                    logger.error(f"❌ Ошибка старта аудио потока: {e}")
            elif self._audio_stream is None:
                logger.error(f"❌ [OUTPUT] НЕ МОГУ СТАРТОВАТЬ: stream is None!")
            elif self._stream_started:
                logger.debug(f"✅ [OUTPUT] Поток уже стартован")
    
    def _get_safe_stream_config(self, device_name: str, is_bluetooth: bool, device_id: Optional[int]) -> Dict[str, Any]:
        """
        Получает безопасную конфигурацию потока с учетом истории ошибок.
        
        ✅ ФАЗА 3: Использует StreamConfigResolver для определения конфигурации
        
        Args:
            device_name: Имя устройства
            is_bluetooth: Является ли устройство Bluetooth
            device_id: PortAudio ID устройства (None для BT устройств)
        
        Returns:
            dict: Конфигурация потока (device, channels, dtype, samplerate, callback, blocksize, latency)
        """
        # ✅ ФАЗА 3: Используем resolver для определения конфигурации
        return self._stream_config_resolver.resolve_stream_config(
            device_name=device_name,
            is_bluetooth=is_bluetooth,
            device_id=device_id,
            callback=self._audio_callback,
            error_cache=self._device_error_cache,
            error_cache_lock=self._error_cache_lock
        )
    
    def _cache_error_config(self, device_name: str, error_code: int, safe_config: Dict[str, Any]):
        """
        Сохраняет "плохую" конфигурацию в кэш для будущего использования.
        
        ✅ ФАЗА 3: Использует StreamConfigResolver для сохранения конфигурации
        
        Args:
            device_name: Имя устройства
            error_code: Код ошибки (-9986, -10851)
            safe_config: Безопасная конфигурация, которая сработала после ошибки
        """
        # ✅ ФАЗА 3: Используем resolver для сохранения конфигурации
        self._stream_config_resolver.cache_error_config(
            device_name=device_name,
            error_code=error_code,
            safe_config=safe_config,
            error_cache=self._device_error_cache,
            error_cache_lock=self._error_cache_lock
        )
    
    def _clear_error_cache(self, device_name: Optional[str] = None):
        """
        Очищает кэш ошибок для конкретного устройства или всех устройств.
        
        Args:
            device_name: Имя устройства для очистки (None = очистить все)
        """
        with self._error_cache_lock:
            if device_name:
                if device_name in self._device_error_cache:
                    del self._device_error_cache[device_name]
                    logger.info(f"🗑️ [OUTPUT] Очищен кэш ошибок для \"{device_name}\"")
            else:
                self._device_error_cache.clear()
                logger.info(f"🗑️ [OUTPUT] Очищен весь кэш ошибок")
    
    def _stop_audio_stream(self, is_bluetooth: bool = False):
        """
        Остановка аудио потока с гарантией полного освобождения устройства.
        
        ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Дожидается реального закрытия потока через проверку active.
        Это предотвращает ошибки -9986 при создании нового потока на том же устройстве.
        
        Args:
            is_bluetooth: True если устройство является Bluetooth устройством (требует большей задержки)
        """
        try:
            with self._stream_lock:
                if self._audio_stream is not None:
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем, является ли текущее устройство BT
                    # Проверяем имя текущего устройства для определения типа
                    current_device_name = getattr(self, '_current_device_name', None)
                    if current_device_name and not is_bluetooth:
                        is_bluetooth = self._is_bluetooth_device(current_device_name)
                    
                    stream_ref = self._audio_stream  # Сохраняем ссылку для проверки active
                    
                    try:
                        if self._stream_started:
                            logger.debug("🔄 [OUTPUT] Останавливаем активный поток...")
                            stream_ref.stop()
                            self._stream_started = False
                            logger.debug("✅ [OUTPUT] Поток остановлен (stop() вызван)")
                    except Exception as stop_error:
                        logger.warning(f"⚠️ [OUTPUT] Ошибка при остановке потока: {stop_error}")
                    
                    try:
                        logger.debug("🔄 [OUTPUT] Закрываем поток...")
                        stream_ref.close()
                        logger.debug("✅ [OUTPUT] Поток закрыт (close() вызван)")
                    except Exception as close_error:
                        logger.warning(f"⚠️ [OUTPUT] Ошибка при закрытии потока: {close_error}")
                    
                    # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Дожидаемся реального освобождения устройства
                    # Цикл ожидания: while stream_ref.active: time.sleep(0.02) с таймаутом
                    max_wait_time = 3.0 if is_bluetooth else 1.0  # Увеличено для BT: 3.0с
                    wait_interval = 0.02  # Интервал проверки (20ms)
                    waited_time = 0.0
                    stream_was_active = False
                    
                    # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Цикл ожидания active=False
                    while waited_time < max_wait_time:
                        try:
                            # Проверяем, что поток действительно не активен
                            if hasattr(stream_ref, 'active'):
                                if stream_ref.active:
                                    stream_was_active = True
                                    if waited_time == 0:
                                        logger.warning(f"⚠️ [OUTPUT] Поток еще активен (active=True), ожидаем освобождения...")
                                    elif waited_time % 0.5 < wait_interval:  # Логируем каждые 0.5с
                                        logger.debug(f"⏳ [OUTPUT] Поток еще активен (active=True), ожидание: {waited_time:.3f}с...")
                                    time.sleep(wait_interval)
                                    waited_time += wait_interval
                                    continue
                                else:
                                    # Поток не активен - выходим из цикла
                                    if stream_was_active:
                                        logger.info(f"✅ [OUTPUT] old stream active=False (ожидание: {waited_time:.3f}с)")
                                    else:
                                        logger.debug(f"✅ [OUTPUT] Поток не был активен (active=False)")
                                    break
                            else:
                                # Если нет атрибута active, считаем что поток закрыт
                                logger.debug("💡 [OUTPUT] Поток не имеет атрибута active, считаем закрытым")
                                break
                        except (AttributeError, RuntimeError) as e:
                            # Поток уже закрыт или удален
                            logger.debug(f"✅ [OUTPUT] Поток уже закрыт/удален: {e}")
                            break
                        except Exception as e:
                            logger.warning(f"⚠️ [OUTPUT] Ошибка при проверке active: {e}")
                            break
                    
                    if waited_time >= max_wait_time:
                        logger.warning(f"⚠️ [OUTPUT] Превышено время ожидания освобождения потока ({max_wait_time}с), продолжаем...")
                    
                    # ✅ КРИТИЧЕСКОЕ УЛУЧШЕНИЕ: Дополнительная проверка перед установкой _audio_stream = None
                    # Убеждаемся, что поток действительно не активен
                    final_check_passed = False
                    try:
                        if hasattr(stream_ref, 'active'):
                            if not stream_ref.active:
                                final_check_passed = True
                                logger.info(f"✅ [OUTPUT] Финальная проверка: поток не активен (active=False)")
                            else:
                                logger.warning(f"⚠️ [OUTPUT] Финальная проверка: поток все еще активен (active=True)!")
                        else:
                            final_check_passed = True
                    except Exception:
                        final_check_passed = True
                    
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Только после проверки active=False устанавливаем _audio_stream = None
                    # Логируем подтверждение, что поток не активен
                    if final_check_passed:
                        logger.info(f"✅ [OUTPUT] Финальная проверка: поток не активен (active=False) - можно устанавливать _audio_stream=None")
                    else:
                        logger.warning(f"⚠️ [OUTPUT] Финальная проверка: поток может быть активен (active=True) - продолжаем с осторожностью")
                    
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Устанавливаем _audio_stream=None только после подтверждения active=False
                    self._audio_stream = None
                    logger.info(f"🛑 Аудио поток остановлен и закрыт (ожидание: {waited_time:.3f}с, active=False: {final_check_passed})")
                    
                    # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Задержка после close() для гарантии освобождения устройства
                    # Для BT устройств нужна большая задержка (2.0с), для обычных - меньшая (0.3с)
                    if is_bluetooth:
                        close_delay = 2.0  # 2.0с для BT устройств
                        logger.info(f"⏳ [OUTPUT] Задержка после close() для BT устройства: {close_delay}с (гарантия освобождения)...")
                    else:
                        close_delay = 0.3  # 0.3с для обычных устройств
                        logger.debug(f"⏳ [OUTPUT] Задержка после close() для обычного устройства: {close_delay}с...")
                    time.sleep(close_delay)
                    
                    logger.info(f"✅ [OUTPUT] Поток полностью закрыт (общее время: {waited_time + close_delay:.3f}с, active=False: {final_check_passed})")
                    logger.info(f"✅ [OUTPUT] Лог подтверждения: active=False → _audio_stream=None → устройство освобождено")

        except Exception as e:
            logger.error(f"❌ Ошибка остановки аудио потока: {e}", exc_info=True)
            # При ошибке все равно очищаем ссылку
            with self._stream_lock:
                self._audio_stream = None
                self._stream_started = False
    
    def _is_bluetooth_device(self, name: str) -> bool:
        """Проверяет, является ли устройство Bluetooth по имени"""
        if not name:
            return False
        lowered = name.lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpods", "airpod", "beats", "headset", "earbud"))

    def _query_default_output_device(self):
        """
        Возвращает информацию о текущем системном выходном устройстве.
        
        ✅ ШАГ 1.2: Улучшено логирование приоритетов
        
        Использует SwitchAudioSource (приоритет 1) или PortAudio (fallback).
        """
        try:
            logger.debug("🔍 [OUTPUT] Запрашиваем системное default output устройство...")
            
            # ✅ ПРИОРИТЕТ 1: Получаем имя устройства через macOS API (SwitchAudioSource)
            # ✅ ШАГ 1.2: macOS API всегда вызывается первым - это источник истины
            logger.debug("🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)")
            device_name = self._get_output_device_name_via_macos_api()
            if device_name:
                logger.info(f"🔍 [OUTPUT] macOS default OUTPUT (источник истины): \"{device_name}\"")
                # Ищем ID устройства по имени в PortAudio
                device_id = self._find_device_id_by_name(device_name, device_type='output')
                if device_id is not None:
                    logger.debug(f"🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name={device_name}, id={device_id}")
                    device_info = sd.query_devices(device_id, 'output')
                    if device_info:
                        logger.info(f"✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):")
                        logger.info(f"   Name: {device_name}")
                        logger.info(f"   Index: {device_info.get('index', 'N/A')}")
                        logger.info(f"   Max Output Channels: {device_info.get('max_output_channels', 'N/A')}")
                        logger.info(f"   Default Sample Rate: {device_info.get('default_samplerate', 'N/A')} Hz")
                        logger.debug(f"🔍 [OUTPUT] Полная информация: {device_info}")
                        return device_info
                    else:
                        logger.warning(f"⚠️ [OUTPUT] device_info пуст для device_id={device_id}")
                else:
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: macOS API вернул имя устройства, но PortAudio не видит его
                    # Возвращаем словарь с name и index=None, чтобы _start_audio_stream() мог обработать это
                    # Это особенно важно для BT устройств, которые могут быть не видны в PortAudio сразу
                    logger.warning(f"⚠️ [OUTPUT] Устройство \"{device_name}\" не найдено в PortAudio после всех попыток")
                    logger.info(f"💡 [OUTPUT] Возвращаем устройство с index=None для обработки в _start_audio_stream()")
                    return {'name': device_name, 'index': None}
            else:
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: SwitchAudioSource - единственный источник истины
                # Нет fallback на PortAudio или sd.default.device
                logger.warning("⚠️ [OUTPUT] SwitchAudioSource не вернул имя устройства (единственный источник истины)")
                logger.warning("⚠️ [OUTPUT] Возвращаем None - используем device=None (системный дефолт)")
                return None
        except Exception as e:
            logger.error(f"❌ [OUTPUT] Критическая ошибка получения default output устройства: {e}", exc_info=True)
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
        """Подстраивает sample_rate и channels под текущее выходное устройство."""
        if not self.config.auto_device_selection:
            return False

        sample_rate, adjusted_channels, device_name = self._probe_output_format()
        if sample_rate is None and adjusted_channels is None:
            return False

        sample_rate_changed = False
        channel_changed = False

        if sample_rate is not None and sample_rate > 0 and sample_rate != self.config.sample_rate:
            logger.info(
                "🎛 Обновляем sample_rate плеера: %s → %s (device=%s)",
                self.config.sample_rate,
                sample_rate,
                device_name or "unknown",
            )
            self.config.sample_rate = sample_rate
            sample_rate_changed = True

        if adjusted_channels is not None and adjusted_channels > 0 and adjusted_channels != self.config.channels:
            logger.info(
                "🎛 Обновляем channels плеера: %s → %s (device=%s)",
                self.config.channels,
                adjusted_channels,
                device_name or "unknown",
            )
            self.config.channels = adjusted_channels
            channel_changed = True
            try:
                self.chunk_buffer.set_channels(adjusted_channels)
            except Exception as channel_err:
                logger.debug(f"⚠️ Не удалось обновить каналы буфера: {channel_err}")

        if restart_stream and (sample_rate_changed or channel_changed) and self._audio_stream is not None:
            was_active = self.state_manager.is_playing or self.state_manager.is_paused
            self._stop_audio_stream()
            if was_active:
                self._start_audio_stream(sync_output=False)

        return sample_rate_changed or channel_changed

    def resync_output_device(self) -> bool:
        """Переопределяет формат вывода и перезапускает поток при необходимости."""
        return self._sync_output_format(restart_stream=True)

    def _check_device_available(self, device_id) -> bool:
        """
        Проверяет доступность устройства перед созданием потока.
        
        Args:
            device_id: ID устройства для проверки (int, None или "System Default")
            
        Returns:
            True если устройство доступно, False иначе
        """
        try:
            logger.debug(f"🔍 [OUTPUT] Проверка доступности устройства ID {device_id}...")
            
            # ✅ FIX: Если device_id является None или "System Default", пропускаем проверку
            # Системный дефолт всегда доступен (PortAudio сам выберет устройство)
            if device_id is None or device_id == "System Default":
                logger.debug(f"🔍 [OUTPUT] Пропускаем проверку для системного дефолта (device_id={device_id})")
                return True
            
            # Проверяем, что device_id является числом
            if not isinstance(device_id, int):
                logger.warning(f"⚠️ [OUTPUT] device_id должен быть int, получен {type(device_id).__name__}: {device_id}")
                return False
            
            # Проверяем, что устройство существует в списке устройств
            logger.debug(f"🔍 [OUTPUT] Получаем список всех устройств...")
            devices = sd.query_devices()
            logger.debug(f"🔍 [OUTPUT] Всего устройств в системе: {len(devices)}")
            
            if device_id >= len(devices):
                logger.warning(f"⚠️ [OUTPUT] Устройство ID {device_id} не найдено в списке устройств (всего устройств: {len(devices)})")
                return False
            
            # Получаем информацию об устройстве
            logger.debug(f"🔍 [OUTPUT] Запрашиваем информацию об устройстве ID {device_id}...")
            try:
                device_info = sd.query_devices(device_id, 'output')
                logger.debug(f"🔍 [OUTPUT] sd.query_devices() завершён для ID {device_id}")
            except Exception as query_error:
                logger.error(f"❌ [OUTPUT] Ошибка при вызове sd.query_devices(device_id={device_id}, 'output'): {query_error}", exc_info=True)
                return False
            
            if not device_info:
                logger.warning(f"⚠️ [OUTPUT] Не удалось получить информацию об устройстве ID {device_id} (device_info is None/empty)")
                return False
            
            device_name = device_info.get('name', 'Unknown')
            logger.debug(f"🔍 [OUTPUT] Информация об устройстве получена: {device_name}")
            logger.debug(f"   Index: {device_info.get('index', 'N/A')}")
            logger.debug(f"   Max Input Channels: {device_info.get('max_input_channels', 'N/A')}")
            logger.debug(f"   Max Output Channels: {device_info.get('max_output_channels', 'N/A')}")
            logger.debug(f"   Default Sample Rate: {device_info.get('default_samplerate', 'N/A')} Hz")
            logger.debug(f"   Host API: {device_info.get('hostapi', 'N/A')}")
            
            # Проверяем, что устройство поддерживает output
            max_output_channels = device_info.get('max_output_channels', 0)
            if max_output_channels <= 0:
                logger.warning(f"⚠️ [OUTPUT] Устройство ID {device_id} ({device_name}) не поддерживает output (max_output_channels={max_output_channels})")
                return False
            
            # Проверяем sample rate
            sample_rate = device_info.get('default_samplerate', 0)
            if sample_rate <= 0:
                logger.warning(f"⚠️ [OUTPUT] Устройство ID {device_id} ({device_name}) имеет некорректный sample rate: {sample_rate}")
                return False
            
            logger.info(f"✅ [OUTPUT] Устройство ID {device_id} ({device_name}) доступно:")
            logger.info(f"   Sample Rate: {sample_rate} Hz")
            logger.info(f"   Max Output Channels: {max_output_channels}")
            return True
            
        except Exception as e:
            logger.error(f"❌ [OUTPUT] Ошибка проверки доступности устройства ID {device_id}: {e}", exc_info=True)
            return False

    def _get_last_host_error_code(self) -> Optional[int]:
        """
        Возвращает последний код ошибки хоста PortAudio (например, -10851 для Invalid Property Value).
        """
        try:
            lib = getattr(sd, '_lib', None)
            if not lib or not hasattr(lib, 'Pa_GetLastHostErrorInfo'):
                return None
            info = lib.Pa_GetLastHostErrorInfo()
            if not info:
                return None
            for candidate in ("errorCode", "contents", 0):
                try:
                    if candidate == 0:
                        value = info[candidate].errorCode
                    else:
                        attr = getattr(info, candidate)
                        value = attr if candidate == "errorCode" else attr.errorCode
                    return int(value)
                except Exception:
                    continue
            return None
        except Exception as e:
            logger.debug(f"⚠️ [OUTPUT] Не удалось получить host error code: {e}")
            return None

    def _check_and_update_output_device(self) -> bool:
        """
        Проверяет изменилось ли output устройство И обновляет кэш.
        Атомарная операция (проверка + обновление) для предотвращения рассинхронизации.

        Использует NAME-based сравнение (аналогично INPUT логике).

        Returns:
            True если устройство изменилось (или первый запуск), False если осталось тем же
        """
        if not self.config.auto_output_device_switch:
            logger.debug("🔍 [OUTPUT] Автопереключение отключено (auto_output_device_switch=False)")
            return False

        try:
            logger.debug("🔍 [OUTPUT] Проверка смены устройства...")

            # ✅ НЕ вызываем sd._terminate() здесь!
            # Это будет сделано ПОСЛЕ остановки старого потока, но ПЕРЕД созданием нового
            # (в методе add_audio_data после того как мы вернём True)

            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: SwitchAudioSource - единственный источник истины
            # Не используем PortAudio как fallback - это предотвращает рассинхронизацию
            current_device_name = self._get_output_device_name_via_macos_api()
            
            if not current_device_name:
                logger.debug("⚠️ [OUTPUT] SwitchAudioSource не вернул имя устройства (единственный источник истины)")
                return False

            # ✅ FIX: Защищаем доступ к output_device_name блокировкой
            with self._device_tracking_lock:
                # Сохраняем старое имя для сравнения
                old_device_name = self.output_device_name

            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем, является ли устройство BT
            is_bluetooth = self._is_bluetooth_device(current_device_name)

            # ✅ АТОМАРНО: Обновляем кэш СРАЗУ (не откладываем на потом)
            with self._device_tracking_lock:
                self.output_device_name = current_device_name
                self._is_current_device_bluetooth = is_bluetooth

            # Проверяем изменилось ли
            if old_device_name is None:
                # Первый запуск
                logger.info(f"🔊 [OUTPUT] Начальное устройство: \"{current_device_name}\" (BT={is_bluetooth})")
                return True

            if current_device_name != old_device_name:
                # Устройство изменилось
                logger.info(
                    f"🔄 [OUTPUT] Смена устройства: \"{old_device_name}\" → \"{current_device_name}\" (BT={is_bluetooth})"
                )
                return True

            # Устройство не изменилось
            logger.debug(f"✅ [OUTPUT] Устройство не изменилось: \"{current_device_name}\" (BT={is_bluetooth}, интервал={5.0 if is_bluetooth else self._device_check_interval}с)")
            return False

        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка проверки устройства: {e}")
            return False
    
    def _query_system_default_output(self) -> tuple[Optional[str], Optional[int]]:
        """
        Получает имя и PortAudio ID текущего системного default output устройства.
        
        ✅ ШАГ 1.2: Улучшено логирование приоритетов
        
        Использует SwitchAudioSource (приоритет 1) или PortAudio (fallback).
        
        Returns:
            tuple: (device_name, device_id) или (None, None) если не удалось получить
        """
        try:
            # ✅ ПРИОРИТЕТ 1: Получаем через macOS API (SwitchAudioSource)
            # ✅ ШАГ 1.2: macOS API всегда вызывается первым - это источник истины
            logger.debug("🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)")
            device_name = self._get_output_device_name_via_macos_api()
            if device_name:
                logger.info(f"✅ [OUTPUT] SwitchAudioSource → \"{device_name}\"")
                logger.info(f"🔍 [OUTPUT] macOS default OUTPUT (источник истины): \"{device_name}\"")
                
                # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Для BT устройств НЕ ищем ID в PortAudio
                # Определяем, является ли устройство BT, и если да - сразу возвращаем с device_id=None
                is_bluetooth = self._is_bluetooth_device(device_name)
                if is_bluetooth:
                    logger.info(f"💡 [OUTPUT] BT устройство \"{device_name}\" - НЕ ищем ID в PortAudio, используем device_id=None")
                    return device_name, None
                
                # Для обычных устройств ищем ID в PortAudio
                device_id = self._find_device_id_by_name(device_name, device_type='output')
                if device_id is not None:
                    logger.info(f"✅ [OUTPUT] Получено через SwitchAudioSource: name=\"{device_name}\", id={device_id}")
                    return device_name, device_id
                else:
                    logger.warning(f"⚠️ [OUTPUT] SwitchAudioSource вернул имя '{device_name}', но ID не найден в PortAudio после всех попыток")
            
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: SwitchAudioSource - единственный источник истины
            # Нет fallback на PortAudio или sd.default.device
            logger.warning("⚠️ [OUTPUT] SwitchAudioSource не вернул имя устройства (единственный источник истины)")
            logger.warning("⚠️ [OUTPUT] Возвращаем (None, None) - используем device=None (системный дефолт)")
            return None, None
            
        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка получения системного default output: {e}")
            return None, None
    
    def _get_output_device_name_via_macos_api(self) -> Optional[str]:
        """
        Получает имя текущего default output устройства через macOS API (SwitchAudioSource).
        
        ✅ ШАГ 1.2: Улучшена обработка ошибок и логирование
        
        Returns:
            Имя устройства или None если не удалось получить
        """
        try:
            import subprocess
            import json
            import shutil
            
            # ✅ ШАГ 1.2: Проверяем доступность SwitchAudioSource
            switch_audio_source_path = shutil.which('SwitchAudioSource')
            if not switch_audio_source_path:
                logger.warning("⚠️ [OUTPUT] SwitchAudioSource не найден в PATH (единственный источник истины)")
                logger.warning("⚠️ [OUTPUT] Возвращаем None - используем device=None (системный дефолт)")
                return None
            
            logger.debug(f"🔍 [OUTPUT] Используем SwitchAudioSource: {switch_audio_source_path}")
            
            result = subprocess.run(
                [switch_audio_source_path, '-c', '-t', 'output', '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                try:
                    device_info = json.loads(result.stdout.strip())
                    device_name = device_info.get('name', '')
                    if device_name:
                        logger.info(f"✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): \"{device_name}\"")
                        return device_name
                    else:
                        logger.warning("⚠️ [OUTPUT] SwitchAudioSource вернул пустое имя устройства")
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ [OUTPUT] Ошибка парсинга JSON от SwitchAudioSource: {e}, stdout: {result.stdout[:100]}")
            else:
                logger.warning(f"⚠️ [OUTPUT] SwitchAudioSource вернул код ошибки {result.returncode}: {result.stderr[:200]}")
                
        except subprocess.TimeoutExpired:
            logger.warning("⚠️ [OUTPUT] SwitchAudioSource превысил таймаут (5s) (единственный источник истины)")
            logger.warning("⚠️ [OUTPUT] Возвращаем None - используем device=None (системный дефолт)")
        except FileNotFoundError:
            logger.warning("⚠️ [OUTPUT] SwitchAudioSource не найден (единственный источник истины)")
            logger.warning("⚠️ [OUTPUT] Возвращаем None - используем device=None (системный дефолт)")
        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка получения имени через SwitchAudioSource: {e} (единственный источник истины)")
            logger.warning("⚠️ [OUTPUT] Возвращаем None - используем device=None (системный дефолт)")
        
        return None
    
    def _find_device_id_by_name(self, device_name: str, device_type: str = 'output') -> Optional[int]:
        """
        Находит PortAudio ID устройства по имени.
        
        Args:
            device_name: Имя устройства
            device_type: Тип устройства ('input' или 'output')
        
        Returns:
            PortAudio ID устройства или None если не найдено
        """
        try:
            # Получаем все устройства
            all_devices = sd.query_devices()
            
            # Фильтруем по типу устройства
            if device_type == 'output':
                # Для output: проверяем max_output_channels > 0
                filtered_devices = [
                    d for d in all_devices
                    if isinstance(d, dict) and d.get('max_output_channels', 0) > 0
                ]
            else:
                # Для input: проверяем max_input_channels > 0
                filtered_devices = [
                    d for d in all_devices
                    if isinstance(d, dict) and d.get('max_input_channels', 0) > 0
                ]
            
            # Ищем устройство по имени (точное совпадение)
            for device in filtered_devices:
                device_name_found = device.get('name', '')
                if device_name_found == device_name:
                    device_id = device.get('index')
                    logger.debug(f"🔍 [OUTPUT] Найден ID для '{device_name}': {device_id}")
                    return device_id
            
            # Если точное совпадение не найдено, пробуем нечувствительное к регистру сравнение
            for device in filtered_devices:
                device_name_found = device.get('name', '')
                if device_name_found.lower() == device_name.lower():
                    device_id = device.get('index')
                    logger.debug(f"🔍 [OUTPUT] Найден ID для '{device_name}' (без учета регистра): {device_id}")
                    return device_id
            
            # Если всё ещё не найдено, пробуем частичное совпадение (для случаев, когда имена немного отличаются)
            for device in filtered_devices:
                device_name_found = device.get('name', '')
                # Проверяем, содержит ли имя устройства искомое имя или наоборот
                if device_name.lower() in device_name_found.lower() or device_name_found.lower() in device_name.lower():
                    device_id = device.get('index')
                    logger.info(f"🔍 [OUTPUT] Найден ID для '{device_name}' (частичное совпадение с '{device_name_found}'): {device_id}")
                    return device_id
            
            logger.warning(f"⚠️ [OUTPUT] Устройство '{device_name}' не найдено в PortAudio")
            
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств пропускаем обновление кэша PortAudio
            # BT устройства часто не видны в PortAudio сразу, и обновление кэша не поможет
            # Это экономит время и предотвращает множественные попытки поиска
            is_bluetooth = False
            if device_name:
                lowered = device_name.lower()
                is_bluetooth = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
            
            if is_bluetooth:
                logger.info(f"💡 [OUTPUT] BT устройство '{device_name}' не найдено в PortAudio - это нормально, используем device=None (системный дефолт)")
                logger.info(f"💡 [OUTPUT] Пропускаем обновление кэша PortAudio для BT устройства (не поможет)")
                return None
            
            # ✅ ШАГ 1.3: Обновляем кэш PortAudio при неудачном поиске OUTPUT устройства (только для НЕ-BT устройств)
            logger.info("🔄 [OUTPUT] ШАГ 1.3: Обновление кэша PortAudio после неудачного поиска...")
            try:
                # Безопасное обновление кэша PortAudio
                if hasattr(sd.query_devices, 'clear_cache'):
                    sd.query_devices.clear_cache()
                    logger.debug("✅ [OUTPUT] Кэш PortAudio очищен через clear_cache()")
                else:
                    # ✅ АЛЬТЕРНАТИВНЫЙ СПОСОБ: Если clear_cache() недоступен, делаем несколько запросов с задержкой
                    # Это принудительно обновит список устройств в PortAudio
                    logger.debug("⚠️ [OUTPUT] Метод clear_cache() недоступен, используем альтернативный способ обновления кэша...")
                    import time
                    for retry in range(3):
                        time.sleep(0.2 * (retry + 1))  # Увеличиваем задержку с каждой попыткой
                        logger.debug(f"🔍 [OUTPUT] Попытка {retry + 1}/3 обновления кэша через повторный запрос...")
                        # Принудительно запрашиваем список устройств заново
                        _ = sd.query_devices()
                
                # Пробуем найти устройство еще раз после обновления кэша
                logger.debug(f"🔍 [OUTPUT] Повторный поиск '{device_name}' после обновления кэша...")
                all_devices = sd.query_devices()
                
                # Фильтруем по типу устройства
                if device_type == 'output':
                    filtered_devices = [
                        d for d in all_devices
                        if isinstance(d, dict) and d.get('max_output_channels', 0) > 0
                    ]
                else:
                    filtered_devices = [
                        d for d in all_devices
                        if isinstance(d, dict) and d.get('max_input_channels', 0) > 0
                    ]
                
                # Ищем устройство по имени (точное совпадение)
                for device in filtered_devices:
                    device_name_found = device.get('name', '')
                    if device_name_found == device_name:
                        device_id = device.get('index')
                        logger.info(f"✅ [OUTPUT] Устройство найдено после обновления кэша: '{device_name}' → ID {device_id}")
                        return device_id
            except Exception as e:
                logger.warning(f"⚠️ [OUTPUT] Ошибка обновления кэша PortAudio: {e}")
            
            # ✅ ШАГ 1.2: Логируем все доступные OUTPUT устройства для диагностики
            try:
                available_outputs = []
                for device in filtered_devices:
                    dev_name = device.get('name', 'Unknown')
                    dev_id = device.get('index', 'N/A')
                    available_outputs.append(f"ID {dev_id}: \"{dev_name}\"")
                
                if available_outputs:
                    logger.info(f"📋 [OUTPUT] Доступные {device_type.upper()} устройства в PortAudio ({len(available_outputs)}):")
                    for device_info in available_outputs:
                        logger.info(f"   - {device_info}")
                else:
                    logger.warning(f"⚠️ [OUTPUT] В PortAudio не найдено ни одного {device_type.upper()} устройства")
            except Exception as e:
                logger.warning(f"⚠️ [OUTPUT] Ошибка получения списка устройств для диагностики: {e}")
            
            return None
        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка поиска ID устройства '{device_name}': {e}")
            return None
    
    def _start_output_monitoring(self):
        """Запуск фонового мониторинга output устройства
        
        ✅ ФАЗА 2: Сначала пытается использовать Core Audio нотификации,
        если недоступны - использует polling как fallback
        """
        if self._output_monitor_thread and self._output_monitor_thread.is_alive():
            logger.warning("⚠️ [OUTPUT] Мониторинг output устройства уже запущен")
            return
        
        if not self.config.auto_output_device_switch:
            logger.info("🔍 [OUTPUT] Автопереключение отключено (auto_output_device_switch=False), мониторинг не запускается")
            return
        
        # ✅ ФАЗА 2: Пытаемся использовать Core Audio нотификации
        if self._core_audio_manager.is_notifications_available():
            logger.info("🔔 [OUTPUT] Попытка использовать Core Audio нотификации для мониторинга устройств...")
            if self._core_audio_manager.start_device_notifications(self._on_device_changed_notification):
                logger.info("✅ [OUTPUT] Core Audio нотификации активированы (событийная реакция)")
                # Инициализируем текущее устройство
                self._check_and_update_output_device()
                return
        
        # Fallback на polling
        logger.info(f"🚀 [OUTPUT] Запуск фонового мониторинга output устройства через polling (интервал={self._device_check_interval}s)")
        self._stop_device_monitor.clear()
        self._output_monitor_thread = threading.Thread(
            target=self._output_monitor_loop,
            name="OutputDeviceMonitor",
            daemon=True
        )
        self._output_monitor_thread.start()
        logger.info("✅ [OUTPUT] Фоновый мониторинг output устройства запущен (polling mode)")
    
    def _stop_output_monitoring(self):
        """Остановка фонового мониторинга output устройства
        
        ✅ ФАЗА 2: Останавливает как нотификации, так и polling
        """
        # ✅ ФАЗА 2: Останавливаем нотификации
        if self._core_audio_manager.is_notifications_available():
            self._core_audio_manager.stop_device_notifications()
        
        # Останавливаем polling
        if not self._output_monitor_thread or not self._output_monitor_thread.is_alive():
            return
        
        self._stop_device_monitor.set()
        self._output_monitor_thread.join(timeout=2.0)
        logger.info("🛑 [OUTPUT] Фоновый мониторинг output устройства остановлен")
    
    def _on_device_changed_notification(self):
        """
        ✅ ФАЗА 2: Callback для Core Audio нотификаций о смене default output устройства.
        Вызывается автоматически при изменении устройства в системе.
        """
        try:
            logger.info("🔔 [OUTPUT] Core Audio нотификация: default output устройство изменилось")
            
            # Получаем информацию о новом устройстве
            current_device_name = self._get_output_device_name_via_macos_api()
            if not current_device_name:
                logger.debug("⚠️ [OUTPUT] SwitchAudioSource не вернул имя устройства после нотификации")
                return
            
            # Определяем тип устройства (BT/обычное)
            is_bluetooth = self._is_bluetooth_device(current_device_name)
            
            # Получаем ID устройства (для обычных устройств)
            current_device_id = None
            if not is_bluetooth:
                current_device_id = self._find_device_id_by_name(current_device_name, device_type='output')
                if current_device_id is None:
                    logger.debug(f"⚠️ [OUTPUT] Устройство '{current_device_name}' не найдено в PortAudio, используем device=None")
            else:
                logger.debug(f"💡 [OUTPUT] BT устройство '{current_device_name}' - используем device=None (не ищем ID в PortAudio)")
            
            # Получаем старое устройство для логирования
            with self._device_tracking_lock:
                old_name = self.output_device_name
                old_id = self._current_output_device_id
            
            # Переключаем устройство
            if old_name is None or current_device_name != old_name:
                logger.info(
                    f"🔄 [OUTPUT] Core Audio нотификация: смена устройства "
                    f"\"{old_name}\" (ID={old_id}, BT={getattr(self, '_is_current_device_bluetooth', False)}) → "
                    f"\"{current_device_name}\" (ID={current_device_id}, BT={is_bluetooth})"
                )
                # ✅ ФАЗА 2: Используем тот же метод переключения, что и в polling
                self._switch_output_device(current_device_name, current_device_id, is_bluetooth)
            else:
                logger.debug(f"✅ [OUTPUT] Core Audio нотификация: устройство не изменилось \"{current_device_name}\"")
                
        except Exception as e:
            logger.error(f"❌ [OUTPUT] Ошибка обработки нотификации Core Audio: {e}", exc_info=True)
    
    def _output_monitor_loop(self):
        """Основной цикл фонового мониторинга output устройства (polling fallback)
        
        ✅ ФАЗА 2: Используется только если Core Audio нотификации недоступны
        """
        logger.info("🔄 [OUTPUT] Запуск цикла мониторинга output устройства (polling mode)")
        
        # Логируем все доступные output устройства при старте
        try:
            all_devices = sd.query_devices()
            output_devices = [
                d for d in all_devices
                if isinstance(d, dict) and d.get('max_output_channels', 0) > 0
            ]
            logger.info(f"🔍 [OUTPUT] Доступные output устройства при старте мониторинга: {[d.get('name') for d in output_devices]}")
        except Exception as e:
            logger.warning(f"⚠️ [OUTPUT] Ошибка получения списка устройств: {e}")
        
        while not self._stop_device_monitor.is_set():
            try:
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: SwitchAudioSource - единственный источник истины
                # Получаем имя устройства только через macOS API
                current_device_name = self._get_output_device_name_via_macos_api()
                
                if not current_device_name:
                    logger.debug("⚠️ [OUTPUT] SwitchAudioSource не вернул имя устройства, пропускаем проверку")
                    # Используем адаптивный интервал: для BT устройств больше
                    check_interval = 5.0 if getattr(self, '_is_current_device_bluetooth', False) else self._device_check_interval
                    self._stop_device_monitor.wait(check_interval)
                    continue
                
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем тип устройства (BT/обычное)
                is_bluetooth = self._is_bluetooth_device(current_device_name)
                
                # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств используем device=None (не ищем ID в PortAudio)
                # Для обычных устройств пытаемся найти ID в PortAudio
                current_device_id = None
                if not is_bluetooth:
                    current_device_id = self._find_device_id_by_name(current_device_name, device_type='output')
                    if current_device_id is None:
                        logger.debug(f"⚠️ [OUTPUT] Устройство '{current_device_name}' не найдено в PortAudio, используем device=None")
                else:
                    logger.debug(f"💡 [OUTPUT] BT устройство '{current_device_name}' - используем device=None (не ищем ID в PortAudio)")
                
                # Под замком сравниваем с сохранённым
                with self._device_tracking_lock:
                    old_name = self.output_device_name
                    old_id = self._current_output_device_id
                
                # Проверяем изменилось ли устройство
                if old_name is None:
                    # Первый запуск - сохраняем текущее устройство
                    with self._device_tracking_lock:
                        self.output_device_name = current_device_name
                        self._current_output_device_id = current_device_id
                        self._is_current_device_bluetooth = is_bluetooth
                    logger.info(f"🔊 [OUTPUT] Начальное устройство: \"{current_device_name}\" (ID={current_device_id}, BT={is_bluetooth})")
                elif current_device_name != old_name:
                    # Устройство изменилось - переключаем
                    logger.info(
                        f"🔄 [OUTPUT] Обнаружена смена устройства: "
                        f"\"{old_name}\" (ID={old_id}, BT={self._is_current_device_bluetooth}) → "
                        f"\"{current_device_name}\" (ID={current_device_id}, BT={is_bluetooth})"
                    )
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств передаем device=None
                    self._switch_output_device(current_device_name, current_device_id, is_bluetooth)
                
                # Ждём до следующей проверки
                self._stop_device_monitor.wait(self._device_check_interval)
                
            except Exception as e:
                logger.error(f"❌ [OUTPUT] Ошибка в цикле мониторинга устройства: {e}", exc_info=True)
                self._stop_device_monitor.wait(1.0)  # Пауза при ошибке
    
    def _switch_output_device(self, new_name: str, new_id: Optional[int], is_bluetooth: bool = None):
        """
        Безопасно переключает output устройство.
        
        ✅ СИСТЕМНОЕ РЕШЕНИЕ: Всегда останавливает/закрывает старый поток, ждет задержку
        (0.3с для обычных, 2.0с для BT), и только потом создает новый поток.
        
        Args:
            new_name: Имя нового устройства (из SwitchAudioSource - единственный источник истины)
            new_id: PortAudio ID нового устройства (None для BT устройств)
            is_bluetooth: Является ли устройство Bluetooth (если None, определяется автоматически)
        """
        try:
            # ✅ РАСШИРЕННОЕ ЛОГИРОВАНИЕ: Фиксируем старое устройство
            with self._device_tracking_lock:
                old_name = self.output_device_name
                old_id = self._current_output_device_id
                old_is_bluetooth = getattr(self, '_is_current_device_bluetooth', False)
            
            logger.info(
                f"🔄 [OUTPUT] Начало переключения устройства: "
                f"\"{old_name}\" (ID={old_id}, BT={old_is_bluetooth}) → "
                f"\"{new_name}\" (ID={new_id}, BT={is_bluetooth})"
            )
            
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Определяем тип нового устройства если не передан
            if is_bluetooth is None:
                is_bluetooth = self._is_bluetooth_device(new_name)
                logger.debug(f"🔍 [OUTPUT] Тип устройства определен автоматически: BT={is_bluetooth}")
            
            # 1. Устанавливаем _stop_event для остановки воспроизведения
            self._stop_event.set()
            
            # 2. ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Останавливаем и закрываем старый поток
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Используем _stop_audio_stream() с правильным параметром is_bluetooth
            # Это обеспечит правильную задержку после закрытия потока (2.0с для BT, 0.3с для обычных)
            logger.info(f"🛑 [OUTPUT] Остановка старого потока для устройства \"{old_name}\"...")
            self._stop_audio_stream(is_bluetooth=old_is_bluetooth)
            
            # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Дополнительная задержка после закрытия потока
            # Для BT устройств требуется больше времени для освобождения ресурсов CoreAudio
            # Важно: эта задержка применяется ПОСЛЕ полного закрытия потока в _stop_audio_stream()
            switch_delay = 2.0 if is_bluetooth else 0.5  # 2.0с для BT, 0.5с для обычных
            logger.info(f"⏳ [OUTPUT] Задержка перед созданием нового потока: {switch_delay}с (BT={is_bluetooth})")
            logger.info(f"✅ [OUTPUT] Подтверждение: старый поток полностью закрыт, устройство освобождено")
            time.sleep(switch_delay)
            
            # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Устанавливаем флаг типа устройства
            with self._device_tracking_lock:
                self._is_current_device_bluetooth = is_bluetooth
            
            # 3. Дожидаемся завершения playback thread
            if self._playback_thread and self._playback_thread.is_alive():
                logger.debug("🔄 [OUTPUT] Ожидаем завершения playback thread")
                self._playback_thread.join(timeout=1.0)
            
            # 4. Очищаем буфер
            self.chunk_buffer.clear_all()
            logger.debug("🔄 [OUTPUT] Буфер очищен")
            
            # 5. ✅ СИСТЕМНОЕ РЕШЕНИЕ: Получаем информацию о новом устройстве для нормализации параметров
            # Для BT устройств с device_id=None пропускаем получение информации из PortAudio
            device_info = {}
            if not is_bluetooth and new_id is not None:
                try:
                    device_info = sd.query_devices(new_id, 'output')
                    if not device_info:
                        logger.warning(f"⚠️ [OUTPUT] Не удалось получить информацию об устройстве ID {new_id}")
                        device_info = {}
                except Exception as e:
                    logger.warning(f"⚠️ [OUTPUT] Ошибка получения информации об устройстве ID {new_id}: {e}")
                    device_info = {}
            else:
                logger.debug(f"💡 [OUTPUT] BT устройство или device_id=None - пропускаем получение информации из PortAudio")
            
            # 6. Обновляем параметры через DeviceParamsNormalizer (если есть)
            # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств используем значения по умолчанию
            if self._params_normalizer and device_info:
                try:
                    normalized = self._params_normalizer.normalize_device_info(
                        device_info=device_info,
                        device_type='output'
                    )
                    if normalized:
                        # normalized - это словарь, не объект с атрибутами
                        old_channels = self.config.channels
                        old_rate = self.config.sample_rate
                        
                        if normalized.get('channels'):
                            self.config.channels = normalized['channels']
                        if normalized.get('sample_rate'):
                            self.config.sample_rate = normalized['sample_rate']
                        
                        # Обновляем буфер если каналы изменились
                        if old_channels != self.config.channels:
                            try:
                                self.chunk_buffer.set_channels(self.config.channels)
                                logger.debug(f"✅ [OUTPUT] Буфер обновлён: {old_channels} → {self.config.channels} каналов")
                            except Exception as e:
                                logger.warning(f"⚠️ [OUTPUT] Ошибка обновления буфера: {e}")
                        
                        logger.info(
                            f"✅ [OUTPUT] Параметры нормализованы: "
                            f"rate={old_rate}Hz → {self.config.sample_rate}Hz, "
                            f"channels={old_channels} → {self.config.channels}"
                        )
                except Exception as e:
                    logger.warning(f"⚠️ [OUTPUT] Ошибка нормализации параметров: {e}")
            
            # 7. ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Обновляем tracking поля
            with self._device_tracking_lock:
                self.output_device_name = new_name
                self._current_output_device_id = new_id
                self._is_current_device_bluetooth = is_bluetooth
                self._last_device_check_time = time.time()
            
            # 8. Сбрасываем _stop_event для следующего воспроизведения
            self._stop_event.clear()
            
            # 9. ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Вызываем _start_audio_stream() для создания нового потока
            # Для BT устройств передаем device_id=None
            device_id_for_start = None if is_bluetooth else new_id
            logger.info(f"🔍 [OUTPUT] Создаем новый поток для устройства \"{new_name}\" (device_id={device_id_for_start}, BT={is_bluetooth})...")
            success = self._start_audio_stream(sync_output=True, device_id=device_id_for_start)
            if success:
                logger.info(f"✅ [OUTPUT] Новый поток успешно создан для устройства \"{new_name}\"")
                logger.info(f"✅ [OUTPUT] SwitchAudioSource → {new_name}, delay={switch_delay}с, stream created successfully")
            else:
                logger.error(f"❌ [OUTPUT] Не удалось создать новый поток для устройства \"{new_name}\"")
            
            logger.info(
                f"✅ [OUTPUT] Переключение завершено: "
                f"\"{old_name}\" (ID={old_id}, BT={old_is_bluetooth}) → "
                f"\"{new_name}\" (ID={new_id}, BT={is_bluetooth}). "
                f"Задержки: stop={2.0 if old_is_bluetooth else 0.3}с, switch={switch_delay}с"
            )
            
        except Exception as e:
            logger.error(f"❌ [OUTPUT] Ошибка переключения устройства: {e}", exc_info=True)
            # В случае ошибки сбрасываем _stop_event чтобы не заблокировать дальнейшее воспроизведение
            self._stop_event.clear()

    def _audio_callback(self, outdata, frames, time_info, status):
        """Callback для воспроизведения аудио"""
        try:
            if status:
                logger.warning(f"⚠️ Статус аудио потока: {status}")

            # Получаем данные из буфера (2D: frames x channels)
            data = self.chunk_buffer.get_playback_data(frames)

            # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Используем фактическое количество каналов потока
            # Поток может быть создан с другим количеством каналов, чем self.config.channels
            actual_stream_channels = outdata.shape[1] if outdata.ndim >= 2 else 1

            # 🔍 ДИАГНОСТИКА: Увеличено логирование для отладки
            if not hasattr(self, '_callback_debug_count'):
                self._callback_debug_count = 0
            if self._callback_debug_count < 10:  # ✅ Увеличено с 3 до 10
                buffer_size = self.chunk_buffer.buffer_size
                has_data = len(data) > 0
                logger.info(f"🎵 [CALLBACK #{self._callback_debug_count}] frames={frames}, data_shape={data.shape if has_data else 'EMPTY'}, buffer_size={buffer_size}, config_channels={self.config.channels}, stream_channels={actual_stream_channels}")
                self._callback_debug_count += 1
            elif self._callback_debug_count == 10:
                logger.info(f"🔇 [CALLBACK] Дальнейшее логирование callback отключено (работает нормально)")
                self._callback_debug_count += 1
            
            # Формируем выходные данные (ожидаем 2D)
            if len(data) == 0:
                outdata[:] = 0
            else:
                # ✅ FIX: Конвертация каналов перед записью в outdata
                # Используем фактическое количество каналов потока, а не self.config.channels
                # Если данные стерео (2 канала), а поток моно (1 канал) — конвертируем в моно
                if data.ndim == 2 and data.shape[1] > actual_stream_channels:
                    # Усредняем каналы для конвертации стерео → моно
                    data = np.mean(data, axis=1, keepdims=True)
                    logger.debug(f"🔧 [CALLBACK] Конвертировано {data.shape[1]} каналов → {actual_stream_channels} каналов: shape={data.shape}")
                # Если у нас моно-данные, а поток ждёт стерео — дублируем канал
                elif data.ndim == 2 and data.shape[1] == 1 and actual_stream_channels > 1:
                    data = np.repeat(data, actual_stream_channels, axis=1)
                    logger.debug(f"🔧 [CALLBACK] Дублирован моно канал → {actual_stream_channels} каналов: shape={data.shape}")
                elif data.ndim == 1 and actual_stream_channels > 1:
                    # На всякий случай обрабатываем 1D буфер
                    mono = data.reshape(-1, 1)
                    data = np.repeat(mono, actual_stream_channels, axis=1)
                    logger.debug(f"🔧 [CALLBACK] Конвертирован 1D буфер → {actual_stream_channels} каналов: shape={data.shape}")
                elif data.ndim == 1 and actual_stream_channels == 1:
                    # 1D → 2D для моно
                    data = data.reshape(-1, 1)
                    logger.debug(f"🔧 [CALLBACK] Конвертирован 1D буфер → 2D моно: shape={data.shape}")

                # ✅ FIX: Проверяем, что data имеет правильную форму перед записью
                if data.ndim != 2:
                    logger.error(f"❌ [CALLBACK] Неожиданная размерность data: {data.ndim}, shape={data.shape}")
                    outdata[:] = 0
                    return

                # ✅ FIX: Используем фактическое количество каналов потока
                copy_ch = min(actual_stream_channels, data.shape[1])
                out_frames = min(frames, data.shape[0])
                
                # ✅ FIX: Проверяем совместимость форм перед записью (используем actual_stream_channels)
                if outdata.shape[1] != actual_stream_channels:
                    logger.error(f"❌ [CALLBACK] Несовместимость форм: outdata.shape={outdata.shape}, expected_channels={actual_stream_channels}")
                    outdata[:] = 0
                    return
                
                # ✅ FIX: Записываем данные с учетом фактического количества каналов потока
                outdata[:out_frames, :copy_ch] = data[:out_frames, :copy_ch]
                if copy_ch < actual_stream_channels:
                    # Если входных каналов меньше — копируем последний доступный канал
                    last_col = min(data.shape[1], 1) - 1
                    fill_segment = data[:out_frames, last_col:last_col + 1]
                    for ch in range(copy_ch, actual_stream_channels):
                        outdata[:out_frames, ch] = fill_segment.squeeze(axis=1)
                if out_frames < frames:
                    outdata[out_frames:, :] = 0
                
        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}", exc_info=True)
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
            try:
                self.chunk_buffer.set_channels(new_ch)
            except Exception:
                pass
            # Запускаем заново если были в состоянии PLAYING
            if self.state_manager.is_playing or self.state_manager.is_paused:
                return self._start_audio_stream()
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка reconfigure_channels: {e}")
            return False
    
    def _playback_loop(self):
        """Основной цикл воспроизведения - упрощенная версия"""
        try:
            logger.info("🔄 Playback loop запущен")
            
            while not self._stop_event.is_set():
                # Проверяем паузу
                self._pause_event.wait()
                
                # Получаем следующий чанк
                chunk_info = self.chunk_buffer.get_next_chunk(timeout=0.1)
                
                if chunk_info is not None:
                    # Отмечаем начало обработки
                    chunk_info.state = ChunkState.PLAYING
                    
                    # Callback начала чанка
                    if self._on_chunk_started:
                        self._on_chunk_started(chunk_info)
                    
                    # Добавляем в буфер воспроизведения
                    if not self.chunk_buffer.add_to_playback_buffer(chunk_info):
                        logger.error(f"❌ Ошибка добавления чанка {chunk_info.id} в буфер воспроизведения")
                        chunk_info.state = ChunkState.ERROR
                        continue
                    
                    # Ждем завершения воспроизведения этого чанка
                    self._wait_for_chunk_completion(chunk_info)
                    
                    # Отмечаем завершение
                    self.chunk_buffer.mark_chunk_completed(chunk_info)
                    
                    # Callback завершения чанка
                    if self._on_chunk_completed:
                        self._on_chunk_completed(chunk_info)
                    
                    logger.info(f"✅ Чанк обработан: {chunk_info.id}")
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
                logger.info(f"⏹️ Прерывание чанка {chunk_info.id} по stop_event")
                return
            if not self.chunk_buffer.has_data:
                logger.info(f"✅ Чанк {chunk_info.id} полностью воспроизведен")
                return
            
            time.sleep(0.01)
        
        logger.warning(f"⚠️ Таймаут ожидания завершения чанка {chunk_info.id}")
    
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
            
            # Останавливаем фоновый мониторинг output устройства
            self._stop_output_monitoring()

            # Очищаем буферы
            self.chunk_buffer.clear_all()

            # Очищаем кэш устройств (при завершении плеера)
            with self._device_tracking_lock:
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
