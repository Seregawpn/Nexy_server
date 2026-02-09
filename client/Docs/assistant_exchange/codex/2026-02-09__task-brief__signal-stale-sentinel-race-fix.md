# Task Brief: Signal playback stale-sentinel race

## Problem
In logs after previous fix:
- `▶️ Playback started`
- immediately `🛑 _playback_loop exited. _playing=True`

This indicates stale stop sentinel (`None`) can be consumed after next start, causing cue worker to exit at wrong time.

## Fix
- File: `modules/speech_playback/core/avf_player.py`
- In `_playback_loop`, changed sentinel handling:
  - `chunk is None` now breaks only when `self._playing == False`
  - if `self._playing == True`, stale sentinel is ignored (`continue`)

## Architecture Fit
- Source of truth unchanged.
- Playback lifecycle remains centralized in `AVFoundationPlayer`.
- No new state owners introduced.

## Validation
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` passed.

## Runtime expectation
- No more `..._playback_loop exited. _playing=True` immediately after signal start.
- `DONE`/`LISTEN_START` cues should be stable across rapid mode transitions.
