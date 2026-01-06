# Pre-build Gate Run

- Date: 2026-01-05
- Command: ./scripts/pre_build_gate.sh
- Result: FAILED

## Key Failures
- Tests: schema/gateways/init/first-run/SLO failed due to pyproject.toml parse error: "Cannot overwrite a value (line 73, column 40)".
- Config validation: interaction_matrix.yaml invalid (decision value "degrade" not in schema).
- 4-artifacts invariant: test_gateways.py missing entries for update_in_progress, restart_pending.
- Predicate coverage: missing predicates in registry (app.update_in_progress, appMode, permission_restart).
- Critical paths & tray termination: Abort trap 6 during test execution.

## Warnings
- ruff not installed (lint skipped).
- No-direct-state-access check has warnings but passed.

## Passed
- pb2 freshness, feature flags registration, requirements snapshot validation, TAL assertion checks.
