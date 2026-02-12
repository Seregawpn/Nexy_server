# Task
Fix strict first-run lifecycle bug where `_running` could remain `True` after `start() -> False`.

# Diagnosis
After strict policy changes, `FirstRunPermissionsIntegration.start()` gained real failure paths.
`_running` was set to `True` before work and not reset on failure, causing sticky state.

# Implemented Fix
- File: `integration/integrations/first_run_permissions_integration.py`
- Added `success` lifecycle guard and `finally` reset:
  - `_running` remains `True` only on successful start.
  - `_running` is reset to `False` for strict failures and exceptions.

# Tests
- Added: `tests/test_first_run_strict_lifecycle.py`
  - `test_strict_start_resets_running_when_completion_is_false`
  - `test_strict_start_resets_running_when_v2_start_raises`
- Verified with:
  - `tests/test_first_run_strict_lifecycle.py`
  - `tests/test_first_run_timeout_task_lifecycle.py`
  - `tests/test_permissions_completed_state.py`
  - `tests/test_coordinator_critical_subscriptions.py`

# Result
- `11 passed`
- Strict mode now blocks startup correctly without leaving integration in a false running state.
