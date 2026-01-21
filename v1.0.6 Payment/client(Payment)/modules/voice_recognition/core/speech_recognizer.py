"""
Основной класс распознавания речи с использованием SpeechRecognition
"""

import asyncio
import logging
import time
import threading
from typing import Callable, Dict, Any, List, Optional
import sounddevice as sd
import numpy as np
import speech_recognition as sr

from .types import (
    RecognitionConfig, RecognitionResult, RecognitionState, 
    RecognitionEventType, RecognitionMetrics, AudioStreamState
)
# ✅ ЦИКЛ 3: AudioDeviceMonitor удален - используем DeviceChangePublisher через EventBus
from .audio_recovery_manager import AudioRecoveryManager, preflight_check

# ✅ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ УСТРОЙСТВ
from modules.audio_core import DeviceParamsNormalizer, InputParams
# ✅ ЦИКЛ 2: AudioStreamManager для управления PortAudio streams
from modules.audio_core.stream_manager import AudioStreamManager, StreamConfig, StreamOperationResult

logger = logging.getLogger(__name__)

class SpeechRecognizer:
    """Основной класс распознавания речи"""
    
    def __init__(self, config: RecognitionConfig):
        self.config = config
        self.state = RecognitionState.IDLE
        
        # Аудио данные
        self.audio_data = []
        self.is_listening = False
        self.listen_start_time = None
        
        # Threading
        self.listen_thread = None
        self.stop_event = threading.Event()
        self.audio_lock = threading.Lock()
        
        # Event loop для асинхронных операций из audio callback
        self._main_loop = None
        
        # Callbacks
        self.state_callbacks: Dict[RecognitionState, Callable] = {}
        self.event_callbacks: Dict[RecognitionEventType, Callable] = {}
        
        # Метрики
        self.metrics = RecognitionMetrics()

        # Управление состоянием запуска/остановки
        self._start_lock = asyncio.Lock()
        self._initializing = False
        self._cooldown_until = 0.0
        self._last_successful_start = 0.0
        
        # State machine для аудио-потока (предотвращение гонок)
        self._stream_state = AudioStreamState.IDLE
        self._stream_state_lock = threading.RLock()  # RLock для многопоточного доступа
        self._last_stop_time = 0.0  # Время последней остановки для дебаунса
        self._min_stop_start_interval = 0.3  # Минимальный интервал между stop→start (300мс)
        
        # Audio Recovery Manager
        self.recovery_manager: Optional[AudioRecoveryManager] = None
        self.recovery_enabled = bool(getattr(self.config, "enable_audio_recovery", True))
        self._current_stream: Optional[sd.InputStream] = None
        self._stream_lock = threading.RLock()  # ✅ FIX: Блокировка для защиты _current_stream от race conditions
        self._device_priority: List[Any] = []
        
        # ✅ ЦИКЛ 2: AudioStreamManager для управления PortAudio streams
        self._stream_manager = AudioStreamManager(stream_type="input")

        # Параметры входного устройства - используем системные дефолты
        self.actual_input_rate: int = self.config.sample_rate
        self.actual_input_channels: int = self.config.channels
        self.input_device_info: Dict[str, Any] = {}

        # PRIMARY идентификатор - NAME (стабильный, для логики и сравнений)
        self.input_device_name: Optional[str] = None

        # RUNTIME идентификатор - ID (для sounddevice API, может меняться)
        self.input_device_id: Any = None

        self.output_device_info: Dict[str, Any] = {}
        self.output_device_name: Optional[str] = None
        self.output_device_id: Any = None
        self.host_apis: List[Dict[str, Any]] = []

        # Кэш для быстрого маппинга name → id
        self._device_name_to_id_cache: Dict[str, int] = {}
        self._device_cache_valid: bool = False

        # УБРАНО: prepared_device_id и prepared_device_name (избыточно)
        # Теперь используем только input_device_id и input_device_name

        self.last_audio_stats: Dict[str, Any] = {}
        self._async_loop: Optional[asyncio.AbstractEventLoop] = None
        self._restart_task: Optional[Any] = None

        # ✅ ЦИКЛ 3: AudioDeviceMonitor удален - используем DeviceChangePublisher через EventBus
        # Мониторинг устройств теперь централизован в DeviceChangePublisher
        self.last_device_change_time = 0.0
        self.stabilization_delay = 0.3  # 300мс задержка стабилизации
        
        # ✅ ИТЕРАЦИЯ 4: Инициализация нормализатора параметров устройств (пока не используется)
        try:
            from config.unified_config_loader import unified_config
            audio_config = unified_config.get_audio_config()
            normalizer_config = audio_config.get('normalization', {})
            if normalizer_config:
                self._params_normalizer = DeviceParamsNormalizer(normalizer_config)
                self._normalized_input_params: Optional[InputParams] = None
                logger.debug("✅ DeviceParamsNormalizer инициализирован для INPUT (готов к использованию)")
            else:
                logger.warning("⚠️ Конфигурация нормализации не найдена, используем fallback")
                self._params_normalizer = None
                self._normalized_input_params = None
        except Exception as e:
            logger.warning(f"⚠️ Ошибка инициализации нормализатора: {e}")
            self._params_normalizer = None
            self._normalized_input_params = None

    def set_event_loop(self, loop: asyncio.AbstractEventLoop):
        """Устанавливает event loop для асинхронных операций из audio callback."""
        self._main_loop = loop
        logger.debug(f"🔧 Event loop установлен в SpeechRecognizer: {loop}")

        # Retry параметры для мягкого перезапуска потока (адаптивные для BT-устройств)
        self.max_stream_start_retries = 7  # Увеличено для BT-устройств (было 5)
        self.retry_delay = 0.8  # 800мс между попытками (проводные устройства)
        self.first_chunk_timeout = 2.0  # 2s ожидание первого чанка по умолчанию
        self.first_chunk_timeout_bt = 3.5  # 3.5s для BT-маршрутов
        self.retry_delay_bt = 1.2  # BT-устройства стабилизируются дольше
        self.bt_prestart_delay = 0.5  # 500мс задержка перед start() для BT (FIX для Error 89)

        # Счётчик пустых чанков для диагностики CoreAudio overload
        self.empty_chunk_counter = 0
        self.empty_chunk_threshold = 10  # Предупреждение после 10 пустых подряд
        self.first_chunk_received = False
        self._signal_threshold = 1e-5  # Минимальный пик для признания сигнала
        self._max_silence_start_bt = 0.35  # секунды тишины для BT-профиля
        self._max_silence_start_default = 1.0  # секунды тишины для проводных/встроенных устройств
        self.allow_device_fallback = False  # используем только текущее системное устройство без цепочки fallback
        self.auto_reselect_default = True  # обновлять ли устройство, если системный default сменился

        # Инициализируем распознаватель
        self._init_recognizer()

    @property
    def audio_data_len(self) -> int:
        """Возвращает количество записанных аудио чанков"""
        with self.audio_lock:
            return len(self.audio_data)

    def __del__(self):
        """Деструктор для корректной остановки мониторинга"""
        try:
            # ✅ ЦИКЛ 1: Старый polling отключен
            if hasattr(self, 'device_monitor') and self.device_monitor is not None and self.device_monitor.is_monitoring():
                self.device_monitor.stop_monitoring()
        except Exception:
            pass  # Игнорируем ошибки в деструкторе
        
    def _init_recognizer(self):
        """Инициализирует распознаватель речи"""
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            
            # Настраиваем параметры
            self.recognizer.energy_threshold = self.config.energy_threshold
            self.recognizer.dynamic_energy_threshold = self.config.dynamic_energy_threshold
            self.recognizer.pause_threshold = self.config.pause_threshold
            self.recognizer.phrase_threshold = self.config.phrase_threshold
            self.recognizer.non_speaking_duration = self.config.non_speaking_duration
            
            # Настраиваем микрофон для фонового шума (БЕЗ БЛОКИРОВКИ)
            try:
                with self.microphone as source:
                    logger.info("🔧 Настраиваем микрофон для фонового шума...")
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    logger.info(f"📊 Энергетический порог установлен: {self.recognizer.energy_threshold}")
            except Exception as mic_error:
                # НЕ блокируем приложение - используем значения по умолчанию
                logger.warning(f"⚠️ Не удалось настроить микрофон (используем значения по умолчанию): {mic_error}")
                self.recognizer.energy_threshold = 300  # Значение по умолчанию
            
            logger.info(f"✅ Распознаватель речи инициализирован (язык: {self.config.language})")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка инициализации распознавателя (продолжаем работу): {e}")
            # НЕ устанавливаем ERROR - позволяем работать в degraded режиме
    
    def _build_stream_config_for_device(self, device_name: str, device_id: Optional[int], is_bluetooth: bool = False) -> StreamConfig:
        """
        ✅ РЕФАКТОРИНГ: Создает StreamConfig для устройства (переиспользуется в разных местах)
        
        Args:
            device_name: Имя устройства
            device_id: PortAudio ID устройства (None для BT)
            is_bluetooth: Является ли устройство Bluetooth
        
        Returns:
            StreamConfig для создания потока
        """
        # Получаем информацию об устройстве для определения параметров
        device_info = {}
        if device_id is not None:
            try:
                device_info = sd.query_devices(device_id, 'input')
            except Exception as e:
                logger.warning(f"⚠️ Не удалось получить информацию об устройстве {device_id}: {e}")
        
        # Определяем параметры устройства
        samplerate = device_info.get('default_samplerate') or self.config.sample_rate
        channels_available = int(device_info.get('max_input_channels') or 1)
        channels_target = max(1, self.config.channels)
        
        # Нормализация параметров (если доступен нормализатор)
        if device_info and self._params_normalizer:
            try:
                normalized = self._params_normalizer.select_input_params(device_info)
                actual_rate = normalized.device_rate
                actual_channels = normalized.channels
            except Exception:
                # Fallback на существующую логику
                actual_rate = float(samplerate)
                actual_channels = 1 if is_bluetooth and channels_available >= 1 else max(1, min(channels_available, channels_target))
        else:
            # Fallback на существующую логику
            if is_bluetooth:
                actual_rate = float(samplerate)
                actual_channels = 1 if channels_available >= 1 else max(1, min(channels_available, channels_target))
            else:
                actual_rate = float(samplerate)
                actual_channels = max(1, min(channels_available, channels_target))
        
        return StreamConfig(
            device_id=device_id,
            device_name=device_name,
            samplerate=int(actual_rate),
            channels=actual_channels,
            dtype='float32',
            blocksize=self.config.chunk_size,
            callback=self._audio_callback,
            is_bluetooth=is_bluetooth
        )
    
    def _on_device_changed(self, old_device_id: Any, new_device_id: Any):
        """
        ✅ УСТАРЕВШИЙ: Callback для смены аудио устройства (старый формат для обратной совместимости).
        
        ВАЖНО: Этот метод вызывается только из старого AudioDeviceMonitor (который удален).
        Новый метод on_device_changed() используется из VoiceRecognitionIntegration.
        """
        logger.warning("⚠️ [MONITOR] _on_device_changed вызван (устаревший метод), используйте on_device_changed()")
        # Для обратной совместимости просто логируем
        self.last_device_change_time = time.time()
        self._invalidate_device_cache()
    
    async def on_device_changed(self, device_name: str, device_id: Optional[int], is_bluetooth: bool = False):
        """
        ✅ РЕФАКТОРИНГ: Обработка смены INPUT устройства через AudioStreamManager
        
        Вызывается из VoiceRecognitionIntegration при событии device.default_input_changed.
        
        Args:
            device_name: Имя нового устройства
            device_id: PortAudio ID нового устройства (None для BT)
            is_bluetooth: Является ли устройство Bluetooth
        """
        try:
            self.last_device_change_time = time.time()
            
            # Получаем текущее имя устройства
            old_device_name = self.input_device_name
            old_device_id = self.input_device_id
            
            logger.info(
                f"🔄 [DEVICE_CHANGE] Смена INPUT устройства: "
                f"\"{old_device_name}\" (ID={old_device_id}) → "
                f"\"{device_name}\" (ID={device_id}, BT={is_bluetooth})"
            )
            
            logger.debug(
                f"🔍 [DEVICE_CHANGE] Текущее состояние: "
                f"state={self.state.value}, "
                f"is_listening={self.is_listening}"
            )
            
            # Инвалидируем кэш при любом изменении устройств
            self._invalidate_device_cache()
            
            # Сравниваем по именам
            if device_name == old_device_name:
                # Имя не изменилось, только ID мог измениться
                logger.debug(
                    f"ℹ️ [DEVICE_CHANGE] Имя устройства не изменилось: \"{device_name}\", "
                    f"обновляем только ID ({old_device_id} → {device_id})"
                )
                self.input_device_id = device_id
                return
            
            # Реальная смена устройства (изменилось имя)
            logger.info(
                f"✅ [DEVICE_CHANGE] РЕАЛЬНАЯ смена устройства: \"{old_device_name}\" → \"{device_name}\""
            )
            
            # Если сейчас идет запись - останавливаем gracefully
            if self.state == RecognitionState.LISTENING:
                logger.warning(
                    f"⚠️ [DEVICE_CHANGE] Устройство изменилось во время записи - останавливаем запись. "
                    f"Пользователь должен повторно нажать SPACE для записи на новом устройстве."
                )
                self._graceful_stop_listening(reason="device_changed")
                # НЕ перезапускаем автоматически - пользователь должен сам решить
                return
            
            # Если запись НЕ идет - переключаем устройство через AudioStreamManager
            logger.debug(f"🔍 [DEVICE_CHANGE] state != LISTENING - переключаем устройство через AudioStreamManager")
            
            # Создаем StreamConfig для нового устройства
            stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
            
            # Получаем текущий поток
            with self._stream_lock:
                old_stream = self._current_stream
            
            # Переключаем устройство через AudioStreamManager
            if old_stream is None:
                # Если потока нет, создаем новый
                logger.debug("🔍 [DEVICE_CHANGE] Текущего потока нет, создаем новый через AudioStreamManager")
                result = await self._stream_manager.create_stream(stream_config)
            else:
                # Если поток есть, переключаем устройство
                logger.debug("🔍 [DEVICE_CHANGE] Переключаем устройство через AudioStreamManager.switch_device")
                result = await self._stream_manager.switch_device(old_stream, stream_config)
            
            if result.success and result.stream:
                # Обновляем ссылку на поток и параметры устройства
                with self._stream_lock:
                    self._current_stream = result.stream
                
                self.input_device_name = device_name
                self.input_device_id = device_id
                self.actual_input_rate = stream_config.samplerate
                self.actual_input_channels = stream_config.channels
                
                logger.info(
                    f"✅ [DEVICE_CHANGE] Устройство успешно переключено: \"{device_name}\" "
                    f"(ID={device_id}, rate={stream_config.samplerate}Hz, channels={stream_config.channels})"
                )
            else:
                logger.error(
                    f"❌ [DEVICE_CHANGE] Не удалось переключить устройство: {result.error_message} "
                    f"(error_code={result.error_code})"
                )
                # Обновляем только имя и ID, но не поток
                self.input_device_name = device_name
                self.input_device_id = device_id
                
        except Exception as e:
            logger.error(f"❌ [DEVICE_CHANGE] Ошибка обработки смены устройства: {e}", exc_info=True)

    def _graceful_stop_listening(self, reason: str):
        """Безопасно останавливает текущий поток прослушивания (синхронно)."""
        try:
            # ✅ FIX: Устанавливаем stop_event ПЕРЕД is_listening для более быстрой реакции
            self.stop_event.set()
            # ✅ FIX: Используем memory barrier для гарантии видимости в других потоках
            self.is_listening = False
        except Exception:
            pass

        # ✅ FIX: Обновляем состояние аудио-потока
        with self._stream_state_lock:
            if self._stream_state == AudioStreamState.RUNNING:
                old_state = self._stream_state
                self._stream_state = AudioStreamState.STOPPING
                self._last_stop_time = time.time()
                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (graceful stop: {reason})")

        # ВАЖНО: Принудительно закрываем аудио поток перед join треда
        with self._stream_lock:
            if self._current_stream:
                try:
                    logger.debug(f"🛑 Принудительное закрытие аудио потока (reason={reason})")
                    self._current_stream.stop()
                    self._current_stream.close()
                except Exception as e:
                    logger.debug(f"⚠️ Ошибка закрытия потока в _graceful_stop: {e}")
                finally:
                    self._current_stream = None  # Всегда очищаем ссылку

        thread = self.listen_thread
        if thread and thread.is_alive():
            thread.join(timeout=0.5)  # ✅ FIX: Уменьшено с 2.0 до 0.5 секунды для быстрого отклика
            if thread.is_alive():
                logger.warning("⚠️ Поток прослушивания не завершился за 0.5с (reason=%s), продолжаем без ожидания", reason)
        self.listen_thread = None

        with self.audio_lock:
            self.audio_data = []

        self.is_listening = False
        self.first_chunk_received = False
        self.empty_chunk_counter = 0
        self.state = RecognitionState.IDLE
        
        # ✅ FIX: Возвращаемся в IDLE после graceful stop
        with self._stream_state_lock:
            old_state = self._stream_state
            self._stream_state = AudioStreamState.IDLE
            logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (graceful stop завершен)")

        # Сбрасываем stop_event, чтобы следующий запуск получил чистый объект
        self.stop_event = threading.Event()

        loop = self._async_loop
        if loop:
            try:
                asyncio.run_coroutine_threadsafe(
                    self._notify_event(RecognitionEventType.LISTENING_STOP, reason=reason),
                    loop,
                )
            except Exception as e:
                logger.debug("⚠️ Не удалось отправить LISTENING_STOP при принудительной остановке: %s", e)
            try:
                asyncio.run_coroutine_threadsafe(
                    self._notify_state_change(RecognitionState.IDLE, reason=reason),
                    loop,
                )
            except Exception as e:
                logger.debug("⚠️ Не удалось отправить state=IDLE при принудительной остановке: %s", e)

    def _schedule_listening_restart(self, delay: float):
        """Планирует повторный запуск прослушивания после стабилизации устройства."""
        loop = self._async_loop
        if not loop:
            logger.debug("⚠️ Невозможно перезапустить прослушивание: event loop не задан")
            return

        # Отменяем предыдущую задачу перезапуска, если она ещё активна
        if self._restart_task and not self._restart_task.done():
            self._restart_task.cancel()
            self._restart_task = None

        async def _restart():
            try:
                await asyncio.sleep(max(delay, 0.0))
                if self.state == RecognitionState.IDLE and not self.is_listening:
                    logger.info("🔁 Перезапускаем прослушивание после смены устройства")
                    await self.start_listening()
            except asyncio.CancelledError:
                logger.debug("🔁 Задача перезапуска прослушивания отменена")
            except Exception as e:
                logger.error(f"❌ Ошибка перезапуска прослушивания: {e}")

        try:
            self._restart_task = asyncio.run_coroutine_threadsafe(_restart(), loop)
        except Exception as e:
            logger.error(f"❌ Не удалось запланировать перезапуск прослушивания: {e}")

    async def start_listening(self) -> bool:
        """Начинает прослушивание микрофона с задержкой стабилизации"""
        async with self._start_lock:
            start_time = time.time()
            try:
                # ✅ FIX: Проверка всех условий ПЕРЕД переходом в STARTING
                with self._stream_state_lock:
                    if self._stream_state != AudioStreamState.IDLE:
                        logger.warning(
                            f"⚠️ Невозможно начать прослушивание: аудио-поток в состоянии {self._stream_state.value}"
                        )
                        return False
                    
                    # Дебаунс: проверяем минимальный интервал между stop→start
                    time_since_stop = start_time - self._last_stop_time
                    if time_since_stop < self._min_stop_start_interval:
                        wait_for = self._min_stop_start_interval - time_since_stop
                        logger.debug(f"⏳ Дебаунс stop→start: ожидаем {wait_for:.3f}с")
                        await asyncio.sleep(wait_for)
                        start_time = time.time()  # Обновляем время после ожидания
                
                # Проверяем RecognitionState ДО перехода в STARTING
                if self.state != RecognitionState.IDLE:
                    logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self.state.value}")
                    return False
                if self._initializing:
                    logger.debug("🔁 Запуск прослушивания уже выполняется, пропускаем повторный вызов")
                    return False
                
                # ✅ FIX: Переходим в состояние STARTING только после всех проверок
                with self._stream_state_lock:
                    old_state = self._stream_state
                    self._stream_state = AudioStreamState.STARTING
                    logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value}")

                if start_time < self._cooldown_until:
                    wait_for = self._cooldown_until - start_time
                    logger.debug(f"⏳ Ожидаем cooldown перед запуском прослушивания: {wait_for:.3f}с")
                    await asyncio.sleep(wait_for)

                self._initializing = True

                self._async_loop = asyncio.get_running_loop()
                if self._restart_task and not self._restart_task.done():
                    self._restart_task.cancel()
                    self._restart_task = None

                # Проверяем, не было ли недавней смены устройства
                time_since_device_change = start_time - self.last_device_change_time

                if time_since_device_change < self.stabilization_delay:
                    remaining_delay = self.stabilization_delay - time_since_device_change
                    logger.info(f"⏳ Ждем стабилизации устройства: {remaining_delay:.3f}с")
                    await asyncio.sleep(remaining_delay)

                # ✅ ЦИКЛ 1: Старый polling отключен - используем DeviceChangePublisher через EventBus
                # Мониторинг устройств теперь происходит через события device.default_input_changed
                # if self.device_monitor and not self.device_monitor.is_monitoring():
                #     self.device_monitor.start_monitoring()
                #     logger.debug("🚀 Мониторинг устройств запущен")

                device_id = self._prepare_input_device()
                if device_id is None:
                    logger.error("❌ Входное устройство недоступно, запись не запущена")
                    # ✅ FIX: Возвращаемся в IDLE при ошибке устройства
                    with self._stream_state_lock:
                        old_state = self._stream_state
                        self._stream_state = AudioStreamState.IDLE
                        logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (устройство недоступно)")
                    self._device_priority = []
                    self._schedule_cooldown(0.5)
                    return False
                
                # ✅ ОПТИМИЗАЦИЯ: Проверяем, можно ли переиспользовать существующий поток
                device_name = self.input_device_info.get('name', 'Unknown Device') if hasattr(self, 'input_device_info') else 'Unknown Device'
                with self._stream_lock:
                    if self._current_stream is not None and self._current_stream.active:
                        # Проверяем, что устройство не изменилось
                        current_device_id = getattr(self, 'input_device_id', None)
                        current_device_name = getattr(self, 'input_device_name', None)
                        
                        if current_device_id == device_id and current_device_name == device_name:
                            logger.info(f"✅ Переиспользуем существующий поток для устройства '{device_name}' (ID={device_id})")
                            # Поток уже активен и устройство не изменилось - переиспользуем
                            self._device_priority = self._build_device_priority(device_id)
                            self.state = RecognitionState.LISTENING
                            self.is_listening = True
                            self.audio_data = []
                            self.stop_event.clear()
                            
                            # Уведомляем о начале прослушивания
                            await self._notify_state_change(RecognitionState.LISTENING)
                            await self._notify_event(RecognitionEventType.LISTENING_START)
                            
                            # Переходим в состояние RUNNING (поток уже активен)
                            with self._stream_state_lock:
                                old_state = self._stream_state
                                self._stream_state = AudioStreamState.RUNNING
                                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (переиспользование потока)")
                            
                            self._initializing = False
                            return True
                        else:
                            logger.info(f"🔄 Устройство изменилось: '{current_device_name}' (ID={current_device_id}) → '{device_name}' (ID={device_id}), создаем новый поток")
                            # Устройство изменилось - закрываем старый поток
                            try:
                                is_bluetooth_old = self._is_bluetooth_device(current_device_name or '')
                                await self._stream_manager.close_stream(self._current_stream, is_bluetooth=is_bluetooth_old)
                            except Exception as e:
                                logger.warning(f"⚠️ Ошибка закрытия старого потока: {e}")
                            finally:
                                self._current_stream = None
                
                # Preflight проверка устройства
                preflight_success, preflight_peak = await preflight_check(device_id, device_name, duration_ms=100)
                
                if not preflight_success:
                    logger.warning(f"⚠️ Preflight check failed: peak={preflight_peak:.6f}")
                    # Если есть RecoveryManager, инициируем восстановление
                    if self.recovery_enabled and self.recovery_manager:
                        logger.info("🔧 Инициируем восстановление после failed preflight")
                        # Сбрасываем счетчик для немедленного восстановления
                        self.recovery_manager.stats.silent_chunks = 10  # Порог A
                        recovery_step = self.recovery_manager.on_chunk_received(
                            np.zeros((1024, 1), dtype='float32'), 0.0, 0.0
                        )
                        if recovery_step:
                            await self._execute_recovery(recovery_step)
                else:
                    logger.info(f"✅ Preflight check passed: peak={preflight_peak:.6f}")
                
                self._device_priority = self._build_device_priority(device_id)
                self.state = RecognitionState.LISTENING
                self.is_listening = True
                self.audio_data = []
                self.stop_event.clear()

                # Уведомляем о начале прослушивания
                await self._notify_state_change(RecognitionState.LISTENING)
                await self._notify_event(RecognitionEventType.LISTENING_START)
                logger.debug(
                    "🎤 Параметры прослушивания: target_rate=%sHz, channels=%s, chunk=%s, dtype=%s",
                    self.config.sample_rate,
                    self.config.channels,
                    self.config.chunk_size,
                    self.config.dtype,
                )

                # Запускаем поток прослушивания
                self.listen_thread = threading.Thread(
                    target=self._run_listening,
                    name="SpeechListening",
                    daemon=True
                )
                self.listen_thread.start()
                
                # ✅ FIX: Переходим в состояние RUNNING после успешного запуска потока
                with self._stream_state_lock:
                    old_state = self._stream_state
                    self._stream_state = AudioStreamState.RUNNING
                    logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value}")

                logger.info("🎤 Прослушивание микрофона начато")
                return True

            except Exception as e:
                logger.warning(f"⚠️ Ошибка начала прослушивания (продолжаем работу): {e}")
                # НЕ устанавливаем ERROR - возвращаемся в IDLE для повторных попыток
                with self._stream_state_lock:
                    old_state = self._stream_state
                    self._stream_state = AudioStreamState.IDLE
                    logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (ошибка)")
                self.state = RecognitionState.IDLE
                self._device_priority = []
                await self._notify_state_change(RecognitionState.IDLE, error=str(e))
                self._schedule_cooldown(0.5)
                return False
            finally:
                self._initializing = False
            
    async def stop_listening(self) -> RecognitionResult:
        """Останавливает прослушивание и возвращает результат распознавания"""
        try:
            # ✅ FIX: Проверка всех условий ПЕРЕД переходом в STOPPING
            with self._stream_state_lock:
                if self._stream_state != AudioStreamState.RUNNING:
                    logger.warning(
                        f"⚠️ Невозможно остановить прослушивание: аудио-поток в состоянии {self._stream_state.value}"
                    )
                    return RecognitionResult(text="", error="Not listening")
            
            # Проверяем RecognitionState ДО перехода в STOPPING
            if self.state != RecognitionState.LISTENING:
                logger.warning(f"⚠️ Невозможно остановить прослушивание в состоянии {self.state.value}")
                return RecognitionResult(text="", error="Not listening")
            
            # ✅ FIX: Переходим в состояние STOPPING только после всех проверок
            with self._stream_state_lock:
                old_state = self._stream_state
                self._stream_state = AudioStreamState.STOPPING
                self._last_stop_time = time.time()  # Сохраняем время остановки для дебаунса
                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value}")
                
            self.state = RecognitionState.PROCESSING
            # ✅ FIX: Устанавливаем stop_event ПЕРЕД is_listening для более быстрой реакции потока
            self.stop_event.set()
            # ✅ FIX: Используем явное присваивание для memory barrier (гарантия видимости в других потоках)
            self.is_listening = False
            
            # ✅ ЦИКЛ 1: Старый polling отключен - DeviceChangePublisher управляет мониторингом
            # if self.device_monitor and self.device_monitor.is_monitoring():
            #     self.device_monitor.stop_monitoring()
            #     logger.debug("🛑 Мониторинг устройств остановлен")
            
            # Уведомляем об остановке прослушивания
            await self._notify_event(RecognitionEventType.LISTENING_STOP)
            await self._notify_state_change(RecognitionState.PROCESSING)
            
            # ✅ FIX: Уменьшаем таймаут ожидания потока для быстрого отклика
            if self.listen_thread and self.listen_thread.is_alive():
                logger.debug("⏳ Ожидаем завершение потока записи...")
                self.listen_thread.join(timeout=1.0)  # ✅ FIX: Уменьшено с 5.0 до 1.0 секунды
                if self.listen_thread.is_alive():
                    logger.warning("⚠️ Поток прослушивания не завершился за 1с, продолжаем без ожидания")

            # ВАЖНО: Принудительно очищаем поток после завершения треда
            with self._stream_lock:
                if self._current_stream:
                    try:
                        self._current_stream.stop()
                        self._current_stream.close()
                    except Exception as e:
                        logger.debug(f"⚠️ Ошибка закрытия потока в stop_listening: {e}")
                    finally:
                        self._current_stream = None

            # Распознаем речь
            logger.debug(
                "🎧 Завершаем запись: chunks=%s, thread_alive=%s",
                len(self.audio_data),
                self.listen_thread.is_alive() if self.listen_thread else False,
            )
            result = await self._recognize_audio()
            
            # Обновляем метрики
            self._update_metrics(result)
            
            # ✅ FIX: Переходим в состояние IDLE после успешной остановки
            with self._stream_state_lock:
                old_state = self._stream_state
                self._stream_state = AudioStreamState.IDLE
                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value}")
            
            self.state = RecognitionState.IDLE
            await self._notify_state_change(RecognitionState.IDLE)
            self._device_priority = []
            
            if result.text:
                logger.info(f"📝 Распознано: {result.text}")
            else:
                logger.warning("⚠️ Речь не распознана")
                
            return result
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки прослушивания: {e}")
            # ✅ FIX: Возвращаемся в IDLE при ошибке
            with self._stream_state_lock:
                old_state = self._stream_state
                self._stream_state = AudioStreamState.IDLE
                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (ошибка)")
            self.state = RecognitionState.ERROR
            await self._notify_state_change(RecognitionState.ERROR, error=str(e))
            return RecognitionResult(text="", error=str(e))
            
    def _prepare_input_device(self) -> Any:
        """Выбирает и подготавливает входное и выходное устройство"""
        try:
            try:
                self.host_apis = sd.query_hostapis()
            except Exception as host_err:
                logger.debug("⚠️ Не удалось получить список host API: %s", host_err)

            # Кэш устройств обновляется в _get_system_default_input_index()
            # Не дублируем обновление здесь

            # ✅ FIX: Сначала пробуем strict=True (предпочитаем системный default)
            # Если default недоступен (например, AirPods отключены), автоматически переключаемся на альтернативы
            try:
                device_id, device_info = self._select_default_input_device(strict=True)
            except RuntimeError as e:
                # Если default устройство недоступно, пробуем найти любое доступное
                logger.warning(f"⚠️ Системное default устройство недоступно: {e}")
                logger.info("🔄 Пробуем найти альтернативное доступное устройство...")
                device_id, device_info = self._select_default_input_device(strict=False)
                if device_id is None or device_info is None:
                    logger.error("❌ Не найдено ни одного доступного входного устройства")
                    raise RuntimeError("Не найдено ни одного доступного входного устройства")
                logger.info(f"✅ Найдено альтернативное устройство: \"{device_info.get('name')}\" (ID: {device_id})")
            
            new_device_name = device_info.get('name') if device_info else None

            # ВСЕГДА обновляем поля устройства (система может переключиться)
            logger.debug(
                f"🔍 [DEVICE] Обновление устройства: \"{self.input_device_name}\" → \"{new_device_name}\" (ID: {self.input_device_id} → {device_id})"
            )
            self.input_device_info = device_info
            self.input_device_id = device_id  # RUNTIME: для sounddevice API
            self.input_device_name = new_device_name  # PRIMARY: для логики

            logger.debug(
                f"🔍 [DEVICE] Обновлены поля: "
                f"input_device_id={self.input_device_id}, "
                f"input_device_name=\"{self.input_device_name}\""
            )

            samplerate = device_info.get('default_samplerate')
            channels = device_info.get('max_input_channels')
            
            if not samplerate:
                raise RuntimeError(f"Устройство {device_info.get('name', 'Unknown')} не предоставляет default_samplerate")
            if not channels:
                raise RuntimeError(f"Устройство {device_info.get('name', 'Unknown')} не предоставляет max_input_channels")
            
            self.actual_input_rate = float(samplerate)
            self.actual_input_channels = int(channels)

            logger.info(
                "🎧 Входное устройство: \"%s\" (ID: %s) | rate=%sHz, channels=%s, latency=%.3f-%.3fms",
                self.input_device_name,
                self.input_device_id,
                self.actual_input_rate,
                self.actual_input_channels,
                (device_info.get('default_low_input_latency') or 0) * 1000,
                (device_info.get('default_high_input_latency') or 0) * 1000,
            )

            # Диагностика выходного устройства
            default_output = None
            try:
                default_setting = sd.default.device
                # Обрабатываем _InputOutputPair и обычные списки/кортежи
                if hasattr(default_setting, '__getitem__'):
                    try:
                        default_output = default_setting[1]
                    except IndexError:
                        default_output = None
            except Exception:
                default_output = None

            output_info = None
            try:
                output_info = sd.query_devices(default_output, 'output')
            except Exception:
                output_info = None

            if not output_info:
                try:
                    for idx, dev in enumerate(sd.query_devices()):
                        if dev.get('max_output_channels', 0) > 0:
                            output_info = dev
                            default_output = idx
                            break
                except Exception:
                    output_info = None

            if output_info:
                self.output_device_info = output_info
                self.output_device_id = default_output
                self.output_device_name = output_info.get('name')  # Сохраняем NAME
                logger.info(
                    "🔊 Выходное устройство: \"%s\" (ID: %s) | channels=%s, rate=%sHz",
                    self.output_device_name,
                    self.output_device_id,
                    output_info.get('max_output_channels'),
                    output_info.get('default_samplerate'),
                )
            else:
                self.output_device_info = {}
                self.output_device_id = None
                self.output_device_name = None

            # Инициализируем RecoveryManager (опционально)
            if self.recovery_enabled:
                device_name = device_info.get('name', 'Unknown Device')
                self.recovery_manager = AudioRecoveryManager(self.input_device_id, device_name)
                logger.info(f"🔧 AudioRecoveryManager инициализирован для {device_name} (ID: {self.input_device_id})")
            else:
                self.recovery_manager = None
            
            return self.input_device_id

        except Exception as e:
            logger.error("❌ Не удалось определить входное устройство: %s", e)
            raise RuntimeError(f"Ошибка определения входного устройства: {e}")

    def _run_listening(self):
        """Запускает прослушивание микрофона через sounddevice с мягким retry"""
        stream = None
        stream_started = False
        stream_closed = False  # ✅ FIX: Инициализируем в начале функции для предотвращения UnboundLocalError

        try:
            logger.info("🎤 Прослушивание микрофона начато")
            self.listen_start_time = time.time()

            device_candidates = self._device_priority[:] if self._device_priority else []
            if not device_candidates:
                # Если нет приоритетного списка, получаем текущее устройство
                primary = self.input_device_id or self._prepare_input_device()
                device_candidates = self._build_device_priority(primary)
                if not device_candidates and primary is not None:
                    device_candidates = [primary]

            for candidate_index, device_id in enumerate(device_candidates):
                try:
                    device_info = sd.query_devices(device_id, 'input')
                except Exception as info_err:
                    logger.warning(f"⚠️ Не удалось получить информацию об устройстве {device_id}: {info_err}")
                    continue

                self.input_device_info = device_info or {}
                self.input_device_id = device_id

                # ✅ FIX: Используем формат устройства (не принуждаем для BT, чтобы не конфликтовать с воспроизведением)
                device_name = device_info.get('name', '')
                samplerate = device_info.get('default_samplerate') or self.config.sample_rate
                channels_available = int(device_info.get('max_input_channels') or 1)
                channels_target = max(1, self.config.channels)
                
                # ✅ ИТЕРАЦИЯ 5: Нормализуем параметры устройства
                if device_info and self._params_normalizer:
                    try:
                        normalized = self._params_normalizer.select_input_params(device_info)
                        self._normalized_input_params = normalized
                        
                        # Обновляем параметры с нормализованными значениями
                        self.actual_input_rate = normalized.device_rate
                        self.actual_input_channels = normalized.channels
                        
                        logger.info(f"✅ [INPUT] Нормализованные параметры для \"{device_name}\":")
                        logger.info(f"   Device Rate: {normalized.device_rate} Hz")
                        logger.info(f"   Target Rate: {normalized.target_rate} Hz (ASR)")
                        logger.info(f"   Channels: {normalized.channels}")
                    except Exception as e:
                        logger.warning(f"⚠️ Ошибка нормализации параметров: {e}, используем существующую логику")
                        # Fallback на существующую логику
                        if self._is_bluetooth_device(device_name):
                            self.actual_input_rate = float(samplerate)
                            self.actual_input_channels = 1 if channels_available >= 1 else max(1, min(channels_available, channels_target))
                            logger.info(f"🔵 Bluetooth устройство обнаружено - формат: {self.actual_input_rate}Hz, {self.actual_input_channels} канал(ов)")
                        else:
                            self.actual_input_rate = float(samplerate)
                            self.actual_input_channels = max(1, min(channels_available, channels_target))
                else:
                    # Fallback на существующую логику если нормализатор недоступен
                    if not self._params_normalizer:
                        logger.debug("⚠️ Нормализатор недоступен, используем существующую логику")
                    else:
                        logger.debug("⚠️ Информация об устройстве недоступна, используем существующую логику")
                
                # Для Bluetooth устройств используем формат устройства, но ограничиваем каналы до моно если нужно
                if self._is_bluetooth_device(device_name):
                    # Используем формат устройства, но для BT предпочитаем моно
                    self.actual_input_rate = float(samplerate)
                    # Для BT устройств предпочитаем моно, но не принуждаем
                    self.actual_input_channels = 1 if channels_available >= 1 else max(1, min(channels_available, channels_target))
                    logger.info(f"🔵 Bluetooth устройство обнаружено - формат: {self.actual_input_rate}Hz, {self.actual_input_channels} канал(ов)")
                else:
                    # Для проводных/встроенных устройств используем формат устройства
                    self.actual_input_rate = float(samplerate)
                    self.actual_input_channels = max(1, min(channels_available, channels_target))

                first_chunk_timeout, retry_delay = self._get_stream_start_timing()
                max_silence_start = (
                    self._max_silence_start_bt
                    if self._is_bluetooth_device(device_info.get('name', ''))
                    else self._max_silence_start_default
                )
                if not self.allow_device_fallback:
                    max_silence_start = float("inf")
                logger.debug(
                    "🎧 Настройка окна старта: timeout=%.2fs, retry_delay=%.2fs, retries=%s, device=%s (%s)",
                    first_chunk_timeout,
                    retry_delay,
                    self.max_stream_start_retries,
                    device_id,
                    device_info.get('name'),
                )

                for attempt in range(self.max_stream_start_retries):
                    try:
                        # Сбрасываем флаг первого чанка
                        self.first_chunk_received = False
                        self.empty_chunk_counter = 0

                        # Используем консервативный подход к выбору blocksize
                        # Сначала пробуем config.chunk_size, потом увеличиваем постепенно
                        effective_blocksize = self.config.chunk_size
                        logger.info(
                            "🔧 Используем blocksize=%s (без принудительного увеличения)",
                            effective_blocksize,
                        )

                        # Засекаем время для диагностики Error 89
                        stream_create_start = time.time()

                        logger.info(
                            "🔊 AUDIO: Создание потока: device_id=%s (%s), rate=%.1fHz, channels=%s, blocksize=%s, latency=high",
                            device_id,
                            device_info.get('name'),
                            self.actual_input_rate,
                            self.actual_input_channels,
                            effective_blocksize,
                        )

                        # ✅ РЕФАКТОРИНГ: Используем переиспользуемый метод для создания StreamConfig
                        is_bluetooth = self._is_bluetooth_device(device_info.get('name', ''))
                        stream_config = self._build_stream_config_for_device(
                            device_info.get('name', ''),
                            device_id,
                            is_bluetooth
                        )
                        # Переопределяем blocksize если нужно
                        stream_config.blocksize = effective_blocksize
                        
                        # ✅ КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Создаем поток через AudioStreamManager в отдельном потоке с новым event loop
                        # Это гарантирует, что async операции выполняются даже если основной loop заблокирован
                        logger.debug("🔍 [AUDIO] Начинаем создание потока через AudioStreamManager...")
                        
                        def _run_async_in_thread(coro):
                            """Выполняет async coroutine в новом event loop в отдельном потоке"""
                            import threading
                            result_container = [None]
                            exception_container = [None]
                            
                            def _run():
                                try:
                                    new_loop = asyncio.new_event_loop()
                                    asyncio.set_event_loop(new_loop)
                                    result_container[0] = new_loop.run_until_complete(coro)
                                except Exception as e:
                                    exception_container[0] = e
                                finally:
                                    new_loop.close()
                            
                            thread = threading.Thread(target=_run, daemon=True)
                            thread.start()
                            thread.join(timeout=30.0 if is_bluetooth else 15.0)  # Таймаут для BT устройств больше
                            
                            if thread.is_alive():
                                raise TimeoutError("Таймаут создания потока через AudioStreamManager")
                            
                            if exception_container[0]:
                                raise exception_container[0]
                            
                            return result_container[0]
                        
                        result = _run_async_in_thread(
                            self._stream_manager.create_stream(stream_config, max_retries=1)
                        )
                        
                        logger.debug(f"🔍 [AUDIO] Результат создания потока: success={result.success}, stream={result.stream is not None}")
                        
                        if not result.success:
                            error_msg = f"Не удалось создать поток: {result.error_message} (error_code={result.error_code})"
                            logger.error(f"❌ [AUDIO] {error_msg}")
                            raise RuntimeError(error_msg)
                        
                        stream = result.stream
                        if stream is None:
                            error_msg = "Поток не был создан (result.stream is None)"
                            logger.error(f"❌ [AUDIO] {error_msg}")
                            raise RuntimeError(error_msg)
                        
                        logger.info(f"✅ [AUDIO] Поток успешно создан через AudioStreamManager: device_id={device_id}, stream.active={stream.active}")

                        # Сохраняем ссылку на поток для recovery
                        with self._stream_lock:
                            self._current_stream = stream

                        # ✅ FIX для Error 89: Задержка перед start() для Bluetooth устройств
                        # Bluetooth устройствам нужно время на инициализацию CoreAudio pipeline
                        if is_bluetooth:
                            logger.info(
                                "⏳ Ожидание готовности Bluetooth устройства (%.1fs)...",
                                self.bt_prestart_delay
                            )
                            time.sleep(self.bt_prestart_delay)  # Синхронная задержка

                        stream.start()

                        # Логируем время от создания до старта (диагностика Error 89)
                        stream_start_elapsed = time.time() - stream_create_start
                        logger.info(
                            f"✅ Поток запущен за {stream_start_elapsed:.3f}s (попытка {attempt + 1}/{self.max_stream_start_retries})"
                        )

                        start_wait = time.time()
                        while not self.first_chunk_received:
                            elapsed = time.time() - start_wait
                            if elapsed > first_chunk_timeout:
                                raise TimeoutError(f"Первый чанк не получен за {first_chunk_timeout:.1f}s")
                            if (
                                elapsed > max_silence_start
                                and self.empty_chunk_counter >= self.empty_chunk_threshold
                            ):
                                raise TimeoutError("В начале записи обнаружена продолжительная тишина")
                            if not self.is_listening or self.stop_event.is_set():
                                return
                            time.sleep(0.01)

                        logger.info(
                            "✅ Аудио поток стабилен: device=%s (%s), rate=%.1fHz, channels=%s",
                            device_id,
                            device_info.get('name'),
                            self.actual_input_rate,
                            self.actual_input_channels,
                        )
                        stream_started = True
                        self._last_successful_start = time.time()
                        break

                    except (sd.PortAudioError, TimeoutError) as e:
                        # Специальная обработка Error 89 (Hardware Not Running)
                        error_msg = str(e)
                        is_error_89 = "Error -9986" in error_msg or "Hardware" in error_msg

                        if is_error_89:
                            logger.warning(
                                f"⚠️ Попытка {attempt + 1}/{self.max_stream_start_retries}: "
                                f"Audio Hardware Not Running (Error 89) - устройство не готово"
                            )
                        else:
                            logger.warning(f"⚠️ Попытка {attempt + 1}/{self.max_stream_start_retries}: {e}")

                        if stream:
                            # ✅ ЦИКЛ 2: Используем AudioStreamManager для закрытия потока
                            is_bluetooth = self._is_bluetooth_device(device_info.get('name', ''))
                            loop = self._main_loop or asyncio.get_event_loop()
                            if loop.is_running():
                                import concurrent.futures
                                future = asyncio.run_coroutine_threadsafe(
                                    self._stream_manager.close_stream(stream, is_bluetooth=is_bluetooth),
                                    loop
                                )
                                future.result(timeout=5.0)
                            else:
                                asyncio.run(self._stream_manager.close_stream(stream, is_bluetooth=is_bluetooth))
                            stream = None

                        if attempt < self.max_stream_start_retries - 1 and not self.stop_event.is_set():
                            # Для Error 89 на BT устройствах увеличиваем задержку
                            current_retry_delay = retry_delay
                            if is_error_89 and self._is_bluetooth_device(device_info.get('name', '')):
                                current_retry_delay = retry_delay * 1.5  # Увеличиваем на 50%
                                logger.info(f"⏳ Увеличена задержка для BT после Error 89: {current_retry_delay:.1f}s")

                            time.sleep(current_retry_delay)
                            continue
                        break  # переходим к следующему устройству

                if stream_started:
                    break

                if self.allow_device_fallback:
                    logger.info("🔁 Переходим к fallback-устройству для записи")
                else:
                    break

            if not stream_started:
                self._schedule_cooldown(0.8)
                self._notify_microphone_unstable()
                raise RuntimeError("Не удалось запустить аудио поток ни на одном устройстве")

            # ✅ FIX: Управляем потоком вручную (БЕЗ `with stream:`) для немедленной остановки
            # Проблема: `with stream:` контекстный менеджер блокирует выход до полного закрытия потока
            # Решение: управляем потоком вручную, чтобы иметь полный контроль над остановкой
            # stream_closed уже инициализирован в начале функции
            # ✅ FIX: Поток работает - ждём завершения с немедленной остановкой при stop_event
            while self.is_listening and not self.stop_event.is_set():
                # ✅ FIX: Проверяем stop_event часто (каждые 50ms) для быстрой реакции
                time.sleep(0.05)
                
                # ✅ FIX: Дополнительная проверка - если stop_event установлен, выходим немедленно
                if self.stop_event.is_set():
                    logger.debug("🛑 stop_event установлен, выходим из цикла")
                    break

            duration = time.time() - self.listen_start_time if self.listen_start_time else 0
            logger.debug("🛑 Поток записи остановлен, длительность=%.2fs", duration)

        except Exception as e:
            logger.error(f"❌ Ошибка прослушивания микрофона: {e}")
            # ✅ FIX: Обновляем состояние при ошибке
            with self._stream_state_lock:
                old_state = self._stream_state
                self._stream_state = AudioStreamState.IDLE
                logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (ошибка в _run_listening)")
            self.state = RecognitionState.ERROR
            self._schedule_cooldown(0.6)
        finally:
            # ✅ ЦИКЛ 2: Используем AudioStreamManager для безопасного закрытия потока
            if stream and not stream_closed:
                try:
                    # Определяем тип устройства для правильной задержки
                    is_bluetooth = False
                    if hasattr(self, 'input_device_info') and self.input_device_info:
                        device_name = self.input_device_info.get('name', '')
                        is_bluetooth = self._is_bluetooth_device(device_name)
                    
                    # Используем AudioStreamManager для закрытия (синхронный вызов через event loop)
                    loop = self._main_loop or asyncio.get_event_loop()
                    if loop.is_running():
                        import concurrent.futures
                        future = asyncio.run_coroutine_threadsafe(
                            self._stream_manager.close_stream(stream, is_bluetooth=is_bluetooth),
                            loop
                        )
                        future.result(timeout=5.0)
                    else:
                        asyncio.run(self._stream_manager.close_stream(stream, is_bluetooth=is_bluetooth))
                    stream_closed = True
                    logger.debug("✅ Поток закрыт через AudioStreamManager")
                except Exception as e:
                    logger.debug(f"⚠️ Ошибка закрытия потока через AudioStreamManager: {e}")
                    stream_closed = True  # Помечаем как закрытый даже при ошибке

            # ✅ ЦИКЛ 2: Также закрываем _current_stream через AudioStreamManager если он отличается от stream
            with self._stream_lock:
                if self._current_stream and self._current_stream != stream:
                    try:
                        is_bluetooth = False
                        if hasattr(self, 'input_device_info') and self.input_device_info:
                            device_name = self.input_device_info.get('name', '')
                            is_bluetooth = self._is_bluetooth_device(device_name)
                        
                        loop = self._main_loop or asyncio.get_event_loop()
                        if loop.is_running():
                            import concurrent.futures
                            future = asyncio.run_coroutine_threadsafe(
                                self._stream_manager.close_stream(self._current_stream, is_bluetooth=is_bluetooth),
                                loop
                            )
                            future.result(timeout=5.0)
                        else:
                            asyncio.run(self._stream_manager.close_stream(self._current_stream, is_bluetooth=is_bluetooth))
                        logger.debug("✅ _current_stream закрыт через AudioStreamManager")
                    except Exception as e:
                        logger.debug(f"⚠️ Ошибка закрытия _current_stream через AudioStreamManager: {e}")

            # ВАЖНО: Очищаем ссылку на поток для предотвращения утечек ресурсов
            with self._stream_lock:
                self._current_stream = None
            logger.debug("🧹 Аудио поток очищен (_current_stream = None)")
            
            # ✅ FIX: Возвращаемся в IDLE после завершения потока
            with self._stream_state_lock:
                if self._stream_state == AudioStreamState.RUNNING:
                    old_state = self._stream_state
                    self._stream_state = AudioStreamState.IDLE
                    self._last_stop_time = time.time()
                    logger.debug(f"🔄 [AUDIO_STATE] {old_state.value} → {self._stream_state.value} (поток завершен)")
            
            logger.debug("🧹 Аудио поток очищен (_current_stream = None)")

    def _get_stream_start_timing(self) -> tuple[float, float]:
        """Подбирает тайминги старта потока в зависимости от типа устройства."""
        try:
            device_name = (self.input_device_info or {}).get("name", "") or ""
            device_name_lower = device_name.lower()
            is_bluetooth = any(
                keyword in device_name_lower
                for keyword in ("bluetooth", "airpods", "beats", "headset")
            )
            if is_bluetooth:
                return self.first_chunk_timeout_bt, self.retry_delay_bt
        except Exception:
            pass
        return self.first_chunk_timeout, self.retry_delay

    def _notify_microphone_unstable(self):
        """Уведомляет пользователя о нестабильности микрофона"""
        logger.warning("⚠️ Микрофон переключается, попробуйте через пару секунд")
        # TODO: Добавить визуальное уведомление через EventBus
        # self.event_bus.publish("notification.show", {
        #     "title": "Микрофон нестабилен",
        #     "message": "Устройство переключается, попробуйте через 2-3 секунды"
        # })

    def _schedule_cooldown(self, seconds: float):
        """Устанавливает период, в течение которого не запускаем запись повторно."""
        delay = max(0.0, seconds)
        self._cooldown_until = max(self._cooldown_until, time.time() + delay)

    @staticmethod
    def _is_bluetooth_device(name: str) -> bool:
        lowered = (name or "").lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpods", "beats", "headset", "earbud"))

    def _device_is_available(self, device_id: Any, device_info: Dict[str, Any]) -> bool:
        """Проверяет, доступно ли устройство для записи (sd.check_input_settings)."""
        try:
            samplerate = device_info.get('default_samplerate') or self.config.sample_rate
            try:
                samplerate = float(samplerate)
            except Exception:
                samplerate = float(self.config.sample_rate)
            channels_available = int(device_info.get('max_input_channels') or 1)
            channels_target = max(1, min(channels_available, self.config.channels))
            sd.check_input_settings(
                device=device_id,
                samplerate=samplerate,
                channels=channels_target,
                dtype='float32',
            )
            return True
        except Exception as e:
            logger.debug(f"⚠️ check_input_settings для устройства {device_info.get('name')} (id={device_id}) не пройден: {e}")
            return False

    # ✅ УДАЛЕНО: _refresh_portaudio_device_cache()
    # Причина: sd._terminate() / sd._initialize() опасны - убивают все потоки PortAudio
    # Новый подход: используем sd.default.device[0] как фолбэк когда устройство не найдено по имени

    def _get_system_default_input_name(self) -> Optional[str]:
        """
        Возвращает ИМЯ системного дефолтного INPUT устройства от macOS.

        ✅ NAME-BASED ПОДХОД (аналогично OUTPUT):
        1. Получаем имя от macOS через SwitchAudioSource
        2. Возвращаем только имя (не ID), т.к. ID могут меняться при переподключении

        Returns:
            str: Имя устройства или None если не удалось определить
        """
        try:
            import subprocess
            import json

            result = subprocess.run(
                ['SwitchAudioSource', '-c', '-t', 'input', '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                device_info = json.loads(result.stdout.strip())
                device_name = device_info.get('name', '')
                if device_name:
                    logger.debug(f"🔍 [INPUT] macOS default INPUT: \"{device_name}\"")
                    return device_name

        except Exception as e:
            logger.debug(f"⚠️ [INPUT] Ошибка получения имени: {e}")

        return None

    def _find_device_id_by_name_input(self, device_name: str) -> Optional[int]:
        """
        Находит ID INPUT устройства по имени в PortAudio.

        Args:
            device_name: Имя устройства для поиска

        Returns:
            int: ID устройства или None если не найдено
        """
        if not device_name:
            return None

        try:
            all_devices = sd.query_devices()
            logger.debug(f"🔍 [INPUT] Поиск \"{device_name}\" среди {len(all_devices)} устройств")

            # 1. Точное совпадение
            for idx, dev in enumerate(all_devices):
                if dev.get('max_input_channels', 0) > 0:
                    dev_name = dev.get('name', '')
                    if dev_name == device_name:
                        logger.debug(f"✅ [INPUT] Найдено (точное): ID {idx} - \"{dev_name}\"")
                        return idx

            # 2. Частичное совпадение (для разных апострофов)
            search_keywords = device_name.replace("'s", "").replace("'s", "").lower().split()
            for idx, dev in enumerate(all_devices):
                if dev.get('max_input_channels', 0) > 0:
                    dev_name = dev.get('name', '')
                    dev_name_normalized = dev_name.replace("'s", "").replace("'s", "").lower()
                    if all(keyword in dev_name_normalized for keyword in search_keywords):
                        logger.debug(f"✅ [INPUT] Найдено (частичное): ID {idx} - \"{dev_name}\"")
                        return idx

            logger.debug(f"⚠️ [INPUT] Устройство \"{device_name}\" не найдено в PortAudio")
            return None

        except Exception as e:
            logger.debug(f"⚠️ [INPUT] Ошибка поиска: {e}")
            return None

    def _safe_refresh_portaudio_cache(self) -> bool:
        """
        ОТКЛЮЧЕНО: Обновление кэша PortAudio через sd._terminate() / sd._initialize().

        ⚠️ ПРОБЛЕМА:
        - sd._terminate() убивает ВСЕ PortAudio потоки (INPUT + OUTPUT)
        - Race condition: OUTPUT может создаваться параллельно
        - Результат: CRASH приложения (PaErrorCode -9986)

        ✅ РЕШЕНИЕ:
        - Не обновляем кэш автоматически
        - Показываем пользователю сообщение о необходимости перезапуска

        Returns:
            bool: Всегда False (обновление отключено)
        """
        logger.warning("⚠️ [CACHE] Автоматическое обновление кэша ОТКЛЮЧЕНО")
        logger.info("💡 [CACHE] Для распознавания новых устройств необходим перезапуск приложения")
        return False

    def _get_system_default_input_index(self) -> Optional[int]:
        """
        Возвращает индекс системного дефолтного INPUT устройства.
        
        ✅ ФАЗА 1, ШАГ 1.1: Упрощенная логика "следуем за системным дефолтом"
        - Если feature flag device_switch_v2 включен: использует sd.default.device[0] напрямую
        - Если feature flag выключен: использует старую логику через SwitchAudioSource (fallback)
        """
        try:
            # ✅ ФАЗА 1: Проверка feature flag
            feature_config = unified_config._load_config().get("features", {}).get("device_switch_v2", {})
            use_v2_logic = feature_config.get("enabled", False)
            
            if use_v2_logic:
                # ✅ НОВАЯ ЛОГИКА: Используем системный дефолт PortAudio напрямую
                logger.debug("🔍 [INPUT][V2] Используем системный дефолт PortAudio напрямую")
                try:
                    default_setting = sd.default.device
                    if hasattr(default_setting, '__getitem__'):
                        input_device_id = default_setting[0]  # INPUT устройство (индекс 0)
                        
                        if input_device_id is not None:
                            # Проверяем что устройство действительно INPUT
                            try:
                                device_info = sd.query_devices(input_device_id, 'input')
                                if device_info and device_info.get('max_input_channels', 0) > 0:
                                    device_name = device_info.get('name', 'Unknown')
                                    logger.info(
                                        f"✅ [INPUT][V2] Системный дефолт PortAudio: "
                                        f"name=\"{device_name}\", id={input_device_id}"
                                    )
                                    return input_device_id
                                else:
                                    logger.warning(f"⚠️ [INPUT][V2] Устройство ID {input_device_id} не является INPUT устройством")
                                    return None
                            except Exception as e:
                                logger.warning(f"⚠️ [INPUT][V2] Ошибка проверки устройства ID {input_device_id}: {e}")
                                return None
                        else:
                            logger.warning("⚠️ [INPUT][V2] sd.default.device[0] вернул None")
                            return None
                    else:
                        logger.warning("⚠️ [INPUT][V2] sd.default.device не поддерживает индексацию")
                        return None
                except Exception as e:
                    logger.warning(f"⚠️ [INPUT][V2] Ошибка получения системного дефолта PortAudio: {e}")
                    return None
            
            # ✅ СТАРАЯ ЛОГИКА (fallback если feature flag выключен)
            logger.debug("🔍 [INPUT][LEGACY] Используем старую логику через SwitchAudioSource")
            # ✅ ПРИОРИТЕТ 1: Получаем имя устройства через macOS API (как для OUTPUT)
            system_device_name = self._get_system_default_input_name()
            if system_device_name:
                logger.debug(f"🔍 [INPUT] macOS default INPUT: \"{system_device_name}\"")
                # Ищем устройство по имени в PortAudio
                device_id = self._find_device_id_by_name_input(system_device_name)
                if device_id is not None:
                    logger.debug(f"✅ [INPUT] Найдено устройство по имени: \"{system_device_name}\" → ID {device_id}")
                    return device_id
                else:
                    logger.warning(f"⚠️ [INPUT] Устройство \"{system_device_name}\" не найдено в PortAudio, пробуем sd.default.device...")

            # ✅ ПРИОРИТЕТ 2: Используем sd.default.device как fallback
            default_setting = sd.default.device
            logger.debug(f"🔍 [INPUT] sd.default.device = {default_setting}")

            input_device_id = None
            if hasattr(default_setting, '__getitem__'):
                try:
                    input_device_id = default_setting[0]  # INPUT устройство (индекс 0)
                    logger.debug(f"🔍 [INPUT] input_device_id = {input_device_id}")
                except IndexError:
                    input_device_id = None
                    logger.warning(f"⚠️ [INPUT] IndexError при получении input device из {default_setting}")

            if input_device_id is not None:
                # Проверяем что устройство действительно INPUT
                try:
                    device_info = sd.query_devices(input_device_id, 'input')
                    if device_info and device_info.get('max_input_channels', 0) > 0:
                        device_name = device_info.get('name', 'Unknown')
                        logger.debug(f"✅ [INPUT] Найдено INPUT устройство через sd.default.device: ID {input_device_id} - \"{device_name}\"")
                        return input_device_id
                    else:
                        logger.warning(f"⚠️ [INPUT] Устройство ID {input_device_id} не является INPUT устройством")
                except Exception as e:
                    logger.warning(f"⚠️ [INPUT] Ошибка проверки устройства ID {input_device_id}: {e}")

            # Fallback: если ничего не сработало, используем старый метод
            logger.debug("🔄 [INPUT] Fallback к поиску по имени (старый метод)...")
            return self._get_system_default_input_index_fallback()

        except Exception as e:
            logger.error(f"❌ [INPUT] Ошибка получения default input: {e}")
            # Fallback к старому методу
            return self._get_system_default_input_index_fallback()

    def _get_system_default_input_index_fallback(self) -> Optional[int]:
        """
        Fallback метод - старый подход через поиск по имени.
        Используется если sd.default.device не работает.
        """
        # Получаем имя системного default устройства
        system_device_name = self._get_system_default_input_name()
        if not system_device_name:
            logger.debug("⚠️ [INPUT] Не удалось получить имя системного устройства")
            return None

        # Ищем ID по имени
        device_id = self._find_device_id_by_name_input(system_device_name)
        if device_id is not None:
            logger.debug(f"✅ [INPUT] Найдено устройство (fallback): \"{system_device_name}\" → ID {device_id}")
            return device_id

        # Не найдено
        logger.warning(f"⚠️ [INPUT] Устройство \"{system_device_name}\" не найдено в кэше PortAudio")
        logger.error(f"❌ [INPUT] macOS использует \"{system_device_name}\", но PortAudio его не видит")
        logger.info(f"💡 [INPUT] РЕШЕНИЕ: Перезапустите приложение для обновления списка устройств")

        # Показываем доступные INPUT устройства для диагностики
        try:
            all_devices = sd.query_devices()
            available_inputs = [
                f"{idx}: {dev.get('name')}"
                for idx, dev in enumerate(all_devices)
                if dev.get('max_input_channels', 0) > 0
            ]
            logger.info(f"📋 [INPUT] Доступные INPUT устройства в PortAudio: {', '.join(available_inputs)}")
        except Exception:
            pass

        return None


    def _select_default_input_device(self, strict: bool = True) -> tuple[Any, Optional[Dict[str, Any]]]:
        """
        Возвращает (device_id, device_info) для системного default входа.
        Если strict=True и default недоступен — автоматически ищет альтернативные устройства.
        Если strict=False — пытается найти первый доступный альтернативный input.
        """
        logger.debug(f"🔍 [SELECT] Начинаем выбор default input устройства (strict={strict})")

        # ✅ ПОДХОД: _get_system_default_input_index() ищет устройство по имени
        # от macOS и при необходимости обновляет кэш PortAudio

        default_input = self._get_system_default_input_index()
        logger.debug(f"🔍 [SELECT] Системный default input ID: {default_input}")

        devices_snapshot: List[Dict[str, Any]] = []
        try:
            devices_snapshot = sd.query_devices()
            logger.debug(f"🔍 [SELECT] Всего устройств в системе: {len(devices_snapshot)}")
        except Exception:
            devices_snapshot = []

        candidates: List[Any] = []
        # Добавляем default_input если он найден
        if default_input is not None:
            candidates.append(default_input)
            logger.debug(f"🔍 [SELECT] Добавлен кандидат (default): ID {default_input}")

        # ✅ FIX: Если strict=True, но default недоступен, автоматически добавляем альтернативы
        # Это позволяет системе переключаться на доступные устройства при отключении AirPods
        should_try_alternatives = not strict or (strict and default_input is not None)
        
        if should_try_alternatives and devices_snapshot:
            sorted_indices = sorted(
                (
                    idx
                    for idx, dev in enumerate(devices_snapshot)
                    if dev.get('max_input_channels', 0) > 0 and idx != default_input
                ),
                key=lambda idx: self._classify_input_device(devices_snapshot[idx].get('name', '')),
            )
            candidates.extend(sorted_indices)
            logger.debug(f"🔍 [SELECT] Добавлены альтернативные кандидаты: {sorted_indices}")

        logger.debug(f"🔍 [SELECT] Всего кандидатов: {len(candidates)} → {candidates}")

        if not candidates:
            if strict:
                raise RuntimeError("Системное входное устройство недоступно")
            return None, None

        # Пробуем все кандидаты по порядку
        for candidate in candidates:
            logger.debug(f"🔍 [SELECT] Проверяем кандидата ID {candidate}...")
            try:
                info = sd.query_devices(candidate, 'input')
                device_name = info.get('name', 'Unknown')
                logger.debug(f"🔍 [SELECT] ID {candidate}: \"{device_name}\"")
            except Exception as e:
                logger.debug(f"⚠️ [SELECT] ID {candidate}: не удалось получить info: {e}")
                info = None
            if not info:
                logger.debug(f"⚠️ [SELECT] ID {candidate}: info пуст, пропускаем")
                continue
            if not self._device_is_available(candidate, info):
                logger.warning(f"⚠️ [SELECT] ID {candidate} (\"{device_name}\"): устройство недоступно, пробуем следующее")
                continue
            self._set_portaudio_default_input(candidate)
            logger.info(f"✅ [SELECT] ВЫБРАН: ID {candidate} - \"{info.get('name')}\"")
            return candidate, info

        # Если дошли сюда - все кандидаты недоступны
        if strict:
            raise RuntimeError("Системное входное устройство недоступно или занято")
        return None, None

    def _set_portaudio_default_input(self, device_id: Any):
        """Устанавливает выбранный input как default внутри PortAudio (без изменения системного default)."""
        try:
            current_default = sd.default.device
            output_part = None
            if hasattr(current_default, '__getitem__'):
                if len(current_default) > 1:
                    output_part = current_default[1]
            elif current_default not in (None, -1):
                output_part = current_default
        except Exception:
            output_part = None
        try:
            sd.default.device = (device_id, output_part)
        except Exception as e:
            logger.debug(f"⚠️ Не удалось обновить портативный default для устройства {device_id}: {e}")

    @staticmethod
    def _is_builtin_device(name: str) -> bool:
        lowered = (name or "").lower()
        return any(keyword in lowered for keyword in ("built-in", "internal microphone", "macbook", "mac mini"))

    @staticmethod
    def _is_remote_device(name: str) -> bool:
        lowered = (name or "").lower()
        return any(keyword in lowered for keyword in ("iphone", "ipad", "ipod", "continuity", "handoff"))

    def _classify_input_device(self, name: str) -> int:
        """Возвращает приоритет устройства: меньше — предпочтительнее."""
        lowered = (name or "").lower()
        if self._is_builtin_device(lowered):
            return 0
        if not self._is_bluetooth_device(lowered) and not self._is_remote_device(lowered):
            return 1
        if self._is_bluetooth_device(lowered):
            return 2
        if self._is_remote_device(lowered):
            return 3
        return 4

    def _build_device_priority(self, primary_device: Any) -> List[Any]:
        """Формирует предпочтительный список устройств для запуска записи."""
        if not self.allow_device_fallback:
            return [primary_device] if primary_device is not None else []

        priority: List[Any] = []
        seen = set()

        def _append(device_id: Any):
            if device_id is None or device_id in seen:
                return
            seen.add(device_id)
            priority.append(device_id)

        _append(primary_device)

        try:
            devices = sd.query_devices()
        except Exception as e:
            logger.debug(f"⚠️ Не удалось получить список устройств для fallback: {e}")
            return priority

        buckets: Dict[int, List[int]] = {}
        for idx, dev in enumerate(devices):
            if dev.get("max_input_channels", 0) <= 0 or idx == primary_device:
                continue
            score = self._classify_input_device(dev.get("name", ""))
            buckets.setdefault(score, []).append(idx)

        for score in sorted(buckets.keys()):
            for idx in buckets[score]:
                _append(idx)

        return priority

    # ========== NAME-BASED DEVICE MANAGEMENT ==========

    def _refresh_device_cache(self):
        """
        Обновляет кэш маппинга device_name → device_id.
        Вызывается при изменении списка устройств.
        """
        import sys
        import threading
        import time
        
        # Логируем информацию о потоке для отслеживания race conditions
        current_thread = threading.current_thread()
        thread_id = current_thread.ident
        thread_name = current_thread.name
        timestamp = time.time()
        
        logger.debug("🔍 [CACHE] === НАЧИНАЕМ ОБНОВЛЕНИЕ КЭША УСТРОЙСТВ ===")
        logger.debug(f"🔍 [CACHE] Thread: {thread_name} (ID: {thread_id}), timestamp: {timestamp}")
        logger.debug(f"🔍 [CACHE] Python executable: {sys.executable}")
        logger.debug(f"🔍 [CACHE] sounddevice version: {sd.__version__}")
        logger.debug(f"🔍 [CACHE] Текущее состояние sd.default.device: {sd.default.device}")
        
        self._device_name_to_id_cache.clear()

        try:
            # ✅ ИСПРАВЛЕНИЕ: НЕ используем sd._terminate() / sd._initialize()!
            # Причина: это уничтожает ВСЕ PortAudio потоки (включая OUTPUT),
            # что вызывает segfault/crash в многопоточной среде.
            #
            # Вместо этого полагаемся на то, что sounddevice.query_devices()
            # получает актуальный список устройств без необходимости реинициализации.
            # Если устройство подключилось после запуска - macOS/PortAudio автоматически
            # обнаружат его при следующем query_devices().

            # ✅ ИСПРАВЛЕНИЕ: Убрали _refresh_default_devices()
            # Причина: Не даёт эффекта, т.к. sd.default.device не обновляется без sd._terminate()
            # Теперь полагаемся на SwitchAudioSource + поиск по имени в sd.query_devices()

            logger.debug("🔍 [CACHE] Получение списка устройств (без reinit)")

            devices = sd.query_devices()
            logger.debug(f"🔍 [CACHE] Получено {len(devices)} устройств от sounddevice")

            # ДЕТАЛЬНОЕ ЛОГИРОВАНИЕ ВСЕХ УСТРОЙСТВ
            for idx, dev in enumerate(devices):
                in_ch = dev.get('max_input_channels', 0)
                out_ch = dev.get('max_output_channels', 0)
                name = dev.get('name', 'Unknown')
                logger.debug(f"🔍 [CACHE] ID {idx}: \"{name}\" | IN={in_ch}, OUT={out_ch}")

        except Exception as e:
            logger.warning(f"⚠️ [CACHE] Не удалось получить список устройств: {e}")
            self._device_cache_valid = False
            return

        input_devices_count = 0
        for idx, dev in enumerate(devices):
            if dev.get('max_input_channels', 0) > 0:
                input_devices_count += 1
                name = dev.get('name')
                if name:
                    # Для уникальности используем name@hostapi
                    host_api = dev.get('hostapi', 0)
                    unique_key = f"{name}@{host_api}"
                    self._device_name_to_id_cache[unique_key] = idx

                    # Также сохраняем просто имя (для простого поиска)
                    # Если есть дубликаты - приоритет у первого найденного
                    if name not in self._device_name_to_id_cache:
                        self._device_name_to_id_cache[name] = idx
                        logger.debug(f"🔍 [CACHE] Добавлено в кэш: \"{name}\" → ID {idx}")

        self._device_cache_valid = True
        logger.debug(
            f"✅ [CACHE] Кэш обновлён: {len(self._device_name_to_id_cache)} записей "
            f"({input_devices_count} входных устройств)"
        )

    def _find_device_id_by_name(self, target_name: str, strict: bool = True) -> Optional[int]:
        """
        Находит индекс устройства по имени.

        Args:
            target_name: Имя устройства для поиска
            strict: Если True - требуется точное совпадение, иначе - частичное

        Returns:
            Индекс устройства или None если не найдено
        """
        if not target_name:
            return None

        # Обновляем кэш если не валиден
        if not self._device_cache_valid:
            self._refresh_device_cache()

        # 1. Поиск в кэше (точное совпадение)
        if target_name in self._device_name_to_id_cache:
            return self._device_name_to_id_cache[target_name]

        # 2. Если strict=False, ищем частичное совпадение
        if not strict:
            target_lower = target_name.lower()
            for cached_name, device_id in self._device_name_to_id_cache.items():
                # Пропускаем ключи с @hostapi
                if '@' in cached_name:
                    continue
                if target_lower in cached_name.lower():
                    logger.debug(f"🔍 Частичное совпадение: '{target_name}' → '{cached_name}' (ID: {device_id})")
                    return device_id

        # 3. Не найдено - обновляем кэш и пробуем ещё раз
        self._refresh_device_cache()

        if target_name in self._device_name_to_id_cache:
            return self._device_name_to_id_cache[target_name]

        return None

    def _get_device_name_by_id(self, device_id: int) -> Optional[str]:
        """
        Получает имя устройства по его индексу.

        Args:
            device_id: Индекс устройства

        Returns:
            Имя устройства или None
        """
        try:
            device_info = sd.query_devices(device_id, 'input')
            device_name = device_info.get('name')
            logger.debug(f"🔍 [LOOKUP] ID {device_id} → \"{device_name}\"")
            return device_name
        except Exception as e:
            logger.warning(f"⚠️ [LOOKUP] Не удалось получить имя устройства {device_id}: {e}")
            return None

    def _invalidate_device_cache(self):
        """Помечает кэш устройств как невалидный (нужно обновить)."""
        logger.debug("🔍 [CACHE] Кэш устройств помечен как невалидный")
        self._device_cache_valid = False

    # ========== END NAME-BASED DEVICE MANAGEMENT ==========

    def _audio_callback(self, indata, frames, time, status):
        """Callback для записи аудио с диагностикой пустых чанков"""
        try:
            # ✅ FIX: Немедленно выходим если запись остановлена
            # ✅ FIX: Проверяем stop_event и is_listening атомарно (локальные копии)
            stop_requested = self.stop_event.is_set()
            listening_active = self.is_listening
            
            if stop_requested or not listening_active:
                # ✅ FIX: Немедленно останавливаем поток при установке stop_event
                with self._stream_lock:
                    if self._current_stream and self._current_stream.active:
                        try:
                            self._current_stream.stop()
                            self._current_stream.close()
                            self._current_stream = None
                            logger.debug("🛑 Аудио поток принудительно остановлен в callback")
                        except Exception as e:
                            logger.debug(f"⚠️ Ошибка принудительной остановки потока в callback: {e}")
                return
            
            if status:
                logger.warning(f"⚠️ AUDIO callback status: {status}, frames={frames}")

            # ✅ FIX: Используем локальную копию для проверки (уже получена выше)
            if listening_active:
                # Проверяем уровень сигнала (диагностика CoreAudio overload)
                peak = float(np.max(np.abs(indata)))
                signal_detected = peak >= self._signal_threshold

                if not signal_detected and len(self.audio_data) < 10:
                    mean_abs = float(np.mean(np.abs(indata)))
                    logger.debug(
                        "🔇 AUDIO chunk looks silent: peak=%.8f, mean_abs=%.8f, dtype=%s",
                        peak,
                        mean_abs,
                        indata.dtype,
                    )

                # Интеграция с RecoveryManager
                if self.recovery_enabled and self.recovery_manager:
                    recovery_step = self.recovery_manager.on_chunk_received(indata, peak, float(np.mean(np.abs(indata))))
                    if recovery_step:
                        # Запускаем восстановление асинхронно из другого потока
                        try:
                            # Получаем event loop из главного потока
                            if hasattr(self, '_main_loop') and self._main_loop and not self._main_loop.is_closed():
                                asyncio.run_coroutine_threadsafe(
                                    self._execute_recovery(recovery_step), 
                                    self._main_loop
                                )
                            else:
                                logger.warning("⚠️ Event loop недоступен для recovery")
                        except Exception as e:
                            logger.error(f"❌ Ошибка запуска recovery: {e}")
                
                if not signal_detected:  # Пустой чанк
                    self.empty_chunk_counter += 1
                    if self.empty_chunk_counter >= 10:  # Порог для WARNING
                        if self.empty_chunk_counter == 10 or self.empty_chunk_counter % 50 == 0:  # Логируем на 10, потом каждые 50
                            logger.warning(
                                f"⚠️ {self.empty_chunk_counter} пустых чанков подряд - возможна перегрузка CoreAudio"
                            )
                else:
                    # Сигнал есть - сбрасываем счётчик
                    if self.empty_chunk_counter >= 10:
                        logger.info(f"✅ Сигнал восстановлен после {self.empty_chunk_counter} пустых чанков")
                    elif self.empty_chunk_counter > 0:
                        logger.debug(f"✅ Сигнал восстановлен после {self.empty_chunk_counter} пустых чанков")
                    self.empty_chunk_counter = 0

                # DEBUG: каждые N чанков с сигналом логируем состояние
                if signal_detected and len(self.audio_data) % 20 == 0:  # Каждые 20 чанков
                    logger.debug(f"🔊 AUDIO callback: chunks={len(self.audio_data)}, peak={peak:.4f}, frames={frames}")

                with self.audio_lock:
                    self.audio_data.append(indata.copy())
                    if len(self.audio_data) == 1 and not self.first_chunk_received:
                        self.first_chunk_received = True
                        logger.info(
                            "🔊 Первый чанк получен: frames=%s, dtype=%s, peak=%.6f (signal=%s)",
                            frames,
                            indata.dtype,
                            peak,
                            signal_detected,
                        )

        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}")
            import traceback
            logger.error(f"❌ Traceback: {traceback.format_exc()}")
    
    async def _execute_recovery(self, recovery_step):
        """Выполнение шага восстановления аудио."""
        if not self.recovery_enabled or not self.recovery_manager:
            return
            
        logger.info(f"🔧 Выполняем восстановление: {recovery_step.value}")
        
        # ✅ РЕФАКТОРИНГ: Создаем callback для управления потоком через AudioStreamManager
        async def stream_callback(**kwargs):
            if 'stop' in kwargs and kwargs['stop']:
                # Останавливаем поток через AudioStreamManager
                with self._stream_lock:
                    old_stream = self._current_stream
                    if old_stream:
                        is_bluetooth = self._is_bluetooth_device(self.input_device_name or '')
                        await self._stream_manager.close_stream(old_stream, is_bluetooth=is_bluetooth)
                        self._current_stream = None
            elif 'start' in kwargs and kwargs['start']:
                # Запускаем поток (если он существует)
                with self._stream_lock:
                    if self._current_stream:
                        self._current_stream.start()
                    else:
                        logger.warning("⚠️ [RECOVERY] Попытка запустить несуществующий поток")
            elif 'recreate' in kwargs and kwargs['recreate']:
                # Пересоздаем поток с новой конфигурацией через AudioStreamManager
                config = kwargs.get('config')
                if config:
                    await self._recreate_stream_with_config(config)
            elif 'device_id' in kwargs:
                # Переключаем устройство через AudioStreamManager
                await self._switch_device(kwargs['device_id'])
        
        # Выполняем восстановление
        success = await self.recovery_manager.execute_recovery(recovery_step, stream_callback)
        
        if success:
            logger.info(f"✅ Восстановление {recovery_step.value} выполнено успешно")
        else:
            logger.warning(f"⚠️ Восстановление {recovery_step.value} не удалось")
    
    async def _recreate_stream_with_config(self, config):
        """
        ✅ РЕФАКТОРИНГ: Пересоздание потока с новой конфигурацией через AudioStreamManager.
        
        Args:
            config: Конфигурация для пересоздания (может быть dict или StreamConfig)
        """
        try:
            logger.info(f"🔄 [RECOVERY] Пересоздаем поток с конфигурацией: {config}")
            
            # Преобразуем config в StreamConfig если нужно
            if isinstance(config, dict):
                # Если config - это dict, создаем StreamConfig
                stream_config = StreamConfig(
                    device_id=config.get('device_id') or self.input_device_id,
                    device_name=config.get('device_name') or self.input_device_name,
                    samplerate=config.get('samplerate', self.actual_input_rate),
                    channels=config.get('channels', self.actual_input_channels),
                    dtype=config.get('dtype', 'float32'),
                    blocksize=config.get('blocksize', self.config.chunk_size),
                    callback=self._audio_callback,
                    is_bluetooth=config.get('is_bluetooth', False)
                )
            elif isinstance(config, StreamConfig):
                stream_config = config
            else:
                # Fallback: создаем StreamConfig из текущих параметров
                device_name = self.input_device_name or 'Unknown Device'
                device_id = self.input_device_id
                is_bluetooth = self._is_bluetooth_device(device_name)
                stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
            
            # Получаем текущий поток
            with self._stream_lock:
                old_stream = self._current_stream
            
            # Переключаем устройство через AudioStreamManager
            if old_stream is None:
                result = await self._stream_manager.create_stream(stream_config)
            else:
                result = await self._stream_manager.switch_device(old_stream, stream_config)
            
            if result.success and result.stream:
                # Обновляем ссылку на поток и параметры
                with self._stream_lock:
                    self._current_stream = result.stream
                
                self.actual_input_rate = stream_config.samplerate
                self.actual_input_channels = stream_config.channels
                
                logger.info(f"✅ [RECOVERY] Поток пересоздан успешно (attempt: {result.attempt}, duration: {result.duration_ms:.1f}ms)")
            else:
                logger.error(
                    f"❌ [RECOVERY] Не удалось пересоздать поток: {result.error_message} "
                    f"(error_code={result.error_code})"
                )
                raise RuntimeError(f"Failed to recreate stream: {result.error_message}")
            
        except Exception as e:
            logger.error(f"❌ [RECOVERY] Ошибка при пересоздании потока: {e}", exc_info=True)
            raise
    
    async def _switch_device(self, device_id):
        """
        ✅ РЕФАКТОРИНГ: Переключение на другое устройство через AudioStreamManager.
        
        Args:
            device_id: PortAudio ID нового устройства
        """
        try:
            logger.info(f"🔄 [RECOVERY] Переключаемся на устройство {device_id}")
            
            # Получаем информацию об устройстве
            try:
                device_info = sd.query_devices(device_id, 'input')
                device_name = device_info.get('name', 'Unknown Device')
            except Exception as e:
                logger.warning(f"⚠️ [RECOVERY] Не удалось получить информацию об устройстве {device_id}: {e}")
                device_name = 'Unknown Device'
            
            is_bluetooth = self._is_bluetooth_device(device_name)
            
            # Создаем StreamConfig для нового устройства
            stream_config = self._build_stream_config_for_device(device_name, device_id, is_bluetooth)
            
            # Получаем текущий поток
            with self._stream_lock:
                old_stream = self._current_stream
            
            # Переключаем устройство через AudioStreamManager
            if old_stream is None:
                result = await self._stream_manager.create_stream(stream_config)
            else:
                result = await self._stream_manager.switch_device(old_stream, stream_config)
            
            if result.success and result.stream:
                # Обновляем ссылку на поток и параметры устройства
                with self._stream_lock:
                    self._current_stream = result.stream
                
                self.input_device_name = device_name
                self.input_device_id = device_id
                self.actual_input_rate = stream_config.samplerate
                self.actual_input_channels = stream_config.channels
                
                logger.info(
                    f"✅ [RECOVERY] Успешно переключились на устройство \"{device_name}\" "
                    f"(ID={device_id}, attempt: {result.attempt}, duration: {result.duration_ms:.1f}ms)"
                )
            else:
                logger.error(
                    f"❌ [RECOVERY] Не удалось переключить устройство: {result.error_message} "
                    f"(error_code={result.error_code})"
                )
                raise RuntimeError(f"Failed to switch device: {result.error_message}")
            
        except Exception as e:
            logger.error(f"❌ [RECOVERY] Ошибка при переключении устройства: {e}", exc_info=True)
            raise
            
    async def _recognize_audio(self) -> RecognitionResult:
        """Распознает записанное аудио"""
        try:
            if not self.audio_data:
                logger.warning("⚠️ Нет аудио данных для распознавания")
                return RecognitionResult(text="", error="No audio data")
                
            # Объединяем аудио чанки
            with self.audio_lock:
                audio_data = np.concatenate(self.audio_data, axis=0).astype(np.float32, copy=False)

            if audio_data.size == 0:
                logger.warning("⚠️ Нет аудио данных после конкатенации")
                return RecognitionResult(text="", error="No audio data")

            sample_count = audio_data.shape[0]
            duration_sec = sample_count / float(self.actual_input_rate or self.config.sample_rate)
            peak = float(np.max(np.abs(audio_data)))
            rms = float(np.sqrt(np.mean(audio_data.astype(np.float64) ** 2)))
            rms_db = float(20 * np.log10(rms)) if rms > 0 else float("-inf")

            self.last_audio_stats = {
                "chunks": len(self.audio_data),
                "samples": sample_count,
                "duration_sec": duration_sec,
                "peak": peak,
                "rms": rms,
                "rms_db": rms_db,
                "raw_rate": self.actual_input_rate,
                "raw_channels": self.actual_input_channels,
            }

            logger.info(
                "📈 AUDIO: Статистика перед распознаванием: chunks=%s, samples=%s, duration=%.2fs, peak=%.4f, rms=%.4f, rms_db=%.1fdB, actual_rate=%s, target_rate=%s, channels=%s",
                len(self.audio_data),
                sample_count,
                duration_sec,
                peak,
                rms,
                rms_db,
                self.actual_input_rate,
                self.config.sample_rate,
                self.actual_input_channels,
            )

            # Конвертируем в формат для распознавания
            target_channels = max(1, self.config.channels)
            if audio_data.ndim > 1:
                raw_channels = audio_data.shape[1]
            else:
                raw_channels = 1

            if target_channels == 1 and raw_channels > 1:
                audio_data = np.mean(audio_data, axis=1, dtype=np.float32)
            elif target_channels > 1:
                if raw_channels == 1:
                    audio_data = np.repeat(audio_data[:, np.newaxis], target_channels, axis=1)
                elif raw_channels != target_channels:
                    # Приводим к нужному количеству каналов через усреднение/обрезание
                    if raw_channels > target_channels:
                        audio_data = audio_data[:, :target_channels]
                    else:
                        audio_data = np.repeat(audio_data, target_channels // raw_channels, axis=1)

            # Если запись велась не на той частоте, приводим к целевой
            effective_rate = self.actual_input_rate
            try:
                if self.actual_input_rate != self.config.sample_rate:
                    from modules.voice_recognition.utils.audio_utils import resample_audio
                    logger.debug(
                        "🔄 Выполняем ресемплинг: %s → %s",
                        self.actual_input_rate,
                        self.config.sample_rate,
                    )
                    audio_data = resample_audio(audio_data, self.actual_input_rate, self.config.sample_rate)
                    effective_rate = self.config.sample_rate
            except Exception as re:
                logger.debug(f"Resample skipped: {re}")

            # Нормализуем аудио в диапазон [-1, 1]
            audio_float = np.clip(audio_data, -1.0, 1.0).astype(np.float32, copy=False)

            # Создаем AudioData для распознавания
            audio_bytes = (audio_float * 32767.0).astype(np.int16).tobytes()
            audio_data_obj = sr.AudioData(audio_bytes, effective_rate, 2)

            # Распознаем речь
            start_time = time.time()
            await self._notify_event(RecognitionEventType.RECOGNITION_START)
            
            try:
                text = await self._recognize_with_engine(audio_data_obj)
                duration = time.time() - start_time
                
                result = RecognitionResult(
                    text=text,
                    confidence=None,  # SpeechRecognition не всегда предоставляет confidence
                    language=self.config.language,
                    duration=duration,
                    timestamp=time.time()
                )
                
                await self._notify_event(RecognitionEventType.RECOGNITION_COMPLETE, result=result)
                logger.info(
                    "✅ Распознавание завершено: text_length=%s, duration=%.2fs, language=%s",
                    len(text),
                    duration,
                    self.config.language,
                )
                return result
                
            except sr.UnknownValueError:
                logger.warning(
                    "⚠️ Google Speech Recognition не распознал аудио (duration=%.2fs, rms=%.1f, peak=%.0f)",
                    duration_sec,
                    rms,
                    peak,
                )
                return RecognitionResult(text="", error="Speech not recognized")
            except sr.RequestError as e:
                logger.error(
                    "❌ Ошибка сервиса распознавания (language=%s, duration=%.2fs): %s",
                    self.config.language,
                    duration_sec,
                    e,
                )
                return RecognitionResult(text="", error=str(e))
                
        except Exception as e:
            logger.error(f"❌ Ошибка распознавания аудио: {e}", exc_info=True)
            return RecognitionResult(text="", error=str(e))
            
    async def _recognize_with_engine(self, audio_data: sr.AudioData) -> str:
        """Распознает аудио с помощью Google Speech Recognition"""
        try:
            return self.recognizer.recognize_google(audio_data, language=self.config.language)
                
        except Exception as e:
            logger.error(f"❌ Ошибка распознавания с Google Speech Recognition: {e}")
            raise
            
    def _update_metrics(self, result: RecognitionResult):
        """Обновляет метрики распознавания"""
        self.metrics.total_recognitions += 1
        
        if result.text and not result.error:
            self.metrics.successful_recognitions += 1
            self.metrics.recognitions_by_language[result.language] = (
                self.metrics.recognitions_by_language.get(result.language, 0) + 1
            )
            
            if result.confidence:
                # Обновляем среднюю уверенность
                if self.metrics.successful_recognitions > 0:
                    self.metrics.average_confidence = (
                        (self.metrics.average_confidence * (self.metrics.successful_recognitions - 1) + result.confidence) 
                        / self.metrics.successful_recognitions
                    )
        else:
            self.metrics.failed_recognitions += 1
            
                
    def register_callback(self, state: RecognitionState, callback: Callable):
        """Регистрирует callback для состояния"""
        self.state_callbacks[state] = callback
        logger.debug(f"📝 Зарегистрирован callback для состояния {state.value}")
        
    def register_event_callback(self, event_type: RecognitionEventType, callback: Callable):
        """Регистрирует callback для события"""
        self.event_callbacks[event_type] = callback
        logger.debug(f"📝 Зарегистрирован callback для события {event_type.value}")
        
    async def _notify_state_change(self, state: RecognitionState, **kwargs):
        """Уведомляет об изменении состояния"""
        try:
            callback = self.state_callbacks.get(state)
            if callback:
                from .types import RecognitionEvent
                event = RecognitionEvent(
                    event_type=RecognitionEventType.LISTENING_START,  # Базовое событие
                    state=state,
                    timestamp=time.time(),
                    **kwargs
                )
                await callback(event)
        except Exception as e:
            logger.error(f"❌ Ошибка уведомления о смене состояния: {e}")
            
    async def _notify_event(self, event_type: RecognitionEventType, **kwargs):
        """Уведомляет о событии"""
        try:
            callback = self.event_callbacks.get(event_type)
            if callback:
                from .types import RecognitionEvent
                event = RecognitionEvent(
                    event_type=event_type,
                    state=self.state,
                    timestamp=time.time(),
                    **kwargs
                )
                await callback(event)
        except Exception as e:
            logger.error(f"❌ Ошибка уведомления о событии: {e}")
            
    def get_status(self) -> Dict[str, Any]:
        """Возвращает статус распознавания речи"""
        return {
            "state": self.state.value,
            "is_listening": self.is_listening,
            "audio_data_chunks": len(self.audio_data),
            "config": {
                "language": self.config.language,
                "sample_rate": self.config.sample_rate,
                "chunk_size": self.config.chunk_size,
                "channels": self.config.channels,
            },
            "actual_device": {
                "id": self.input_device_id,
                "name": self.input_device_info.get("name"),
                "default_samplerate": self.input_device_info.get("default_samplerate"),
                "default_low_latency": self.input_device_info.get("default_low_input_latency"),
                "default_high_latency": self.input_device_info.get("default_high_input_latency"),
                "max_input_channels": self.input_device_info.get("max_input_channels"),
                "max_output_channels": self.input_device_info.get("max_output_channels"),
                "hostapi": self.input_device_info.get("hostapi"),
                "effective_rate": self.actual_input_rate,
                "effective_channels": self.actual_input_channels,
            },
            "output_device": {
                "id": self.output_device_id,
                "name": self.output_device_info.get("name"),
                "default_samplerate": self.output_device_info.get("default_samplerate"),
                "default_low_latency": self.output_device_info.get("default_low_output_latency"),
                "default_high_latency": self.output_device_info.get("default_high_output_latency"),
                "max_input_channels": self.output_device_info.get("max_input_channels"),
                "max_output_channels": self.output_device_info.get("max_output_channels"),
                "hostapi": self.output_device_info.get("hostapi"),
            },
            "signal_last_recording": self.last_audio_stats,
            "host_apis": self.host_apis,
            "metrics": {
                "total_recognitions": self.metrics.total_recognitions,
                "successful_recognitions": self.metrics.successful_recognitions,
                "failed_recognitions": self.metrics.failed_recognitions,
                "success_rate": (
                    self.metrics.successful_recognitions / max(self.metrics.total_recognitions, 1) * 100
                ),
                "average_confidence": self.metrics.average_confidence,
                "average_duration": self.metrics.average_duration,
            },
            "callbacks_registered": len(self.state_callbacks) + len(self.event_callbacks)
        }
        
    def get_metrics(self) -> RecognitionMetrics:
        """Возвращает метрики распознавания"""
        return self.metrics
