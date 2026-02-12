# Task Brief: Fix early first-run completion before actual restart

## Goal
Устранить гонку, где `permissions.first_run_completed` публиковался до фактического перезапуска процесса.

## Root Cause
- `modules/permissions/v2/integration.py` помечал completion на `RESTART_SCHEDULED`.
- `_run_orchestrator()` в `finally` всегда сигналил completion независимо от текущей фазы.
- В результате first-run gate снимался до реального restart/resume.

## Changes
1. `modules/permissions/v2/integration.py`
   - Удалён ранний completion сигнал на `UIEventType.RESTART_SCHEDULED`.
   - `_run_orchestrator()` теперь сигналит completion **только** для терминальных фаз:
     - `COMPLETED`
     - `LIMITED_MODE`
   - Для `RESTART_PENDING` / `POST_RESTART_VERIFY` completion откладывается.

2. `integration/integrations/first_run_permissions_integration.py`
   - В timeout-mode completion events публикуются только если `all_granted=True` после `wait_for_completion()`.
   - При `all_granted=False` публикация completion откладывается (нет ложного снятия gate).

3. Tests
   - Новый файл: `tests/test_permissions_v2_completion_gate.py`
     - `test_restart_scheduled_does_not_signal_completion`
     - `test_non_terminal_phase_defers_completion_signal`
     - `test_terminal_phase_signals_completion`
   - `tests/test_first_run_status_policy.py`
     - добавлен `test_timeout_mode_does_not_publish_completion_when_not_terminal`

## Validation
- `PYTHONPATH=. pytest -q tests/test_permissions_v2_completion_gate.py tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_coordinator_critical_subscriptions.py` -> `15 passed`
- `python3 -m py_compile modules/permissions/v2/integration.py integration/integrations/first_run_permissions_integration.py tests/test_permissions_v2_completion_gate.py tests/test_first_run_status_policy.py` -> OK

## Result
- First-run completion больше не публикуется до фактического restart/resume.
- Убран конфликт “startup продолжился в старом процессе, который уже уходит в restart”.
