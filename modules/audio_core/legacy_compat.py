"""
Временные заглушки для обратной совместимости со старой архитектурой

TODO: Удалить после миграции SpeechRecognizer и SequentialSpeechPlayer на новую архитектуру
"""

import logging
from typing import Optional, Dict, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)

# Временные заглушки для обратной совместимости
# Импортируем только типы, чтобы избежать циклических импортов
try:
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from modules.audio_core.stream_managers import OutputStreamManager, InputStreamManager
        from modules.audio_core.types import DeviceDescriptor
    else:
        # Ленивая загрузка для избежания циклических импортов
        OutputStreamManager = None
        InputStreamManager = None
        DeviceDescriptor = None
except ImportError:
    OutputStreamManager = None
    InputStreamManager = None
    DeviceDescriptor = None


@dataclass
class StreamConfig:
    """Временная заглушка StreamConfig для обратной совместимости"""
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    samplerate: int = 48000
    channels: int = 1
    dtype: str = 'int16'
    blocksize: Optional[int] = None
    latency: Optional[float] = None
    callback: Optional[Any] = None
    is_bluetooth: bool = False


@dataclass
class StreamOperationResult:
    """Временная заглушка StreamOperationResult для обратной совместимости"""
    success: bool
    stream: Optional[Any] = None
    error_code: Optional[int] = None
    error_message: Optional[str] = None
    attempt: int = 1


class AudioStreamManager:
    """
    Временный адаптер для обратной совместимости со старым async API
    
    TODO: Удалить после миграции на новую архитектуру (OutputStreamManager/InputStreamManager)
    """
    
    def __init__(self, stream_type: str = "output"):
        """
        Инициализация адаптера
        
        Args:
            stream_type: Тип потока ("input" или "output")
        """
        self.stream_type = stream_type
        self._stream_type = stream_type
        
        # Ленивая загрузка для избежания циклических импортов
        self._manager = None
        self._stream_type = stream_type
        
        # Для обратной совместимости со старым API
        self._current_stream = None
        self._close_delay_bt = 2.5
        self._close_delay_normal = 0.3
        
        # Безопасное получение имени класса для предупреждения
        manager_name = "InputStreamManager" if stream_type == "input" else "OutputStreamManager"
        logger.warning(
            f"⚠️ AudioStreamManager используется как временный адаптер. "
            f"Мигрируйте на {manager_name} из новой архитектуры."
        )
    
    def _get_manager(self):
        """Ленивая загрузка менеджера"""
        if self._manager is None:
            try:
                from modules.audio_core.stream_managers import OutputStreamManager, InputStreamManager
                from modules.audio_core.types import DeviceDescriptor as DD
                if self._stream_type == "input":
                    self._manager = InputStreamManager()
                else:
                    self._manager = OutputStreamManager()
                return self._manager, DD
            except ImportError:
                return None, None
        else:
            from modules.audio_core.types import DeviceDescriptor as DD
            return self._manager, DD
    
    async def create_stream(
        self,
        config: StreamConfig,
        max_retries: int = 5
    ) -> StreamOperationResult:
        """
        Создание потока (async API для обратной совместимости)
        
        TODO: Мигрировать на синхронный API новой архитектуры
        """
        manager, DeviceDescriptor = self._get_manager()
        if not manager:
            return StreamOperationResult(
                success=False,
                error_message="Stream manager недоступен (миграция на новую архитектуру)"
            )
        
        try:
            # Преобразуем StreamConfig в DeviceDescriptor
            device_desc = DeviceDescriptor(
                uid=config.device_name or "unknown",
                name=config.device_name or "Unknown",
                latency=config.latency or 0.01,
                blocksize=config.blocksize or 0,
                sample_rate=float(config.samplerate),
                is_bluetooth=config.is_bluetooth,
                is_input=(self._stream_type == "input"),
                device_id=config.device_id
            )
            
            # Используем синхронный API новой архитектуры
            success = manager._open(device_desc, config.callback)
            
            if success:
                stream = manager._context.stream
                self._current_stream = stream
                return StreamOperationResult(success=True, stream=stream, attempt=1)
            else:
                return StreamOperationResult(
                    success=False,
                    error_message="Не удалось создать поток"
                )
                
        except Exception as e:
            logger.error(f"❌ Ошибка создания потока: {e}", exc_info=True)
            return StreamOperationResult(
                success=False,
                error_message=str(e)
            )
    
    async def close_stream(self, stream: Any, is_bluetooth: bool = False) -> bool:
        """
        Закрытие потока (async API для обратной совместимости)
        
        TODO: Мигрировать на синхронный API новой архитектуры
        """
        manager, _ = self._get_manager()
        if not manager:
            logger.debug("⚠️ AudioStreamManager: manager не инициализирован, пропускаем закрытие")
            return False
        
        try:
            # Выполняем закрытие в отдельном потоке, чтобы не блокировать async контекст
            import asyncio
            import concurrent.futures
            
            loop = asyncio.get_event_loop()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = loop.run_in_executor(executor, manager.close)
                # Ожидаем закрытие с таймаутом (5 секунд)
                try:
                    await asyncio.wait_for(future, timeout=5.0)
                except asyncio.TimeoutError:
                    logger.debug("⚠️ Таймаут закрытия потока через AudioStreamManager (5.0s), продолжаем")
                    # Продолжаем выполнение даже при таймауте
                    return False
            
            self._current_stream = None
            return True
        except Exception as e:
            error_msg = str(e) if e and str(e) else f"{type(e).__name__} (без сообщения)"
            logger.debug(f"⚠️ Ошибка закрытия потока через AudioStreamManager: {error_msg}")
            # Не логируем как error, так как это может быть нормальной ситуацией (поток уже закрыт)
            return False
    
    async def switch_device(
        self,
        old_stream: Optional[Any],
        config: StreamConfig,
        callback: Optional[Any] = None,
        is_bluetooth: bool = False
    ) -> StreamOperationResult:
        """
        Переключение устройства (async API для обратной совместимости)
        
        TODO: Мигрировать на синхронный API новой архитектуры
        """
        manager, DeviceDescriptor = self._get_manager()
        if not manager:
            return StreamOperationResult(
                success=False,
                error_message="Stream manager недоступен (миграция на новую архитектуру)"
            )
        
        try:
            # Преобразуем StreamConfig в DeviceDescriptor
            device_desc = DeviceDescriptor(
                uid=config.device_name or "unknown",
                name=config.device_name or "Unknown",
                latency=config.latency or 0.01,
                blocksize=config.blocksize or 0,
                sample_rate=float(config.samplerate),
                is_bluetooth=config.is_bluetooth,
                is_input=(self._stream_type == "input"),
                device_id=config.device_id
            )
            
            # Используем синхронный API новой архитектуры
            success = manager.switch_device(device_desc, callback)
            
            if success:
                stream = manager._context.stream
                self._current_stream = stream
                return StreamOperationResult(success=True, stream=stream, attempt=1)
            else:
                return StreamOperationResult(
                    success=False,
                    error_message="Не удалось переключить устройство"
                )
                
        except Exception as e:
            logger.error(f"❌ Ошибка переключения устройства: {e}", exc_info=True)
            return StreamOperationResult(
                success=False,
                error_message=str(e)
            )


# Временные заглушки для DevicePolicy и DeviceParamsNormalizer
class DevicePolicy:
    """Временная заглушка DevicePolicy для обратной совместимости"""
    
    @staticmethod
    def get_policy(is_bluetooth: bool = False, device_name: Optional[str] = None) -> 'DevicePolicyConfig':
        """Получить политику устройства"""
        return DevicePolicyConfig(
            max_retries=3 if is_bluetooth else 2,
            operation_timeout=15.0 if is_bluetooth else 10.0
        )


@dataclass
class DevicePolicyConfig:
    """Временная заглушка DevicePolicyConfig"""
    max_retries: int = 2
    operation_timeout: float = 10.0


class DeviceParamsNormalizer:
    """Временная заглушка DeviceParamsNormalizer для обратной совместимости"""
    
    def __init__(self, config: Dict[str, Any]):
        """Инициализация нормализатора"""
        self.config = config
        logger.warning("⚠️ DeviceParamsNormalizer используется как временная заглушка")
    
    def is_bluetooth_device(self, device_name: str) -> bool:
        """
        Проверяет, является ли устройство Bluetooth по имени
        
        Args:
            device_name: Имя устройства
            
        Returns:
            True если устройство Bluetooth
        """
        if not device_name:
            return False
        lowered = device_name.lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpods", "airpod", "beats", "headset", "earbud"))
    
    def select_output_params(self, device_info: Dict[str, Any]) -> 'OutputParams':
        """
        Выбирает параметры вывода для устройства
        
        Args:
            device_info: Информация об устройстве
            
        Returns:
            OutputParams с параметрами устройства
        """
        # Получаем исходную частоту устройства
        device_rate = device_info.get('default_samplerate', 48000.0)
        # Возвращаем параметры из device_info или дефолтные
        return OutputParams(
            device_id=device_info.get('index'),
            device_name=device_info.get('name', 'Unknown'),
            sample_rate=device_rate,
            channels=device_info.get('max_output_channels', 2),
            latency=device_info.get('default_low_output_latency', 0.01),
            blocksize=device_info.get('default_buffer_size', 512),
            device_rate=device_rate  # Исходная частота устройства
        )
    
    def select_input_params(self, device_info: Dict[str, Any]) -> 'InputParams':
        """
        Выбирает параметры ввода для устройства
        
        Args:
            device_info: Информация об устройстве
            
        Returns:
            InputParams с параметрами устройства
        """
        # Получаем исходную частоту устройства
        device_rate = device_info.get('default_samplerate', 48000.0)
        # Возвращаем параметры из device_info или дефолтные
        return InputParams(
            device_id=device_info.get('index'),
            device_name=device_info.get('name', 'Unknown'),
            sample_rate=device_rate,
            channels=device_info.get('max_input_channels', 1),
            latency=device_info.get('default_low_input_latency', 0.01),
            blocksize=device_info.get('default_buffer_size', 512),
            device_rate=device_rate,  # Исходная частота устройства
            target_rate=16000.0  # Целевая частота для ASR (обычно 16kHz)
        )
    
    def normalize_device_info(self, device_info: Dict[str, Any], device_type: str = 'output') -> Dict[str, Any]:
        """
        Нормализует информацию об устройстве
        
        Args:
            device_info: Информация об устройстве
            device_type: Тип устройства ('input' или 'output')
            
        Returns:
            Нормализованная информация об устройстве
        """
        # Просто возвращаем device_info как есть (заглушка)
        return device_info


@dataclass
class OutputParams:
    """Временная заглушка OutputParams"""
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    sample_rate: float = 48000.0
    samplerate: int = 48000  # Алиас для обратной совместимости
    channels: int = 1
    dtype: str = 'int16'
    latency: float = 0.01
    blocksize: int = 512
    device_rate: Optional[float] = None  # Исходная частота устройства
    
    def __post_init__(self):
        """Синхронизация samplerate и sample_rate"""
        if self.samplerate != int(self.sample_rate):
            self.samplerate = int(self.sample_rate)


@dataclass
class InputParams:
    """Временная заглушка InputParams"""
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    sample_rate: float = 48000.0
    samplerate: int = 48000  # Алиас для обратной совместимости
    channels: int = 1
    dtype: str = 'int16'
    latency: float = 0.01
    blocksize: int = 512
    device_rate: Optional[float] = None  # Исходная частота устройства
    target_rate: Optional[float] = 16000.0  # Целевая частота для ASR (обычно 16kHz)
    
    def __post_init__(self):
        """Синхронизация samplerate и sample_rate"""
        if self.samplerate != int(self.sample_rate):
            self.samplerate = int(self.sample_rate)

