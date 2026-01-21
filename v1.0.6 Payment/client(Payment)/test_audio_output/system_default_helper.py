"""
Helper для получения реального системного default OUTPUT устройства macOS

Использует системные команды macOS для обхода ограничений PortAudio
"""

import logging
import subprocess
import re
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


def get_system_default_output_via_switchaudio() -> Optional[Dict[str, Any]]:
    """
    Получить системный default OUTPUT через switchaudio-source (если доступен)
    
    Returns:
        Dict с информацией об устройстве или None
    """
    try:
        # Проверяем доступен ли switchaudio-source
        result = subprocess.run(
            ['which', 'switchaudio-source'],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        if result.returncode != 0:
            return None
        
        # Получаем текущее default устройство
        result = subprocess.run(
            ['switchaudio-source', '-c'],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        if result.returncode == 0:
            device_name = result.stdout.strip()
            if device_name:
                return {
                    'name': device_name,
                    'source': 'switchaudio-source'
                }
    except Exception as e:
        logger.debug(f"switchaudio-source недоступен: {e}")
    
    return None


def get_system_default_output_via_system_profiler() -> Optional[Dict[str, Any]]:
    """
    Получить системный default OUTPUT через system_profiler
    
    Returns:
        Dict с информацией об устройстве или None
    """
    try:
        result = subprocess.run(
            ['system_profiler', 'SPAudioDataType'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            output = result.stdout
            
            # Ищем строку с "Default Output Device: Yes"
            lines = output.split('\n')
            current_device = None
            
            for i, line in enumerate(lines):
                if 'Default Output Device: Yes' in line:
                    # Ищем имя устройства выше
                    for j in range(max(0, i-10), i):
                        if 'Output Source:' in lines[j]:
                            device_name = lines[j].split('Output Source:')[1].strip()
                            return {
                                'name': device_name,
                                'source': 'system_profiler'
                            }
                        elif ':' in lines[j] and 'Output' in lines[j]:
                            # Альтернативный формат
                            parts = lines[j].split(':')
                            if len(parts) > 1:
                                device_name = parts[-1].strip()
                                if device_name:
                                    return {
                                        'name': device_name,
                                        'source': 'system_profiler'
                                    }
    except Exception as e:
        logger.debug(f"Ошибка system_profiler: {e}")
    
    return None


def get_system_default_output_via_osascript() -> Optional[Dict[str, Any]]:
    """
    Получить системный default OUTPUT через AppleScript
    
    Returns:
        Dict с информацией об устройстве или None
    """
    try:
        script = '''
        tell application "System Events"
            tell process "System Preferences"
                -- Получаем информацию о звуке
            end tell
        end tell
        '''
        
        # Более простой способ через osascript
        script = '''
        tell application "System Events"
            set soundOutput to name of (first output device of (first audio device of (first sound device)))
            return soundOutput
        end tell
        '''
        
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=3
        )
        
        if result.returncode == 0:
            device_name = result.stdout.strip()
            if device_name and 'error' not in device_name.lower():
                return {
                    'name': device_name,
                    'source': 'osascript'
                }
    except Exception as e:
        logger.debug(f"Ошибка osascript: {e}")
    
    return None


def get_real_system_default_output() -> Optional[Dict[str, Any]]:
    """
    Получить реальное системное default OUTPUT устройство
    
    Пробует несколько методов:
    1. switchaudio-source (если установлен)
    2. system_profiler
    3. osascript
    
    Returns:
        Dict с информацией об устройстве или None
    """
    # Метод 1: switchaudio-source (самый надежный)
    device = get_system_default_output_via_switchaudio()
    if device:
        return device
    
    # Метод 2: system_profiler
    device = get_system_default_output_via_system_profiler()
    if device:
        return device
    
    # Метод 3: osascript
    device = get_system_default_output_via_osascript()
    if device:
        return device
    
    return None


def find_device_in_portaudio_by_name(device_name: str) -> Optional[int]:
    """
    Найти устройство в PortAudio по имени
    
    Args:
        device_name: Имя устройства для поиска
        
    Returns:
        device_id или None если не найдено
    """
    try:
        import sounddevice as sd
        
        devices = sd.query_devices()
        device_name_lower = device_name.lower()
        
        # Точное совпадение
        for i, dev in enumerate(devices):
            if dev.get('max_output_channels', 0) > 0:
                dev_name = dev.get('name', '').lower()
                if dev_name == device_name_lower:
                    return i
        
        # Частичное совпадение
        for i, dev in enumerate(devices):
            if dev.get('max_output_channels', 0) > 0:
                dev_name = dev.get('name', '').lower()
                if device_name_lower in dev_name or dev_name in device_name_lower:
                    return i
        
        # Поиск по ключевым словам
        keywords = device_name_lower.split()
        for i, dev in enumerate(devices):
            if dev.get('max_output_channels', 0) > 0:
                dev_name = dev.get('name', '').lower()
                if any(keyword in dev_name for keyword in keywords if len(keyword) > 3):
                    return i
                    
    except Exception as e:
        logger.debug(f"Ошибка поиска устройства: {e}")
    
    return None

