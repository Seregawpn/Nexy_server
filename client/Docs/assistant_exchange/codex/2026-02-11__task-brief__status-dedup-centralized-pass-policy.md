# Task Brief: Status dedup with centralized pass-only decision policy

## Goal
Убрать дубли и временные статусные ветки из decision path first-run, сохранив единый критерий "получено" = `pass`.

## Changes
1. `integration/integrations/first_run_permissions_integration.py`
   - В `start()` удалена дублирующая локальная проверка `all_steps_passed`.
   - Оставлен один источник решения: `all_granted = wait_for_completion(...)` из V2 integration.

2. `modules/permissions/v2/integration.py`
   - Добавлен централизованный helper `_get_missing_hard_permissions(...)`.
   - На helper переведены:
     - `hard_permissions_summary()`
     - `_summarize_hard_permissions()`
     - `_run_orchestrator()` (расчёт `_missing_hard`)
   - Политика едина: только `StepState.PASS_` считается полученным.

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_permission_restart_v2_freeze.py tests/test_user_quit_ack.py` -> `11 passed`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py modules/permissions/v2/integration.py` -> OK

## Result
- Устранены дубли интерпретации статусов в first-run.
- Решение централизовано и опирается на одну pass-only политику.
- Временные статусы остаются для внутреннего FSM/телеметрии, но не влияют на итоговое решение успеха.
