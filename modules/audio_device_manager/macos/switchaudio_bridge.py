"""
Мост для работы с switchaudio - утилитой переключения аудио устройств на macOS
"""

import asyncio
import logging
import subprocess
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Callable
from ..core.types import AudioDevice, DeviceType, DeviceStatus, DevicePriority

# Импорт sounddevice для маппинга
try:
    import sounddevice as sd
    _SOUNDDEVICE_AVAILABLE = True
except ImportError:
    _SOUNDDEVICE_AVAILABLE = False
    logger.warning("⚠️ [AUDIO_DEBUG] sounddevice не доступен - portaudio_index будет None")

logger = logging.getLogger(__name__)

class SwitchAudioBridge:
    """Мост для работы с switchaudio и мониторинга устройств"""
    
    def __init__(self):
        self._is_monitoring = False
        self._device_listener: Optional[Callable] = None
        self._current_devices: Dict[str, AudioDevice] = {}
        self._monitoring_task: Optional[asyncio.Task] = None
        self._last_device_count = 0
    
    def _get_switchaudio_path(self) -> str:
        """
        Определяет путь к бинарнику SwitchAudioSource.
        
        Поддерживает:
        - PyInstaller onefile (sys._MEIPASS)
        - PyInstaller bundle (.app/Contents/Resources/)
        - Development/Homebrew (PATH)
        
        Returns:
            str: Полный путь к SwitchAudioSource или 'SwitchAudioSource' для PATH
        """
        # 1) PyInstaller onefile: проверяем sys._MEIPASS
        if hasattr(sys, "_MEIPASS"):
            path = Path(sys._MEIPASS) / "resources" / "audio" / "SwitchAudioSource"
            if path.exists():
                logger.debug(f"🔍 Найден SwitchAudioSource (onefile): {path}")
                return str(path)
        
        # 2) PyInstaller bundle: проверяем Contents/Resources/
        macos_dir = Path(sys.argv[0]).resolve().parent
        resources_path = macos_dir.parent / "Resources" / "resources" / "audio" / "SwitchAudioSource"
        if resources_path.exists():
            logger.debug(f"🔍 Найден SwitchAudioSource (bundle): {resources_path}")
            return str(resources_path)
        
        # 3) Fallback на PATH (Homebrew в dev режиме)
        logger.debug("🔍 Используем SwitchAudioSource из PATH")
        return 'SwitchAudioSource'
        
    async def start_monitoring(self, device_change_callback: Callable):
        """Запуск мониторинга изменений устройств"""
        if self._is_monitoring:
            logger.warning("⚠️ Мониторинг уже запущен")
            return
            
        self._device_listener = device_change_callback
        self._is_monitoring = True
        
        try:
            # Получаем начальный список устройств
            initial_devices = await self.get_available_devices()
            self._current_devices = {device.id: device for device in initial_devices}
            self._last_device_count = len(initial_devices)
            
            # Запускаем мониторинг через polling
            self._monitoring_task = asyncio.create_task(self._monitor_devices())
            
            logger.info(f"✅ SwitchAudio мониторинг запущен, найдено {len(initial_devices)} устройств")
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска мониторинга: {e}")
            self._is_monitoring = False
            raise
    
    async def stop_monitoring(self):
        """Остановка мониторинга"""
        if not self._is_monitoring:
            return
            
        try:
            self._is_monitoring = False
            self._device_listener = None
            self._current_devices.clear()
            
            if self._monitoring_task and not self._monitoring_task.done():
                self._monitoring_task.cancel()
                try:
                    await self._monitoring_task
                except asyncio.CancelledError:
                    pass
            
            logger.info("✅ SwitchAudio мониторинг остановлен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки мониторинга: {e}")
    
    async def _monitor_devices(self):
        """Мониторинг устройств через polling"""
        try:
            logger.info("🔄 Запуск мониторинга устройств через switchaudio...")
            logger.info("💡 Подключайте/отключайте наушники для тестирования")
            
            while self._is_monitoring:
                try:
                    # Получаем текущий список устройств
                    current_devices = await self.get_available_devices()
                    current_count = len(current_devices)
                    
                    # Проверяем изменения в количестве устройств
                    if current_count != self._last_device_count:
                        logger.info(f"🔄 Обнаружено изменение: {self._last_device_count} -> {current_count} устройств")
                        
                        # Определяем изменения
                        current_devices_dict = {device.id: device for device in current_devices}
                        old_devices = self._current_devices.copy()
                        self._current_devices = current_devices_dict
                        self._last_device_count = current_count
                        
                        # Создаем объект изменений
                        from ..core.types import DeviceChange
                        changes = DeviceChange(
                            added=[device for device in current_devices if device.id not in old_devices],
                            removed=[device for device_id, device in old_devices.items() if device_id not in current_devices_dict],
                            current_devices=current_devices_dict,
                            timestamp=datetime.now(),
                            change_type="device_change"
                        )
                        
                        # Уведомляем callback
                        if self._device_listener:
                            await self._device_listener(changes)
                    
                    # Ждем перед следующей проверкой
                    await asyncio.sleep(1)  # Проверяем каждую секунду
                    
                except Exception as e:
                    logger.error(f"❌ Ошибка в мониторинге устройств: {e}")
                    await asyncio.sleep(3)  # Ждем дольше при ошибке
                    
        except Exception as e:
            logger.error(f"❌ Ошибка в monitor_devices: {e}")
    
    async def get_available_devices(self, device_type: Optional[str] = None) -> List[AudioDevice]:
        """Получение списка доступных аудио устройств через switchaudio с поддержкой типов"""
        try:
            logger.debug(f"🔍 [AUDIO_DEBUG] Запрос устройств типа: {device_type or 'all'}")
            
            # Используем switchaudio для получения списка устройств
            devices = await self._get_devices_from_switchaudio(device_type)
            
            # Сортируем по приоритету (меньшее значение = выше приоритет)
            devices.sort(key=lambda x: x.priority.value)
            
            logger.info(f"📊 [AUDIO_STATS] Получено {len(devices)} устройств типа {device_type or 'all'}")
            return devices
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения устройств: {e}")
            return []
    
    async def _get_devices_from_switchaudio(self, device_type: Optional[str] = None) -> List[AudioDevice]:
        """Получение устройств через switchaudio с поддержкой INPUT/OUTPUT"""
        try:
            logger.debug(f"🔍 [AUDIO_DEBUG] Выполнение команды: switchaudio -a -t {device_type or 'all'}")
            
            # Получаем путь к бинарнику и запускаем
            switchaudio_cmd = self._get_switchaudio_path()
            cmd = [switchaudio_cmd, '-a']
            
            # Добавляем тип устройства если указан
            if device_type:
                cmd.extend(['-t', device_type])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                logger.warning("⚠️ switchaudio недоступен, возвращаем пустой список")
                return []
            
            # Парсим вывод switchaudio
            devices = []
            lines = result.stdout.strip().split('\n')
            
            for line in lines:
                if line.strip():
                    device = await self._parse_switchaudio_line(line, device_type)
                    if device:
                        devices.append(device)
            
            # Если не нашли устройств, возвращаем пустой список
            if not devices:
                logger.info(f"ℹ️ Устройства типа {device_type or 'all'} не найдены через switchaudio")
                return []
            
            logger.info(f"📊 [AUDIO_STATS] SwitchAudio вернул {len(devices)} устройств типа {device_type or 'all'}")
            return devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройств через switchaudio: {e}")
            return []
    
    async def _parse_switchaudio_line(self, line: str, device_type: Optional[str] = None) -> Optional[AudioDevice]:
        """Парсинг строки вывода switchaudio с поддержкой стабильных ID"""
        try:
            # Пример строки: "MacBook Air Speakers (Built-in Output)"
            # Или: "AirPods Pro (Bluetooth)"
            
            # Извлекаем имя устройства
            name_match = re.match(r'^(.+?)\s*\((.+?)\)', line)
            if not name_match:
                # Если нет скобок, используем всю строку как имя
                name = line.strip()
                device_type_str = "Unknown"
            else:
                name = name_match.group(1).strip()
                device_type_str = name_match.group(2).strip()
            
            # Создаем стабильный ID устройства (вместо hash)
            device_id = f"device_{name.replace(' ', '_').replace('(', '').replace(')', '').lower()}"
            logger.debug(f"🔍 [AUDIO_DEBUG] Генерация стабильного ID для: {name} -> {device_id}")
            
            # Определяем тип устройства с учетом переданного типа
            detected_type = await self._detect_device_type(name, device_type_str, device_type)
            
            # Определяем количество каналов
            channels = await self._get_device_channels(name)
            
            # Определяем дополнительные свойства
            is_bluetooth = 'bluetooth' in device_type_str.lower() or 'bt' in device_type_str.lower()
            is_usb = 'usb' in device_type_str.lower()
            is_builtin = 'built-in' in device_type_str.lower() or 'internal' in device_type_str.lower()
            
            # Определяем приоритет на основе типа устройства и канальности
            if is_bluetooth and detected_type == DeviceType.OUTPUT:
                priority = DevicePriority.HIGHEST  # Bluetooth наушники - высший приоритет
            elif detected_type == DeviceType.OUTPUT and channels == 2 and not is_builtin:
                priority = DevicePriority.HIGH  # Двухканальные внешние устройства (наушники)
            elif detected_type == DeviceType.OUTPUT and channels == 1 and is_builtin:
                priority = DevicePriority.LOWEST  # Одноканальные встроенные устройства
            elif is_builtin:
                priority = DevicePriority.LOWEST  # Встроенные устройства
            else:
                priority = DevicePriority.NORMAL  # Остальные устройства
            
            # Создаем объект устройства
            # Получаем portaudio_index для устройства
            portaudio_index = self._map_to_portaudio_index(name)
            
            device = AudioDevice(
                id=device_id,
                name=name,
                type=detected_type,
                status=DeviceStatus.AVAILABLE,
                channels=channels,
                priority=priority,
                portaudio_index=portaudio_index
            )
            
            return device
            
        except Exception as e:
            logger.error(f"❌ Ошибка парсинга строки switchaudio: {e}")
            return None
    
    async def _detect_device_type(self, name: str, device_type_str: str, requested_type: Optional[str] = None) -> DeviceType:
        """Определение типа устройства по имени и типу с поддержкой INPUT/OUTPUT"""
        try:
            name_lower = name.lower()
            type_lower = device_type_str.lower()
            
            # Если запрошен конкретный тип, используем его
            if requested_type:
                if requested_type.lower() == 'input':
                    logger.debug(f"🔍 [AUDIO_DEBUG] Принудительно определяем как INPUT: {name}")
                    return DeviceType.INPUT
                elif requested_type.lower() == 'output':
                    logger.debug(f"🔍 [AUDIO_DEBUG] Принудительно определяем как OUTPUT: {name}")
                    return DeviceType.OUTPUT
            
            # Ключевые слова для наушников
            headphone_keywords = [
                'headphone', 'headset', 'earphone', 'earbud', 'earpod',
                'airpod', 'beats', 'sony', 'bose', 'sennheiser', 'audio-technica',
                'bluetooth', 'wireless', 'наушник', 'гарнитур'
            ]
            
            # Ключевые слова для динамиков
            speaker_keywords = [
                'speaker', 'monitor', 'studio', 'desktop', 'external',
                'built-in', 'internal', 'macbook', 'imac', 'mac pro',
                'динамик', 'колонк', 'монитор', 'output'
            ]
            
            # Ключевые слова для микрофонов (исключаем из переключения)
            microphone_keywords = [
                'microphone', 'mic', 'input', 'вход', 'микрофон'
            ]
            
            # Проверяем на гарнитуры/наушники (поддерживают И INPUT И OUTPUT)
            if (any(keyword in name_lower for keyword in headphone_keywords) or
                any(keyword in type_lower for keyword in headphone_keywords)):
                # Если это Bluetooth наушники или гарнитуры, они поддерживают И микрофон И динамики
                if ('bluetooth' in name_lower or 'wireless' in name_lower or 
                    'headset' in name_lower or 'airpod' in name_lower):
                    logger.debug(f"🔍 [AUDIO_DEBUG] Определяем как BOTH (гарнитура): {name}")
                    return DeviceType.BOTH
                else:
                    logger.debug(f"🔍 [AUDIO_DEBUG] Определяем как OUTPUT (наушники): {name}")
                    return DeviceType.OUTPUT
            
            # Проверяем на микрофоны (только INPUT)
            if (any(keyword in name_lower for keyword in microphone_keywords) or
                any(keyword in type_lower for keyword in microphone_keywords)):
                logger.debug(f"🔍 [AUDIO_DEBUG] Определяем как INPUT (микрофон): {name}")
                return DeviceType.INPUT
            
            # Проверяем на динамики (только OUTPUT)
            if (any(keyword in name_lower for keyword in speaker_keywords) or
                any(keyword in type_lower for keyword in speaker_keywords)):
                logger.debug(f"🔍 [AUDIO_DEBUG] Определяем как OUTPUT (динамики): {name}")
                return DeviceType.OUTPUT
            
            # По умолчанию считаем OUTPUT
            logger.debug(f"🔍 [AUDIO_DEBUG] Определяем как OUTPUT (по умолчанию): {name}")
            return DeviceType.OUTPUT
            
        except Exception as e:
            logger.error(f"❌ Ошибка определения типа устройства: {e}")
            return DeviceType.OUTPUT  # По умолчанию OUTPUT
    
    async def _get_device_channels(self, name: str) -> int:
        """Получение количества каналов устройства"""
        try:
            name_lower = name.lower()
            
            # Наушники обычно стерео (двухканальные)
            if any(keyword in name_lower for keyword in ['headphone', 'headset', 'earphone', 'earbud', 'airpod']):
                return 2
            
            # Встроенные динамики macOS обычно одноканальные
            if any(keyword in name_lower for keyword in ['built-in', 'internal', 'macbook', 'imac']):
                return 1
            
            # Микрофоны моно (одноканальные)
            if any(keyword in name_lower for keyword in ['microphone', 'mic']):
                return 1
            
            # По умолчанию стерео (двухканальные)
            return 2
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения каналов устройства: {e}")
            return 2
    
    async def _get_fallback_devices(self) -> List[AudioDevice]:
        """Fallback устройства если switchaudio недоступен"""
        try:
            devices = [
                AudioDevice(
                    id="builtin_speakers",
                    name="MacBook Air Speakers",
                    type=DeviceType.OUTPUT,
                    status=DeviceStatus.AVAILABLE,
                    channels=2,
                    priority=DevicePriority.LOWEST,
                    portaudio_index=self._map_to_portaudio_index("MacBook Air Speakers")
                ),
                AudioDevice(
                    id="builtin_microphone",
                    name="MacBook Air Microphone",
                    type=DeviceType.INPUT,
                    status=DeviceStatus.AVAILABLE,
                    channels=1,
                    priority=DevicePriority.LOWEST,
                    portaudio_index=self._map_to_portaudio_index("MacBook Air Microphone")
                )
            ]
            
            return devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания fallback устройств: {e}")
            return []
    
    async def get_default_output_device(self) -> Optional[AudioDevice]:
        """Получение устройства вывода по умолчанию"""
        try:
            devices = await self.get_available_devices()
            if devices:
                return devices[0]  # Возвращаем первое (с наивысшим приоритетом)
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройства по умолчанию: {e}")
            return None
    
    async def set_default_output_device(self, device_id: str) -> bool:
        """Установка устройства вывода по умолчанию через switchaudio"""
        try:
            # Находим устройство по ID
            devices = await self.get_available_devices()
            target_device = next((d for d in devices if d.id == device_id), None)
            
            if not target_device:
                logger.error(f"❌ Устройство с ID {device_id} не найдено")
                return False
            
            # Проверяем, что это не микрофон
            if target_device.type == DeviceType.INPUT:
                logger.warning(f"⚠️ Пропускаем переключение на микрофон: {target_device.name}")
                return False
            
            logger.info(f"🔄 Попытка переключения на: {target_device.name} (тип: {target_device.type.value})")
            
            # Получаем путь к бинарнику и используем SwitchAudioSource для переключения
            switchaudio_cmd = self._get_switchaudio_path()
            result = subprocess.run([
                switchaudio_cmd, '-t', 'output', '-s', target_device.name
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                logger.info(f"✅ Успешно переключились на: {target_device.name}")
                return True
            else:
                logger.error(f"❌ Ошибка переключения на {target_device.name}: {result.stderr}")
                
                # Пробуем альтернативный способ переключения
                logger.info("🔄 Пробуем альтернативный способ переключения...")
                return await self._try_alternative_switch(target_device)
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка установки устройства по умолчанию: {e}")
            return False
    
    async def set_default_input_device(self, device_id: str) -> bool:
        """Установка устройства ввода по умолчанию через sounddevice"""
        try:
            # Находим устройство по ID
            devices = await self.get_available_devices()
            target_device = next((d for d in devices if d.id == device_id), None)
            
            if not target_device:
                logger.error(f"❌ [AUDIO_ERROR] Устройство с ID {device_id} не найдено")
                return False
            
            # Проверяем, что это устройство поддерживает INPUT функцию
            if target_device.type not in [DeviceType.INPUT, DeviceType.BOTH]:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Устройство не поддерживает INPUT функцию: {target_device.name}")
                return False
            
            logger.info(f"🔄 [AUDIO_SWITCH] Попытка переключения на INPUT: {target_device.name} (тип: {target_device.type.value})")
            
            # Используем sounddevice для переключения INPUT устройства
            import sounddevice as sd
            
            # Получаем portaudio_index устройства
            portaudio_index = target_device.portaudio_index
            if portaudio_index is None:
                logger.error(f"❌ [AUDIO_ERROR] portaudio_index не найден для устройства: {target_device.name}")
                return False
            
            # Устанавливаем устройство по умолчанию через sounddevice
            current_default = sd.default.device
            sd.default.device = (portaudio_index, current_default[1])  # (input, output)
            
            # Проверяем, что переключение прошло успешно
            new_default = sd.default.device
            if new_default[0] == portaudio_index:
                logger.info(f"✅ [AUDIO_SUCCESS] Переключено на INPUT устройство: {target_device.name} (index: {portaudio_index})")
                return True
            else:
                logger.error(f"❌ [AUDIO_ERROR] Не удалось переключиться на INPUT устройство: {target_device.name}")
                return False
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка установки устройства ввода: {e}")
            return False
    
    async def _try_alternative_switch(self, target_device: AudioDevice) -> bool:
        """Альтернативный способ переключения устройства"""
        try:
            # Получаем путь к бинарнику
            switchaudio_cmd = self._get_switchaudio_path()
            
            # Пробуем переключиться по части имени
            name_parts = target_device.name.split()
            for part in name_parts:
                if len(part) > 3:  # Игнорируем короткие части
                    logger.info(f"🔄 Пробуем переключиться по части имени: {part}")
                    result = subprocess.run([
                        switchaudio_cmd, '-t', 'output', '-s', part
                    ], capture_output=True, text=True, timeout=10)
                    
                    if result.returncode == 0:
                        logger.info(f"✅ Успешно переключились на: {part}")
                        return True
            
            # Если не получилось, пробуем переключиться на встроенные динамики
            logger.info("🔄 Переключаемся на встроенные динамики...")
            result = subprocess.run([
                switchaudio_cmd, '-t', 'output', '-s', 'MacBook Air Speakers'
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                logger.info("✅ Успешно переключились на встроенные динамики")
                return True
            else:
                logger.error("❌ Не удалось переключиться даже на встроенные динамики")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка альтернативного переключения: {e}")
            return False
    
    def _map_to_portaudio_index(self, device_name: str) -> Optional[int]:
        """
        Маппинг имени устройства switchaudio в portaudio_index для sounddevice.
        
        Args:
            device_name: Имя устройства из switchaudio
            
        Returns:
            portaudio_index для sounddevice или None если не найден
        """
        if not _SOUNDDEVICE_AVAILABLE:
            logger.warning(f"⚠️ [AUDIO_DEBUG] sounddevice недоступен - portaudio_index будет None для {device_name}")
            return None
            
        try:
            logger.debug(f"🔍 [AUDIO_DEBUG] Маппинг устройства '{device_name}' в portaudio_index")
            
            # Получаем список всех устройств sounddevice
            devices = sd.query_devices()
            logger.debug(f"🔍 [AUDIO_DEBUG] Найдено {len(devices)} устройств в sounddevice")
            
            # Ищем точное совпадение имени
            for i, dev in enumerate(devices):
                if dev['name'] == device_name:
                    logger.debug(f"✅ [AUDIO_SUCCESS] Устройство найдено: '{device_name}' -> portaudio_index {i}")
                    return i
            
            # Если точного совпадения нет, ищем частичное совпадение
            for i, dev in enumerate(devices):
                if device_name.lower() in dev['name'].lower() or dev['name'].lower() in device_name.lower():
                    logger.debug(f"✅ [AUDIO_SUCCESS] Устройство найдено (частичное): '{device_name}' -> '{dev['name']}' -> portaudio_index {i}")
                    return i
            
            logger.warning(f"⚠️ [AUDIO_DEBUG] Устройство '{device_name}' не найдено в sounddevice")
            return None
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка маппинга устройства '{device_name}' в portaudio_index: {e}")
            return None









































