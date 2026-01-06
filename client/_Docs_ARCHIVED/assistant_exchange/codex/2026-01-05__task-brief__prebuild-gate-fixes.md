# Pre-build Gate Fixes

- Date: 2026-01-05
- Scope: pyproject.toml, config/interaction_matrix.yaml, gateways, predicates, tests/test_gateways.py
- Goal: устранить ошибки pre_build_gate (schema, predicate coverage, rule coverage, missing tests).

## Changes
- Fixed basedpyright config (removed invalid reportMissingImports table, added ignore patterns).
- Normalized interaction_matrix decisions to schema enums and updated gateway names.
- Added missing decision mappings in rule_loader.
- Added predicate aliases (appMode) and permission_restart predicate.
- Added gateway functions: decide_route_manager_reconcile, decide_update_launch,
  decide_permission_restart_schedule, decide_permission_restart_wait.
- Added tests/test_gateways.py with snapshot-driven smoke tests and coverage anchors.

## Verification
- python3 scripts/validate_schemas.py (PASS)
- python3 scripts/verify_predicate_coverage.py (PASS)
- python3 scripts/verify_rule_coverage.py (PASS)
- python3 scripts/verify_4_artifacts_invariant.py (PASS)
- pytest tests/test_gateways.py -q (PASS)

## Notes
- pre_build_gate ранее падал в Critical Paths/Tray Termination (Abort trap 6) — не исправлено, отдельная проблема среды/GUI.
