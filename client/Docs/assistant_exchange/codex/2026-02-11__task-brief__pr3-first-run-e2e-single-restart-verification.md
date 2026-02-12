# Task Brief: PR-3 first-run e2e single-restart verification

## Goal
Закрепить end-to-end сценарий first-run в автотесте: один restart после полного pipeline, затем resume без повторного restart.

## Scope
- Расширен тестовый сценарий для `PermissionOrchestrator` в timeout-driven режиме.
- Проверен переход `restart_count: 0 -> 1` и отсутствие второго restart после `resume_after_restart()`.

## Code Changes
1. `tests/test_first_run_orchestrator_single_restart.py`
   - Добавлен `_EventRecorder` для фиксации фазовых событий.
   - Расширен helper `_create_orchestrator(..., emit=...)`.
   - Добавлен тест:
     - `test_full_flow_restart_count_transitions_once_and_resume_completes`
   - Что проверяет новый тест:
     - до старта ledger отсутствует;
     - после `start()` ledger в `POST_RESTART_VERIFY` и `restart_count == 1`;
     - вызов restart handler ровно 1 раз;
     - после `resume_after_restart()` ledger в `COMPLETED`, `restart_count` остаётся `1`;
     - в event stream присутствуют `phase_changed`, `restart_scheduled`, `restart_started`, `completed`.

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_orchestrator_single_restart.py` -> `4 passed`
- `PYTHONPATH=. pytest -q tests/test_permission_restart_v2_freeze.py` -> `3 passed`
- `python3 -m py_compile tests/test_first_run_orchestrator_single_restart.py` -> OK

## Result
- End-to-end поведение single-restart закреплено автоматическим тестом.
- Риск повторного restart после первого цикла дополнительно закрыт regression-проверкой.
