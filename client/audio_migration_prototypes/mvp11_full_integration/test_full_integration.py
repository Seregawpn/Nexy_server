"""
MVP-11: Full Integration - Push-to-Talk + Device Switching + Google SR

Цель: Интеграция всех компонентов:
- Push-to-talk (клавиша) → активация микрофона
- Переключение устройств во время работы
- Запись речи через Google SR
- Распознавание речи

Exit Gate:
- [ ] Push-to-talk активирует микрофон на текущем устройстве
- [ ] Переключение устройств работает во время активной записи
- [ ] Запись продолжается после переключения устройства
- [ ] Распознавание речи работает корректно
"""

import sys
import os
import time
import logging
import threading
from typing import Optional, Dict, List
from dataclasses import dataclass

# Добавляем пути к предыдущим MVP
mvp1_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp1_device_discovery"
mvp2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp2_device_mapping"
mvp5_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp5_input_google_sr"
sys.path.insert(0, mvp1_path)
sys.path.insert(0, mvp2_path)
sys.path.insert(0, mvp5_path)

# Импорты из предыдущих MVP
from test_device_discovery import DeviceDiscoveryPrototype
from test_device_mapping import DeviceMappingPrototype
from test_input_google_sr_pipeline import GoogleSRPipelinePrototype

# Импорты для push-to-talk
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    logging.warning("⚠️ pynput не доступен, push-to-talk будет симулирован")

import speech_recognition as sr

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class RecordingEvent:
    """Событие записи"""
    timestamp: float
    device_name: str
    device_index: int
    sample_rate: int
    duration_ms: int
    recognized_text: Optional[str] = None
    error: Optional[str] = None


class FullIntegrationPrototype:
    """Полная интеграция: Push-to-Talk + Device Switching + Google SR"""
    
    def __init__(self):
        self.device_discovery = DeviceDiscoveryPrototype()
        self.device_mapping = DeviceMappingPrototype()
        self.google_sr_pipeline = GoogleSRPipelinePrototype()
        
        # Состояние
        self.is_recording = False
        self.current_device_data: Optional[Dict] = None
        self.current_microphone: Optional[sr.Microphone] = None
        self.current_recognizer = sr.Recognizer()
        
        # События
        self.recording_events: List[RecordingEvent] = []
        
        # Push-to-talk
        self.key_pressed = False
        self.key_listener: Optional[keyboard.Listener] = None
        self.monitoring_thread: Optional[threading.Thread] = None
        self.stop_monitoring = threading.Event()
        
        # Мониторинг устройств
        self.device_monitoring_thread: Optional[threading.Thread] = None
        self.stop_device_monitoring = threading.Event()
        self.last_device_uid: Optional[str] = None
        
    def setup(self) -> bool:
        """Инициализация компонентов"""
        logger.info("📋 Инициализация компонентов...")
        
        # Настройка AVAudioSession
        if not self.device_discovery.setup_audio_session():
            logger.error("❌ Не удалось настроить AVAudioSession")
            return False
        
        # Инициализация маппинга
        if not self.device_mapping.setup():
            logger.error("❌ Не удалось инициализировать device mapping")
            return False
        
        # Получаем начальное устройство
        initial_device = self._get_current_device_data()
        if not initial_device:
            logger.error("❌ Не удалось получить начальное устройство")
            return False
        
        self.current_device_data = initial_device
        self.last_device_uid = initial_device['uid']
        
        # Инициализируем микрофон на начальном устройстве
        if not self._switch_to_device(initial_device):
            logger.error("❌ Не удалось инициализировать микрофон")
            return False
        
        logger.info(f"✅ Инициализация завершена")
        logger.info(f"   Начальное устройство: {self.current_device_data['name']}")
        logger.info(f"   PortAudio index: {self.current_device_data['device_index']}")
        logger.info("")
        
        return True
    
    def _get_current_device_data(self) -> Optional[Dict]:
        """Получение данных текущего устройства (используем логику из MVP-10)"""
        try:
            import sounddevice as sd
            from AVFoundation import AVAudioSession
            
            # ВАЖНО: Получаем все устройства через PortAudio (включая встроенный микрофон)
            # AVFoundation может не показывать встроенный микрофон, когда Bluetooth подключен
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
                except Exception as reinit_e:
                    logger.error(f"❌ Не удалось переинициализировать PortAudio: {reinit_e}")
            
            # Получаем текущее устройство через AVFoundation
            session = AVAudioSession.sharedInstance()
            current_route = session.currentRoute()
            current_inputs = current_route.inputs() if current_route else []
            
            # Получаем список всех доступных устройств через AVFoundation
            avf_devices = self.device_discovery.get_input_devices()
            
            device_info = None
            device_uid = None
            device_name = None
            current_portaudio_index = None
            
            # Если есть текущее устройство в route, используем его
            if current_inputs and len(current_inputs) > 0:
                port = current_inputs[0]
                
                # Получаем UID и имя
                if hasattr(port, 'uid'):
                    device_uid = port.uid()
                elif hasattr(port, 'portName'):
                    device_uid = port.portName()
                
                if hasattr(port, 'portName'):
                    device_name = port.portName()
                
                # Ищем устройство в списке доступных AVFoundation
                for dev in avf_devices:
                    if dev.uid == device_uid or dev.name == device_name:
                        device_info = dev
                        break
                
                # Если не найдено в AVFoundation, ищем в PortAudio по имени
                if not device_info and device_name:
                    for pa_dev in all_portaudio_devices:
                        if device_name.lower() in pa_dev['name'].lower() or pa_dev['name'].lower() in device_name.lower():
                            current_portaudio_index = pa_dev['index']
                            break
            
            # Если текущее устройство не найдено или недоступно, используем fallback
            if not device_info and not current_portaudio_index:
                # Fallback: используем системное default устройство или первое доступное
                try:
                    default_input = sd.default.device[0]  # (input, output)
                    if default_input is not None and default_input >= 0:
                        default_info = sd.query_devices(default_input)
                        current_portaudio_index = default_input
                        device_name = default_info.get('name', 'Unknown')
                    elif all_portaudio_devices:
                        # Используем первое доступное устройство
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        logger.error("❌ Нет доступных устройств")
                        return None
                except Exception as e:
                    logger.error(f"❌ Ошибка получения default устройства: {e}")
                    if all_portaudio_devices:
                        current_portaudio_index = all_portaudio_devices[0]['index']
                        device_name = all_portaudio_devices[0]['name']
                    else:
                        return None
            
            # Если нашли через PortAudio, но не через AVFoundation, создаем device_info из PortAudio
            if current_portaudio_index is not None and not device_info:
                pa_device = None
                for pa_dev in all_portaudio_devices:
                    if pa_dev['index'] == current_portaudio_index:
                        pa_device = pa_dev
                        break
                
                if pa_device:
                    # Создаем DeviceInfo из PortAudio данных
                    from test_device_discovery import DeviceInfo
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
                logger.error("❌ Не удалось получить устройство")
                return None
            
            # Получаем маппинг на PortAudio
            # Если уже знаем PortAudio index, используем его напрямую
            if current_portaudio_index is not None:
                # Создаем простой объект для mapping_result
                class SimpleMappingResult:
                    def __init__(self, device_index):
                        self.device_index = device_index
                        self.confidence = 'high'
                    def is_usable(self):
                        return True
                
                mapping_result = SimpleMappingResult(current_portaudio_index)
            else:
                mapping_result = self.device_mapping.find_portaudio_match(
                    device_info.name, device_info.channels, device_info.transport
                )
                
                if not mapping_result.is_usable():
                    logger.warning(f"⚠️ Маппинг для {device_info.name} не найден, используем системное default")
                    try:
                        default_input = sd.default.device[0]
                        if default_input is None or default_input < 0:
                            logger.error("❌ Нет доступных устройств")
                            return None
                        mapping_result = SimpleMappingResult(default_input)
                    except Exception as e:
                        logger.error(f"❌ Ошибка получения default устройства: {e}")
                        return None
            
            # Получаем технические данные из PortAudio
            try:
                pa_device_info = sd.query_devices(mapping_result.device_index)
                sample_rate = int(pa_device_info.get('default_samplerate', 44100))
                max_input_channels = int(pa_device_info.get('max_input_channels', 1))
            except Exception as e:
                logger.warning(f"⚠️ Ошибка получения PortAudio данных: {e}")
                sample_rate = 44100
                max_input_channels = 1
            
            device_data = {
                "uid": device_info.uid,
                "name": device_info.name,
                "device_index": mapping_result.device_index,
                "sample_rate": sample_rate,
                "max_input_channels": max_input_channels
            }
            
            return device_data
                
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None
    
    def _switch_to_device(self, device_data: Dict) -> bool:
        """Переключение на новое устройство"""
        try:
            logger.info(f"      🔄 Переключение на устройство: {device_data['name']}")
            
            # Закрываем текущий микрофон
            if self.current_microphone:
                try:
                    logger.info(f"      🛑 Закрытие текущего микрофона...")
                    if hasattr(self.current_microphone, 'close'):
                        self.current_microphone.close()
                    logger.info(f"      ✅ Текущий микрофон закрыт")
                except Exception as e:
                    logger.warning(f"      ⚠️ Ошибка закрытия микрофона: {e}")
                self.current_microphone = None
            
            # Создаем новый микрофон
            device_index = device_data['device_index']
            logger.info(f"      🎙️ Создание нового микрофона (index: {device_index})...")
            self.current_microphone = sr.Microphone(device_index=device_index)
            logger.info(f"      ✅ Микрофон создан: {device_data['name']} (index: {device_index})")
            return True
            
        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def _start_recording(self) -> bool:
        """Начало записи"""
        if self.is_recording:
            logger.warning("⚠️ Запись уже активна")
            return False
        
        if not self.current_microphone:
            logger.error("❌ Микрофон не инициализирован, пытаемся инициализировать...")
            if not self.current_device_data:
                logger.error("❌ Нет данных устройства")
                return False
            if not self._switch_to_device(self.current_device_data):
                logger.error("❌ Не удалось инициализировать микрофон")
                return False
        
        try:
            device_name = self.current_device_data['name'] if self.current_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🎙️ НАЧАЛО ЗАПИСИ")
            logger.info(f"   📱 Устройство: {device_name}")
            logger.info(f"   📊 PortAudio index: {self.current_device_data['device_index'] if self.current_device_data else 'N/A'}")
            logger.info(f"   📊 Sample rate: {self.current_device_data['sample_rate'] if self.current_device_data else 'N/A'}Hz")
            logger.info("")
            self.is_recording = True
            
            # Калибровка для окружающего шума (быстрая, неблокирующая)
            try:
                logger.info("   🔊 Калибровка для окружающего шума...")
                with self.current_microphone as source:
                    self.current_recognizer.adjust_for_ambient_noise(source, duration=0.3)
                logger.info("   ✅ Калибровка завершена")
            except Exception as calib_e:
                logger.warning(f"   ⚠️ Ошибка калибровки (продолжаем): {calib_e}")
            
            logger.info("   ✅ ЗАПИСЬ АКТИВНА - ГОВОРИТЕ В МИКРОФОН")
            logger.info("=" * 80)
            logger.info("")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка начала записи: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_recording = False
            return False
    
    def _stop_recording(self) -> Optional[str]:
        """Остановка записи и распознавание"""
        if not self.is_recording:
            return None
        
        try:
            device_name = self.current_device_data['name'] if self.current_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info(f"🛑 ОСТАНОВКА ЗАПИСИ")
            logger.info(f"   📱 Устройство: {device_name}")
            logger.info("")
            start_time = time.time()
            
            # Записываем аудио
            logger.info("   🎙️ Запись аудио...")
            with self.current_microphone as source:
                audio = self.current_recognizer.listen(source, timeout=1.0, phrase_time_limit=5.0)
            
            duration_ms = int((time.time() - start_time) * 1000)
            logger.info(f"   ✅ Аудио записано (длительность: {duration_ms}ms)")
            
            # Распознавание через Google SR
            recognized_text = None
            logger.info("   🔍 Распознавание через Google SR...")
            try:
                recognized_text = self.current_recognizer.recognize_google(audio, language="ru-RU")
                logger.info(f"   ✅ РАСПОЗНАНО: {recognized_text}")
            except sr.UnknownValueError:
                logger.warning("   ⚠️ Google SR не смог распознать речь")
            except sr.RequestError as e:
                logger.error(f"   ❌ Ошибка Google SR: {e}")
            
            # Записываем событие
            event = RecordingEvent(
                timestamp=time.time(),
                device_name=device_name,
                device_index=self.current_device_data['device_index'] if self.current_device_data else -1,
                sample_rate=self.current_device_data['sample_rate'] if self.current_device_data else 0,
                duration_ms=duration_ms,
                recognized_text=recognized_text
            )
            self.recording_events.append(event)
            
            self.is_recording = False
            logger.info(f"   ✅ Запись остановлена")
            logger.info("=" * 80)
            logger.info("")
            
            return recognized_text
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки записи: {e}")
            self.is_recording = False
            return None
    
    def _on_key_press(self, key):
        """Обработка нажатия клавиши"""
        try:
            # Проверяем Control+N
            if hasattr(key, 'char') and key.char == 'n':
                # Проверяем, зажат ли Control
                if keyboard.Key.ctrl_l in self._pressed_keys or keyboard.Key.ctrl_r in self._pressed_keys:
                    if not self.key_pressed:
                        self.key_pressed = True
                        logger.info("⌨️ Control+N нажата - начало записи")
                        self._start_recording()
        except Exception as e:
            logger.error(f"❌ Ошибка обработки нажатия: {e}")
    
    def _on_key_release(self, key):
        """Обработка отпускания клавиши"""
        try:
            # Проверяем Control+N
            if hasattr(key, 'char') and key.char == 'n':
                if self.key_pressed:
                    self.key_pressed = False
                    logger.info("⌨️ Control+N отпущена - остановка записи")
                    self._stop_recording()
        except Exception as e:
            logger.error(f"❌ Ошибка обработки отпускания: {e}")
    
    def _monitor_devices(self):
        """Мониторинг изменений устройств"""
        logger.info("🔄 Мониторинг устройств запущен")
        logger.info("")
        
        while not self.stop_device_monitoring.is_set():
            try:
                current_device = self._get_current_device_data()
                
                if current_device:
                    # Логируем текущее устройство каждую проверку (для видимости)
                    if current_device['uid'] != self.last_device_uid:
                        logger.info("=" * 80)
                        logger.info(f"🔄 ОБНАРУЖЕНО ПЕРЕКЛЮЧЕНИЕ УСТРОЙСТВА!")
                        logger.info(f"   📱 Старое устройство: {self.last_device_uid}")
                        logger.info(f"   📱 Новое устройство: {current_device['uid']} ({current_device['name']})")
                        logger.info(f"   📊 PortAudio index: {current_device['device_index']}")
                        logger.info(f"   📊 Sample rate: {current_device['sample_rate']}Hz")
                        logger.info(f"   🎙️ Статус записи: {'АКТИВНА' if self.is_recording else 'неактивна'}")
                        logger.info("")
                        
                        # Переключаемся на новое устройство
                        logger.info("   🔄 Переключение на новое устройство...")
                        if self._switch_to_device(current_device):
                            self.current_device_data = current_device
                            self.last_device_uid = current_device['uid']
                            logger.info(f"   ✅ Успешно переключено на: {current_device['name']}")
                            
                            # Если запись активна, перекалибруем
                            if self.is_recording:
                                logger.info("   🔄 Запись активна - перекалибровка микрофона...")
                                try:
                                    with self.current_microphone as source:
                                        self.current_recognizer.adjust_for_ambient_noise(source, duration=0.3)
                                    logger.info("   ✅ Перекалибровка завершена")
                                except Exception as e:
                                    logger.warning(f"   ⚠️ Ошибка перекалибровки: {e}")
                        else:
                            logger.error(f"   ❌ Ошибка переключения на: {current_device['name']}")
                        
                        logger.info("=" * 80)
                        logger.info("")
                    else:
                        # Периодически логируем текущее устройство (каждые 5 секунд для видимости)
                        if int(time.time()) % 5 == 0:
                            logger.debug(f"📱 Текущее устройство: {current_device['name']} (UID: {current_device['uid']}, запись: {'активна' if self.is_recording else 'неактивна'})")
                
                time.sleep(1.0)  # Проверка каждую секунду
                
            except Exception as e:
                logger.error(f"❌ Ошибка мониторинга устройств: {e}")
                import traceback
                logger.error(traceback.format_exc())
                time.sleep(1.0)
    
    def start_keyboard_monitoring(self):
        """Запуск мониторинга клавиатуры"""
        if not PYNPUT_AVAILABLE:
            logger.warning("⚠️ pynput не доступен, используем симуляцию")
            return
        
        try:
            self._pressed_keys = set()
            
            def on_press(key):
                try:
                    # Логируем все нажатия для отладки
                    key_str = str(key)
                    if hasattr(key, 'char') and key.char:
                        key_str = f"'{key.char}'"
                    logger.debug(f"🔑 Нажата клавиша: {key_str}")
                    
                    self._pressed_keys.add(key)
                    
                    # Проверяем Control+N
                    n_pressed = hasattr(key, 'char') and key.char == 'n'
                    ctrl_pressed = keyboard.Key.ctrl_l in self._pressed_keys or keyboard.Key.ctrl_r in self._pressed_keys
                    
                    if n_pressed and ctrl_pressed:
                        if not self.key_pressed:
                            self.key_pressed = True
                            logger.info("⌨️ Control+N нажата - начало записи")
                            self._start_recording()
                    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                        # Если Control нажат, проверяем, не нажата ли уже N
                        if hasattr(keyboard.KeyCode, 'from_char'):
                            # Проверяем, есть ли 'n' в нажатых клавишах
                            for k in self._pressed_keys:
                                if hasattr(k, 'char') and k.char == 'n':
                                    if not self.key_pressed:
                                        self.key_pressed = True
                                        logger.info("⌨️ Control+N нажата (Control после N) - начало записи")
                                        self._start_recording()
                                    break
                except Exception as e:
                    logger.error(f"❌ Ошибка on_press: {e}")
                    import traceback
                    logger.error(traceback.format_exc())
            
            def on_release(key):
                try:
                    if key in self._pressed_keys:
                        self._pressed_keys.remove(key)
                    if hasattr(key, 'char') and key.char == 'n':
                        if self.key_pressed:
                            self.key_pressed = False
                            logger.info("⌨️ Control+N отпущена - остановка записи")
                            self._stop_recording()
                    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                        if self.key_pressed:
                            self.key_pressed = False
                            logger.info("⌨️ Control отпущен - остановка записи")
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
            self.key_listener = None
            logger.info("🛑 Мониторинг клавиатуры остановлен")
    
    def test_full_integration(self) -> bool:
        """Тест полной интеграции"""
        logger.info("=" * 80)
        logger.info("MVP-11: Full Integration - Push-to-Talk + Device Switching + Google SR")
        logger.info("=" * 80)
        logger.info("")
        
        logger.info("📋 Инструкция:")
        logger.info("   1. Нажмите и удерживайте Control+N для начала записи")
        logger.info("   2. Говорите в микрофон")
        logger.info("   3. Отпустите Control+N для остановки записи и распознавания")
        logger.info("   4. Переключайте устройства (отключите/подключите наушники)")
        logger.info("   5. Повторите несколько раз")
        logger.info("")
        
        # Запускаем мониторинг клавиатуры
        self.start_keyboard_monitoring()
        
        # Запускаем мониторинг устройств
        self.device_monitoring_thread = threading.Thread(target=self._monitor_devices, daemon=True)
        self.device_monitoring_thread.start()
        
        logger.info("⏳ Ожидание действий пользователя (60 секунд)...")
        logger.info("")
        
        # Ждем 60 секунд
        time.sleep(60)
        
        # Останавливаем мониторинг
        self.stop_device_monitoring.set()
        self.stop_keyboard_monitoring()
        
        # Если запись активна, останавливаем
        if self.is_recording:
            self._stop_recording()
        
        # Выводим результаты
        logger.info("")
        logger.info("=" * 80)
        logger.info("РЕЗУЛЬТАТЫ")
        logger.info("=" * 80)
        logger.info("")
        
        logger.info(f"📊 Всего записей: {len(self.recording_events)}")
        successful = sum(1 for e in self.recording_events if e.recognized_text)
        logger.info(f"✅ Успешных распознаваний: {successful}")
        logger.info(f"❌ Неудачных распознаваний: {len(self.recording_events) - successful}")
        logger.info("")
        
        for i, event in enumerate(self.recording_events, 1):
            logger.info(f"📝 Запись #{i}:")
            logger.info(f"   Устройство: {event.device_name} (index: {event.device_index})")
            logger.info(f"   Sample rate: {event.sample_rate}Hz")
            logger.info(f"   Длительность: {event.duration_ms}ms")
            if event.recognized_text:
                logger.info(f"   ✅ Распознано: {event.recognized_text}")
            else:
                logger.info(f"   ❌ Не распознано")
            logger.info("")
        
        return len(self.recording_events) > 0


def main():
    """Главная функция"""
    prototype = FullIntegrationPrototype()
    
    if not prototype.setup():
        logger.error("❌ Не удалось инициализировать прототип")
        return False
    
    success = prototype.test_full_integration()
    
    if success:
        logger.info("✅ MVP-11: Full Integration - УСПЕШНО")
    else:
        logger.error("❌ MVP-11: Full Integration - ПРОВАЛ")
    
    return success


if __name__ == "__main__":
    main()

