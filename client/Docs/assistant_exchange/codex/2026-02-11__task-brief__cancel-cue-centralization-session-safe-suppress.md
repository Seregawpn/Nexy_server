# Task Brief: CANCEL cue centralization + session-safe suppression

## Goal
Eliminate duplicate CANCEL cue paths and remove cross-session suppression race.

## What changed
1. `integration/integrations/signal_integration.py`
- Removed duplicate CANCEL emission path from `keyboard.short_press`.
- CANCEL cue is now emitted from a single source: `playback.cancelled`.
- Replaced global keyboard-interrupt suppression fields with per-session map:
  - removed `_last_keyboard_interrupt_ts`, `_last_keyboard_interrupt_session_id`
  - added `_keyboard_interrupt_by_session: dict[str, float]`
- `interrupt.request` is now used only as metadata for suppression window per session.
- Added stale-session cleanup in suppression map by time cutoff.
- Removed unused fields:
  - `_cancel_to_done_suppress_sec`
  - `_last_cancel_session_id`

2. No behavior change for mode/state owners
- PTT/mode transitions unchanged.
- Signal policy remains centralized in SignalIntegration.

## Why this is safer
- One owner-path for CANCEL signal = no duplicate cue generation.
- Session-keyed suppression removes cross-session overwrite race.

## Verification
Executed:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_microphone_activation.py tests/test_mode_management_mode_request_dedup.py tests/test_quartz_voiceover_passthrough.py`

Result:
- `39 passed`
