"""
Основной класс распознавания речи с использованием SpeechRecognition
"""

import asyncio
import logging
import time
import threading
from typing import Callable, Dict, Any, List
import sounddevice as sd
import numpy as np
import speech_recognition as sr

from .types import (
    RecognitionConfig, RecognitionResult, RecognitionState, 
    RecognitionEventType, RecognitionMetrics
)
from .audio_device_monitor import AudioDeviceMonitor

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
        
        # Callbacks
        self.state_callbacks: Dict[RecognitionState, Callable] = {}
        self.event_callbacks: Dict[RecognitionEventType, Callable] = {}
        
        # Метрики
        self.metrics = RecognitionMetrics()

        # Параметры входного устройства - используем системные дефолты
        self.actual_input_rate: int = self.config.sample_rate
        self.actual_input_channels: int = self.config.channels
        self.input_device_info: Dict[str, Any] = {}
        self.input_device_id: Any = None
        self.output_device_info: Dict[str, Any] = {}
        self.output_device_id: Any = None
        self.host_apis: List[Dict[str, Any]] = []
        self.prepared_device_id: Any = None
        self.last_audio_stats: Dict[str, Any] = {}
        self._async_loop: Optional[asyncio.AbstractEventLoop] = None
        self._restart_task: Optional[Any] = None

        # Монитор устройств для стабилизации
        self.device_monitor = AudioDeviceMonitor(check_interval=0.5)
        self.device_monitor.set_device_change_callback(self._on_device_changed)
        self.last_device_change_time = 0.0
        self.stabilization_delay = 0.3  # 300мс задержка стабилизации

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
    
    def _on_device_changed(self, old_device: Any, new_device: Any):
        """Callback для смены аудио устройства"""
        self.last_device_change_time = time.time()
        logger.info(f"🔄 Обнаружена смена аудио устройства: {old_device} -> {new_device}")
        
        should_restart = self.state == RecognitionState.LISTENING
        if should_restart:
            logger.info("⏳ Устройство изменилось во время прослушивания - выполняем мягкую перезагрузку потока")
            self._graceful_stop_listening(reason="device_changed")
            self._schedule_listening_restart(self.stabilization_delay)

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
        self.prepared_device_id = None
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
        try:
            if self.state != RecognitionState.IDLE:
                logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self.state.value}")
                return False

            self._async_loop = asyncio.get_running_loop()
            if self._restart_task and not self._restart_task.done():
                self._restart_task.cancel()
                self._restart_task = None

            # Проверяем, не было ли недавней смены устройства
            current_time = time.time()
            time_since_device_change = current_time - self.last_device_change_time
            
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
                return False

            self.state = RecognitionState.LISTENING
            self.is_listening = True
            self.audio_data = []
            self.stop_event.clear()
            self.prepared_device_id = device_id
            
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
            self.prepared_device_id = None
            await self._notify_state_change(RecognitionState.IDLE, error=str(e))
            return False
            
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

            # Получаем текущий активный input (id может быть int или None)
            default_input = None
            try:
                default_setting = sd.default.device
                # Обрабатываем _InputOutputPair и обычные списки/кортежи
                if hasattr(default_setting, '__getitem__'):
                    default_input = default_setting[0]
            except Exception:
                default_input = None

            device_info = None
            try:
                device_info = sd.query_devices(default_input, 'input')
            except Exception:
                device_info = None

            if not device_info:
                try:
                    for idx, dev in enumerate(sd.query_devices()):
                        if dev.get('max_input_channels', 0) > 0:
                            device_info = dev
                            default_input = idx
                            break
                except Exception:
                    device_info = None

            if not device_info:
                raise RuntimeError("Входное аудио устройство не найдено")

            self.input_device_info = device_info
            self.input_device_id = default_input

            # Частота и количество каналов устройства - только от устройства
            samplerate = device_info.get('default_samplerate')
            channels = device_info.get('max_input_channels')
            
            if not samplerate:
                raise RuntimeError(f"Устройство {device_info.get('name', 'Unknown')} не предоставляет default_samplerate")
            if not channels:
                raise RuntimeError(f"Устройство {device_info.get('name', 'Unknown')} не предоставляет max_input_channels")
            
            self.actual_input_rate = float(samplerate)
            self.actual_input_channels = int(channels)

            logger.info(
                "🎧 Входное устройство: name=%s, id=%s, default_rate=%s, max_channels=%s, low_latency=%s, high_latency=%s → actual_rate=%s, channels=%s",
                device_info.get('name'),
                self.input_device_id,
                device_info.get('default_samplerate'),
                device_info.get('max_input_channels'),
                device_info.get('default_low_input_latency'),
                device_info.get('default_high_input_latency'),
                self.actual_input_rate,
                self.actual_input_channels,
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
                logger.info(
                    "🔊 Выходное устройство: name=%s, id=%s, max_channels=%s, default_rate=%s, low_latency=%s, high_latency=%s",
                    output_info.get('name'),
                    self.output_device_id,
                    output_info.get('max_output_channels'),
                    output_info.get('default_samplerate'),
                    output_info.get('default_low_output_latency'),
                    output_info.get('default_high_output_latency'),
                )
            else:
                self.output_device_info = {}
                self.output_device_id = None

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
            device_id = self.prepared_device_id or self._prepare_input_device()
            first_chunk_timeout, retry_delay = self._get_stream_start_timing()
            logger.debug(
                "🎧 Настройка окна и повтора старта: timeout=%.2fs, retry_delay=%.2fs, retries=%s",
                first_chunk_timeout,
                retry_delay,
                self.max_stream_start_retries,
            )

            # Мягкий retry: пытаемся стартовать поток с паузами между попытками
            for attempt in range(self.max_stream_start_retries):
                try:
                    # Сбрасываем флаг первого чанка
                    self.first_chunk_received = False

                    # Создаём поток
                    # КРИТИЧНО: Используем blocksize >= 2048 и latency='high' для предотвращения CoreAudio overload
                    # Минимальный blocksize = 2048 для стабильности на macOS
                    effective_blocksize = max(2048, self.config.chunk_size)
                    if effective_blocksize > self.config.chunk_size:
                        logger.info(f"🔧 Blocksize увеличен с {self.config.chunk_size} до {effective_blocksize} для стабильности CoreAudio")

                    logger.info(f"🔊 AUDIO: Создание потока: device_id={device_id}, rate={self.actual_input_rate}Hz, channels={self.actual_input_channels}, blocksize={effective_blocksize}, latency=high")

                    stream = sd.InputStream(
                        device=device_id,
                        samplerate=self.actual_input_rate,
                        channels=self.actual_input_channels,
                        dtype='float32',
                        blocksize=effective_blocksize,  # Минимум 2048 для предотвращения overload
                        latency='high',  # Высокая латентность для предотвращения пропуска циклов
                        callback=self._audio_callback,
                    )

                    # Стартуем поток
                    stream.start()
                    logger.debug(f"🔊 AUDIO: Поток стартовал успешно")
                    logger.debug(f"🔄 Попытка {attempt + 1}/{self.max_stream_start_retries}: поток стартовал")

                    # Ждём первый чанк с таймаутом
                    start_wait = time.time()
                    while not self.first_chunk_received:
                        if (time.time() - start_wait) > first_chunk_timeout:
                            raise TimeoutError(f"Первый чанк не получен за {first_chunk_timeout:.1f}s")
                        if not self.is_listening or self.stop_event.is_set():
                            # Пользователь отменил - выходим
                            return
                        time.sleep(0.01)

                    # Успех! Первый чанк получен
                    logger.info("✅ Аудио поток стабилен, первый чанк получен")
                    stream_started = True
                    break

                except (sd.PortAudioError, TimeoutError) as e:
                    logger.warning(f"⚠️ Попытка {attempt + 1}/{self.max_stream_start_retries}: {e}")

                    # Закрываем неудачный поток
                    if stream:
                        try:
                            stream.stop()
                            stream.close()
                        except Exception:
                            pass
                        stream = None

                    # Если ещё есть попытки - ждём и пробуем снова
                    if attempt < self.max_stream_start_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    else:
                        # Последняя попытка провалилась - уведомляем пользователя
                        logger.error("❌ Не удалось стартовать аудио поток после всех попыток")
                        self._notify_microphone_unstable()
                        raise

            if not stream_started:
                raise RuntimeError("Не удалось запустить аудио поток")

            # Поток работает - ждём завершения
            with stream:
                while self.is_listening and not self.stop_event.is_set():
                    time.sleep(0.1)

            duration = time.time() - self.listen_start_time if self.listen_start_time else 0
            logger.debug("🛑 Поток записи остановлен, длительность=%.2fs", duration)

        except Exception as e:
            logger.error(f"❌ Ошибка прослушивания микрофона: {e}")
            self.state = RecognitionState.ERROR
        finally:
            # Закрываем поток если он всё ещё открыт
            if stream:
                try:
                    stream.stop()
                    stream.close()
                except Exception:
                    pass
            self.prepared_device_id = None

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
            
    def _audio_callback(self, indata, frames, time, status):
        """Callback для записи аудио с диагностикой пустых чанков"""
        try:
            if status:
                logger.warning(f"⚠️ AUDIO callback status: {status}, frames={frames}")

            if self.is_listening:
                # Проверяем уровень сигнала (диагностика CoreAudio overload)
                peak = float(np.max(np.abs(indata)))

                if peak < 0.001:  # Пустой чанк
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
                    if len(self.audio_data) % 20 == 0:  # Каждые 20 чанков
                        logger.debug(f"🔊 AUDIO callback: chunks={len(self.audio_data)}, peak={peak:.4f}, frames={frames}")

                with self.audio_lock:
                    self.audio_data.append(indata.copy())
                    if len(self.audio_data) == 1:
                        # Устанавливаем флаг для retry логики
                        self.first_chunk_received = True
                        logger.info(
                            "🔊 Первый чанк получен: frames=%s, dtype=%s, peak=%.4f",
                            frames,
                            indata.dtype,
                            peak,
                        )

        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}")
            import traceback
            logger.error(f"❌ Traceback: {traceback.format_exc()}")
            
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
