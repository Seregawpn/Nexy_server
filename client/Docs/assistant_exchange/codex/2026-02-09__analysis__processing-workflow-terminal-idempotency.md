# ProcessingWorkflow terminal idempotency guard

## Problem
В failure/interrupt потоках одна и та же session могла порождать повторные terminal-реакции:
- дубли `return_to_sleeping`,
- повторные `mode.request` при уже завершенном исходе.

## Root Cause
`ProcessingWorkflow` получал несколько terminal-событий почти одновременно
(`grpc.request_failed`, `playback.failed`, `interrupt.request`) и обрабатывал их как независимые.

## Change
- Файл: `integration/workflows/processing_workflow.py`
- Добавлены поля:
  - `_terminal_outcome_session_id`
  - `_terminal_outcome_reason`
- На старте новой processing-цепочки marker сбрасывается.
- В `_return_to_sleeping()`:
  - повторный terminal для той же session игнорируется (idempotency).
- В `_on_interrupt_request()` (ветка когда workflow не активен):
  - если interrupt уже относится к terminal-handled session, `mode.request` не публикуется повторно.

## Architecture Fit
- Source of truth terminal outcome централизован в owner-оркестраторе (`ProcessingWorkflow`).
- Решение не добавляет альтернативных каналов управления режимом.

## Verification
- `python3 -m py_compile integration/workflows/processing_workflow.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅
- `pytest -q tests/test_welcome_startup_sequence.py` ✅

## Expected Effect
- Одна terminal-реакция на одну session в processing-фазе.
- Меньше дублей mode transitions и побочных сигналов после failure/interruption.
