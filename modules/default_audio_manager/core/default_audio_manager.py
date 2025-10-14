"""
DefaultAudioManager - управление аудио через системные дефолты macOS
"""

import asyncio
import logging
import time
import threading
from typing import Optional, Callable, Dict, Any
import sounddevice as sd
import numpy as np

from .types import (
    DefaultAudioConfig, AudioStreamState, HealthStatus,
    StreamError, AudioMetrics
)
from .health_checker import HealthChecker

logger = logging.getLogger(__name__)

class DefaultAudioManager:
    """Менеджер аудио, использующий системные дефолты macOS"""
    
    def __init__(self, config: DefaultAudioConfig):
        self.config = config
        self.state = AudioStreamState.STOPPED
        
        # Потоки
        self.input_stream: Optional[sd.InputStream] = None
        self.output_stream: Optional[sd.OutputStream] = None
        
        # Health checker
        self.health_checker = HealthChecker(
            sample_rate=config.input_sample_rate,
            channels=config.input_channels,
            dtype=config.dtype,
            rms_threshold=config.rms_threshold,
            silent_threshold=config.silent_threshold,
            check_duration=config.health_check_duration
        )
        
        # Мониторинг
        self.monitor_thread: Optional[threading.Thread] = None
        self.stop_monitoring = threading.Event()
        self.last_health_check = 0.0
        
        # Метрики
        self.metrics = AudioMetrics()
        self.error_count = 0
        self.last_error_time = 0.0
        
        # Callbacks
        self._setup_callbacks()
        
        # Буферы для аудио данных
        self.audio_data_buffer = []
        self.audio_lock = threading.Lock()
        
    def _setup_callbacks(self):
        """Настройка callback функций"""
        self.health_checker.set_callbacks(
            on_health_change=self._on_health_change,
            on_metrics_update=self._on_metrics_update
        )
    
    def _on_health_change(self, status: HealthStatus):
        """Callback изменения статуса здоровья"""
        if self.config.on_health_status_change:
            self.config.on_health_status_change(status)
        
        if self.config.log_health_checks:
            logger.info(f"🏥 [HEALTH] Статус изменился: {status.value}")
    
    def _on_metrics_update(self, metrics: AudioMetrics):
        """Callback обновления метрик"""
        self.metrics = metrics
        if self.config.on_metrics_update:
            self.config.on_metrics_update(metrics)
        
        if self.config.log_health_checks:
            logger.debug(f"📊 [METRICS] RMS: {metrics.rms_value:.6f}, Peak: {metrics.peak_value:.6f}")
    
    def _input_callback(self, indata, frames, time_info, status):
        """Callback для входного потока"""
        if status:
            logger.warning(f"[INPUT] Status: {status}")
        
        with self.audio_lock:
            self.audio_data_buffer.append(indata.copy())
            
            # Ограничиваем размер буфера
            if len(self.audio_data_buffer) > 100:
                self.audio_data_buffer = self.audio_data_buffer[-50:]
    
    def _output_callback(self, outdata, frames, time_info, status):
        """Callback для выходного потока"""
        if status:
            logger.warning(f"[OUTPUT] Status: {status}")
        
        # Заполняем тишиной (TTS будет подставлять свои данные)
        outdata.fill(0)
    
    async def start(self) -> bool:
        """Запуск аудио потоков"""
        try:
            if self.state != AudioStreamState.STOPPED:
                logger.warning(f"⚠️ [AUDIO] Потоки уже запущены в состоянии {self.state.value}")
                return False
            
            self.state = AudioStreamState.STARTING
            await self._notify_state_change()
            
            logger.info("🔄 [AUDIO] Запуск аудио потоков с системными дефолтами...")
            
            # Создаем входной поток
            self.input_stream = sd.InputStream(
                device=None,  # Default input
                samplerate=self.config.input_sample_rate,
                channels=self.config.input_channels,
                dtype=self.config.dtype,
                blocksize=self.config.chunk_size,
                callback=self._input_callback
            )
            
            # Создаем выходной поток
            self.output_stream = sd.OutputStream(
                device=None,  # Default output
                samplerate=self.config.output_sample_rate,
                channels=self.config.output_channels,
                dtype=self.config.dtype,
                blocksize=self.config.chunk_size,
                callback=self._output_callback
            )
            
            # Запускаем потоки
            self.input_stream.start()
            self.output_stream.start()
            
            self.state = AudioStreamState.RUNNING
            await self._notify_state_change()
            
            # Запускаем мониторинг
            self._start_monitoring()
            
            logger.info("✅ [AUDIO] Аудио потоки запущены успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка запуска потоков: {e}")
            self.state = AudioStreamState.ERROR
            await self._notify_state_change()
            await self._handle_error(StreamError(
                error_type="startup_error",
                error_message=str(e)
            ))
            return False
    
    async def stop(self) -> bool:
        """Остановка аудио потоков"""
        try:
            if self.state == AudioStreamState.STOPPED:
                return True
            
            self.state = AudioStreamState.STOPPING
            await self._notify_state_change()
            
            # Останавливаем мониторинг
            self._stop_monitoring()
            
            # Останавливаем потоки
            if self.input_stream:
                try:
                    self.input_stream.stop()
                    self.input_stream.close()
                except Exception as e:
                    logger.warning(f"⚠️ [AUDIO] Ошибка остановки input потока: {e}")
                finally:
                    self.input_stream = None
            
            if self.output_stream:
                try:
                    self.output_stream.stop()
                    self.output_stream.close()
                except Exception as e:
                    logger.warning(f"⚠️ [AUDIO] Ошибка остановки output потока: {e}")
                finally:
                    self.output_stream = None
            
            self.state = AudioStreamState.STOPPED
            await self._notify_state_change()
            
            logger.info("🛑 [AUDIO] Аудио потоки остановлены")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка остановки потоков: {e}")
            self.state = AudioStreamState.ERROR
            await self._notify_state_change()
            return False
    
    def _start_monitoring(self):
        """Запуск мониторинга здоровья"""
        if self.monitor_thread and self.monitor_thread.is_alive():
            return
        
        self.stop_monitoring.clear()
        self.monitor_thread = threading.Thread(
            target=self._monitor_loop,
            name="AudioHealthMonitor",
            daemon=True
        )
        self.monitor_thread.start()
        logger.debug("🔍 [MONITOR] Мониторинг здоровья запущен")
    
    def _stop_monitoring(self):
        """Остановка мониторинга здоровья"""
        if self.monitor_thread:
            self.stop_monitoring.set()
            self.monitor_thread.join(timeout=2.0)
            self.monitor_thread = None
            logger.debug("🛑 [MONITOR] Мониторинг здоровья остановлен")
    
    def _monitor_loop(self):
        """Цикл мониторинга здоровья"""
        while not self.stop_monitoring.is_set():
            try:
                current_time = time.time()
                
                # Проверяем здоровье с заданным интервалом
                if current_time - self.last_health_check >= self.config.health_check_interval:
                    self._check_health()
                    self.last_health_check = current_time
                
                # Небольшая пауза
                time.sleep(0.1)
                
            except Exception as e:
                logger.error(f"❌ [MONITOR] Ошибка в цикле мониторинга: {e}")
                time.sleep(1.0)
    
    def _check_health(self):
        """Проверка здоровья аудио"""
        try:
            health_status, metrics = self.health_checker.check_health()
            
            # Если здоровье плохое и включено авто-переоткрытие
            if (health_status == HealthStatus.ERROR and 
                self.config.auto_reopen_on_error and
                self.state == AudioStreamState.RUNNING):
                
                # Проверяем cooldown
                current_time = time.time()
                if current_time - self.last_error_time >= self.config.error_cooldown:
                    logger.warning("⚠️ [AUDIO] Плохое здоровье, переоткрываем потоки...")
                    # Запускаем переоткрытие в отдельном потоке
                    threading.Thread(
                        target=self._reopen_streams_sync,
                        daemon=True
                    ).start()
                    self.last_error_time = current_time
                    
        except Exception as e:
            logger.error(f"❌ [MONITOR] Ошибка проверки здоровья: {e}")
    
    def _reopen_streams_sync(self):
        """Синхронное переоткрытие потоков при ошибках"""
        try:
            logger.info("🔄 [AUDIO] Переоткрытие потоков...")
            
            # Останавливаем текущие потоки синхронно
            self._stop_streams_sync()
            
            # Небольшая пауза
            time.sleep(self.config.retry_delay)
            
            # Запускаем заново синхронно
            self._start_streams_sync()
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка переоткрытия потоков: {e}")
    
    def _start_streams_sync(self):
        """Синхронный запуск потоков"""
        try:
            # Создаем входной поток
            self.input_stream = sd.InputStream(
                device=None,  # Default input
                samplerate=self.config.input_sample_rate,
                channels=self.config.input_channels,
                dtype=self.config.dtype,
                blocksize=self.config.chunk_size,
                callback=self._input_callback
            )
            
            # Создаем выходной поток
            self.output_stream = sd.OutputStream(
                device=None,  # Default output
                samplerate=self.config.output_sample_rate,
                channels=self.config.output_channels,
                dtype=self.config.dtype,
                blocksize=self.config.chunk_size,
                callback=self._output_callback
            )
            
            # Запускаем потоки
            self.input_stream.start()
            self.output_stream.start()
            
            self.state = AudioStreamState.RUNNING
            logger.info("✅ [AUDIO] Потоки переоткрыты успешно")
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка переоткрытия: {e}")
            self.state = AudioStreamState.ERROR
    
    def _stop_streams_sync(self):
        """Синхронная остановка потоков"""
        try:
            if self.input_stream:
                self.input_stream.stop()
                self.input_stream.close()
                self.input_stream = None
            
            if self.output_stream:
                self.output_stream.stop()
                self.output_stream.close()
                self.output_stream = None
                
            self.state = AudioStreamState.STOPPED
            
        except Exception as e:
            logger.warning(f"⚠️ [AUDIO] Ошибка остановки потоков: {e}")
    
    async def _reopen_streams(self):
        """Переоткрытие потоков при ошибках (async версия)"""
        try:
            logger.info("🔄 [AUDIO] Переоткрытие потоков...")
            
            # Останавливаем текущие потоки
            await self.stop()
            
            # Небольшая пауза
            await asyncio.sleep(self.config.retry_delay)
            
            # Запускаем заново
            await self.start()
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка переоткрытия потоков: {e}")
            await self._handle_error(StreamError(
                error_type="reopen_error",
                error_message=str(e)
            ))
    
    async def _notify_state_change(self):
        """Уведомление об изменении состояния"""
        if self.config.on_stream_state_change:
            self.config.on_stream_state_change(self.state)
        
        if self.config.log_stream_events:
            logger.info(f"🔄 [STATE] Состояние изменилось: {self.state.value}")
    
    async def _handle_error(self, error: StreamError):
        """Обработка ошибок"""
        self.error_count += 1
        error.retry_count = self.error_count
        
        if self.config.on_error:
            self.config.on_error(error)
        
        logger.error(f"❌ [ERROR] {error.error_type}: {error.error_message}")
    
    def get_audio_data(self, max_samples: Optional[int] = None) -> np.ndarray:
        """Получение аудио данных из буфера"""
        with self.audio_lock:
            if not self.audio_data_buffer:
                return np.array([])
            
            # Объединяем все данные
            all_data = np.concatenate(self.audio_data_buffer, axis=0)
            
            # Ограничиваем количество сэмплов
            if max_samples and len(all_data) > max_samples:
                all_data = all_data[-max_samples:]
            
            # Очищаем буфер
            self.audio_data_buffer.clear()
            
            return all_data
    
    def get_current_state(self) -> AudioStreamState:
        """Получение текущего состояния"""
        return self.state
    
    def get_health_status(self) -> HealthStatus:
        """Получение статуса здоровья"""
        return self.health_checker.get_last_status()
    
    def get_metrics(self) -> AudioMetrics:
        """Получение текущих метрик"""
        return self.health_checker.get_last_metrics()
    
    def is_healthy(self) -> bool:
        """Проверка здоровья микрофона"""
        return self.health_checker.quick_check()
    
    async def __aenter__(self):
        """Async context manager entry"""
        await self.start()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        await self.stop()
