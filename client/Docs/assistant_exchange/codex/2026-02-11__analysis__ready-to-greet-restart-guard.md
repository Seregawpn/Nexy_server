# Task
Suppress `system.ready_to_greet` in the same pre-restart first-run process when centralized restart is already scheduled.

# Diagnosis
- `permissions.first_run_completed` schedules restart in restricted startup mode, but V2 integration still publishes `system.ready_to_greet` immediately.
- This creates a duplicate pre-restart side effect path (welcome flow before relaunch).

# Implemented Fix
1. Added centralized state key:
   - `integration/core/state_keys.py`
   - `StateKeys.FIRST_RUN_RESTART_SCHEDULED`
2. Centralized owner writes scheduling state:
   - `integration/integrations/permission_restart_integration.py`
   - Added `_set_first_run_restart_scheduled(value)` and `_attach_restart_task(task)`
   - Set key `True` when restart task is scheduled.
   - Reset key to `False` on process startup and on restart task completion callback.
3. V2 guard before greet publishing:
   - `modules/permissions/v2/integration.py`
   - Added optional `state_manager` dependency.
   - In `_publish_ready_to_greet`, skip publish when `FIRST_RUN_RESTART_SCHEDULED=True`.
4. Passed state manager into V2 integration:
   - `integration/integrations/first_run_permissions_integration.py`

# Tests
- Updated:
  - `tests/test_restart_pending_state_keys.py`
    - `test_permission_restart_marks_first_run_restart_scheduled_state`
- Added:
  - `tests/test_permissions_v2_ready_to_greet_guard.py`
    - skip publish when restart scheduled
    - publish when not scheduled

# Verification
- `python3 -m py_compile` on touched files: OK
- `PYTHONPATH=. pytest -q tests/test_restart_pending_state_keys.py tests/test_permissions_v2_ready_to_greet_guard.py tests/test_event_ownership_contract.py`: **13 passed**
- Extended targeted pack earlier: **31 passed**

# Result
- Single owner for restart scheduling state: `PermissionRestartIntegration`.
- `system.ready_to_greet` is no longer published in pre-restart process when restart is already planned.
- Duplicate first-run side effects are reduced; flow remains architecture-aligned and centralized.
