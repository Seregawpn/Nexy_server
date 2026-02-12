# Task Brief: waiting_grpc deadlock after STT fail-before-release

## Symptom
User holds combo, app enters LISTENING, but later combo no longer starts capture and key input leaks as normal typing.

## Root cause
In `InputProcessingIntegration`, `voice.recognition_failed` was ignored in `PTTState.RECORDING`.
If STT failed before physical key release, then on `release` flow switched to `WAITING_GRPC` even though no gRPC request would ever start.
This created a sticky stale session (`state=waiting_grpc`) and blocked subsequent long-press capture starts.

## Changes
- File: `integration/integrations/input_processing_integration.py`
  - Added deferred STT-fail marker: `_deferred_recognition_failed_session_id`.
  - On `_on_recognition_failed` during `RECORDING`, store deferred failure for active session.
  - On `_handle_release`, if deferred STT fail matches session:
    - publish `mode.request -> SLEEPING` with reason `recognition_failed_after_release`
    - reset input cycle
    - skip transition to `PROCESSING/WAITING_GRPC`.
  - Cleared deferred marker in reset/finalize/new press cycle.

## Tests
- Added test:
  - `tests/test_microphone_activation.py::test_recognition_failed_while_recording_finalized_on_release`
- Validation:
  - `PYTHONPATH=. pytest -q tests/test_microphone_activation.py -k "recognition_failed_while_recording_finalized_on_release or mic_open_watchdog_resets_stuck_recording"`
  - `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py -k "not long_press_timeout_handling"`

## Expected runtime effect
- No more sticky `state=waiting_grpc` after STT fail that happened before release.
- Next combo press can start a new recording cycle normally.
