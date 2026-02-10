# Task Brief: DONE signal no suppress on PROCESSING->SLEEPING

Date: 2026-02-10
Assistant: codex

## Goal
Не подавлять сигнал при переходе `PROCESSING -> SLEEPING`: cue должен активироваться всегда для валидного перехода с `session_id`.

## Root cause
`SignalIntegration` имел дополнительные suppress-guards (`recent error/cancel`, `same session as error/cancel`), из-за которых `DONE` пропускался даже при валидном переходе в `SLEEPING`.

## Changes
Files:
- `integration/integrations/signal_integration.py`
- `tests/test_signal_integration_cancel_done_suppression.py`

Implemented:
1. В `SignalIntegration._on_mode_changed` удалены suppress-guards для `DONE`:
   - `recent error`
   - `recent cancel`
   - `same session as last error`
   - `same session as last cancel`
2. Сохранены базовые архитектурные guard-условия:
   - только `prev_mode == PROCESSING`
   - обязательно наличие `session_id`
3. Обновлены тестовые ожидания:
   - `DONE` теперь ожидается даже после недавнего cancel/error при валидном `PROCESSING -> SLEEPING`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`

Result:
- `22 passed`

## Expected runtime effect
- При переходе `PROCESSING -> SLEEPING` сигнал `DONE` больше не подавляется внутренними suppress-окнами и стабильно воспроизводится.
