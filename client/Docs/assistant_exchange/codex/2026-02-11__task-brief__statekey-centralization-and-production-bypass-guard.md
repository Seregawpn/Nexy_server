# Task Brief: StateKey centralization and production bypass guard

## Scope
Дополнительно к предыдущим фиксам убраны оставшиеся неконтролируемые точки:
1) raw string state keys для restart_pending payload,
2) readiness bypass через env в production.

## Implemented changes

### 1) Centralized restart_pending payload keys via StateKeys
- File: `integration/core/state_keys.py`
- Added keys:
  - `PERMISSIONS_RESTART_PENDING_PERMISSIONS`
  - `PERMISSIONS_RESTART_PENDING_SESSION_ID`
  - `PERMISSIONS_RESTART_PENDING_BATCH_INDEX`
  - `PERMISSIONS_RESTART_PENDING_TOTAL_BATCHES`
  - `PERMISSIONS_RESTART_PENDING_IS_LAST_BATCH`

- File: `integration/core/simple_module_coordinator.py`
  - `_on_permissions_restart_pending` now writes payload using new `StateKeys` constants.
  - Also persists batch metadata explicitly (`batch_index`, `total_batches`, `is_last_batch`) in StateManager.

- File: `integration/integrations/permission_restart_integration.py`
  - `_resume_pending_first_run_restart` now reads all restart-pending payload fields via `StateKeys` constants.

### 2) Hardened readiness bypass behavior in production
- File: `integration/integrations/permission_restart_integration.py`
- Behavior update:
  - `NEXY_BYPASS_PERMISSION_READY` is now ignored in production (`return`), no forced ready publication.
  - Previous behavior allowed bypass even in production with warning.

## Added tests
- File: `tests/test_restart_pending_state_keys.py`
  1. `test_coordinator_persists_restart_pending_batch_metadata_in_state_keys`
     - verifies coordinator writes all restart-pending fields via centralized keys.
  2. `test_permission_restart_bypass_env_ignored_in_production`
     - verifies production guard ignores env bypass and does not publish readiness events.

## Verification
Executed:
- `pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py tests/test_permissions_completed_state.py tests/test_coordinator_shutdown_user_initiated.py tests/test_restart_pending_state_keys.py`
- `python3 -m py_compile integration/core/state_keys.py integration/core/simple_module_coordinator.py integration/integrations/permission_restart_integration.py tests/test_restart_pending_state_keys.py`

Result:
- tests: `11 passed` (1 known warning in tray dispatch test mock path)
- py_compile: OK

## Impact
- Reduced risk of key mismatch/typos in restart-pending lifecycle.
- Removed production path that could force readiness via env bypass.
- Improved shutdown/restart determinism under first-run and restart_pending flows.
