# Permissions Restart Event Order Fix

## Context
- Symptoms: restart after first-run permissions looked delayed/absent; `system.ready_to_greet` processing could run before centralized restart scheduling.
- Scope: V2 permissions integration event emission order.

## Change
- File: `modules/permissions/v2/integration.py`
- Function: `_emit_event`
- Update:
  - Publish legacy event (`permissions.first_run_completed` / `permissions.first_run_failed`) first.
  - Publish `system.ready_to_greet` after legacy event.

## Why
- Centralized restart scheduling is bound to legacy completion path in coordinator + `PermissionRestartIntegration`.
- If greeting runs first, restart scheduling can be delayed by greeting pipeline/waits.

## Expected Effect
- Faster and deterministic restart scheduling after first-run completion.
- No new owner introduced; restart remains centralized in `PermissionRestartIntegration`.

## Validation
- `python3 -m py_compile modules/permissions/v2/integration.py` passed.
