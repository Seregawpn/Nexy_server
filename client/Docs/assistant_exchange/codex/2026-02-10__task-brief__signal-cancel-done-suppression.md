# Task Brief: signal cancel->done suppression

## Context
- После `playback.cancelled` сразу шёл переход `PROCESSING -> SLEEPING`, и `SignalIntegration` публиковал `DONE`.
- Это создавало конфликтный хвост cue: `CANCEL` и затем `DONE` в одном коротком окне.

## Changes
- Обновлен `/Users/sergiyzasorin/Fix_new/client/integration/integrations/signal_integration.py`:
  - Добавлено окно подавления `DONE` после `CANCEL`: `_cancel_to_done_suppress_sec = 0.8`.
  - В `_on_mode_changed` при переходе в `SLEEPING` добавлен guard:
    - если `now - _last_cancel_ts < _cancel_to_done_suppress_sec`, `DONE` не публикуется.
  - Логика централизована в owner сигналов (`SignalIntegration`), другие интеграции не менялись.

## Tests
- Добавлен файл `/Users/sergiyzasorin/Fix_new/client/tests/test_signal_integration_cancel_done_suppression.py`:
  - `test_done_suppressed_after_recent_cancel`
  - `test_done_emitted_on_sleeping_without_recent_cancel`

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py` → `2 passed`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py tests/test_user_quit_ack.py tests/test_signal_integration_cancel_done_suppression.py` → `14 passed`

## Result
- Устранён конфликтный сценарий `CANCEL` + `DONE` в одном хвосте после прерывания.
- Нормальный `DONE` при обычном завершении (без недавнего cancel) сохранён.
