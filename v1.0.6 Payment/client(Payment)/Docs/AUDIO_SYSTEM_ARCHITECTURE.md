# Архитектура аудиосистемы Nexy

## Дата создания
2025-12-02

## Последнее обновление
2025-12-02 - **КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ**: Исправлена передача callback в StreamConfig при создании PortAudio потоков. Без callback PortAudio не вызывал _audio_callback для записи данных, что приводило к отсутствию воспроизведения.

## Обзор

Аудиосистема Nexy состоит из двух независимых подсистем:
- **INPUT** - захват и распознавание речи с микрофона
- **OUTPUT** - воспроизведение аудио ответов через динамики/наушники

Обе подсистемы взаимодействуют через **EventBus** - событийную шину, которая обеспечивает слабую связанность компонентов.

---

## 1. Архитектурные принципы

### 1.1 Событийная архитектура (EventBus)

Все взаимодействие между компонентами происходит через **EventBus**:
- Компоненты **публикуют** события (`event_bus.publish()`)
- Компоненты **подписываются** на события (`event_bus.subscribe()`)
- События имеют **приоритеты** (CRITICAL, HIGH, MEDIUM, LOW)
- Обработка событий **асинхронная** (async/await)

### 1.2 Разделение ответственности

- **Модули** (`modules/`) - низкоуровневая логика (работа с PortAudio, Core Audio)
- **Интеграции** (`integration/integrations/`) - адаптеры между модулями и EventBus
- **Workflows** (`integration/workflows/`) - координаторы сложных цепочек действий
- **Core** (`integration/core/`) - инфраструктура (EventBus, StateManager, ErrorHandler)

### 1.3 Единый источник истины

- **ApplicationStateManager** - единый источник истины для состояния приложения
- **session_id** - всегда берется из `state_manager.get_current_session_id()`
- **AppMode** - управляется через `state_manager.set_mode()`

---

## 2. INPUT подсистема (Захват и распознавание речи)

### 2.1 Компоненты

#### 2.1.1 InputProcessingIntegration
**Файл:** `integration/integrations/input_processing_integration.py`

**Ответственность:**
- Обработка событий клавиатуры (PRESS, LONG_PRESS, RELEASE, SHORT_PRESS)
- Управление состоянием комбинации (InputState: IDLE, PENDING, LISTENING, PROCESSING)
- Публикация событий `voice.recording_start` и `voice.recording_stop`
- Координация перехода в режим LISTENING → PROCESSING

**События:**
- **Публикует:**
  - `keyboard.press` - нажатие клавиши
  - `keyboard.short_press_cancelled` - короткое нажатие отменено
  - `voice.recording_start{session_id}` - начало записи (при LONG_PRESS)
  - `voice.recording_stop{session_id}` - конец записи (при RELEASE)
  - `mode.request{target=LISTENING|PROCESSING}` - запрос смены режима

- **Подписывается:**
  - `keyboard.press/release/short_press/long_press` - события клавиатуры
  - `voice.recognition_completed/failed` - результаты распознавания
  - `playback.completed` - завершение воспроизведения
  - `grpc.request_completed` - завершение gRPC запроса

#### 2.1.2 VoiceRecognitionIntegration
**Файл:** `integration/integrations/voice_recognition_integration.py`

**Ответственность:**
- Координация распознавания речи
- Управление микрофоном через `MicrophoneStateManager`
- Публикация результатов распознавания
- Работа с `SpeechRecognizer` для низкоуровневой работы с микрофоном
- ✅ **ЦИКЛ 1**: Обработка смены INPUT устройств через `device.default_input_changed`

**События:**
- **Публикует:**
  - `voice.recognition_started{session_id}` - начало распознавания
  - `voice.recognition_completed{session_id, text, confidence}` - успешное распознавание
  - `voice.recognition_failed{session_id, error}` - ошибка распознавания
  - `voice.mic_opened{session_id}` - микрофон открыт
  - `voice.mic_closed{session_id}` - микрофон закрыт

- **Подписывается:**
  - `voice.recording_start` - начало записи
  - `voice.recording_stop` - конец записи
  - `microphone.open_requested` - запрос открытия микрофона
  - `microphone.close_requested` - запрос закрытия микрофона
  - ✅ **ЦИКЛ 1**: `device.default_input_changed` - смена INPUT устройства (от DeviceChangePublisher)

#### 2.1.3 SpeechRecognizer
**Файл:** `modules/voice_recognition/core/speech_recognizer.py`

**Ответственность:**
- Низкоуровневая работа с PortAudio для захвата аудио
- Создание и управление PortAudio стримами через `AudioStreamManager`
- Обработка аудио чанков через `_audio_callback`
- VAD (Voice Activity Detection) и нормализация аудио

**Особенности:**
- ✅ **ЦИКЛ 2**: Использует `AudioStreamManager` для управления потоками (гарантированное закрытие, retry логика)
- ✅ **ЦИКЛ 3**: Подписан на `device.default_input_changed` от `DeviceChangePublisher` (событийная реакция)
- ✅ **РЕФАКТОРИНГ**: Все пути создания потоков проходят через `AudioStreamManager`:
  - `_run_listening()` → `AudioStreamManager.create_stream()`
  - `on_device_changed()` → `AudioStreamManager.switch_device()` (если state != LISTENING)
  - `_recreate_stream_with_config()` → `AudioStreamManager.switch_device()`
  - `_switch_device()` → `AudioStreamManager.switch_device()`
- Использует **SwitchAudioSource** как helper для чтения системного default input устройства (источник истины - CoreAudio через DeviceChangePublisher)
- Специальная обработка BT устройств (увеличенные задержки, retry логика)
- ✅ Старый polling (`AudioDeviceMonitor`) удален - использует централизованный мониторинг

#### 2.1.4 MicrophoneStateManager
**Файл:** `modules/microphone_state/core/microphone_state_manager.py`

**Ответственность:**
- Управление состоянием микрофона (IDLE, OPENING, OPEN, CLOSING)
- Координация открытия/закрытия микрофона
- Публикация событий `microphone.opened/closed/error`

**Состояния:**
- `IDLE` - микрофон закрыт
- `OPENING` - процесс открытия микрофона
- `OPEN` - микрофон открыт и готов к записи
- `CLOSING` - процесс закрытия микрофона

### 2.2 Поток INPUT (от нажатия клавиши до распознавания)

```
1. Пользователь нажимает Ctrl+N (PRESS)
   └─ InputProcessingIntegration._handle_press()
      ├─ Создает pending_session_id = timestamp
      ├─ Переход: IDLE → PENDING
      └─ Публикует: keyboard.press

2. Пользователь удерживает Ctrl+N > 0.6s (LONG_PRESS)
   └─ InputProcessingIntegration._handle_long_press()
      ├─ Проверки (5 защит):
      │   ├─ _long_press_in_progress? → игнорируем
      │   ├─ _input_state == PENDING? → проверяем
      │   ├─ keyboard_monitor.key_pressed? → проверяем
      │   ├─ state_manager.is_microphone_active()? → игнорируем если True
      │   └─ _recording_started? → игнорируем если True
      │
      ├─ Ожидания:
      │   ├─ _ensure_playback_idle() (таймаут 0.5s)
      │   └─ _wait_for_mic_closed() (таймаут 0.3s)
      │
      ├─ Сброс состояния:
      │   ├─ _reset_session("long_press_start")
      │   ├─ _set_session_id(new_session_id, "long_press_start")
      │   └─ _pending_session_id = None
      │
      └─ Публикует: voice.recording_start{session_id}
         └─ Переход: PENDING → LISTENING

3. VoiceRecognitionIntegration получает voice.recording_start
   └─ VoiceRecognitionIntegration._on_recording_start()
      ├─ MicrophoneStateManager.request_open(session_id)
      │   ├─ Переход: IDLE → OPENING
      │   ├─ Публикует: microphone.open_requested
      │   └─ Ждет: microphone.opened (таймаут 5s)
      │
      └─ SpeechRecognizer.start_listening()
         ├─ ✅ ЦИКЛ 2: Использует AudioStreamManager.create_stream()
         ├─ ✅ ЦИКЛ 1: Устройство определяется через DeviceChangePublisher (событийная реакция)
         ├─ Публикует: microphone.opened
         └─ Публикует: voice.mic_opened

4. SpeechRecognizer._audio_callback получает аудио чанки
   ├─ Получает аудио данные из PortAudio
   ├─ Обрабатывает (нормализация, VAD)
   └─ Сохраняет в буфер для распознавания

5. Пользователь отпускает Ctrl+N (RELEASE)
   └─ InputProcessingIntegration._handle_key_release()
      ├─ Публикует: voice.recording_stop{session_id}
      └─ _wait_for_mic_closed() (таймаут 1.0s)

6. VoiceRecognitionIntegration получает voice.recording_stop
   └─ VoiceRecognitionIntegration._on_recording_stop()
      ├─ SpeechRecognizer.stop_listening()
      │   ├─ Останавливает поток через AudioStreamManager
      │   └─ Публикует: microphone.closed
      │
      └─ Запускает распознавание (симуляция или реальное)
         └─ Публикует: voice.recognition_completed{session_id, text, confidence}
            └─ Переход: LISTENING → PROCESSING
```

### 2.3 ListeningWorkflow

**Файл:** `integration/workflows/listening_workflow.py`

**Ответственность:**
- Координация режима LISTENING
- Дебаунс защита от случайных нажатий
- Умные таймауты (адаптивные)
- Мониторинг качества записи

**События:**
- **Подписывается:**
  - `voice.recording_start` - начало записи
  - `voice.recording_stop` - конец записи
  - `keyboard.short_press` - прерывание
  - `interrupt.request` - запрос прерывания
  - `app.mode_changed` - смена режима

**Особенности:**
- Проверяет минимальную длительность записи (debounce_threshold = 0.3s)
- Отслеживает максимальную длительность (max_listening_duration = 30.0s)
- Координирует возврат в SLEEPING при прерывании

---

## 3. OUTPUT подсистема (Воспроизведение аудио)

### 3.1 Компоненты

#### 3.1.1 SpeechPlaybackIntegration
**Файл:** `integration/integrations/speech_playback_integration.py`

**Ответственность:**
- Координация воспроизведения аудио ответов
- Обработка аудио чанков от gRPC сервера
- Управление `SequentialSpeechPlayer`
- Финализация воспроизведения по тишине
- ✅ **ЦИКЛ 1**: Обработка смены OUTPUT устройств через `device.default_output_changed`

**События:**
- **Публикует:**
  - `playback.started{session_id}` - начало воспроизведения
  - `playback.completed{session_id}` - завершение воспроизведения
  - `playback.failed{session_id, error}` - ошибка воспроизведения

- **Подписывается:**
  - `grpc.response.audio` - аудио чанки от сервера
  - `grpc.request_completed` - завершение gRPC запроса
  - `grpc.request_failed` - ошибка gRPC запроса
  - `playback.raw_audio` - сырые аудио данные
  - `playback.signal` - короткие сигналы (тоны)
  - `grpc.request_cancel` - отмена gRPC запроса
  - ✅ **ЦИКЛ 1**: `device.default_output_changed` - смена OUTPUT устройства (от DeviceChangePublisher)

#### 3.1.2 SequentialSpeechPlayer
**Файл:** `modules/speech_playback/core/player.py`

**Ответственность:**
- Низкоуровневая работа с PortAudio для воспроизведения
- Создание и управление PortAudio стримами через `AudioStreamManager`
- Обработка аудио чанков через `_audio_callback`
- Управление буфером воспроизведения (`ChunkBuffer`)
- ✅ **ЦИКЛ 1**: Автоматическое переключение устройств через `device.default_output_changed`

**Особенности:**
- ✅ **ЦИКЛ 2**: Использует `AudioStreamManager` для управления потоками (гарантированное закрытие, retry логика)
- ✅ **ЦИКЛ 3**: Подписан на `device.default_output_changed` от `DeviceChangePublisher` (событийная реакция)
- ✅ **РЕФАКТОРИНГ**: Все пути создания потоков проходят через `AudioStreamManager`:
  - `_start_audio_stream()` → `AudioStreamManager.create_stream()`
  - `_switch_output_device()` → `AudioStreamManager.switch_device()` (hot-plug, ручное переключение)
  - `_stop_audio_stream()` → `AudioStreamManager.close_stream()`
- ✅ **КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ (2025-12-02)**: Callback `_audio_callback` правильно передается в `StreamConfig` при создании потока:
  - `_get_stream_config()` возвращает dict с `callback=self._audio_callback`
  - `StreamConfig` создается с `callback=stream_config.get('callback')` (не `None`)
  - `AudioStreamManager` передает callback в `sd.OutputStream(callback=config.callback)`
  - PortAudio вызывает `_audio_callback` для записи данных из буфера в поток
- Использует **SwitchAudioSource** как helper для чтения системного default output устройства (источник истины - CoreAudio через DeviceChangePublisher)
- Специальная обработка BT устройств:
  - Использует `device=None` (macOS управляет параметрами)
  - Увеличенные задержки (2.5с для prestart и close_delay)
  - Не задает `blocksize` и `latency` (macOS выбирает сам)
- ✅ **ЦИКЛ 2**: Гарантированное закрытие старого потока через `AudioStreamManager`:
  - Цикл ожидания `active=False` (таймаут 3с для BT, 1с для обычных)
  - Задержка после `close()` (2.5с для BT, 0.3с для обычных)
- ✅ Старый polling (`_output_monitor_loop`) удален - использует централизованный мониторинг

#### 3.1.3 CoreAudioManager
**Файл:** `modules/speech_playback/macos/core_audio.py`

**Ответственность:**
- ✅ **ЦИКЛ 1**: Подписка на Core Audio нотификации о смене default INPUT и OUTPUT устройств
- Мгновенная реакция на смену устройства (без polling)
- Fallback на polling при недоступности Core Audio

**Особенности:**
- ✅ **ЦИКЛ 1**: Поддержка INPUT нотификаций (`kAudioHardwarePropertyDefaultInputDevice`)
- ✅ **ЦИКЛ 1**: Поддержка OUTPUT нотификаций (`kAudioHardwarePropertyDefaultOutputDevice`)
- ✅ **ЦИКЛ 3**: Упрощенный callback (передача функции напрямую, fallback на polling работает)
- Используется `DeviceChangePublisher` для подписки на нотификации
- При успешной подписке отключает polling мониторинг

### 3.2 Поток OUTPUT (от gRPC ответа до воспроизведения)

```
1. GrpcClientIntegration получает аудио чанк от сервера
   └─ GrpcClientIntegration._on_audio_chunk()
      └─ Публикует: grpc.response.audio{session_id, audio_data, dtype, sample_rate, channels}

2. SpeechPlaybackIntegration получает grpc.response.audio
   └─ SpeechPlaybackIntegration._on_audio_chunk()
      ├─ Декодирует audio_data из bytes
      ├─ Проверяет/инициализирует плеер
      ├─ ✅ ЦИКЛ 1: Смена устройства обрабатывается через device.default_output_changed (от DeviceChangePublisher)
      │   └─ SpeechPlaybackIntegration._on_output_device_changed()
      │      └─ SequentialSpeechPlayer._switch_output_device()
      │         └─ ✅ ЦИКЛ 2: AudioStreamManager.switch_device() (hot-plug, ручное переключение)
      │            ├─ Гарантированное закрытие старого потока
      │            ├─ Ожидание active=False (таймаут 3с для BT, 1с для обычных)
      │            ├─ Задержка после close() (2.5с для BT, 0.3с для обычных)
      │            ├─ Создание нового потока с retry логикой
      │            └─ Очистка буфера и обновление параметров
      │
      ├─ start_playback()  # Если не играет
      │   └─ _ensure_stream_started()
      │      ├─ ✅ ЦИКЛ 2: Использует AudioStreamManager.create_stream()
      │      ├─ ✅ РЕФАКТОРИНГ: Все пути создания потоков проходят через AudioStreamManager
      │      └─ ✅ РЕФАКТОРИНГ: switch_device() используется для hot-plug и recovery
      │      ├─ Для BT устройств: device=None, channels=1, без blocksize/latency
      │      └─ Запускает поток
      │
      └─ add_audio_data(audio_data, metadata)
         ├─ Добавляет в ChunkBuffer
         └─ Поток воспроизводит через _audio_callback()

3. SequentialSpeechPlayer._audio_callback получает запрос на воспроизведение
   ├─ Получает данные из ChunkBuffer
   ├─ Конвертирует каналы (моно → стерео при необходимости)
   └─ Записывает в outdata (PortAudio воспроизводит)

4. GrpcClientIntegration получает end_message от сервера
   └─ GrpcClientIntegration._on_end_message()
      └─ Публикует: grpc.request_completed{session_id}

5. SpeechPlaybackIntegration получает grpc.request_completed
   └─ SpeechPlaybackIntegration._on_grpc_completed()
      ├─ Устанавливает флаг _grpc_done_sessions[session_id] = True
      └─ Запускает _finalize_on_silence(session_id, timeout=3.0s)
         └─ После тишины публикует: playback.completed{session_id}
```

### 3.3 ProcessingWorkflow

**Файл:** `integration/workflows/processing_workflow.py`

**Ответственность:**
- Координация режима PROCESSING
- Управление цепочкой: capture → gRPC → playback → SLEEPING
- Ожидание реальных событий вместо таймаутов

**Этапы обработки:**
1. **CAPTURING** - захват скриншота
2. **SENDING_GRPC** - отправка на сервер
3. **PLAYING_AUDIO** - воспроизведение ответа
4. **COMPLETING** - завершение и возврат в SLEEPING

**События:**
- **Подписывается:**
  - `app.mode_changed` - вход в PROCESSING
  - `screenshot.captured/error` - результат захвата
  - `grpc.request_started/completed/failed` - статус gRPC
  - `playback.started/completed/failed` - статус воспроизведения
  - `keyboard.short_press/interrupt.request` - прерывания

- **Публикует:**
  - `mode.request{target=SLEEPING}` - возврат в SLEEPING
  - `grpc.request_cancel` - отмена gRPC при прерывании
  - `playback.stop` - остановка воспроизведения при прерывании

**Особенности:**
- Ждет **РЕАЛЬНЫХ событий** вместо таймаутов:
  - `screenshot.captured` → переход к gRPC
  - `grpc.request_completed` → ожидание завершения воспроизведения
  - `playback.completed` → возврат в SLEEPING
- Координирует прерывания через `playback.cancelled`

---

## 4. Взаимодействие INPUT и OUTPUT

### 4.1 Независимость подсистем

INPUT и OUTPUT работают **независимо** друг от друга:
- INPUT использует PortAudio стримы через `AudioStreamManager` для захвата аудио
- OUTPUT использует PortAudio стримы через `AudioStreamManager` для воспроизведения аудио
- Оба используют **общий AudioStreamManager** для управления PortAudio-потоками
- Оба используют **разные устройства** (input vs output)
- Оба имеют **собственные потоки** и буферы

### 4.2 Координация через EventBus

Взаимодействие происходит через **EventBus события**:

```
INPUT → OUTPUT координация:
1. INPUT завершает распознавание
   └─ voice.recognition_completed → InputProcessingIntegration
      └─ mode.request(PROCESSING) → ModeManagementIntegration
         └─ app.mode_changed(PROCESSING) → ProcessingWorkflow
            └─ Запускает цепочку: capture → gRPC → playback

2. OUTPUT начинает воспроизведение
   └─ playback.started → ProcessingWorkflow
      └─ Отслеживает этап PLAYING_AUDIO

3. OUTPUT завершает воспроизведение
   └─ playback.completed → ProcessingWorkflow
      └─ mode.request(SLEEPING) → ModeManagementIntegration
         └─ app.mode_changed(SLEEPING) → Все подписчики
```

### 4.3 Защита от конфликтов

**INPUT защита:**
- Проверка `state_manager.is_microphone_active()` перед началом записи
- Ожидание `_wait_for_mic_closed()` перед началом новой записи
- Проверка `_recording_started` для предотвращения дублирования

**OUTPUT защита:**
- Подписка на `device.default_output_changed` от DeviceChangePublisher
- Автоматическое переключение через `AudioStreamManager.switch_device()` при смене устройства
- Гарантированное закрытие старого потока перед созданием нового (через AudioStreamManager)
- Ожидание `active=False` перед пересозданием потока

### 4.4 Прерывания

**Единый канал прерывания:**
- `keyboard.short_press` / `interrupt.request` → `playback.cancelled`
- **`playback.cancelled`** - ЕДИНЫЙ канал прерывания аудио
- ProcessingWorkflow/ListeningWorkflow обрабатывают прерывания и координируют возврат в SLEEPING

---

## 5. Определение устройств (Device Detection)

### 5.1 Единый источник истины

**System Default (CoreAudio)** - источник истины для default устройств:
- CoreAudioManager отслеживает изменения default INPUT/OUTPUT устройств через системные нотификации
- DeviceChangePublisher подписывается на CoreAudio нотификации и публикует события в EventBus
- При недоступности CoreAudio используется polling fallback

**SwitchAudioSource** - основной helper для чтения/смены системного default в слое Python:
- Используется для получения имени текущего default устройства
- Используется для поиска device_id по имени через PortAudio
- Если SwitchAudioSource не вернул устройство → используется `device=None` (системный дефолт)

### 5.2 DeviceChangePublisher - Единый монитор устройств ✅ РЕАЛИЗОВАНО

**✅ ЦИКЛ 1 (2025-12-02):** Внедрен и работает единый компонент для мониторинга устройств.

**Компонент:** `modules/audio_core/device_change_publisher.py`

**Ответственность:**
- ✅ Единый мониторинг INPUT и OUTPUT устройств
- ✅ Подписка на Core Audio нотификации (приоритет 1)
- ✅ Fallback на polling при недоступности Core Audio
- ✅ Публикация событий в EventBus: `device.default_input_changed` / `device.default_output_changed`
- ✅ Debounce механизм (300ms) для rapid device switch
- ✅ Логирование источника (CoreAudio vs polling)

**Интеграция:** `integration/integrations/device_change_publisher_integration.py`
- ✅ Инициализируется в SimpleModuleCoordinator на позиции 9 (перед voice_recognition и speech_playback)
- ✅ Запускается при старте приложения
- ✅ Публикует события в EventBus для подписки INPUT/OUTPUT компонентов
- ✅ `VoiceRecognitionIntegration` и `SpeechPlaybackIntegration` подписаны на события

**События EventBus:**
- `device.default_input_changed{device_name, device_id, is_bluetooth, source, old_device_name, old_device_id}`
- `device.default_output_changed{device_name, device_id, is_bluetooth, source, old_device_name, old_device_id}`
- `device.monitoring_started{source, monitor_input, monitor_output}`
- `device.monitoring_stopped{}`

**Источники событий:**
- `DeviceChangeSource.CORE_AUDIO` - Core Audio нотификации (мгновенная реакция)
- `DeviceChangeSource.POLLING` - Polling fallback (интервал: 5.0s для BT, 1.0s для обычных)

### 5.3 CoreAudioManager - Улучшенная поддержка нотификаций ✅ РЕАЛИЗОВАНО

**✅ ЦИКЛ 1 (2025-12-02):** Добавлена поддержка INPUT нотификаций.

**Компонент:** `modules/speech_playback/macos/core_audio.py`

**Реализовано:**
- ✅ Поддержка INPUT нотификаций (`kAudioHardwarePropertyDefaultInputDevice`)
- ✅ Поддержка OUTPUT нотификаций (`kAudioHardwarePropertyDefaultOutputDevice`)
- ✅ Поддержка одновременных подписок на INPUT и OUTPUT
- ✅ Метод `start_device_notifications(callback, device_type="input"|"output")`
- ✅ Метод `stop_device_notifications(device_type=None)` - от всех или конкретный тип
- ✅ **ЦИКЛ 3**: Упрощенный callback (передача функции напрямую, fallback на polling работает)

**Использование:**
- ✅ DeviceChangePublisher использует CoreAudioManager для подписки на нотификации
- ✅ При успешной подписке отключается polling fallback
- ✅ При ошибке подписки автоматически используется polling

### 5.4 Автоматическое переключение устройств ✅ РЕАЛИЗОВАНО

**INPUT (SpeechRecognizer):**
- ✅ **ЦИКЛ 1**: `VoiceRecognitionIntegration` подписан на `device.default_input_changed` от DeviceChangePublisher
- ✅ **ЦИКЛ 1**: При смене устройства вызывается `SpeechRecognizer.on_device_changed()`
- ✅ **ЦИКЛ 2**: Пересоздание потока через `AudioStreamManager.switch_device()` только если запись НЕ идёт (state != LISTENING)
- ✅ **ЦИКЛ 3**: Старый polling (`AudioDeviceMonitor`) удален - используется централизованный мониторинг
- ✅ **РЕФАКТОРИНГ**: Метод `on_device_changed()` использует `AudioStreamManager.switch_device()` для атомарного переключения устройства

**OUTPUT (SequentialSpeechPlayer):**
- ✅ **ЦИКЛ 1**: `SpeechPlaybackIntegration` подписан на `device.default_output_changed` от DeviceChangePublisher
- ✅ **ЦИКЛ 1**: При смене устройства вызывается `SequentialSpeechPlayer._switch_output_device()`
- ✅ **ЦИКЛ 2**: Безопасное переключение через `AudioStreamManager.switch_device()` с гарантированным закрытием старого потока
- ✅ **ЦИКЛ 3**: Старый polling (`_output_monitor_loop`) удален - используется централизованный мониторинг
- ✅ **РЕФАКТОРИНГ**: Все пути создания потоков проходят через `AudioStreamManager`:
  - При создании потока (`_start_audio_stream`) → `AudioStreamManager.create_stream()`
  - При авто-переключении устройства (`_switch_output_device`) → `AudioStreamManager.switch_device()`
  - При остановке потока (`_stop_audio_stream`) → `AudioStreamManager.close_stream()`

### 5.5 Специальная обработка BT устройств

**INPUT:**
- Увеличенные задержки (bt_prestart_delay = 0.5s)
- Увеличенные retry (max_stream_start_retries = 7)
- Увеличенные таймауты (first_chunk_timeout_bt = 3.5s)

**OUTPUT:**
- Использует `device=None` (macOS управляет параметрами)
- Обязательно `channels=1` (из конфига)
- НЕ задает `blocksize` и `latency` (macOS выбирает сам)
- Увеличенные задержки:
  - `bt_prestart_delay = 2.5s` (перед созданием потока)
  - `close_delay = 2.5s` (после закрытия потока)
- Увеличенные таймауты ожидания `active=False` (3.0s для BT, 1.0s для обычных)

---

## 6. Диаграмма взаимодействия

```mermaid
graph TB
    subgraph "INPUT FLOW"
        K[KeyboardMonitor] -->|PRESS/LONG_PRESS| I[InputProcessingIntegration]
        I -->|voice.recording_start| V[VoiceRecognitionIntegration]
        V -->|request_open| M[MicrophoneStateManager]
        M -->|microphone.open_requested| V
        V -->|start_listening| S[SpeechRecognizer]
        S -->|on_device_changed| ASM[AudioStreamManager]
        S -->|create_stream| ASM
        S -->|switch_device| ASM
        ASM -->|PortAudio InputStream| STREAM1[Audio Stream]
        STREAM1 -->|_audio_callback| S
        S -->|voice.recognition_completed| I
        I -->|voice.recording_stop| V
        V -->|stop_listening| S
        S -->|microphone.closed| M
    end
    
    subgraph "OUTPUT FLOW"
        G[GrpcClientIntegration] -->|grpc.response.audio| P[SpeechPlaybackIntegration]
        P -->|add_audio_data| PL[SequentialSpeechPlayer]
        PL -->|_switch_output_device| ASM
        PL -->|create_stream| ASM
        PL -->|switch_device| ASM
        ASM -->|PortAudio OutputStream| STREAM2[Audio Stream]
        STREAM2 -->|_audio_callback| PL
        PL -->|ChunkBuffer| STREAM2
    end
    
    subgraph "COORDINATION"
        I -->|mode.request| MODE[ModeManagementIntegration]
        MODE -->|app.mode_changed| WF1[ListeningWorkflow]
        MODE -->|app.mode_changed| WF2[ProcessingWorkflow]
        WF2 -->|playback.completed| MODE
        MODE -->|app.mode_changed| ALL[All Subscribers]
    end
    
    subgraph "DEVICE MONITORING - ЦИКЛ 1 (РЕАЛИЗОВАНО)"
        DCP[DeviceChangePublisher] -->|Core Audio| CAM[CoreAudioManager]
        DCP -->|Polling Fallback| POLL[Polling Loop]
        CAM -->|INPUT notifications| DCP
        CAM -->|OUTPUT notifications| DCP
        DCP -->|device.default_input_changed| EB
        DCP -->|device.default_output_changed| EB
        EB -->|device.default_input_changed| VRI[VoiceRecognitionIntegration]
        EB -->|device.default_output_changed| SPI[SpeechPlaybackIntegration]
        VRI -->|on_device_changed| S
        SPI -->|switch_output_device| PL
    end
    
    subgraph "STREAM MANAGEMENT - ЦИКЛ 2 (РЕАЛИЗОВАНО + РЕФАКТОРИНГ)"
        ASM[AudioStreamManager] -->|create_stream| STREAM1[INPUT Stream]
        ASM -->|create_stream| STREAM2[OUTPUT Stream]
        ASM -->|close_stream| STREAM1
        ASM -->|close_stream| STREAM2
        ASM -->|switch_device| STREAM1[Hot-plug, Recovery]
        ASM -->|switch_device| STREAM2[Hot-plug, Recovery]
        S -->|on_device_changed| ASM
        PL -->|_switch_output_device| ASM
        S -->|_recreate_stream_with_config| ASM
        S -->|_switch_device| ASM
    end
    
    style K fill:#e1f5ff
    style I fill:#e1f5ff
    style V fill:#e1f5ff
    style S fill:#e1f5ff
    style G fill:#fff4e1
    style P fill:#fff4e1
    style PL fill:#fff4e1
    style MODE fill:#e1ffe1
    style WF1 fill:#e1ffe1
    style WF2 fill:#e1ffe1
    style DCP fill:#ffeb3b
    style CAM fill:#ffeb3b
    style POLL fill:#ffeb3b
    style EB fill:#ffeb3b
    style ASM fill:#4caf50
    style VRI fill:#e1f5ff
    style SPI fill:#fff4e1
```

---

## 7. Ключевые события EventBus

### 7.1 Режимы
- `mode.request{target, source, session_id, priority}` - запрос смены режима
- `app.mode_changed{mode, session_id}` - факт смены режима (источник истины)
- `app.state_changed{old_mode, new_mode}` - мост для совместимости

### 7.6 Устройства (ЦИКЛ 1 - НОВОЕ)
- `device.default_input_changed{device_name, device_id, is_bluetooth, source, old_device_name, old_device_id}` - смена INPUT устройства
- `device.default_output_changed{device_name, device_id, is_bluetooth, source, old_device_name, old_device_id}` - смена OUTPUT устройства
- `device.monitoring_started{source, monitor_input, monitor_output}` - мониторинг устройств запущен
- `device.monitoring_stopped{}` - мониторинг устройств остановлен

**Источники (`source`):**
- `"core_audio"` - Core Audio нотификации (мгновенная реакция)
- `"polling"` - Polling fallback (интервал: 5.0s для BT, 1.0s для обычных)

### 7.2 Голос (INPUT)
- `keyboard.press/release/short_press/long_press` - события клавиатуры
- `voice.recording_start{session_id}` - начало записи
- `voice.recording_stop{session_id}` - конец записи
- `voice.recognition_started{session_id}` - начало распознавания
- `voice.recognition_completed{session_id, text, confidence}` - успешное распознавание
- `voice.recognition_failed{session_id, error}` - ошибка распознавания
- `voice.mic_opened{session_id}` - микрофон открыт
- `voice.mic_closed{session_id}` - микрофон закрыт
- `microphone.open_requested{session_id}` - запрос открытия микрофона
- `microphone.close_requested{session_id}` - запрос закрытия микрофона
- `microphone.opened{session_id}` - микрофон открыт (от MicrophoneStateManager)
- `microphone.closed{session_id}` - микрофон закрыт (от MicrophoneStateManager)

### 7.3 Воспроизведение (OUTPUT)
- `grpc.response.audio{session_id, audio_data, dtype, sample_rate, channels}` - аудио чанк от сервера
- `grpc.request_started{session_id}` - начало gRPC запроса
- `grpc.request_completed{session_id}` - завершение gRPC запроса
- `grpc.request_failed{session_id, error}` - ошибка gRPC запроса
- `grpc.request_cancel{session_id}` - отмена gRPC запроса
- `playback.started{session_id}` - начало воспроизведения
- `playback.completed{session_id}` - завершение воспроизведения
- `playback.failed{session_id, error}` - ошибка воспроизведения
- `playback.cancelled{session_id}` - отмена воспроизведения (ЕДИНЫЙ канал прерывания)
- `playback.raw_audio{session_id, audio_data}` - сырые аудио данные
- `playback.signal{pcm, sample_rate, channels, gain, priority, pattern}` - короткие сигналы (тоны)

### 7.4 Скриншоты
- `screenshot.captured{session_id, image_path}` - скриншот захвачен
- `screenshot.error{session_id, error}` - ошибка захвата скриншота

### 7.5 Прерывания
- `keyboard.short_press` - короткое нажатие (прерывание)
- `interrupt.request{reason}` - запрос прерывания

---

## 8. Конфигурация

### 8.1 Централизованная конфигурация

Все параметры аудио системы находятся в `config/unified_config.yaml`:

```yaml
voice:
  sample_rate: 48000
  channels: 1
  dtype: int16
  buffer_size: 512
  timeout_sec: 10.0
  start_retry_delay_ms: 300

speech_playback:
  sample_rate: 48000
  channels: 2
  dtype: int16
  buffer_size: 512
  max_memory_mb: 50
  auto_device_selection: true
  auto_output_device_switch: true
```

### 8.2 Задержки и таймауты

**INPUT:**
- `bt_prestart_delay = 0.5s` - задержка перед start() для BT устройств
- `max_stream_start_retries = 7` - максимум попыток запуска потока
- `first_chunk_timeout_bt = 3.5s` - таймаут первого чанка для BT устройств

**OUTPUT:**
- `bt_prestart_delay = 2.5s` - задержка перед созданием потока для BT устройств
- `close_delay = 2.5s` (BT) / `0.3s` (обычные) - задержка после close()
- `max_wait_time = 3.0s` (BT) / `1.0s` (обычные) - таймаут ожидания active=False

---

## 9. Обработка ошибок

### 9.1 Типы ошибок

**INPUT:**
- `E_DEP_TIMEOUT` - таймаут открытия микрофона
- `E_DEP_UNAVAILABLE` - микрофон недоступен
- `E_INPUT_INVALID` - невалидные входные данные

**OUTPUT:**
- `PaErrorCode -9986` - Internal PortAudio error (устройство занято)
- `PaErrorCode -10851` - Audio Unit: Invalid Property Value (конфигурационная ошибка)
- `E_DEP_TIMEOUT` - таймаут создания потока

### 9.2 Стратегии восстановления

**INPUT:**
- Retry логика с экспоненциальным backoff
- Fallback на системный дефолт при ошибках
- Публикация `voice.recognition_failed` при критических ошибках

**OUTPUT:**
- Retry логика с увеличением задержек для BT устройств
- При ошибке -9986/-10851: принудительное закрытие старого потока, задержка, повторная попытка
- Кэширование безопасных конфигураций для устройств
- Fallback на `device=None` для BT устройств

---

## 10. Реализованные циклы улучшения (2025-12-02)

### 10.1 Цикл 1: DeviceChangePublisher ✅ ЗАВЕРШЕН

**DeviceChangePublisher** - единый монитор устройств:
- ✅ Создан компонент `modules/audio_core/device_change_publisher.py`
- ✅ Создана интеграция `integration/integrations/device_change_publisher_integration.py`
- ✅ Интегрирован в SimpleModuleCoordinator (позиция 9, перед voice_recognition и speech_playback)
- ✅ Улучшен CoreAudioManager для поддержки INPUT и OUTPUT нотификаций
- ✅ `VoiceRecognitionIntegration` подписан на `device.default_input_changed`
- ✅ `SpeechPlaybackIntegration` подписан на `device.default_output_changed`
- ✅ Старый polling удален из `SpeechRecognizer` и `SequentialSpeechPlayer`

**Архитектура:**
```
DeviceChangePublisher
├── CoreAudioManager (приоритет 1)
│   ├── INPUT нотификации → _on_input_device_changed_core_audio()
│   └── OUTPUT нотификации → _on_output_device_changed_core_audio()
├── Polling fallback (если Core Audio недоступен)
│   └── _polling_loop() → проверка каждые 1-5 секунд
└── Debounce механизм
    └── _handle_device_change() → задержка 300ms перед публикацией
```

### 10.2 Цикл 2: AudioStreamManager ✅ ЗАВЕРШЕН + РЕФАКТОРИНГ (2025-12-02)

**AudioStreamManager** - единый API для управления PortAudio streams:
- ✅ Создан компонент `modules/audio_core/stream_manager.py`
- ✅ Рефакторинг `SpeechRecognizer` для использования `AudioStreamManager`
- ✅ Рефакторинг `SequentialSpeechPlayer` для использования `AudioStreamManager`
- ✅ Гарантированное закрытие старого потока перед созданием нового
- ✅ Retry логика с экспоненциальным backoff
- ✅ Обработка ошибок -9986/-10851
- ✅ Кэширование безопасных конфигураций
- ✅ **РЕФАКТОРИНГ (2025-12-02)**: Все пути создания потоков проходят через `AudioStreamManager`:
  - `SpeechRecognizer`: `_run_listening()`, `on_device_changed()`, `_recreate_stream_with_config()`, `_switch_device()`
  - `SequentialSpeechPlayer`: `_start_audio_stream()`, `_switch_output_device()`, `_stop_audio_stream()`
- ✅ **РЕФАКТОРИНГ**: `switch_device()` используется для hot-plug и ручного переключения устройств

**Архитектура:**
```
AudioStreamManager
├── create_stream() → создание потока с retry
├── close_stream() → гарантированное закрытие
├── switch_device() → атомарное переключение (hot-plug, ручное переключение, recovery)
└── Кэш безопасных конфигураций
```

**Использование в SpeechRecognizer:**
- `_run_listening()` → `AudioStreamManager.create_stream()`
- `on_device_changed()` → `AudioStreamManager.switch_device()` (если state != LISTENING)
- `_recreate_stream_with_config()` → `AudioStreamManager.switch_device()`
- `_switch_device()` → `AudioStreamManager.switch_device()`

**Использование в SequentialSpeechPlayer:**
- `_start_audio_stream()` → `AudioStreamManager.create_stream()`
- `_switch_output_device()` → `AudioStreamManager.switch_device()`
- `_stop_audio_stream()` → `AudioStreamManager.close_stream()`

### 10.3 Цикл 3: Единый монитор + избавление от polling ✅ ЗАВЕРШЕН

**Очистка кода:**
- ✅ Удален импорт `AudioDeviceMonitor` из `SpeechRecognizer`
- ✅ Удален метод `_output_monitor_loop` из `SequentialSpeechPlayer`
- ✅ Упрощены заглушки `_start_output_monitoring` и `_stop_output_monitoring`
- ✅ Исправлен PyObjC callback (упрощен, fallback работает)
- ✅ Polling полностью централизован в `DeviceChangePublisher`

### 10.4 Цикл 4: Observability + документация ✅ ЗАВЕРШЕН

**Документация:**
- ✅ Создана `Docs/AUDIO_DEVICE_CHANGE_PUBLISHER.md`
- ✅ Создана `Docs/AUDIO_STREAM_MANAGER.md`
- ✅ Создана `Docs/AUDIO_INVARIANTS.md`
- ✅ Обновлена `Docs/AUDIO_SYSTEM_ARCHITECTURE.md`
- ✅ Логирование уже достаточно подробное (INFO, DEBUG, WARNING, ERROR)

### 10.3 Порядок инициализации (обновлен)

**SimpleModuleCoordinator startup_order:**
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions
5. permission_restart
6. mode_management
7. input
8. network
9. **device_change_publisher** ← НОВОЕ (ЦИКЛ 1)
10. voice_recognition (подписывается на device.default_input_changed)
11. interrupt
12. screenshot_capture
13. grpc
14. action_execution
15. speech_playback (подписывается на device.default_output_changed)
16. signals
17. update_notification
18. updater
19. welcome_message
20. voiceover_ducking
21. autostart_manager

---

## 11. Заключение

Аудиосистема Nexy построена на принципах:
- **Событийная архитектура** - все через EventBus
- **Независимость подсистем** - INPUT и OUTPUT работают независимо
- **Единый источник истины** - System Default (CoreAudio) для устройств, SwitchAudioSource как helper, ApplicationStateManager для состояния
- **Единый монитор устройств** - DeviceChangePublisher для централизованного мониторинга (ЦИКЛ 1)
- **Защита от конфликтов** - проверки и ожидания перед критическими операциями
- **Специальная обработка BT** - увеличенные задержки и таймауты
- **Graceful обработка ошибок** - retry логика и fallback стратегии

**Текущее состояние (2025-12-02):**
- ✅ **Цикл 1 завершен**: DeviceChangePublisher создан, интегрирован, INPUT/OUTPUT подписаны на события
- ✅ **Цикл 2 завершен**: AudioStreamManager создан, используется в SpeechRecognizer и SequentialSpeechPlayer
- ✅ **Цикл 3 завершен**: Старый polling удален, мониторинг централизован в DeviceChangePublisher
- ✅ **Цикл 4 завершен**: Документация создана, логирование улучшено
- ✅ **Рефакторинг завершен**: Все пути создания потоков проходят через `AudioStreamManager`, включая `switch_device()` для hot-plug
- ✅ **КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ (2025-12-02)**: Исправлена передача callback в StreamConfig - теперь `_audio_callback` правильно передается в PortAudio, что обеспечивает корректное воспроизведение аудио

**Тестирование (2025-12-02):**
- ✅ **AudioStreamManager**: 14/14 unit тестов пройдено
  - Сценарии смены устройств (CoreAudio vs polling)
  - Ошибки -9986/-10851 и recovery механизмы
  - Создание, закрытие и переключение потоков
- ✅ **SpeechRecognizer интеграция**: 3/3 теста пройдено
- ✅ **DeviceChangePublisher интеграция**: 6/6 тестов пройдено
- ✅ **SequentialSpeechPlayer интеграция**: 4/4 теста пройдено
- ✅ **ИТОГО**: 27/27 тестов пройдено (100%)
- ✅ **Линтер**: 0 ошибок

**Проверка использования AudioStreamManager:**
- ✅ **SpeechRecognizer**: Все пути создания потоков проходят через `AudioStreamManager`
  - При старте прослушивания → `create_stream()`
  - При авто-переключении устройства → `switch_device()`
  - При recovery → `switch_device()`
- ✅ **SequentialSpeechPlayer**: Все пути создания потоков проходят через `AudioStreamManager`
  - При создании потока → `create_stream()`
  - При авто-переключении устройства → `switch_device()`
  - При остановке потока → `close_stream()`

Эта архитектура обеспечивает надежную работу с различными аудио устройствами и устойчивость к ошибкам. Все запланированные циклы улучшения успешно завершены, рефакторинг завершен, документация соответствует реализации.

