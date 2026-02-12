# Task Brief: Quit/shutdown ack hardening and restart race guards

## Goal
Снизить риск ошибочного повторного запуска после выключения приложения пользователем.

## Key fixes

1. Quit dispatch hardening in tray controller
- File: `modules/tray_controller/core/tray_controller.py`
- Changes:
  - увеличен timeout ожидания подтверждения dispatch `quit_clicked` с `0.5s` до `2.0s`;
  - добавлен sync fallback, если нет running asyncio loop: callback `quit_clicked` вызывается напрямую (`asyncio.run(...)` для coroutine callback).
- Effect:
  - меньше шансов потерять `quit_clicked` событие до фактического `quit()`.

2. app.shutdown payload now carries user intent in coordinator stop
- File: `integration/core/simple_module_coordinator.py`
- Changes:
  - при `stop()` в payload `app.shutdown` добавлены:
    - `source: "coordinator.stop"`
    - `user_initiated: <from StateKeys.USER_QUIT_INTENT>`
- Effect:
  - downstream guards (autostart/updater/restart) получают единый признак пользовательского выхода даже в пограничных путях.

## Added tests

1. `tests/test_tray_quit_dispatch.py`
- updated expectation: timeout = `2.0s`
- added test:
  - `test_quit_fallback_dispatch_when_no_loop_available`
  - verifies sync fallback publishes `quit_clicked` callback and still exits tray.

2. `tests/test_coordinator_shutdown_user_initiated.py`
- new test:
  - `test_stop_publishes_user_initiated_shutdown_payload`
  - verifies `coordinator.stop()` publishes `app.shutdown` with `user_initiated=True` when quit intent is set.

## Verification
Executed:
- `pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py tests/test_permissions_completed_state.py tests/test_coordinator_shutdown_user_initiated.py`
- `python3 -m py_compile modules/tray_controller/core/tray_controller.py integration/core/simple_module_coordinator.py tests/test_tray_quit_dispatch.py tests/test_coordinator_shutdown_user_initiated.py`

Result:
- tests: `9 passed`
- note: one pre-existing RuntimeWarning in tray dispatch tests about un-awaited coroutine mock path (non-blocking warning)
- py_compile: OK
