# Task Brief: Timeout first-run single-restart contract

## Goal
Зафиксировать контракт:
- каждый permission step в first-run закрывается по timeout (15s),
- после завершения всех step выполняется ровно один restart,
- после restart повторный restart больше не выполняется.

## Changes

1. Restart policy config hardened
- File: `config/unified_config.yaml`
- Updated:
  - `integrations.permissions_v2.restart.require_needs_restart: true`

2. V2 restart decision logic aligned with timeout contract
- File: `modules/permissions/v2/orchestrator.py`
- `should_restart(...)`:
  - removed broad fallback behavior,
  - now in strict mode restart requires `needs_restart_marked`.
- `_decide_after_first_run(...)`:
  - for `advance_on_timeout=true`:
    - if `restart_count < 1` and restart is safe -> `_enter_restart_sequence()`
    - else -> `_complete(full_mode=True)`
  - ensures one-time restart in timeout mode.

3. Added tests
- File: `tests/test_permissions_v2_restart_policy.py`
  - `test_should_restart_requires_needs_restart_mark_when_enabled`
  - `test_should_restart_true_when_needs_restart_mark_present`
  - `test_decide_after_first_run_timeout_mode_triggers_single_restart_once`
  - `test_decide_after_first_run_timeout_mode_no_second_restart`

## Verification
Executed:
- `pytest -q tests/test_permissions_v2_restart_policy.py tests/test_restart_pending_state_keys.py tests/test_permissions_completed_state.py tests/test_coordinator_shutdown_user_initiated.py tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`
- `python3 -m py_compile modules/permissions/v2/orchestrator.py tests/test_permissions_v2_restart_policy.py`

Result:
- tests: `16 passed`
- note: one pre-existing RuntimeWarning in tray/mock test path
- py_compile: OK
