# Current code audit: problem hotspots (first-run / quit / restart)

## Scope
- integration/core/simple_module_coordinator.py
- integration/core/integration_factory.py
- integration/integrations/permission_restart_integration.py
- modules/permission_restart/macos/permissions_restart_handler.py
- related tests

## Confirmed stable
- Quit/restart guards are active (cancel pending restart + abort marker on quit/shutdown).
- V2 freeze of legacy restart paths is present and tested.

## Problem hotspots
1) **Test coverage gap in startup-order contract (high confidence)**
- `tests/test_init_order.py` currently returns `ssss` (all skipped), because it parses a literal list in coordinator while startup order now comes from `IntegrationFactory.get_startup_order(...)`.
- Risk: regressions in startup sequencing won’t be caught in CI.

2) **Dual startup gating and duplicated control path (medium confidence)**
- Coordinator uses both:
  - global branch `restrict_to_permissions` with early return,
  - per-module state gates (`FIRST_RUN_IN_PROGRESS` / `PERMISSIONS_RESTART_PENDING`).
- Plus `IntegrationFactory.PERMISSIONS_ONLY_ORDER` as second gate owner.
- Risk: divergence between global and selective gates, harder reasoning/debugging.

3) **Legacy path complexity still present in runtime code (medium confidence)**
- Even with V2 owner, legacy handlers/resume-paths remain in runtime code (`first_run_restart_pending`, replay/resume branches).
- Risk: future edits can accidentally re-activate competing path.

## Recommended priority
1. Unskip and rewrite startup-order tests against `IntegrationFactory` as source of truth.
2. Choose one startup gate owner (factory-level or coordinator selective state-gates) and de-duplicate the other.
3. Keep legacy path only behind strict config gate and reinforce tests that it cannot run in V2 mode.

## Quick verification evidence
- `PYTHONPATH=. pytest -q tests/test_init_order.py -q` -> `ssss`.
- `PYTHONPATH=. pytest -q tests/test_coordinator_critical_subscriptions.py tests/test_permission_restart_v2_freeze.py tests/test_user_quit_ack.py` -> `14 passed`.
