# FLOW_INTERACTION_SPEC (CLIENT)

Единый источник истины по взаимодействию Flow, контрактам событий и требованиям к формату payload. Все профильные документы должны ссылаться сюда и не дублировать общий контракт.

## 0) Область и источники истины

- Область: клиент (EventBus) + gRPC контракт на границе клиента и сервера.
- Источник истины по состояниям: `client/Docs/STATE_CATALOG.md`.
- Источник истины по архитектуре: `client/Docs/ARCHITECTURE_OVERVIEW.md`.
- Этот документ: Source of Truth по Flow взаимодействиям и event contract.

## 1) Общий формат событий (EventBus)

EventBus публикует событие как:

```json
{
  "type": "event.name",
  "data": { "payload": "..." },
  "timestamp": 12345.67
}
```

Правила:
- Все поля payload должны лежать в `event.data`.
- `event.timestamp` — время публикации (asyncio loop).
- Не размещать данные payload на верхнем уровне `event`.
- Поля `session_id` и `source` обязательны там, где указано в контракте.
- Типы событий должны использовать константы из `integration/core/event_types.py` (EventTypes).

## 2) Глобальные инварианты

- Смена режима: только через `mode.request`; факт смены — только `ApplicationStateManager` (`app.mode_changed`).
- `session_id` — единый источник истины: `ApplicationStateManager`.
- Завершение PROCESSING: только по `playback.completed` или `grpc.request_completed` (без фиксированных таймаутов).
- Прерывания: единый канал отмены аудио — `playback.cancelled` (publisher только `SpeechPlaybackIntegration`).
- `grpc.request_cancel` публикуется только `InterruptManagementIntegration`.
- Cancel side effects (stop/clear/guard/session cleanup) выполняются только одним owner-обработчиком в `SpeechPlaybackIntegration` по событию `playback.cancelled`.
- Любые локальные стейты не заменяют централизованные оси (`STATE_CATALOG.md`).

## 3) Контракты событий (канонические)

### 3.1 Режимы

Event: `mode.request`  
Publisher: любые интеграции/модули  
Subscriber: `ModeManagementIntegration`  
Payload:
```yaml
required:
  target: "SLEEPING|LISTENING|PROCESSING"
  source: str
optional:
  session_id: str|float|None
  priority: int
  reason: str
  data: dict
```

Event: `app.mode_changed`  
Publisher: `ApplicationStateManager`  
Subscribers: все  
Payload:
```yaml
required:
  mode: "SLEEPING|LISTENING|PROCESSING"
optional:
  session_id: str|float|None
```

Event: `app.state_changed` (мост совместимости)  
Payload:
```yaml
required:
  old_mode: AppMode
  new_mode: AppMode
```

### 3.2 Ввод (клавиатура)

Event: `keyboard.short_press`  
Payload:
```yaml
required:
  source: "keyboard"
  timestamp: float
  duration: float
optional:
  key: str|None
  reason: str
```

### 3.3 Голос / распознавание

Event: `voice.recording_start`  
Payload:
```yaml
required:
  session_id: str|float
  source: str
  timestamp: float
```

Event: `voice.recording_stop`  
Payload:
```yaml
required:
  source: str
  timestamp: float
  duration: float
optional:
  session_id: str|float|None
```

Event: `voice.mic_opened|voice.mic_closed`  
Payload:
```yaml
required:
  session_id: str|float
```

Event: `voice.recognition_started`  
Payload:
```yaml
required:
  session_id: str|float
  language: str
```

Event: `voice.recognition_completed`  
Payload:
```yaml
required:
  session_id: str|float
  text: str
  confidence: float
  language: str
```

Event: `voice.recognition_failed`  
Payload:
```yaml
required:
  session_id: str|float
  error: str
optional:
  reason: str
```

Event: `voice.recognition_timeout`  
Payload:
```yaml
required:
  session_id: str|float
  timeout_sec: float
```

### 3.4 Скриншоты

Event: `screenshot.captured`  
Payload:
```yaml
required:
  session_id: str|float|None
  image_path: str
  format: str
  width: int|None
  height: int|None
  size_bytes: int|None
  mime_type: str
  capture_time: float
```

Event: `screenshot.error`  
Payload:
```yaml
required:
  session_id: str|float|None
  error: str
```

### 3.5 gRPC (клиент)

Event: `grpc.request_started`  
Payload:
```yaml
required:
  session_id: str|float
  has_screenshot: bool
```

Event: `grpc.request_completed`  
Payload:
```yaml
required:
  session_id: str|float
```

Event: `grpc.request_failed`  
Payload:
```yaml
required:
  session_id: str|float
  error: str
```

Event: `grpc.request_cancel`  
Publisher: `InterruptManagementIntegration`  
Payload:
```yaml
required:
  session_id: str|float
```

Event: `grpc.response.audio`  
Payload:
```yaml
required:
  session_id: str|float
  dtype: str
  sample_rate: int
  channels: int
  shape: list[int]
  bytes: bytes
```

Event: `grpc.response.text`  
Payload:
```yaml
required:
  session_id: str|float
  text: str
```

Event: `grpc.response.action` (MCP)  
Publisher: `GrpcClientIntegration` (только ActionMessage; legacy text‑tunneling отключен)  
Payload:
```yaml
required:
  session_id: str|float
  action_json: str|None
  feature_id: str
  source: str  # action_message
optional:
  error: str
```

### 3.6 Воспроизведение (SpeechPlayback)

Event: `playback.started`  
Payload:
```yaml
required:
  session_id: str|float
optional:
  pattern: str
```

Event: `playback.completed`  
Payload:
```yaml
required:
  session_id: str|float
optional:
  pattern: str
```

Event: `playback.failed`  
Payload:
```yaml
required:
  session_id: str|float
  error: str
```

Event: `playback.cancelled` (единый канал прерывания)  
Publisher: `SpeechPlaybackIntegration`  
Payload:
```yaml
required:
  session_id: str|float|None
  reason: str
  source: str
optional:
  original_event: str
```

### 3.7 Прерывания

Event: `interrupt.request`  
Publisher: любые (в т.ч. InputProcessing)  
Subscriber: `InterruptManagementIntegration`  
Payload:
```yaml
required:
  type: str   # например: "speech_stop"
  source: str
  timestamp: float
optional:
  session_id: str|float|None
  duration: float
  reason: str
  priority: "LOW|NORMAL|HIGH|CRITICAL"
```

Event: `interrupt.completed`  
Payload:
```yaml
required:
  interrupt_id: str
  result: "completed|cancelled|failed"
```

### 3.8 Разрешения (first-run)

Event: `permissions.first_run_started`  
Payload:
```yaml
required:
  session_id: str
  source: str
```

Event: `permissions.status_checked`  
Payload:
```yaml
required:
  permission: str
  status: str
  session_id: str
  source: str
```

Event: `permissions.changed`  
Payload:
```yaml
required:
  permission: str
  old_status: str
  new_status: str
  session_id: str
  source: str
optional:
  is_timeout: bool  # true если new_status="denied" из-за таймаута (source="permissions.timeout")
                    # false или отсутствует для реального отказа (source="permissions.denied")
```

ВАЖНО: Различие между timeout и реальным отказом:
- Реальный отказ: new_status="denied", source="permissions.denied", is_timeout=false (или отсутствует)
- Timeout: new_status="denied", source="permissions.timeout", is_timeout=true
Подписчики должны проверять is_timeout для корректной обработки (не путать таймаут с явным отказом).

Event: `permissions.first_run_restart_pending`  
Payload:
```yaml
required:
  session_id: str
  source: str
  reason: str
```

Event: `permissions.first_run_completed`  
Payload:
```yaml
required:
  session_id: str
  source: str
  all_granted: bool
optional:
  restart_needed: bool
```

Event: `permissions.first_run_failed`  
Payload:
```yaml
required:
  session_id: str
  error: str
  source: str
```

### 3.9 Permission Restart

Event: `permission_restart.scheduled`  
Payload:
```yaml
required:
  session_id: str|None
  reason: str
  delay_sec: float
  critical_permissions: list[str]
```

Event: `permission_restart.executing`  
Payload:
```yaml
required:
  session_id: str|None
  reason: str
```

### 3.10 Обновления

Event: `updater.update_started`  
Payload:
```yaml
required:
  trigger: str
  version: str
```

Event: `updater.update_skipped`  
Payload:
```yaml
required:
  trigger: str
  reason: str
  current_version: str
```

Event: `updater.update_completed`  
Payload:
```yaml
required:
  trigger: str
  version: str
```

Event: `updater.update_failed`  
Payload:
```yaml
required:
  trigger: str
  error: str
  version: str
```

Event: `updater.in_progress.changed`  
Payload:
```yaml
required:
  active: bool
  trigger: str
```

Event: `updater.download_progress`  
Payload:
```yaml
required:
  percent: int
  stage: "download"
  trigger: str
```

Event: `updater.install_progress`  
Payload:
```yaml
required:
  percent: int
  stage: str
  trigger: str
```

Event: `updater.check_manual`  
Payload: пустой объект `{}`.

### 3.11 Сеть

Event: `network.status_snapshot`  
Payload:
```yaml
required:
  status: str
  quality: str
  connection_type: str
  metrics: { ping_time: float, last_updated: float }
  is_monitoring: bool
  config: { check_interval: float, ping_timeout: float, ping_hosts: list[str] }
```

Event: `network.status_changed`  
Payload:
```yaml
required:
  old: str
  new: str
  details: dict
  timestamp: float
```

### 3.12 App lifecycle

Event: `app.startup`  
Payload:
```yaml
required:
  coordinator: str
  integrations: list[str]
```

Event: `app.shutdown`  
Payload:
```yaml
required:
  coordinator: str
```

### 3.13 Браузер (Browser Automation)

Event: `browser.started`
Payload:
```yaml
required:
  session_id: str|float
  source: str
```

Event: `browser.completed`
Payload:
```yaml
required:
  session_id: str|float
  timestamp: float
```

Event: `browser.failed`
Payload:
```yaml
required:
  session_id: str|float
  error: str
  timestamp: float
```

Event: `browser.cancelled`
Payload:
```yaml
required:
  session_id: str|float
  reason: str
  timestamp: float
```

Event: `browser.progress`
Payload:
```yaml
required:
  session_id: str|float
  step_description: str
  progress_percent: int
```

Event: `browser.task_request` (клиент -> интеграция, canonical)
Payload:
```yaml
required:
  session_id: str|float
  task_goal: str
```

### 3.14 Сообщения (Messages MCP)

Event: `messages.read_request`
Payload:
```yaml
required:
  session_id: str|float
  contact_name: str|None
  limit: int
```

Event: `messages.send_request`
Payload:
```yaml
required:
  session_id: str|float
  contact_name: str
  message_content: str
```

Event: `messages.contact_search`
Payload:
```yaml
required:
  session_id: str|float
  query: str
```

### 3.15 Платежи и подписки (Payment)

Event: `payment.sync_requested`
Payload:
```yaml
required:
  session_id: str|float
  source: str
```

Event: `subscription.status_check`
Payload:
```yaml
required:
  session_id: str|float
```

Event: `subscription.status_updated`
Payload:
```yaml
required:
  status: "active|inactive|trial|expired|payment_failed"
  plan: str
  expiration_date: str|None
  features: list[str]
```

## 4) Спецификации Flow

### 4.1 Startup Flow

Coordinator: `SimpleModuleCoordinator`  
Source of Truth: `SimpleModuleCoordinator.startup_order`  

Sequence:
1. Создать core: EventBus, ApplicationStateManager, ErrorHandler.
2. Закрепить EventBus loop и подписки на критичные permissions-события.
3. Создать интеграции в фиксированном порядке.
4. `initialize()` для интеграций и workflows.
5. `start()` по `startup_order` (instance_manager → tray → hardware_id → first_run_permissions → permission_restart → mode_management → остальные).
6. `app.startup` публикуется после запуска всех интеграций и workflows.

Requirements:
- Подписки на `permissions.first_run_*` должны быть до `FirstRunPermissionsIntegration.initialize()` (race fix).
- `instance_manager` блокирует запуск и может завершить процесс.

### 4.2 First-Run Permissions Flow

Coordinator: `FirstRunPermissionsIntegration`  
Source of Truth: флаги `permissions_first_run_completed.flag`, `restart_completed.flag`  

Sequence:
1. Проверить флаг `permissions_first_run_completed.flag`. Если есть — публикуется `permissions.first_run_completed`, flow завершается.
2. Публиковать `permissions.first_run_started`.
3. Для каждого permission:
   - `permissions.status_checked` (до запроса)
   - инициировать запрос (TCC)
   - `permissions.status_checked` (после изменения)
   - при изменении — `permissions.changed`
4. Если требуется перезапуск → публиковать `permissions.first_run_restart_pending` и передать управление `PermissionRestartIntegration`.
5. После рестарта второй процесс публикует `permissions.first_run_completed`.

Requirements:
- Без таймаута ожидания GRANTED (infinite polling).
- Все события содержат `session_id` и `source`.

### 4.3 Permission Restart Flow

Coordinator: `PermissionRestartIntegration`  
Source of Truth: `decide_permission_restart_safety()` (gateway) + flags  

Sequence:
1. Получить `permissions.changed` и детектировать переход GRANTED для критических permissions.
2. Проверить безопасность (нет активных сессий, нет обновлений, appMode=SLEEPING).
3. Публиковать `permission_restart.scheduled` (delay).
4. По истечении delay — `permission_restart.executing` и выполнить restart (execv/open -n -a).

Requirements:
- Respect `update_in_progress`.
- Дебаунс множественных разрешений.

### 4.4 PTT / Listening Flow (SLEEPING → LISTENING)

Coordinator: `InputProcessingIntegration` + `ListeningWorkflow`  
Source of Truth: `ApplicationStateManager` (mode + session_id)  

Sequence:
1. LONG_PRESS → `voice.recording_start` + `mode.request(LISTENING)`.
2. `VoiceRecognitionIntegration` выполняет runtime-gate `decide_route_manager_reconcile(snapshot)` перед фактическим стартом микрофона.
3. При `abort`/`retry->abort`/`retry->retry` публикуются terminal события `voice.mic_closed` + `voice.recognition_failed`, запуск записи не продолжается.
4. `ModeManagementIntegration` → `app.mode_changed(LISTENING)`.
5. `SignalIntegration` на `app.mode_changed(LISTENING)` публикует `playback.signal(pattern=listen_start)`.
6. `SpeechPlaybackIntegration` воспроизводит сигнал и публикует `playback.started(signal=true)`.
7. `VoiceRecognitionIntegration` → `voice.recognition_started`.
8. `ListeningWorkflow` следит за debounce/таймаутами и при необходимости публикует `mode.request(SLEEPING)`.

Requirements:
- `voice.recording_start` публикуется до установки локальных флагов записи.
- `session_id` берется из `ApplicationStateManager`.
- Keyboard monitor работает в observe-only режиме (не блокирует системные шорткаты).

### 4.5 Processing Flow (LISTENING → PROCESSING → SLEEPING)

Coordinator: `ProcessingWorkflow`  
Source of Truth: `ProcessingWorkflow` состояние + EventBus события  

Sequence:
1. RELEASE → `voice.recording_stop` + `mode.request(PROCESSING)`.
2. `app.mode_changed(PROCESSING)` → `screenshot_capture_integration` делает `screenshot.captured|error`.
3. `grpc_client_integration` начинает запрос: `grpc.request_started`, затем поток `grpc.response.audio|text|action`.
4. `speech_playback_integration` публикует `playback.started`, затем `playback.completed|failed`.
5. `ProcessingWorkflow` по `grpc.request_completed` или `playback.completed` → `mode.request(SLEEPING)`.

Requirements:
- Нет фиксированных таймаутов завершения.
- `playback.cancelled` — единственный канал прерывания аудио.

### 4.6 Interrupt Flow

Coordinator: `InterruptManagementIntegration`  
Source of Truth: `InterruptCoordinator`  

Sequence:
1. `keyboard.short_press` или программный вызов публикует `interrupt.request`.
2. `InterruptManagementIntegration` при `type="speech_stop"` публикует `grpc.request_cancel`.
3. `SpeechPlaybackIntegration` при `grpc.request_cancel` публикует канонический `playback.cancelled` (без прямых side effects в этом шаге).
4. `SpeechPlaybackIntegration` обрабатывает `playback.cancelled` как единый owner cancel side effects.
5. Дополнительно публикуется `mode.request(SLEEPING)` как гарантия возврата.

Requirements:
- `interrupt.request.type` обязателен.
- `session_id` восстанавливается через `ApplicationStateManager` при отсутствии в payload.

### 4.7 Update Flow

Coordinator: `UpdaterIntegration`  
Source of Truth: `UpdaterIntegration` + state axis `update_in_progress`  

Sequence:
1. Триггер: `app.startup` (если `check_on_startup`), периодический таймер, или `updater.check_manual`.
2. Сначала `check_for_updates`; если нет обновлений → `updater.update_skipped`.
3. Если есть обновление → `updater.update_started`, затем прогресс `updater.download_progress`, `updater.install_progress`.
4. По завершению → `updater.update_completed`.
5. `relaunch_app` выполняется только если `USER_QUIT_INTENT=false`; при `USER_QUIT_INTENT=true` relaunch пропускается.
6. `updater.in_progress.changed` публикуется при изменении состояния (shadow-mode).

Requirements:
- `update_in_progress` блокирует permission_restart (через gateway).

### 4.8 Welcome Message Flow

Coordinator: `WelcomeMessageIntegration`  
Source of Truth: `WelcomeMessageIntegration`  

Sequence:
1. Триггеры: `app.startup`, `speech_playback.ready`.
2. `mode.request(PROCESSING)` для воспроизведения приветствия.
3. Отправка аудио в `SpeechPlaybackIntegration` и ожидание `playback.completed`.
4. `mode.request(SLEEPING)` по завершению или ошибке.

Requirements:
- Не дублировать запросы разрешений (это зона first-run).

### 4.9 Network Status Flow

Coordinator: `NetworkManagerIntegration`  
Source of Truth: `NetworkManager`  

Sequence:
1. На `app.startup` публикуется `network.status_snapshot`.
2. При изменениях сети публикуется `network.status_changed`.

### 4.10 VoiceOver Ducking Flow

Coordinator: `VoiceoverDuckingIntegration`  
Source of Truth: `VoiceOverController`  

Sequence:
1. На `app.mode_changed(LISTENING|PROCESSING)` — отключить VoiceOver.
2. На `app.mode_changed(SLEEPING)` — восстановить исходное состояние.

## 5) Запреты и совместимость

- Запрещено менять режим напрямую через `state_manager.set_mode()` вне `ModeManagementIntegration`.
- Запрещено вводить новые события без добавления в этот документ и без синхронизации с `STATE_CATALOG.md`.
- При добавлении новых полей в payload — документ должен быть обновлен синхронно.
