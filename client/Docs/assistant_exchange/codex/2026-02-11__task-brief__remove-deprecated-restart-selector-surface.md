# Task Brief: remove deprecated restart selector/fallback surface

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
After race/duplication hardening, one residual risk remained: deprecated restart selector/fallback API still existed in code, even though runtime no longer used it.

## Changes
- Removed dead state key:
  - `integration/core/state_keys.py`
  - deleted `PERMISSIONS_RESTART_COMPLETED_FALLBACK`
- Removed dead typed accessors:
  - `integration/core/state_manager.py`
  - deleted:
    - `set_restart_completed_fallback(...)`
    - `get_restart_completed_fallback(...)`
- Removed deprecated restart selector wrappers:
  - `integration/core/selectors.py`
  - deleted:
    - `is_restart_pending(...)`
    - `is_first_run_restart_pending(...)`
    - `is_restart_completed_fallback(...)`

## Why
- Prevent reintroduction of legacy path usage.
- Reduce API surface that no longer has an owner in current architecture.
- Keep first-run/restart flow strictly on state snapshot + coordinator/V2 contracts.

## Validation
- `pytest -q tests/test_gateways.py tests/test_restart_pending_state_keys.py tests/test_first_run_timeout_task_lifecycle.py tests/test_welcome_startup_sequence.py`
  - Result: `24 passed`
- `python3 -m py_compile integration/core/state_keys.py integration/core/state_manager.py integration/core/selectors.py`
  - Result: OK

## Outcome
- Fewer ambiguous code paths around restart state.
- Cleaner centralized contract for first-run/restart without deprecated fallback API.
