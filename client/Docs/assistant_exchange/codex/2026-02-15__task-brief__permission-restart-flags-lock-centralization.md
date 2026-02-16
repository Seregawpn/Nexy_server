# Task Brief: Permission Restart Flags/Lock Centralization

## Context
- Observed mixed control paths for restart control files (`restart_abort.flag`, `restart_in_progress.lock`, `restart_completed.flag`) across `Nexy` and `Nexy-Dev` directories.
- Shutdown/Quit flow could leave stale restart lock files that were not proactively cleaned in normal lifecycle paths.

## Changes
1. Centralized restart control directory resolution in `PermissionsRestartHandler`:
- Replaced hardcoded `get_user_data_dir("Nexy")` with runtime `get_user_data_dir()` in class/instance paths.
- Aligns dev runs with `Nexy-Dev` and packaged runs with `Nexy`.

2. Added safe stale-lock cleanup API in owner module:
- New method: `PermissionsRestartHandler.cleanup_stale_restart_lock(source=...)`.
- Guardrails:
  - no cleanup if current process holds restart lock fd,
  - no cleanup if lock is actively held by another process,
  - removes file only when advisory lock is acquired and owner PID is dead/malformed.

3. Wired cleanup into centralized lifecycle owner (`PermissionRestartIntegration`):
- `permission_restart.start`
- `app.shutdown`
- `tray.quit_clicked`
- `permission_restart.stop`

## Files touched
- `modules/permission_restart/macos/permissions_restart_handler.py`
- `integration/integrations/permission_restart_integration.py`
- `tests/test_permission_restart_handler_lock_hygiene.py`

## Verification
- Ran:
  - `PYTHONPATH=. pytest -q tests/test_permission_restart_handler_lock_hygiene.py tests/test_permission_restart_v2_freeze.py tests/test_centralization_regressions.py`
- Result: `9 passed`

## Expected impact
- Single runtime owner directory for restart control artifacts.
- Lower false stale-lock noise after normal Quit/Shutdown.
- No additional state owners introduced; restart control remains centralized in PermissionRestart handler/integration.
