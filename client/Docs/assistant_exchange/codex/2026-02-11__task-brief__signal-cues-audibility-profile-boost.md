# Task Brief: signal cues audibility profile boost

Date: 2026-02-11
Owner: Codex

## Context
User reports that mode-transition cues (listen_start/sleep done) are not heard after assistant speech playback, despite cue events being emitted.

## Diagnosis
Event flow is correct (`app.mode_changed` -> `SignalIntegration` -> `playback.signal` -> `SpeechPlaybackIntegration` -> AVF render), but cue profile was too subtle (short/quiet) for practical audibility on Bluetooth route after TTS.

## Architecture Fit
- Where: `integration/integrations/signal_integration.py`
- Source of Truth: cue policy/profile remains centralized in `SignalIntegration`
- No new signal path, no new state axis

## Changes
Updated default cue profile to stronger audibility:
- `LISTEN_START`: 1200Hz, 220ms, volume 0.65
- `DONE`: 1000Hz, 220ms, volume 0.62
- `ERROR`: 740Hz, 240ms, volume 0.68
- `CANCEL`: 660Hz, 220ms, volume 0.62

## Verification
- `python3 -m py_compile integration/integrations/signal_integration.py` passed.

## Risk
Low-medium UX risk (cues are louder/longer), architecture risk low.
