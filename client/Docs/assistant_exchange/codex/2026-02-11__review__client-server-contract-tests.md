# Client-Server Contract Tests

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-11
- ID (INS-###): INS-UNKNOWN

## Diagnosis
После contract-hardening требовалась проверка, что не осталось скрытых вторых путей в action/cancel и что core регрессии не затронуты.

## Root Cause
Новые ограничения контракта (action_message-only, session-scoped cancel, interrupt-only runtime cancel) должны быть закреплены тестами, иначе возможен откат поведения при следующих изменениях.

## Optimal Fix
Добавлены 3 узких теста и прогнан целевой набор:
- `test_grpc_ignores_action_like_text_chunk_contract`
- `test_grpc_request_cancel_requires_session_id`
- `test_action_execution_cancel_trigger_is_interrupt_only`

Файл:
- `tests/test_client_server_flow_contracts.py`

## Verification
Команда:
`PYTHONPATH=. pytest tests/test_client_server_flow_contracts.py tests/test_interrupt_playback.py tests/test_mode_management_mode_request_dedup.py tests/test_centralization_regressions.py`

Результат:
- `30 passed`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: canonical root/client DOCS_INDEX + PRE_CHANGE_CHECKLIST + FLOW_INTERACTION_SPEC + ARCHITECTURE_OVERVIEW + PROJECT_REQUIREMENTS + FEATURE_FLAGS.
- Source of Truth: `GrpcClientIntegration`, `InterruptManagementIntegration`, `ActionExecutionIntegration`, `FLOW_INTERACTION_SPEC`.
- Дублирование: покрыто тестами (legacy action path, keyboard short-press cancel path).
- Feature Flags check: новые флаги не вводились.
- Race check: добавлен test guard на session-scoped cancel.

## Запрос/цель
Закрепить изменения тестами и подтвердить отсутствие регрессий в целевом наборе.

## Контекст
- Файлы: `tests/test_client_server_flow_contracts.py`, `integration/integrations/grpc_client_integration.py`, `integration/integrations/action_execution_integration.py`, `integration/integrations/interrupt_management_integration.py`, `integration/core/event_bus.py`.

## Решения/выводы
- Контрактные изменения подтверждены тестами.
- Целевые regression-наборы прошли без падений.

## Открытые вопросы
- Нужен ли отдельный тест на deterministic ordering `app.mode_changed` subscribers в `EventBus`.

## Следующие шаги
- При желании добавить отдельный stress-test на ordering для `app.mode_changed`.
