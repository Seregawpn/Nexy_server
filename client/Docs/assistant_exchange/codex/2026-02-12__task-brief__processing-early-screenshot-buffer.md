# Task Brief: processing early screenshot buffer (owner-side)

## Problem
`ProcessingWorkflow` мог зависать в `PROCESSING` без прогресса, если `screenshot.captured` приходил до активации workflow.  
Событие терялось из-за `not is_active()`/relevance-гейта, и цепочка оставалась на `CAPTURING`.

## Root cause
Race порядка событий: `app.mode_changed(processing)` и ранний `screenshot.captured` могли приходить в обратном порядке.

## Fix (centralized)
- Owner: `integration/workflows/processing_workflow.py`
- Добавлен owner-local буфер: `_pending_screenshot_by_session`.
- Если `screenshot.captured` приходит до `ACTIVE`, событие кэшируется по `session_id`.
- После старта цепочки (`_start_processing_chain`) pending-скриншот consume-ится и workflow сразу переходит `CAPTURING -> SENDING_GRPC`.

## Why architecture-safe
- Логика осталась в одном owner (`ProcessingWorkflow`).
- Новых путей принятия решений вне workflow не добавлено.
- Источник истины stage/state не размыт.

## Verification
- `PYTHONPATH=. pytest -q tests/test_processing_workflow_session_guard.py` -> `3 passed`
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_interrupt_playback.py` -> `21 passed`

## Regression coverage
- Добавлен тест:
  - `test_early_screenshot_is_buffered_and_consumed_on_processing_start`
  - Проверяет буферизацию раннего `screenshot.captured` и корректный переход в `SENDING_GRPC`.
