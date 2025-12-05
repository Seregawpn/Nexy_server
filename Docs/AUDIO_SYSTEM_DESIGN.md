# Архитектура и принципы работы новой аудиосистемы Nexy

**Дата создания:** 2025-01-XX  
**Статус:** Проектирование  
**Owner:** Tech Lead клиента  
**Основан на:** `Docs/AUDIO_SYSTEM_NEW_REQUIREMENTS.md`

---

## Назначение документа

Этот документ описывает, **как должна работать** новая аудиосистема управления устройствами на основе всех требований. Документ показывает архитектуру, потоки данных, взаимодействия компонентов и примеры работы системы.

---

## 1. ОБЩАЯ АРХИТЕКТУРА

### 1.1 Слоистая архитектура

```
┌─────────────────────────────────────────────────────────────────┐
│                    ИНТЕГРАЦИОННЫЙ СЛОЙ                            │
│  integration/integrations/audio_system_integration.py            │
│  - Адаптер между модулем и EventBus                              │
│  - Публикация/подписка событий                                   │
│  - Координация работы компонентов                                │
└─────────────────────────────────────────────────────────────────┘
                              ↕ EventBus
┌─────────────────────────────────────────────────────────────────┐
│                    МОДУЛЬНЫЙ СЛОЙ                                │
│  modules/audio_system/                                           │
│  ├── core/                                                       │
│  │   ├── device_manager.py      - Единый менеджер устройств     │
│  │   ├── device_monitor.py      - Мониторинг изменений           │
│  │   ├── device_state_cache.py  - Кэш состояний устройств        │
│  │   ├── stream_manager.py      - Базовый менеджер потоков       │
│  │   ├── input_stream_manager.py - Менеджер INPUT потоков        │
│  │   └── output_stream_manager.py - Менеджер OUTPUT потоков     │
│  ├── utils/                                                      │
│  │   ├── device_utils.py        - Утилиты работы с устройствами  │
│  │   └── audio_utils.py        - Утилиты обработки аудио         │
│  └── types.py                    - Типы данных                   │
└─────────────────────────────────────────────────────────────────┘
                              ↕ Системные API
┌─────────────────────────────────────────────────────────────────┐
│                    СИСТЕМНЫЙ СЛОЙ                                │
│  - SwitchAudioSource (бинарный файл) - имя default устройства   │
│  - PortAudio (PyAudio/sounddevice) - device_id, потоки          │
│  - Core Audio (PyObjC) - нотификации изменений устройств         │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Принципы работы

**1. Единый источник истины:**
- `DeviceManager` - единственный компонент, который работает с системными API
- `DeviceStateCache` - единственное место хранения состояний устройств
- Все остальные модули получают информацию через эти компоненты

**2. Событийная архитектура:**
- Все взаимодействия через EventBus
- События: `audio.device.input_changed`, `audio.device.output_changed`
- Никаких прямых вызовов между модулями

**3. Централизация:**
- Все утилиты в `device_utils.py` и `audio_utils.py`
- Все операции с потоками через `StreamManager`
- Все мониторинг через `DeviceMonitor`

---

## 2. КОМПОНЕНТЫ СИСТЕМЫ

### 2.0 CoreAudio UID как единый идентификатор

**ВАЖНО:** Все устройства идентифицируются по CoreAudio UID, а не по имени или device_id.

**Принципы:**
- **DeviceDescriptor всегда содержит UID** - это единственный стабильный идентификатор, который не меняется при переподключении
- **Все маппинги** `SwitchAudioSource name → PortAudio device_id → CoreAudio UID` делает исключительно `DeviceManager`
- **Все маппинги кэшируются** для быстрого доступа
- **Все сравнения устройств** используют UID, а не name или device_id
- Если UID недоступен (старые системы) - используется fallback на имя устройства

**Пример правильного использования:**
```python
# Правильно: сравнение по UID
if current_device.uid != new_device.uid:
    # Устройство изменилось
    await stream_manager.switch_device(new_device)

# Неправильно: сравнение по имени или device_id
if current_device.name != new_device.name:  # ❌
    await stream_manager.switch_device(new_device)
```

**Реализация маппинга:**
```python
class DeviceManager:
    def __init__(self):
        self._uid_to_device: Dict[str, DeviceDescriptor] = {}
        self._name_to_uid: Dict[str, str] = {}
        self._device_id_to_uid: Dict[Optional[int], str] = {}
    
    def get_device_by_uid(self, uid: str) -> Optional[DeviceDescriptor]:
        """Получить устройство по UID (из кэша или через системные API)"""
        if uid in self._uid_to_device:
            return self._uid_to_device[uid]
        
        # Получаем через системные API
        device = self._build_device_from_uid(uid)
        if device:
            self._cache_device(device)
        return device
    
    def _build_device_from_uid(self, uid: str) -> Optional[DeviceDescriptor]:
        """Построить DeviceDescriptor из UID через системные API"""
        # 1. Получаем имя через SwitchAudioSource (если нужно)
        # 2. Получаем device_id через PortAudio
        # 3. Получаем параметры через Core Audio
        # 4. Создаем DeviceDescriptor с UID
        pass
```

### 2.1 DeviceManager (Единый менеджер устройств)

**Назначение:** Единственный компонент, который работает с системными API для определения устройств.

**Ответственность:**
- Получение списка доступных устройств
- Определение default INPUT/OUTPUT устройства через SwitchAudioSource
- Поиск device_id по имени через PortAudio
- **Построение маппинга `SwitchAudioSource name → PortAudio device_id → CoreAudio UID`**
- **Кэширование маппингов для быстрого доступа**
- Нормализация параметров устройств
- Определение типа устройства (Bluetooth, builtin, remote)

**Использование:**
```python
# Только DeviceManager может вызывать системные API
device_manager = DeviceManager()
default_input = device_manager.get_default_input_device()  # Использует SwitchAudioSource
device_id = device_manager.find_device_id_by_name("AirPods", "input")  # Использует PortAudio
is_bt = device_manager.is_bluetooth_device("AirPods")  # Использует device_utils
```

**Запрещено:**
- Прямые вызовы `SwitchAudioSource`, `sd.query_devices()` в других модулях
- Дублирование логики определения устройств

### 2.2 DeviceStateCache (Кэш состояний устройств)

**Назначение:** Единое место хранения текущих состояний устройств.

**Ответственность:**
- Хранение текущего INPUT устройства (имя, device_id, параметры)
- Хранение текущего OUTPUT устройства (имя, device_id, параметры)
- Thread-safe доступ к состояниям
- Обновление состояний при смене устройств

**Использование:**
```python
# Все модули читают состояние из DeviceStateCache
cache = DeviceStateCache()
input_device = cache.get_default_input()  # DeviceDescriptor
output_device = cache.get_default_output()  # DeviceDescriptor

# Обновление только через DeviceMonitor
cache.update_default_input(device_descriptor)
```

**Запрещено:**
- Локальные переменные `_current_device`, `_device_name` в других модулях
- Прямое обновление кэша из других модулей (только через DeviceMonitor)

### 2.3 DeviceMonitor (Мониторинг изменений)

**Назначение:** Единственный компонент, который мониторит изменения устройств.

**Ответственность:**
- Подписка на Core Audio нотификации (приоритет 1)
- Polling fallback (интервал 2.0 сек) если нотификации недоступны
- Обновление DeviceStateCache при обнаружении изменений
- Публикация событий `audio.device.input_changed` / `audio.device.output_changed`
- Debounce механизм (300ms) для предотвращения множественных публикаций

**Поток работы:**
```
1. DeviceMonitor.start_monitoring() - запускается при инициализации и работает ПОСТОЯННО
   ├─ Подписка на Core Audio нотификации (kAudioHardwarePropertyDefaultInputDevice)
   ├─ Подписка на Core Audio нотификации (kAudioHardwarePropertyDefaultOutputDevice)
   └─ Запуск polling fallback (всегда, для гарантированного обнаружения)
      └─ Polling работает в отдельном потоке (daemon thread) и НЕ останавливается

2. ПОСТОЯННЫЙ МОНИТОРИНГ (работает непрерывно):
   ├─ Core Audio нотификации работают в фоновом режиме
   │   └─ Мгновенная реакция на изменения (< 50ms)
   ├─ Polling fallback опрашивает устройства каждые 2.0 сек
   │   └─ Гарантирует обнаружение даже если нотификации не сработали
   └─ Оба механизма работают параллельно для максимальной надежности

3. При обнаружении изменения (Core Audio notification или polling):
   ├─ DeviceMonitor обнаруживает изменение UID default устройства
   ├─ Определяет, что это новое устройство (сравнение с кэшем)
   ├─ Получает новое устройство через DeviceManager
   │   ├─ SwitchAudioSource → имя устройства
   │   └─ PortAudio → device_id
   ├─ Нормализует параметры устройства
   ├─ Обновляет DeviceStateCache
   └─ МГНОВЕННО публикует событие audio.device.input_changed / audio.device.output_changed
      ├─ Debounce: если событие уже опубликовано за последние 300ms, пропускаем
      └─ Подписчики автоматически переключаются на новое устройство
```

**Ключевые особенности:**
- ✅ **Непрерывный мониторинг:** Работает с момента старта до завершения приложения
- ✅ **Обнаружение новых устройств:** Отслеживает не только смену, но и подключение новых устройств
- ✅ **Мгновенное переключение:** Автоматическое переключение при обнаружении нового default устройства
- ✅ **Двойная гарантия:** Core Audio нотификации + polling fallback работают параллельно

**Запрещено:**
- Параллельный polling в других модулях
- Публикация событий смены устройств из других мест
- Синхронные вызовы SwitchAudioSource в callback'ах

### 2.4 StreamManager (Управление потоками)

**Назначение:** Единый компонент для создания и управления PortAudio потоками.

**Ответственность:**
- Создание INPUT/OUTPUT потоков через PortAudio
- Закрытие потоков с гарантированным освобождением ресурсов
- Переключение устройств во время работы потока
- Retry логика с экспоненциальным backoff
- Обработка ошибок PortAudio (-9986, -10851)
- Специальная обработка Bluetooth устройств

**Использование:**
```python
# INPUT поток
input_manager = InputStreamManager(device_state_cache, device_manager)
result = await input_manager.create_stream(
    sample_rate=48000,
    channels=1,
    blocksize=1024
)
stream = result.stream

# OUTPUT поток
output_manager = OutputStreamManager(device_state_cache, device_manager)
result = await output_manager.create_stream(
    sample_rate=48000,
    channels=2,
    blocksize=1024
)
stream = result.stream

# Переключение устройства
result = await stream_manager.switch_device(old_stream, new_device_config)
```

**Запрещено:**
- Прямое создание потоков через `sd.InputStream()` / `sd.OutputStream()` в других модулях
- Дублирование логики retry и обработки ошибок

### 2.5 DeviceUtils (Утилиты работы с устройствами)

**Назначение:** Единое место для всех утилит работы с устройствами.

**Функции:**
```python
# Определение типа устройства
is_bluetooth_device(name: str) -> bool
is_remote_device(name: str) -> bool
is_builtin_device(name: str) -> bool
classify_device(name: str, direction: str) -> int

# Поиск устройств
find_device_id_by_name(name: str, direction: str) -> Optional[int]
get_system_default_device(direction: str) -> tuple[Optional[str], Optional[int]]

# Построение конфигурации
build_stream_config(device_name, device_id, is_bluetooth, ...) -> StreamConfig
```

**Запрещено:**
- Дублирование этих функций в других модулях
- Прямые вызовы системных API для определения устройств

### 2.6 AudioUtils (Утилиты обработки аудио)

**Назначение:** Единое место для всех утилит обработки аудио данных.

**Функции:**
```python
# Обработка аудио
normalize_audio(audio_data: np.ndarray, target_dtype: np.dtype) -> np.ndarray
resample_audio(audio_data: np.ndarray, original_rate: int, target_rate: int) -> np.ndarray
convert_channels(audio_data: np.ndarray, target_channels: int) -> np.ndarray

# Анализ аудио
calculate_rms(audio_data: np.ndarray) -> float
detect_silence(audio_data: np.ndarray, threshold: float) -> bool
```

**Запрещено:**
- Дублирование этих функций в других модулях

---

## 3. ПОТОКИ РАБОТЫ СИСТЕМЫ

### 3.1 Инициализация системы

```
1. SimpleModuleCoordinator создает AudioSystemIntegration (позиция 9)
   └─ AudioSystemIntegration.initialize()
      ├─ Создает DeviceManager
      ├─ Создает DeviceStateCache
      ├─ Создает DeviceMonitor
      ├─ Создает InputStreamManager
      ├─ Создает OutputStreamManager
      └─ Запускает DeviceMonitor.start_monitoring()
         ├─ Подписка на Core Audio нотификации
         ├─ Инициализация начального состояния устройств
         └─ Запуск polling fallback

2. DeviceMonitor определяет начальные устройства
   ├─ DeviceManager.get_default_input_device() → SwitchAudioSource
   ├─ DeviceManager.find_device_id_by_name() → PortAudio
   ├─ DeviceStateCache.update_default_input(descriptor)
   ├─ DeviceManager.get_default_output_device() → SwitchAudioSource
   ├─ DeviceManager.find_device_id_by_name() → PortAudio
   └─ DeviceStateCache.update_default_output(descriptor)

3. Система готова к работе
   └─ DeviceStateCache содержит актуальные устройства
```

### 3.2 Обнаружение смены устройства и подключения новых устройств

```
1. Пользователь подключает новое устройство (например, надевает AirPods)
   └─ macOS автоматически переключает default INPUT/OUTPUT на новое устройство

2. DeviceMonitor ПОСТОЯННО мониторит изменения (Core Audio нотификация или polling через 2.0 сек):
   └─ DeviceMonitor._on_device_changed(direction="input", new_uid)
      ├─ Обнаружение: новый UID отличается от кэшированного
      ├─ Определение: это новое устройство (не было в кэше)
      ├─ ПОЛУЧЕНИЕ ВСЕХ НЕОБХОДИМЫХ ДАННЫХ:
      │   └─ DeviceManager.get_device_by_uid(new_uid)
      │      ├─ SwitchAudioSource → имя устройства ("Sergiy's AirPods")
      │      ├─ PortAudio → device_id (5 или None для BT)
      │      ├─ Core Audio → uid, sample_rate, channels, latency
      │      └─ DeviceUtils.is_bluetooth_device() → is_bluetooth (True)
      ├─ ВАЛИДАЦИЯ ДАННЫХ:
      │   ├─ Проверка наличия обязательных данных (device_name, uid)
      │   ├─ Проверка корректности параметров (sample_rate в диапазоне, channels > 0)
      │   ├─ Проверка доступности устройства (существует в PortAudio или BT)
      │   └─ Если валидация не прошла → публикация ошибки, переключение не происходит
      ├─ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ:
      │   └─ DeviceManager.normalize_device_params(device)
      │      ├─ INPUT: sample_rate → 16000-48000 Hz, channels=1
      │      ├─ OUTPUT: sample_rate → 16000-48000 Hz, channels → 1-2
      │      └─ Для BT: device=None, без blocksize/latency
      ├─ DeviceStateCache.update_default_input(new_descriptor)
      └─ МГНОВЕННАЯ публикация события (debounce 300ms):
         └─ EventBus.publish("audio.device.input_changed", {
               "device_name": "Sergiy's AirPods",
               "device_id": None,  # BT устройство
               "uid": "AirPods-UID",
               "is_bluetooth": True,
               "sample_rate": 48000,
               "channels": 1,
               "blocksize": None,  # BT устройство
               "latency": None,    # BT устройство
               "old_device_name": "MacBook Air Microphone",
               "old_device_id": 3,
               "is_new_device": True  # Флаг нового устройства
            })

3. Подписчики МГНОВЕННО получают событие и автоматически переключаются:
   ├─ VoiceRecognitionIntegration._on_input_device_changed()
   │   └─ SpeechRecognizer.on_device_changed()
   │      └─ InputStreamManager.switch_device()
   │         ├─ Закрывает старый поток
   │         ├─ Создает новый поток на новом устройстве
   │         └─ Продолжает запись (если была активна)
   │
   └─ SpeechPlaybackIntegration._on_output_device_changed()
      └─ SequentialSpeechPlayer._switch_output_device()
         └─ OutputStreamManager.switch_device()
            ├─ Сохраняет буфер воспроизведения
            ├─ Закрывает старый поток
            ├─ Создает новый поток на новом устройстве
            └─ Продолжает воспроизведение
```

### 3.3 Создание INPUT потока (запись с микрофона)

```
1. VoiceRecognitionIntegration получает voice.recording_start
   └─ SpeechRecognizer.start_listening()

2. SpeechRecognizer использует InputStreamManager:
   └─ input_manager.create_stream()
      ├─ ПОЛУЧЕНИЕ ВСЕХ НЕОБХОДИМЫХ ДАННЫХ:
      │   ├─ Получает устройство из DeviceStateCache
      │   │   └─ cache.get_default_input() → DeviceDescriptor
      │   │      ├─ device_name, device_id, uid, is_bluetooth
      │   │      ├─ sample_rate, channels, blocksize, latency
      │   │      └─ Все данные уже получены и валидированы
      │   └─ Если cache пуст → fallback на системный дефолт
      │      └─ DeviceManager.get_default_input_device()
      │         ├─ SwitchAudioSource → device_name
      │         ├─ PortAudio → device_id
      │         ├─ Core Audio → параметры (sample_rate, channels, ...)
      │         └─ DeviceUtils → is_bluetooth
      ├─ ВАЛИДАЦИЯ ДАННЫХ:
      │   ├─ Проверка наличия обязательных данных
      │   ├─ Проверка корректности параметров
      │   └─ Если валидация не прошла → ошибка, поток не создается
      ├─ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ:
      │   └─ DeviceManager.normalize_device_params()
      │      ├─ INPUT: sample_rate → 16000-48000 Hz, channels=1
      │      └─ Для BT: device=None, без blocksize/latency
      ├─ Для BT устройств: задержка bt_prestart_delay (0.5s)
      ├─ СОЗДАНИЕ ПОТОКА С ПРАВИЛЬНЫМИ ПАРАМЕТРАМИ:
      │   └─ sd.InputStream(
      │         device=device_id,  # или None для BT
      │         channels=1,        # всегда моно для INPUT
      │         samplerate=48000,  # нормализованный rate
      │         blocksize=1024,    # только для обычных устройств
      │         latency=0.021,     # только для обычных устройств
      │         ...
      │      )
      ├─ Retry логика при ошибках (до 7 попыток для BT, 3 для обычных)
      ├─ Обработка ошибок PortAudio (-9986, -10851)
      └─ Возвращает StreamResult с потоком

3. Поток готов к записи
   └─ SpeechRecognizer._audio_callback получает чанки
      ├─ PortAudio возвращает данные в float32
      ├─ Сохранение в буфер (self.audio_data)
      └─ При завершении записи → _recognize_audio()
         ├─ Конкатенация всех чанков
         ├─ Конвертация форматов для SpeechRecognition:
         │   ├─ Ресемплинг до 16000 Hz (если actual_rate != 16000)
         │   ├─ Конвертация каналов в моно (если channels > 1)
         │   ├─ Нормализация: float32 → int16
         │   └─ Конвертация в bytes: audio_int16.tobytes()
         ├─ Создание AudioData для SpeechRecognition:
         │   └─ sr.AudioData(audio_bytes, sample_rate=16000, sample_width=2)
         └─ Передача в SpeechRecognition для распознавания
```

### 3.4 Создание OUTPUT потока (воспроизведение)

```
1. SpeechPlaybackIntegration получает grpc.response.audio
   └─ SequentialSpeechPlayer.add_audio_data()

2. SequentialSpeechPlayer использует OutputStreamManager:
   └─ output_manager.create_stream()  # Если поток еще не создан
      ├─ ПОЛУЧЕНИЕ ВСЕХ НЕОБХОДИМЫХ ДАННЫХ:
      │   ├─ Получает устройство из DeviceStateCache
      │   │   └─ cache.get_default_output() → DeviceDescriptor
      │   │      ├─ device_name, device_id, uid, is_bluetooth
      │   │      ├─ sample_rate, channels, blocksize, latency
      │   │      └─ Все данные уже получены и валидированы
      │   └─ Если cache пуст → fallback на системный дефолт
      │      └─ DeviceManager.get_default_output_device()
      │         ├─ SwitchAudioSource → device_name
      │         ├─ PortAudio → device_id
      │         ├─ Core Audio → параметры (sample_rate, channels, ...)
      │         └─ DeviceUtils → is_bluetooth
      ├─ ВАЛИДАЦИЯ ДАННЫХ:
      │   ├─ Проверка наличия обязательных данных
      │   ├─ Проверка корректности параметров
      │   └─ Если валидация не прошла → ошибка, поток не создается
      ├─ НОРМАЛИЗАЦИЯ ПАРАМЕТРОВ:
      │   └─ DeviceManager.normalize_device_params()
      │      ├─ OUTPUT: sample_rate → 16000-48000 Hz, channels → 1-2
      │      └─ Для BT: device=None, channels=1, без blocksize/latency
      ├─ Для BT устройств:
      │   ├─ device=None (macOS управляет параметрами)
      │   ├─ channels=1 (из конфига)
      │   └─ Не задаются blocksize и latency
      ├─ Для BT устройств: задержка bt_prestart_delay (2.5s)
      ├─ СОЗДАНИЕ ПОТОКА С ПРАВИЛЬНЫМИ ПАРАМЕТРАМИ:
      │   └─ sd.OutputStream(
      │         device=device_id,  # или None для BT
      │         channels=2,        # нормализованные channels (1-2)
      │         samplerate=48000,  # нормализованный rate
      │         blocksize=1024,    # только для обычных устройств
      │         latency=0.021,     # только для обычных устройств
      │         ...
      │      )
      ├─ Retry логика при ошибках
      ├─ Обработка ошибок PortAudio (-9986, -10851)
      └─ Возвращает StreamResult с потоком

3. Поток готов к воспроизведению
   └─ SequentialSpeechPlayer._audio_callback воспроизводит чанки
      ├─ Получает данные из ChunkBuffer (int16 или float32)
      ├─ Конвертация форматов для sounddevice:
      │   ├─ Ресемплинг до 48000 Hz (если sample_rate != 48000)
      │   ├─ Конвертация каналов (моно → стерео, если нужно)
      │   └─ Нормализация формата (int16 или float32)
      └─ Записывает в outdata (PortAudio воспроизводит)
         └─ sounddevice автоматически обрабатывает данные
```

### 3.5 Мониторинг уровня шума

```
1. InputStreamManager создает поток и начинает запись

2. Каждый чанк аудио обрабатывается:
   └─ input_manager._process_audio_chunk(chunk)
      ├─ AudioUtils.calculate_rms(chunk)
      │   └─ rms = sqrt(mean(chunk.astype(float32) ** 2))
      ├─ Обновление статистики (rms_avg, rms_peak)
      └─ Проверка порогов:
         ├─ Если rms < noise_threshold_min (0.001):
         │   └─ Предупреждение: audio.device.low_signal
         ├─ Если rms > noise_threshold_max (0.9):
         │   └─ Нормализация громкости: chunk *= (0.9 / rms)
         └─ Если rms < silence_threshold (0.01) в течение silent_window_seconds (0.3s):
            └─ Обнаружение тишины: audio.silence.detected

3. Логирование метрик (если log_health_checks: true):
   └─ [NOISE] RMS={rms:.6f}, peak={peak:.6f}, avg={avg:.6f}, device={device_name}
```

### 3.6 Переключение устройства во время записи (правильное без ошибок)

```
1. Пользователь надевает AirPods во время записи

2. DeviceMonitor обнаруживает смену устройства:
   └─ Публикует audio.device.input_changed с ВСЕМИ данными:
      {
         "device_name": "Sergiy's AirPods",
         "device_id": None,
         "uid": "AirPods-UID",
         "is_bluetooth": True,
         "sample_rate": 48000,
         "channels": 1,
         "blocksize": None,
         "latency": None
      }

3. VoiceRecognitionIntegration получает событие:
   └─ SpeechRecognizer.on_device_changed(event_data)
      ├─ ПРОВЕРКА ДАННЫХ ИЗ СОБЫТИЯ:
      │   ├─ Проверка наличия всех необходимых данных
      │   ├─ Если данных не хватает → запрос через DeviceManager
      │   └─ Валидация данных перед переключением
      └─ ПРАВИЛЬНОЕ ПЕРЕКЛЮЧЕНИЕ БЕЗ ОШИБОК:
         └─ input_manager.switch_device(old_stream, new_device_config)
            ├─ 1. Сохранение текущего буфера записи (не теряет данные)
            ├─ 2. Graceful stop старого потока:
            │   ├─ stream.stop()
            │   ├─ stream.close()
            │   ├─ Ожидание active=False (таймаут 3с для BT, 1с для обычных)
            │   └─ Задержка close_delay (2.5с для BT, 0.3с для обычных)
            ├─ 3. Создание нового потока с ПРАВИЛЬНЫМИ параметрами:
            │   ├─ Для BT: device=None, channels=1, без blocksize/latency
            │   ├─ Для обычных: device_id, sample_rate=48000, channels=1, blocksize=1024
            │   ├─ Задержка bt_prestart_delay (0.5s для BT)
            │   ├─ sd.InputStream(device=new_device_id, channels=1, samplerate=48000, ...)
            │   └─ Retry логика при ошибках (до 7 попыток для BT, 3 для обычных)
            ├─ 4. Обработка ошибок PortAudio (-9986, -10851):
            │   ├─ При ошибке -9986: принудительное закрытие, задержка, повторная попытка
            │   ├─ При ошибке -10851: fallback на device=None (для BT)
            │   └─ Логирование ошибок с контекстом
            ├─ 5. Проверка успешности создания потока
            ├─ 6. Восстановление буфера записи
            └─ 7. Продолжение записи на новом устройстве
               └─ Восстанавливает буфер (продолжает с того места, где остановился)

4. Запись продолжается без потери данных и БЕЗ ОШИБОК
```

### 3.7 Переключение устройства во время воспроизведения (правильное без ошибок)

```
1. Пользователь переключает OUTPUT устройство во время воспроизведения

2. DeviceMonitor обнаруживает смену устройства:
   └─ Публикует audio.device.output_changed с ВСЕМИ данными:
      {
         "device_name": "Sergiy's AirPods",
         "device_id": None,
         "uid": "AirPods-UID",
         "is_bluetooth": True,
         "sample_rate": 48000,
         "channels": 1,
         "blocksize": None,
         "latency": None
      }

3. SpeechPlaybackIntegration получает событие:
   └─ SequentialSpeechPlayer._switch_output_device(event_data)
      ├─ ПРОВЕРКА ДАННЫХ ИЗ СОБЫТИЯ:
      │   ├─ Проверка наличия всех необходимых данных
      │   ├─ Если данных не хватает → запрос через DeviceManager
      │   └─ Валидация данных перед переключением
      └─ ПРАВИЛЬНОЕ ПЕРЕКЛЮЧЕНИЕ БЕЗ ОШИБОК:
         └─ output_manager.switch_device(old_stream, new_device_config)
            ├─ 1. Сохранение буфера воспроизведения (ChunkBuffer не очищается)
            ├─ 2. Graceful stop старого потока:
            │   ├─ stream.stop()
            │   ├─ stream.close()
            │   ├─ Ожидание active=False (таймаут 3с для BT, 1с для обычных)
            │   └─ Задержка close_delay (2.5с для BT, 0.3с для обычных)
            ├─ 3. Создание нового потока с ПРАВИЛЬНЫМИ параметрами:
            │   ├─ Для BT: device=None, channels=1, без blocksize/latency
            │   ├─ Для обычных: device_id, sample_rate=48000, channels=2, blocksize=1024
            │   ├─ Задержка bt_prestart_delay (2.5s для BT)
            │   ├─ sd.OutputStream(device=new_device_id, channels=2, samplerate=48000, ...)
            │   └─ Retry логика при ошибках (до 7 попыток для BT, 3 для обычных)
            ├─ 4. Обработка ошибок PortAudio (-9986, -10851):
            │   ├─ При ошибке -9986: принудительное закрытие, задержка, повторная попытка
            │   ├─ При ошибке -10851: fallback на device=None (для BT)
            │   └─ Логирование ошибок с контекстом
            ├─ 5. Проверка успешности создания потока
            ├─ 6. Восстановление буфера воспроизведения
            └─ 7. Продолжение воспроизведения на новом устройстве
               └─ Восстанавливает буфер (продолжает с того места, где остановился)

4. Воспроизведение продолжается без пауз и БЕЗ ОШИБОК
```

### 3.8 Правильное взаимодействие с библиотеками записи и воспроизведения

#### 3.8.1 Взаимодействие с SpeechRecognition (запись)

```
1. InputStreamManager создает поток с параметрами устройства:
   └─ sd.InputStream(device=device_id, channels=1, samplerate=48000, dtype='float32')
      └─ PortAudio возвращает данные в float32

2. SpeechRecognizer._audio_callback получает чанки:
   └─ indata (float32, shape=(frames, 1), samplerate=48000)
      ├─ Сохранение в буфер: self.audio_data.append(indata.copy())
      └─ Накопление чанков до завершения записи

3. При завершении записи (voice.recording_stop):
   └─ SpeechRecognizer._recognize_audio()
      ├─ Конкатенация всех чанков:
      │   └─ audio_data = np.concatenate(self.audio_data, axis=0).astype(np.float32)
      ├─ РЕСЕМПЛИНГ до 16000 Hz (если actual_rate != 16000):
      │   └─ AudioUtils.resample_audio(audio_data, actual_rate=48000, target_rate=16000)
      ├─ КОНВЕРТАЦИЯ КАНАЛОВ в моно (если channels > 1):
      │   └─ AudioUtils.convert_channels(audio_data, target_channels=1)
      ├─ НОРМАЛИЗАЦИЯ и конвертация в int16:
      │   ├─ audio_float = np.clip(audio_data, -1.0, 1.0).astype(np.float32)
      │   └─ audio_bytes = (audio_float * 32767.0).astype(np.int16).tobytes()
      ├─ Создание AudioData для SpeechRecognition:
      │   └─ audio_data_obj = sr.AudioData(
      │         audio_bytes,        # bytes в формате int16
      │         sample_rate=16000,  # Целевой rate для ASR
      │         sample_width=2       # 2 байта для int16
      │      )
      └─ Передача в SpeechRecognition:
         └─ text = recognizer.recognize_google(audio_data_obj, language="en-US")
```

**Требования к формату данных для SpeechRecognition:**
- ✅ `sample_rate`: 16000 Hz (обязательно)
- ✅ `channels`: 1 (моно, обязательно)
- ✅ `dtype`: int16 (обязательно)
- ✅ `sample_width`: 2 (2 байта для int16)
- ✅ Формат: `bytes` в `sr.AudioData`

#### 3.8.2 Взаимодействие с sounddevice/pydub (воспроизведение)

```
1. gRPC возвращает аудио чанки:
   └─ grpc.response.audio{session_id, audio_data, dtype, sample_rate, channels}
      ├─ audio_data: bytes (int16 PCM)
      ├─ sample_rate: обычно 48000 Hz (от сервера)
      └─ channels: обычно 1 (моно от сервера)

2. SpeechPlaybackIntegration получает чанк:
   └─ _on_audio_chunk(event)
      ├─ Декодирование bytes в numpy:
      │   └─ audio_data = np.frombuffer(event['audio_data'], dtype=np.int16)
      ├─ Ресемплинг до 48000 Hz (если sample_rate != 48000):
      │   └─ AudioUtils.resample_audio(audio_data, original_rate, target_rate=48000)
      ├─ Конвертация каналов (если нужно):
      │   └─ AudioUtils.convert_channels(audio_data, target_channels=2)  # моно → стерео
      └─ Добавление в буфер воспроизведения:
         └─ player.add_audio_data(audio_data, priority=0)

3. SequentialSpeechPlayer._audio_callback воспроизводит:
   └─ Получает данные из ChunkBuffer
      ├─ Данные уже в правильном формате (int16, 48000 Hz, 1-2 канала)
      ├─ Конвертация для sounddevice (если нужно):
      │   └─ outdata[:] = audio_data.reshape(-1, channels)
      └─ sounddevice автоматически воспроизводит
```

**Требования к формату данных для sounddevice:**
- ✅ `sample_rate`: 48000 Hz (стандарт для воспроизведения)
- ✅ `channels`: 1 (моно) или 2 (стерео) - определяется устройством
- ✅ `dtype`: int16 или float32
- ✅ Формат: `np.ndarray` с правильной формой (frames, channels)

#### 3.8.3 Гарантии правильного формата данных

**Для INPUT (SpeechRecognition):**
- ✅ Все данные ресемплятся до 16000 Hz перед передачей в SpeechRecognition
- ✅ Все данные конвертируются в моно (channels=1) перед передачей в SpeechRecognition
- ✅ Все данные конвертируются в int16 перед передачей в SpeechRecognition
- ✅ Конвертация в bytes выполняется правильно: `audio_int16.tobytes()`
- ✅ AudioData создается с правильными параметрами: `sample_rate=16000, sample_width=2`

**Для OUTPUT (sounddevice):**
- ✅ Все данные ресемплятся до 48000 Hz перед передачей в sounddevice
- ✅ Конвертация каналов выполняется правильно (моно → стерео при необходимости)
- ✅ Формат данных соответствует требованиям sounddevice (int16 или float32)
- ✅ Форма массива правильная: `(frames, channels)`

**Проверка правильности формата:**
- Логи показывают все конвертации с параметрами (исходный → целевой формат)
- Тесты проверяют формат данных перед передачей в библиотеки
- Ошибки формата логируются с детальной информацией

### 3.9 Защита от параллельных переключений устройств

**Проблема:** При быстрой смене устройств могут возникать race conditions, когда несколько переключений выполняются параллельно.

**Решение:** Использование блокировки `switch_in_progress` и очереди переключений.

```
1. InputStreamManager/OutputStreamManager получают событие audio.device.*_changed
   └─ Проверка switch_in_progress:
      ├─ Если False → начинаем переключение:
      │   ├─ Устанавливаем switch_in_progress = True
      │   ├─ Выполняем переключение (graceful stop → создание нового потока)
      │   └─ Сбрасываем switch_in_progress = False
      └─ Если True → отменяем старое переключение или ставим в очередь:
         ├─ Вариант 1 (рекомендуется): Отменяем старое, начинаем новое
         │   └─ Логируем: "Отменяем старое переключение, начинаем новое с актуальными данными"
         └─ Вариант 2: Ставим в очередь, выполняем после завершения текущего
            └─ Логируем: "Переключение в очереди, выполним после завершения текущего"
```

**Реализация:**
```python
class InputStreamManager:
    def __init__(self):
        self._switch_lock = threading.Lock()
        self._switch_in_progress = False
    
    async def switch_device(self, new_device: DeviceDescriptor):
        with self._switch_lock:
            if self._switch_in_progress:
                logger.warning("Переключение уже в процессе, отменяем старое")
                # Отменяем старое переключение (если возможно)
                # Или ставим в очередь
                return
        
            self._switch_in_progress = True
        
        try:
            # Выполняем переключение
            await self._do_switch_device(new_device)
        finally:
            with self._switch_lock:
                self._switch_in_progress = False
```

---

## 4. ИНТЕГРАЦИЯ С СУЩЕСТВУЮЩИМИ МОДУЛЯМИ

### 4.1 Интеграция с VoiceRecognitionIntegration

**Как работает:**
```python
# VoiceRecognitionIntegration получает InputStreamManager через конструктор
class VoiceRecognitionIntegration:
    def __init__(self, ..., input_stream_manager: InputStreamManager):
        self._input_stream_manager = input_stream_manager
        self._device_state_cache = input_stream_manager.device_state_cache
        
    def _on_recording_start(self, event):
        # Использует InputStreamManager для создания потока
        result = await self._input_stream_manager.create_stream(...)
        stream = result.stream
        
    def _on_input_device_changed(self, event):
        # Переключает устройство через InputStreamManager
        await self._input_stream_manager.switch_device(...)
```

**Что НЕ делает:**
- ❌ Не вызывает SwitchAudioSource напрямую
- ❌ Не опрашивает устройства
- ❌ Не создает потоки напрямую через sd.InputStream()
- ❌ Не хранит локальные копии состояния устройств

### 4.2 Интеграция с SpeechPlaybackIntegration

**Как работает:**
```python
# SpeechPlaybackIntegration получает OutputStreamManager через конструктор
class SpeechPlaybackIntegration:
    def __init__(self, ..., output_stream_manager: OutputStreamManager):
        self._output_stream_manager = output_stream_manager
        self._device_state_cache = output_stream_manager.device_state_cache
        
    def _on_audio_chunk(self, event):
        # Использует OutputStreamManager для создания потока
        if not self._stream_active:
            result = await self._output_stream_manager.create_stream(...)
            stream = result.stream
            
    def _on_output_device_changed(self, event):
        # Переключает устройство через OutputStreamManager
        await self._output_stream_manager.switch_device(...)
```

**Что НЕ делает:**
- ❌ Не проверяет устройство при каждом чанке
- ❌ Не вызывает SwitchAudioSource в callback'ах
- ❌ Не создает потоки напрямую через sd.OutputStream()
- ❌ Не хранит локальные копии состояния устройств

---

## 5. ПРИМЕРЫ РАБОТЫ СИСТЕМЫ

### 5.1 Пример 1: Первый запуск приложения

```
1. Приложение запускается
   └─ SimpleModuleCoordinator создает интеграции

2. AudioSystemIntegration.initialize() (позиция 9)
   ├─ Создает DeviceManager
   ├─ Создает DeviceStateCache
   ├─ Создает DeviceMonitor
   ├─ Создает InputStreamManager, OutputStreamManager
   └─ DeviceMonitor.start_monitoring()
      ├─ Подписка на Core Audio нотификации
      └─ Запуск polling fallback

3. DeviceMonitor определяет начальные устройства
   ├─ INPUT: "MacBook Air Microphone" (device_id=3)
   └─ OUTPUT: "MacBook Air Speakers" (device_id=2)

4. DeviceStateCache обновлен
   └─ Система готова к работе

5. VoiceRecognitionIntegration инициализируется (позиция 11)
   └─ Получает InputStreamManager и DeviceStateCache

6. SpeechPlaybackIntegration инициализируется (позиция 16)
   └─ Получает OutputStreamManager и DeviceStateCache
```

### 5.2 Пример 2: Пользователь надевает AirPods (новое устройство)

```
1. Пользователь надевает AirPods (новое устройство подключается)
   └─ macOS автоматически переключает default INPUT/OUTPUT на AirPods

2. DeviceMonitor ПОСТОЯННО мониторит изменения:
   └─ Обнаружение происходит через Core Audio нотификацию (< 50ms) или polling (через 2 сек максимум)
   └─ DeviceMonitor._on_device_changed("input", new_uid="AirPods-UID")
      ├─ Обнаружение: новый UID "AirPods-UID" отличается от кэшированного (сравнение по UID!)
      ├─ Определение: это новое устройство (не было в кэше)
      ├─ DeviceManager.get_device_by_uid("AirPods-UID")
      │   ├─ Проверка кэша маппинга UID → DeviceDescriptor
      │   ├─ Если нет в кэше → построение маппинга через системные API
      │   │   ├─ SwitchAudioSource → "Sergiy's AirPods" (имя)
      │   │   ├─ PortAudio → device_id=None (BT устройство)
      │   │   └─ Core Audio → параметры (sample_rate, channels, ...)
      │   └─ Кэширование маппинга для быстрого доступа
      │   ├─ SwitchAudioSource → "Sergiy's AirPods"
      │   └─ PortAudio → device_id=None (BT устройство, macOS управляет параметрами)
      ├─ DeviceManager.is_bluetooth_device("Sergiy's AirPods") → True
      ├─ DeviceManager.normalize_device_params()
      │   └─ Для BT: device=None, channels=1, без blocksize/latency
      ├─ DeviceStateCache.update_default_input(new_descriptor)
      └─ МГНОВЕННАЯ публикация события (< 500ms от момента подключения):
         └─ EventBus.publish("audio.device.input_changed", {
               "device_name": "Sergiy's AirPods",
               "device_id": None,  # BT устройство
               "is_bluetooth": True,
               "old_device_name": "MacBook Air Microphone",
               "old_device_id": 3,
               "is_new_device": True  # Флаг нового устройства
            })

3. VoiceRecognitionIntegration МГНОВЕННО получает событие и автоматически переключается:
   └─ SpeechRecognizer.on_device_changed(event_data)
      ├─ ПРОВЕРКА ДАННЫХ ИЗ СОБЫТИЯ:
      │   ├─ Проверка наличия всех необходимых данных (device_name, uid, is_bluetooth)
      │   ├─ Проверка параметров (sample_rate, channels)
      │   └─ Если данных не хватает → запрос данных через DeviceManager
      └─ Если запись активна:
         ├─ ПРАВИЛЬНОЕ ПЕРЕКЛЮЧЕНИЕ БЕЗ ОШИБОК:
         │   └─ input_manager.switch_device(old_stream, new_device_config)
         │      ├─ 1. Сохранение текущего буфера записи (не теряет данные)
         │      ├─ 2. Graceful stop старого потока:
         │      │   ├─ stream.stop()
         │      │   ├─ stream.close()
         │      │   ├─ Ожидание active=False (таймаут 3с для BT, 1с для обычных)
         │      │   └─ Задержка close_delay (2.5с для BT, 0.3с для обычных)
         │      ├─ 3. Создание нового потока с ПРАВИЛЬНЫМИ параметрами:
         │      │   ├─ Для BT: device=None, channels=1, без blocksize/latency
         │      │   ├─ Для обычных: device_id, sample_rate, channels=1, blocksize, latency
         │      │   ├─ Задержка bt_prestart_delay (0.5s для BT)
         │      │   ├─ sd.InputStream(device=new_device_id, channels=1, samplerate=48000, ...)
         │      │   └─ Retry логика при ошибках (до 7 попыток для BT, 3 для обычных)
         │      ├─ 4. Проверка успешности создания потока
         │      ├─ 5. Восстановление буфера записи
         │      └─ 6. Продолжение записи на новом устройстве
         │         └─ Восстанавливает буфер (продолжает с того места, где остановился)
         └─ Если запись не активна:
            └─ Просто обновляет конфигурацию для следующего запуска

4. Аналогично для OUTPUT устройства
   └─ SpeechPlaybackIntegration получает audio.device.output_changed
      └─ output_manager.switch_device(...)
         └─ Переключает воспроизведение на AirPods
```

### 5.3 Пример 3: Запись речи с автоматическим обнаружением тишины

```
1. Пользователь нажимает LONG_PRESS
   └─ VoiceRecognitionIntegration._on_recording_start()
      └─ input_manager.create_stream()
         ├─ Получает устройство из DeviceStateCache
         ├─ Создает поток
         └─ Начинает запись

2. Каждый чанк обрабатывается:
   └─ input_manager._process_audio_chunk(chunk)
      ├─ AudioUtils.calculate_rms(chunk) → rms = 0.15
      ├─ Обновление статистики
      └─ Логирование (если log_health_checks: true)

3. Пользователь перестает говорить
   └─ RMS падает ниже silence_threshold (0.01)

4. Обнаружение тишины:
   └─ input_manager._detect_silence()
      ├─ Счетчик тихих окон увеличивается
      ├─ После 2 подряд тихих окон (silent_windows_threshold):
      └─ Публикует audio.silence.detected
         └─ VoiceRecognitionIntegration завершает запись
            └─ voice.recording_stop
```

---

## 6. ГАРАНТИИ ЦЕНТРАЛИЗАЦИИ

### 6.1 Проверки на этапе разработки

**1. Проверка дублирования кода:**
```bash
# Скрипт проверяет дублирование функций
python scripts/check_code_duplication.py

# Должен найти дублирование:
# - is_bluetooth_device() в 5 местах → ОШИБКА
# - Все функции должны быть только в device_utils.py
```

**2. Проверка прямых вызовов:**
```bash
# Скрипт проверяет прямые вызовы системных API
python scripts/verify_no_direct_state_access.py

# Должен найти прямые вызовы:
# - subprocess.run.*SwitchAudioSource в других модулях → ОШИБКА
# - sd.query_devices() в других модулях → ОШИБКА
# - sd.InputStream() / sd.OutputStream() в других модулях → ОШИБКА
```

**3. Проверка локальных переменных состояния:**
```bash
# Grep по паттернам локальных переменных
grep -r "_current_device\|_device_name\|_device_id" modules/ --exclude="device_state_cache.py"

# Должен найти локальные переменные:
# - _current_device в SpeechRecognizer → ОШИБКА
# - Все состояния должны быть в DeviceStateCache
```

### 6.2 Проверки на этапе выполнения

**1. Логирование источников:**
- Все операции с устройствами логируют источник: `[DEVICE_MANAGER]`, `[DEVICE_MONITOR]`
- Проверка логов на наличие прямых вызовов системных API из других модулей

**2. Метрики:**
- Количество вызовов SwitchAudioSource (должно быть только из DeviceManager)
- Количество вызовов sd.query_devices() (должно быть только из DeviceManager)
- Количество событий смены устройств (не должно быть дублирования)

---

## 6. КОНФИГУРАЦИЯ

### 6.1 Bluetooth-специфичные параметры

Все задержки и параметры для Bluetooth устройств вынесены в `unified_config.yaml`:

```yaml
audio_system:
  bluetooth:
    # Задержка перед созданием потока для BT устройств (секунды)
    # Эмпирическое значение для стабилизации BT соединения
    # Тип: float, диапазон: 0.1-2.0, по умолчанию: 0.5
    # Влияние: Больше значение = стабильнее, но больше задержка
    bt_prestart_delay_sec: 0.5
    
    # Задержка после закрытия потока для BT устройств (секунды)
    # Эмпирическое значение для полного закрытия BT соединения
    # Тип: float, диапазон: 1.0-5.0, по умолчанию: 2.5
    # Влияние: Больше значение = надежнее закрытие, но больше задержка
    bt_close_delay_sec: 2.5
    
    # Количество попыток retry для BT устройств
    # Эмпирическое значение для нестабильных BT соединений
    # Тип: int, диапазон: 3-10, по умолчанию: 7
    # Влияние: Больше значение = больше попыток, но больше задержка
    bt_retry_attempts: 7
    
    # Базовая задержка между попытками для BT (секунды)
    # Эмпирическое значение для экспоненциального backoff
    # Тип: float, диапазон: 0.3-1.0, по умолчанию: 0.5
    # Влияние: Больше значение = больше задержка, но меньше нагрузка
    bt_retry_delay_sec: 0.5
    
    # Таймаут ожидания активного потока для BT (секунды)
    # Эмпирическое значение для проверки стабильности потока
    # Тип: float, диапазон: 2.0-5.0, по умолчанию: 3.0
    # Влияние: Больше значение = больше время ожидания, но надежнее
    bt_stream_timeout_sec: 3.0
```

**ВАЖНО:** Все значения эмпирические и настраиваемые без правки кода.

### 6.2 Режим работы с устройствами

Система поддерживает два режима работы:

```yaml
audio_system:
  device_policy:
    # Следовать системному default устройству
    # true: автоматически переключается при смене системного default
    # false: использует прибитое устройство (pinned device)
    # Тип: bool, по умолчанию: true
    follow_system_default: true
    
    # Прибитое INPUT устройство (UID)
    # null: использовать системный default
    # "UID-STRING": всегда использовать это устройство
    # Тип: Optional[str], по умолчанию: null
    pinned_input_device_uid: null
    
    # Прибитое OUTPUT устройство (UID)
    # null: использовать системный default
    # "UID-STRING": всегда использовать это устройство
    # Тип: Optional[str], по умолчанию: null
    pinned_output_device_uid: null
    
    # Автоматически переключаться на новое устройство
    # true: при обнаружении нового устройства автоматически переключаться
    # false: только логировать, не переключаться
    # Тип: bool, по умолчанию: true
    auto_switch_on_new_device: true
```

**Приоритет устройства:**
1. `pinned_device_uid` (если задан и доступен)
2. `system_default` (если `follow_system_default: true`)
3. `fallback_device` (последнее рабочее устройство)

### 6.3 Метрики производительности

Все метрики логируются в структурированном формате:

```python
# Формат метрики
{
    "type": "metric",
    "name": "device_detection_latency_ms",
    "value": 250,
    "unit": "ms",
    "timestamp": "2024-01-15T10:30:45.123Z",
    "session_id": "abc123",
    "device": {
        "uid": "AirPods-UID",
        "name": "Sergiy's AirPods",
        "is_bluetooth": True
    }
}
```

**Обязательные метрики:**
- `device_detection_latency_ms` - время обнаружения устройства (цель: < 500ms)
- `device_switch_latency_ms` - время переключения устройства (цель: < 200ms для обычных, < 1000ms для BT)
- `portaudio_error_rate` - процент ошибок PortAudio (цель: < 1%)
- `stream_creation_success_rate` - процент успешных созданий потоков (цель: ≥ 98%)
- `device_switch_success_rate` - процент успешных переключений (цель: ≥ 95%)

---

## 7. ГАРАНТИИ ПОСТОЯННОГО МОНИТОРИНГА И МГНОВЕННОГО ПЕРЕКЛЮЧЕНИЯ

### 7.1 Постоянный мониторинг

**Гарантии:**
- ✅ Мониторинг работает **непрерывно** с момента старта приложения до его завершения
- ✅ Core Audio нотификации работают в фоновом режиме и не останавливаются
- ✅ Polling fallback работает в отдельном потоке (daemon thread) и не останавливается
- ✅ Оба механизма работают **параллельно** для максимальной надежности
- ✅ Мониторинг не зависит от состояния приложения (работает даже в режиме SLEEPING)

**Проверка:**
- Логи показывают непрерывную работу мониторинга
- Тесты проверяют обнаружение устройств через длительное время работы (30+ минут)
- Проверка, что мониторинг не останавливается после инициализации

### 7.2 Обнаружение новых устройств

**Гарантии:**
- ✅ Система обнаруживает **не только смену** default устройства, но и **подключение новых устройств**
- ✅ Новые устройства обнаруживаются сразу после подключения (< 500ms)
- ✅ Система определяет, что устройство новое (сравнение с кэшем)
- ✅ События содержат флаг `is_new_device: true` для новых устройств

**Проверка:**
- Тесты: подключение нового устройства → обнаружение → переключение
- Логи показывают обнаружение новых устройств с флагом `is_new_device: true`
- Проверка времени от подключения до обнаружения (< 500ms)

### 7.3 Мгновенное автоматическое переключение

**Гарантии:**
- ✅ Переключение происходит **автоматически** при обнаружении нового default устройства
- ✅ Переключение **не требует действий пользователя**
- ✅ Переключение происходит **мгновенно** (< 200ms для INPUT, < 100ms для OUTPUT)
- ✅ Переключение **не прерывает** активные операции (запись/воспроизведение продолжаются)
- ✅ Переключение происходит **прозрачно** для пользователя (без задержек и ошибок)

**Проверка:**
- Тесты: обнаружение нового устройства → автоматическое переключение без пользовательских действий
- Логи показывают автоматическое переключение
- Проверка, что активные операции не прерываются при переключении
- Проверка времени переключения (< 200ms для INPUT, < 100ms для OUTPUT)

### 7.4 Метрики производительности

**Целевые метрики:**
- Время обнаружения нового устройства: < 500ms (p95)
- Время переключения INPUT: < 200ms (p95)
- Время переключения OUTPUT: < 100ms (p95)
- Процент успешных автоматических переключений: > 99%
- Непрерывность мониторинга: 100% (работает постоянно)

**Мониторинг:**
- Логирование времени обнаружения и переключения
- Метрики: `device_detection_time_ms`, `device_switch_time_ms`
- Алерты при превышении целевых метрик

---

## 8. ЗАКЛЮЧЕНИЕ

Новая аудиосистема работает по принципам:

1. **Единый источник истины:** Все операции с устройствами через DeviceManager и DeviceStateCache
2. **Событийная архитектура:** Все взаимодействия через EventBus
3. **Централизация:** Все утилиты в одном месте, нет дублирования
4. **Постоянный мониторинг:** Непрерывное отслеживание подключения новых устройств
5. **Мгновенная адаптация:** Обнаружение смены устройств за < 500ms, переключение за < 200ms
6. **Автоматическое переключение:** Мгновенное переключение на новые устройства без действий пользователя
7. **Надежность:** Автоматическое восстановление после ошибок
8. **Прозрачность:** Все операции логируются и отслеживаются

Эта архитектура обеспечивает:
- **Постоянный мониторинг** подключения новых устройств
- **Мгновенное автоматическое переключение** на новые устройства
- Отсутствие дублирования кода
- Отсутствие конфликтов при работе с устройствами
- Правильную интеграцию с существующими модулями
- Простоту поддержки и развития
