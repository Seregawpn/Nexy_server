# Task Brief: Deferred startup after permissions completion (mic activation fix)

## Context
User reported that after first-run permissions flow completed, mic activation still "skipped" and input path did not work.

## Diagnosis
`SimpleModuleCoordinator.start()` used `restrict_to_permissions=True` and returned early after starting only permission flow modules.
On `permissions.first_run_completed`, coordinator only updated state and did not start deferred integrations (`input`, `voice_recognition`, etc.).

## Changes
- File: `integration/core/simple_module_coordinator.py`
- Added coordinator-owned deferred startup state:
  - `_deferred_start_task`
  - `_permissions_restricted_startup`
  - `_started_integrations`
  - `_workflows_started`
- In `start()`:
  - track restricted mode and started modules
  - mark `is_running=True` in restricted mode before early return
- In `_on_permissions_completed()`:
  - schedule single-flight deferred startup task
- Added `_start_deferred_integrations_after_permissions()`:
  - start missing integrations in factory order
  - start remaining integrations not in order
  - start workflows once
  - publish `app.startup` after deferred startup
  - clear restricted mode

## Verification
- `python3 -m py_compile integration/core/simple_module_coordinator.py` passed.

## Expected runtime effect
After `permissions.first_run_completed`, logs should show `🚀 Дозапуск input`, `🚀 Дозапуск voice_recognition` and related module starts, then mic activation should no longer skip due to missing started integrations.
