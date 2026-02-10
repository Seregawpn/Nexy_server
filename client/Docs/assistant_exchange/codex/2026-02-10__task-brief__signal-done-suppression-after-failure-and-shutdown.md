# Task Brief: Signal DONE suppression after failure/shutdown

## Context
Observed false/late `DONE` cues after transition to `SLEEPING`, including race windows after `voice.recognition_failed` and during quit path.

## Changes
- Updated `integration/integrations/signal_integration.py`:
  - Added shutdown guard (`_shutdown_requested`) and subscription to `app.shutdown`.
  - Added per-session anti-conflict markers:
    - `_last_error_session_id`
    - `_last_cancel_session_id`
  - `DONE` on `app.mode_changed -> sleeping` is now suppressed when:
    - recent error/cancel cooldown active,
    - same session as latest error/cancel.
  - `_on_error_like` now stores error timestamp/session before mode check to avoid out-of-order race.
  - Suppressed all cue emission after shutdown request.

- Updated tests `tests/test_signal_integration_cancel_done_suppression.py`:
  - Added `test_done_suppressed_for_same_session_after_recognition_failed`
  - Added `test_shutdown_suppresses_followup_done`

## Verification
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py` -> 4 passed
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py` -> 7 passed

## Expected runtime effect
- No false `DONE` for same session after recognition failure.
- No late cue emission after `app.shutdown`.
- Existing interrupt dedup behavior preserved.
