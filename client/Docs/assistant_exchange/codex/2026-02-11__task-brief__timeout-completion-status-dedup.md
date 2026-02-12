# Task Brief: Timeout completion status dedup in first-run integration

## Goal
Убрать дубли ветвлений в timeout completion path и оставить один канонический payload статуса завершения.

## Changes
1. `integration/integrations/first_run_permissions_integration.py`
   - В `_await_timeout_completion()` удалено дублирование `permissions.first_run_completed` публикации в двух ветках.
   - Введён единый `completion_payload`:
     - `session_id=timeout_mode`
     - `source=permissions_v2_timeout`
     - `all_granted=true`
     - `missing=[]`
   - Логика:
     - всегда публикуем `permissions.first_run_completed`;
     - `system.ready_to_greet` публикуем только если `_ready_published` ещё не выставлен V2.

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_user_quit_ack.py` -> `8 passed`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py` -> OK

## Result
- Убраны лишние статусные дубли в timeout completion.
- Поведение сохранено, decision path стал проще и централизованнее.
