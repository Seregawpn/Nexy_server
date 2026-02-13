# Task Brief: AVF runtime render guard for silent playback

## Context
User reports: gRPC audio chunks arrive and are queued/scheduled, but no audible speech.

## Diagnosis
Playback readiness gate in `AVFoundationPlayer.is_playing()` could return true even when engine/player node runtime path was not actually rendering, which could skip `start_playback()` reassertion.

## Changes
- Updated `modules/speech_playback/core/avf_player.py`:
  - `is_playing()` now requires all runtime conditions:
    - `_playing`
    - playback thread alive
    - engine running
    - player node playing
    - queue/buffer has audio tail
  - Added playback-loop guard before scheduling:
    - if `playerNode` is not playing, call `playerNode.play()` and log warning.

## Why architecture-fit
- Single owner preserved: playback runtime ownership remains in `AVFoundationPlayer`.
- No new integration-level flags/routes introduced.
- No duplicate playback path added.

## Validation
- `python3 -m py_compile modules/speech_playback/core/avf_player.py integration/integrations/speech_playback_integration.py` passed.

## Expected runtime signal after fix
- If node unexpectedly stops, log should contain:
  - `Player node was not playing; resumed before scheduling chunk`
- `SpeechPlaybackIntegration` should no longer treat non-rendering runtime as ready.
