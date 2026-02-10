# Handoff: mode/action dedup and playback finalize idempotency

## What was cleaned

1. ModeManagementIntegration action accounting dedup
- Removed subscriptions to specific action events:
  - `actions.open_app.started/completed/failed`
  - `actions.close_app.started/completed/failed`
- Kept only unified lifecycle subscriptions:
  - `actions.lifecycle.started`
  - `actions.lifecycle.finished`

Result: one counting path for active actions, no double increment/decrement for open/close flows.

2. ModeManagementIntegration sleep transition dedup on playback done
- `_bridge_playback_done` no longer publishes `mode.request(SLEEPING)` directly.
- It now marks session as deferred; single publish path remains in `_on_playback_finished` after active playback session is removed.

Result: reduced duplicate `mode.request` emissions (`source=playback` + `source=playback.finished`).

3. SpeechPlaybackIntegration finalize idempotency
- Added finalized guard in `_finalize_on_silence` (early return if already finalized).
- Marked `_finalized_sessions[sid] = True` before publishing `playback.completed` in:
  - no-audio completion path (`_on_grpc_completed`)
  - queue-drained completion path (`_finalize_on_silence`)

Result: prevents repeated terminal playback completion publication for the same session.

## Files changed
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/mode_management_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/speech_playback_integration.py`

## Validation
- Python compile check passed for:
  - `mode_management_integration.py`
  - `speech_playback_integration.py`
  - `grpc_client_integration.py`
- Grep check confirmed removed specific action subscriptions in mode management.
