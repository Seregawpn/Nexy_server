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
    RecognitionEventType, RecognitionMetrics
)
from .audio_device_monitor import AudioDeviceMonitor
from .audio_recovery_manager import AudioRecoveryManager, preflight_check

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
        
        # Audio Recovery Manager
        self.recovery_manager: Optional[AudioRecoveryManager] = None
        self.recovery_enabled = bool(getattr(self.config, "enable_audio_recovery", True))
        self._current_stream: Optional[sd.InputStream] = None
        self._device_priority: List[Any] = []

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

        # Монитор устройств для стабилизации
        self.device_monitor = AudioDeviceMonitor(check_interval=0.5)
        self.device_monitor.set_device_change_callback(self._on_device_changed)
        self.last_device_change_time = 0.0
        self.stabilization_delay = 0.3  # 300мс задержка стабилизации

    def set_event_loop(self, loop: asyncio.AbstractEventLoop):
        """Устанавливает event loop для асинхронных операций из audio callback."""
        self._main_loop = loop
        logger.debug(f"🔧 Event loop установлен в SpeechRecognizer: {loop}")

        # Retry параметры для мягкого перезапуска потока (адаптивные для BT-устройств)
        self.max_stream_start_retries = 5
        self.retry_delay = 0.8  # 800мс между попытками (проводные устройства)
        self.first_chunk_timeout = 2.0  # 2s ожидание первого чанка по умолчанию
        self.first_chunk_timeout_bt = 3.5  # 3.5s для BT-маршрутов
        self.retry_delay_bt = 1.2  # BT-устройства стабилизируются дольше

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
            if hasattr(self, 'device_monitor') and self.device_monitor.is_monitoring():
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
    
    def _on_device_changed(self, old_device_id: Any, new_device_id: Any):
        """
        Callback для смены аудио устройства.
        КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Сравниваем устройства по NAME, а не по ID!
        """
        self.last_device_change_time = time.time()

        # Получаем ИМЕНА устройств (не ID!)
        old_device_name = self.input_device_name  # Текущее имя устройства
        new_device_name = self._get_device_name_by_id(new_device_id)  # Новое имя

        logger.info(
            f"🔄 [MONITOR] AudioDeviceMonitor callback: "
            f"ID изменился ({old_device_id} → {new_device_id}), "
            f"проверяем имена: \"{old_device_name}\" → \"{new_device_name}\""
        )

        logger.debug(
            f"🔍 [MONITOR] Текущее состояние: "
            f"state={self.state.value}, "
            f"is_listening={self.is_listening}"
        )

        # Инвалидируем кэш при любом изменении устройств
        self._invalidate_device_cache()

        # КРИТИЧНО: Сравниваем по ИМЕНАМ, а не по ID!
        if new_device_name != old_device_name:
            # Реальная смена устройства (изменилось имя)
            logger.info(
                f"✅ [MONITOR] РЕАЛЬНАЯ смена устройства: \"{old_device_name}\" → \"{new_device_name}\" "
                f"(ID: {old_device_id} → {new_device_id})"
            )

            logger.debug(
                f"🔍 [MONITOR] NAME сравнение: \"{new_device_name}\" != \"{old_device_name}\" = True"
            )

            # Если сейчас идет запись - останавливаем
            if self.state == RecognitionState.LISTENING:
                logger.debug(f"🔍 [MONITOR] state=LISTENING - будем останавливать запись")
                logger.warning(
                    f"⚠️ Устройство изменилось во время записи - ОСТАНАВЛИВАЕМ запись. "
                    f"Пользователь должен повторно нажать SPACE для записи на новом устройстве."
                )
                self._graceful_stop_listening(reason="device_changed")
                # ❌ НЕ перезапускаем автоматически!
                # Пользователь должен сам решить, когда начать запись на новом устройстве
            else:
                # Если запись НЕ идет, просто логируем информацию
                logger.debug(f"🔍 [MONITOR] state!= LISTENING - запись не идет, просто логируем")
                logger.info(f"ℹ️ Системное устройство изменилось на: \"{new_device_name}\" (ID: {new_device_id})")
        else:
            # ID изменился, но NAME остался тот же
            # Это может быть при переподключении других устройств
            logger.debug(
                f"🔍 [MONITOR] NAME сравнение: \"{new_device_name}\" == \"{old_device_name}\" = True (НЕ реальная смена)"
            )
            logger.debug(
                f"ℹ️ [MONITOR] ID изменился ({old_device_id} → {new_device_id}), "
                f"но устройство то же: \"{new_device_name}\" - продолжаем без изменений"
            )
            # Ничего не делаем - start_listening() сам получит актуальный ID при следующем запуске

    def _graceful_stop_listening(self, reason: str):
        """Безопасно останавливает текущий поток прослушивания (синхронно)."""
        try:
            self.stop_event.set()
        except Exception:
            pass

        thread = self.listen_thread
        if thread and thread.is_alive():
            thread.join(timeout=2.0)
            if thread.is_alive():
                logger.warning("⚠️ Поток прослушивания не завершился за 2с (reason=%s)", reason)
        self.listen_thread = None

        with self.audio_lock:
            self.audio_data = []

        self.is_listening = False
        self.first_chunk_received = False
        self.empty_chunk_counter = 0
        self.state = RecognitionState.IDLE

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
                if self.state != RecognitionState.IDLE:
                    logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self.state.value}")
                    return False
                if self._initializing:
                    logger.debug("🔁 Запуск прослушивания уже выполняется, пропускаем повторный вызов")
                    return False

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

                # Запускаем мониторинг устройств если еще не запущен
                if not self.device_monitor.is_monitoring():
                    self.device_monitor.start_monitoring()
                    logger.debug("🚀 Мониторинг устройств запущен")

                device_id = self._prepare_input_device()
                if device_id is None:
                    logger.error("❌ Входное устройство недоступно, запись не запущена")
                    self._device_priority = []
                    self._schedule_cooldown(0.5)
                    return False
                
                # Preflight проверка устройства
                device_name = self.input_device_info.get('name', 'Unknown Device') if hasattr(self, 'input_device_info') else 'Unknown Device'
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

                logger.info("🎤 Прослушивание микрофона начато")
                return True

            except Exception as e:
                logger.warning(f"⚠️ Ошибка начала прослушивания (продолжаем работу): {e}")
                # НЕ устанавливаем ERROR - возвращаемся в IDLE для повторных попыток
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
            if self.state != RecognitionState.LISTENING:
                logger.warning(f"⚠️ Невозможно остановить прослушивание в состоянии {self.state.value}")
                return RecognitionResult(text="", error="Not listening")
                
            self.state = RecognitionState.PROCESSING
            self.is_listening = False
            self.stop_event.set()
            
            # Останавливаем мониторинг устройств
            if self.device_monitor.is_monitoring():
                self.device_monitor.stop_monitoring()
                logger.debug("🛑 Мониторинг устройств остановлен")
            
            # Уведомляем об остановке прослушивания
            await self._notify_event(RecognitionEventType.LISTENING_STOP)
            await self._notify_state_change(RecognitionState.PROCESSING)
            
            # Ждем завершения потока прослушивания
            if self.listen_thread and self.listen_thread.is_alive():
                logger.debug("⏳ Ожидаем завершение потока записи...")
                self.listen_thread.join(timeout=5.0)
            
            # Распознаем речь
            logger.debug(
                "🎧 Завершаем запись: chunks=%s, thread_alive=%s",
                len(self.audio_data),
                self.listen_thread.is_alive() if self.listen_thread else False,
            )
            result = await self._recognize_audio()
            
            # Обновляем метрики
            self._update_metrics(result)
            
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

            device_id, device_info = self._select_default_input_device(strict=True)
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

                samplerate = device_info.get('default_samplerate') or self.config.sample_rate
                channels_available = int(device_info.get('max_input_channels') or 1)
                channels_target = max(1, self.config.channels)
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

                        logger.info(
                            "🔊 AUDIO: Создание потока: device_id=%s (%s), rate=%.1fHz, channels=%s, blocksize=%s, latency=high",
                            device_id,
                            device_info.get('name'),
                            self.actual_input_rate,
                            self.actual_input_channels,
                            effective_blocksize,
                        )

                        stream = sd.InputStream(
                            device=device_id,
                            samplerate=self.actual_input_rate,
                            channels=self.actual_input_channels,
                            dtype='float32',
                            blocksize=effective_blocksize,
                            # latency убран - пусть PortAudio подберет сам
                            callback=self._audio_callback,
                        )

                        # Сохраняем ссылку на поток для recovery
                        self._current_stream = stream
                        
                        stream.start()
                        logger.debug(f"🔄 Попытка {attempt + 1}/{self.max_stream_start_retries}: поток стартовал")

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
                        logger.warning(f"⚠️ Попытка {attempt + 1}/{self.max_stream_start_retries}: {e}")
                        if stream:
                            try:
                                stream.stop()
                                stream.close()
                            except Exception:
                                pass
                            stream = None

                        if attempt < self.max_stream_start_retries - 1 and not self.stop_event.is_set():
                            time.sleep(retry_delay)
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

            # Поток работает - ждём завершения
            with stream:
                while self.is_listening and not self.stop_event.is_set():
                    time.sleep(0.1)

            duration = time.time() - self.listen_start_time if self.listen_start_time else 0
            logger.debug("🛑 Поток записи остановлен, длительность=%.2fs", duration)

        except Exception as e:
            logger.error(f"❌ Ошибка прослушивания микрофона: {e}")
            self.state = RecognitionState.ERROR
            self._schedule_cooldown(0.6)
        finally:
            # Закрываем поток если он всё ещё открыт
            if stream:
                try:
                    stream.stop()
                    stream.close()
                except Exception:
                    pass

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
        
        ✅ НОВЫЙ ПОДХОД (как в OUTPUT):
        Использует sd.default.device для получения актуального устройства,
        вместо поиска по имени в кэшированном списке.
        
        Это решает проблему с AirPods - sd.default.device обновляется
        автоматически при смене устройства в macOS.
        """
        try:
            # ✅ ИСПОЛЬЗУЕМ sd.default.device как в OUTPUT
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
                        logger.debug(f"✅ [INPUT] Найдено INPUT устройство: ID {input_device_id} - \"{device_info.get('name')}\"")
                        return input_device_id
                    else:
                        logger.warning(f"⚠️ [INPUT] Устройство ID {input_device_id} не является INPUT устройством")
                except Exception as e:
                    logger.warning(f"⚠️ [INPUT] Ошибка проверки устройства ID {input_device_id}: {e}")

            # Fallback: если sd.default.device не работает, используем старый метод
            logger.debug("🔄 [INPUT] Fallback к поиску по имени...")
            return self._get_system_default_input_index_fallback()

        except Exception as e:
            logger.error(f"❌ [INPUT] Ошибка получения default input через sd.default.device: {e}")
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
        Если strict=True и default недоступен — выбрасывает RuntimeError.
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

        if not strict and devices_snapshot:
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

        if strict and not candidates:
            raise RuntimeError("Системное входное устройство недоступно")

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
                logger.debug(f"⚠️ [SELECT] ID {candidate}: устройство недоступно")
                continue
            self._set_portaudio_default_input(candidate)
            logger.debug(f"✅ [SELECT] ВЫБРАН: ID {candidate} - \"{info.get('name')}\"")
            return candidate, info

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
            if status:
                logger.warning(f"⚠️ AUDIO callback status: {status}, frames={frames}")

            if self.is_listening:
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
        
        # Создаем callback для управления потоком
        async def stream_callback(**kwargs):
            if 'stop' in kwargs and kwargs['stop']:
                # Останавливаем поток
                if hasattr(self, '_current_stream') and self._current_stream:
                    self._current_stream.stop()
            elif 'start' in kwargs and kwargs['start']:
                # Запускаем поток
                if hasattr(self, '_current_stream') and self._current_stream:
                    self._current_stream.start()
            elif 'recreate' in kwargs and kwargs['recreate']:
                # Пересоздаем поток с новой конфигурацией
                config = kwargs.get('config')
                if config:
                    await self._recreate_stream_with_config(config)
            elif 'device_id' in kwargs:
                # Переключаем устройство
                await self._switch_device(kwargs['device_id'])
        
        # Выполняем восстановление
        success = await self.recovery_manager.execute_recovery(recovery_step, stream_callback)
        
        if success:
            logger.info(f"✅ Восстановление {recovery_step.value} выполнено успешно")
        else:
            logger.warning(f"⚠️ Восстановление {recovery_step.value} не удалось")
    
    async def _recreate_stream_with_config(self, config):
        """Пересоздание потока с новой конфигурацией."""
        try:
            logger.info(f"🔄 Пересоздаем поток с конфигурацией: {config}")
            
            # Останавливаем текущий поток
            if hasattr(self, '_current_stream') and self._current_stream:
                self._current_stream.stop()
                self._current_stream.close()
            
            # Обновляем параметры
            self.actual_input_rate = config.samplerate
            # blocksize и dtype можно добавить в конфигурацию позже
            
            # Создаем новый поток
            self._current_stream = sd.InputStream(
                device=self.input_device_id,
                samplerate=self.actual_input_rate,
                channels=self.actual_input_channels,
                dtype=config.dtype,
                blocksize=config.blocksize,
                callback=self._audio_callback,
            )
            
            self._current_stream.start()
            logger.info(f"✅ Поток пересоздан с {config}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка при пересоздании потока: {e}")
    
    async def _switch_device(self, device_id):
        """Переключение на другое устройство."""
        try:
            logger.info(f"🔄 Переключаемся на устройство {device_id}")
            
            # Останавливаем текущий поток
            if hasattr(self, '_current_stream') and self._current_stream:
                self._current_stream.stop()
                self._current_stream.close()
            
            # Создаем поток с новым устройством
            self._current_stream = sd.InputStream(
                device=device_id,
                samplerate=self.actual_input_rate,
                channels=self.actual_input_channels,
                dtype='float32',
                blocksize=1024,
                callback=self._audio_callback,
            )
            
            self._current_stream.start()
            logger.info(f"✅ Переключились на устройство {device_id}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка при переключении устройства: {e}")
            
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
