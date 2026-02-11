# Runtime Duplication/Race Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): INS-UNASSIGNED

## Diagnosis
Обнаружены 3 архитектурных риска: sessionless cancel fallback, sessionless mode.request в interrupt-path и нецентрализованный screenshot session routing через `_last_session_id`.

## Root Cause
Локальные fallback-механизмы и дублирующие пути принятия решений обходят строгий session-scoped контракт (`session_id` как SoT) и создают out-of-order/нецелевые side effects.

## Optimal Fix
Цель: убрать конфликтующие ветки cancel/screenshot и оставить один детерминированный путь по session_id.

Где в архитектуре:
- `InterruptManagementIntegration` (owner cancel orchestration)
- `GrpcClientIntegration` (owner gRPC cancel delivery)
- `ScreenshotCaptureIntegration` (owner screenshot routing/publish)
- `ModeManagementIntegration` + `ApplicationStateManager` (owner mode transition)

Source of Truth:
- `ApplicationStateManager.current_session_id` + payload `session_id` в контрактах `FLOW_INTERACTION_SPEC.md`.

План внедрения:
1. Убрать fallback отмены “latest inflight” в `GrpcClientIntegration._on_request_cancel`; при отсутствии `session_id` — reject + log + metric.
2. Прокинуть `session_id` в `InterruptManagementIntegration._handle_speech_stop -> mode.request`.
3. В `ScreenshotCaptureIntegration` читать `session_id` из события `app.mode_changed` (payload), `_last_session_id` оставить только fallback с явным guard и reason.
4. Закрепить idempotency для `screenshot.captured`: один publish на session_id; re-publish только при explicit `replay_reason`.
5. Добавить тесты гонок: cancel без session_id, concurrent inflight sessions, mode_changed(PROCESSING) с рассинхроном `_last_session_id`.

Code Touchpoints:
- `integration/integrations/grpc_client_integration.py::_on_request_cancel`
- `integration/integrations/interrupt_management_integration.py::_handle_speech_stop`
- `integration/integrations/screenshot_capture_integration.py::_on_mode_changed`
- `tests/*` (race/idempotency contracts)

Concurrency Guard:
- state-guard + idempotency + coordinator (session_id-required contract).

What to remove / merge:
- Remove: sessionless cancel fallback (`latest inflight`).
- Merge: screenshot routing to single owner rule `session_id from event payload`.

## Verification
- Проверка: `interrupt.request` без `session_id` не должен завершать чужую inflight-сессию.
- Проверка: `mode.request` из interrupt всегда содержит `session_id`.
- Проверка: при раннем screenshot не появляется дублированный publish для той же session_id без `replay_reason`.
- Логи: no `grpc.request_cancel missing session_id; fallback to latest inflight`.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`; `Docs/DOCS_INDEX.md`; `Docs/PRE_CHANGE_CHECKLIST.md`; `Docs/PROJECT_REQUIREMENTS.md` (REQ-001/003/007/009/024/025); `Docs/ARCHITECTURE_OVERVIEW.md` (централизация mode/session/cancel); `Docs/FEATURE_FLAGS.md`; `Docs/FLOW_INTERACTION_SPEC.md` (разделы 2, 3.1, 3.5, 4.5, 4.6); `Docs/STATE_CATALOG.md` (оси `appMode`, `session_id`, `update_in_progress`); `../Docs/DOCS_INDEX.md`; `../Docs/PRE_CHANGE_CHECKLIST.md`; `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`; `../Docs/ANTIGRAVITY_PROMPT.md`; `../Docs/CODEX_PROMPT.md`; `../Docs/assistant_exchange/TEMPLATE.md`.
- Source of Truth: `ApplicationStateManager` + event payload contract (`session_id`) + `ModeManagementIntegration` owner mode changes.
- Дублирование: обнаружены параллельные screenshot-trigger paths (`voice.recording_stop` и `app.mode_changed`) с привязкой к `_last_session_id`; требуется merge к payload-driven routing.
- Feature Flags check: новых/измененных флагов нет.
- Race check: подтверждён риск sessionless cancel/mode-request в concurrent inflight.

## Запрос/цель
Проверить наличие дублей/конфликтов/гонок и проблем передачи данных server->client/client runtime.

## Контекст
- Файлы: `integration/core/event_bus.py`, `integration/integrations/grpc_client_integration.py`, `integration/integrations/interrupt_management_integration.py`, `integration/integrations/screenshot_capture_integration.py`, `integration/integrations/mode_management_integration.py`.
- Ограничения: без реархитектуры, только внутри текущих owners/coordinators.

## Решения/выводы
- Риски подтверждены статическим аудитом кода; приоритет исправления — cancel/mode session contract, затем screenshot routing.

## Открытые вопросы
- Нужен ли строгий reject `grpc.request_cancel` без `session_id` во всех environments или только в production profile.

## Следующие шаги
- Подготовить patch с 3 изменениями и минимальным набором regression-тестов.
