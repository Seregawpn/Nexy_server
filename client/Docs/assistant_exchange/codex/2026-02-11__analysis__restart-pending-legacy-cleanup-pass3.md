# Task
Remove remaining runtime `restart_pending` dependencies that could cause confusion/duplicate logic paths.

# Changes
1. `AutostartManagerIntegration` policy cleanup:
   - File: `integration/integrations/autostart_manager_integration.py`
   - Removed selector dependency `is_restart_pending(...)`.
   - Replaced with centralized key check:
     - `StateKeys.FIRST_RUN_RESTART_SCHEDULED`
   - New blocked reason: `first_run_restart_scheduled`.

2. `PermissionRestartIntegration` runtime guard cleanup:
   - File: `integration/integrations/permission_restart_integration.py`
   - Removed conditions tied to legacy axis:
     - `snapshot.first_run and not snapshot.restart_pending` -> `snapshot.first_run`
   - Updated logs accordingly (no `restart_pending` in runtime decision output).
   - Result: no behavioral dependency on deprecated `restart_pending`.

3. Tests:
   - File: `tests/test_autostart_repair_policy.py`
   - Removed monkeypatching of `is_restart_pending`.
   - Added test:
     - `test_should_not_repair_when_first_run_restart_scheduled`.

# Verification
- `python3 -m py_compile` on changed files: OK
- `PYTHONPATH=. pytest -q tests/test_autostart_repair_policy.py tests/test_restart_pending_state_keys.py tests/test_permissions_v2_ready_to_greet_guard.py tests/test_gateways.py tests/test_centralization_regressions.py`
- Result: `31 passed`.

# Remaining legacy mentions (intentional compatibility)
- `integration/core/selectors.py`: compatibility axis `restart_pending=False`.
- `integration/core/gateways/base.py`: optional context field for legacy logs.
- `modules/permissions/v2/types.py`: phase enum `RESTART_PENDING` (FSM-level, not runtime decision axis).

These do not currently drive restart behavior and are safe to keep until full compatibility strip.
