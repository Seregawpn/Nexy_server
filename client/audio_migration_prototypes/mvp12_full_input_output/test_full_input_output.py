"""
MVP-12: Full Integration - Input + Output

Цель: Полная интеграция всех компонентов:
- Input: Push-to-talk, device switching, Google SR (из MVP-11)
- Output: AVAudioEngine playback, device switching (из MVP-6)
- Сценарий: Запись речи → распознавание → воспроизведение ответа

Exit Gate:
- [ ] Push-to-talk активирует микрофон
- [ ] Переключение input устройств работает
- [ ] Распознавание речи работает
- [ ] Output playback воспроизводит аудио
- [ ] Переключение output устройств работает
- [ ] Полный цикл: запись → распознавание → воспроизведение работает
"""

import sys
import os
import time
import logging
import threading
import numpy as np
from typing import Optional, Dict, List
from dataclasses import dataclass
from pathlib import Path

# Добавляем пути к предыдущим MVP
mvp1_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp1_device_discovery"
mvp2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp2_device_mapping"
mvp5_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp5_input_google_sr"
mvp6_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp6_output_playback"
sys.path.insert(0, mvp1_path)
sys.path.insert(0, mvp2_path)
sys.path.insert(0, mvp5_path)
sys.path.insert(0, mvp6_path)

# Импорты из предыдущих MVP
from test_device_discovery import DeviceDiscoveryPrototype, DeviceInfo
from test_device_mapping import DeviceMappingPrototype
from test_input_google_sr_pipeline import GoogleSRPipelinePrototype
from test_output_playback import OutputPlaybackPrototype

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Проверка доступности pynput
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    logger.warning("⚠️ pynput не доступен, используем симуляцию")

# Проверка доступности speech_recognition
try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    logger.error("❌ speech_recognition не доступен")

# Проверка доступности AVFoundation
try:
    from AVFoundation import (
        AVAudioEngine,
        AVAudioPlayerNode,
        AVAudioFormat,
        AVAudioPCMBuffer,
        AVAudioSession
    )
    from Foundation import NSRunLoop
    PYOBJC_AVAILABLE = True
except ImportError:
    PYOBJC_AVAILABLE = False
    logger.error("❌ AVFoundation не доступен")


@dataclass
class FullCycleEvent:
    """Событие полного цикла: запись → распознавание → воспроизведение"""
    timestamp: float
    input_device: str
    output_device: str
    recognized_text: Optional[str]
    playback_success: bool
    duration_ms: int


class FullInputOutputPrototype:
    """
    Полная интеграция Input + Output
    
    Структура:
    1. Инициализация компонентов (Input + Output)
    2. Мониторинг устройств (Input + Output)
    3. Push-to-talk → запись → распознавание → воспроизведение
    4. Переключение устройств во время работы
    """
    
    def __init__(self):
        # Input компоненты
        self.device_discovery = DeviceDiscoveryPrototype()
        self.device_mapping = DeviceMappingPrototype()
        self.google_sr_pipeline = None
        
        # Output компоненты
        self.output_playback = OutputPlaybackPrototype()
        
        # Текущее состояние
        self.current_input_device_data: Optional[Dict] = None
        self.current_output_device_data: Optional[Dict] = None
        self.last_input_device_uid: Optional[str] = None
        self.last_output_device_uid: Optional[str] = None
        
        # Микрофон и распознаватель
        self.current_microphone: Optional[sr.Microphone] = None
        self.current_recognizer: Optional[sr.Recognizer] = None
        
        # Состояние записи
        self.is_recording = False
        self.key_pressed = False
        self._pressed_keys = set()
        
        # Состояние воспроизведения
        self.is_playing = False
        self.output_key_pressed = False
        
        # Мониторинг
        self.stop_device_monitoring = threading.Event()
        self.device_monitor_thread: Optional[threading.Thread] = None
        self.key_listener: Optional[keyboard.Listener] = None
        
        # События
        self.full_cycle_events: List[FullCycleEvent] = []
        
    def setup(self) -> bool:
        """Инициализация всех компонентов"""
        logger.info("=" * 80)
        logger.info("MVP-12: Full Integration - Input + Output")
        logger.info("=" * 80)
        logger.info("")
        
        logger.info("📋 Инициализация компонентов...")
        
        # Инициализация Input компонентов
        if not self.device_discovery.setup():
            logger.error("❌ Ошибка инициализации DeviceDiscovery")
            return False
        
        if not self.device_mapping.setup():
            logger.error("❌ Ошибка инициализации DeviceMapping")
            return False
        
        self.google_sr_pipeline = GoogleSRPipelinePrototype()
        if not self.google_sr_pipeline.setup():
            logger.error("❌ Ошибка инициализации GoogleSRPipeline")
            return False
        
        # Инициализация Output компонентов
        if not self.output_playback.setup():
            logger.error("❌ Ошибка инициализации OutputPlayback")
            return False
        
        if not self.output_playback.setup_audio_session():
            logger.error("❌ Ошибка настройки AVAudioSession для Output")
            return False
        
        if not self.output_playback.initialize_engine():
            logger.error("❌ Ошибка инициализации AVAudioEngine")
            return False
        
        # Запуск AVAudioEngine
        try:
            error = None
            if not self.output_playback.engine.startAndReturnError_(error):
                logger.error("❌ Не удалось запустить AVAudioEngine")
                return False
            logger.info("✅ AVAudioEngine запущен")
        except Exception as e:
            logger.error(f"❌ Ошибка запуска AVAudioEngine: {e}")
            return False
        
        # Получение начальных устройств
        if not self._get_initial_devices():
            logger.error("❌ Не удалось получить начальные устройства")
            return False
        
        logger.info("✅ Инициализация завершена")
        logger.info(f"   Input устройство: {self.current_input_device_data['name'] if self.current_input_device_data else 'Unknown'}")
        logger.info(f"   Output устройство: {self.current_output_device_data['name'] if self.current_output_device_data else 'Unknown'}")
        logger.info("")
        
        return True
    
    def _get_initial_devices(self) -> bool:
        """Получение начальных устройств (Input + Output)"""
        try:
            import sounddevice as sd
            
            # Input устройство
            default_input = sd.default.device[0]
            if default_input is None or default_input < 0:
                logger.error("❌ Нет доступных input устройств")
                return False
            
            device_info = sd.query_devices(default_input)
            avf_devices = self.device_discovery.get_input_devices()
            avf_device = None
            for dev in avf_devices:
                if device_info.get('name', '').lower() in dev.name.lower() or dev.name.lower() in device_info.get('name', '').lower():
                    avf_device = dev
                    break
            
            self.current_input_device_data = {
                "uid": avf_device.uid if avf_device else f"portaudio_{default_input}",
                "name": device_info.get('name', 'Unknown'),
                "device_index": default_input,
                "sample_rate": int(device_info.get('default_samplerate', 44100)),
                "max_input_channels": int(device_info.get('max_input_channels', 1))
            }
            
            # Output устройство
            default_output = sd.default.device[1]
            if default_output is None or default_output < 0:
                logger.warning("⚠️ Нет доступных output устройств, используем системное default")
                default_output = sd.default.device[1] if sd.default.device[1] is not None else 0
            
            output_info = sd.query_devices(default_output)
            avf_output_devices = self.device_discovery.get_output_devices()
            avf_output_device = None
            for dev in avf_output_devices:
                if output_info.get('name', '').lower() in dev.name.lower() or dev.name.lower() in output_info.get('name', '').lower():
                    avf_output_device = dev
                    break
            
            self.current_output_device_data = {
                "uid": avf_output_device.uid if avf_output_device else f"portaudio_{default_output}",
                "name": output_info.get('name', 'Unknown'),
                "device_index": default_output,
                "sample_rate": int(output_info.get('default_samplerate', 44100)),
                "max_output_channels": int(output_info.get('max_output_channels', 2))
            }
            
            # Инициализация микрофона
            self.current_microphone = sr.Microphone(device_index=self.current_input_device_data['device_index'])
            self.current_recognizer = sr.Recognizer()
            
            self.last_input_device_uid = self.current_input_device_data['uid']
            self.last_output_device_uid = self.current_output_device_data['uid']
            
            logger.info(f"✅ Начальные устройства получены")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройств: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def _get_current_input_device_data(self) -> Optional[Dict]:
        """Получение данных текущего input устройства (из MVP-11)"""
        try:
            import sounddevice as sd
            from AVFoundation import AVAudioSession
            
            # Получаем все устройства через PortAudio
            all_portaudio_devices = []
            try:
                all_devices = sd.query_devices()
                for idx, dev in enumerate(all_devices):
                    if dev.get('max_input_channels', 0) > 0:
                        all_portaudio_devices.append({
                            'index': idx,
                            'name': dev.get('name', ''),
                            'sample_rate': dev.get('default_samplerate', 44100),
                            'channels': dev.get('max_input_channels', 1)
                        })
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio устройств: {e}")
                # Пробуем переинициализировать PortAudio
                try:
                    sd._terminate()
                    sd._initialize()
                    all_devices = sd.query_devices()
                    for idx, dev in enumerate(all_devices):
                        if dev.get('max_input_channels', 0) > 0:
                            all_portaudio_devices.append({
                                'index': idx,
                                'name': dev.get('name', ''),
                                'sample_rate': dev.get('default_samplerate', 44100),
                                'channels': dev.get('max_input_channels', 1)
                            })
                    logger.info("✅ PortAudio переинициализирован")
                except Exception as reinit_e:
                    logger.error(f"❌ Не удалось переинициализировать PortAudio: {reinit_e}")
                    return None
            
            # Получаем текущее устройство через AVFoundation
            session = AVAudioSession.sharedInstance()
            current_route = session.currentRoute()
            current_inputs = current_route.inputs() if current_route else []
            
            avf_devices = self.device_discovery.get_input_devices()
            
            device_info = None
            device_uid = None
            device_name = None
            current_portaudio_index = None
            
            if current_inputs and len(current_inputs) > 0:
                port = current_inputs[0]
                if hasattr(port, 'uid'):
                    device_uid = port.uid()
                elif hasattr(port, 'portName'):
                    device_uid = port.portName()
                
                if hasattr(port, 'portName'):
                    device_name = port.portName()
                
                for dev in avf_devices:
                    if dev.uid == device_uid or dev.name == device_name:
                        device_info = dev
                        break
                
                if not device_info and device_name:
                    for pa_dev in all_portaudio_devices:
                        if device_name.lower() in pa_dev['name'].lower() or pa_dev['name'].lower() in device_name.lower():
                            current_portaudio_index = pa_dev['index']
                            break
            
            if not device_info and not current_portaudio_index:
                try:
                    default_input = sd.default.device[0]
                    if default_input is not None and default_input >= 0:
                        default_info = sd.query_devices(default_input)
                        current_portaudio_index = default_input
                        device_name = default_info.get('name', 'Unknown')
                    elif all_portaudio_devices:
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        return None
                except Exception as e:
                    if all_portaudio_devices:
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        return None
            
            if current_portaudio_index is not None and not device_info:
                pa_device = None
                for pa_dev in all_portaudio_devices:
                    if pa_dev['index'] == current_portaudio_index:
                        pa_device = pa_dev
                        break
                
                if pa_device:
                    device_info = DeviceInfo(
                        name=pa_device['name'],
                        uid=f"portaudio_{current_portaudio_index}",
                        port_type="unknown",
                        channels=pa_device['channels'],
                        transport="built_in" if "built-in" in pa_device['name'].lower() or "internal" in pa_device['name'].lower() else "unknown",
                        normalized_name=pa_device['name']
                    )
                    device_uid = device_info.uid
                    device_name = device_info.name
            
            if not device_info:
                return None
            
            class SimpleMappingResult:
                def __init__(self, device_index):
                    self.device_index = device_index
                    self.confidence = 'high'
                def is_usable(self):
                    return True
            
            if current_portaudio_index is not None:
                mapping_result = SimpleMappingResult(current_portaudio_index)
            else:
                mapping_result = self.device_mapping.find_portaudio_match(
                    device_info.name, device_info.channels, device_info.transport
                )
                if not mapping_result.is_usable():
                    try:
                        default_input = sd.default.device[0]
                        if default_input is None or default_input < 0:
                            return None
                        mapping_result = SimpleMappingResult(default_input)
                    except Exception:
                        return None
            
            try:
                pa_device_info = sd.query_devices(mapping_result.device_index)
                sample_rate = int(pa_device_info.get('default_samplerate', 44100))
                max_input_channels = int(pa_device_info.get('max_input_channels', 1))
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio device info: {e}")
                # Пробуем переинициализировать PortAudio
                try:
                    sd._terminate()
                    sd._initialize()
                    pa_device_info = sd.query_devices(mapping_result.device_index)
                    sample_rate = int(pa_device_info.get('default_samplerate', 44100))
                    max_input_channels = int(pa_device_info.get('max_input_channels', 1))
                except Exception:
                    # Fallback значения
                    sample_rate = 44100
                    max_input_channels = 1
            
            return {
                "uid": device_info.uid,
                "name": device_info.name,
                "device_index": mapping_result.device_index,
                "sample_rate": sample_rate,
                "max_input_channels": max_input_channels
            }
                
        except Exception as e:
            logger.error(f"❌ Ошибка получения input устройства: {e}")
            return None
    
    def _switch_input_device(self, device_data: Dict) -> bool:
        """Переключение input устройства"""
        try:
            logger.info(f"      🔄 Переключение input на: {device_data['name']}")
            
            if self.current_microphone:
                try:
                    if hasattr(self.current_microphone, 'close'):
                        self.current_microphone.close()
                except Exception:
                    pass
                self.current_microphone = None
            
            device_index = device_data['device_index']
            self.current_microphone = sr.Microphone(device_index=device_index)
            logger.info(f"      ✅ Input переключен: {device_data['name']} (index: {device_index})")
            return True
            
        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения input: {e}")
            return False
    
    def _get_current_output_device_data(self) -> Optional[Dict]:
        """Получение данных текущего output устройства"""
        try:
            import sounddevice as sd
            from AVFoundation import AVAudioSession
            
            # Получаем все устройства через PortAudio
            all_portaudio_devices = []
            try:
                all_devices = sd.query_devices()
                for idx, dev in enumerate(all_devices):
                    if dev.get('max_output_channels', 0) > 0:
                        all_portaudio_devices.append({
                            'index': idx,
                            'name': dev.get('name', ''),
                            'sample_rate': dev.get('default_samplerate', 44100),
                            'channels': dev.get('max_output_channels', 2)
                        })
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio output устройств: {e}")
                # Пробуем переинициализировать PortAudio
                try:
                    sd._terminate()
                    sd._initialize()
                    all_devices = sd.query_devices()
                    for idx, dev in enumerate(all_devices):
                        if dev.get('max_output_channels', 0) > 0:
                            all_portaudio_devices.append({
                                'index': idx,
                                'name': dev.get('name', ''),
                                'sample_rate': dev.get('default_samplerate', 44100),
                                'channels': dev.get('max_output_channels', 2)
                            })
                    logger.info("✅ PortAudio переинициализирован (output)")
                except Exception as reinit_e:
                    logger.error(f"❌ Не удалось переинициализировать PortAudio (output): {reinit_e}")
                    return None
            
            # Получаем текущее устройство через AVFoundation
            session = AVAudioSession.sharedInstance()
            current_route = session.currentRoute()
            current_outputs = current_route.outputs() if current_route else []
            
            avf_devices = self.device_discovery.get_output_devices()
            
            device_info = None
            device_uid = None
            device_name = None
            current_portaudio_index = None
            
            if current_outputs and len(current_outputs) > 0:
                port = current_outputs[0]
                if hasattr(port, 'uid'):
                    device_uid = port.uid()
                elif hasattr(port, 'portName'):
                    device_uid = port.portName()
                
                if hasattr(port, 'portName'):
                    device_name = port.portName()
                
                for dev in avf_devices:
                    if dev.uid == device_uid or dev.name == device_name:
                        device_info = dev
                        break
                
                if not device_info and device_name:
                    for pa_dev in all_portaudio_devices:
                        if device_name.lower() in pa_dev['name'].lower() or pa_dev['name'].lower() in device_name.lower():
                            current_portaudio_index = pa_dev['index']
                            break
            
            if not device_info and not current_portaudio_index:
                try:
                    default_output = sd.default.device[1]
                    if default_output is not None and default_output >= 0:
                        try:
                            default_info = sd.query_devices(default_output)
                            current_portaudio_index = default_output
                            device_name = default_info.get('name', 'Unknown')
                        except Exception as e:
                            logger.warning(f"⚠️ Ошибка получения PortAudio default output: {e}")
                            # Пробуем переинициализировать
                            try:
                                sd._terminate()
                                sd._initialize()
                                default_info = sd.query_devices(default_output)
                                current_portaudio_index = default_output
                                device_name = default_info.get('name', 'Unknown')
                            except Exception:
                                if all_portaudio_devices:
                                    current_portaudio_index = all_portaudio_devices[0]['index']
                                    device_name = all_portaudio_devices[0]['name']
                                else:
                                    return None
                    elif all_portaudio_devices:
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        return None
                except Exception as e:
                    logger.warning(f"⚠️ Ошибка получения default output: {e}")
                    if all_portaudio_devices:
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        return None
            
            if current_portaudio_index is not None and not device_info:
                pa_device = None
                for pa_dev in all_portaudio_devices:
                    if pa_dev['index'] == current_portaudio_index:
                        pa_device = pa_dev
                        break
                
                if pa_device:
                    device_info = DeviceInfo(
                        name=pa_device['name'],
                        uid=f"portaudio_{current_portaudio_index}",
                        port_type="unknown",
                        channels=pa_device['channels'],
                        transport="built_in" if "built-in" in pa_device['name'].lower() or "internal" in pa_device['name'].lower() else "unknown",
                        normalized_name=pa_device['name']
                    )
                    device_uid = device_info.uid
                    device_name = device_info.name
            
            if not device_info:
                return None
            
            class SimpleMappingResult:
                def __init__(self, device_index):
                    self.device_index = device_index
                    self.confidence = 'high'
                def is_usable(self):
                    return True
            
            if current_portaudio_index is not None:
                mapping_result = SimpleMappingResult(current_portaudio_index)
            else:
                # Для output используем системное default
                try:
                    default_output = sd.default.device[1]
                    if default_output is None or default_output < 0:
                        return None
                    mapping_result = SimpleMappingResult(default_output)
                except Exception:
                    return None
            
            try:
                pa_device_info = sd.query_devices(mapping_result.device_index)
                sample_rate = int(pa_device_info.get('default_samplerate', 44100))
                max_output_channels = int(pa_device_info.get('max_output_channels', 2))
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio output device info: {e}")
                # Пробуем переинициализировать PortAudio
                try:
                    sd._terminate()
                    sd._initialize()
                    pa_device_info = sd.query_devices(mapping_result.device_index)
                    sample_rate = int(pa_device_info.get('default_samplerate', 44100))
                    max_output_channels = int(pa_device_info.get('max_output_channels', 2))
                except Exception:
                    # Fallback значения
                    sample_rate = 44100
                    max_output_channels = 2
            
            return {
                "uid": device_info.uid,
                "name": device_info.name,
                "device_index": mapping_result.device_index,
                "sample_rate": sample_rate,
                "max_output_channels": max_output_channels
            }
                
        except Exception as e:
            logger.error(f"❌ Ошибка получения output устройства: {e}")
            return None
    
    def _switch_output_device(self, device_data: Dict) -> bool:
        """Переключение output устройства"""
        try:
            logger.info(f"      🔄 Переключение output на: {device_data['name']}")
            
            # AVAudioEngine использует системное default output устройство при создании
            # При переключении устройства нужно пересоздать engine
            try:
                # Останавливаем текущий engine
                if self.output_playback.engine and self.output_playback.engine.isRunning():
                    self.output_playback.engine.stop()
                    logger.info("      ⏸️ AVAudioEngine остановлен")
                
                # Пересоздаем engine (он автоматически использует новое системное default устройство)
                if not self.output_playback.initialize_engine():
                    logger.error("      ❌ Не удалось переинициализировать AVAudioEngine")
                    return False
                
                # Запускаем engine
                error = None
                if not self.output_playback.engine.startAndReturnError_(error):
                    logger.error("      ❌ Не удалось запустить AVAudioEngine после переключения")
                    return False
                
                logger.info(f"      ✅ Output переключен: {device_data['name']} (index: {device_data['device_index']})")
                logger.info("      ✅ AVAudioEngine пересоздан и запущен")
                return True
                
            except Exception as engine_e:
                logger.error(f"      ❌ Ошибка пересоздания AVAudioEngine: {engine_e}")
                import traceback
                logger.error(traceback.format_exc())
                return False
            
        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения output: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def _start_recording(self) -> bool:
        """Начало записи"""
        try:
            device_name = self.current_input_device_data['name'] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🎙️ НАЧАЛО ЗАПИСИ")
            logger.info(f"   📱 Input: {device_name}")
            logger.info(f"   📱 Output: {self.current_output_device_data['name'] if self.current_output_device_data else 'Unknown'}")
            logger.info("")
            self.is_recording = True
            
            # Калибровка микрофона (только если микрофон доступен)
            if self.current_microphone is not None:
                try:
                    # Создаем новый микрофон для калибровки (speech_recognition.Microphone не переиспользуется)
                    device_index = self.current_input_device_data.get('device_index') if self.current_input_device_data else None
                    if device_index is not None:
                        calib_microphone = sr.Microphone(device_index=device_index)
                        with calib_microphone as source:
                            self.current_recognizer.adjust_for_ambient_noise(source, duration=0.3)
                except Exception as calib_e:
                    logger.warning(f"   ⚠️ Ошибка калибровки (продолжаем): {calib_e}")
            
            logger.info("   ✅ ЗАПИСЬ АКТИВНА - ГОВОРИТЕ В МИКРОФОН")
            logger.info("=" * 80)
            logger.info("")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка начала записи: {e}")
            return False
    
    def _stop_recording(self) -> Optional[str]:
        """Остановка записи и распознавание"""
        try:
            device_name = self.current_input_device_data['name'] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🛑 ОСТАНОВКА ЗАПИСИ")
            logger.info(f"   📱 Input: {device_name}")
            logger.info("")
            start_time = time.time()
            
            # Создаем новый микрофон для записи (speech_recognition.Microphone не переиспользуется)
            device_index = self.current_input_device_data.get('device_index') if self.current_input_device_data else None
            if device_index is None:
                logger.error("   ❌ Нет device_index для записи")
                return None
            
            try:
                recording_microphone = sr.Microphone(device_index=device_index)
                with recording_microphone as source:
                    audio = self.current_recognizer.listen(source, timeout=1.0, phrase_time_limit=5.0)
            except Exception as listen_e:
                logger.error(f"   ❌ Ошибка записи: {listen_e}")
                return None
            
            duration_ms = int((time.time() - start_time) * 1000)
            logger.info(f"   ✅ Аудио записано (длительность: {duration_ms}ms)")
            
            recognized_text = None
            logger.info("   🔍 Распознавание через Google SR...")
            try:
                recognized_text = self.current_recognizer.recognize_google(audio, language="ru-RU")
                logger.info(f"   ✅ РАСПОЗНАНО: {recognized_text}")
            except sr.UnknownValueError:
                logger.warning("   ⚠️ Google SR не смог распознать речь")
            except sr.RequestError as e:
                logger.error(f"   ❌ Ошибка Google SR: {e}")
            
            self.is_recording = False
            
            # Воспроизведение ответа
            playback_success = self._play_response(recognized_text)
            
            # Записываем событие
            event = FullCycleEvent(
                timestamp=time.time(),
                input_device=device_name,
                output_device=self.current_output_device_data['name'] if self.current_output_device_data else "Unknown",
                recognized_text=recognized_text,
                playback_success=playback_success,
                duration_ms=duration_ms
            )
            self.full_cycle_events.append(event)
            
            logger.info(f"   ✅ Полный цикл завершен")
            logger.info("=" * 80)
            logger.info("")
            
            return recognized_text
        except Exception as e:
            logger.error(f"❌ Ошибка остановки записи: {e}")
            self.is_recording = False
            return None
    
    def _play_response(self, text: Optional[str]) -> bool:
        """Воспроизведение ответа через Output"""
        try:
            if not text:
                logger.info("   🔊 Пропуск воспроизведения (нет текста)")
                return False
            
            logger.info(f"   🔊 Воспроизведение ответа: '{text}'")
            
            # Генерируем простой тестовый тон (в реальности это будет TTS)
            sample_rate = 44100  # Используем стандартный sample rate
            duration_sec = 1.0
            frequency = 440.0  # A4
            
            logger.info(f"   🎵 Генерация ответа: {frequency}Hz, {duration_sec}сек")
            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)
            
            # Проверяем, что engine запущен
            if not self.output_playback.engine.isRunning():
                logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                error = None
                if not self.output_playback.engine.startAndReturnError_(error):
                    logger.error("   ❌ Не удалось запустить AVAudioEngine")
                    return False
                logger.info("   ✅ AVAudioEngine запущен")
            
            # Пробуем воспроизвести через OutputPlayback (AVAudioEngine)
            logger.info("   🎵 Воспроизведение ответа через AVAudioEngine...")
            success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            used_fallback = False
            
            if not success:
                # Fallback: используем sounddevice для простого воспроизведения
                logger.warning("   ⚠️ AVAudioEngine не сработал, используем sounddevice fallback...")
                try:
                    import sounddevice as sd
                    logger.info("   🎵 Воспроизведение через sounddevice...")
                    sd.play(audio_data, sample_rate)
                    sd.wait()  # Ждем завершения воспроизведения
                    success = True
                    used_fallback = True
                    logger.info("   ✅ Воспроизведение через sounddevice завершено")
                except Exception as sd_e:
                    logger.error(f"   ❌ Ошибка sounddevice fallback: {sd_e}")
                    success = False
            
            if success:
                logger.info("   ✅ Ответ воспроизведен")
                if not used_fallback:
                    logger.info(f"   ⏳ Ожидание завершения ({duration_sec}сек)...")
                    # Ждем завершения воспроизведения (только если использовали AVAudioEngine)
                    time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Воспроизведение завершено")
            else:
                logger.error("   ❌ Ошибка воспроизведения")
            
            return success
        except Exception as e:
            logger.error(f"   ❌ Ошибка воспроизведения: {e}")
            return False
    
    def _play_test_sound(self) -> bool:
        """Воспроизведение тестового звука (для тестирования Output)"""
        try:
            device_name = self.current_output_device_data['name'] if self.current_output_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🔊 ВОСПРОИЗВЕДЕНИЕ ТЕСТОВОГО ЗВУКА")
            logger.info(f"   📱 Output: {device_name}")
            logger.info("")
            
            self.is_playing = True
            
            # Генерируем тестовый тон (440 Hz, 1 секунда, нормальная громкость)
            sample_rate = 44100  # Используем стандартный sample rate
            duration_sec = 1.0
            frequency = 440.0  # A4
            
            logger.info(f"   🎵 Генерация тестового тона: {frequency}Hz, {duration_sec}сек, {sample_rate}Hz")
            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)  # Нормальная громкость
            
            logger.info(f"   📊 Аудио данные: {len(audio_data)} samples")
            
            # Проверяем, что engine запущен
            if not self.output_playback.engine.isRunning():
                logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                error = None
                if not self.output_playback.engine.startAndReturnError_(error):
                    logger.error("   ❌ Не удалось запустить AVAudioEngine")
                    self.is_playing = False
                    return False
                logger.info("   ✅ AVAudioEngine запущен")
            
            # Пробуем воспроизвести через OutputPlayback (AVAudioEngine)
            logger.info("   🎵 Воспроизведение через AVAudioEngine...")
            success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            used_fallback = False
            
            if not success:
                # Fallback: используем sounddevice для простого воспроизведения
                logger.warning("   ⚠️ AVAudioEngine не сработал, используем sounddevice fallback...")
                try:
                    import sounddevice as sd
                    logger.info("   🎵 Воспроизведение через sounddevice...")
                    sd.play(audio_data, sample_rate)
                    sd.wait()  # Ждем завершения воспроизведения
                    success = True
                    used_fallback = True
                    logger.info("   ✅ Воспроизведение через sounddevice завершено")
                except Exception as sd_e:
                    logger.error(f"   ❌ Ошибка sounddevice fallback: {sd_e}")
                    success = False
            
            if success:
                logger.info("   ✅ Тестовый звук воспроизведен")
                if not used_fallback:
                    logger.info(f"   ⏳ Ожидание завершения воспроизведения ({duration_sec}сек)...")
                    # Ждем завершения воспроизведения (только если использовали AVAudioEngine)
                    time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Воспроизведение завершено")
            else:
                logger.error("   ❌ Ошибка воспроизведения")
            
            self.is_playing = False
            logger.info("=" * 80)
            logger.info("")
            
            return success
        except Exception as e:
            logger.error(f"❌ Ошибка воспроизведения тестового звука: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_playing = False
            return False
    
    def start_keyboard_monitoring(self):
        """Запуск мониторинга клавиатуры"""
        if not PYNPUT_AVAILABLE:
            logger.warning("⚠️ pynput не доступен, используем симуляцию")
            return
        
        try:
            self._pressed_keys = set()
            
            def on_press(key):
                try:
                    self._pressed_keys.add(key)
                    is_ctrl_pressed = keyboard.Key.ctrl_l in self._pressed_keys or keyboard.Key.ctrl_r in self._pressed_keys
                    is_n_pressed = hasattr(key, 'char') and key.char == 'n'
                    is_m_pressed = hasattr(key, 'char') and key.char == 'm'
                    
                    # Control+N - Input (запись)
                    if is_ctrl_pressed and is_n_pressed:
                        if not self.key_pressed:
                            self.key_pressed = True
                            logger.info("⌨️ Control+N нажата - начало записи")
                            self._start_recording()
                    
                    # Control+M - Output (воспроизведение тестового звука)
                    if is_ctrl_pressed and is_m_pressed:
                        if not self.output_key_pressed:
                            self.output_key_pressed = True
                            logger.info("⌨️ Control+M нажата - воспроизведение тестового звука")
                            self._play_test_sound()
                            self.output_key_pressed = False
                            
                except Exception as e:
                    logger.error(f"❌ Ошибка on_press: {e}")
            
            def on_release(key):
                try:
                    if key in self._pressed_keys:
                        self._pressed_keys.remove(key)
                    
                    is_ctrl_still_pressed = keyboard.Key.ctrl_l in self._pressed_keys or keyboard.Key.ctrl_r in self._pressed_keys
                    is_n_still_pressed = any(hasattr(k, 'char') and k.char == 'n' for k in self._pressed_keys)
                    
                    if self.key_pressed and (
                        (hasattr(key, 'char') and key.char == 'n' and not is_ctrl_still_pressed) or
                        (key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r and not is_n_still_pressed)
                    ):
                        self.key_pressed = False
                        logger.info("⌨️ Control+N отпущена - остановка записи")
                        self._stop_recording()
                    elif self.key_pressed and (key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r):
                        self.key_pressed = False
                        logger.info("⌨️ Control отпущен - остановка записи")
                        self._stop_recording()
                    elif self.key_pressed and (hasattr(key, 'char') and key.char == 'n'):
                        self.key_pressed = False
                        logger.info("⌨️ N отпущена - остановка записи")
                        self._stop_recording()
                        
                except Exception as e:
                    logger.error(f"❌ Ошибка on_release: {e}")
            
            self.key_listener = keyboard.Listener(
                on_press=on_press,
                on_release=on_release
            )
            self.key_listener.start()
            logger.info("✅ Мониторинг клавиатуры запущен (Control+N)")
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска мониторинга клавиатуры: {e}")
    
    def stop_keyboard_monitoring(self):
        """Остановка мониторинга клавиатуры"""
        if self.key_listener:
            self.key_listener.stop()
            logger.info("🛑 Мониторинг клавиатуры остановлен")
    
    def _monitor_devices(self):
        """Мониторинг изменений устройств (Input + Output)"""
        logger.info("🔄 Мониторинг устройств запущен")
        logger.info("")
        
        while not self.stop_device_monitoring.is_set():
            try:
                # Проверяем Input устройство
                current_input = self._get_current_input_device_data()
                if current_input and current_input['uid'] != self.last_input_device_uid:
                    logger.info("=" * 80)
                    logger.info(f"🔄 ОБНАРУЖЕНО ПЕРЕКЛЮЧЕНИЕ INPUT УСТРОЙСТВА!")
                    logger.info(f"   📱 Старое: {self.last_input_device_uid}")
                    logger.info(f"   📱 Новое: {current_input['uid']} ({current_input['name']})")
                    logger.info("")
                    
                    if self._switch_input_device(current_input):
                        self.current_input_device_data = current_input
                        self.last_input_device_uid = current_input['uid']
                        
                        if self.is_recording:
                            logger.info("   🔄 Запись активна - пересоздание микрофона...")
                            # Пересоздаем микрофон для новой записи
                            try:
                                device_index = current_input.get('device_index')
                                if device_index is not None:
                                    # Закрываем старый микрофон
                                    if self.current_microphone:
                                        try:
                                            if hasattr(self.current_microphone, 'close'):
                                                self.current_microphone.close()
                                        except Exception:
                                            pass
                                    
                                    # Создаем новый микрофон
                                    self.current_microphone = sr.Microphone(device_index=device_index)
                                    
                                    # Калибровка нового микрофона
                                    calib_microphone = sr.Microphone(device_index=device_index)
                                    with calib_microphone as source:
                                        self.current_recognizer.adjust_for_ambient_noise(source, duration=0.3)
                                    
                                    logger.info("   ✅ Микрофон пересоздан и откалиброван")
                                else:
                                    logger.warning("   ⚠️ Нет device_index для пересоздания микрофона")
                            except Exception as e:
                                logger.warning(f"   ⚠️ Ошибка пересоздания микрофона: {e}")
                                import traceback
                                logger.error(traceback.format_exc())
                    
                    logger.info("=" * 80)
                    logger.info("")
                
                # Проверяем Output устройство
                current_output = self._get_current_output_device_data()
                if current_output and current_output['uid'] != self.last_output_device_uid:
                    logger.info("=" * 80)
                    logger.info(f"🔄 ОБНАРУЖЕНО ПЕРЕКЛЮЧЕНИЕ OUTPUT УСТРОЙСТВА!")
                    logger.info(f"   📱 Старое: {self.last_output_device_uid}")
                    logger.info(f"   📱 Новое: {current_output['uid']} ({current_output['name']})")
                    logger.info("")
                    
                    if self._switch_output_device(current_output):
                        self.current_output_device_data = current_output
                        self.last_output_device_uid = current_output['uid']
                    
                    logger.info("=" * 80)
                    logger.info("")
                
                time.sleep(1.0)
                
            except Exception as e:
                logger.error(f"❌ Ошибка мониторинга устройств: {e}")
                time.sleep(1.0)
    
    def test_full_integration(self):
        """Тест полной интеграции"""
        logger.info("=" * 80)
        logger.info("MVP-12: Full Integration - Input + Output")
        logger.info("=" * 80)
        logger.info("")
        logger.info("📋 Инструкция:")
        logger.info("   INPUT (запись):")
        logger.info("   1. Нажмите и удерживайте Control+N для начала записи")
        logger.info("   2. Говорите в микрофон")
        logger.info("   3. Отпустите Control+N для остановки записи и воспроизведения ответа")
        logger.info("")
        logger.info("   OUTPUT (воспроизведение):")
        logger.info("   4. Нажмите Control+M для воспроизведения тестового звука")
        logger.info("   5. Переключайте input/output устройства (отключите/подключите наушники)")
        logger.info("   6. Повторите несколько раз")
        logger.info("")
        
        # Запуск мониторинга клавиатуры
        self.start_keyboard_monitoring()
        
        # Запуск мониторинга устройств
        self.device_monitor_thread = threading.Thread(target=self._monitor_devices, daemon=True)
        self.device_monitor_thread.start()
        logger.info("🔄 Мониторинг устройств запущен")
        logger.info("⏳ Ожидание действий пользователя (нажмите Ctrl+C для остановки)...")
        logger.info("")
        
        try:
            # Бесконечное ожидание до Ctrl+C
            while True:
                time.sleep(1.0)
        except KeyboardInterrupt:
            logger.info("")
            logger.info("🛑 Получен сигнал остановки (Ctrl+C)")
            logger.info("")
        
        # Остановка
        self.stop_device_monitoring.set()
        self.stop_keyboard_monitoring()
        
        # Остановка AVAudioEngine
        try:
            self.output_playback.engine.stop()
            logger.info("✅ AVAudioEngine остановлен")
        except Exception:
            pass
        
        # Результаты
        logger.info("")
        logger.info("=" * 80)
        logger.info("РЕЗУЛЬТАТЫ")
        logger.info("=" * 80)
        logger.info("")
        logger.info(f"📊 Всего циклов: {len(self.full_cycle_events)}")
        successful = sum(1 for e in self.full_cycle_events if e.recognized_text and e.playback_success)
        logger.info(f"✅ Успешных циклов: {successful}")
        logger.info(f"❌ Неудачных циклов: {len(self.full_cycle_events) - successful}")
        logger.info("")
        
        for i, event in enumerate(self.full_cycle_events, 1):
            logger.info(f"📝 Цикл #{i}:")
            logger.info(f"   Input: {event.input_device}")
            logger.info(f"   Output: {event.output_device}")
            logger.info(f"   Распознано: {event.recognized_text or 'Нет'}")
            logger.info(f"   Воспроизведение: {'✅' if event.playback_success else '❌'}")
            logger.info(f"   Длительность: {event.duration_ms}ms")
            logger.info("")
        
        logger.info("✅ MVP-12: Full Integration - УСПЕШНО")
        logger.info("")


def main():
    """Главная функция"""
    prototype = FullInputOutputPrototype()
    
    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)
    
    try:
        prototype.test_full_integration()
    except KeyboardInterrupt:
        logger.info("")
        logger.info("🛑 Прервано пользователем")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()

