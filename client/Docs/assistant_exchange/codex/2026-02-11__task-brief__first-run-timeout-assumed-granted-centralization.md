# Task Brief: First-run timeout assumed-granted centralization

## Request
Сделать policy: если шаг разрешения не подтвержден за отведённый таймаут, считать шаг пройденным (assumed), без ручной проверки фактического grant.

## What changed

1. Config policy switched to timeout-driven flow
- `config/unified_config.yaml`
  - `integrations.permissions_v2.advance_on_timeout: true`
  - `integrations.permissions_v2.default_step_timeout_s: 15.0`

2. V2 integration now emits canonical completion in timeout mode
- `modules/permissions/v2/integration.py`
  - `UIEventType.COMPLETED` в `advance_on_timeout` больше не игнорируется.
  - Публикуется legacy событие `permissions.first_run_completed` с:
    - `source: v2_integration_timeout_assumed`
    - `assumed_by_timeout: true`
    - `all_granted/missing` из summary.

3. HARD summary aligned with timeout policy
- `modules/permissions/v2/integration.py`
  - Для HARD permissions accepted states: `pass`, `skipped`, `needs_restart`.
  - Это применено и в `_summarize_hard_permissions`, и в `_run_orchestrator` (`_all_hard_granted`).

4. Removed duplicate manual completion publish in timeout branch
- `integration/integrations/first_run_permissions_integration.py`
  - `_await_timeout_completion()` больше НЕ публикует вручную:
    - `permissions.first_run_completed`
    - `system.ready_to_greet`
  - Теперь только зеркалит локальный flag, и только если `is_first_run_complete() == True`.

5. Coordinator no longer forces completed=true for all completion events
- `integration/core/simple_module_coordinator.py`
  - `_on_permissions_completed`:
    - `all_granted=true` -> `in_progress=false, required=false, completed=true`
    - `all_granted=false` -> `in_progress=false, required=true, completed=false`

## Why this fits architecture
- Source of truth for completion remains V2 orchestrator + ledger.
- Timeout policy centralized in one owner (V2 path), no parallel completion path.
- StateManager reflects event payload instead of force-setting completed.

## Verification
Executed:
- `pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py tests/test_permissions_completed_state.py`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py integration/core/simple_module_coordinator.py modules/permissions/v2/integration.py`

Result:
- tests: `7 passed`
- py_compile: OK

## Added tests
- `tests/test_permissions_completed_state.py`
  - verifies coordinator sets `FIRST_RUN_COMPLETED` only when `all_granted=true`
  - verifies `required=true` remains when `all_granted=false`
