# Review: grpc_cancel NameError and PTT delay

## Context
User observed 3-5s hold required to activate mic.

## Findings
- Root issue in `integration/integrations/speech_playback_integration.py`:
  - `_on_grpc_cancel()` published `playback.cancelled` with variables `cancel_source/cancel_reason/cancel_initiator` that were not defined in this scope.
  - Runtime error: `name 'cancel_source' is not defined`.
- Effect:
  - `playback.cancelled` was not emitted on preempt.
  - `InputProcessingIntegration` waited for `playback finish timeout` (configured 5s) before starting recording.

## Changes
- Fixed `_on_grpc_cancel()` by initializing:
  - `cancel_source`
  - `cancel_reason`
  - `cancel_initiator` (with fallback derivation from source)
- Added regression test:
  - `tests/test_interrupt_playback.py::test_grpc_cancel_publishes_playback_cancelled_with_source_payload`

## Validation
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "grpc_cancel_publishes_playback_cancelled_with_source_payload"` -> passed.
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py tests/test_signal_integration_cancel_done_suppression.py` -> passed (16).

## Expected Runtime Outcome
- On keyboard preempt during playback, cancel path emits `playback.cancelled` without exception.
- No forced 5s wait before mic activation caused by cancel-path crash.
