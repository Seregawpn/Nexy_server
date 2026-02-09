# Task Brief: Sleep signal intermittently missing

## Context
- Symptom: `Signals: DONE` is logged, but audio cue on transition to `SLEEPING` is intermittent.
- Architecture: signal source is centralized in `SignalIntegration` (`app.mode_changed -> sleeping`), playback owner is `SpeechPlaybackIntegration` + `AVFoundationPlayer`.

## Diagnosis
- In logs, cue publication and `playback.signal` dispatch happen.
- Intermittency is consistent with playback worker lifecycle race:
  - `start_playback`: `Playback thread already alive, skipping thread restart`
  - shortly after: `_playback_loop exited`
- Result: short cue can be enqueued while worker is effectively exiting.

## Fix
- File: `modules/speech_playback/core/avf_player.py`
- Updated `stop_playback()`:
  - wakes worker queue with sentinel (`None`) to unblock loop quickly;
  - short-joins playback thread (`0.25s`) outside lock to reduce overlap with next `start_playback`;
  - keeps non-blocking behavior (logs if thread still stopping in background).

## Why this fits architecture
- No new owner introduced.
- Signal source remains single (`SignalIntegration`), playback owner remains single (`SpeechPlaybackIntegration`/`AVFoundationPlayer`).
- Fix is local to playback lifecycle (where race occurs).

## Validation
- `python3 -m py_compile modules/speech_playback/core/avf_player.py integration/integrations/signal_integration.py integration/integrations/speech_playback_integration.py` passed.

## Next runtime checks
- On each sleeping transition:
  - expect `Signals: DONE (app.mode_changed -> sleeping)`
  - expect `TRACE phase=playback.start ... pattern=done, signal=true`
  - avoid repeated `Playback thread already alive, skipping thread restart` immediately followed by `_playback_loop exited`
