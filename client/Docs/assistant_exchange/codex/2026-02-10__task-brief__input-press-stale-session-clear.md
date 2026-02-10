# Task Brief: input press stale session clear

## Problem
В логах после завершения/ошибки цикла на новом `PRESS` в `idle/sleeping` оставался stale `session_id` прошлого цикла:
- `PRESS_PREEMPT ... sid=<old_sid> state=idle`
- `PTT_STATE: idle -> armed ... session=<old_sid>`

Это создавало ложный контекст в новом press-cycle.

## Root cause
`InputProcessingIntegration._handle_press` брал `session_id` из `state_manager` до preempt-решения, но не очищал его в safe-idle сценарии, где preempt не нужен.

## Fix
Файл: `integration/integrations/input_processing_integration.py`
- В `_handle_press` добавлен guard:
  - если `should_preempt == False`, состояние `IDLE`, и есть `preempt_session_id`, то:
    - принудительно очищаем session через `_set_session_id(None, "press_stale_session_clear")`
    - локально обнуляем `preempt_session_id`.

## Tests
Файл: `tests/test_interrupt_playback.py`
- Усилен тест `test_press_does_not_publish_interrupt_when_sleeping_with_stale_session`:
  - добавлена проверка, что после `PRESS` stale session очищен (`state_manager.get_current_session_id() is None`).

## Validation
Команда:
`PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Результат:
- `24 passed`
