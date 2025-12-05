"""
Stream Managers - InputStreamManager и OutputStreamManager

Каждый держит StreamContext с StreamState (IDLE → OPENING → ACTIVE → CLOSING → IDLE/ERROR).
Умеет switch_device(desc) и open(desc) с BT delay и retry.
"""

import logging
import threading
import time
import asyncio
import sounddevice as sd
import numpy as np
from typing import Optional, Callable, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .device_state_cache import DeviceStateCache
from .types import DeviceDescriptor, StreamState, StreamContext

logger = logging.getLogger(__name__)


class BaseStreamManager:
    """Базовый класс для управления потоками"""
    
    def __init__(self, stream_type: str = "input", device_cache: Optional['DeviceStateCache'] = None):
        """
        Инициализация менеджера
        
        Args:
            stream_type: Тип потока ("input" или "output")
            device_cache: Опциональный кэш устройств (DeviceStateCache)
        """
        self._stream_type = stream_type
        self._context = StreamContext()
        self._device_cache = device_cache  # Для получения устройств из кэша
        self._retry_count = 0
        self._max_retries = 3
        self._bt_delay = 2.5  # Задержка для Bluetooth устройств (секунды)
        self._normal_delay = 0.3  # Задержка для обычных устройств (секунды)
        
        logger.info(f"BaseStreamManager создан (тип: {stream_type})")
    
    def ensure_stream(self, callback: Optional[Callable] = None) -> bool:
        """
        Обеспечивает наличие активного потока
        
        Согласно документации: берет current descriptor из кэша и вызывает open(desc)/switch_device.
        
        Args:
            callback: Callback функция для обработки данных потока
            
        Returns:
            True если поток успешно создан/уже активен
        """
        with self._context.lock:
            if self._context.state == StreamState.ACTIVE:
                logger.debug("Поток уже активен")
                return True
            
            if self._context.state in {StreamState.OPENING, StreamState.CLOSING}:
                logger.warning("⚠️ Поток в процессе открытия/закрытия, ожидаем...")
                return False
            
            # Получаем устройство из кэша или используем текущее
            device = None
            if self._context.current_device:
                device = self._context.current_device
            elif self._device_cache:
                # Берем устройство из кэша согласно документации
                try:
                    if self._stream_type == "input":
                        device = self._device_cache.get_default_input()
                    else:
                        device = self._device_cache.get_default_output()
                except RuntimeError:
                    logger.warning("⚠️ Устройство не инициализировано в кэше")
                    return False
            else:
                logger.warning("⚠️ Устройство не установлено и кэш недоступен, невозможно создать поток")
                return False
            
            # Если устройство уже установлено и совпадает - просто открываем
            if self._context.current_device and self._context.current_device.uid == device.uid:
                return self._open(device, callback)
            else:
                # Переключаем устройство
                return self.switch_device(device, callback)
    
    def switch_device(self, desc: DeviceDescriptor, callback: Optional[Callable] = None) -> bool:
        """
        Переключает устройство потока
        
        Args:
            desc: Дескриптор нового устройства
            callback: Callback функция для обработки данных потока
            
        Returns:
            True если переключение успешно
        """
        with self._context.lock:
            if self._context.current_device and self._context.current_device.uid == desc.uid:
                logger.debug(f"Устройство уже установлено: {desc.name}")
                return True
            
            if self._context.state in {StreamState.ACTIVE, StreamState.OPENING}:
                # Устанавливаем pending_device и начинаем graceful close
                logger.info(f"🔄 Переключение устройства: {self._context.current_device.name if self._context.current_device else 'None'} -> {desc.name}")
                self._context.pending_device = desc
                self._context.transition(StreamState.CLOSING)
                self._graceful_close()
            else:
                # Поток не активен, просто открываем новое устройство
                self._context.pending_device = desc
                return self._open(desc, callback)
        
        # После закрытия открываем новое устройство
        return self._open_after_close(desc, callback)
    
    def _open(self, desc: DeviceDescriptor, callback: Optional[Callable] = None) -> bool:
        """
        Открывает поток на устройстве
        
        Args:
            desc: Дескриптор устройства
            callback: Callback функция
            
        Returns:
            True если открытие успешно
        """
        self._context.transition(StreamState.OPENING)
        
        try:
            # Получаем индекс устройства по имени или используем дефолтное
            device_index = None
            try:
                devices = sd.query_devices()
                for idx, device in enumerate(devices):
                    if device.get('name') == desc.name:
                        device_index = idx
                        break
            except Exception as e:
                logger.warning(f"⚠️ Не удалось найти устройство по имени, используем дефолтное: {e}")
            
            # Создаём поток через sounddevice
            if self._stream_type == "input":
                stream = sd.InputStream(
                    device=device_index,
                    samplerate=int(desc.sample_rate),
                    channels=1,
                    dtype='int16',
                    blocksize=int(desc.blocksize) if desc.blocksize > 0 else None,
                    latency=desc.latency if desc.latency > 0 else None,
                    callback=callback
                )
            else:
                stream = sd.OutputStream(
                    device=device_index,
                    samplerate=int(desc.sample_rate),
                    channels=1,
                    dtype='int16',
                    blocksize=int(desc.blocksize) if desc.blocksize > 0 else None,
                    latency=desc.latency if desc.latency > 0 else None,
                    callback=callback
                )
            
            stream.start()
            
            with self._context.lock:
                self._context.stream = stream
                self._context.current_device = desc
                self._context.pending_device = None
                self._context.transition(StreamState.ACTIVE)
                self._retry_count = 0
            
            logger.info(f"✅ Поток открыт: {desc.name} (тип: {self._stream_type})")
            return True
            
        except sd.PortAudioError as e:
            error_code = e.args[0] if e.args else 0
            logger.error(f"❌ PortAudio ошибка при открытии потока: {error_code} - {e}")
            
            # Обработка специфичных ошибок PortAudio
            if error_code in (-9986, -10851):
                return self._handle_portaudio_error(desc, callback, error_code)
            else:
                self._context.transition(StreamState.IDLE)
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка открытия потока: {e}", exc_info=True)
            self._context.transition(StreamState.IDLE)
            return False
    
    def _handle_portaudio_error(self, desc: DeviceDescriptor, callback: Optional[Callable], error_code: int) -> bool:
        """
        Обрабатывает ошибки PortAudio с retry логикой
        
        Args:
            desc: Дескриптор устройства
            callback: Callback функция
            error_code: Код ошибки PortAudio
            
        Returns:
            True если после retry поток открыт успешно
        """
        if self._retry_count >= self._max_retries:
            logger.error(f"❌ Достигнут максимум попыток ({self._max_retries}) для ошибки {error_code}")
            self._context.transition(StreamState.IDLE)
            return False
        
        self._context.transition(StreamState.ERROR_RETRYING)
        self._retry_count += 1
        
        # Экспоненциальный backoff: min(0.5 * retry, 5) секунд
        delay = min(0.5 * self._retry_count, 5.0)
        logger.info(f"🔄 Retry {self._retry_count}/{self._max_retries} через {delay} сек (ошибка: {error_code})")
        time.sleep(delay)
        
        # Повторная попытка открытия
        return self._open(desc, callback)
    
    def _graceful_close(self):
        """Graceful закрытие потока"""
        try:
            if self._context.stream:
                self._context.stream.stop()
                self._context.stream.close()
                self._context.stream = None
            
            self._context.transition(StreamState.IDLE)
            logger.debug("✅ Поток закрыт gracefully")
            
        except Exception as e:
            logger.error(f"❌ Ошибка закрытия потока: {e}", exc_info=True)
            self._context.transition(StreamState.IDLE)
    
    def _open_after_close(self, desc: DeviceDescriptor, callback: Optional[Callable] = None) -> bool:
        """
        Открывает поток после закрытия с задержкой для BT
        
        Args:
            desc: Дескриптор устройства
            callback: Callback функция
            
        Returns:
            True если открытие успешно
        """
        # Задержка для Bluetooth устройств
        delay = self._bt_delay if desc.is_bluetooth else self._normal_delay
        if delay > 0:
            logger.debug(f"⏳ Задержка {delay} сек перед открытием потока (BT: {desc.is_bluetooth})")
            time.sleep(delay)
        
        return self._open(desc, callback)
    
    def close(self):
        """Закрывает поток"""
        with self._context.lock:
            if self._context.state == StreamState.IDLE:
                return
            
            self._context.transition(StreamState.CLOSING)
            self._graceful_close()
    
    def get_current_device(self) -> Optional[DeviceDescriptor]:
        """Получает текущее устройство"""
        with self._context.lock:
            return self._context.current_device
    
    def is_active(self) -> bool:
        """Проверяет, активен ли поток"""
        with self._context.lock:
            return self._context.state == StreamState.ACTIVE


class InputStreamManager(BaseStreamManager):
    """Менеджер INPUT потоков"""
    
    def __init__(self, device_cache: Optional['DeviceStateCache'] = None):
        super().__init__(stream_type="input", device_cache=device_cache)
        logger.info("InputStreamManager создан")


class OutputStreamManager(BaseStreamManager):
    """Менеджер OUTPUT потоков"""
    
    def __init__(self, device_cache: Optional['DeviceStateCache'] = None):
        super().__init__(stream_type="output", device_cache=device_cache)
        logger.info("OutputStreamManager создан")

