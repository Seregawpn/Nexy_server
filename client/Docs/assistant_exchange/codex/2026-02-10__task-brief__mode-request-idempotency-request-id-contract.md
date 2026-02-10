# Task Brief: mode.request idempotency via request_id contract

## Goal
Stabilize `mode.request` handling under burst/retry conditions by explicit request-level dedup.

## Implemented

1. `ModeManagementIntegration` dedup contract updated:
- File: `integration/integrations/mode_management_integration.py`
- Added request-id cache: `_last_mode_request_id_ts`.
- If `request_id` exists in payload, dedup is done by `request_id` (primary path).
- If `request_id` is missing, fallback dedup remains, now keyed by `(target, session_id, source)`.
- Existing deferred-finalize bypass preserved.

2. Tests added:
- File: `tests/test_mode_management_mode_request_dedup.py`
- `test_mode_request_dedup_by_request_id`
- `test_mode_request_different_request_id_not_deduped`

## Verification
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_user_quit_ack.py` -> 15 passed.
- `python3 -m py_compile integration/integrations/mode_management_integration.py` -> OK.

## Expected runtime effect
- Duplicate retries with same `request_id` are ignored in `ModeManagementIntegration`.
- Distinct intents with different `request_id` are processed normally.
