# Task Brief: ownership contracts and docs sync for first-run/restart

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
Final hardening step requested: centralize behavior, remove ambiguity, and ensure no conflict/race-prone duplicate owners remain.

## Code changes

1. Ownership contract tests (new)
- File: `tests/test_event_ownership_contract.py`
- Added AST-based contract checks:
  - only `modules/permissions/v2/integration.py` may publish `system.ready_to_greet`
  - only `integration/core/simple_module_coordinator.py` may call `set_restart_pending(...)`

2. Restart race/guard stress coverage (extended)
- File: `tests/test_restart_pending_state_keys.py`
- Added:
  - `test_permission_restart_aborts_if_user_quit_intent_is_set_before_trigger`
  - `test_permission_restart_aborts_if_updater_is_busy_before_trigger`

## Documentation sync

1. Architecture overview updates
- File: `Docs/ARCHITECTURE_OVERVIEW.md`
- Updated StateKeys list to current keys:
  - removed stale `PERMISSIONS_RESTART_COMPLETED_FALLBACK`
  - included pending metadata keys and `USER_QUIT_INTENT`
- Updated `permission_restart_integration` section:
  - clarified V2/legacy subscriptions split
  - clarified it does not own `system.ready_to_greet`
  - clarified final revalidation guard before restart trigger

2. Requirements snapshot updates
- File: `Docs/PROJECT_REQUIREMENTS.md`
- REQ-010 updated:
  - V2 first-run with `advance_on_timeout=true`
  - timeout treated as assumed-granted without status check
- REQ-011 updated:
  - one-restart contract for first-run chain
  - explicit expected result: no repeated restart from same chain

## Validation
- `pytest -q tests/test_event_ownership_contract.py tests/test_restart_pending_state_keys.py tests/test_first_run_timeout_task_lifecycle.py tests/test_welcome_startup_sequence.py tests/test_gateways.py`
  - Result: `28 passed`
- `python3 -m py_compile` on updated Python files
  - Result: OK

## Outcome
- Ownership boundaries are now executable contracts (tests).
- Documentation reflects actual runtime behavior and current state model.
- Reduced risk of reintroducing duplicate owners/conflicting restart paths.
