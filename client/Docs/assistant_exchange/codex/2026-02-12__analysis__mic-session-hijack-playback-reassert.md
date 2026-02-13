# Mic session hijack -> playback reassert fix

## Problem
Intermittent "audio not audible" after input/microphone usage while playback pipeline logs remained healthy.

## Root cause
SpeechPlaybackIntegration `_ensure_player_ready()` skipped `start_playback()` when player already running.
But AVF owner re-asserts playback AVAudioSession profile inside `start_playback()`.
So after microphone path reconfigured AVAudioSession, playback session could remain non-playback while `_playing=True`.

## Fix
- File: `integration/integrations/speech_playback_integration.py`
- Change: `_ensure_player_ready()` now always calls `self._avf_player.start_playback()`.
- Rationale: method is idempotent/no-op for running thread, but re-applies playback audio session profile.

## Verification
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py` passed.

## Architecture
- Source of truth preserved in AVFoundationPlayer for AVAudioSession playback profile.
- No duplicate owner introduced.
