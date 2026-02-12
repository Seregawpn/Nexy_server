# Task Brief: Status policy cleanup (pass-only) for first-run decisions

## Goal
Убрать зависимость first-run outcome от временных/промежуточных статусов и оставить единый финальный критерий "получено" = `pass`.

## Scope
- First-run integration outcome checks.
- V2 integration hard permissions summary.
- Timeout completion payload consistency.

## Code Changes
1. `integration/integrations/first_run_permissions_integration.py`
   - В blocking ветке `start()` финальный критерий шагов изменен на `allowed={"pass"}`.
   - В timeout completion публикация `permissions.first_run_completed` теперь ставит `all_granted=True`.

2. `modules/permissions/v2/integration.py`
   - `hard_permissions_summary()` теперь считает выданным только `StepState.PASS_`.
   - `_run_orchestrator()` now computes `_missing_hard` по правилу `state == "pass"` (без `needs_restart`).

3. Tests
   - Добавлен `tests/test_first_run_status_policy.py`:
     - `test_hard_permissions_summary_requires_pass_only`
     - `test_timeout_completion_publishes_all_granted_true`

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_permission_restart_v2_freeze.py` -> `9 passed`
- `python3 -m py_compile tests/test_first_run_status_policy.py integration/integrations/first_run_permissions_integration.py modules/permissions/v2/integration.py` -> OK

## Result
- First-run outcome больше не опирается на временные статусы (`needs_restart`, `skipped`) как на "успех".
- Централизованная политика финального статуса: только `pass` = "получено".
