# Task Brief: Diagnostic cancel terminal dedup fix

Date: 2026-02-11
Owner: Codex

## Context
User requested reproducible end-to-end diagnostics for speech playback and root-cause isolation.

## Diagnosis
A shared cancel helper pre-marked terminal state (`playback.cancelled`) before terminal event publish path. This caused `playback.cancelled` to be dedup-skipped and not emitted in specific concurrent cancel flows.

## Changes
- Removed premature terminal mark from cancel state helper.
- Kept terminal event ownership in `_emit_terminal_playback_event(...)` only.
- Preserved centralized cancel guard and cleanup owner.

### Code
- `integration/integrations/speech_playback_integration.py`
  - removed: `_terminal_event_by_session[str(sid)] = "playback.cancelled"` from `_apply_cancel_state(...)`

## Repro/Verification
1. Added/used diagnostic pipeline test covering grpc audio -> complete -> concurrent cancel paths.
2. Ran tests:
   - `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_pipeline_diagnostic.py`
   - `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_grpc_audio_format.py tests/test_interrupt_playback.py -k "playback_started or signal or interrupt_idempotently"`

## Result
- Diagnostic test passes and reproduces expected centralized behavior.
- No duplicate terminal cancel events.
- Terminal event owner remains single source (`_emit_terminal_playback_event`).
