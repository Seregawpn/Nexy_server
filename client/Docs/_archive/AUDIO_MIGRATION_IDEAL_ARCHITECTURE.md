# Идеальная архитектура аудио-системы (с учетом текущего проекта)

**Статус**: Идеальная архитектура для интеграции  
**Основан на**: Текущая архитектура проекта + MVP-12 прототипы + AUDIO_MIGRATION_MASTER_SPECIFICATION.md

---

## 🏗️ Идеальная архитектура: Полная схема

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ИДЕАЛЬНАЯ АРХИТЕКТУРА NEXY                           │
│                  (с учетом текущего проекта)                            │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                          1. CORE LAYER                                  │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ EventBus         │      │ StateManager      │      │ ErrorHandler     │
│                  │      │                   │      │                  │
│ • subscribe()    │      │ • get_state()     │      │ • handle_error() │
│ • publish()     │      │ • update_state()   │      │ • log_error()    │
└──────────────────┘      └──────────────────┘      └──────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ SimpleModuleCoordinator │
                    │                         │
                    │ • Инициализация         │
                    │ • Порядок интеграций    │
                    │ • Управление жизненным  │
                    │   циклом                │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼

┌─────────────────────────────────────────────────────────────────────────┐
│                     2. INTEGRATION LAYER                                │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ БЛОКИРУЮЩИЕ ИНТЕГРАЦИИ (инициализация до остальных)                    │
└─────────────────────────────────────────────────────────────────────────┘

1. InstanceManagerIntegration
   └─→ Управление единственным экземпляром приложения

2. HardwareIdIntegration
   └─→ Получение hardware ID

3. FirstRunPermissionsIntegration
   └─→ Запрос разрешений при первом запуске
   └─→ Публикует: permissions.first_run_started/completed/failed

4. PermissionRestartIntegration
   └─→ Автоматический перезапуск после критических разрешений
   └─→ Публикует: permission_restart.scheduled/executing/completed

┌─────────────────────────────────────────────────────────────────────────┐
│ АУДИО-МАРШРУТИЗАЦИЯ (новая интеграция)                                   │
└─────────────────────────────────────────────────────────────────────────┘

5. AudioRouteManagerIntegration ← НОВОЕ
   │
   ├─→ Модуль: modules/audio_route_manager/
   │   ├─→ DeviceDiscovery (AVFoundation)
   │   ├─→ DeviceMapping (PortAudio)
   │   ├─→ RouteManager (управление маршрутизацией)
   │   ├─→ ReconcileEngine (принятие решений)
   │   ├─→ InputStateMachine (FSM для input)
   │   ├─→ OutputStateMachine (FSM для output)
   │   └─→ Adapters:
   │       ├─→ AVFInputAdapter (sounddevice.InputStream)
   │       └─→ AVFOutputAdapter (AVAudioEngine)
   │
   ├─→ Подписки:
   │   ├─→ voice.recording_start → запуск input через reconcile
   │   ├─→ voice.recording_stop → остановка input
   │   ├─→ app.mode_changed → проверка необходимости переключения
   │   ├─→ permissions.first_run_* → блокировка активации
   │   └─→ permission_restart.* → блокировка активации
   │
   └─→ Публикации:
       ├─→ audio.input.active → input готов
       ├─→ audio.output.ready → output готов
       ├─→ audio.device.changed → уведомление о смене устройства
       └─→ audio.route.snapshot → диагностика

┌─────────────────────────────────────────────────────────────────────────┐
│ ОСНОВНЫЕ ИНТЕГРАЦИИ (зависят от AudioRouteManager)                     │
└─────────────────────────────────────────────────────────────────────────┘

6. TrayControllerIntegration
   └─→ Управление tray icon

7. ModeManagementIntegration
   └─→ Управление режимами (SLEEPING/LISTENING/PROCESSING)
   └─→ Публикует: app.mode_changed

8. InputProcessingIntegration
   └─→ Мониторинг клавиатуры (KeyboardMonitor)
   └─→ Публикует: voice.recording_start/stop, keyboard.*

9. VoiceRecognitionIntegration ← АДАПТИРОВАННАЯ
   │
   ├─→ Подписки:
   │   ├─→ voice.recording_start (от InputProcessingIntegration)
   │   ├─→ audio.input.active (от AudioRouteManagerIntegration) ← НОВОЕ
   │   └─→ permissions.first_run_* (блокировка)
   │
   ├─→ Логика (feature flag):
   │   ├─→ Если audio_route_manager.enabled = true:
   │   │   └─→ Получает аудио-данные из AudioRouteManager
   │   │       (НЕ управляет микрофоном напрямую)
   │   └─→ Если audio_route_manager.enabled = false:
   │       └─→ Старая логика (SpeechRecognizer с sr.Microphone)
   │
   └─→ Публикации (сохраняются):
       ├─→ voice.mic_opened/closed
       └─→ voice.recognition_*

10. NetworkManagerIntegration
    └─→ Мониторинг сети
    └─→ Публикует: network.online/offline

11. InterruptManagementIntegration
    └─→ Управление прерываниями
    └─→ Подписывается: keyboard.short_press, interrupt.request

12. ScreenshotCaptureIntegration
    └─→ Захват скриншотов
    └─→ Публикует: screenshot.captured/error

13. GrpcClientIntegration
    └─→ gRPC клиент
    └─→ Публикует: grpc.response.audio, grpc.request_completed/failed

14. SpeechPlaybackIntegration ← АДАПТИРОВАННАЯ
    │
    ├─→ Подписки:
    │   ├─→ grpc.response.audio (от GrpcClientIntegration)
    │   ├─→ audio.output.ready (от AudioRouteManagerIntegration) ← НОВОЕ
    │   └─→ playback.cancelled (от InterruptManagementIntegration)
    │
    ├─→ Логика (feature flag):
    │   ├─→ Если audio_route_manager.enabled = true:
    │   │   └─→ Использует AVAudioEngine через AudioRouteManager
    │   │       (НЕ управляет output напрямую)
    │   └─→ Если audio_route_manager.enabled = false:
    │       └─→ Старая логика (SequentialSpeechPlayer с sounddevice.OutputStream)
    │
    └─→ Публикации (сохраняются):
        ├─→ playback.started/completed/failed
        └─→ playback.cancelled

15. SignalIntegration
    └─→ Аудио-сигналы (тоны)
    └─→ Подписывается: voice.mic_opened, playback.completed

16. UpdaterIntegration
    └─→ Управление обновлениями
    └─→ Публикует: updater.in_progress.changed

17. AutostartManagerIntegration
    └─→ Управление автозапуском

18. WelcomeMessageIntegration
    └─→ Приветственное сообщение

19. VoiceOverDuckingIntegration
    └─→ Ducking для VoiceOver

20. ActionExecutionIntegration
    └─→ Выполнение действий (open_app)
```

---

## 🔄 Детальная схема: Поток данных (идеальная архитектура)

### Сценарий 1: Push-to-talk (запись)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PUSH-TO-TALK FLOW                                    │
└─────────────────────────────────────────────────────────────────────────┘

1. Пользователь нажимает Control+N
   │
   ▼
2. KeyboardMonitor (Quartz/pynput)
   └─→ Генерирует: KeyEvent(PRESS)
   │
   ▼
3. InputProcessingIntegration
   ├─→ Обрабатывает: KeyEvent(PRESS)
   ├─→ Публикует: keyboard.press
   ├─→ Обрабатывает: KeyEvent(LONG_PRESS)
   └─→ Публикует: voice.recording_start {session_id: "123"}
   │
   ▼
4. AudioRouteManagerIntegration
   ├─→ Подписывается: voice.recording_start
   ├─→ Reconcile loop:
   │   ├─→ Создает Snapshot:
   │   │   ├─→ permissions.mic (из StateManager)
   │   │   ├─→ firstRun (из StateManager)
   │   │   ├─→ appMode (из StateManager)
   │   │   └─→ audio.input.state (из RouteManager)
   │   │
   │   ├─→ Gateway: decide_audio_input_start(snapshot)
   │   │   ├─→ Проверяет: permissions.mic = granted
   │   │   ├─→ Проверяет: firstRun = false
   │   │   ├─→ Проверяет: appMode = LISTENING
   │   │   └─→ Решение: START
   │   │
   │   ├─→ DeviceDiscovery: get_input_devices()
   │   │   └─→ AVFoundation: AVAudioSession.sharedInstance()
   │   │
   │   ├─→ DeviceMapping: find_portaudio_match()
   │   │   └─→ PortAudio: sd.query_devices()
   │   │
   │   └─→ AVFInputAdapter: start_stream()
   │       ├─→ sounddevice.InputStream(device_index, samplerate, callback)
   │       └─→ input_stream.start()
   │
   └─→ Публикует: audio.input.active {session_id: "123", device_uid: "..."}
   │
   ▼
5. VoiceRecognitionIntegration
   ├─→ Подписывается: audio.input.active
   ├─→ Получает аудио-данные из AudioRouteManager (callback)
   │   └─→ audio_buffer → накопление данных
   │
   ├─→ Публикует: voice.mic_opened {session_id: "123"}
   │   └─→ SignalIntegration реагирует (воспроизводит тон)
   │
   └─→ Отправляет в Google SR:
       ├─→ Ресемплинг: 16k mono
       ├─→ speech_recognition.Recognizer().recognize_google()
       └─→ Публикует: voice.recognition_started/completed
   │
   ▼
6. Пользователь отпускает Control+N
   │
   ▼
7. InputProcessingIntegration
   └─→ Публикует: voice.recording_stop {session_id: "123"}
   │
   ▼
8. AudioRouteManagerIntegration
   ├─→ Подписывается: voice.recording_stop
   ├─→ AVFInputAdapter: stop_stream()
   │   └─→ input_stream.stop() + close()
   └─→ Публикует: audio.input.inactive {session_id: "123"}
   │
   ▼
9. VoiceRecognitionIntegration
   ├─→ Завершает распознавание
   └─→ Публикует: voice.recognition_completed, voice.mic_closed
```

### Сценарий 2: Воспроизведение ответа

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PLAYBACK FLOW                                       │
└─────────────────────────────────────────────────────────────────────────┘

1. GrpcClientIntegration
   └─→ Публикует: grpc.response.audio {session_id: "123", audio_bytes: ...}
   │
   ▼
2. SpeechPlaybackIntegration
   ├─→ Подписывается: grpc.response.audio
   ├─→ Проверяет: audio.output.ready (от AudioRouteManager)
   │
   ├─→ Логика (feature flag):
   │   ├─→ Если audio_route_manager.enabled = true:
   │   │   ├─→ Использует: AudioRouteManager.get_output_adapter()
   │   │   ├─→ AVFOutputAdapter: play_audio_chunk()
   │   │   │   ├─→ numpy → AVAudioPCMBuffer
   │   │   │   ├─→ AVAudioPlayerNode.scheduleBuffer_()
   │   │   │   └─→ AVAudioEngine.start()
   │   │   └─→ Публикует: playback.started/completed
   │   │
   │   └─→ Если audio_route_manager.enabled = false:
   │       └─→ Старая логика (SequentialSpeechPlayer)
   │
   └─→ Публикует: playback.started/completed (сохраняется для совместимости)
   │
   ▼
3. ProcessingWorkflow
   ├─→ Подписывается: playback.completed
   └─→ Переход в SLEEPING режим
```

### Сценарий 3: Переключение устройства

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DEVICE SWITCHING FLOW                                │
└─────────────────────────────────────────────────────────────────────────┘

1. AudioRouteManagerIntegration (мониторинг thread)
   ├─→ Каждую секунду:
   │   ├─→ DeviceDiscovery: get_input_devices() / get_output_devices()
   │   ├─→ PortAudio: sd.default.device[0] / sd.default.device[1]
   │   └─→ DeviceMapping: find_portaudio_match()
   │
   ├─→ Обнаруживает: изменение устройства (UID изменился)
   │
   ├─→ Reconcile loop:
   │   ├─→ Создает Snapshot:
   │   │   ├─→ audio.input.state (active?)
   │   │   ├─→ audio.output.state (playing?)
   │   │   └─→ audio.input.device_uid (старое vs новое)
   │   │
   │   ├─→ Gateway: decide_audio_device_switch(snapshot)
   │   │   ├─→ Проверяет: можно ли переключать (не во время записи/воспроизведения?)
   │   │   └─→ Решение: SWITCH
   │   │
   │   └─→ Выполняет переключение:
   │       ├─→ Input: AVFInputAdapter.switch_device()
   │       │   ├─→ Останавливает старый stream
   │       │   ├─→ Очищает audio_buffer
   │       │   └─→ Создает новый stream на новом устройстве
   │       │
   │       └─→ Output: AVFOutputAdapter.switch_device()
   │           ├─→ Останавливает engine (с engine_lock)
   │           └─→ Пересоздает engine (автоматически на новом устройстве)
   │
   └─→ Публикует: audio.device.changed {type: "input|output", old_uid, new_uid}
   │
   ▼
2. VoiceRecognitionIntegration / SpeechPlaybackIntegration
   ├─→ Подписывается: audio.device.changed
   └─→ Адаптируется к новому устройству (если нужно)
```

---

## 🎯 Точки входа в проект

### Точка входа 1: SimpleModuleCoordinator

**Файл**: `integration/core/simple_module_coordinator.py`

**Место добавления**:
```python
# В методе _create_integrations() после PermissionRestartIntegration

# AudioRouteManager Integration (НОВАЯ)
audio_route_config = config_data.get('audio_route_manager', {})
self.integrations['audio_route_manager'] = AudioRouteManagerIntegration(
    event_bus=self.event_bus,
    state_manager=self.state_manager,
    error_handler=self.error_handler,
    config=audio_route_config
)
```

**Порядок инициализации**:
- Позиция: 5 (после PermissionRestart, перед Tray)
- Причина: Должен быть инициализирован до VoiceRecognition и SpeechPlayback

---

### Точка входа 2: VoiceRecognitionIntegration

**Файл**: `integration/integrations/voice_recognition_integration.py`

**Место изменения**:
```python
# В методе __init__()
self._use_audio_route_manager = (
    unified_config.get('audio_route_manager', {}).get('enabled', False) and
    not unified_config.get('audio_route_manager', {}).get('kill_switch', False)
)

# В методе _on_recording_start()
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return
    
    if self._use_audio_route_manager:
        # Новая логика: AudioRouteManager управляет микрофоном
        session_id = event.get("session_id")
        await self.event_bus.publish("audio.input.request_start", {
            "session_id": session_id
        })
        # Ждем audio.input.active для получения аудио-данных
    else:
        # Старая логика (fallback)
        if not self.config.simulate and self._recognizer:
            await self._recognizer.start_listening()
```

**Новая подписка**:
```python
# В методе initialize()
await self.event_bus.subscribe("audio.input.active", self._on_audio_input_active, EventPriority.HIGH)
```

---

### Точка входа 3: SpeechPlaybackIntegration

**Файл**: `integration/integrations/speech_playback_integration.py`

**Место изменения**:
```python
# В методе __init__()
self._use_audio_route_manager = (
    unified_config.get('audio_route_manager', {}).get('enabled', False) and
    not unified_config.get('audio_route_manager', {}).get('kill_switch', False)
)

# В методе _on_audio_chunk()
async def _on_audio_chunk(self, event):
    if self._use_audio_route_manager:
        # Новая логика: используем AVAudioEngine через AudioRouteManager
        # Проверяем audio.output.ready перед воспроизведением
        # Используем AVFOutputAdapter для воспроизведения
    else:
        # Старая логика (fallback)
        # Используем SequentialSpeechPlayer как раньше
```

**Новая подписка**:
```python
# В методе initialize()
await self.event_bus.subscribe("audio.output.ready", self._on_audio_output_ready, EventPriority.HIGH)
```

---

### Точка входа 4: unified_config.yaml

**Файл**: `config/unified_config.yaml`

**Место добавления**:
```yaml
# Новый раздел (добавляется в конец файла)
audio_route_manager:
  enabled: false  # Feature flag (по умолчанию выключен)
  kill_switch: false  # Kill-switch для мгновенного отката
  
  device_monitoring_interval_sec: 1.0
  reconcile_debounce_ms: 500
  
  input:
    fallback_samplerates: [48000, 16000, 44100, 48000]
    blocksize: 1024
    auto_device_switch: true
    
  output:
    auto_device_switch: true
    recreate_on_switch: true
```

---

### Точка входа 5: STATE_CATALOG.md

**Файл**: `Docs/STATE_CATALOG.md`

**Место добавления**:
```markdown
#### 11) audio.input.state
- **владелец**: AudioRouteManagerIntegration owner
- **пишет**: `audio_route_manager`
- **читает**: `voice_recognition`, `gateways`
- **источник истины**: RouteManager (внутреннее состояние)
- **метрики**: `audio_input_start_success_rate`
- **правила в interaction_matrix.yaml**: `hard_stop` при `error` → `abort_listen`

#### 12) audio.output.state
- **владелец**: AudioRouteManagerIntegration owner
- **пишет**: `audio_route_manager`
- **читает**: `speech_playback`, `gateways`
- **источник истины**: RouteManager (внутреннее состояние)
- **метрики**: `audio_output_start_success_rate`
- **правила в interaction_matrix.yaml**: `graceful` при `error` → `retry`
```

---

### Точка входа 6: interaction_matrix.yaml

**Файл**: `config/interaction_matrix.yaml`

**Место добавления**:
```yaml
axes:
  # ... существующие оси ...
  audio.input.state: [idle, starting, active, stopping, error]
  audio.output.state: [idle, initializing, ready, playing, error]
  audio.input.device_uid: [string]
  audio.output.device_uid: [string]
  audio.reconcile.pending: [true, false]

rules:
  # ... существующие правила ...
  
  # Hard stop: audio.input.state = error
  - when: {audio.input.state: error}
    decision: abort
    priority: hard_stop
    gateway: decide_audio_input_start
    description: Audio input in error state - cannot proceed
    
  # Graceful: audio.output.state = error
  - when: {audio.output.state: error}
    decision: retry
    priority: graceful
    gateway: decide_audio_output_start
    description: Audio output in error state - retry with fallback
```

---

### Точка входа 7: gateways.py

**Файл**: `integration/core/gateways.py`

**Место добавления**:
```python
# Новые gateway функции
def decide_audio_input_start(snapshot: Snapshot) -> Decision:
    """Принятие решения о запуске audio input"""
    # Проверяет: permissions.mic, firstRun, appMode, audio.input.state
    # Возвращает: START, ABORT, RETRY, DEGRADE

def decide_audio_output_start(snapshot: Snapshot) -> Decision:
    """Принятие решения о запуске audio output"""
    # Проверяет: audio.output.state
    # Возвращает: START, ABORT, RETRY, DEGRADE

def decide_audio_device_switch(snapshot: Snapshot) -> Decision:
    """Принятие решения о переключении устройства"""
    # Проверяет: audio.input.state, audio.output.state
    # Возвращает: SWITCH, ABORT, RETRY
```

---

### Точка входа 8: selectors.py

**Файл**: `integration/core/selectors.py`

**Место добавления**:
```python
# Новые selectors
def audio_input_active(snapshot: Snapshot) -> bool:
    """Проверка: audio input активен"""
    return snapshot.audio_input_state == "active"

def audio_output_ready(snapshot: Snapshot) -> bool:
    """Проверка: audio output готов"""
    return snapshot.audio_output_state == "ready"

def audio_device_changed(snapshot: Snapshot, old_uid: str) -> bool:
    """Проверка: устройство изменилось"""
    return snapshot.audio_input_device_uid != old_uid
```

---

## 🔄 Интеграция с существующими компонентами

### Workflows

#### ListeningWorkflow

**Текущие подписки**:
- `voice.recording_start` ✅ Сохраняется
- `voice.recognition_completed` ✅ Сохраняется
- `app.mode_changed` ✅ Сохраняется

**Изменения**: НЕТ (все события сохраняются)

#### ProcessingWorkflow

**Текущие подписки**:
- `screenshot.captured` ✅ Сохраняется
- `grpc.request_completed` ✅ Сохраняется
- `playback.completed` ✅ Сохраняется

**Изменения**: НЕТ (все события сохраняются)

---

### StateManager

**Текущие оси**:
- `permissions.mic/screen/accessibility`
- `device.input`
- `network`
- `firstRun`
- `appMode`
- `permissions.restart_pending`
- `process.lifecycle`
- `update_in_progress`

**Новые оси** (добавляются):
- `audio.input.state`
- `audio.output.state`
- `audio.input.device_uid`
- `audio.output.device_uid`
- `audio.reconcile.pending`

**Изменения**: Минимальные (только добавление новых осей)

---

### ErrorHandler

**Текущие категории**:
- `INITIALIZATION`
- `RUNTIME`
- `CONFIGURATION`
- `NETWORK`
- `PERMISSION`
- `UNKNOWN`

**Новые категории** (опционально):
- `AUDIO_INPUT`
- `AUDIO_OUTPUT`
- `AUDIO_ROUTE`

**Изменения**: Минимальные (только добавление новых категорий, если нужно)

---

## ✅ Итоговая карта точек входа

| Точка входа | Файл | Тип изменения | Критичность |
|-------------|------|---------------|-------------|
| 1. SimpleModuleCoordinator | `integration/core/simple_module_coordinator.py` | Добавление интеграции | Высокая |
| 2. VoiceRecognitionIntegration | `integration/integrations/voice_recognition_integration.py` | Адаптация (feature flag) | Высокая |
| 3. SpeechPlaybackIntegration | `integration/integrations/speech_playback_integration.py` | Адаптация (feature flag) | Высокая |
| 4. unified_config.yaml | `config/unified_config.yaml` | Добавление конфигурации | Средняя |
| 5. STATE_CATALOG.md | `Docs/STATE_CATALOG.md` | Добавление осей | Средняя |
| 6. interaction_matrix.yaml | `config/interaction_matrix.yaml` | Добавление правил | Средняя |
| 7. gateways.py | `integration/core/gateways.py` | Добавление функций | Средняя |
| 8. selectors.py | `integration/core/selectors.py` | Добавление функций | Средняя |
| 9. Новый модуль | `modules/audio_route_manager/` | Создание модуля | Высокая |
| 10. Новая интеграция | `integration/integrations/audio_route_manager_integration.py` | Создание интеграции | Высокая |

---

## 🎯 Критерии готовности к реализации

### Технические

- [x] Все точки входа определены
- [x] Порядок инициализации правильный
- [x] Нет циклических зависимостей
- [x] Feature flag работает
- [x] Kill-switch работает

### Функциональные

- [x] Все существующие события сохраняются
- [x] Обратная совместимость обеспечена
- [x] Новые события не конфликтуют
- [x] Workflows не затрагиваются

### Процессные

- [x] STATE_CATALOG.md обновлен
- [x] interaction_matrix.yaml обновлен
- [x] Контракт EventBus создан
- [x] Метрики определены

---

## 📋 Чек-лист перед началом реализации

- [ ] Создать Impact Map для Этапа 1
- [ ] Обновить STATE_CATALOG.md с новыми осями
- [ ] Обновить interaction_matrix.yaml с новыми правилами
- [ ] Создать контракт EventBus для новых событий
- [ ] Обновить selectors.py с новыми selectors
- [ ] Обновить gateways.py с новыми gateway функциями
- [ ] Начать реализацию Этапа 1 (модуль audio_route_manager)

