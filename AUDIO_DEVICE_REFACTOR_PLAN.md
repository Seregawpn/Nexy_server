# План рефакторинга управления аудиоустройствами

## 🎯 Цель
Создать единую систему управления аудиоустройствами с поддержкой INPUT/OUTPUT, устранить конфликты и дублирование кода.

## 🚨 Текущие проблемы
1. **Конфликты управления**: AudioDeviceIntegration vs SpeechRecognizer vs SpeechPlayback
2. **Дублирование функций**: get_available_devices(), get_best_audio_device() в разных модулях
3. **Дублирование типов**: AudioDevice определен в двух местах (audio_device_manager и speech_playback)
4. **Нестабильные ID**: hash(name) меняется при каждом запуске
5. **Отсутствие INPUT поддержки**: SwitchAudioBridge работает только с OUTPUT
6. **Множественные источники truth**: switchaudio, sounddevice, собственные приоритеты
7. **Отсутствие dependency injection**: SpeechRecognizer и SpeechPlayback не имеют доступа к AudioDeviceManager

## 📋 Этапы реализации

### **Этап 1: Очистка дублирующих функций** ⏱️ 30 минут
**Цель**: Удалить дублирующие функции из SpeechPlayback

#### 1.1 Удаление из `modules/speech_playback/utils/device_utils.py`
```python
# УДАЛИТЬ функции:
- get_available_devices()
- get_best_audio_device() 
- test_audio_device()
- get_device_info()

# УДАЛИТЬ дублирующий тип:
- class AudioDevice (использовать из audio_device_manager)

# ОСТАВИТЬ только:
- normalize_audio()
- resample_audio() 
- convert_channels()
- detect_silence()
- trim_silence()
- get_audio_info()
```

#### 1.2 Обновление `modules/speech_playback/core/player.py`
```python
# БЫЛО:
from ..utils.device_utils import get_best_audio_device, AudioDevice
device = get_best_audio_device()

# СТАЛО:
from modules.audio_device_manager.core.types import AudioDevice, DeviceType

async def _select_audio_device(self):
    """Получение аудио устройства через EventBus"""
    try:
        # Получаем AudioDeviceManager через EventBus
        audio_manager = await self._get_audio_manager_via_eventbus()
        if audio_manager:
            best_output = await audio_manager.get_best_device(DeviceType.OUTPUT)
            if best_output:
                # Конвертируем в portaudio index
                return self._convert_to_portaudio_index(best_output)
        return None
    except Exception as e:
        logger.error(f"❌ Ошибка выбора аудио устройства: {e}")
        return None

async def _get_audio_manager_via_eventbus(self):
    """Получение AudioDeviceManager через EventBus"""
    # Это будет реализовано в Этапе 7
    pass

def _convert_to_portaudio_index(self, device: AudioDevice) -> Optional[int]:
    """Конвертация AudioDevice в portaudio index"""
    try:
        devices = sd.query_devices()
        for i, dev in enumerate(devices):
            if dev['name'] == device.name:
                return i
        return None
    except Exception as e:
        logger.error(f"❌ Ошибка конвертации в portaudio index: {e}")
        return None
```

#### 1.3 Обновление `modules/speech_playback/__init__.py`
```python
# УДАЛИТЬ:
'get_best_audio_device',

# ОБНОВИТЬ __all__ список
```

**Тест 1.1**: Проверить отсутствие дублирующих функций
```bash
# Должно быть пусто
grep -r "get_available_devices\|get_best_audio_device" modules/speech_playback/
```

**Тест 1.2**: Проверить что приложение запускается без ошибок
```bash
python client/main.py
# Проверить что нет ImportError или AttributeError
```

**Тест 1.3**: Проверить что SpeechPlayback работает (базовая функциональность)
```bash
# В логах должно быть:
# ✅ SpeechPlaybackIntegration инициализирован
# ✅ SpeechPlaybackIntegration запущен
```

**Тест 1.4**: Проверить что дублирующий тип AudioDevice удален
```bash
# Должно быть пусто
grep -r "class AudioDevice" modules/speech_playback/
```

---

### **Этап 2: Расширение AudioDeviceManager для INPUT/OUTPUT** ⏱️ 1 час
**Цель**: Добавить поддержку управления INPUT/OUTPUT функциями устройств

**ВАЖНО**: Одно устройство (например, AirPods) поддерживает И INPUT И OUTPUT функции одновременно.
- `DeviceType.BOTH` - устройство с функциями микрофона И динамиков
- `input_devices` - устройства, которые могут работать как микрофоны
- `output_devices` - устройства, которые могут работать как динамики
- Одно устройство может быть в обеих категориях одновременно

#### 2.1 Обновление `modules/audio_device_manager/core/types.py`
```python
@dataclass
class AudioDeviceManagerConfig:
    # ... существующие поля ...
    
    # Новые настройки
    separate_input_output_management: bool = True
    input_device_priorities: Dict[str, int] = None
    output_device_priorities: Dict[str, int] = None
    
    def __post_init__(self):
        if self.input_device_priorities is None:
            self.input_device_priorities = {
                'builtin_microphone': 1,
                'usb_microphone': 2,
                'bluetooth_microphone': 3,
                'external_microphone': 4,
                'virtual_microphone': 5
            }
        
        if self.output_device_priorities is None:
            self.output_device_priorities = {
                'airpods': 1,
                'bluetooth_headphones': 2,
                'usb_headphones': 3,
                'external_speakers': 4,
                'builtin_speakers': 5
            }
```

#### 2.2 Обновление `modules/audio_device_manager/core/device_manager.py`
```python
class AudioDeviceManager:
    def __init__(self, config: Optional[AudioDeviceManagerConfig] = None):
        # ... существующий код ...
        
        # Добавляем отдельное управление INPUT/OUTPUT
        self.current_input_device: Optional[AudioDevice] = None
        self.current_output_device: Optional[AudioDevice] = None
        self.input_devices: Dict[str, AudioDevice] = {}
        self.output_devices: Dict[str, AudioDevice] = {}
    
    async def get_best_input_device(self) -> Optional[AudioDevice]:
        """Получение лучшего входного устройства"""
        devices = await self.get_available_devices(DeviceType.INPUT)
        if not devices:
            return None
        sorted_devices = sorted(devices, key=lambda x: self._get_input_priority(x))
        return sorted_devices[0] if sorted_devices else None
    
    async def get_best_output_device(self) -> Optional[AudioDevice]:
        """Получение лучшего выходного устройства"""
        devices = await self.get_available_devices(DeviceType.OUTPUT)
        if not devices:
            return None
        sorted_devices = sorted(devices, key=lambda x: self._get_output_priority(x))
        return sorted_devices[0] if sorted_devices else None
    
    async def switch_to_input_device(self, device: AudioDevice) -> bool:
        """Переключение на входное устройство"""
        if device.type != DeviceType.INPUT:
            return False
        success = await self.device_switcher._switch_to_input_device(device)
        if success:
            self.current_input_device = device
        return success
    
    async def switch_to_output_device(self, device: AudioDevice) -> bool:
        """Переключение на выходное устройство"""
        if device.type != DeviceType.OUTPUT:
            return False
        success = await self.device_switcher._switch_to_output_device(device)
        if success:
            self.current_output_device = device
        return success
    
    def _get_input_priority(self, device: AudioDevice) -> int:
        """Получение приоритета input устройства"""
        device_name_lower = device.name.lower()
        for keyword, priority in self.config.input_device_priorities.items():
            if keyword in device_name_lower:
                return priority
        return 10
    
    def _get_output_priority(self, device: AudioDevice) -> int:
        """Получение приоритета output устройства"""
        device_name_lower = device.name.lower()
        for keyword, priority in self.config.output_device_priorities.items():
            if keyword in device_name_lower:
                return priority
        return 10
```

**Тест 2.1**: Проверить что новые методы существуют
```python
# Тест в Python REPL
from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import DeviceType

manager = AudioDeviceManager()
# Проверить что методы существуют
assert hasattr(manager, 'get_best_input_device')
assert hasattr(manager, 'get_best_output_device')
assert hasattr(manager, 'switch_to_input_device')
assert hasattr(manager, 'switch_to_output_device')
print("✅ Все новые методы существуют")
```

**Тест 2.2**: Проверить что конфигурация загружается корректно
```python
# Тест конфигурации
config = manager.config
assert hasattr(config, 'input_device_priorities')
assert hasattr(config, 'output_device_priorities')
assert hasattr(config, 'separate_input_output_management')
print("✅ Конфигурация INPUT/OUTPUT загружена")
```

**Тест 2.3**: Проверить что приложение запускается с новыми методами
```bash
python client/main.py
# В логах должно быть:
# ✅ AudioDeviceManager запущен
# ✅ Компоненты AudioDeviceManager настроены
```

**Тест 2.4**: Проверить что новые поля состояния инициализированы
```python
# Тест состояния
assert hasattr(manager, 'current_input_device')
assert hasattr(manager, 'current_output_device')
assert hasattr(manager, 'input_devices')
assert hasattr(manager, 'output_devices')
print("✅ Новые поля состояния инициализированы")

# Тест правильной архитектуры: одно устройство в обеих категориях
from modules.audio_device_manager.core.types import DeviceType, AudioDevice

airpods = AudioDevice(id='test', name='AirPods', type=DeviceType.BOTH)
asyncio.run(manager._categorize_devices([airpods]))

assert 'test' in manager.input_devices, "AirPods должны быть в input_devices"
assert 'test' in manager.output_devices, "AirPods должны быть в output_devices"
print("✅ Одно устройство правильно попадает в обе категории")
```

---

### **Этап 3: Расширение SwitchAudioBridge для INPUT/OUTPUT** ⏱️ 1 час
**Цель**: Научить SwitchAudioBridge работать с input устройствами

#### 3.1 Обновление `modules/audio_device_manager/macos/switchaudio_bridge.py`
```python
async def _get_devices_from_switchaudio(self, device_type: Optional[str] = None) -> List[AudioDevice]:
    """Получение устройств через switchaudio с поддержкой типов"""
    try:
        switchaudio_cmd = self._get_switchaudio_path()
        
        if device_type:
            result = subprocess.run([
                switchaudio_cmd, '-a', '-t', device_type
            ], capture_output=True, text=True, timeout=10)
        else:
            result = subprocess.run([
                switchaudio_cmd, '-a'
            ], capture_output=True, text=True, timeout=10)
        
        if result.returncode != 0:
            return []
        
        devices = []
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if line.strip():
                device = await self._parse_switchaudio_line(line, device_type)
                if device:
                    devices.append(device)
        return devices
        
    except Exception as e:
        logger.error(f"❌ Ошибка получения устройств: {e}")
        return []

async def _parse_switchaudio_line(self, line: str, device_type: Optional[str] = None) -> Optional[AudioDevice]:
    """Парсинг строки с учетом типа и стабильным ID"""
    try:
        # ... парсинг имени ...
        
        # ИСПРАВЛЕНИЕ: Стабильный ID вместо hash(name)
        device_id = f"device_{name.replace(' ', '_').replace('(', '').replace(')', '').lower()}"
        
        # Определяем тип устройства
        if device_type:
            if device_type == 'input':
                device_type_enum = DeviceType.INPUT
            elif device_type == 'output':
                device_type_enum = DeviceType.OUTPUT
            else:
                device_type_enum = await self._detect_device_type(name, device_type_str)
        else:
            device_type_enum = await self._detect_device_type(name, device_type_str)
        
        # ... создание AudioDevice ...
        
    except Exception as e:
        logger.error(f"❌ Ошибка парсинга: {e}")
        return None

async def set_default_input_device(self, device_id: str) -> bool:
    """Установка устройства ввода по умолчанию"""
    try:
        devices = await self.get_available_devices()
        target_device = next((d for d in devices if d.id == device_id), None)
        
        if not target_device or target_device.type != DeviceType.INPUT:
            return False
        
        switchaudio_cmd = self._get_switchaudio_path()
        result = subprocess.run([
            switchaudio_cmd, '-t', 'input', '-s', target_device.name
        ], capture_output=True, text=True, timeout=10)
        
        return result.returncode == 0
        
    except Exception as e:
        logger.error(f"❌ Ошибка установки input устройства: {e}")
        return False
```

#### 3.2 Обновление DeviceMonitor
```python
# В modules/audio_device_manager/core/device_monitor.py
async def set_default_input_device(self, device_id: str) -> bool:
    """Установка input устройства по умолчанию"""
    try:
        return await self._core_audio_bridge.set_default_input_device(device_id)
    except Exception as e:
        logger.error(f"❌ Ошибка установки input устройства: {e}")
        return False
```

**Тест 3.1**: Проверить что switchaudio поддерживает типы устройств
```bash
# Проверить что команды работают
switchaudio -a -t input
switchaudio -a -t output
# Должны возвращать разные списки устройств
```

**Тест 3.2**: Проверить что стабильные ID работают
```python
# Тест стабильности ID
from modules.audio_device_manager.macos.switchaudio_bridge import SwitchAudioBridge
import asyncio

async def test_stable_ids():
    bridge = SwitchAudioBridge()
    devices1 = await bridge.get_available_devices()
    devices2 = await bridge.get_available_devices()
    
    # ID должны быть одинаковыми
    ids1 = [d.id for d in devices1]
    ids2 = [d.id for d in devices2]
    assert ids1 == ids2, "ID устройств должны быть стабильными"
    print("✅ ID устройств стабильны")

asyncio.run(test_stable_ids())
```

**Тест 3.3**: Проверить что новые методы SwitchAudioBridge работают
```python
# Тест новых методов
bridge = SwitchAudioBridge()
assert hasattr(bridge, 'set_default_input_device')
print("✅ Новые методы SwitchAudioBridge существуют")
```

**Тест 3.4**: Проверить что DeviceMonitor поддерживает input устройства
```python
# Тест DeviceMonitor
from modules.audio_device_manager.core.device_monitor import DeviceMonitor

monitor = DeviceMonitor()
assert hasattr(monitor, 'set_default_input_device')
print("✅ DeviceMonitor поддерживает input устройства")
```

**Тест 3.5**: Проверить что приложение запускается с расширенным SwitchAudioBridge
```bash
python client/main.py
# В логах должно быть:
# ✅ SwitchAudio мониторинг запущен
# ✅ Найдено X устройств (input + output)
```

---

### **Этап 4: Обновление DeviceSwitcher** ⏱️ 30 минут
**Цель**: Добавить методы для переключения input/output устройств

#### 4.1 Обновление `modules/audio_device_manager/core/device_switcher.py`
```python
class DeviceSwitcher:
    def __init__(self, device_monitor: DeviceMonitor):
        # ... существующий код ...
        self.current_input_device: Optional[AudioDevice] = None
        self.current_output_device: Optional[AudioDevice] = None

async def _switch_to_input_device(self, device: AudioDevice):
    """Переключение на входное устройство"""
    try:
        logger.info(f"🔄 Переключение на input: {device.name}")
        success = await self.device_monitor.set_default_input_device(device.id)
        if success:
            self.current_input_device = device
            logger.info(f"✅ Переключено на input: {device.name}")
        else:
            logger.error(f"❌ Не удалось переключиться на input: {device.name}")
    except Exception as e:
        logger.error(f"❌ Ошибка переключения input: {e}")

async def _switch_to_output_device(self, device: AudioDevice):
    """Переключение на выходное устройство"""
    try:
        logger.info(f"🔄 Переключение на output: {device.name}")
        success = await self.device_monitor.set_default_output_device(device.id)
        if success:
            self.current_output_device = device
            logger.info(f"✅ Переключено на output: {device.name}")
        else:
            logger.error(f"❌ Не удалось переключиться на output: {device.name}")
    except Exception as e:
        logger.error(f"❌ Ошибка переключения output: {e}")

def _find_best_input_device(self, devices: List[AudioDevice]) -> Optional[AudioDevice]:
    """Поиск лучшего input устройства"""
    input_devices = [
        d for d in devices 
        if d.status.value == "available" and d.type == DeviceType.INPUT
    ]
    if not input_devices:
        return None
    return min(input_devices, key=lambda x: x.priority.value)

def _find_best_output_device(self, devices: List[AudioDevice]) -> Optional[AudioDevice]:
    """Поиск лучшего output устройства"""
    output_devices = [
        d for d in devices 
        if d.status.value == "available" and d.type == DeviceType.OUTPUT
    ]
    if not output_devices:
        return None
    return min(output_devices, key=lambda x: x.priority.value)
```

**Тест 4.1**: Проверить что новые методы DeviceSwitcher существуют
```python
# Тест DeviceSwitcher
from modules.audio_device_manager.core.device_switcher import DeviceSwitcher
from modules.audio_device_manager.core.device_monitor import DeviceMonitor

monitor = DeviceMonitor()
switcher = DeviceSwitcher(monitor)

assert hasattr(switcher, '_switch_to_input_device')
assert hasattr(switcher, '_switch_to_output_device')
assert hasattr(switcher, '_find_best_input_device')
assert hasattr(switcher, '_find_best_output_device')
print("✅ Все новые методы DeviceSwitcher существуют")
```

**Тест 4.2**: Проверить что новые поля состояния инициализированы
```python
# Тест состояния DeviceSwitcher
assert hasattr(switcher, 'current_input_device')
assert hasattr(switcher, 'current_output_device')
print("✅ Новые поля состояния DeviceSwitcher инициализированы")
```

**Тест 4.3**: Проверить что приложение запускается с обновленным DeviceSwitcher
```bash
python client/main.py
# В логах должно быть:
# ✅ AudioDeviceManager запущен
# ✅ Компоненты AudioDeviceManager настроены
```

**Тест 4.4**: Проверить что методы переключения не вызывают ошибок
```python
# Тест методов (без реального переключения)
from modules.audio_device_manager.core.types import AudioDevice, DeviceType

# Создаем тестовое устройство
test_device = AudioDevice(
    id="test_device",
    name="Test Device",
    type=DeviceType.INPUT
)

# Проверяем что методы не падают
try:
    # Не вызываем реально, только проверяем что методы существуют
    assert callable(switcher._switch_to_input_device)
    assert callable(switcher._switch_to_output_device)
    print("✅ Методы переключения доступны")
except Exception as e:
    print(f"❌ Ошибка в методах переключения: {e}")
```

---

### **Этап 5: Очистка AudioDeviceIntegration** ⏱️ 30 минут
**Цель**: Убрать прямое управление sounddevice, использовать AudioDeviceManager

#### 5.1 Удаление методов из `integration/integrations/audio_device_integration.py`
```python
# УДАЛИТЬ методы:
- _get_sounddevice_defaults()
- _apply_sounddevice_input_default()
- _ensure_input_device_selected()
- _select_input_device_index()
- _probe_input_device()
- _reinitialize_portaudio()
```

#### 5.2 Замена _enable_microphone()
```python
async def _enable_microphone(self):
    """Включение микрофона через AudioDeviceManager"""
    try:
        if not self._manager:
            return
        
        logger.info("Enabling microphone...")
        
        # Получаем лучшее input устройство
        best_input = await self._manager.get_best_input_device()
        if not best_input:
            logger.warning("⚠️ Нет доступных input устройств")
            await self.event_bus.publish("audio.microphone_error", {
                "error": "no_input_devices",
                "context": "enable_microphone"
            })
            return
        
        # Переключаемся на лучшее input устройство
        success = await self._manager.switch_to_input_device(best_input)
        if success:
            logger.info(f"✅ Microphone enabled: {best_input.name}")
            await self.event_bus.publish("audio.microphone_enabled", {
                "device": best_input.name,
                "device_type": "input",
                "is_available": True,
                "mode": "physical_switch"
            })
        else:
            logger.error("❌ Failed to enable microphone")
            await self.event_bus.publish("audio.microphone_error", {
                "error": "switch_failed",
                "context": "enable_microphone"
            })
            
    except Exception as e:
        logger.error(f"Error enabling microphone: {e}")
        await self.event_bus.publish("audio.microphone_error", {
            "error": str(e),
            "context": "enable_microphone"
        })
```

**Тест 5.1**: Проверить что дублирующие методы удалены
```bash
# Должно быть пусто
grep -r "_get_sounddevice_defaults\|_apply_sounddevice_input_default\|_ensure_input_device_selected" integration/integrations/audio_device_integration.py
```

**Тест 5.2**: Проверить что приложение запускается без удаленных методов
```bash
python client/main.py
# Проверить что нет AttributeError или NameError
```

**Тест 5.3**: Проверить что _enable_microphone использует AudioDeviceManager
```python
# Проверить что метод _enable_microphone обновлен
grep -A 10 "_enable_microphone" integration/integrations/audio_device_integration.py
# Должно содержать:
# - await self._manager.get_best_input_device()
# - await self._manager.switch_to_input_device()
```

**Тест 5.4**: Проверить что AudioDeviceIntegration работает с AudioDeviceManager
```bash
python client/main.py
# В логах должно быть:
# ✅ AudioDeviceIntegration инициализирован
# ✅ AudioDeviceManager запущен
# ✅ Microphone enabled: [device_name]
```

**Тест 5.5**: Проверить что события микрофона публикуются корректно
```bash
# В логах должно быть:
# audio.microphone_enabled
# audio.microphone_disabled
# audio.microphone_error (при ошибках)
```

---

### **Этап 6: Обновление SpeechRecognizer** ⏱️ 30 минут
**Цель**: Убрать собственную логику выбора микрофона, использовать AudioDeviceManager

#### 6.1 Обновление `modules/voice_recognition/core/speech_recognizer.py`
```python
# ЗАМЕНИТЬ _pick_input_device():
async def _pick_input_device(self) -> Optional[int]:
    """Подбирает стабильное входное устройство через AudioDeviceManager"""
    try:
        audio_manager = self._get_audio_manager()
        if audio_manager:
            best_input = await audio_manager.get_best_input_device()
            if best_input:
                # Конвертируем в portaudio index
                devices = sd.query_devices()
                for i, device in enumerate(devices):
                    if device['name'] == best_input.name:
                        logger.info(f"🎚️ Выбрано input: {best_input.name} (index={i})")
                        return i
        
        # Fallback к системному default
        logger.info("🎚️ Используем системный default input")
        return None
        
    except Exception as e:
        logger.error(f"❌ Ошибка выбора input устройства: {e}")
        return None

def _get_audio_manager(self):
    """Получение AudioDeviceManager из интеграции"""
    try:
        return getattr(self, '_audio_manager', None)
    except Exception as e:
        logger.error(f"❌ Ошибка получения AudioDeviceManager: {e}")
        return None
```

#### 6.2 Добавление dependency injection
```python
# В __init__ или через event_bus
def set_audio_manager(self, audio_manager):
    """Установка AudioDeviceManager"""
    self._audio_manager = audio_manager
```

**Тест 6.1**: Проверить что _pick_input_device обновлен
```python
# Проверить что метод использует AudioDeviceManager
grep -A 15 "_pick_input_device" modules/voice_recognition/core/speech_recognizer.py
# Должно содержать:
# - audio_manager = self._get_audio_manager()
# - best_input = await audio_manager.get_best_input_device()
```

**Тест 6.2**: Проверить что _get_audio_manager существует
```python
# Проверить что метод dependency injection существует
grep -A 5 "_get_audio_manager" modules/voice_recognition/core/speech_recognizer.py
# Должен содержать логику получения AudioDeviceManager
```

**Тест 6.3**: Проверить что приложение запускается с обновленным SpeechRecognizer
```bash
python client/main.py
# В логах должно быть:
# ✅ VoiceRecognitionIntegration инициализирован
# ✅ SpeechRecognizer инициализирован
```

**Тест 6.4**: Проверить что SpeechRecognizer работает (базовая функциональность)
```bash
# В логах должно быть:
# 🎚️ Выбрано input устройство: [device_name]
# 🎛️ Audio stream запущен
```

**Тест 6.5**: Проверить что старый код _pick_input_device удален
```bash
# Должно быть пусто или содержать только новый код
grep -r "builtin_keywords\|candidates.*sort" modules/voice_recognition/core/speech_recognizer.py
```

---

### **Этап 7: Добавление dependency injection** ⏱️ 45 минут
**Цель**: Обеспечить доступ SpeechRecognizer и SpeechPlayback к AudioDeviceManager

#### 7.1 Обновление SimpleModuleCoordinator
```python
# В integration/core/simple_module_coordinator.py
async def _setup_coordination(self):
    """Настройка координации между модулями"""
    try:
        # ... существующий код ...
        
        # Добавляем dependency injection для AudioDeviceManager
        await self._setup_audio_dependencies()
        
    except Exception as e:
        logger.error(f"❌ Ошибка настройки координации: {e}")

async def _setup_audio_dependencies(self):
    """Настройка зависимостей для аудио модулей"""
    try:
        # Получаем AudioDeviceManager из интеграции
        audio_integration = self.integrations.get('audio')
        if not audio_integration or not hasattr(audio_integration, '_manager'):
            logger.warning("⚠️ AudioDeviceManager недоступен для dependency injection")
            return
        
        audio_manager = audio_integration._manager
        
        # Инжектим в SpeechPlayback
        speech_playback = self.integrations.get('speech_playback')
        if speech_playback and hasattr(speech_playback, 'set_audio_manager'):
            speech_playback.set_audio_manager(audio_manager)
            logger.info("✅ AudioDeviceManager инжектирован в SpeechPlayback")
        
        # Инжектим в VoiceRecognition
        voice_recognition = self.integrations.get('voice_recognition')
        if voice_recognition and hasattr(voice_recognition, 'set_audio_manager'):
            voice_recognition.set_audio_manager(audio_manager)
            logger.info("✅ AudioDeviceManager инжектирован в VoiceRecognition")
            
    except Exception as e:
        logger.error(f"❌ Ошибка настройки аудио зависимостей: {e}")
```

#### 7.2 Обновление SpeechPlaybackIntegration
```python
# В integration/integrations/speech_playback_integration.py
class SpeechPlaybackIntegration:
    def __init__(self, ...):
        # ... существующий код ...
        self._audio_manager = None
    
    def set_audio_manager(self, audio_manager):
        """Установка AudioDeviceManager через dependency injection"""
        self._audio_manager = audio_manager
        logger.info("✅ AudioDeviceManager установлен в SpeechPlaybackIntegration")
    
    async def _get_audio_manager(self):
        """Получение AudioDeviceManager"""
        return self._audio_manager
```

#### 7.3 Обновление VoiceRecognitionIntegration
```python
# В integration/integrations/voice_recognition_integration.py
class VoiceRecognitionIntegration:
    def __init__(self, ...):
        # ... существующий код ...
        self._audio_manager = None
    
    def set_audio_manager(self, audio_manager):
        """Установка AudioDeviceManager через dependency injection"""
        self._audio_manager = audio_manager
        logger.info("✅ AudioDeviceManager установлен в VoiceRecognitionIntegration")
    
    async def _get_audio_manager(self):
        """Получение AudioDeviceManager"""
        return self._audio_manager
```

**Тест 7.1**: Проверить что SimpleModuleCoordinator имеет метод _setup_audio_dependencies
```python
# Проверить что метод существует
grep -A 10 "_setup_audio_dependencies" integration/core/simple_module_coordinator.py
# Должен содержать логику dependency injection
```

**Тест 7.2**: Проверить что SpeechPlaybackIntegration имеет set_audio_manager
```python
# Проверить что метод существует
grep -A 5 "set_audio_manager" integration/integrations/speech_playback_integration.py
# Должен устанавливать self._audio_manager
```

**Тест 7.3**: Проверить что VoiceRecognitionIntegration имеет set_audio_manager
```python
# Проверить что метод существует
grep -A 5 "set_audio_manager" integration/integrations/voice_recognition_integration.py
# Должен устанавливать self._audio_manager
```

**Тест 7.4**: Проверить что dependency injection работает при запуске
```bash
python client/main.py
# В логах должно быть:
# ✅ AudioDeviceManager инжектирован в SpeechPlayback
# ✅ AudioDeviceManager инжектирован в VoiceRecognition
```

**Тест 7.5**: Проверить что модули получают доступ к AudioDeviceManager
```python
# Тест в Python REPL после запуска приложения
# (Этот тест нужно выполнить после запуска приложения)

# Проверить что SpeechPlaybackIntegration имеет AudioDeviceManager
# Проверить что VoiceRecognitionIntegration имеет AudioDeviceManager
print("✅ Dependency injection работает")
```

**Тест 7.6**: Проверить что приложение запускается без ошибок dependency injection
```bash
python client/main.py
# Проверить что нет ошибок:
# - AttributeError: 'SpeechPlaybackIntegration' object has no attribute 'set_audio_manager'
# - AttributeError: 'VoiceRecognitionIntegration' object has no attribute 'set_audio_manager'
```

---

### **Этап 8: Создание единого интерфейса** ⏱️ 30 минут
**Цель**: Создать единый интерфейс для всех модулей

#### 7.1 Создание `modules/audio_device_manager/core/unified_interface.py`
```python
"""
Единый интерфейс для управления аудиоустройствами
"""

from typing import Optional, List
from .device_manager import AudioDeviceManager
from .types import AudioDevice, DeviceType

class UnifiedAudioDeviceInterface:
    """Единый интерфейс для всех модулей"""
    
    def __init__(self, audio_manager: AudioDeviceManager):
        self.audio_manager = audio_manager
    
    async def get_best_input_device(self) -> Optional[AudioDevice]:
        """Для SpeechRecognizer"""
        return await self.audio_manager.get_best_input_device()
    
    async def get_best_output_device(self) -> Optional[AudioDevice]:
        """Для SpeechPlayback"""
        return await self.audio_manager.get_best_output_device()
    
    async def switch_to_input_device(self, device: AudioDevice) -> bool:
        """Для AudioDeviceIntegration"""
        return await self.audio_manager.switch_to_input_device(device)
    
    async def switch_to_output_device(self, device: AudioDevice) -> bool:
        """Для AudioDeviceIntegration"""
        return await self.audio_manager.switch_to_output_device(device)
    
    async def get_available_input_devices(self) -> List[AudioDevice]:
        """Получение всех input устройств"""
        return await self.audio_manager.get_available_devices(DeviceType.INPUT)
    
    async def get_available_output_devices(self) -> List[AudioDevice]:
        """Получение всех output устройств"""
        return await self.audio_manager.get_available_devices(DeviceType.OUTPUT)
    
    def get_current_input_device(self) -> Optional[AudioDevice]:
        """Текущее input устройство"""
        return self.audio_manager.current_input_device
    
    def get_current_output_device(self) -> Optional[AudioDevice]:
        """Текущее output устройство"""
        return self.audio_manager.current_output_device
```

**Тест 8.1**: Проверить что файл unified_interface.py создан
```bash
# Проверить что файл существует
ls -la modules/audio_device_manager/core/unified_interface.py
```

**Тест 8.2**: Проверить что UnifiedAudioDeviceInterface работает
```python
# Тест интерфейса
from modules.audio_device_manager.core.unified_interface import UnifiedAudioDeviceInterface
from modules.audio_device_manager.core.device_manager import AudioDeviceManager

manager = AudioDeviceManager()
interface = UnifiedAudioDeviceInterface(manager)

# Проверить что все методы существуют
assert hasattr(interface, 'get_best_input_device')
assert hasattr(interface, 'get_best_output_device')
assert hasattr(interface, 'switch_to_input_device')
assert hasattr(interface, 'switch_to_output_device')
assert hasattr(interface, 'get_available_input_devices')
assert hasattr(interface, 'get_available_output_devices')
assert hasattr(interface, 'get_current_input_device')
assert hasattr(interface, 'get_current_output_device')
print("✅ UnifiedAudioDeviceInterface работает")
```

**Тест 8.3**: Проверить что интерфейс экспортируется из модуля
```python
# Проверить что интерфейс доступен для импорта
from modules.audio_device_manager import UnifiedAudioDeviceInterface
print("✅ UnifiedAudioDeviceInterface экспортируется")
```

**Тест 8.4**: Проверить что приложение запускается с единым интерфейсом
```bash
python client/main.py
# В логах должно быть:
# ✅ AudioDeviceManager запущен
# ✅ Все интеграции работают
```

**Тест 8.5**: Проверить что интерфейс можно использовать в других модулях
```python
# Тест использования интерфейса
from modules.audio_device_manager.core.unified_interface import UnifiedAudioDeviceInterface
from modules.audio_device_manager.core.device_manager import AudioDeviceManager

# Создаем интерфейс
manager = AudioDeviceManager()
interface = UnifiedAudioDeviceInterface(manager)

# Проверяем что методы вызываются без ошибок
try:
    # Не вызываем реально, только проверяем что методы доступны
    assert callable(interface.get_best_input_device)
    assert callable(interface.get_best_output_device)
    print("✅ Интерфейс готов к использованию")
except Exception as e:
    print(f"❌ Ошибка в интерфейсе: {e}")
```

---

### **Этап 9: Дополнительные дублирования** ⏱️ 30 минут
**Цель**: Устранить оставшиеся дублирования в voice_recognition

#### 9.1 Очистка `modules/voice_recognition/utils/audio_utils.py`
```python
# УДАЛИТЬ функции (дублируют функциональность AudioDeviceManager):
- list_audio_devices()
- find_best_microphone()

# ОСТАВИТЬ только аудио обработку:
- normalize_audio()
- resample_audio()
- convert_channels()
- detect_silence()
- trim_silence()
- get_audio_info()
```

#### 9.2 Обновление импортов в SpeechRecognizer
```python
# В modules/voice_recognition/core/speech_recognizer.py
# БЫЛО:
from ..utils.audio_utils import find_best_microphone

# СТАЛО:
# Убрать импорт, использовать AudioDeviceManager через dependency injection
```

**Тест 9.1**: Проверить что дублирующие функции удалены из voice_recognition
```bash
# Должно быть пусто
grep -r "list_audio_devices\|find_best_microphone" modules/voice_recognition/utils/audio_utils.py
```

**Тест 9.2**: Проверить что импорты обновлены в SpeechRecognizer
```bash
# Должно быть пусто
grep -r "from ..utils.audio_utils import find_best_microphone" modules/voice_recognition/core/speech_recognizer.py
```

**Тест 9.3**: Проверить что приложение запускается без удаленных функций
```bash
python client/main.py
# Проверить что нет ImportError или AttributeError
```

**Тест 9.4**: Проверить что SpeechRecognizer работает без дублирующих функций
```bash
# В логах должно быть:
# ✅ VoiceRecognitionIntegration инициализирован
# ✅ SpeechRecognizer инициализирован
# 🎚️ Выбрано input устройство: [device_name]
```

**Тест 9.5**: Проверить что все дублирования устранены
```bash
# Проверить что нет дублирующих функций управления устройствами
grep -r "get_available_devices\|get_best_audio_device\|list_audio_devices\|find_best_microphone" modules/
# Должно показывать только AudioDeviceManager
```

**Тест 9.6**: Финальная проверка архитектуры
```bash
# Проверить что все модули используют единый источник truth
grep -r "AudioDeviceManager\|switchaudio" modules/ | grep -v audio_device_manager
# Должно быть минимальное количество ссылок
```

---

## 🔍 **ДОПОЛНИТЕЛЬНЫЕ ДУБЛИРОВАНИЯ (ОБНАРУЖЕНЫ)**

### **1. Дублирование типов AudioDevice**
- **modules/audio_device_manager/core/types.py** - основной тип
- **modules/speech_playback/utils/device_utils.py** - дублирующий тип ❌

### **2. Дублирование функций получения устройств**
- **AudioDeviceManager**: `get_available_devices()` ✅
- **SpeechPlayback**: `get_available_devices()` ❌
- **VoiceRecognition**: `list_audio_devices()` ❌

### **3. Дублирование функций выбора устройств**
- **AudioDeviceManager**: `get_best_device()` ✅
- **SpeechPlayback**: `get_best_audio_device()` ❌
- **VoiceRecognition**: `find_best_microphone()` ❌

### **4. Дублирование приоритетов устройств**
- **AudioDeviceManager**: `device_priorities.py` ✅
- **SpeechRecognizer**: собственные приоритеты в `_pick_input_device()` ❌

### **5. Дублирование источников truth**
- **AudioDeviceManager**: `switchaudio -a` ✅
- **SpeechPlayback**: `sd.query_devices()` ❌
- **VoiceRecognition**: `sd.query_devices()` ❌

---

### **Этап 8: Обновление конфигурации** ⏱️ 15 минут
**Цель**: Добавить новые настройки в unified_config.yaml

#### 8.1 Обновление `config/unified_config.yaml`
```yaml
audio:
  device_manager:
    # ... существующие настройки ...
    
    # Новые настройки для INPUT/OUTPUT
    separate_input_output_management: true
    input_device_priorities:
      builtin_microphone: 1
      usb_microphone: 2
      bluetooth_microphone: 3
      external_microphone: 4
      virtual_microphone: 5
    output_device_priorities:
      airpods: 1
      bluetooth_headphones: 2
      usb_headphones: 3
      external_speakers: 4
      builtin_speakers: 5
```

**Тест**: Проверить что конфигурация загружается корректно.

---

## 🧪 План тестирования

### **📋 Правила тестирования**
1. **НЕ ПЕРЕХОДИМ** к следующему этапу без успешного прохождения всех тестов текущего этапа
2. **При ошибке** - исправляем и повторяем тесты
3. **Документируем** результаты каждого теста
4. **Откатываемся** к предыдущему этапу при критических ошибках

### **Быстрые тесты (5-10 минут каждый этап)**
```bash
# Тест 1: Проверка отсутствия дублирования
grep -r "get_available_devices\|get_best_audio_device" modules/speech_playback/
# Должно быть пусто

# Тест 2: Проверка стабильных ID
python -c "
from modules.audio_device_manager.macos.switchaudio_bridge import SwitchAudioBridge
import asyncio
async def test():
    bridge = SwitchAudioBridge()
    devices = await bridge.get_available_devices()
    for d in devices:
        print(f'{d.id}: {d.name}')
asyncio.run(test())
"
# ID должны быть стабильными между запусками

# Тест 3: Проверка INPUT/OUTPUT разделения
python -c "
from modules.audio_device_manager.core.device_manager import AudioDeviceManager
import asyncio
async def test():
    manager = AudioDeviceManager()
    input_devs = await manager.get_available_devices(DeviceType.INPUT)
    output_devs = await manager.get_available_devices(DeviceType.OUTPUT)
    print(f'Input: {len(input_devs)}, Output: {len(output_devs)}')
asyncio.run(test())
"
```

### **Интеграционные тесты (15-20 минут)**

#### **Тест A: Полный функциональный тест**
```bash
# Запуск приложения
python client/main.py

# Проверка логов при запуске:
# ✅ AudioDeviceManager запущен
# ✅ SwitchAudio мониторинг запущен
# ✅ AudioDeviceIntegration инициализирован
# ✅ SpeechPlaybackIntegration инициализирован
# ✅ VoiceRecognitionIntegration инициализирован
# ✅ AudioDeviceManager инжектирован в SpeechPlayback
# ✅ AudioDeviceManager инжектирован в VoiceRecognition
```

#### **Тест B: Тест переключения OUTPUT устройств**
```bash
# 1. Подключить AirPods
# В логах должно быть:
# 🔄 Обнаружено изменение: X -> Y устройств
# 🔄 Переключение на output устройство: AirPods
# ✅ Переключено на output: AirPods
# audio.device_switched

# 2. Отключить AirPods
# В логах должно быть:
# 🔄 Обнаружено изменение: Y -> X устройств
# 🔄 Переключение на output устройство: MacBook Air Speakers
# ✅ Переключено на output: MacBook Air Speakers
```

#### **Тест C: Тест переключения INPUT устройств**
```bash
# 1. Включить микрофон (переход в LISTENING режим)
# В логах должно быть:
# 🔄 Переключение на input устройство: [device_name]
# ✅ Переключено на input: [device_name]
# audio.microphone_enabled

# 2. Выключить микрофон (переход в SLEEPING режим)
# В логах должно быть:
# audio.microphone_disabled
```

#### **Тест D: Тест стабильности ID**
```bash
# 1. Запустить приложение
python client/main.py
# Записать ID устройств из логов

# 2. Перезапустить приложение
python client/main.py
# Проверить что ID устройств не изменились
```

#### **Тест E: Тест отсутствия конфликтов**
```bash
# Проверить что нет дублирующих событий в логах:
grep -E "(device|audio|microphone)" logs/nexy.log | sort | uniq -c
# Каждое событие должно появляться только один раз
```

#### **Тест F: Тест производительности**
```bash
# Измерить время переключения устройств:
# - Подключение AirPods: < 2 секунд
# - Отключение AirPods: < 2 секунд
# - Включение микрофона: < 1 секунды
# - Выключение микрофона: < 1 секунды
```

### **Сценарии тестирования**
1. **Подключение AirPods** → должен переключиться на AirPods (output)
2. **Отключение AirPods** → должен вернуться на встроенные динамики (output)
3. **Переключение микрофона** → должен работать независимо от динамиков (input)
4. **Перезапуск приложения** → ID устройств должны остаться теми же
5. **Одновременное переключение** → input и output должны работать независимо

---

## 📊 Критерии успеха

### **Функциональные критерии**
- ✅ Нет дублирующих функций управления устройствами
- ✅ Единый источник truth - AudioDeviceManager
- ✅ Стабильные ID устройств между перезапусками
- ✅ Поддержка INPUT/OUTPUT устройств
- ✅ Независимое переключение микрофонов и динамиков
- ✅ Корректная работа при подключении/отключении устройств

### **Архитектурные критерии**
- ✅ Отсутствие конфликтов между модулями
- ✅ Четкое разделение ответственности
- ✅ Единый интерфейс для всех модулей
- ✅ Централизованная конфигурация
- ✅ Логирование всех операций

### **Производительные критерии**
- ✅ Быстрое переключение устройств (< 1 секунды)
- ✅ Отсутствие блокировок при мониторинге
- ✅ Стабильная работа при частых переключениях
- ✅ Корректная обработка ошибок

---

## 🚀 Порядок выполнения

1. **Этап 1** → **Этап 2** → **Этап 3** → **Этап 4** → **Этап 5** → **Этап 6** → **Этап 7** → **Этап 8** → **Этап 9**
2. После каждого этапа - тестирование
3. При ошибках - откат к предыдущему этапу
4. Документирование изменений

### **Критический путь:**
- **Этапы 1-3**: Очистка дублирования + расширение AudioDeviceManager
- **Этап 7**: Dependency injection (критично для интеграции)
- **Этапы 5-6**: Очистка AudioDeviceIntegration и SpeechRecognizer

### **Архитектурные ограничения:**
- ✅ **Не нарушает SimpleModuleCoordinator** - только расширяет существующую логику
- ✅ **Сохраняет EventBus паттерн** - все коммуникации через события
- ✅ **Следует принципу интеграций** - тонкие обертки над модулями
- ✅ **Использует unified_config.yaml** - централизованная конфигурация

---

## 📝 Логирование

Все изменения должны логироваться с префиксами:
- `🎯 [AUDIO_REFACTOR]` - для рефакторинга
- `🔄 [AUDIO_SWITCH]` - для переключений
- `❌ [AUDIO_ERROR]` - для ошибок
- `✅ [AUDIO_SUCCESS]` - для успешных операций
- `🔍 [AUDIO_DEBUG]` - для отладочной информации
- `📊 [AUDIO_STATS]` - для статистики и метрик

### **Ключевые точки для логирования:**
1. **Инициализация модулей** - начало/конец инициализации
2. **Получение устройств** - количество найденных устройств, их типы
3. **Переключение устройств** - до/после переключения, причины
4. **Обработка ошибок** - детали ошибок, контекст
5. **Dependency injection** - успешная/неуспешная инъекция зависимостей
6. **EventBus события** - публикация/подписка на события
7. **Конфигурация** - загрузка/применение настроек
8. **Производительность** - время выполнения операций

### **Шаблоны логирования для каждого этапа:**

#### **Этап 2: AudioDeviceManager**
```python
# Инициализация
logger.info("🎯 [AUDIO_REFACTOR] Начало инициализации AudioDeviceManager...")
logger.debug(f"🔍 [AUDIO_DEBUG] Загрузка конфигурации: {config}")
logger.info("✅ [AUDIO_SUCCESS] AudioDeviceManager инициализирован")

# Получение устройств
logger.debug(f"🔍 [AUDIO_DEBUG] Запрос INPUT устройств...")
logger.info(f"📊 [AUDIO_STATS] Найдено {len(input_devices)} INPUT устройств")
logger.debug(f"🔍 [AUDIO_DEBUG] Запрос OUTPUT устройств...")
logger.info(f"📊 [AUDIO_STATS] Найдено {len(output_devices)} OUTPUT устройств")

# Переключение устройств
logger.info(f"🔄 [AUDIO_SWITCH] Переключение на INPUT устройство: {device.name}")
logger.info(f"✅ [AUDIO_SUCCESS] Переключено на INPUT: {device.name}")
```

#### **Этап 3: SwitchAudioBridge**
```python
# Команды switchaudio
logger.debug(f"🔍 [AUDIO_DEBUG] Выполнение команды: switchaudio -a -t {device_type}")
logger.info(f"📊 [AUDIO_STATS] SwitchAudio вернул {len(devices)} устройств типа {device_type}")

# Стабильные ID
logger.debug(f"🔍 [AUDIO_DEBUG] Генерация стабильного ID для: {device_name}")
logger.info(f"✅ [AUDIO_SUCCESS] Стабильный ID создан: {stable_id}")

# Ошибки
logger.error(f"❌ [AUDIO_ERROR] Ошибка выполнения switchaudio: {error}")
```

#### **Этап 7: Dependency Injection**
```python
# Инъекция зависимостей
logger.info("🎯 [AUDIO_REFACTOR] Начало dependency injection...")
logger.debug(f"🔍 [AUDIO_DEBUG] Инъекция AudioDeviceManager в {integration_name}")
logger.info(f"✅ [AUDIO_SUCCESS] AudioDeviceManager инжектирован в {integration_name}")
logger.warning(f"⚠️ [AUDIO_DEBUG] AudioDeviceManager недоступен для {integration_name}")
```

---

## 🔄 Откат

В случае критических ошибок:
1. Остановить приложение
2. Восстановить файлы из git
3. Проанализировать ошибки
4. Исправить и повторить этап

---

**Общее время выполнения**: ~5-6 часов
**Критический путь**: Этапы 1-3, 7 (очистка + расширение + dependency injection)
**Риски**: 
- Конфликты при одновременном изменении нескольких модулей
- Нарушение порядка инициализации в SimpleModuleCoordinator
- Проблемы с dependency injection между интеграциями
