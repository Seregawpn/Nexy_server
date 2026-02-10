# Task Brief: user quit fast-ack and background shutdown

## Context
- После предыдущего фикса в логах оставался симптом: `quit_clicked dispatch timeout/error`.
- Источник: `tray.quit_clicked` ожидал слишком длинный обработчик в `SimpleModuleCoordinator._on_user_quit`.

## Diagnosis
- `_on_user_quit` выполнял блокирующую цепочку: `publish(app.shutdown)` + `await stop()`.
- При этом tray callback ожидал completion события, и таймаут срабатывал до безопасного завершения обработчика.

## Change
- В `integration/core/simple_module_coordinator.py` реализован fast-ack путь:
  - `_on_user_quit` теперь:
    - идемпотентно проверяет `USER_QUIT_INTENT`,
    - немедленно выставляет `USER_QUIT_INTENT=True`,
    - логирует `QUIT_ACK`,
    - отправляет `app.shutdown` best-effort в фоновой задаче без блокировки.
  - Убран `await self.stop()` из user-quit обработчика.
  - Добавлено поле `self._user_quit_task` для контроля фоновой публикации.

## Architecture fit
- Source of Truth сохранён: `StateManager[USER_QUIT_INTENT]`.
- Не добавлен новый путь управления рестартом; изменения только в существующем lifecycle owner (`SimpleModuleCoordinator`).
- Тяжелый shutdown остаётся в `run().finally` после выхода из `app.run()`.

## Tests
- Добавлен тест: `tests/test_user_quit_ack.py`
  - `test_user_quit_ack_is_non_blocking`
  - `test_user_quit_ack_is_idempotent`
- Прогон:
  - `pytest -q tests/test_user_quit_ack.py` → `2 passed`
  - `pytest -q tests/verify_menu_quit_fix.py` → `2 passed`

## Risk
- Низкий: логика затронута только в quit-path coordinator.
- Потенциальный побочный эффект: `app.shutdown` из user-quit стал best-effort (асинхронно), но полный shutdown по-прежнему гарантируется через `run().finally`.
