# Task Brief: race/duplication hardening for first-run, welcome, and restart

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
User requested elimination of remaining conflict/race/duplication points around first-run permissions, restart logic, and startup greeting.

## Implemented changes

1. First-run timeout waiter lifecycle made managed (single-flight + stop-cancel)
- File: `integration/integrations/first_run_permissions_integration.py`
- Added `self._timeout_wait_task` as owned task handle.
- In timeout mode, `start()` now reuses active waiter instead of creating duplicates.
- `stop()` now cancels and awaits waiter cancellation.
- `_await_timeout_completion()` now clears handle in `finally`.

2. Welcome trigger centralized
- File: `integration/integrations/welcome_message_integration.py`
- Removed subscription to `permissions.first_run_completed`.
- `_on_first_run_completed` changed to explicit no-op log (no welcome playback request).
- Effective owner for welcome trigger remains `system.ready_to_greet`.

3. Final restart revalidation before trigger
- File: `integration/integrations/permission_restart_integration.py`
- In `_execute_scheduled_restart(...)`, added final guards after delay and before `trigger_restart`:
  - abort if recent restart flag/cached restarted session is detected;
  - abort if `first_run` is still active while `restart_pending` is not set.

4. Coordinator duplicate cleanup
- File: `integration/core/simple_module_coordinator.py`
- Removed duplicated error log line in anti-TAL exception branch.
- Removed duplicated `get_tray_controller()` call.

## Tests added/updated
- Added: `tests/test_first_run_timeout_task_lifecycle.py`
  - `test_timeout_wait_task_cancelled_on_stop`
  - `test_timeout_wait_task_single_flight_when_already_active`
- Updated: `tests/test_restart_pending_state_keys.py`
  - `test_permission_restart_aborts_if_first_run_active_without_restart_pending_before_trigger`
  - `test_permission_restart_aborts_if_recent_restart_flag_detected_before_trigger`
- Updated: `tests/test_welcome_startup_sequence.py`
  - `test_first_run_completed_event_is_noop_for_welcome_trigger`

## Validation
- `pytest -q tests/test_welcome_startup_sequence.py tests/test_restart_pending_state_keys.py tests/test_first_run_timeout_task_lifecycle.py tests/test_gateways.py`
  - Result: `24 passed`
- `python3 -m py_compile ...` on modified python files
  - Result: OK

## Outcome
- Reduced duplicate trigger paths and background-task leaks.
- Added revalidation guard against out-of-order restart execution.
- Preserved centralized ownership model (V2 orchestrator / coordinator state keys).
