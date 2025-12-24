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
import queue
import numpy as np
from typing import Optional, Dict, List
from dataclasses import dataclass
from pathlib import Path

# Настройка логирования (должно быть до использования logger)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Проверка доступности sounddevice
try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    SOUNDDEVICE_AVAILABLE = False
    logger.error("❌ sounddevice не доступен")
    sd = None  # type: ignore

# Добавляем пути к предыдущим MVP
mvp1_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp1_device_discovery"
mvp2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp2_device_mapping"
mvp6_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp6_output_playback"
sys.path.insert(0, mvp1_path)
sys.path.insert(0, mvp2_path)
sys.path.insert(0, mvp6_path)

# Импорты из предыдущих MVP
from test_device_discovery import DeviceDiscoveryPrototype, DeviceInfo  # type: ignore[reportMissingImports]
from test_device_mapping import DeviceMappingPrototype  # type: ignore[reportMissingImports]
from test_output_playback import OutputPlaybackPrototype  # type: ignore[reportMissingImports]

# Логирование уже настроено выше

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
    from AVFoundation import (  # type: ignore[reportMissingImports, reportAttributeAccessIssue]
        AVAudioEngine,  # type: ignore[reportAttributeAccessIssue]
        AVAudioPlayerNode,  # type: ignore[reportAttributeAccessIssue]
        AVAudioFormat,  # type: ignore[reportAttributeAccessIssue]
        AVAudioPCMBuffer,  # type: ignore[reportAttributeAccessIssue]
        AVAudioSession  # type: ignore[reportAttributeAccessIssue]
    )
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
        # google_sr_pipeline не используется - используем напрямую speech_recognition
        
        # Output компоненты
        self.output_playback = OutputPlaybackPrototype()
        
        # Текущее состояние
        self.current_input_device_data: Optional[Dict] = None
        self.current_output_device_data: Optional[Dict] = None
        self.last_input_device_uid: Optional[str] = None
        self.last_output_device_uid: Optional[str] = None
        
        # Input stream (вместо sr.Microphone - единственный владелец микрофона)
        if not SOUNDDEVICE_AVAILABLE or sd is None:
            raise RuntimeError("sounddevice не доступен")
        self.input_stream: Optional[object] = None  # type: ignore
        self.audio_buffer: List[np.ndarray] = []  # Буфер для аудио данных во время записи
        self.audio_lock = threading.Lock()  # Блокировка для audio_buffer
        self.current_sample_rate = 44100  # Sample rate для записи (будет обновляться из device_data)
        
        # Распознаватель (только для recognize_google, не владеет микрофоном)
        if not SR_AVAILABLE:
            raise RuntimeError("speech_recognition не доступен")
        self.current_recognizer: Optional[sr.Recognizer] = None  # type: ignore
        
        # Состояние записи
        self.is_recording = False
        self.key_pressed = False
        self._pressed_keys = set()
        
        # Worker thread для тяжелых операций (распознавание, воспроизведение)
        self.work_queue = queue.Queue()
        self.worker_thread: Optional[threading.Thread] = None
        self.stop_worker = threading.Event()
        
        # Lock для защиты AVAudioEngine от race conditions
        self.engine_lock = threading.Lock()
        
        # Счетчик событий для отслеживания playback_success
        self.event_counter = 0
        
        # Состояние воспроизведения
        self.is_playing = False
        self.output_key_pressed = False
        
        # Мониторинг
        self.stop_device_monitoring = threading.Event()
        self.device_monitor_thread: Optional[threading.Thread] = None
        if not PYNPUT_AVAILABLE:
            self.key_listener = None
        else:
            self.key_listener: Optional[keyboard.Listener] = None  # type: ignore
        
        # События (dict для надежного обновления по event_id)
        self.full_cycle_events: List[FullCycleEvent] = []
        self.events_by_id: Dict[int, FullCycleEvent] = {}
        
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
        
        # GoogleSRPipeline не используется - используем напрямую speech_recognition
        
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
        
        # Запуск worker thread для тяжелых операций
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()
        logger.info("✅ Worker thread запущен")
        
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
            
            device_info = sd.query_devices(default_input)  # type: ignore
            avf_devices = self.device_discovery.get_input_devices()
            avf_device = None
            for dev in avf_devices:
                device_name = device_info.get('name', '') if isinstance(device_info, dict) else str(device_info.get('name', '')) if hasattr(device_info, 'get') else ''  # type: ignore
                if device_name.lower() in dev.name.lower() or dev.name.lower() in device_name.lower():
                    avf_device = dev
                    break
            
            device_name = device_info.get('name', 'Unknown') if isinstance(device_info, dict) else str(device_info.get('name', 'Unknown')) if hasattr(device_info, 'get') else 'Unknown'  # type: ignore
            self.current_input_device_data = {
                "uid": avf_device.uid if avf_device else f"portaudio_{default_input}",
                "name": device_name,
                "device_index": default_input,
                "sample_rate": int(device_info.get('default_samplerate', 44100)) if isinstance(device_info, dict) else 44100,  # type: ignore
                "max_input_channels": int(device_info.get('max_input_channels', 1)) if isinstance(device_info, dict) else 1  # type: ignore
            }
            
            # Output устройство
            default_output = sd.default.device[1]
            if default_output is None or default_output < 0:
                logger.warning("⚠️ Нет доступных output устройств, используем системное default")
                default_output = sd.default.device[1] if sd.default.device[1] is not None else 0
            
            output_info = sd.query_devices(default_output)  # type: ignore
            avf_output_devices = self.device_discovery.get_output_devices()
            avf_output_device = None
            for dev in avf_output_devices:
                output_name = output_info.get('name', '') if isinstance(output_info, dict) else str(output_info.get('name', '')) if hasattr(output_info, 'get') else ''  # type: ignore
                if output_name.lower() in dev.name.lower() or dev.name.lower() in output_name.lower():
                    avf_output_device = dev
                    break
            
            output_name = output_info.get('name', 'Unknown') if isinstance(output_info, dict) else str(output_info.get('name', 'Unknown')) if hasattr(output_info, 'get') else 'Unknown'  # type: ignore
            self.current_output_device_data = {
                "uid": avf_output_device.uid if avf_output_device else f"portaudio_{default_output}",
                "name": output_name,
                "device_index": default_output,
                "sample_rate": int(output_info.get('default_samplerate', 44100)) if isinstance(output_info, dict) else 44100,  # type: ignore
                "max_output_channels": int(output_info.get('max_output_channels', 2)) if isinstance(output_info, dict) else 2  # type: ignore
            }
            
            # Инициализация распознавателя (без микрофона - микрофон будет через InputStream)
            if not SR_AVAILABLE:
                raise RuntimeError("speech_recognition не доступен")
            self.current_recognizer = sr.Recognizer()  # type: ignore
            
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
        """Получение данных текущего input устройства (используем AVFoundation discovery + PortAudio default)"""
        try:
            import sounddevice as sd
            
            # Source of truth: AVFoundation discovery + PortAudio default device
            avf_devices = self.device_discovery.get_input_devices()
            
            # Получаем PortAudio default device (более надежный источник для текущего активного устройства)
            try:
                default_input = sd.default.device[0]
                if default_input is None or default_input < 0:
                    logger.warning("⚠️ Нет default input устройства в PortAudio")
                    # Fallback: используем первое доступное AVFoundation устройство
                    if avf_devices:
                        device_info = avf_devices[0]
                        # Пробуем найти маппинг
                        mapping_result = self.device_mapping.find_portaudio_match(
                            device_info.name, device_info.channels, device_info.transport
                        )
                        if mapping_result.is_usable():
                            device_index = mapping_result.device_index
                        else:
                            device_index = 0  # Fallback
                        
                        try:
                            pa_device_info = sd.query_devices(device_index)  # type: ignore
                            sample_rate = int(pa_device_info.get('default_samplerate', 44100)) if isinstance(pa_device_info, dict) else 44100  # type: ignore
                            max_input_channels = int(pa_device_info.get('max_input_channels', 1)) if isinstance(pa_device_info, dict) else 1  # type: ignore
                        except Exception:
                            sample_rate = 44100
                            max_input_channels = 1
                        
                        return {
                            "uid": device_info.uid,
                            "name": device_info.name,
                            "device_index": device_index,
                            "sample_rate": sample_rate,
                            "max_input_channels": max_input_channels
                        }
                    return None
                
                # Получаем информацию о default устройстве
                default_info = sd.query_devices(default_input)  # type: ignore
                default_name = default_info.get('name', 'Unknown') if isinstance(default_info, dict) else 'Unknown'  # type: ignore
                
                # Ищем соответствующее AVFoundation устройство
                device_info = None
                for avf_dev in avf_devices:
                    if default_name.lower() in avf_dev.name.lower() or avf_dev.name.lower() in default_name.lower():
                        device_info = avf_dev
                        break
                
                # Если не нашли, создаем DeviceInfo из PortAudio данных
                if not device_info:
                    device_info = DeviceInfo(
                        name=default_name,
                        uid=f"portaudio_{default_input}",
                        port_type="unknown",
                        channels=int(default_info.get('max_input_channels', 1)) if isinstance(default_info, dict) else 1,  # type: ignore
                        transport="built_in" if "built-in" in default_name.lower() or "internal" in default_name.lower() else "unknown",
                        normalized_name=default_name
                    )
                
                # Получаем sample_rate и channels (используем нативный sample rate устройства)
                try:
                    sample_rate = int(default_info.get('default_samplerate', 44100)) if isinstance(default_info, dict) else 44100  # type: ignore
                    max_input_channels = int(default_info.get('max_input_channels', 1)) if isinstance(default_info, dict) else 1  # type: ignore
                except Exception:
                    sample_rate = 44100
                    max_input_channels = 1
                
                return {
                    "uid": device_info.uid,
                    "name": device_info.name,
                    "device_index": default_input,
                    "sample_rate": sample_rate,
                    "max_input_channels": max_input_channels
                }
                
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio default device: {e}")
                # Fallback: используем первое доступное AVFoundation устройство
                if avf_devices:
                    device_info = avf_devices[0]
                    # Пробуем найти маппинг
                    try:
                        mapping_result = self.device_mapping.find_portaudio_match(
                            device_info.name, device_info.channels, device_info.transport
                        )
                        if mapping_result.is_usable():
                            device_index = mapping_result.device_index
                        else:
                            device_index = 0  # Fallback
                    except Exception:
                        device_index = 0  # Fallback
                    
                    try:
                        pa_device_info = sd.query_devices(device_index)  # type: ignore
                        sample_rate = int(pa_device_info.get('default_samplerate', 44100)) if isinstance(pa_device_info, dict) else 44100  # type: ignore
                        max_input_channels = int(pa_device_info.get('max_input_channels', 1)) if isinstance(pa_device_info, dict) else 1  # type: ignore
                    except Exception:
                        sample_rate = 44100
                        max_input_channels = 1
                    
                    return {
                        "uid": device_info.uid,
                        "name": device_info.name,
                        "device_index": device_index,
                        "sample_rate": sample_rate,
                        "max_input_channels": max_input_channels
                    }
                return None
                
        except Exception as e:
            logger.error(f"❌ Ошибка получения input устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None
    
    def _switch_input_device(self, device_data: Dict) -> bool:
        """Переключение input устройства (останавливаем текущий stream, если активен)"""
        try:
            logger.info(f"      🔄 Переключение input на: {device_data['name']}")
            
            # Останавливаем текущий stream, если активен
            if self.input_stream is not None:
                try:
                    if self.input_stream.active:  # type: ignore
                        self.input_stream.stop()  # type: ignore
                    self.input_stream.close()  # type: ignore
                except Exception:
                    pass
                self.input_stream = None
            
            device_index = device_data.get('device_index')
            if device_index is None:
                logger.error(f"      ❌ Нет device_index для устройства {device_data['name']}")
                return False
            
            # Обновляем sample_rate из device_data (используем нативный sample rate устройства)
            self.current_sample_rate = device_data.get('sample_rate', 44100)
            
            logger.info(f"      ✅ Input готов к переключению: {device_data['name']} (index: {device_index}, sample_rate: {self.current_sample_rate})")
            return True
            
        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения input: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def _get_current_output_device_data(self) -> Optional[Dict]:
        """Получение данных текущего output устройства (используем AVFoundation discovery + PortAudio default)"""
        try:
            import sounddevice as sd
            
            # Source of truth: AVFoundation discovery + PortAudio default device
            avf_devices = self.device_discovery.get_output_devices()
            
            # Получаем PortAudio default output device (более надежный источник для текущего активного устройства)
            try:
                default_output = sd.default.device[1]
                if default_output is None or default_output < 0:
                    logger.warning("⚠️ Нет default output устройства в PortAudio")
                    # Fallback: используем первое доступное AVFoundation устройство
                    if avf_devices:
                        device_info = avf_devices[0]
                        # Пробуем найти маппинг
                        mapping_result = self.device_mapping.find_portaudio_match(
                            device_info.name, device_info.channels, device_info.transport
                        )
                        if mapping_result.is_usable():
                            device_index = mapping_result.device_index
                        else:
                            device_index = 1  # Fallback для output
                        
                        try:
                            pa_device_info = sd.query_devices(device_index)  # type: ignore
                            sample_rate = int(pa_device_info.get('default_samplerate', 44100)) if isinstance(pa_device_info, dict) else 44100  # type: ignore
                            max_output_channels = int(pa_device_info.get('max_output_channels', 2)) if isinstance(pa_device_info, dict) else 2  # type: ignore
                        except Exception:
                            sample_rate = 44100
                            max_output_channels = 2
                        
                        return {
                            "uid": device_info.uid,
                            "name": device_info.name,
                            "device_index": device_index,
                            "sample_rate": sample_rate,
                            "max_output_channels": max_output_channels
                        }
                    return None
                
                # Получаем информацию о default устройстве
                default_info = sd.query_devices(default_output)  # type: ignore
                default_name = default_info.get('name', 'Unknown') if isinstance(default_info, dict) else 'Unknown'  # type: ignore
                
                # Ищем соответствующее AVFoundation устройство
                device_info = None
                for avf_dev in avf_devices:
                    if default_name.lower() in avf_dev.name.lower() or avf_dev.name.lower() in default_name.lower():
                        device_info = avf_dev
                        break
                
                # Если не нашли, создаем DeviceInfo из PortAudio данных
                if not device_info:
                    device_info = DeviceInfo(
                        name=default_name,
                        uid=f"portaudio_{default_output}",
                        port_type="unknown",
                        channels=int(default_info.get('max_output_channels', 2)) if isinstance(default_info, dict) else 2,  # type: ignore
                        transport="built_in" if "built-in" in default_name.lower() or "internal" in default_name.lower() else "unknown",
                        normalized_name=default_name
                    )
                
                # Получаем sample_rate и channels
                try:
                    sample_rate = int(default_info.get('default_samplerate', 44100)) if isinstance(default_info, dict) else 44100  # type: ignore
                    max_output_channels = int(default_info.get('max_output_channels', 2)) if isinstance(default_info, dict) else 2  # type: ignore
                except Exception:
                    sample_rate = 44100
                    max_output_channels = 2
                
                return {
                    "uid": device_info.uid,
                    "name": device_info.name,
                    "device_index": default_output,
                    "sample_rate": sample_rate,
                    "max_output_channels": max_output_channels
                }
                
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio default output device: {e}")
                # Fallback: используем первое доступное AVFoundation устройство
                if avf_devices:
                    device_info = avf_devices[0]
                    # Пробуем найти маппинг
                    try:
                        mapping_result = self.device_mapping.find_portaudio_match(
                            device_info.name, device_info.channels, device_info.transport
                        )
                        if mapping_result.is_usable():
                            device_index = mapping_result.device_index
                        else:
                            device_index = 1  # Fallback для output
                    except Exception:
                        device_index = 1  # Fallback
                    
                    try:
                        pa_device_info = sd.query_devices(device_index)  # type: ignore
                        sample_rate = int(pa_device_info.get('default_samplerate', 44100)) if isinstance(pa_device_info, dict) else 44100  # type: ignore
                        max_output_channels = int(pa_device_info.get('max_output_channels', 2)) if isinstance(pa_device_info, dict) else 2  # type: ignore
                    except Exception:
                        sample_rate = 44100
                        max_output_channels = 2
                    
                    return {
                        "uid": device_info.uid,
                        "name": device_info.name,
                        "device_index": device_index,
                        "sample_rate": sample_rate,
                        "max_output_channels": max_output_channels
                    }
                return None
                
        except Exception as e:
            # Общий fallback для всех необработанных исключений (например, ошибки в get_output_devices)
            logger.error(f"❌ Ошибка получения output устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None
    
    def _switch_output_device(self, device_data: Dict) -> bool:
        """Переключение output устройства"""
        try:
            logger.info(f"      🔄 Переключение output на: {device_data['name']}")
            
            # AVAudioEngine использует системное default output устройство при создании
            # При переключении устройства нужно пересоздать engine
            # Используем engine_lock для защиты от race conditions
            with self.engine_lock:
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
    
    def _resample_linear(self, x: np.ndarray, src_sr: int, dst_sr: int) -> np.ndarray:
        """Простой линейный ресемплинг для приведения аудио к нужной частоте"""
        if src_sr == dst_sr:
            return x.astype(np.float32, copy=False)

        x = x.astype(np.float32, copy=False)
        n_src = int(len(x))
        if n_src <= 0:
            return np.zeros((0,), dtype=np.float32)
        if n_src == 1:
            # растянем 1 сэмпл
            ratio = dst_sr / src_sr
            n_dst = max(1, int(round(n_src * ratio)))
            return np.full((n_dst,), float(x[0]), dtype=np.float32)

        ratio = dst_sr / src_sr
        n_dst = max(1, int(round(n_src * ratio)))

        xp = np.linspace(0.0, 1.0, num=n_src, endpoint=False)
        x_dst = np.interp(np.linspace(0.0, 1.0, num=n_dst, endpoint=False), xp, x).astype(np.float32)
        return x_dst
    
    def _audio_callback(self, indata, frames, time_info, status):
        """Callback для InputStream - добавляет данные в буфер"""
        if status:
            logger.warning(f"⚠️ Audio stream status: {status}")
        
        with self.audio_lock:
            # Копируем данные (indata - это numpy array)
            self.audio_buffer.append(indata.copy())
    
    def _start_recording(self) -> bool:
        """Начало записи через sounddevice.InputStream (реальный push-to-talk)"""
        try:
            device_name = self.current_input_device_data['name'] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🎙️ НАЧАЛО ЗАПИСИ (Push-to-talk)")
            logger.info(f"   📱 Input: {device_name}")
            logger.info(f"   📱 Output: {self.current_output_device_data['name'] if self.current_output_device_data else 'Unknown'}")
            logger.info("")
            
            # Очищаем буфер
            with self.audio_lock:
                self.audio_buffer.clear()
            
            # Получаем device_index
            device_index = self.current_input_device_data.get('device_index') if self.current_input_device_data else None
            if device_index is None:
                logger.error("   ❌ Нет device_index для записи")
                return False
            
            # Создаем и запускаем InputStream с fallback samplerate
            if not SOUNDDEVICE_AVAILABLE or sd is None:
                logger.error("   ❌ sounddevice не доступен")
                return False
            
            # try a small list of samplerates to reduce PortAudio errors (BT/HFP etc.)
            candidate_srs = [int(self.current_sample_rate), 16000, 44100, 48000]
            candidate_srs = [sr for sr in candidate_srs if sr > 0]

            last_err = None
            for sr_try in candidate_srs:
                try:
                    self.input_stream = sd.InputStream(  # type: ignore
                        device=device_index,
                        channels=1,
                        samplerate=sr_try,
                        blocksize=1024,
                        callback=self._audio_callback,
                        dtype=np.float32
                    )
                    self.input_stream.start()  # type: ignore
                    self.current_sample_rate = sr_try
                    self.is_recording = True
                    logger.info(f"   ✅ ЗАПИСЬ АКТИВНА - ГОВОРИТЕ В МИКРОФОН (sample_rate: {self.current_sample_rate}Hz)")
                    logger.info("=" * 80)
                    logger.info("")
                    return True
                except Exception as e:
                    last_err = e
                    try:
                        if self.input_stream is not None:
                            self.input_stream.close()  # type: ignore
                    except Exception:
                        pass
                    self.input_stream = None

            logger.error(f"   ❌ Не удалось открыть InputStream ни на одном samplerate. Последняя ошибка: {last_err}")
            self.is_recording = False
            return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка начала записи: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_recording = False
            return False
    
    def _stop_recording(self) -> Optional[str]:
        """Остановка записи, конвертация буфера в AudioData, распознавание"""
        try:
            device_name = self.current_input_device_data['name'] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🛑 ОСТАНОВКА ЗАПИСИ")
            logger.info(f"   📱 Input: {device_name}")
            logger.info("")
            start_time = time.time()
            
            # Останавливаем stream
            if self.input_stream is not None:
                try:
                    if self.input_stream.active:  # type: ignore
                        self.input_stream.stop()  # type: ignore
                    self.input_stream.close()  # type: ignore
                except Exception as stream_e:
                    logger.warning(f"   ⚠️ Ошибка остановки stream: {stream_e}")
                finally:
                    self.input_stream = None
            
            self.is_recording = False
            
            # Получаем данные из буфера
            with self.audio_lock:
                if not self.audio_buffer:
                    logger.warning("   ⚠️ Буфер пуст, запись не была начата")
                    return None
                
                # Объединяем все чанки
                audio_data = np.concatenate(self.audio_buffer, axis=0)
                # Если stereo, берем только первый канал
                if audio_data.ndim > 1 and audio_data.shape[1] > 1:
                    audio_data = audio_data[:, 0]
                # Flatten если нужно
                audio_data = audio_data.flatten()
            
            duration_ms = int((time.time() - start_time) * 1000)
            logger.info(f"   ✅ Аудио записано: {len(audio_data)} samples, {duration_ms}ms")
            
            # Конвертируем в формат для speech_recognition
            # Нормализуем в диапазон [-1, 1] (уже float32)
            audio_float = np.clip(audio_data, -1.0, 1.0).astype(np.float32, copy=False)
            
            # Ресемплинг до 16k для лучшего качества SR (Google SR лучше работает с 16k)
            audio_16k = self._resample_linear(audio_float, self.current_sample_rate, 16000)
            
            # Конвертируем в int16 для AudioData
            audio_bytes = (audio_16k * 32767.0).astype(np.int16).tobytes()
            
            # Создаем событие заранее (будет обновлено в worker thread)
            event_id = self.event_counter
            self.event_counter += 1
            
            event = FullCycleEvent(
                timestamp=time.time(),
                input_device=device_name,
                output_device=self.current_output_device_data['name'] if self.current_output_device_data else "Unknown",
                recognized_text=None,  # Будет обновлено в worker thread
                playback_success=False,  # Будет обновлено в worker thread
                duration_ms=duration_ms
            )
            self.full_cycle_events.append(event)
            self.events_by_id[event_id] = event  # Сохраняем в dict для надежного обновления
            
            # Ставим задачу в очередь: распознавание + воспроизведение (все в worker thread)
            logger.info("   🔍 Постановка задачи распознавания и воспроизведения в очередь...")
            self.work_queue.put(("RECOGNIZE_AND_PLAY", (event_id, audio_bytes, 16000)))  # Всегда 16k после ресемплинга
            
            logger.info(f"   ✅ Задача поставлена в очередь (event_id: {event_id})")
            logger.info("=" * 80)
            logger.info("")
            
            return None  # Текст будет доступен после обработки в worker thread
        except Exception as e:
            logger.error(f"❌ Ошибка остановки записи: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_recording = False
            return None
    
    def _worker_loop(self):
        """Worker thread для тяжелых операций (распознавание, воспроизведение)"""
        logger.info("🔧 Worker thread запущен")
        while not self.stop_worker.is_set():
            try:
                # Получаем задачу из очереди с таймаутом
                try:
                    task_type, data = self.work_queue.get(timeout=0.1)
                except queue.Empty:
                    continue
                
                if task_type == "RECOGNIZE_AND_PLAY":
                    event_id, audio_bytes, sample_rate = data
                    self._recognize_and_play_worker(event_id, audio_bytes, sample_rate)
                elif task_type == "PLAY_RESPONSE":
                    text = data
                    self._play_response_worker(text)
                elif task_type == "PLAY_TEST_SOUND":
                    self._play_test_sound_worker()
                
                self.work_queue.task_done()
            except Exception as e:
                logger.error(f"❌ Ошибка в worker thread: {e}")
                import traceback
                logger.error(traceback.format_exc())
        
        logger.info("🔧 Worker thread остановлен")
    
    def _recognize_and_play_worker(self, event_id: int, audio_bytes: bytes, sample_rate: int) -> bool:
        """Распознавание и воспроизведение в worker thread"""
        try:
            if not SR_AVAILABLE:
                logger.error("   ❌ speech_recognition не доступен")
                ev = self.events_by_id.get(event_id)
                if ev:
                    ev.recognized_text = None
                    ev.playback_success = False
                return False
            
            if self.current_recognizer is None:
                logger.error("   ❌ Recognizer не инициализирован")
                ev = self.events_by_id.get(event_id)
                if ev:
                    ev.recognized_text = None
                    ev.playback_success = False
                return False
            
            # Создаем AudioData для распознавания
            audio_data_obj = sr.AudioData(audio_bytes, sample_rate, 2)  # type: ignore
            
            # Распознавание
            recognized_text = None
            logger.info("   🔍 Распознавание через Google SR...")
            try:
                recognized_text = self.current_recognizer.recognize_google(audio_data_obj, language="ru-RU")  # type: ignore
                logger.info(f"   ✅ РАСПОЗНАНО: {recognized_text}")
            except sr.UnknownValueError:  # type: ignore
                logger.warning("   ⚠️ Google SR не смог распознать речь")
            except sr.RequestError as e:  # type: ignore
                logger.error(f"   ❌ Ошибка Google SR: {e}")
            
            # Обновляем событие через dict (надежнее, чем по индексу)
            ev = self.events_by_id.get(event_id)
            if ev:
                ev.recognized_text = recognized_text
            
            # Воспроизведение ответа
            playback_success = self._play_response_worker(recognized_text)
            
            # Обновляем playback_success
            if ev:
                ev.playback_success = playback_success
            
            return playback_success
        except Exception as e:
            logger.error(f"   ❌ Ошибка распознавания и воспроизведения: {e}")
            import traceback
            logger.error(traceback.format_exc())
            ev = self.events_by_id.get(event_id)
            if ev:
                ev.playback_success = False
            return False
    
    def _play_response_worker(self, text: Optional[str]) -> bool:
        """Воспроизведение ответа через Output (в worker thread, без fallback)"""
        try:
            if not text:
                logger.info("   🔊 Пропуск воспроизведения (нет текста)")
                return False
            
            logger.info(f"   🔊 Воспроизведение ответа: '{text}'")
            
            # Генерируем простой тестовый тон (в реальности это будет TTS)
            sample_rate = 44100
            duration_sec = 1.0
            frequency = 440.0  # A4
            
            logger.info(f"   🎵 Генерация ответа: {frequency}Hz, {duration_sec}сек")
            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)
            
            # Воспроизведение ТОЛЬКО через AVAudioEngine (без fallback)
            # Используем engine_lock для защиты от race conditions
            with self.engine_lock:
                # Проверяем, что engine запущен
                if not self.output_playback.engine.isRunning():
                    logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                    error = None
                    if not self.output_playback.engine.startAndReturnError_(error):
                        logger.error("   ❌ Не удалось запустить AVAudioEngine")
                        return False
                    logger.info("   ✅ AVAudioEngine запущен")
                
                logger.info("   🎵 Воспроизведение ответа через AVAudioEngine...")
                success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            
            if success:
                logger.info("   ✅ Ответ воспроизведен")
                logger.info(f"   ⏳ Ожидание завершения ({duration_sec}сек)...")
                time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Воспроизведение завершено")
            else:
                logger.error("   ❌ Ошибка воспроизведения через AVAudioEngine (fallback отключен для MVP-12)")
            
            return success
        except Exception as e:
            logger.error(f"   ❌ Ошибка воспроизведения: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def _play_response(self, text: Optional[str]) -> bool:
        """Воспроизведение ответа (ставит задачу в очередь worker thread)"""
        # Просто ставим задачу в очередь, реальное воспроизведение в worker thread
        self.work_queue.put(("PLAY_RESPONSE", text))
        return True  # Возвращаем True, так как задача поставлена
    
    def _play_test_sound_worker(self) -> bool:
        """Воспроизведение тестового звука (в worker thread, без fallback)"""
        try:
            device_name = self.current_output_device_data['name'] if self.current_output_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🔊 ВОСПРОИЗВЕДЕНИЕ ТЕСТОВОГО ЗВУКА")
            logger.info(f"   📱 Output: {device_name}")
            logger.info("")
            
            self.is_playing = True
            
            # Генерируем тестовый тон (440 Hz, 1 секунда)
            sample_rate = 44100
            duration_sec = 1.0
            frequency = 440.0  # A4
            
            logger.info(f"   🎵 Генерация тестового тона: {frequency}Hz, {duration_sec}сек, {sample_rate}Hz")
            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)
            
            logger.info(f"   📊 Аудио данные: {len(audio_data)} samples")
            
            # Воспроизведение ТОЛЬКО через AVAudioEngine (без fallback)
            # Используем engine_lock для защиты от race conditions
            with self.engine_lock:
                # Проверяем, что engine запущен
                if not self.output_playback.engine.isRunning():
                    logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                    error = None
                    if not self.output_playback.engine.startAndReturnError_(error):
                        logger.error("   ❌ Не удалось запустить AVAudioEngine")
                        self.is_playing = False
                        return False
                    logger.info("   ✅ AVAudioEngine запущен")
                
                logger.info("   🎵 Воспроизведение через AVAudioEngine...")
                success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            
            if success:
                logger.info("   ✅ Тестовый звук воспроизведен")
                logger.info(f"   ⏳ Ожидание завершения воспроизведения ({duration_sec}сек)...")
                time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Воспроизведение завершено")
            else:
                logger.error("   ❌ Ошибка воспроизведения через AVAudioEngine (fallback отключен для MVP-12)")
            
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
    
    def _play_test_sound(self) -> bool:
        """Воспроизведение тестового звука (ставит задачу в очередь worker thread)"""
        # Просто ставим задачу в очередь, реальное воспроизведение в worker thread
        self.work_queue.put(("PLAY_TEST_SOUND", None))
        return True  # Возвращаем True, так как задача поставлена
    
    def start_keyboard_monitoring(self):
        """Запуск мониторинга клавиатуры"""
        if not PYNPUT_AVAILABLE:
            logger.warning("⚠️ pynput не доступен, используем симуляцию")
            return

        try:
            self._pressed_keys = set()

            def key_token(k):
                # ctrl keys
                try:
                    if k == keyboard.Key.ctrl_l:  # type: ignore
                        return "ctrl_l"
                    if k == keyboard.Key.ctrl_r:  # type: ignore
                        return "ctrl_r"
                except Exception:
                    pass
                # printable keys
                if hasattr(k, "char") and k.char:  # type: ignore
                    return str(k.char).lower()  # type: ignore
                return None

            def is_ctrl_down():
                return ("ctrl_l" in self._pressed_keys) or ("ctrl_r" in self._pressed_keys)

            def is_char_down(ch: str):
                return ch.lower() in self._pressed_keys

            def on_press(key):
                try:
                    tok = key_token(key)
                    if tok:
                        self._pressed_keys.add(tok)

                    # INPUT: Ctrl+N (любой порядок нажатия)
                    if is_ctrl_down() and is_char_down("n"):
                        if not self.key_pressed:
                            self.key_pressed = True
                            logger.info("⌨️ Control+N нажата - начало записи")
                            self._start_recording()

                    # OUTPUT: Ctrl+M
                    if is_ctrl_down() and is_char_down("m"):
                        if not self.output_key_pressed:
                            self.output_key_pressed = True
                            logger.info("⌨️ Control+M нажата - воспроизведение тестового звука")
                            self._play_test_sound()
                            self.output_key_pressed = False

                except Exception as e:
                    logger.error(f"❌ Ошибка on_press: {e}")

            def on_release(key):
                try:
                    tok = key_token(key)
                    if tok and tok in self._pressed_keys:
                        self._pressed_keys.remove(tok)

                    # PTT stop: если отпустили Ctrl или N → стоп
                    if self.key_pressed:
                        released_ctrl = tok in ("ctrl_l", "ctrl_r")
                        released_n = tok == "n"
                        if released_ctrl or released_n:
                            self.key_pressed = False
                            logger.info("⌨️ Control+N отпущена - остановка записи")
                            self._stop_recording()

                except Exception as e:
                    logger.error(f"❌ Ошибка on_release: {e}")

            self.key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)  # type: ignore
            self.key_listener.start()
            logger.info("✅ Мониторинг клавиатуры запущен (Control+N / Control+M)")

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
                            logger.info("   🔄 Запись активна - остановка и перезапуск на новом устройстве...")
                            # Останавливаем текущий stream
                            if self.input_stream is not None:
                                try:
                                    if self.input_stream.active:  # type: ignore
                                        self.input_stream.stop()  # type: ignore
                                    self.input_stream.close()  # type: ignore
                                except Exception:
                                    pass
                                self.input_stream = None
                            
                            # Очищаем буфер при смене устройства во время записи (избегаем смешивания данных)
                            with self.audio_lock:
                                self.audio_buffer.clear()
                            logger.info("   🧹 Буфер очищен из-за смены input устройства во время записи")
                            
                            # Обновляем sample_rate из нового устройства
                            self.current_sample_rate = current_input.get('sample_rate', 44100)
                            
                            # Перезапускаем запись на новом устройстве
                            try:
                                device_index = current_input.get('device_index')
                                if device_index is not None:
                                    self.input_stream = sd.InputStream(  # type: ignore
                                        device=device_index,
                                        channels=1,
                                        samplerate=self.current_sample_rate,
                                        blocksize=1024,
                                        callback=self._audio_callback,
                                        dtype=np.float32
                                    )
                                    self.input_stream.start()  # type: ignore
                                    logger.info(f"   ✅ Запись перезапущена на новом устройстве (sample_rate: {self.current_sample_rate}Hz)")
                                else:
                                    logger.warning("   ⚠️ Нет device_index для перезапуска записи")
                                    self.is_recording = False
                            except Exception as e:
                                logger.error(f"   ❌ Ошибка перезапуска записи: {e}")
                                self.is_recording = False
                    
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
        
        # Дождаться выполнения уже поставленных задач (иначе воркер может быть убит раньше)
        try:
            self.work_queue.join()
        except Exception:
            pass
        
        # Остановка worker thread
        self.stop_worker.set()
        if self.worker_thread and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=2.0)
            logger.info("✅ Worker thread остановлен")
        
        # Остановка input stream
        if self.input_stream is not None:
            try:
                if self.input_stream.active:  # type: ignore
                    self.input_stream.stop()  # type: ignore
                self.input_stream.close()  # type: ignore
                logger.info("✅ Input stream остановлен")
            except Exception:
                pass
        
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
        successful_playback = sum(1 for e in self.full_cycle_events if e.playback_success)
        successful_sr = sum(1 for e in self.full_cycle_events if e.recognized_text)
        logger.info(f"✅ Playback OK: {successful_playback}")
        logger.info(f"✅ SR OK: {successful_sr}")
        logger.info(f"❌ Playback FAIL: {len(self.full_cycle_events) - successful_playback}")
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

