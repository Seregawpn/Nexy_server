# Single-Shot First-Run Restart Latch

## Context
- Need: restart after first-run must happen once and not be scheduled repeatedly.
- Existing flow already centralized through `PermissionRestartIntegration`.

## Change
- File: `integration/integrations/permission_restart_integration.py`
- Function: `request_restart_after_first_run_completed`
- Added:
  - Set `_was_restarted_this_session = True` immediately after scheduling restart task.
  - Log marker: `First-run restart latch set (single-shot per session)`.

## Why
- Prevents duplicate scheduling if completion events are repeated/out-of-order in the same session.
- Keeps one restart owner and one decision path.

## Validation
- `python3 -m py_compile` passed for modified files.
- `rg` confirms single centralized request path remains:
  - coordinator -> `request_restart_after_first_run_completed` -> `PermissionsRestartHandler.trigger_restart`.
