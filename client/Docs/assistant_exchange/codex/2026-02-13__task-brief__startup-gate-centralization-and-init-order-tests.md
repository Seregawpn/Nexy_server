# Startup gate centralization and init-order test alignment

## Goal
Eliminate duplicated startup gating paths, keep one centralized startup decision flow, and restore real startup-order test coverage.

## Changes
1. `integration/core/simple_module_coordinator.py`
- Removed global permissions-only branch in `start()`:
  - removed dynamic `restrict_to_permissions = bool(first_run and not first_run.are_all_granted)`
  - removed early return `First-run mode: skipping remaining integrations`
- Kept selective state-based gates (`FIRST_RUN_IN_PROGRESS`, `PERMISSIONS_RESTART_PENDING`) as runtime owner.
- Startup order is requested via factory in single canonical mode.

2. `integration/core/integration_factory.py`
- Removed `PERMISSIONS_ONLY_ORDER` (duplicate owner path).
- `get_startup_order()` now always returns filtered `STARTUP_ORDER`.
- `restrict_to_permissions` kept in signature for backward compatibility only.

3. `tests/test_init_order.py`
- Replaced AST-based brittle/skip-prone tests.
- New contract tests target `IntegrationFactory` directly:
  - tray after instance_manager
  - permission_restart after first_run_permissions
  - required integrations present
  - `get_startup_order()` filters by available
  - `restrict_to_permissions` does not change selection (single owner path)

## Verification
- `python3 -m py_compile integration/core/integration_factory.py integration/core/simple_module_coordinator.py tests/test_init_order.py`
- `PYTHONPATH=. pytest -q tests/test_init_order.py tests/test_coordinator_critical_subscriptions.py tests/test_permission_restart_v2_freeze.py tests/test_user_quit_ack.py tests/test_first_run_orchestrator_single_restart.py`

## Result
- `23 passed`
- No skips in init-order contract tests.
- Startup gate ownership is centralized (no duplicate permissions-only branch).
