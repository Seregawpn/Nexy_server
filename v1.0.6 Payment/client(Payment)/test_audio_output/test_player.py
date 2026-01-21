"""
Упрощенный Player для тестирования Output Device Switching

Включает быстрые фиксы:
1. device=None в OutputStream
2. Пересоздание потока при каждой новой сессии
3. Флаг _stream_broken для обработки ошибок
"""

import logging
import threading
import time
import sounddevice as sd
import numpy as np
from typing import Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum

# ✅ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ УСТРОЙСТВ
from device_params_normalizer import DeviceParamsNormalizer, OutputParams

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PlaybackState(Enum):
    IDLE = "idle"
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"
    ERROR = "error"


@dataclass
class PlayerConfig:
    """Упрощенная конфигурация плеера"""
    sample_rate: int = 48000
    channels: int = 1
    dtype: str = 'int16'
    buffer_size: int = 512


class TestPlayer:
    """
    Упрощенный Player для тестирования Output Device Switching
    
    Ключевые изменения от оригинального Player:
    1. Использует device=None - PortAudio сам выберет default
    2. Пересоздает поток при каждой новой сессии
    3. Имеет флаг _stream_broken для обработки ошибок
    4. Интегрирован с CoreAudioMonitor для мониторинга в реальном времени
    """
    
    def __init__(self, config: Optional[PlayerConfig] = None, enable_realtime_monitoring: bool = True):
        """
        Инициализация плеера
        
        Args:
            config: Конфигурация плеера
            enable_realtime_monitoring: Включить мониторинг устройств в реальном времени
        """
        self.config = config or PlayerConfig()
        
        # ✅ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ УСТРОЙСТВ
        # Конфигурация нормализатора (можно загрузить из unified_config.yaml)
        normalizer_config = {
            'output_min_rate': 16000,
            'output_max_rate': 48000,
            'output_default_rate': 48000,
            'output_max_channels': 2,
        }
        self._params_normalizer = DeviceParamsNormalizer(normalizer_config)
        
        # Аудио поток
        self._audio_stream: Optional[sd.OutputStream] = None
        self._stream_lock = threading.RLock()
        self._stream_started = False
        
        # Текущая сессия
        self._current_playback_session_id: Optional[Any] = None
        
        # Флаг для обработки ошибок (используем Event вместо bool для thread-safety)
        self._stream_broken = threading.Event()
        
        # Отслеживание устройства для проверки смены во время воспроизведения
        self._last_known_device_id: Optional[int] = None
        self._device_check_counter = 0  # Счетчик для периодической проверки
        
        # Нормализованные параметры текущего устройства
        self._normalized_params: Optional[OutputParams] = None
        
        # Буфер для аудио данных
        self._audio_buffer = []
        self._buffer_lock = threading.Lock()
        
        # Состояние
        self.state = PlaybackState.IDLE
        
        # ✅ НОВОЕ: Мониторинг устройств в реальном времени
        self._realtime_monitoring_enabled = enable_realtime_monitoring
        self._device_monitor = None
        if enable_realtime_monitoring:
            try:
                from core_audio_monitor import CoreAudioMonitor
                self._device_monitor = CoreAudioMonitor(monitor_output=True, monitor_input=False)
                # Устанавливаем callback для автоматического переключения
                self._device_monitor.start_monitoring(
                    check_interval=0.5,
                    output_callback=self._on_device_changed_realtime
                )
                logger.info("✅ Мониторинг устройств в реальном времени включен")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось включить мониторинг устройств: {e}")
                self._realtime_monitoring_enabled = False
        
        logger.info("🔧 TestPlayer инициализирован")
        logger.info(f"📊 Конфигурация: sample_rate={self.config.sample_rate}Hz, channels={self.config.channels}")
    
    def add_audio_data(self, audio_data: np.ndarray, metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Добавить аудио данные для воспроизведения
        
        Ключевая логика:
        - При новой сессии - пересоздаем поток
        - Если поток сломан - пересоздаем
        - Используем device=None для автоматического выбора default
        """
        try:
            session_id = metadata.get('session_id') if metadata else None
            
            # ✅ ФИКС 1: Проверяем сломан ли поток (включая смену устройства)
            if self._stream_broken.is_set():
                logger.warning("🔄 [OUTPUT] Поток помечен как сломанный — пересоздаём")
                with self._stream_lock:
                    if self._stream_broken.is_set():  # Double-check под lock
                        self._stream_broken.clear()
                        if self._audio_stream is not None:
                            self._stop_audio_stream()
                        self._start_audio_stream()
                        # Обновляем информацию об устройстве после пересоздания
                        self._update_last_known_device()
            
            # ✅ ФИКС 2: Пересоздаем поток при каждой новой сессии
            if session_id != self._current_playback_session_id:
                logger.info(f"🔄 [OUTPUT] Новая сессия: {session_id} (старая: {self._current_playback_session_id})")
                
                # Останавливаем старый поток
                if self._audio_stream is not None:
                    logger.debug("🔄 [OUTPUT] Останавливаем старый поток")
                    self._stop_audio_stream()
                
                # Создаем новый поток с device=None
                self._start_audio_stream()
                
                # Обновляем текущую сессию и запоминаем устройство
                self._current_playback_session_id = session_id
                self._update_last_known_device()
            
            # Конвертируем данные в int16 если нужно
            if audio_data.dtype != np.int16:
                if audio_data.dtype in (np.float32, np.float64):
                    audio_data = np.clip(audio_data, -1.0, 1.0)
                    audio_data = (audio_data * 32767.0).astype(np.int16)
                else:
                    audio_data = audio_data.astype(np.int16)
            
            # Убеждаемся что данные в правильной форме
            if audio_data.ndim == 1:
                audio_data = audio_data.reshape(-1, 1)
            
            # Добавляем в буфер
            with self._buffer_lock:
                self._audio_buffer.append(audio_data)
            
            # Создаем поток если его нет
            if self._audio_stream is None:
                logger.debug("🔍 [OUTPUT] Поток не существует, создаём новый...")
                self._start_audio_stream()
            
            # Стартуем поток если нужно
            self._ensure_stream_started()
            
            logger.debug(f"✅ Аудио данные добавлены (shape: {audio_data.shape})")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка добавления аудио данных: {e}")
            self.state = PlaybackState.ERROR
            return False
    
    def _start_audio_stream(self, device_id: Optional[int] = None) -> bool:
        """
        Запуск аудио потока с нормализацией параметров устройства
        
        ✅ ФИКС 3: Используем device=None для автоматического выбора default
        ✅ НОРМАЛИЗАЦИЯ: Приводим параметры устройства к внутреннему формату Nexy
        """
        try:
            with self._stream_lock:
                if self._audio_stream is not None:
                    logger.warning("⚠️ Аудио поток уже создан")
                    return True
                
                # ✅ ШАГ 1: Получаем информацию об устройстве
                device_info = None
                device_name = "Unknown"
                
                try:
                    if device_id is None:
                        default_setting = sd.default.device
                        if hasattr(default_setting, '__getitem__'):
                            try:
                                device_id = default_setting[1]
                            except (IndexError, TypeError):
                                pass
                    
                    if device_id is not None:
                        device_info = sd.query_devices(device_id, 'output')
                        device_name = device_info.get('name', 'Unknown') if device_info else 'Unknown'
                except Exception as e:
                    logger.debug(f"⚠️ Ошибка получения информации об устройстве: {e}")
                
                # ✅ ШАГ 2: Нормализуем параметры устройства
                if device_info:
                    normalized = self._params_normalizer.select_output_params(device_info)
                    self._normalized_params = normalized
                    
                    # Обновляем конфиг с нормализованными параметрами
                    self.config.sample_rate = normalized.sample_rate
                    self.config.channels = normalized.channels
                    
                    logger.info(f"✅ [OUTPUT] Нормализованные параметры для \"{device_name}\":")
                    logger.info(f"   Sample Rate: {normalized.device_rate or 'N/A'} → {normalized.sample_rate} Hz")
                    logger.info(f"   Channels: {normalized.channels}")
                else:
                    # Fallback на конфиг если устройство не определено
                    self._normalized_params = OutputParams(
                        sample_rate=self.config.sample_rate,
                        channels=self.config.channels
                    )
                    logger.warning(f"⚠️ [OUTPUT] Устройство не определено, используем конфиг: {self.config.sample_rate} Hz, {self.config.channels} ch")
                
                # ✅ ШАГ 3: Создаем поток с нормализованными параметрами
                stream_config = {
                    'device': None,  # PortAudio выберет default
                    'channels': self.config.channels,
                    'dtype': self.config.dtype,
                    'samplerate': self.config.sample_rate,
                    'blocksize': self.config.buffer_size,
                    'callback': self._audio_callback
                }
                
                logger.info(f"🔍 [OUTPUT] Создаём поток для устройства: \"{device_name}\"")
                logger.info(f"   Параметры потока: {self.config.sample_rate} Hz, {self.config.channels} ch")
                
                # Создаем поток БЕЗ старта (lazy start)
                self._audio_stream = sd.OutputStream(**stream_config)
                self._stream_started = False
                
                logger.info("✅ Аудио поток создан с нормализованными параметрами")
                return True
                
        except Exception as e:
            logger.error(f"❌ Ошибка создания аудио потока: {e}")
            return False
    
    def _ensure_stream_started(self):
        """Убеждаемся что поток стартован"""
        with self._stream_lock:
            if self._audio_stream is not None and not self._stream_started:
                try:
                    self._audio_stream.start()
                    self._stream_started = True
                    logger.info("▶️ Аудио поток стартован")
                except Exception as e:
                    logger.error(f"❌ Ошибка старта аудио потока: {e}")
                    self._stream_broken.set()
    
    def _stop_audio_stream(self):
        """Остановка аудио потока"""
        try:
            with self._stream_lock:
                if self._audio_stream is not None:
                    if self._stream_started:
                        self._audio_stream.stop()
                    self._audio_stream.close()
                    self._audio_stream = None
                    self._stream_started = False
                    logger.info("🛑 Аудио поток остановлен")
        except Exception as e:
            logger.error(f"❌ Ошибка остановки аудио потока: {e}")
    
    def _audio_callback(self, outdata, frames, time_info, status):
        """
        Callback для воспроизведения аудио
        
        ✅ ФИКС 4: Обработка ошибок - ставим флаг _stream_broken
        ✅ ФИКС 5: Периодическая проверка смены устройства во время воспроизведения
        """
        try:
            # ✅ ПЕРИОДИЧЕСКАЯ ПРОВЕРКА УСТРОЙСТВА (каждые ~100 вызовов callback)
            # Это примерно раз в 1-2 секунды при 48kHz
            self._device_check_counter += 1
            if self._device_check_counter >= 100:
                self._device_check_counter = 0
                if self._check_device_changed_during_playback():
                    logger.warning("🔄 [OUTPUT] Устройство изменилось во время воспроизведения - помечаем поток для пересоздания")
                    self._stream_broken.set()
            
            if status:
                logger.warning(f"⚠️ Статус аудио потока: {status}")
                # Если статус содержит ошибку - помечаем поток как сломанный
                if status.input_underflow or status.output_underflow:
                    logger.error("❌ [OUTPUT] Underflow detected - поток сломан")
                    self._stream_broken.set()
                elif status.input_error or status.output_error:
                    logger.error("❌ [OUTPUT] Error detected - поток сломан")
                    self._stream_broken.set()
            
            # Получаем данные из буфера
            with self._buffer_lock:
                if len(self._audio_buffer) > 0:
                    data = self._audio_buffer.pop(0)
                else:
                    data = None
            
            # Формируем выходные данные
            if data is None or len(data) == 0:
                outdata[:] = 0
            else:
                # Убеждаемся что данные в правильной форме
                if data.ndim == 1:
                    data = data.reshape(-1, 1)
                
                # Копируем данные
                copy_frames = min(frames, data.shape[0])
                copy_channels = min(self.config.channels, data.shape[1])
                
                outdata[:copy_frames, :copy_channels] = data[:copy_frames, :copy_channels]
                
                # Заполняем остаток нулями
                if copy_frames < frames:
                    outdata[copy_frames:, :] = 0
                if copy_channels < self.config.channels:
                    outdata[:, copy_channels:] = 0
                
        except Exception as e:
            logger.error(f"❌ Ошибка в audio callback: {e}")
            self._stream_broken.set()
            outdata[:] = 0
    
    def wait_for_completion(self, timeout: float = 5.0) -> bool:
        """Ждать завершения воспроизведения"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            with self._buffer_lock:
                if len(self._audio_buffer) == 0:
                    # Даем время на финальную обработку
                    time.sleep(0.1)
                    return True
            time.sleep(0.1)
        return False
    
    def _on_device_changed_realtime(self, device_name: str, device_id: int):
        """
        Callback при смене устройства (вызывается из мониторинга в реальном времени)
        
        Args:
            device_name: Имя нового устройства
            device_id: ID нового устройства
        """
        logger.info("")
        logger.info("🔄 [REALTIME] Обнаружена смена устройства через мониторинг!")
        logger.info(f"   Новое устройство: \"{device_name}\" (ID={device_id})")
        logger.info("   Помечаю поток для пересоздания...")
        logger.info("")
        
        # Помечаем поток как сломанный - он будет пересоздан при следующем add_audio_data
        self._stream_broken.set()
        # Обновляем информацию об устройстве
        self._last_known_device_id = device_id
    
    def stop(self):
        """Остановка плеера"""
        # Останавливаем мониторинг если включен
        if self._device_monitor:
            self._device_monitor.stop_monitoring()
        
        self._stop_audio_stream()
        with self._buffer_lock:
            self._audio_buffer.clear()
        self.state = PlaybackState.STOPPED
        logger.info("🛑 Плеер остановлен")
    
    def _update_last_known_device(self):
        """Обновить информацию о последнем известном устройстве"""
        try:
            default_setting = sd.default.device
            if hasattr(default_setting, '__getitem__'):
                try:
                    self._last_known_device_id = default_setting[1]
                except (IndexError, TypeError):
                    self._last_known_device_id = None
        except Exception:
            self._last_known_device_id = None
    
    def _check_device_changed_during_playback(self) -> bool:
        """
        Проверяет изменилось ли устройство во время активного воспроизведения
        
        ⚠️ ПРОБЛЕМА: sd.default.device может не обновляться в реальном времени
        Решение: Используем имя устройства для сравнения, а не только ID
        
        Returns:
            True если устройство изменилось, False иначе
        """
        try:
            if self._last_known_device_id is None:
                # Первая проверка - просто запоминаем устройство
                self._update_last_known_device()
                return False
            
            # ✅ УЛУЧШЕНИЕ: Получаем текущее устройство и сравниваем по имени
            # Это более надежно, т.к. ID может не обновляться, но имя устройства может
            default_setting = sd.default.device
            if hasattr(default_setting, '__getitem__'):
                try:
                    current_device_id = default_setting[1]
                    current_device_info = sd.query_devices(current_device_id, 'output')
                    current_device_name = current_device_info.get('name', '') if current_device_info else ''
                    
                    # Получаем имя последнего известного устройства
                    last_device_info = sd.query_devices(self._last_known_device_id, 'output')
                    last_device_name = last_device_info.get('name', '') if last_device_info else ''
                    
                    # Сравниваем по ID И по имени (на случай если ID не обновился)
                    if current_device_id != self._last_known_device_id:
                        logger.info(f"🔄 [OUTPUT] Устройство изменилось по ID: {self._last_known_device_id} → {current_device_id}")
                        logger.info(f"   Старое: \"{last_device_name}\" → Новое: \"{current_device_name}\"")
                        self._last_known_device_id = current_device_id
                        return True
                    elif current_device_name and last_device_name and current_device_name != last_device_name:
                        # ID не изменился, но имя изменилось - возможно устройство переименовано или обновлено
                        logger.warning(f"⚠️ [OUTPUT] Имя устройства изменилось (ID тот же): \"{last_device_name}\" → \"{current_device_name}\"")
                        # Не считаем это сменой устройства, т.к. ID тот же
                except (IndexError, TypeError) as e:
                    logger.debug(f"⚠️ Ошибка получения устройства: {e}")
        except Exception as e:
            logger.debug(f"⚠️ Ошибка проверки устройства: {e}")
        
        return False
    
    def get_current_device_info(self) -> Optional[Dict[str, Any]]:
        """Получить информацию о текущем устройстве"""
        try:
            default_setting = sd.default.device
            if hasattr(default_setting, '__getitem__'):
                try:
                    output_device_id = default_setting[1]
                    device_info = sd.query_devices(output_device_id, 'output')
                    return {
                        'id': output_device_id,
                        'name': device_info.get('name', 'Unknown'),
                        'sample_rate': device_info.get('default_samplerate', 0),
                        'channels': device_info.get('max_output_channels', 0)
                    }
                except (IndexError, TypeError):
                    pass
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения информации об устройстве: {e}")
        return None

