# Review: full codebase health check (local)

## Scope
- Full automated quality pass via `scripts/pre_build_gate.sh`
- Focus on architecture conflicts/duplicates/race risks after recent restart/instance fixes

## Executed
- `scripts/pre_build_gate.sh`

## Result summary
- Gate passed: 21/21 checks
- Tests passed in gate:
  - `tests/test_schemas.py` (2 passed)
  - `tests/test_gateways.py` (13 passed)
  - `tests/perf/test_slo_smoke.py` (1 passed)
  - `tests/test_init_order.py` (4 skipped)
- Lint/type:
  - Ruff: pass
  - basedpyright: 0 errors, 2 warnings (scripts only)

## Findings
1. Minor: duplicate assignment in instance manager integration
- File: `integration/integrations/instance_manager_integration.py:65` and `integration/integrations/instance_manager_integration.py:66`
- `self._initialized = True` set twice (no runtime bug, cleanup recommended).

2. Minor: script import paths trigger basedpyright warnings
- File: `scripts/force_login_whatsapp.py:21`
- File: `scripts/verify_whatsapp.py:10`
- Warning: `Import "client.modules.whatsapp" could not be resolved`.
- Affects diagnostic scripts, not app runtime path.

## Architecture status
- Core startup/restart/duplicate protections now aligned with centralized ownership:
  - duplicate detection in `InstanceManager`
  - single restart cap via V2 `restart_count`
  - deferred startup idempotency + retry-safe lock
  - updater vs permission-restart relaunch arbitration

## Residual risk
- Real `.app` + launchd + TCC race scenarios still require manual E2E validation on installed bundle.
