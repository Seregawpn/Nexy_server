# Task Brief: quit relaunch abort marker and single writer

## What changed
- Added centralized persistent `restart_abort.flag` owner API in `PermissionsRestartHandler`:
  - `mark_user_quit_abort(...)`
  - `clear_user_quit_abort(...)`
  - `is_user_quit_abort_active()`
- Added helper pre-launch guard in `_spawn_delayed_launch_helper`:
  - checks `ABORT_FLAG` right before `open -a`
  - skips launch when marker exists
- Wired lifecycle:
  - `SimpleModuleCoordinator.initialize()` clears stale marker
  - `SimpleModuleCoordinator._on_user_quit()` sets marker before quit intent state update
- Removed duplicate quit-intent writer from `TrayControllerIntegration._on_tray_quit`
  - now only publishes `tray.quit_clicked`

## Why
- Detached permission restart helper could relaunch app after manual quit.
- Runtime guards did not cancel already spawned helper process.
- `USER_QUIT_INTENT` had duplicate writers.

## Validation
- `pytest -q tests/test_user_quit_ack.py` -> 5 passed
- `PYTHONPATH=. pytest -q tests/test_tray_quit_dispatch.py` -> 3 passed
- `PYTHONPATH=. pytest -q tests/test_permission_restart_v2_freeze.py` -> 4 passed

## Runtime DoD to verify manually
1. Trigger scenario where restart helper may be scheduled.
2. Click Quit from tray.
3. Confirm no post-quit `logger launching: /usr/bin/open -a /Applications/Nexy.app`.
4. Confirm helper logs skip due to abort marker.
