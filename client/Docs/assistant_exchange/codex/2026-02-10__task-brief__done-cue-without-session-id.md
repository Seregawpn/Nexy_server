# Task Brief: DONE cue without session_id on PROCESSING->SLEEPING

Date: 2026-02-10
Assistant: codex

## Goal
Сделать `DONE` сигнал стабильным при переходе `PROCESSING -> SLEEPING`, даже когда `app.mode_changed` приходит без `session_id` (типично для interrupt-пути).

## Root cause
`SignalIntegration` требовал `session_id` для `DONE`.  
В interrupt-сценарии mode switch в `SLEEPING` может публиковаться без `session_id`, из-за чего сигнал пропускался (`DONE skipped (missing session_id)`).

## Changes
Files:
- `integration/integrations/signal_integration.py`
- `tests/test_signal_integration_cancel_done_suppression.py`

Implemented:
1. Удален guard `missing session_id` для `DONE`.
2. Сохранен основной guard: `DONE` только при `prev_mode == PROCESSING`.
3. Обновлен тест:
   - `test_done_skipped_on_sleeping_without_session_id` -> `test_done_emitted_on_sleeping_without_session_id`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`

Result:
- `22 passed`

## Expected runtime effect
- В interrupt-переходах `PROCESSING -> SLEEPING` сигнал `DONE` больше не теряется из-за отсутствующего `session_id`.
