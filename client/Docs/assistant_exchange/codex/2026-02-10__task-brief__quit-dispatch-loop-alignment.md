# Task Brief: quit dispatch loop alignment

## Context
- В runtime логах сохранялся симптом: `quit_clicked dispatch timeout/error`.
- Это происходило после предыдущего fast-ack фикса в coordinator.

## Diagnosis
- `TrayController._on_quit_clicked` отправлял `quit_clicked` в loop, захваченный при `TrayController.initialize()`.
- Фактический EventBus/интеграции работают на `bg_loop` (`SimpleModuleCoordinator -> event_bus.attach_loop(self._bg_loop)`).
- Из-за mismatch loop событие из UI callback отправлялось не туда и таймаутилось.

## Change
- `modules/tray_controller/core/tray_controller.py`:
  - `self._main_loop` заменен на `self._dispatch_loop`,
  - добавлен API `set_dispatch_loop(loop)`,
  - `_on_quit_clicked` использует `self._dispatch_loop` для `run_coroutine_threadsafe(...)`.
- `integration/integrations/tray_controller_integration.py`:
  - сразу после создания `TrayController` проставляется dispatch loop:
    `tray_controller.set_dispatch_loop(event_bus.get_loop())`.

## Architecture fit
- Центр принятия решений не изменен: `tray.quit_clicked -> coordinator -> USER_QUIT_INTENT`.
- Исправлен только транспорт события между UI thread и владельцем EventBus loop.

## Verification
- `pytest -q tests/test_user_quit_ack.py` -> `2 passed`
- `pytest -q tests/verify_menu_quit_fix.py` -> `2 passed`

## Risk
- Низкий: изменение локализовано в quit dispatch path.
- Поведение остальных tray событий не изменено.
