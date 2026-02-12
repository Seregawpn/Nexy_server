# Task Brief: Gateway fallback and V2 startup cleanup

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
- User requested additional centralization cleanup: remove conflict/duplication/race points around first-run, permission restart, and app restart behavior.

## Changes
- Removed deprecated selector usage from fallback decision paths:
  - `integration/core/gateways/common.py`
    - `decide_continue_integration_startup()` fallback now uses snapshot fields directly:
      - first-run restart pending: `s.first_run and s.restart_pending`
      - generic restart pending: `s.restart_pending`
  - `integration/core/gateways/permission_gateways.py`
    - `decide_permission_restart_safety()` fallback now uses `snapshot.first_run and snapshot.restart_pending`.
- Simplified V2 startup path in permission restart integration:
  - `integration/integrations/permission_restart_integration.py`
    - `_on_app_startup_event()` now exits early when `_v2_enabled=True`, skipping legacy detector initialization.
    - Removed dead helper `_get_current_permission_statuses()` (unused).
- Added regression coverage:
  - `tests/test_restart_pending_state_keys.py`
    - `test_permission_restart_skips_legacy_startup_detector_when_v2_enabled`

## Why
- Avoid deprecated compatibility selectors in active runtime paths.
- Remove legacy side effects in V2 mode to keep one owner and one execution path.
- Reduce duplicate initialization work and accidental divergence between V1/V2 behavior.

## Validation
- `pytest -q tests/test_gateways.py tests/test_restart_pending_state_keys.py` -> `17 passed`
- `python3 -m py_compile integration/core/gateways/common.py integration/core/gateways/permission_gateways.py integration/integrations/permission_restart_integration.py tests/test_restart_pending_state_keys.py` -> OK

## Result
- Fallback logic is simpler and directly state-driven.
- V2 startup avoids unnecessary legacy detector processing.
- No new state flags introduced; centralization is preserved.
