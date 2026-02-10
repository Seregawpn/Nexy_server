# Review: legacy test cleanup + regression green

## Done

1. Replaced brittle source-code string tests with behavior tests
- File updated: `/Users/sergiyzasorin/Fix_new/tests/test_mode_management_listening_transition.py`
- Old checks based on `inspect.getsource(...)` and hardcoded strings removed.
- New tests validate runtime behavior of `_on_mode_request` with async event payloads:
  - LISTENING request from PROCESSING without session is applied.
  - Session mismatch in PROCESSING is ignored for non-interrupt source.
  - Interrupt source bypasses session guard.

2. Updated interrupt/playback tests to current AVF architecture
- File updated: `/Users/sergiyzasorin/Fix_new/tests/test_interrupt_playback.py`
- Switched legacy expectations to current contract:
  - interrupt flow validates `grpc.request_cancel` emission.
  - speech playback interrupt uses `_avf_player` path.

3. Rewrote legacy no-timeouts/no-duplicates suite
- File replaced: `/Users/sergiyzasorin/Fix_new/tests/test_no_timeouts_no_duplicates.py`
- Removed references to removed modules (`modules.microphone_state`, old `InputState`).
- New compact behavioral coverage for `InputProcessingIntegration`:
  - non-blocking long press path,
  - no duplicate terminal start on repeated long press,
  - event order `voice.recording_start -> mode.request`.

4. Rewrote full interrupt playback legacy suite
- File replaced: `/Users/sergiyzasorin/Fix_new/tests/test_playback_full_interrupt.py`
- Removed dependencies on removed internals (`_avf_chunk_buffer`).
- New checks for current behavior:
  - session cancellation marking,
  - `_avf_player.clear_queue/stop_playback` calls,
  - chunks ignored after cancellation,
  - idempotent repeated cancellation safety.

## Verification

Command:
`PYTHONPATH=/Users/sergiyzasorin/Fix_new/client pytest -q ../tests/test_mode_management_processing_action_guard.py ../tests/test_interrupt_playback.py ../tests/test_playback_full_interrupt.py ../tests/test_mode_management_listening_transition.py ../tests/test_no_timeouts_no_duplicates.py`

Result:
- `17 passed in 0.89s`

## Outcome
- Test layer now matches current architecture and contracts.
- Legacy brittle tests removed/refactored.
- Target regression pack for mode/action/playback/interrupt is fully green.
