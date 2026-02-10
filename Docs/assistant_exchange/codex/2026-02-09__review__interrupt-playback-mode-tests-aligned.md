# Review: interrupt/playback/mode tests aligned with current architecture

## Summary
Updated failing tests to match the current integration contracts (AVF player path, strict interrupt flow, mode/action guards) and reran the targeted suite.

## Updated tests
- `/Users/sergiyzasorin/Fix_new/tests/test_interrupt_playback.py`
  - Replaced legacy expectation `playback.cancelled` from interrupt manager with current `grpc.request_cancel`.
  - Switched legacy `_player` usage to `_avf_player` mocks.
  - Updated idempotency/error/idle assertions to current `_on_unified_interrupt` behavior.

- `/Users/sergiyzasorin/Fix_new/tests/test_playback_full_interrupt.py`
  - Rewritten from legacy `_avf_chunk_buffer` internals to current behavior checks:
    - cancelled session marking,
    - player `clear_queue/stop_playback` calls,
    - ignoring new chunks after interrupt,
    - repeated cancel idempotency safety.

## Verification run
Command:
`PYTHONPATH=/Users/sergiyzasorin/Fix_new/client pytest -q ../tests/test_mode_management_processing_action_guard.py ../tests/test_interrupt_playback.py ../tests/test_playback_full_interrupt.py`

Result:
- `11 passed in 0.86s`

## Notes
- Guard logic in mode management remains validated by `test_mode_management_processing_action_guard.py`.
- Updated tests now verify event contracts and integration behavior, not removed legacy internals.
