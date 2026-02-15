# Mode/Processing Lifecycle — полная карта взаимодействий и план исправления

Дата: 2026-02-15

## 1) Центры управления и владельцы
- Event routing: `integration/core/event_bus.py`
- Mode owner: `integration/integrations/mode_management_integration.py`
- State source of truth: `integration/core/state_manager.py`
- Processing orchestration: `integration/workflows/processing_workflow.py`
- Interrupt owner: `integration/integrations/interrupt_management_integration.py`
- Input lifecycle owner: `integration/integrations/input_processing_integration.py`
- Playback lifecycle owner: `integration/integrations/speech_playback_integration.py`
- Action lifecycle owner: `integration/integrations/action_execution_integration.py`

## 2) Ключевые точки соприкосновения событий
- `mode.request`:
  - publishers: InputProcessing, ProcessingWorkflow, InterruptManagement, WelcomeMessage, ModeManagement bridges
  - consumer: ModeManagementIntegration (central)
- `app.mode_changed`:
  - publisher: ApplicationStateManager (`set_mode`)
  - consumers: ProcessingWorkflow, ScreenshotCapture, ActionExecution, VoiceOverDucking, Tray, Signals, VoiceRecognition, Updater
- playback/browser/actions lifecycle:
  - `SpeechPlaybackIntegration` публикует `playback.started/completed/failed/cancelled`
  - `BrowserUseIntegration` публикует `browser.started/completed/failed/cancelled`
  - `ActionExecutionIntegration` публикует `actions.lifecycle.started/finished`
  - `ModeManagementIntegration` читает эти события и решает, когда можно `SLEEPING`
- interrupts:
  - `InputProcessingIntegration` публикует `interrupt.request`
  - `InterruptManagementIntegration` оркестрирует cancel и mode.request

## 3) Флаги/карты состояния (runtime)

### EventBus
- `_fast_events = {"app.mode_changed", "app.state_changed"}`
- `_background_tasks`

### ApplicationStateManager
- `current_mode`, `previous_mode`
- `current_session_id`
- `state_data` (typed keys)

### ModeManagementIntegration
- `_active_playback_sessions: set[str]`
- `_deferred_sleep_sessions: set[str]`
- `_active_browser_sessions: set[str]`
- `_active_action_sessions: dict[str, int]`
- `_pending_action_intents: dict[str, float]`
- `_mode_request_dedup_window_sec`
- `_last_mode_request_ts`, `_last_mode_request_id_ts`

### ProcessingWorkflow
- `current_stage`, `state`
- `current_session_id`
- `screenshot_captured`, `grpc_completed`, `playback_completed`, `browser_active`, `interrupted`, `grpc_started`, `recognition_failed`
- `_terminal_outcome_session_id`, `_terminal_outcome_reason`

### InputProcessingIntegration
- `_state` (PTT state machine)
- `_active_press_id`, `_terminal_stop_press_id`, `_preempt_sent_press_id`
- `_session_waiting_grpc`, `_active_grpc_session_id`, `_pending_session_id`
- `_recording_started`, `_mic_active`, `_playback_active`
- `_lifecycle_lock`

### InterruptManagementIntegration
- `_interrupt_dedup_window_sec`, `_last_interrupt_publish_ts`
- `_seen_interrupt_events` + TTL

### SpeechPlaybackIntegration
- `_playback_op_lock`
- `_terminal_event_by_session`
- `_finalized_sessions`, `_cancelled_sessions`
- `_had_audio_for_session`, `_grpc_done_sessions`
- `_current_session_id`, `_active_output_session_id`

### ActionExecutionIntegration
- `_actions_lock`
- `_active_actions`, `_active_apps`
- `_action_dedupe`

## 4) Подтвержденные архитектурные зазоры
1. `app.mode_changed` fire-and-forget в EventBus + подписчики с ожиданием последовательности.
2. Dual owner финального перехода в `SLEEPING`:
   - ProcessingWorkflow публикует `mode.request` на terminal path.
   - ModeManagementIntegration параллельно публикует `mode.request` по playback/browser/actions guards.
3. Legacy/compat paths в runtime:
   - `grpc.response.action` compatibility from `text_chunk_legacy`
   - gateway fallback_to=legacy
   - permission_restart legacy branches under freeze gate

## 5) План внедрения (минимальный, архитектурно совместимый)

### Phase 1 (безопасная детерминизация, low risk)
1. Убрать `app.mode_changed` из `_fast_events`.
2. Оставить `app.state_changed` в fast-path (если нужно для старых потребителей).
3. Прогнать targeted tests/лог-проверки на latency mode transitions.

### Phase 2 (single owner terminal sleep)
1. Назначить единственного owner финального `mode.request(target=SLEEPING)` — `ModeManagementIntegration`.
2. В `ProcessingWorkflow` оставить `processing.terminal` и cleanup, убрать terminal `mode.request` publish.
3. Сохранить idempotency guard по `session_id` в ModeManagementIntegration.

### Phase 3 (контрактные зачистки без ломающей миграции)
1. Зафиксировать `text_chunk_legacy` как временный bridge с telemetry и deadline удаления.
2. Для gateway fallback оставить только аварийный путь; добавить метрики срабатываний.
3. Для permission restart не менять V2 owner-path; legacy оставить frozen.

## 6) Критерии успешности
- Для одной `session_id` ровно один terminal sleep transition.
- Нет out-of-order эффектов между subscribers на `app.mode_changed`.
- Нет регрессий interrupt/cancel/restart.
- Снижение объема локальных guard-флагов в workflow-слое (без потери функциональности).
