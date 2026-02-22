# Task Brief — Trim gRPC TTS tail silence to prevent playback “chewing”

## Context
After enforcing commit-on-release, user still observed delayed playback completion (`queue_drained` after ~2.9s) with many near-zero audio chunks in logs.

## Diagnosis
`SpeechPlaybackIntegration` enqueued prolonged near-silent gRPC chunks, so `finalize_on_silence` waited for queue drain even after audible speech ended.

## Changes
1. Added tail-silence trimming in `client/integration/integrations/speech_playback_integration.py`:
- New config-backed controls:
  - `grpc_tail_silence_trim_enabled`
  - `grpc_tail_silence_peak_threshold`
  - `grpc_tail_silence_rms_threshold`
  - `grpc_tail_silence_min_chunks`
- Logic in `_on_audio_chunk`:
  - Track consecutive near-silent chunks per session.
  - Drop chunks after threshold is exceeded (only after session already had audio).

2. Extended playback config loader in `client/config/unified_config_loader.py` to expose new keys.

3. Added defaults in `client/config/unified_config.yaml`.

## Architecture Fit
- Owner preserved: `SpeechPlaybackIntegration` remains single owner of playback queue acceptance policy.
- No new workflow/state owner introduced.

## Validation
- `python3 -m py_compile client/integration/integrations/speech_playback_integration.py client/config/unified_config_loader.py`
- Config read check returned expected new keys/values.

## Expected Runtime Effect
- Fewer trailing silent chunks enqueued.
- Faster `playback.completed` after `grpc.request_completed`.
- Reduced “зажевывание” at phrase end.
