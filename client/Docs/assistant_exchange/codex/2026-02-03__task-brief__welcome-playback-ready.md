# Task Brief: welcome playback readiness gating

## Context
Welcome message audio was sent before SpeechPlaybackIntegration finished AVFoundationPlayer initialization, leading to `Player not initialized` and a welcome timeout.

## Changes
- Publish `playback.ready` from `SpeechPlaybackIntegration` when AVFoundationPlayer is initialized (startup and on-demand).
- Welcome flow waits for `playback.ready` (with timeout) before sending raw audio.
- Added on-demand AVFoundationPlayer initialization guard in `_ensure_player_ready`.

## Files Touched
- integration/integrations/speech_playback_integration.py
- integration/integrations/welcome_message_integration.py

## Verification
Not run in this task.

## Follow-ups
- Run a smoke startup to confirm welcome audio plays and no `Player not initialized` appears.
