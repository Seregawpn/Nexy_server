# Task Brief: Input lifecycle single-flight + start idempotency

## Request
Внести централизацию/защиту от гонок для start/resume и terminal stop в input lifecycle.

## Changes implemented
1. `integration/integrations/input_processing_integration.py`
- Added lifecycle serialization primitives:
  - `_lifecycle_lock: asyncio.Lock`
  - `_start_in_flight: bool`
- Added `async _wait_for_playback_finished()` barrier.
- Updated `_terminal_stop(...)` to return `bool` (idempotent outcome).
- Added unified owner entrypoint:
  - `async _request_terminal_stop(...) -> bool`
  - single-flight lock + state guard before terminal stop.
- Routed stop callsites through unified entrypoint:
  - external interrupt path
  - force stop path
  - short press stop path
  - release stop path
- Hardened long-press start path:
  - preempt interrupt still published if needed
  - waits for playback/mic barriers after preempt
  - start idempotency guard (`_start_in_flight` / `_recording_started` / state)
  - emits `voice.recording_start`/`mode.request` only once.

2. `integration/integrations/interrupt_management_integration.py`
- Strengthened dedup for `speech_stop`:
  - duplicate in dedup window now returns early before coordinator handling.

## Validation
- `python3 -m py_compile integration/integrations/input_processing_integration.py integration/integrations/interrupt_management_integration.py` passed.

## Expected impact
- Fewer overlapping stop/start transitions at audio boundary.
- Reduced duplicate `speech_stop` handling fanout.
- Lower probability of CoreAudio `HALC ... StartIO error 35` during rapid interrupt/start cycles.
