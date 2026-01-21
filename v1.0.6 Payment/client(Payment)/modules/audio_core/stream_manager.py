"""
AudioStreamManager - Менеджер для управления PortAudio streams

✅ ЦИКЛ 2: Единый API для управления lifecycle PortAudio streams
- Гарантированное закрытие старого потока перед созданием нового
- Lock, ожидание active=False, адаптивные задержки
- Логирование PaErrorCode и обработка "неустойчивых" устройств
- Retry логика с экспоненциальным backoff
"""

import asyncio
import logging
import threading
import time
from typing import Optional, Callable, Dict, Any, Literal, Tuple
from dataclasses import dataclass
import sounddevice as sd
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class StreamConfig:
    """Конфигурация для создания PortAudio stream"""
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    samplerate: int = 48000
    channels: int = 1
    dtype: str = 'int16'
    blocksize: Optional[int] = None
    latency: Optional[float] = None
    callback: Optional[Callable] = None
    is_bluetooth: bool = False


@dataclass
class StreamOperationResult:
    """Результат операции со stream"""
    success: bool
    stream: Optional[sd.Stream] = None
    error_code: Optional[int] = None
    error_message: Optional[str] = None
    attempt: int = 0
    duration_ms: float = 0.0


class AudioStreamManager:
    """
    Менеджер для управления lifecycle PortAudio streams
    
    Функции:
    - Гарантированное закрытие старого потока перед созданием нового
    - Адаптивные задержки для BT устройств
    - Retry логика с экспоненциальным backoff
    - Логирование всех операций и ошибок
    - Обработка ошибок -9986/-10851
    """
    
    def __init__(self, stream_type: Literal["input", "output"]):
        """
        Инициализация менеджера
        
        Args:
            stream_type: Тип потока (input/output)
        """
        self.stream_type = stream_type
        self._lock = threading.RLock()
        
        # Текущий активный поток
        self._current_stream: Optional[sd.Stream] = None
        
        # Конфигурация задержек
        self._close_delay_bt = 2.5  # секунд для BT устройств
        self._close_delay_normal = 0.3  # секунд для обычных устройств
        self._max_wait_active_bt = 3.0  # секунд для BT устройств
        self._max_wait_active_normal = 1.0  # секунд для обычных устройств
        
        # Retry конфигурация
        self._max_retries = 5
        self._base_retry_delay = 0.5  # секунд
        
        # Кэш безопасных конфигураций
        self._safe_configs: Dict[str, StreamConfig] = {}
        
        logger.info(f"🔧 AudioStreamManager создан (type: {stream_type})")
    
    async def create_stream(
        self,
        config: StreamConfig,
        max_retries: Optional[int] = None
    ) -> StreamOperationResult:
        """
        Создает новый PortAudio stream
        
        Args:
            config: Конфигурация потока
            max_retries: Максимум попыток (если None, используется дефолт)
        
        Returns:
            StreamOperationResult с результатом операции
        """
        if max_retries is None:
            max_retries = self._max_retries
        
        start_time = time.time()
        attempt = 0
        
        # ✅ ДИАГНОСТИКА: Логируем вход в метод для отслеживания зависаний
        logger.info(
            f"🔍 [{self.stream_type.upper()}] create_stream ВХОД: "
            f"device={config.device_id} ({config.device_name}), "
            f"BT={config.is_bluetooth}, max_retries={max_retries}"
        )
        
        logger.debug(f"🔍 [{self.stream_type.upper()}] create_stream: пытаемся захватить lock...")
        lock_acquire_start = time.time()
        with self._lock:
            lock_acquire_duration = (time.time() - lock_acquire_start) * 1000
            logger.debug(
                f"✅ [{self.stream_type.upper()}] create_stream: lock захвачен "
                f"(время ожидания: {lock_acquire_duration:.1f}ms), начинаем создание потока"
            )
            # Закрываем старый поток если есть
            if self._current_stream:
                await self._close_stream_safe(self._current_stream, config.is_bluetooth)
                self._current_stream = None
            
            while attempt < max_retries:
                try:
                    attempt += 1
                    
                    # ✅ ЦИКЛ 2: Логирование всех параметров перед созданием потока
                    logger.info(
                        f"🔄 [{self.stream_type.upper()}] Попытка {attempt}/{max_retries} создания потока:\n"
                        f"   device_id={config.device_id}, device_name={config.device_name}\n"
                        f"   samplerate={config.samplerate}Hz, channels={config.channels}\n"
                        f"   dtype={config.dtype}, blocksize={config.blocksize}, latency={config.latency}\n"
                        f"   is_bluetooth={config.is_bluetooth}, callback={config.callback is not None}"
                    )
                    
                    # Подготовка параметров для создания потока
                    logger.debug(f"🔍 [{self.stream_type.upper()}] Подготавливаем параметры потока...")
                    stream_params = self._prepare_stream_params(config)
                    logger.debug(f"🔍 [{self.stream_type.upper()}] Параметры подготовлены: {stream_params}")
                    
                    # Создаем поток
                    logger.debug(f"🔍 [{self.stream_type.upper()}] Создаем {self.stream_type} поток через PortAudio...")
                    if self.stream_type == "input":
                        stream = sd.InputStream(**stream_params)
                    else:
                        stream = sd.OutputStream(**stream_params)
                    logger.debug(f"✅ [{self.stream_type.upper()}] Поток создан через PortAudio: {stream}")
                    
                    # Проверяем, что поток создан успешно
                    if stream is None:
                        raise RuntimeError("Поток не был создан")
                    
                    # Сохраняем успешную конфигурацию
                    self._current_stream = stream
                    cache_key = self._get_config_cache_key(config)
                    self._safe_configs[cache_key] = config
                    
                    duration_ms = (time.time() - start_time) * 1000
                    logger.info(
                        f"✅ [{self.stream_type.upper()}] Поток создан успешно на попытке {attempt} "
                        f"(время: {duration_ms:.1f}ms)"
                    )
                    
                    return StreamOperationResult(
                        success=True,
                        stream=stream,
                        attempt=attempt,
                        duration_ms=duration_ms
                    )
                    
                except sd.PortAudioError as e:
                    error_code = e.args[0] if e.args else None
                    error_message = str(e)
                    
                    duration_ms = (time.time() - start_time) * 1000
                    
                    # ✅ ЦИКЛ 2: Специальная обработка ошибок -9986/-10851 с fallback
                    if error_code in (-9986, -10851):
                        logger.warning(
                            f"⚠️ [{self.stream_type.upper()}] PortAudio ошибка {error_code} на попытке {attempt}: {error_message}"
                        )
                        
                        # ✅ ЦИКЛ 2: Fallback на device=None при повторной ошибке (начиная со 2-й попытки)
                        if attempt >= 2 and config.device_id is not None:
                            logger.warning(
                                f"⚠️ [{self.stream_type.upper()}] Fallback на device=None после ошибки {error_code} "
                                f"(попытка {attempt})"
                            )
                            
                            # Создаем fallback конфигурацию: device=None, очищаем blocksize/latency
                            fallback_config = StreamConfig(
                                device_id=None,  # macOS выберет сам
                                device_name=config.device_name,
                                samplerate=config.samplerate,
                                channels=config.channels,
                                dtype=config.dtype,
                                callback=config.callback,
                                blocksize=None,  # Не задаем - macOS выберет
                                latency=None,   # Не задаем - macOS выберет
                                is_bluetooth=config.is_bluetooth
                            )
                            
                            # Пробуем с fallback конфигурацией
                            try:
                                logger.info(
                                    f"🔄 [{self.stream_type.upper()}] Попытка с fallback конфигурацией "
                                    f"(device=None, macOS выберет параметры)"
                                )
                                
                                fallback_params = self._prepare_stream_params(fallback_config)
                                if self.stream_type == "input":
                                    stream = sd.InputStream(**fallback_params)
                                else:
                                    stream = sd.OutputStream(**fallback_params)
                                
                                if stream is None:
                                    raise RuntimeError("Поток не был создан с fallback конфигурацией")
                                
                                # Успех с fallback - сохраняем fallback конфигурацию
                                self._current_stream = stream
                                cache_key = self._get_config_cache_key(fallback_config)
                                self._safe_configs[cache_key] = fallback_config
                                
                                duration_ms = (time.time() - start_time) * 1000
                                logger.info(
                                    f"✅ [{self.stream_type.upper()}] Поток создан успешно с fallback конфигурацией "
                                    f"на попытке {attempt} (время: {duration_ms:.1f}ms)"
                                )
                                
                                return StreamOperationResult(
                                    success=True,
                                    stream=stream,
                                    attempt=attempt,
                                    duration_ms=duration_ms
                                )
                            except Exception as fallback_error:
                                logger.error(
                                    f"❌ [{self.stream_type.upper()}] Fallback также не удался: {fallback_error}"
                                )
                                # Продолжаем с обычным retry
                        
                        # Для этих ошибок увеличиваем задержку перед следующей попыткой
                        if attempt < max_retries:
                            retry_delay = self._base_retry_delay * (2 ** attempt)
                            if config.is_bluetooth:
                                retry_delay *= 2  # Удваиваем для BT
                            
                            logger.info(
                                f"⏳ [{self.stream_type.upper()}] Повтор через {retry_delay:.1f}с "
                                f"(устройство может быть занято)"
                            )
                            await asyncio.sleep(retry_delay)
                            continue
                    
                    # Для других ошибок используем стандартный retry
                    if attempt < max_retries:
                        retry_delay = self._base_retry_delay * (2 ** attempt)
                        logger.warning(
                            f"⚠️ [{self.stream_type.upper()}] Ошибка создания потока на попытке {attempt}: "
                            f"{error_message} (код: {error_code}). Повтор через {retry_delay:.1f}с"
                        )
                        await asyncio.sleep(retry_delay)
                    else:
                        logger.error(
                            f"❌ [{self.stream_type.upper()}] Не удалось создать поток после {max_retries} попыток: "
                            f"{error_message} (код: {error_code})"
                        )
                        return StreamOperationResult(
                            success=False,
                            error_code=error_code,
                            error_message=error_message,
                            attempt=attempt,
                            duration_ms=duration_ms
                        )
                
                except Exception as e:
                    duration_ms = (time.time() - start_time) * 1000
                    logger.error(
                        f"❌ [{self.stream_type.upper()}] Неожиданная ошибка создания потока на попытке {attempt}: {e}",
                        exc_info=True
                    )
                    
                    if attempt < max_retries:
                        retry_delay = self._base_retry_delay * (2 ** attempt)
                        await asyncio.sleep(retry_delay)
                    else:
                        return StreamOperationResult(
                            success=False,
                            error_message=str(e),
                            attempt=attempt,
                            duration_ms=duration_ms
                        )
        
        # Если дошли сюда - все попытки исчерпаны
        duration_ms = (time.time() - start_time) * 1000
        return StreamOperationResult(
            success=False,
            error_message="Все попытки создания потока исчерпаны",
            attempt=max_retries,
            duration_ms=duration_ms
        )
    
    async def close_stream(
        self,
        stream: Optional[sd.Stream],
        is_bluetooth: bool = False
    ) -> bool:
        """
        Безопасно закрывает PortAudio stream
        
        Args:
            stream: Поток для закрытия
            is_bluetooth: Является ли устройство Bluetooth
        
        Returns:
            True если закрытие успешно, False иначе
        """
        if stream is None:
            return True
        
        with self._lock:
            # Если это текущий поток, очищаем ссылку
            if stream == self._current_stream:
                self._current_stream = None
            
            return await self._close_stream_safe(stream, is_bluetooth)
    
    async def switch_device(
        self,
        old_stream: Optional[sd.Stream],
        new_config: StreamConfig,
        max_retries: Optional[int] = None
    ) -> StreamOperationResult:
        """
        Безопасно переключает устройство (закрывает старое, создает новое)
        
        Args:
            old_stream: Старый поток (может быть None)
            new_config: Конфигурация нового потока
            max_retries: Максимум попыток создания нового потока
        
        Returns:
            StreamOperationResult с результатом операции
        """
        start_time = time.time()
        
        with self._lock:
            # Закрываем старый поток
            if old_stream:
                logger.info(
                    f"🔄 [{self.stream_type.upper()}] Закрытие старого потока перед переключением устройства"
                )
                await self._close_stream_safe(old_stream, new_config.is_bluetooth)
            
            # Создаем новый поток
            result = await self.create_stream(new_config, max_retries)
            
            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                f"🔄 [{self.stream_type.upper()}] Переключение устройства завершено "
                f"(время: {duration_ms:.1f}ms, успех: {result.success})"
            )
            
            return result
    
    async def _close_stream_safe(
        self,
        stream: sd.Stream,
        is_bluetooth: bool = False
    ) -> bool:
        """
        Безопасно закрывает поток с ожиданием active=False
        
        Args:
            stream: Поток для закрытия
            is_bluetooth: Является ли устройство Bluetooth
        
        Returns:
            True если закрытие успешно
        """
        try:
            # Останавливаем поток если активен
            if hasattr(stream, 'active') and stream.active:
                logger.debug(f"🛑 [{self.stream_type.upper()}] Остановка активного потока...")
                stream.stop()
            
            # Ждем пока поток станет неактивным
            max_wait = self._max_wait_active_bt if is_bluetooth else self._max_wait_active_normal
            wait_start = time.time()
            
            while hasattr(stream, 'active') and stream.active:
                if time.time() - wait_start > max_wait:
                    logger.warning(
                        f"⚠️ [{self.stream_type.upper()}] Поток не стал неактивным за {max_wait}с, "
                        f"продолжаем закрытие"
                    )
                    break
                await asyncio.sleep(0.1)
            
            # Закрываем поток
            logger.debug(f"🔒 [{self.stream_type.upper()}] Закрытие потока...")
            stream.close()
            
            # Задержка после закрытия (больше для BT устройств)
            close_delay = self._close_delay_bt if is_bluetooth else self._close_delay_normal
            if close_delay > 0:
                logger.debug(
                    f"⏳ [{self.stream_type.upper()}] Задержка после закрытия: {close_delay:.1f}с "
                    f"(BT={is_bluetooth})"
                )
                await asyncio.sleep(close_delay)
            
            logger.debug(f"✅ [{self.stream_type.upper()}] Поток успешно закрыт")
            return True
            
        except Exception as e:
            logger.error(
                f"❌ [{self.stream_type.upper()}] Ошибка закрытия потока: {e}",
                exc_info=True
            )
            return False
    
    def _prepare_stream_params(self, config: StreamConfig) -> Dict[str, Any]:
        """
        Подготавливает параметры для создания PortAudio stream
        
        Args:
            config: Конфигурация потока
        
        Returns:
            Словарь параметров для sd.InputStream/sd.OutputStream
        """
        params: Dict[str, Any] = {
            'device': config.device_id,
            'samplerate': config.samplerate,
            'channels': config.channels,
            'dtype': config.dtype,
            'callback': config.callback,
        }
        
        # Для BT устройств не задаем blocksize и latency (macOS выбирает сам)
        if not config.is_bluetooth:
            if config.blocksize is not None:
                params['blocksize'] = config.blocksize
            if config.latency is not None:
                params['latency'] = config.latency
        
        return params
    
    def _get_config_cache_key(self, config: StreamConfig) -> str:
        """Генерирует ключ для кэша конфигураций"""
        return f"{config.device_name}_{config.samplerate}_{config.channels}_{config.is_bluetooth}"
    
    def get_current_stream(self) -> Optional[sd.Stream]:
        """Получить текущий активный поток"""
        with self._lock:
            return self._current_stream
    
    def is_stream_active(self) -> bool:
        """Проверяет, активен ли текущий поток"""
        with self._lock:
            if self._current_stream:
                return hasattr(self._current_stream, 'active') and self._current_stream.active
            return False

