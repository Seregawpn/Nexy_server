"""
Stream Config Resolver - Решатель конфигурации аудио потока

✅ ФАЗА 3: Вынесен в отдельный класс для лучшей структуризации кода.
Принимает имя устройства, флаг BT, host_error_code и историю ошибок,
возвращает корректную конфигурацию потока.
"""

import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class StreamConfigResolver:
    """
    Решатель конфигурации аудио потока.
    
    ✅ ФАЗА 3: Отдельный класс для определения правильной конфигурации потока
    на основе типа устройства, истории ошибок и доступных параметров.
    """
    
    def __init__(
        self,
        default_sample_rate: int = 48000,
        default_channels: int = 2,
        default_dtype: str = 'int16',
        default_buffer_size: int = 512
    ):
        """
        Инициализация resolver
        
        Args:
            default_sample_rate: Частота дискретизации по умолчанию
            default_channels: Количество каналов по умолчанию
            default_dtype: Тип данных по умолчанию
            default_buffer_size: Размер буфера по умолчанию
        """
        self.default_sample_rate = default_sample_rate
        self.default_channels = default_channels
        self.default_dtype = default_dtype
        self.default_buffer_size = default_buffer_size
        
        # ✅ ФАЗА 3: Кэш ошибок для хранения "плохих" конфигураций
        self._device_error_cache: Dict[str, Dict[str, Any]] = {}
        self._error_cache_lock = None  # Будет установлен извне
        
        logger.debug(f"🔧 StreamConfigResolver создан (rate={default_sample_rate}Hz, channels={default_channels})")
    
    def set_error_cache(self, error_cache: Dict[str, Dict[str, Any]], lock: Any):
        """
        Устанавливает ссылку на кэш ошибок из SequentialSpeechPlayer
        
        Args:
            error_cache: Словарь с кэшем ошибок
            lock: Блокировка для thread-safe доступа
        """
        self._device_error_cache = error_cache
        self._error_cache_lock = lock
    
    def resolve_stream_config(
        self,
        device_name: str,
        is_bluetooth: bool,
        device_id: Optional[int],
        callback: Any,
        error_cache: Optional[Dict[str, Dict[str, Any]]] = None,
        error_cache_lock: Optional[Any] = None
    ) -> Dict[str, Any]:
        """
        Определяет конфигурацию потока на основе устройства и истории ошибок.
        
        ✅ ФАЗА 3: Полная логика resolver с учетом:
        - Типа устройства (BT/обычное)
        - Истории ошибок (кэш)
        - Доступных параметров
        
        Args:
            device_name: Имя устройства
            is_bluetooth: Является ли устройство Bluetooth
            device_id: PortAudio ID устройства (может быть None для BT)
            callback: Callback функция для потока
            error_cache: Кэш ошибок (опционально, если не установлен через set_error_cache)
            error_cache_lock: Блокировка для кэша (опционально)
        
        Returns:
            dict: Конфигурация потока (device, channels, samplerate, dtype, callback, ...)
        """
        # Используем переданный кэш или установленный через set_error_cache
        cache = error_cache if error_cache is not None else self._device_error_cache
        lock = error_cache_lock if error_cache_lock is not None else self._error_cache_lock
        
        # ✅ ФАЗА 3: Проверяем кэш ошибок перед созданием конфигурации
        if cache and lock:
            with lock:
                if device_name in cache:
                    cached = cache[device_name]
                    logger.info(f"💾 [OUTPUT] Используем кэшированную безопасную конфигурацию для \"{device_name}\"")
                    logger.info(f"   Причина: предыдущая ошибка {cached.get('error_code')}")
                    # Копируем безопасную конфигурацию и добавляем callback
                    safe_config = cached['safe_config'].copy()
                    safe_config['callback'] = callback
                    return safe_config
        
        # ✅ ФАЗА 3: Создаем конфигурацию на основе типа устройства
        if is_bluetooth:
            # ✅ ФИНАЛЬНОЕ РЕШЕНИЕ: Для BT устройств ВСЕГДА используем device=None
            # НИКОГДА не используем PortAudio ID для BT устройств - сразу device=None
            logger.info(f"💡 [OUTPUT] SwitchAudioSource → \"{device_name}\" (BT устройство)")
            logger.info(f"✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)")
            
            # channels обязателен, но blocksize/latency не задаем - пусть macOS/PortAudio выберут сами
            logger.info(f"🔧 [OUTPUT] BT устройство: используем channels={self.default_channels} (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)")
            return {
                'device': None,  # macOS сам выберет устройство
                'channels': self.default_channels,  # channels обязателен для sd.OutputStream
                'dtype': self.default_dtype,
                'samplerate': self.default_sample_rate,
                'callback': callback
                # НЕ задаем blocksize, latency - пусть macOS/PortAudio выберут сами
            }
        else:
            # Для обычных устройств используем все параметры
            logger.debug(f"🔧 [OUTPUT] Обычное устройство: используем все параметры (device={device_id}, channels={self.default_channels}, blocksize={self.default_buffer_size})")
            return {
                'device': device_id,
                'channels': self.default_channels,
                'dtype': self.default_dtype,
                'samplerate': self.default_sample_rate,
                'blocksize': self.default_buffer_size,
                'callback': callback
            }
    
    def cache_error_config(
        self,
        device_name: str,
        error_code: int,
        safe_config: Dict[str, Any],
        error_cache: Optional[Dict[str, Dict[str, Any]]] = None,
        error_cache_lock: Optional[Any] = None
    ):
        """
        Сохраняет "плохую" конфигурацию в кэш для будущего использования.
        
        ✅ ФАЗА 3: Сохранение конфигурации в кэш для предотвращения повторных ошибок
        
        Args:
            device_name: Имя устройства
            error_code: Код ошибки (-9986, -10851)
            safe_config: Безопасная конфигурация, которая сработала
            error_cache: Кэш ошибок (опционально)
            error_cache_lock: Блокировка для кэша (опционально)
        """
        cache = error_cache if error_cache is not None else self._device_error_cache
        lock = error_cache_lock if error_cache_lock is not None else self._error_cache_lock
        
        if cache and lock:
            import time
            with lock:
                # Удаляем callback из конфигурации (не сериализуется)
                config_to_cache = safe_config.copy()
                if 'callback' in config_to_cache:
                    del config_to_cache['callback']
                
                cache[device_name] = {
                    'error_code': error_code,
                    'safe_config': config_to_cache,
                    'timestamp': time.time()
                }
                logger.info(f"💾 [OUTPUT] Сохранена безопасная конфигурация для \"{device_name}\" (ошибка: {error_code})")



