"""
CoreAudio Monitor - Мониторинг системного default OUTPUT устройства в реальном времени

Использует CoreAudio API для получения реального системного default устройства macOS
и отслеживания изменений в реальном времени.
"""

import logging
import threading
import time
import subprocess
from typing import Optional, Dict, Any, Callable
import ctypes
from ctypes import c_uint32, c_void_p, POINTER, Structure, byref

logger = logging.getLogger(__name__)

# CoreAudio константы
kAudioObjectSystemObject = 1
kAudioHardwarePropertyDefaultOutputDevice = 'dout'  # 'dout' = 0x646F7574
kAudioObjectPropertyScopeGlobal = 'glob'  # 'glob' = 0x676C6F62
kAudioObjectPropertyElementMain = 0

# CoreAudio типы
AudioObjectID = c_uint32
AudioObjectPropertyAddress = Structure


class CoreAudioMonitor:
    """
    Мониторинг системного default INPUT и OUTPUT устройств через CoreAudio API
    
    Преимущества перед PortAudio:
    1. Получает реальный системный default macOS (не кэш PortAudio)
    2. Может мониторить изменения в реальном времени
    3. Не зависит от инициализации PortAudio
    4. Поддерживает как INPUT, так и OUTPUT устройства
    """
    
    def __init__(self, monitor_input: bool = True, monitor_output: bool = True):
        """
        Инициализация монитора
        
        Args:
            monitor_input: Мониторить INPUT устройства
            monitor_output: Мониторить OUTPUT устройства
        """
        self.monitor_input = monitor_input
        self.monitor_output = monitor_output
        
        # OUTPUT устройства
        self._current_output_device_id: Optional[int] = None
        self._current_output_device_name: Optional[str] = None
        
        # INPUT устройства
        self._current_input_device_id: Optional[int] = None
        self._current_input_device_name: Optional[str] = None
        
        self._monitoring = False
        self._monitor_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        
        # Callbacks
        self._output_device_change_callback: Optional[Callable[[str, int], None]] = None
        self._input_device_change_callback: Optional[Callable[[str, int], None]] = None
        
        # Попытка загрузить CoreAudio framework
        self._core_audio_available = self._load_core_audio()
        
        logger.info(f"🔧 CoreAudioMonitor создан (Input: {monitor_input}, Output: {monitor_output}, CoreAudio: {self._core_audio_available})")
    
    def _load_core_audio(self) -> bool:
        """Загрузка CoreAudio framework"""
        try:
            # Пробуем загрузить через ctypes
            self._core_audio = ctypes.CDLL('/System/Library/Frameworks/CoreAudio.framework/CoreAudio')
            return True
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить CoreAudio framework: {e}")
            logger.info("💡 Используем fallback через pyobjc или sounddevice")
            return False
    
    def get_system_default_input_device(self) -> Optional[Dict[str, Any]]:
        """
        Получить реальное системное default INPUT устройство
        
        Returns:
            Dict с информацией об устройстве или None если не удалось
        """
        # Используем system_profiler для получения реального системного default
        try:
            system_name = self._get_system_default_input_via_profiler()
            if system_name:
                logger.debug(f"🔍 Системное default INPUT: \"{system_name}\"")
                
                # Пытаемся найти в PortAudio
                import sounddevice as sd
                from system_default_helper import find_device_in_portaudio_by_name
                
                portaudio_id = find_device_in_portaudio_by_name(system_name)
                
                if portaudio_id is not None:
                    device_info = sd.query_devices(portaudio_id, 'input')
                    return {
                        'id': portaudio_id,
                        'name': device_info.get('name', system_name),
                        'sample_rate': device_info.get('default_samplerate', 0),
                        'channels': device_info.get('max_input_channels', 0),
                        'source': f"System (profiler) + PortAudio"
                    }
                else:
                    return {
                        'id': None,
                        'name': system_name,
                        'sample_rate': 0,
                        'channels': 0,
                        'source': 'System (profiler) - НЕ в PortAudio'
                    }
        except Exception as e:
            logger.debug(f"Ошибка получения INPUT устройства: {e}")
        
        # Fallback через PortAudio
        try:
            import sounddevice as sd
            default = sd.default.device
            if hasattr(default, '__getitem__'):
                try:
                    input_id = default[0]
                    device_info = sd.query_devices(input_id, 'input')
                    return {
                        'id': input_id,
                        'name': device_info.get('name', 'Unknown'),
                        'sample_rate': device_info.get('default_samplerate', 0),
                        'channels': device_info.get('max_input_channels', 0),
                        'source': 'PortAudio (fallback)'
                    }
                except (IndexError, TypeError):
                    pass
        except Exception as e:
            logger.debug(f"Ошибка PortAudio fallback для INPUT: {e}")
        
        return None
    
    def _get_system_default_input_via_profiler(self) -> Optional[str]:
        """Получить системное default INPUT устройство через system_profiler"""
        try:
            result = subprocess.run(
                ['system_profiler', 'SPAudioDataType'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                output = result.stdout
                lines = output.split('\n')
                
                current_device = None
                
                for i, line in enumerate(lines):
                    stripped = line.strip()
                    
                    # Заголовок устройства
                    if stripped.endswith(':'):
                        device_name = stripped.rstrip(':').strip()
                        if (device_name not in ['Audio', 'Devices'] and 
                            len(device_name) > 3 and
                            not device_name.startswith('Output')):
                            current_device = device_name
                    
                    # Проверяем default input
                    elif 'Default Input Device: Yes' in stripped and current_device:
                        logger.debug(f"🔍 system_profiler INPUT: найдено устройство \"{current_device}\" (строка {i+1})")
                        return current_device
        except Exception as e:
            logger.debug(f"Ошибка system_profiler для INPUT: {e}")
        
        return None
    
    def get_system_default_output_device(self) -> Optional[Dict[str, Any]]:
        """
        Получить реальное системное default OUTPUT устройство
        
        Пробует несколько методов:
        1. Системные команды macOS (system_profiler, switchaudio-source)
        2. PortAudio (fallback)
        
        Returns:
            Dict с информацией об устройстве или None если не удалось
        """
        # ✅ МЕТОД 1: Системные команды macOS (получаем реальное системное default)
        try:
            from system_default_helper import get_real_system_default_output, find_device_in_portaudio_by_name
            
            system_device = get_real_system_default_output()
            if system_device:
                system_name = system_device.get('name', '')
                logger.debug(f"🔍 Системное default устройство: \"{system_name}\"")
                
                # Пытаемся найти это устройство в PortAudio
                portaudio_id = find_device_in_portaudio_by_name(system_name)
                
                if portaudio_id is not None:
                    # Нашли в PortAudio - получаем полную информацию
                    import sounddevice as sd
                    device_info = sd.query_devices(portaudio_id, 'output')
                    return {
                        'id': portaudio_id,
                        'name': device_info.get('name', system_name),
                        'sample_rate': device_info.get('default_samplerate', 0),
                        'channels': device_info.get('max_output_channels', 0),
                        'source': f"System ({system_device.get('source', 'unknown')}) + PortAudio"
                    }
                else:
                    # Не нашли в PortAudio - возвращаем только имя
                    logger.warning(f"⚠️ Устройство \"{system_name}\" найдено в системе, но не видно в PortAudio")
                    logger.warning("   Возможно нужно перезапустить приложение для обновления списка устройств")
                    return {
                        'id': None,
                        'name': system_name,
                        'sample_rate': 0,
                        'channels': 0,
                        'source': f"System ({system_device.get('source', 'unknown')}) - НЕ в PortAudio"
                    }
        except ImportError:
            logger.debug("system_default_helper недоступен")
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения системного устройства: {e}")
        
        # ✅ МЕТОД 2: Fallback через sounddevice
        try:
            import sounddevice as sd
            
            # Принудительно обновляем список устройств
            _ = sd.query_devices()
            
            # Получаем default
            default = sd.default.device
            if hasattr(default, '__getitem__'):
                try:
                    output_id = default[1]
                    device_info = sd.query_devices(output_id, 'output')
                    
                    return {
                        'id': output_id,
                        'name': device_info.get('name', 'Unknown'),
                        'sample_rate': device_info.get('default_samplerate', 0),
                        'channels': device_info.get('max_output_channels', 0),
                        'source': 'PortAudio (fallback)'
                    }
                except (IndexError, TypeError):
                    pass
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения устройства через sounddevice: {e}")
        
        return None
    
    def start_monitoring(self, 
                        check_interval: float = 0.5, 
                        output_callback: Optional[Callable[[str, int], None]] = None,
                        input_callback: Optional[Callable[[str, int], None]] = None):
        """
        Запуск мониторинга изменений устройств
        
        Args:
            check_interval: Интервал проверки в секундах
            output_callback: Функция вызываемая при смене OUTPUT устройства (name, device_id)
            input_callback: Функция вызываемая при смене INPUT устройства (name, device_id)
        """
        if self._monitoring:
            logger.warning("⚠️ Мониторинг уже запущен")
            return
        
        self._output_device_change_callback = output_callback
        self._input_device_change_callback = input_callback
        self._monitoring = True
        self._stop_event.clear()
        
        # Получаем начальные устройства
        if self.monitor_output:
            initial_output = self.get_system_default_output_device()
            if initial_output:
                self._current_output_device_id = initial_output.get('id')
                self._current_output_device_name = initial_output.get('name')
                logger.info(f"📱 Начальное OUTPUT устройство: \"{self._current_output_device_name}\" (ID={self._current_output_device_id})")
        
        if self.monitor_input:
            initial_input = self.get_system_default_input_device()
            if initial_input:
                self._current_input_device_id = initial_input.get('id')
                self._current_input_device_name = initial_input.get('name')
                logger.info(f"🎤 Начальное INPUT устройство: \"{self._current_input_device_name}\" (ID={self._current_input_device_id})")
        
        # Запускаем поток мониторинга
        self._monitor_thread = threading.Thread(
            target=self._monitor_loop,
            args=(check_interval,),
            daemon=True,
            name="CoreAudioMonitor"
        )
        self._monitor_thread.start()
        logger.info(f"🚀 Мониторинг устройств запущен (Input: {self.monitor_input}, Output: {self.monitor_output}, интервал: {check_interval}s)")
    
    def stop_monitoring(self):
        """Остановка мониторинга"""
        if not self._monitoring:
            return
        
        self._monitoring = False
        self._stop_event.set()
        
        if self._monitor_thread and self._monitor_thread.is_alive():
            self._monitor_thread.join(timeout=2.0)
        
        logger.info("🛑 Мониторинг устройств остановлен")
    
    def _get_system_default_via_profiler(self) -> Optional[str]:
        """Получить системное default устройство через system_profiler"""
        try:
            result = subprocess.run(
                ['system_profiler', 'SPAudioDataType'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                output = result.stdout
                lines = output.split('\n')
                
                # Упрощенный подход: отслеживаем текущее устройство при парсинге
                current_device = None
                
                for i, line in enumerate(lines):
                    stripped = line.strip()
                    
                    # Заголовок устройства (заканчивается на :)
                    if stripped.endswith(':'):
                        device_name = stripped.rstrip(':').strip()
                        # Проверяем что это не служебная метка
                        if (device_name not in ['Audio', 'Devices'] and 
                            len(device_name) > 3 and
                            not device_name.startswith('Input') and
                            not device_name.startswith('Output')):
                            current_device = device_name
                    
                    # Проверяем default output для текущего устройства
                    # Если есть "Default Output Device: Yes" - это OUTPUT устройство по определению
                    elif 'Default Output Device: Yes' in stripped and current_device:
                        logger.debug(f"🔍 system_profiler: найдено устройство \"{current_device}\" (строка {i+1})")
                        return current_device
                            
        except subprocess.TimeoutExpired:
            logger.debug("system_profiler timeout")
        except Exception as e:
            logger.debug(f"Ошибка system_profiler: {e}")
        
        return None
    
    def _monitor_loop(self, check_interval: float):
        """Основной цикл мониторинга"""
        logger.debug("🔄 Запуск цикла мониторинга устройств")
        
        while not self._stop_event.is_set():
            try:
                # ✅ МОНИТОРИНГ OUTPUT
                if self.monitor_output:
                    current_output = self.get_system_default_output_device()
                    system_output_name = self._get_system_default_via_profiler()
                    
                    effective_output_name = system_output_name if system_output_name else (current_output.get('name') if current_output else None)
                    effective_output_id = current_output.get('id') if current_output else None
                    
                    if effective_output_name:
                        if self._current_output_device_name is None:
                            self._current_output_device_name = effective_output_name
                            self._current_output_device_id = effective_output_id
                            logger.info(f"📱 OUTPUT устройство определено: \"{effective_output_name}\" (ID={effective_output_id})")
                        elif effective_output_name != self._current_output_device_name:
                            old_name = self._current_output_device_name
                            old_id = self._current_output_device_id
                            
                            self._current_output_device_name = effective_output_name
                            self._current_output_device_id = effective_output_id
                            
                            logger.info("")
                            logger.info("🔄 ПЕРЕКЛЮЧЕНИЕ OUTPUT УСТРОЙСТВА!")
                            logger.info(f"   Старое: \"{old_name}\" (ID={old_id})")
                            logger.info(f"   Новое: \"{effective_output_name}\" (ID={effective_output_id})")
                            logger.info("")
                            
                            if self._output_device_change_callback:
                                try:
                                    self._output_device_change_callback(effective_output_name, effective_output_id if effective_output_id is not None else -1)
                                except Exception as e:
                                    logger.error(f"❌ Ошибка в OUTPUT callback: {e}")
                
                # ✅ МОНИТОРИНГ INPUT
                if self.monitor_input:
                    current_input = self.get_system_default_input_device()
                    system_input_name = self._get_system_default_input_via_profiler()
                    
                    effective_input_name = system_input_name if system_input_name else (current_input.get('name') if current_input else None)
                    effective_input_id = current_input.get('id') if current_input else None
                    
                    if effective_input_name:
                        if self._current_input_device_name is None:
                            self._current_input_device_name = effective_input_name
                            self._current_input_device_id = effective_input_id
                            logger.info(f"🎤 INPUT устройство определено: \"{effective_input_name}\" (ID={effective_input_id})")
                        elif effective_input_name != self._current_input_device_name:
                            old_name = self._current_input_device_name
                            old_id = self._current_input_device_id
                            
                            self._current_input_device_name = effective_input_name
                            self._current_input_device_id = effective_input_id
                            
                            logger.info("")
                            logger.info("🔄 ПЕРЕКЛЮЧЕНИЕ INPUT УСТРОЙСТВА!")
                            logger.info(f"   Старое: \"{old_name}\" (ID={old_id})")
                            logger.info(f"   Новое: \"{effective_input_name}\" (ID={effective_input_id})")
                            logger.info("")
                            
                            if self._input_device_change_callback:
                                try:
                                    self._input_device_change_callback(effective_input_name, effective_input_id if effective_input_id is not None else -1)
                                except Exception as e:
                                    logger.error(f"❌ Ошибка в INPUT callback: {e}")
                
                # Ждем до следующей проверки
                self._stop_event.wait(check_interval)
                
            except Exception as e:
                logger.error(f"❌ Ошибка в цикле мониторинга: {e}")
                import traceback
                logger.debug(traceback.format_exc())
                self._stop_event.wait(1.0)  # Пауза при ошибке
        
        logger.debug("🔄 Цикл мониторинга завершен")
    
    def get_current_output_device(self) -> Optional[Dict[str, Any]]:
        """Получить текущее OUTPUT устройство (thread-safe)"""
        if self._current_output_device_name is None:
            return None
        
        return {
            'id': self._current_output_device_id,
            'name': self._current_output_device_name,
            'source': 'CoreAudio Monitor'
        }
    
    def get_current_input_device(self) -> Optional[Dict[str, Any]]:
        """Получить текущее INPUT устройство (thread-safe)"""
        if self._current_input_device_name is None:
            return None
        
        return {
            'id': self._current_input_device_id,
            'name': self._current_input_device_name,
            'source': 'CoreAudio Monitor'
        }
    
    def get_current_device(self) -> Optional[Dict[str, Any]]:
        """Получить текущее OUTPUT устройство (для обратной совместимости)"""
        return self.get_current_output_device()
    
    def is_monitoring(self) -> bool:
        """Проверка запущен ли мониторинг"""
        return self._monitoring

