# Task
Убрать влияние промежуточных статусов/флагов шагов разрешений на итоговое решение first-run и startup gating.

## Changes
1. modules/permissions/v2/orchestrator.py
- Для `advance_on_timeout=true` финальное решение теперь детерминировано:
  - `restart_count < 1` -> обязательный `_enter_restart_sequence()`
  - иначе `_complete(full_mode=True)`
- Убрана зависимость timeout-ветки от `can_restart_safely(...)` при принятии финального решения.

2. modules/permissions/v2/integration.py
- `hard_permissions_summary()` теперь использует только фазу ledger:
  - `Phase.COMPLETED` => `(True, [])`, иначе `(False, [])`.
- `_summarize_hard_permissions()` переведён на ту же модель (phase-based).
- `_run_orchestrator()` больше не вычисляет итог по step.state; итог только по `ledger.phase == COMPLETED`.
- Удалён неиспользуемый импорт `StepState`.

3. integration/integrations/first_run_permissions_integration.py
- Удалён лишний блок `all_steps_passed` с проверкой `step.state.value`.
- Итог first-run теперь опирается на `all_granted` от V2 integration.

## Validation
- `PYTHONPATH=. pytest -q tests/test_permissions_v2_restart_policy.py tests/test_first_run_timeout_task_lifecycle.py`
- Result: `6 passed`

## Notes
- Модель хранения step-state в ledger сохранена для совместимости формата/восстановления.
- Но step-state больше не участвует в принятии итогового решения first-run startup-gate в V2 timeout-контракте.
