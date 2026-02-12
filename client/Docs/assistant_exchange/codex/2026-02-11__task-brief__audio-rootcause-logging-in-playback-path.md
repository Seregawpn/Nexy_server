# Task Brief: Audio Root-Cause Logging in Playback Path

Date: 2026-02-11
Owner: Codex
Scope: client audio diagnostics only (no behavior change)

## Goal
Add minimally invasive diagnostics to locate why assistant/signal audio is not audible while pipeline events still complete.

## Architecture Fit
- Where it belongs: playback owner path only
  - `integration/integrations/speech_playback_integration.py`
  - `modules/speech_playback/core/avf_player.py`
- Source of Truth: actual PCM amplitude and AVF enqueue/render lifecycle in playback owners.
- No new state axes or feature flags introduced.

## Changes
1. `SpeechPlaybackIntegration`
- Added `ROOTCAUSE[AUDIO_READY]` in `_ensure_player_ready()` with initialized/playing/queue/buffered metrics.
- Added `ROOTCAUSE[AUDIO_CHUNK]` in `_on_audio_chunk()` after audibility profile:
  - session, dtype, samples, sample_rate, channels, peak/rms (int16 scale), zeros flag.
- Added `ROOTCAUSE[SIGNAL_PCM]` in `_on_playback_signal()`:
  - cue_id/pattern/samples/peak/rms (int16 scale).

2. `AVFoundationPlayer`
- Added per-session sampled enqueue diagnostics `ROOTCAUSE[AVF_ENQUEUE]` in `add_audio_data()`:
  - kind/session/count/samples/peak_f/rms_f/queue.
  - logs first 3 chunks per session, then every `audio_diag_log_every`; always logs signal cues.
- Upgraded start no-op diagnostic to info-level `ROOTCAUSE[START_NOOP]` in `start_playback()`:
  - queue_empty/buffered/thread_alive/engine/player states.
- Added render-stage sampled diagnostics `ROOTCAUSE[AVF_RENDER]` in `_playback_loop()`:
  - cue_id/pattern/frames/mid-buffer peak/engine/player.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py`
- `python3 -m py_compile modules/speech_playback/core/avf_player.py`
- Confirmed new markers:
  - `ROOTCAUSE[AUDIO_READY]`
  - `ROOTCAUSE[AUDIO_CHUNK]`
  - `ROOTCAUSE[SIGNAL_PCM]`
  - `ROOTCAUSE[AVF_ENQUEUE]`
  - `ROOTCAUSE[START_NOOP]`
  - `ROOTCAUSE[AVF_RENDER]`

## Expected Debug Value
If issue persists, logs will localize failure to one layer:
- low/zero `AUDIO_CHUNK` + low `AVF_ENQUEUE` => upstream payload amplitude problem
- normal `AUDIO_CHUNK` + low `AVF_RENDER` => AVF copy/render path problem
- normal render peaks + no audible output => route/session/output-device problem outside PCM pipeline
