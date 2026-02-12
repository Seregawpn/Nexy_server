# Task Brief: First-run completion must restart app (no deferred startup)

## Context
User explicitly required: after first-run permissions finish, app must restart (shutdown+relaunch), not continue by deferred module startup.

## Changes
1. `integration/core/simple_module_coordinator.py`
- Removed deferred-start orchestration path added earlier.
- On `permissions.first_run_completed` in restricted first-run mode, coordinator now requests restart via PermissionRestartIntegration.
- If restart cannot be scheduled, writes explicit warning logs.

2. `integration/integrations/permission_restart_integration.py`
- Added public method:
  - `request_restart_after_first_run_completed(session_id: str | None) -> bool`
- Method applies existing guards (disabled, no handler, user quit, updater busy, duplicate/recent restart) and schedules restart via existing `_execute_scheduled_restart` pipeline.

## Verification
- `python3 -m py_compile integration/core/simple_module_coordinator.py integration/integrations/permission_restart_integration.py` passed.

## Expected behavior
After `permissions.first_run_completed` during first-run restricted startup:
- No deferred start of input/voice modules in current process.
- Restart is scheduled and executed by PermissionRestartIntegration.
- Next launch should start as post-first-run flow.
