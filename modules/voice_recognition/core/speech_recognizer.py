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

        # Инициализируем распознаватель
        self._init_recognizer()
        
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
            self.state = RecognitionState.IDLE
    

    async def start_listening(self) -> bool:
        """Начинает прослушивание микрофона"""
        try:
            if self.state != RecognitionState.IDLE:
                logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self.state.value}")
                return False

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
        """Запускает прослушивание микрофона через sounddevice"""
        try:
            logger.info("🎤 Прослушивание микрофона начато")

            self.listen_start_time = time.time()

            device_id = self.prepared_device_id or self._prepare_input_device()

            # Открываем аудио поток с СИСТЕМНЫМ дефолтным устройством
            with sd.InputStream(
                device=device_id,
                samplerate=self.actual_input_rate,
                channels=self.actual_input_channels,
                dtype='float32',  # работаем во float для кросс-девайс совместимости
                blocksize=self.config.chunk_size,
                callback=self._audio_callback,
            ):
                # Ждем пока не остановят прослушивание
                while self.is_listening and not self.stop_event.is_set():
                    time.sleep(0.1)

            duration = time.time() - self.listen_start_time if self.listen_start_time else 0
            logger.debug("🛑 Поток записи остановлен, длительность=%.2fs", duration)

        except Exception as e:
            logger.error(f"❌ Ошибка прослушивания микрофона: {e}")
            self.state = RecognitionState.ERROR
        finally:
            self.prepared_device_id = None
            
    def _audio_callback(self, indata, frames, time, status):
        """Callback для записи аудио"""
        try:
            if status:
                logger.warning(f"⚠️ Статус аудио: {status}")
                
            if self.is_listening:
                with self.audio_lock:
                    self.audio_data.append(indata.copy())
                    if len(self.audio_data) == 1:
                        logger.debug(
                            "🔊 Первый чанк получен: frames=%s, dtype=%s",
                            frames,
                            indata.dtype,
                        )
                    
        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}")
            
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
                "📈 Статистика аудио: chunks=%s, samples=%s, duration=%.2fs, peak=%.4f, rms=%.4f, rms_db=%.1f, actual_rate=%s, target_rate=%s, channels=%s",
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
