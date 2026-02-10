# Signal DONE gate: processing/session

## Context
Проблема: сигнал иногда срабатывал при входе в SLEEPING не по завершению рабочей сессии, и поведение выглядело нестабильным.

## Change
- Файл: `integration/integrations/signal_integration.py`
- Изменено правило `DONE` в `_on_mode_changed`:
  - `DONE` теперь публикуется только при `PROCESSING -> SLEEPING`
  - и только если есть `session_id`
  - переходы в `SLEEPING` без `session_id`/не из `PROCESSING` пропускаются.

## Why
- Убран ложный DONE при пассивных/служебных переходах в sleep.
- Сохранён единый владелец сигналов (SignalIntegration через `app.mode_changed`).
- Исключён второй путь и локальные обходы.

## Tests
- Обновлён: `tests/test_signal_integration_cancel_done_suppression.py`
  - `test_done_emitted_on_sleeping_without_recent_cancel` -> теперь с `session_id`
  - Добавлен `test_done_skipped_on_sleeping_without_session_id`
- Прогон:
  - `tests/test_signal_integration_cancel_done_suppression.py`
  - `tests/test_interrupt_playback.py::TestInterruptPlayback::test_playback_signal_skips_listen_start_outside_listening`
  - `tests/test_mode_management_mode_request_dedup.py`
- Result: 9 passed.
