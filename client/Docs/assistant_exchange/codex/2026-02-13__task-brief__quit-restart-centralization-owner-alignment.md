# Task Brief: quit/restart centralization owner alignment

## Goal
Убрать межслойную связку coordinator -> restart handler и централизовать управление abort-маркером внутри restart-owner integration.

## Changes
1. Removed direct dependency from coordinator:
- `integration/core/simple_module_coordinator.py`
  - removed `PermissionsRestartHandler` import
  - removed direct `clear_user_quit_abort(...)` in initialize
  - removed direct `mark_user_quit_abort(...)` in `_on_user_quit`

2. Moved abort marker lifecycle to restart owner:
- `integration/integrations/permission_restart_integration.py`
  - subscribe to `tray.quit_clicked`
  - on start: `PermissionsRestartHandler.clear_user_quit_abort(source="permission_restart.start")`
  - on quit event: `PermissionsRestartHandler.mark_user_quit_abort(source="tray.quit_clicked")`
  - on app shutdown with user quit intent: mark abort again (idempotent safety)

3. Existing helper-side guard kept unchanged:
- `modules/permission_restart/macos/permissions_restart_handler.py`
  - helper checks `ABORT_FLAG` before `open -a` and skips launch.

## Result
- SoT/ownership cleaner: coordinator only owns state/event intent, restart integration owns restart abort control.
- No duplicate writer for `USER_QUIT_INTENT`.
- Detached helper launch cancellation remains centralized in restart owner path.

## Verification
- `pytest -q tests/test_user_quit_ack.py` -> 5 passed
- `PYTHONPATH=. pytest -q tests/test_tray_quit_dispatch.py` -> 3 passed
- `PYTHONPATH=. pytest -q tests/test_permission_restart_v2_freeze.py` -> 4 passed
