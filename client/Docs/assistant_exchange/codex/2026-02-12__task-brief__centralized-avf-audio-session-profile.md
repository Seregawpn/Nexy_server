# Task Brief: Centralized AVF audio-session profile

## Context
User still reports inaudible gRPC TTS while logs show valid non-zero PCM chunks and successful scheduling in AVF.

## Changes made
- File: `modules/speech_playback/core/avf_player.py`
- Added centralized playback audio-session owner method:
  - `_ensure_playback_audio_session(reason=...)`
- `initialize()` and `start_playback()` now both use this single method.
- Added idempotent guard with real current-profile check (category/mode) to avoid false dedup.
- Added structured diagnostics:
  - `AUDIO_SESSION_PROFILE reason=... applied=true/false ...`
- Kept playback startup path unchanged otherwise (no extra state paths outside AVF owner).

## Why
- Previous path could keep stale non-playback audio-session profile after mic/stt transitions.
- This created mismatch: chunks are decoded/scheduled but output remains effectively inaudible.

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` ✅
- `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_grpc_audio_format.py` ✅ (2 passed)
- `PYTHONPATH=. python3 -m pytest -q tests/test_interrupt_playback.py -k "playback_started or signal"` ✅ (4 passed)

## Next runtime check
Run one live voice cycle and compare logs:
- `AUDIO_SESSION_PROFILE` on welcome vs grpc playback
- `AUDIO_PIPELINE phase=before_queue` and `phase=before_schedule`
- Expect: same playback profile, non-trivial peak values, audible speech.
