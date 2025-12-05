"""
CoreAudioDeviceBus - Нативный слой CoreAudio

Подключается к Swift/ObjC helper'у, который подписывает AudioObjectAddPropertyListener,
вызывает callback с сырым словарём и умеет list_devices() для polling.
"""

import logging
import platform
import sounddevice as sd
from typing import Optional, Callable, Dict, Any, List
from .types import DeviceDescriptor

logger = logging.getLogger(__name__)

# Импорт существующего CoreAudioManager
try:
    import sys
    import os
    # Добавляем путь к модулю speech_playback
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    from modules.speech_playback.macos.core_audio import CoreAudioManager
    CORE_AUDIO_MANAGER_AVAILABLE = True
except ImportError as e:
    CORE_AUDIO_MANAGER_AVAILABLE = False
    CoreAudioManager = None
    logger.warning(f"⚠️ CoreAudioManager недоступен: {e}")


class CoreAudioDeviceBus:
    """
    Шина устройств CoreAudio
    
    Обёртка над CoreAudioManager для работы с нотификациями и списком устройств.
    """
    
    def __init__(self):
        """Инициализация шины"""
        self._is_macos = platform.system() == "Darwin"
        self._core_audio_manager: Optional[CoreAudioManager] = None
        
        if CORE_AUDIO_MANAGER_AVAILABLE and self._is_macos:
            try:
                self._core_audio_manager = CoreAudioManager()
                if not self._core_audio_manager.initialize():
                    logger.warning("⚠️ Не удалось инициализировать CoreAudioManager")
                    self._core_audio_manager = None
            except Exception as e:
                logger.error(f"❌ Ошибка создания CoreAudioManager: {e}", exc_info=True)
                self._core_audio_manager = None
        
        logger.info(f"CoreAudioDeviceBus создан (macOS: {self._is_macos}, CoreAudio: {self._core_audio_manager is not None})")
    
    def subscribe_raw_events(self, callback: Callable[[Dict[str, Any]], None], direction: str = "output") -> bool:
        """
        Подписывается на сырые события CoreAudio
        
        Args:
            callback: Функция, вызываемая при смене устройства (получает сырой словарь)
            direction: Направление устройства ("input" или "output")
            
        Returns:
            True если подписка успешна, False иначе
        """
        if not self._core_audio_manager:
            logger.debug("⚠️ CoreAudioManager недоступен, подписка невозможна")
            return False
        
        def wrapped_callback():
            """Обёртка callback для CoreAudioManager"""
            try:
                # Получаем информацию о текущем устройстве
                device_info = self._get_current_device_info(direction)
                if device_info:
                    callback(device_info)
            except Exception as e:
                logger.error(f"❌ Ошибка в callback CoreAudioDeviceBus: {e}", exc_info=True)
        
        device_type = "input" if direction == "input" else "output"
        success = self._core_audio_manager.start_device_notifications(
            wrapped_callback,
            device_type=device_type
        )
        
        if success:
            logger.info(f"✅ Подписка на {direction} нотификации CoreAudio успешна")
        else:
            logger.warning(f"⚠️ Не удалось подписаться на {direction} нотификации CoreAudio")
        
        return success
    
    def list_devices(self, direction: str = "output") -> List[Dict[str, Any]]:
        """
        Получает список устройств для polling
        
        Args:
            direction: Направление устройства ("input" или "output")
            
        Returns:
            Список словарей с информацией об устройствах
        """
        try:
            devices = sd.query_devices()
            result = []
            
            for idx, device in enumerate(devices):
                is_input = device['max_input_channels'] > 0
                is_output = device['max_output_channels'] > 0
                
                if direction == "input" and not is_input:
                    continue
                if direction == "output" and not is_output:
                    continue
                
                # Определяем, является ли устройство Bluetooth
                is_bluetooth = "bluetooth" in device['name'].lower() or "airpods" in device['name'].lower()
                
                device_info = {
                    'uid': str(device.get('name', f'device_{idx}')),
                    'name': device.get('name', 'Unknown'),
                    'device_id': idx,
                    'latency': device.get('default_low_input_latency', 0.0) if is_input else device.get('default_low_output_latency', 0.0),
                    'blocksize': device.get('default_buffer_size', 0),
                    'sample_rate': device.get('default_samplerate', 48000.0),
                    'is_bluetooth': is_bluetooth,
                    'is_input': is_input,
                }
                
                result.append(device_info)
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения списка устройств: {e}", exc_info=True)
            return []
    
    def get_default_device(self, direction: str = "output") -> Optional[Dict[str, Any]]:
        """
        Получает информацию о дефолтном устройстве
        
        Args:
            direction: Направление устройства ("input" или "output")
            
        Returns:
            Словарь с информацией об устройстве или None
        """
        return self._get_current_device_info(direction)
    
    def _get_current_device_info(self, direction: str) -> Optional[Dict[str, Any]]:
        """
        Получает информацию о текущем устройстве
        
        ✅ УЛУЧШЕННАЯ ЛОГИКА:
        1. Сначала пробуем получить через macOS API (SwitchAudioSource) - актуальное устройство
        2. Находим ID устройства по имени в PortAudio
        3. Если не работает, используем sd.default.device как fallback
        
        Args:
            direction: Направление устройства ("input" или "output")
            
        Returns:
            Словарь с информацией об устройстве или None
        """
        try:
            # ✅ ПРИОРИТЕТ 1: Получаем через macOS API (SwitchAudioSource) - актуальное устройство
            device_name_from_macos = self._get_device_name_via_switchaudio(direction)
            
            if device_name_from_macos:
                # Находим ID устройства по имени в PortAudio
                device_id = self._find_device_id_by_name(device_name_from_macos, direction)
                
                if device_id is not None:
                    # Получаем полную информацию об устройстве
                    device_info = sd.query_devices(device_id)
                    if device_info:
                        is_input = device_info['max_input_channels'] > 0
                        is_bluetooth = "bluetooth" in device_name_from_macos.lower() or "airpods" in device_name_from_macos.lower()
                        
                        logger.debug(
                            f"🔍 [BUS] {direction.upper()}: обнаружено устройство через SwitchAudioSource \"{device_name_from_macos}\" "
                            f"(ID={device_id}, BT={is_bluetooth})"
                        )
                        
                        return {
                            'uid': str(device_name_from_macos),
                            'name': device_name_from_macos,
                            'device_id': device_id,
                            'latency': device_info.get('default_low_input_latency', 0.0) if is_input else device_info.get('default_low_output_latency', 0.0),
                            'blocksize': device_info.get('default_buffer_size', 0),
                            'sample_rate': device_info.get('default_samplerate', 48000.0),
                            'is_bluetooth': is_bluetooth,
                            'is_input': is_input,
                        }
                    else:
                        logger.debug(f"🔍 [BUS] {direction.upper()}: устройство \"{device_name_from_macos}\" найдено по имени, но не найдено в PortAudio")
                else:
                    # BT устройство может не иметь PortAudio ID
                    is_bluetooth = "bluetooth" in device_name_from_macos.lower() or "airpods" in device_name_from_macos.lower()
                    if is_bluetooth:
                        logger.debug(
                            f"🔍 [BUS] {direction.upper()}: BT устройство \"{device_name_from_macos}\" (ID=None, BT=True)"
                        )
                        return {
                            'uid': str(device_name_from_macos),
                            'name': device_name_from_macos,
                            'device_id': None,  # BT устройства могут не иметь PortAudio ID
                            'latency': 0.0,
                            'blocksize': 0,
                            'sample_rate': 48000.0,
                            'is_bluetooth': True,
                            'is_input': direction == "input",
                        }
            
            # ✅ FALLBACK: Используем PortAudio default device
            if direction == "input":
                default_device_id = sd.default.device[0]  # (input, output)
            else:
                default_device_id = sd.default.device[1]  # (input, output)
            
            if default_device_id is None:
                logger.debug(f"🔍 [BUS] {direction.upper()}: default_device_id=None (устройство не найдено)")
                return None
            
            # Получаем информацию об устройстве
            default_device = sd.query_devices(default_device_id)
            
            if default_device is None:
                logger.debug(f"🔍 [BUS] {direction.upper()}: устройство с ID={default_device_id} не найдено в PortAudio")
                return None
            
            device_name = default_device.get('name', 'Unknown')
            is_input = default_device['max_input_channels'] > 0
            is_bluetooth = "bluetooth" in device_name.lower() or "airpods" in device_name.lower()
            
            # ✅ ДИАГНОСТИКА: Логируем обнаруженное устройство
            logger.debug(
                f"🔍 [BUS] {direction.upper()}: обнаружено устройство через PortAudio fallback \"{device_name}\" "
                f"(ID={default_device_id}, BT={is_bluetooth})"
            )
            
            return {
                'uid': str(device_name),
                'name': device_name,
                'device_id': default_device_id,
                'latency': default_device.get('default_low_input_latency', 0.0) if is_input else default_device.get('default_low_output_latency', 0.0),
                'blocksize': default_device.get('default_buffer_size', 0),
                'sample_rate': default_device.get('default_samplerate', 48000.0),
                'is_bluetooth': is_bluetooth,
                'is_input': is_input,
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения информации об устройстве ({direction}): {e}", exc_info=True)
            return None
    
    def _get_device_name_via_switchaudio(self, direction: str) -> Optional[str]:
        """
        Получает имя текущего default устройства через macOS API (SwitchAudioSource)
        
        Args:
            direction: Направление устройства ("input" или "output")
            
        Returns:
            Имя устройства или None если не удалось определить
        """
        try:
            import subprocess
            import json
            import shutil
            
            # Проверяем доступность SwitchAudioSource
            switch_audio_source_path = shutil.which('SwitchAudioSource')
            if not switch_audio_source_path:
                logger.debug(f"🔍 [BUS] SwitchAudioSource не найден в PATH для {direction}")
                return None
            
            # Получаем текущее default устройство
            result = subprocess.run(
                ['SwitchAudioSource', '-c', '-t', direction, '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                device_info = json.loads(result.stdout.strip())
                device_name = device_info.get('name', '')
                if device_name:
                    logger.debug(f"🔍 [BUS] {direction.upper()}: macOS default через SwitchAudioSource: \"{device_name}\"")
                    return device_name
            else:
                logger.debug(f"🔍 [BUS] SwitchAudioSource вернул код ошибки {result.returncode} для {direction}")
                
        except Exception as e:
            logger.debug(f"🔍 [BUS] Ошибка получения имени через SwitchAudioSource для {direction}: {e}")
        
        return None
    
    def _find_device_id_by_name(self, device_name: str, direction: str) -> Optional[int]:
        """
        Находит PortAudio device ID по имени устройства
        
        Args:
            device_name: Имя устройства
            direction: Направление устройства ("input" или "output")
            
        Returns:
            PortAudio device ID или None если не найдено
        """
        try:
            all_devices = sd.query_devices()
            
            for idx, device in enumerate(all_devices):
                if not isinstance(device, dict):
                    continue
                
                # Проверяем направление
                if direction == "input":
                    if device.get('max_input_channels', 0) == 0:
                        continue
                else:
                    if device.get('max_output_channels', 0) == 0:
                        continue
                
                # Сравниваем имена (точное совпадение или case-insensitive)
                device_name_in_list = device.get('name', '')
                if device_name_in_list == device_name or device_name_in_list.lower() == device_name.lower():
                    logger.debug(f"🔍 [BUS] Найден PortAudio ID {idx} для устройства \"{device_name}\" ({direction})")
                    return idx
            
            logger.debug(f"🔍 [BUS] PortAudio ID не найден для устройства \"{device_name}\" ({direction})")
            return None
            
        except Exception as e:
            logger.debug(f"🔍 [BUS] Ошибка поиска PortAudio ID для \"{device_name}\": {e}")
            return None
    
    def is_available(self) -> bool:
        """Проверяет, доступен ли CoreAudio"""
        return self._core_audio_manager is not None and self._core_audio_manager.is_notifications_available()
    
    def cleanup(self):
        """Очистка ресурсов"""
        if self._core_audio_manager:
            try:
                self._core_audio_manager.stop_device_notifications()
                self._core_audio_manager.cleanup()
            except Exception as e:
                logger.error(f"❌ Ошибка очистки CoreAudioDeviceBus: {e}", exc_info=True)

