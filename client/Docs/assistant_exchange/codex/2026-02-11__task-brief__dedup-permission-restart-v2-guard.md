# Task Brief: Dedup cleanup in permission_restart with centralized V2 guard

## Goal
Убрать лишние дубли условий в `permission_restart_integration`, не меняя поведение.

## Changes
1. `integration/integrations/permission_restart_integration.py`
   - В `_do_start()` введён единый локальный флаг `legacy_frozen`, вместо повторных вызовов `_legacy_restart_paths_frozen()`.
   - Удалён избыточный branch в `_on_first_run_restart_pending()`:
     - `source == "v2_integration"` больше не нужен, т.к. ранний централизованный guard уже завершает обработку при V2.
   - Уточнён лог подписок: `Subscribed to integration events`.

## Validation
- `PYTHONPATH=. pytest -q tests/test_permission_restart_v2_freeze.py` -> `3 passed`
- `PYTHONPATH=. pytest -q tests/test_first_run_orchestrator_single_restart.py` -> `4 passed`
- `python3 -m py_compile integration/integrations/permission_restart_integration.py` -> OK

## Result
- Удалены лишние условия/ветки без изменения архитектуры и контракта.
- Централизованный guard остался единственным owner-решением freeze legacy path.
