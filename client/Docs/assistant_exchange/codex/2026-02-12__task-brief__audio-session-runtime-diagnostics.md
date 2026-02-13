# Task Brief: audio-session runtime diagnostics

## Goal
Add decisive runtime logs to confirm whether inaudible playback is caused by wrong AVAudioSession profile/route at playback start.

## Changes
- File: `modules/speech_playback/core/avf_player.py`
- Added:
  - `_capture_audio_session_runtime(session)` snapshot helper.
  - One-time warning when AVAudioSession symbols are unavailable.
  - Extended `AUDIO_SESSION_PROFILE` log with `before`/`after` snapshots.
  - `AUDIO_SESSION_RUNTIME reason=start_playback snapshot=...` log right after route snapshot.

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` ✅
- `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_grpc_audio_format.py` ✅
- `PYTHONPATH=. python3 -m pytest -q tests/test_interrupt_playback.py -k "playback_started or signal"` ✅

## What to collect next
After full app restart and one voice cycle:
- `AUDIO_SESSION_PROFILE ...`
- `AUDIO_SESSION_RUNTIME reason=start_playback ...`
- matching `AUDIO_PIPELINE phase=before_queue/before_schedule ...`
