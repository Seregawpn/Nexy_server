# Task Brief: Speech playback operation serialization

Date: 2026-02-10
Assistant: codex

## Context
Observed race symptoms in logs around overlapping playback signal/start-stop transitions and concurrent cancel paths.

## Change
- Added single serialization guard in `integration/integrations/speech_playback_integration.py`:
  - `self._playback_op_lock = asyncio.Lock()`
- Wrapped player-critical operations under one lock:
  - `_on_audio_chunk` (ensure player + queue chunk)
  - `_on_playback_signal` (ensure player + queue cue)
  - `_on_unified_interrupt` (clear queue + stop)
  - `_on_grpc_cancel` (clear queue + stop)

## Architecture fit
- Source of truth preserved in existing integration owner (`SpeechPlaybackIntegration`).
- No new mode/session state introduced.
- No bypass of EventBus/ModeManagement.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`
- Result: `24 passed`

## Expected outcome
- Deterministic ordering for start/stop/queue operations.
- Reduced probability of cue/playback overlap races under rapid interrupt/restart scenarios.
