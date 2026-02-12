# Task Brief: Simplify permissions.first_run_completed payload

## Goal
Упростить контракт `permissions.first_run_completed`: оставить только факт предоставления, убрать `missing` из completion payload.

## Changes
1. `integration/integrations/first_run_permissions_integration.py`
   - В timeout completion payload удален ключ `missing`.
   - Оставлено:
     - `session_id`
     - `source`
     - `all_granted`

2. `modules/permissions/v2/integration.py`
   - В legacy map для `UIEventType.COMPLETED` удален `missing` из `permissions.first_run_completed`.
   - `missing` сохранен только для `permissions.first_run_failed` (диагностика failure path).

3. `tests/test_first_run_status_policy.py`
   - Добавлена проверка: `missing` отсутствует в payload completion-события.

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py tests/test_coordinator_critical_subscriptions.py tests/test_first_run_orchestrator_single_restart.py` -> `11 passed`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py modules/permissions/v2/integration.py tests/test_first_run_status_policy.py` -> OK

## Result
- Контракт completion-события упрощен.
- Убрано лишнее поле, на которое не нужно ориентироваться в текущей модели.
