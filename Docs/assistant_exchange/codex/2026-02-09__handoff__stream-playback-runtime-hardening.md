# Handoff: stream playback runtime hardening

Date: 2026-02-09  
Type: handoff  
Assistant: codex

## Problem
- gRPC audio chunks were received/published/scheduled with valid amplitudes, but user reported no audible assistant response.
- Existing playback start path could be called repeatedly and was not idempotent (risk of duplicate playback threads/runtime drift).

## Fixes
1. `client/modules/speech_playback/core/avf_player.py`
- `start_playback()` made idempotent:
  - if playback already active (`_playing`, thread alive, engine running, player playing) returns no-op.
  - prevents duplicate playback thread creation.
  - avoids restarting thread when one is already alive.

2. `client/integration/integrations/speech_playback_integration.py`
- On the first streamed audio chunk of each new gRPC session:
  - perform soft playback-node restart (`stop_playback()` -> `start_playback()`).
  - ensures fresh runtime state at session boundary.

## Verification
- `py_compile` for modified files: OK
- Targeted tests: `17 passed`

## Expected runtime behavior
- No duplicate `Playback thread started` lines for active playback.
- For each new gRPC session first chunk: one log about playback node restart.
- Stream chunks with valid amplitudes continue to be scheduled and should be audible with more stable startup.
