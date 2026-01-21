"""
Device Parameters Normalizer - Нормализация параметров аудио устройств

Приводит параметры любых устройств к внутреннему формату Nexy:
- INPUT → ASR: 16 kHz mono
- OUTPUT: максимум 2 канала, частота в заданном диапазоне
"""

import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass
import sounddevice as sd

logger = logging.getLogger(__name__)


@dataclass
class OutputParams:
    """Нормализованные параметры для OUTPUT устройства"""
    sample_rate: int      # Клампированный sample rate
    channels: int         # 1 или 2
    dtype: str = 'int16'  # Тип данных
    device_rate: Optional[int] = None  # Исходный rate устройства (для логирования)


@dataclass
class InputParams:
    """Нормализованные параметры для INPUT устройства"""
    device_rate: int      # Реальный rate устройства (после клампа)
    target_rate: int      # 16 kHz для ASR
    channels: int         # 1 (mono)
    dtype: str = 'float32'  # Тип данных для захвата


class DeviceParamsNormalizer:
    """
    Нормализует параметры устройств к внутреннему формату Nexy
    
    Правила:
    - OUTPUT: максимум 2 канала, sample rate в диапазоне [min_rate, max_rate]
    - INPUT: всегда 1 канал (mono), device_rate в диапазоне, target_rate = 16 kHz
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация нормализатора
        
        Args:
            config: Конфигурация с лимитами (если None - используются дефолты)
        """
        if config is None:
            config = {}
        
        # OUTPUT параметры
        self.output_min_rate = config.get('output_min_rate', 16000)
        self.output_max_rate = config.get('output_max_rate', 48000)
        self.output_default_rate = config.get('output_default_rate', 48000)
        self.output_max_channels = config.get('output_max_channels', 2)  # Максимум стерео
        
        # INPUT параметры
        self.input_min_rate = config.get('input_min_rate', 16000)
        self.input_max_rate = config.get('input_max_rate', 48000)
        self.input_default_rate = config.get('input_default_rate', 48000)
        self.asr_target_rate = config.get('asr_target_rate', 16000)  # Что ожидает ASR
        self.input_channels = 1  # Всегда mono для ASR
        
        logger.info(f"🔧 DeviceParamsNormalizer создан:")
        logger.info(f"   OUTPUT: rate [{self.output_min_rate}-{self.output_max_rate}], max_channels={self.output_max_channels}")
        logger.info(f"   INPUT: device_rate [{self.input_min_rate}-{self.input_max_rate}], target_rate={self.asr_target_rate}, channels={self.input_channels}")
    
    def select_output_params(self, device_info: Dict[str, Any]) -> OutputParams:
        """
        Нормализует параметры OUTPUT устройства
        
        Алгоритм:
        1. Получаем device_rate и max_channels от устройства
        2. Клампим sample_rate в диапазон [min_rate, max_rate]
        3. Ограничиваем channels до 1-2
        4. Возвращаем нормализованные параметры
        
        Args:
            device_info: Информация об устройстве от sd.query_devices()
            
        Returns:
            OutputParams с нормализованными параметрами
        """
        # Шаг 1: Получаем параметры устройства
        device_rate_raw = device_info.get('default_samplerate', 0)
        device_max_channels = device_info.get('max_output_channels', 0)
        device_name = device_info.get('name', 'Unknown')
        
        # Шаг 2: Нормализуем sample_rate
        if device_rate_raw <= 0:
            # Кривое значение → fallback
            output_rate = self.output_default_rate
            logger.warning(f"⚠️ [OUTPUT] Устройство \"{device_name}\" имеет некорректный sample_rate ({device_rate_raw}), используем fallback: {output_rate} Hz")
        elif device_rate_raw < self.output_min_rate:
            # Слишком низкая частота → поднимаем до минимума
            output_rate = self.output_min_rate
            logger.info(f"🔧 [OUTPUT] Устройство \"{device_name}\" имеет низкий rate ({device_rate_raw} Hz), поднимаем до {output_rate} Hz")
        elif device_rate_raw > self.output_max_rate:
            # Слишком высокая частота → ограничиваем максимумом
            output_rate = self.output_max_rate
            logger.info(f"🔧 [OUTPUT] Устройство \"{device_name}\" имеет высокий rate ({device_rate_raw} Hz), ограничиваем до {output_rate} Hz")
        else:
            # В допустимом диапазоне → используем как есть
            output_rate = int(device_rate_raw)
        
        # Шаг 3: Нормализуем channels
        if device_max_channels <= 0:
            # Кривое значение → fallback на стерео
            effective_channels = 2
            logger.warning(f"⚠️ [OUTPUT] Устройство \"{device_name}\" имеет некорректное количество каналов ({device_max_channels}), используем fallback: {effective_channels}")
        elif device_max_channels == 1:
            # Моно устройство
            effective_channels = 1
        else:
            # Многоканальное устройство → ограничиваем до стерео
            effective_channels = min(device_max_channels, self.output_max_channels)
            if device_max_channels > self.output_max_channels:
                logger.info(f"🔧 [OUTPUT] Устройство \"{device_name}\" имеет {device_max_channels} каналов, ограничиваем до {effective_channels}")
        
        logger.debug(f"✅ [OUTPUT] Нормализовано: \"{device_name}\" → {output_rate} Hz, {effective_channels} ch")
        
        return OutputParams(
            sample_rate=output_rate,
            channels=effective_channels,
            device_rate=int(device_rate_raw) if device_rate_raw > 0 else None
        )
    
    def select_input_params(self, device_info: Dict[str, Any]) -> InputParams:
        """
        Нормализует параметры INPUT устройства
        
        Алгоритм:
        1. Получаем device_rate и max_channels от устройства
        2. Клампим device_rate в диапазон [min_rate, max_rate]
        3. Всегда используем 1 канал (mono) для ASR
        4. target_rate всегда = 16 kHz (что ожидает ASR)
        
        Args:
            device_info: Информация об устройстве от sd.query_devices()
            
        Returns:
            InputParams с нормализованными параметрами
        """
        # Шаг 1: Получаем параметры устройства
        device_rate_raw = device_info.get('default_samplerate', 0)
        device_max_channels = device_info.get('max_input_channels', 0)
        device_name = device_info.get('name', 'Unknown')
        
        # Шаг 2: Нормализуем device_rate
        if device_rate_raw <= 0:
            # Кривое значение → fallback
            device_rate = self.input_default_rate
            logger.warning(f"⚠️ [INPUT] Устройство \"{device_name}\" имеет некорректный sample_rate ({device_rate_raw}), используем fallback: {device_rate} Hz")
        elif device_rate_raw < self.input_min_rate:
            # Слишком низкая частота → поднимаем до минимума
            device_rate = self.input_min_rate
            logger.info(f"🔧 [INPUT] Устройство \"{device_name}\" имеет низкий rate ({device_rate_raw} Hz), поднимаем до {device_rate} Hz")
        elif device_rate_raw > self.input_max_rate:
            # Слишком высокая частота → ограничиваем максимумом
            device_rate = self.input_max_rate
            logger.info(f"🔧 [INPUT] Устройство \"{device_name}\" имеет высокий rate ({device_rate_raw} Hz), ограничиваем до {device_rate} Hz")
        else:
            # В допустимом диапазоне → используем как есть
            device_rate = int(device_rate_raw)
        
        # Шаг 3: Проверяем каналы (для логирования)
        if device_max_channels <= 0:
            logger.warning(f"⚠️ [INPUT] Устройство \"{device_name}\" имеет некорректное количество каналов ({device_max_channels})")
        elif device_max_channels > 1:
            logger.debug(f"🔧 [INPUT] Устройство \"{device_name}\" имеет {device_max_channels} каналов, используем только 1 (mono для ASR)")
        
        # Всегда используем 1 канал для ASR
        effective_channels = 1
        
        logger.debug(f"✅ [INPUT] Нормализовано: \"{device_name}\" → device_rate={device_rate} Hz, target_rate={self.asr_target_rate} Hz, {effective_channels} ch")
        
        return InputParams(
            device_rate=device_rate,
            target_rate=self.asr_target_rate,
            channels=effective_channels
        )
    
    def normalize_output_for_device(self, device_id: Optional[int] = None) -> Optional[OutputParams]:
        """
        Получить нормализованные параметры для OUTPUT устройства
        
        Args:
            device_id: ID устройства (None = default)
            
        Returns:
            OutputParams или None если устройство недоступно
        """
        try:
            if device_id is None:
                # Получаем default устройство
                default = sd.default.device
                if hasattr(default, '__getitem__'):
                    try:
                        device_id = default[1]
                    except (IndexError, TypeError):
                        return None
            
            device_info = sd.query_devices(device_id, 'output')
            return self.select_output_params(device_info)
        except Exception as e:
            logger.error(f"❌ Ошибка нормализации OUTPUT параметров: {e}")
            return None
    
    def normalize_input_for_device(self, device_id: Optional[int] = None) -> Optional[InputParams]:
        """
        Получить нормализованные параметры для INPUT устройства
        
        Args:
            device_id: ID устройства (None = default)
            
        Returns:
            InputParams или None если устройство недоступно
        """
        try:
            if device_id is None:
                # Получаем default устройство
                default = sd.default.device
                if hasattr(default, '__getitem__'):
                    try:
                        device_id = default[0]
                    except (IndexError, TypeError):
                        return None
            
            device_info = sd.query_devices(device_id, 'input')
            return self.select_input_params(device_info)
        except Exception as e:
            logger.error(f"❌ Ошибка нормализации INPUT параметров: {e}")
            return None
    
    def normalize_device_info(self, device_info: Dict[str, Any], device_type: str = "input") -> Optional[Dict[str, Any]]:
        """
        Helper: Преобразовать device_info в нормализованные параметры
        
        ✅ УЛУЧШЕНИЕ: Добавлен helper метод для удобного преобразования
        
        Args:
            device_info: Информация об устройстве от sd.query_devices()
            device_type: "input" или "output"
            
        Returns:
            Dict с нормализованными параметрами или None
        """
        try:
            device_name = device_info.get('name', 'Unknown')
            device_id = device_info.get('index', -1)
            
            if device_type == "input":
                params = self.select_input_params(device_info)
                return {
                    'name': device_name,
                    'id': device_id,
                    'device_rate': params.device_rate,
                    'target_rate': params.target_rate,
                    'channels': params.channels,
                    'dtype': params.dtype
                }
            else:
                params = self.select_output_params(device_info)
                return {
                    'name': device_name,
                    'id': device_id,
                    'sample_rate': params.sample_rate,
                    'channels': params.channels,
                    'dtype': params.dtype,
                    'device_rate': params.device_rate
                }
        except Exception as e:
            logger.error(f"❌ Ошибка нормализации device_info: {e}")
            return None
    
    def is_bluetooth_device(self, device_name: str) -> bool:
        """Проверка является ли устройство Bluetooth"""
        lowered = (device_name or "").lower()
        return any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
    
    def get_bluetooth_heuristics(self, device_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Эвристики для Bluetooth устройств
        
        Returns:
            Dict с рекомендациями для BT устройств
        """
        device_name = device_info.get('name', '')
        device_rate = device_info.get('default_samplerate', 0)
        
        is_bt = self.is_bluetooth_device(device_name)
        
        result = {
            'is_bluetooth': is_bt,
            'profile_type': 'unknown',
            'recommended_channels': None,
            'quality_warning': False
        }
        
        if is_bt:
            if device_rate <= 24000:
                result['profile_type'] = 'low_band'  # HFP или низкокачественный A2DP
                result['recommended_channels'] = 1  # Моно для низкого битрейта
                result['quality_warning'] = True
                logger.info(f"🔧 [BT] Устройство \"{device_name}\" использует low-band профиль ({device_rate} Hz) → рекомендуем mono")
            elif device_rate >= 44100:
                result['profile_type'] = 'high_quality'  # A2DP высокого качества
                result['recommended_channels'] = 2  # Стерео
            else:
                result['profile_type'] = 'standard'  # Стандартный A2DP
                result['recommended_channels'] = 2
        
        return result

