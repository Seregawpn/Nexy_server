# Sleep Cue from mode_changed

## Что исправлено
- Добавлен fallback-сигнал `DONE` в `SignalIntegration` при переходе `app.mode_changed -> SLEEPING` из `LISTENING/PROCESSING`.
- Сохранена дедупликация: если уже был terminal-cue для той же `session_id`, повторный sleep-cue не эмитится.

## Изменения в коде
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/signal_integration.py`
  - `_on_mode_changed`: добавлена обработка `SLEEPING` + дедуп по `_last_terminal_session_id`.
- `/Users/sergiyzasorin/Fix_new/client/tests/test_signal_integration_cancel_done_suppression.py`
  - `test_sleep_done_emitted_on_mode_changed_without_processing_terminal`
  - `test_sleep_done_dedup_after_terminal_for_same_session`

## Проверка
- Команда: `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py`
- Результат: `9 passed`.

## Эффект
- Теперь при раннем `recognition_failed` (когда `processing.terminal` может не прийти) переход в `SLEEPING` всё равно даёт звуковой sleep-cue.
- Исключены дубли cue в сценарии, где и terminal, и mode_changed приходят для одной сессии.
