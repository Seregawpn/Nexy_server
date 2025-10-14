"""
HealthChecker - проверка здоровья микрофона
"""

import time
import queue
import numpy as np
import sounddevice as sd
import logging
from typing import Optional, Callable
from .types import HealthStatus, AudioMetrics

logger = logging.getLogger(__name__)

class HealthChecker:
    """Проверка здоровья микрофона через RMS анализ"""
    
    def __init__(
        self,
        sample_rate: int = 16000,
        channels: int = 1,
        dtype: str = "int16",
        rms_threshold: float = 1e-4,
        silent_threshold: float = 1e-6,
        check_duration: float = 0.3
    ):
        self.sample_rate = sample_rate
        self.channels = channels
        self.dtype = dtype
        self.rms_threshold = rms_threshold
        self.silent_threshold = silent_threshold
        self.check_duration = check_duration
        
        # Буфер для аудио данных
        self.audio_queue = queue.Queue(maxsize=8)
        self.is_checking = False
        
        # Callbacks
        self.on_health_change: Optional[Callable[[HealthStatus], None]] = None
        self.on_metrics_update: Optional[Callable[[AudioMetrics], None]] = None
        
        # Состояние
        self.last_health_status = HealthStatus.UNKNOWN
        self.last_metrics = AudioMetrics()
        
    def set_callbacks(
        self,
        on_health_change: Optional[Callable[[HealthStatus], None]] = None,
        on_metrics_update: Optional[Callable[[AudioMetrics], None]] = None
    ):
        """Установка callback функций"""
        self.on_health_change = on_health_change
        self.on_metrics_update = on_metrics_update
    
    def _audio_callback(self, indata, frames, time_info, status):
        """Callback для получения аудио данных"""
        if status:
            logger.debug(f"[HealthCheck] Audio status: {status}")
        
        try:
            self.audio_queue.put_nowait(indata.copy())
        except queue.Full:
            # Игнорируем переполнение буфера
            pass
    
    def check_health(self) -> tuple[HealthStatus, AudioMetrics]:
        """
        Проверка здоровья микрофона
        
        Returns:
            tuple: (HealthStatus, AudioMetrics)
        """
        if self.is_checking:
            return self.last_health_status, self.last_metrics
            
        self.is_checking = True
        
        try:
            # Создаем временный поток для проверки
            stream = sd.InputStream(
                device=None,  # Default input
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype=self.dtype,
                callback=self._audio_callback,
                blocksize=int(self.sample_rate * 0.1)  # 100ms блоки
            )
            
            # Очищаем очередь
            while not self.audio_queue.empty():
                try:
                    self.audio_queue.get_nowait()
                except queue.Empty:
                    break
            
            # Запускаем поток
            stream.start()
            
            # Собираем данные
            need_samples = int(self.check_duration * self.sample_rate)
            collected_data = []
            got_samples = 0
            deadline = time.time() + self.check_duration + 1.0
            
            while got_samples < need_samples and time.time() < deadline:
                try:
                    chunk = self.audio_queue.get(timeout=0.2)
                    collected_data.append(chunk)
                    got_samples += len(chunk)
                except queue.Empty:
                    continue
            
            # Останавливаем поток
            stream.stop()
            stream.close()
            
            # Анализируем данные
            if collected_data:
                audio_data = np.concatenate(collected_data, axis=0)
                
                # Конвертируем в float32 для анализа
                if audio_data.dtype != np.float32:
                    audio_data = audio_data.astype(np.float32)
                
                # Если стерео, усредняем каналы
                if audio_data.ndim == 2 and audio_data.shape[1] > 1:
                    audio_data = audio_data.mean(axis=1)
                
                # Вычисляем метрики
                rms = float(np.sqrt(np.mean(audio_data**2)))
                peak = float(np.max(np.abs(audio_data)))
                
                # Определяем статус здоровья
                if rms >= self.rms_threshold:
                    health_status = HealthStatus.HEALTHY
                elif rms >= self.silent_threshold:
                    health_status = HealthStatus.SILENT
                else:
                    health_status = HealthStatus.ERROR
                
                # Создаем метрики
                metrics = AudioMetrics(
                    rms_value=rms,
                    peak_value=peak,
                    sample_count=len(audio_data),
                    last_health_check=time.time()
                )
                
            else:
                # Нет данных
                health_status = HealthStatus.ERROR
                metrics = AudioMetrics(
                    last_health_check=time.time()
                )
            
            # Обновляем состояние
            if health_status != self.last_health_status:
                self.last_health_status = health_status
                if self.on_health_change:
                    self.on_health_change(health_status)
            
            self.last_metrics = metrics
            if self.on_metrics_update:
                self.on_metrics_update(metrics)
            
            logger.debug(f"[HealthCheck] Status: {health_status.value}, RMS: {metrics.rms_value:.6f}")
            
            return health_status, metrics
            
        except Exception as e:
            logger.error(f"[HealthCheck] Error: {e}")
            error_status = HealthStatus.ERROR
            error_metrics = AudioMetrics(
                error_count=self.last_metrics.error_count + 1,
                last_health_check=time.time()
            )
            
            if error_status != self.last_health_status:
                self.last_health_status = error_status
                if self.on_health_change:
                    self.on_health_change(error_status)
            
            self.last_metrics = error_metrics
            return error_status, error_metrics
            
        finally:
            self.is_checking = False
    
    def quick_check(self) -> bool:
        """
        Быстрая проверка - возвращает True если микрофон работает
        
        Returns:
            bool: True если микрофон активен
        """
        health_status, _ = self.check_health()
        return health_status == HealthStatus.HEALTHY
    
    def get_last_status(self) -> HealthStatus:
        """Получение последнего статуса здоровья"""
        return self.last_health_status
    
    def get_last_metrics(self) -> AudioMetrics:
        """Получение последних метрик"""
        return self.last_metrics
