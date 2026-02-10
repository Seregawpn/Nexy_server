# Task Brief: suppress ERROR when processing terminal path is active

Date: 2026-02-10
Assistant: codex

## Goal
Устранить сценарий, где при `PROCESSING -> SLEEPING` сигнал `DONE` не слышен из-за предшествующего `ERROR`.

## Root cause
`voice.recognition_failed` обрабатывался после запроса перехода в SLEEPING.  
На момент `_on_error_like` текущий mode уже мог быть `SLEEPING`, поэтому старый guard `current_mode == PROCESSING` не срабатывал, и публиковался `ERROR`, после которого сразу публиковался `DONE`.

## Changes
Files:
- `integration/integrations/signal_integration.py`
- `tests/test_signal_integration_cancel_done_suppression.py`

Implemented:
1. Усилен guard в `_on_error_like`:
   - `ERROR` подавляется, если `current_mode == PROCESSING` **или** `self._last_mode == PROCESSING`.
   - это покрывает гонку, когда mode уже переключился в `SLEEPING`, но terminal path начался из `PROCESSING`.
2. Добавлен тест:
   - `test_error_deferred_when_last_mode_processing_even_if_sleeping_now`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`

Result:
- `24 passed`

## Expected runtime effect
- В terminal processing path не публикуется `ERROR`, остается слышимый `DONE` на `PROCESSING -> SLEEPING`.
