# Review: Input dead-state cleanup (recognition flags)

## Scope
Safe cleanup in `InputProcessingIntegration` for non-used fields/handlers.

## Removed
1. Unused fields
- `_last_interrupt_event_id`
- `_session_recognized`

2. Unused handler/subscription
- removed subscription to `voice.recognition_completed`
- removed `_on_recognition_completed` method

3. Related no-op resets
- removed `_session_recognized` resets from `_reset`, `_finalize_grpc_failed`, `_on_grpc_completed` tail path.

## Why safe
- These fields were written/reset but never used for branching/decisions.
- PTT/mode/watchdog logic does not depend on them.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_microphone_activation.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `42 passed`
