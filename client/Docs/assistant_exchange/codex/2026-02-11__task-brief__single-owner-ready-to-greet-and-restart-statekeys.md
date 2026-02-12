# Task Brief: Single-owner ready_to_greet and restart state keys hardening

## What was done

1. `system.ready_to_greet` publisher centralized
- File: `integration/integrations/permission_restart_integration.py`
- Change:
  - Removed all `system.ready_to_greet` publishes from PermissionRestartIntegration.
  - Integration now publishes only `system.permissions_ready` in legacy/non-v2 readiness paths.
- Intent:
  - Keep `system.ready_to_greet` single-owned by V2 permissions integration/orchestrator.

2. Restart pending payload keys centralized via StateKeys
- File: `integration/core/state_keys.py`
  - added typed keys for pending metadata (`*_PERMISSIONS`, `*_SESSION_ID`, `*_BATCH_INDEX`, `*_TOTAL_BATCHES`, `*_IS_LAST_BATCH`).
- Files updated:
  - `integration/core/simple_module_coordinator.py` (write path)
  - `integration/integrations/permission_restart_integration.py` (read path)

3. Production readiness bypass hardened
- File: `integration/integrations/permission_restart_integration.py`
- Change:
  - `NEXY_BYPASS_PERMISSION_READY` ignored in production (no readiness publish).

## Tests
Added/updated:
- `tests/test_restart_pending_state_keys.py`
  - verifies coordinator persists restart-pending batch metadata under StateKeys
  - verifies bypass env ignored in production
  - verifies legacy readiness path publishes only `system.permissions_ready` (no `system.ready_to_greet`)

Executed:
- `pytest -q tests/test_restart_pending_state_keys.py tests/test_permissions_completed_state.py tests/test_coordinator_shutdown_user_initiated.py tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`
- `python3 -m py_compile integration/integrations/permission_restart_integration.py tests/test_restart_pending_state_keys.py`

Result:
- tests: `12 passed`
- note: one pre-existing RuntimeWarning in tray/mock path
- py_compile: OK
