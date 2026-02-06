# Task Brief: architecture normalization follow-up (duplicates/races)

## What changed

1. `integration/core/simple_module_coordinator.py`
- Deferred startup one-shot is now **retry-safe**.
- `_deferred_start_completed` is set to `True` only when deferred startup finishes without failures.
- If some integrations/workflows fail to start, gate remains open for safe retry on next trigger.

2. `integration/integrations/permission_restart_integration.py`
- Removed duplicated V2 guard branches in `_on_first_run_restart_pending`.
- Added explicit relaunch arbitration with updater:
  - scheduled permission restart is aborted if updater is currently active.
  - scheduled restart task is cancelled when `updater.update_started` arrives.

3. Existing fixes kept in place
- `modules/instance_manager/core/instance_manager.py`: packaged-process duplicate detection fixed.
- `modules/permissions/v2/orchestrator.py`: one auto-restart max per first-run cycle (`restart_count >= 1` guard).

## Why
- Prevent duplicate/competing side effects (double relaunch, repeated start paths).
- Preserve centralized ownership:
  - deferred startup owner: coordinator
  - relaunch owner during update: updater
  - restart policy owner: V2 ledger

## Validation
- `python3 -m py_compile integration/core/simple_module_coordinator.py integration/integrations/permission_restart_integration.py modules/permissions/v2/orchestrator.py modules/instance_manager/core/instance_manager.py`

## Expected runtime behavior
- No repeated Nexy process spawning.
- At most one permission-driven auto-restart in first-run cycle.
- No permission-restart relaunch while updater is in active update phase.
- Deferred startup does not get permanently "completed" after partial failure.
