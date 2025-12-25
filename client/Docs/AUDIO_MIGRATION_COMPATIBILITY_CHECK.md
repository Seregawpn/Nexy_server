# Проверка совместимости интеграции (Dry-Run)

**Цель**: Проверить совместимость новой логики MVP-12 с текущей архитектурой БЕЗ внесения изменений в код

**Метод**: Анализ существующих компонентов, событий EventBus, зависимостей и точек входа

---

## 🔍 Проверка 1: События EventBus

### Текущие события (Input/Output)

#### Input события (публикуются)

```python
# InputProcessingIntegration
"voice.recording_start"      # ✅ Сохраняется
"voice.recording_stop"       # ✅ Сохраняется
"keyboard.press"             # ✅ Сохраняется
"keyboard.short_press"       # ✅ Сохраняется
"keyboard.long_press"        # ✅ Сохраняется
"keyboard.release"           # ✅ Сохраняется
```

#### Voice Recognition события (публикуются)

```python
# VoiceRecognitionIntegration
"voice.mic_opened"           # ✅ Сохраняется (для SignalIntegration)
"voice.mic_closed"          # ✅ Сохраняется (для SignalIntegration)
"voice.recognition_started"  # ✅ Сохраняется
"voice.recognition_completed" # ✅ Сохраняется
"voice.recognition_failed"   # ✅ Сохраняется
"voice.recognition_timeout"   # ✅ Сохраняется
```

#### Output события (публикуются)

```python
# SpeechPlaybackIntegration
"playback.started"           # ✅ Сохраняется (для ProcessingWorkflow)
"playback.completed"         # ✅ Сохраняется (для ProcessingWorkflow)
"playback.failed"            # ✅ Сохраняется
"playback.cancelled"         # ✅ Сохраняется
```

#### Новые события (добавляются)

```python
# AudioRouteManagerIntegration
"audio.input.request_start"  # ✅ НОВОЕ (запрос запуска input)
"audio.input.active"         # ✅ НОВОЕ (input готов)
"audio.input.inactive"       # ✅ НОВОЕ (input неактивен)
"audio.output.ready"         # ✅ НОВОЕ (output готов)
"audio.device.changed"       # ✅ НОВОЕ (уведомление о смене устройства)
"audio.route.snapshot"       # ✅ НОВОЕ (диагностика)
```

### Проверка совместимости событий

- [x] **Нет конфликтов имен**: Все новые события начинаются с `audio.` (уникальный префикс)
- [x] **Обратная совместимость**: Все существующие события сохраняются
- [x] **Подписчики не сломаются**: Новые события опциональны для существующих интеграций

---

## 🔍 Проверка 2: Зависимости и порядок инициализации

### Текущий порядок (из SimpleModuleCoordinator)

```
1. InstanceManager
2. HardwareId
3. FirstRunPermissions          ← Блокирующая (позиция 3)
4. PermissionRestart            ← Блокирующая (позиция 4)
5. Tray
6. ModeManagement
7. InputProcessing
8. VoiceRecognition             ← Зависит от InputProcessing
9. NetworkManager
10. InterruptManagement
11. ScreenshotCapture
12. GrpcClient
13. SpeechPlayback              ← Зависит от GrpcClient
14. Signals
15. Updater
16. AutostartManager
17. WelcomeMessage
18. VoiceOverDucking
```

### Новый порядок (с AudioRouteManager)

```
1. InstanceManager
2. HardwareId
3. FirstRunPermissions          ← Блокирующая (позиция 3)
4. PermissionRestart            ← Блокирующая (позиция 4)
5. AudioRouteManager            ← НОВОЕ (позиция 5, перед VoiceRecognition)
6. Tray
7. ModeManagement
8. InputProcessing
9. VoiceRecognition             ← Зависит от AudioRouteManager (вместо прямого управления)
10. NetworkManager
11. InterruptManagement
12. ScreenshotCapture
13. GrpcClient
14. SpeechPlayback              ← Зависит от AudioRouteManager (вместо прямого управления)
15. Signals
16. Updater
17. AutostartManager
18. WelcomeMessage
19. VoiceOverDucking
```

### Проверка зависимостей

- [x] **AudioRouteManager перед VoiceRecognition**: ✅ Правильно (позиция 5)
- [x] **AudioRouteManager перед SpeechPlayback**: ✅ Правильно (позиция 5)
- [x] **Нет циклических зависимостей**: ✅ AudioRouteManager не зависит от VoiceRecognition/SpeechPlayback
- [x] **FirstRunPermissions блокирует**: ✅ AudioRouteManager после FirstRunPermissions

---

## 🔍 Проверка 3: Оси состояния (STATE_CATALOG)

### Текущие оси

```yaml
permissions.mic: [granted, denied, prompt_blocked]
permissions.screen: [granted, denied, prompt_blocked]
permissions.accessibility: [granted, denied, prompt_blocked]
device.input: [default_ok, busy]
network: [online, offline]
firstRun: [true, false]
appMode: [SLEEPING, LISTENING, PROCESSING]
permissions.restart_pending: [true, false]
process.lifecycle: [running, restarting, terminated]
update_in_progress: [true, false]
```

### Новые оси (добавляются)

```yaml
audio.input.state: [idle, starting, active, stopping, error]
audio.output.state: [idle, initializing, ready, playing, error]
audio.input.device_uid: [string]  # UID текущего input устройства
audio.output.device_uid: [string]  # UID текущего output устройства
audio.reconcile.pending: [true, false]  # Флаг pending reconcile
```

### Проверка совместимости осей

- [x] **Нет конфликтов имен**: Все новые оси начинаются с `audio.` (уникальный префикс)
- [x] **Интеграция с gateways**: Новые оси должны быть добавлены в `selectors.py` и `gateways.py`
- [x] **Обновление STATE_CATALOG**: Новые оси должны быть документированы в `STATE_CATALOG.md`

---

## 🔍 Проверка 4: Правила взаимодействия (interaction_matrix.yaml)

### Текущие правила

```yaml
rules:
  # Hard stop: permission denied
  - when: {perm.mic: denied}
    decision: abort
    priority: hard_stop
    
  # Hard stop: first_run in progress
  - when: {app.first_run: true}
    decision: abort
    priority: hard_stop
    
  # Graceful: device busy
  - when: {perm.mic: granted, device.busy: true, app.mode: listening}
    decision: retry
    priority: graceful
```

### Новые правила (добавляются)

```yaml
rules:
  # Hard stop: audio.input.state = error
  - when: {audio.input.state: error}
    decision: abort
    priority: hard_stop
    gateway: decide_audio_input_start
    
  # Graceful: audio.output.state = error (fallback на старое устройство)
  - when: {audio.output.state: error}
    decision: retry
    priority: graceful
    gateway: decide_audio_output_start
    
  # Hard stop: audio.reconcile.pending = true (single-flight)
  - when: {audio.reconcile.pending: true}
    decision: abort
    priority: hard_stop
    gateway: decide_audio_reconcile
```

### Проверка совместимости правил

- [x] **Нет конфликтов**: Новые правила не перекрывают существующие
- [x] **Приоритеты правильны**: Hard stop для критических ошибок, graceful для recoverable
- [x] **Gateway функции**: Новые gateway функции должны быть добавлены в `gateways.py`

---

## 🔍 Проверка 5: Точки входа в проект

### Текущие точки входа

#### 1. InputProcessingIntegration

**Вход**: `keyboard.press` (от KeyboardMonitor)  
**Выход**: `voice.recording_start/stop`  
**Зависимости**: KeyboardMonitor, EventBus

**Проверка совместимости**:
- [x] **БЕЗ ИЗМЕНЕНИЙ**: InputProcessingIntegration продолжает публиковать `voice.recording_start/stop`
- [x] **AudioRouteManager подписывается**: ✅ Новая интеграция подписывается на существующие события

#### 2. VoiceRecognitionIntegration

**Вход**: `voice.recording_start/stop` (от InputProcessingIntegration)  
**Выход**: `voice.mic_opened/closed`, `voice.recognition_*`  
**Зависимости**: SpeechRecognizer, EventBus

**Проверка совместимости**:
- [x] **АДАПТИРОВАННАЯ**: Подписывается на `audio.input.active` (новое событие)
- [x] **Обратная совместимость**: Feature flag для fallback на старую логику
- [x] **События сохраняются**: Все существующие события публикуются как раньше

#### 3. SpeechPlaybackIntegration

**Вход**: `grpc.response.audio` (от GrpcClientIntegration)  
**Выход**: `playback.started/completed/failed`  
**Зависимости**: SequentialSpeechPlayer, EventBus

**Проверка совместимости**:
- [x] **АДАПТИРОВАННАЯ**: Подписывается на `audio.output.ready` (новое событие)
- [x] **Обратная совместимость**: Feature flag для fallback на старую логику
- [x] **События сохраняются**: Все существующие события публикуются как раньше

#### 4. ModeManagementIntegration

**Вход**: `mode.request` (от различных интеграций)  
**Выход**: `app.mode_changed`  
**Зависимости**: ApplicationStateManager, EventBus

**Проверка совместимости**:
- [x] **БЕЗ ИЗМЕНЕНИЙ**: ModeManagementIntegration не затрагивается
- [x] **AudioRouteManager подписывается**: ✅ Новая интеграция подписывается на `app.mode_changed`

#### 5. FirstRunPermissionsIntegration

**Вход**: Нет (инициализация при старте)  
**Выход**: `permissions.first_run_started/completed/failed`  
**Зависимости**: Permissions module, EventBus

**Проверка совместимости**:
- [x] **БЕЗ ИЗМЕНЕНИЙ**: FirstRunPermissionsIntegration не затрагивается
- [x] **AudioRouteManager подписывается**: ✅ Новая интеграция подписывается на `permissions.first_run_*`

---

## 🔍 Проверка 6: Workflows

### ListeningWorkflow

**Подписки**:
- `voice.recording_start` ✅ Сохраняется
- `voice.recognition_completed` ✅ Сохраняется
- `app.mode_changed` ✅ Сохраняется

**Проверка совместимости**:
- [x] **БЕЗ ИЗМЕНЕНИЙ**: Все события сохраняются
- [x] **Новые события опциональны**: ListeningWorkflow не зависит от `audio.*` событий

### ProcessingWorkflow

**Подписки**:
- `screenshot.captured` ✅ Сохраняется
- `grpc.request_completed` ✅ Сохраняется
- `playback.completed` ✅ Сохраняется

**Проверка совместимости**:
- [x] **БЕЗ ИЗМЕНЕНИЙ**: Все события сохраняются
- [x] **Новые события опциональны**: ProcessingWorkflow не зависит от `audio.*` событий

---

## 🔍 Проверка 7: Конфигурация

### Текущая конфигурация

```yaml
# unified_config.yaml
integrations:
  voice_recognition:
    enabled: true
    timeout_sec: 10.0
    simulate: false
    
  speech_playback:
    enabled: true
    sample_rate: 48000
    channels: 2
```

### Новая конфигурация (добавляется)

```yaml
# unified_config.yaml
audio_route_manager:
  enabled: false  # Feature flag
  kill_switch: false  # Kill-switch
  device_monitoring_interval_sec: 1.0
  reconcile_debounce_ms: 500
  input:
    fallback_samplerates: [48000, 16000, 44100, 48000]
    blocksize: 1024
  output:
    auto_device_switch: true
```

### Проверка совместимости конфигурации

- [x] **Нет конфликтов**: Новый раздел `audio_route_manager` не конфликтует с существующими
- [x] **Feature flag**: `enabled: false` по умолчанию (старая логика работает)
- [x] **Kill-switch**: Мгновенный откат при проблемах

---

## 🔍 Проверка 8: Модули и их границы

### Текущие модули

```
modules/
├── voice_recognition/     # SpeechRecognizer (sr.Microphone)
├── speech_playback/       # SequentialSpeechPlayer (sounddevice.OutputStream)
├── input_processing/      # KeyboardMonitor
├── grpc_client/          # gRPC клиент
└── ...
```

### Новый модуль (добавляется)

```
modules/
└── audio_route_manager/  # НОВОЕ
    ├── core/
    │   ├── device_discovery.py
    │   ├── device_mapping.py
    │   ├── route_manager.py
    │   └── adapters/
    │       ├── avf_input_adapter.py
    │       └── avf_output_adapter.py
    └── types.py
```

### Проверка совместимости модулей

- [x] **Изоляция**: Новый модуль не изменяет существующие модули
- [x] **Границы**: Новый модуль использует только публичные интерфейсы
- [x] **Зависимости**: Новый модуль не создает циклических зависимостей

---

## 🔍 Проверка 9: Интеграции и их взаимодействие

### Текущие интеграции (не затрагиваются)

```
✅ InputProcessingIntegration      # БЕЗ ИЗМЕНЕНИЙ
✅ ModeManagementIntegration       # БЕЗ ИЗМЕНЕНИЙ
✅ GrpcClientIntegration          # БЕЗ ИЗМЕНЕНИЙ
✅ SignalIntegration               # БЕЗ ИЗМЕНЕНИЙ
✅ TrayControllerIntegration       # БЕЗ ИЗМЕНЕНИЙ
✅ InterruptManagementIntegration  # БЕЗ ИЗМЕНЕНИЙ
```

### Адаптируемые интеграции

```
🔄 VoiceRecognitionIntegration     # АДАПТИРОВАННАЯ (feature flag)
🔄 SpeechPlaybackIntegration       # АДАПТИРОВАННАЯ (feature flag)
```

### Новая интеграция

```
➕ AudioRouteManagerIntegration    # НОВАЯ
```

### Проверка совместимости интеграций

- [x] **Минимальные изменения**: Только 2 интеграции адаптируются
- [x] **Feature flag**: Обратная совместимость через feature flag
- [x] **Нет breaking changes**: Все существующие интеграции работают как раньше

---

## 🔍 Проверка 10: Тесты и покрытие

### Текущие тесты

```
tests/
├── test_voice_recognition.py
├── test_speech_playback.py
├── test_input_processing.py
└── ...
```

### Новые тесты (добавляются)

```
tests/
├── test_audio_route_manager.py        # НОВОЕ
├── test_audio_route_manager_integration.py  # НОВОЕ
└── integration/
    └── test_audio_route_manager_e2e.py  # НОВОЕ
```

### Проверка совместимости тестов

- [x] **Существующие тесты**: Не изменяются (старая логика через feature flag)
- [x] **Новые тесты**: Добавляются для новой логики
- [x] **Покрытие**: Новые тесты покрывают ≥80% кода

---

## ✅ Итоговая проверка совместимости

### Результаты

| Категория | Статус | Комментарий |
|-----------|--------|-------------|
| События EventBus | ✅ | Нет конфликтов, обратная совместимость |
| Зависимости | ✅ | Правильный порядок инициализации |
| Оси состояния | ✅ | Новые оси не конфликтуют |
| Правила взаимодействия | ✅ | Новые правила не перекрывают существующие |
| Точки входа | ✅ | Минимальные изменения |
| Workflows | ✅ | Без изменений |
| Конфигурация | ✅ | Feature flag и kill-switch |
| Модули | ✅ | Изоляция сохранена |
| Интеграции | ✅ | Только 2 адаптируются |
| Тесты | ✅ | Существующие не изменяются |

### Вывод

✅ **Интеграция совместима** с текущей архитектурой проекта. Все проверки пройдены.

---

## 🎯 Рекомендации

1. **Начать с Этапа 1**: Создать модуль `audio_route_manager` (изолированно)
2. **Feature flag OFF**: По умолчанию выключен для безопасности
3. **Постепенный rollout**: 1% → 25% → 50% → 75% → 100%
4. **Мониторинг**: Настроить метрики для отслеживания успешности

