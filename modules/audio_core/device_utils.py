"""
Централизованные утилиты для работы с аудио устройствами

Этот модуль содержит единые функции для:
- Определения типа устройства (Bluetooth, remote)
- Поиска device_id по имени
- Получения системного default устройства
- Классификации устройств (приоритет)
- Построения StreamConfig

Использование этих функций устраняет дублирование логики и обеспечивает согласованность.
"""

import logging
import sounddevice as sd
from typing import Optional, Tuple, Dict, Any
import subprocess
import json

logger = logging.getLogger(__name__)

# Импорт типов для обратной совместимости
try:
    from .legacy_compat import StreamConfig
except ImportError:
    StreamConfig = None
    logger.warning("⚠️ StreamConfig недоступен, некоторые функции могут не работать")


def is_bluetooth_device(name: str) -> bool:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Определяет, является ли устройство Bluetooth по имени
    
    Единая функция для всех модулей. Использует полный список ключевых слов.
    
    Args:
        name: Имя устройства
        
    Returns:
        True если устройство Bluetooth
    """
    if not name:
        return False
    lowered = name.lower()
    # ✅ ПОЛНЫЙ СПИСОК: включает все варианты для согласованности
    return any(keyword in lowered for keyword in (
        "bluetooth", 
        "airpods", 
        "airpod",  # На случай без 's'
        "beats", 
        "headset", 
        "earbud",
        "earbuds"  # На случай множественного числа
    ))


def is_remote_device(name: str) -> bool:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Определяет, является ли устройство remote (удалённым)
    
    Args:
        name: Имя устройства
        
    Returns:
        True если устройство remote
    """
    if not name:
        return False
    lowered = name.lower()
    return any(keyword in lowered for keyword in (
        "remote", 
        "virtual", 
        "loopback",
        "blackhole"  # Популярный виртуальный аудио драйвер для macOS
    ))


def classify_device(name: str, direction: str = "input") -> int:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Классифицирует устройство по приоритету
    
    Возвращает числовой приоритет:
    - 1: Обычное устройство (высший приоритет)
    - 2: Bluetooth устройство
    - 3: Remote/Virtual устройство (низший приоритет)
    
    Args:
        name: Имя устройства
        direction: Направление ("input" или "output")
        
    Returns:
        Приоритет устройства (1-3)
    """
    if not name:
        return 3  # Неизвестное устройство - низкий приоритет
    
    lowered = name.lower()
    
    if not is_bluetooth_device(name) and not is_remote_device(name):
        return 1  # Обычное устройство - высший приоритет
    if is_bluetooth_device(name):
        return 2  # Bluetooth устройство
    if is_remote_device(name):
        return 3  # Remote/Virtual устройство - низший приоритет
    
    return 3  # По умолчанию - низкий приоритет


def find_device_id_by_name(name: str, direction: str = "input") -> Optional[int]:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Находит PortAudio ID устройства по имени
    
    Args:
        name: Имя устройства
        direction: Направление ("input" или "output")
        
    Returns:
        PortAudio ID устройства или None если не найдено
    """
    if not name:
        return None
    
    try:
        all_devices = sd.query_devices()
        for idx, dev in enumerate(all_devices):
            # Проверяем направление
            if direction == "input":
                if dev.get('max_input_channels', 0) <= 0:
                    continue
            else:  # output
                if dev.get('max_output_channels', 0) <= 0:
                    continue
            
            # Сравниваем имя
            if dev.get('name', '') == name:
                return idx
        
        return None
    except Exception as e:
        logger.debug(f"⚠️ Ошибка поиска device_id по имени '{name}': {e}")
        return None


def get_system_default_device(direction: str = "input") -> Tuple[Optional[str], Optional[int]]:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Получает системное default устройство
    
    Приоритет источников:
    1. macOS API (SwitchAudioSource) - самый актуальный
    2. PortAudio sd.default.device - fallback
    
    Args:
        direction: Направление ("input" или "output")
        
    Returns:
        Tuple: (device_name, device_id) или (None, None) если не найдено
    """
    try:
        # ✅ ПРИОРИТЕТ 1: macOS API через SwitchAudioSource
        try:
            result = subprocess.run(
                ['SwitchAudioSource', '-c', '-t', direction, '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=2
            )
            
            if result.returncode == 0:
                device_info = json.loads(result.stdout.strip())
                device_name = device_info.get('name', '')
                
                if device_name:
                    # Ищем ID в PortAudio
                    device_id = find_device_id_by_name(device_name, direction)
                    if device_id is not None:
                        logger.debug(f"✅ [DEVICE_UTILS] Найдено через SwitchAudioSource: '{device_name}' (ID={device_id})")
                        return device_name, device_id
                    else:
                        logger.debug(f"⚠️ [DEVICE_UTILS] Устройство '{device_name}' найдено через SwitchAudioSource, но ID не найден в PortAudio")
                        return device_name, None
        except (subprocess.TimeoutExpired, subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError) as e:
            logger.debug(f"⚠️ [DEVICE_UTILS] SwitchAudioSource недоступен: {e}")
        
        # ✅ ПРИОРИТЕТ 2: PortAudio sd.default.device
        try:
            default_setting = sd.default.device
            device_id = None
            
            if hasattr(default_setting, '__getitem__'):
                try:
                    if direction == "input":
                        device_id = default_setting[0]  # INPUT устройство (индекс 0)
                    else:
                        device_id = default_setting[1] if len(default_setting) > 1 else default_setting[0]  # OUTPUT устройство
                except (IndexError, TypeError):
                    device_id = None
            
            if device_id is not None:
                # Получаем имя устройства по ID
                device_info = sd.query_devices(device_id, direction)
                if device_info:
                    device_name = device_info.get('name', 'Unknown')
                    logger.debug(f"✅ [DEVICE_UTILS] Найдено через PortAudio: '{device_name}' (ID={device_id})")
                    return device_name, device_id
        except Exception as e:
            logger.debug(f"⚠️ [DEVICE_UTILS] Ошибка получения через PortAudio: {e}")
        
        return None, None
        
    except Exception as e:
        logger.error(f"❌ [DEVICE_UTILS] Критическая ошибка получения системного default устройства: {e}", exc_info=True)
        return None, None


def build_stream_config(
    device_name: str,
    device_id: Optional[int],
    is_bluetooth: bool,
    direction: str,
    sample_rate: int = 48000,
    channels: int = 1,
    dtype: str = 'float32',
    blocksize: Optional[int] = None,
    latency: Optional[float] = None
) -> Optional[Any]:
    """
    ✅ ЦЕНТРАЛИЗОВАНО: Строит StreamConfig для устройства
    
    Args:
        device_name: Имя устройства
        device_id: PortAudio ID устройства (может быть None для BT)
        is_bluetooth: Является ли устройство Bluetooth
        direction: Направление ("input" или "output")
        sample_rate: Частота дискретизации
        channels: Количество каналов
        dtype: Тип данных
        blocksize: Размер блока (опционально)
        latency: Задержка (опционально)
        
    Returns:
        StreamConfig объект или None если StreamConfig недоступен
    """
    if StreamConfig is None:
        logger.warning("⚠️ [DEVICE_UTILS] StreamConfig недоступен, невозможно построить конфигурацию")
        return None
    
    # Для INPUT устройств используем целевую частоту 16000 для ASR
    if direction == "input":
        target_rate = 16000.0
    else:
        target_rate = float(sample_rate)
    
    return StreamConfig(
        device_id=device_id,
        device_name=device_name,
        samplerate=sample_rate,
        channels=channels,
        dtype=dtype,
        blocksize=blocksize,
        latency=latency,
        is_bluetooth=is_bluetooth
    )

