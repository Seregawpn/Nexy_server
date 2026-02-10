# Task Brief: quit timeout elimination and intent hardening

## Context
- После предыдущих изменений в логах оставался warning:
  - `quit_clicked dispatch timeout/error`
- Это означало, что UI callback Quit всё ещё зависел от таймаута ожидания async цепочки.

## Diagnosis
- `TrayController._on_quit_clicked` использовал блокирующий `future.result(timeout=0.5)`.
- Под нагрузкой startup/audio/гибридных событий callback не всегда завершался за 0.5s.
- Даже при корректной архитектуре это создавало ложный timeout и риск гонки.

## Change
- `modules/tray_controller/core/tray_controller.py`
  - удалено блокирующее ожидание `future.result(timeout=0.5)`,
  - dispatch `quit_clicked` теперь fire-and-forget через `run_coroutine_threadsafe(...)+done_callback`.
- `integration/integrations/tray_controller_integration.py`
  - добавлен import `StateKeys`,
  - в `_on_tray_quit` синхронно фиксируется `USER_QUIT_INTENT=True` в `StateManager` до async publish.

## Architecture fit
- Source of Truth сохранён: `StateManager`.
- Решение не вводит новый storage/state; усиливает существующий quit-path.
- Координатор остаётся владельцем lifecycle shutdown, integration обеспечивает ранний intent-ack.

## Verification
- `pytest -q tests/test_user_quit_ack.py` -> `2 passed`
- `pytest -q tests/verify_menu_quit_fix.py` -> `2 passed`

## Expected runtime outcome
- Должна исчезнуть строка `quit_clicked dispatch timeout/error`.
- При Quit должен стабильно фиксироваться `USER_QUIT_INTENT` до завершения приложения.
