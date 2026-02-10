# Task Brief: Speech playback diagnostics verbosity centralization

Date: 2026-02-10
Assistant: codex
Type: task-brief

## Goal
Reduce playback log flood (`AUDIO_RECV`, `RAW_AUDIO_DIAG`, AVF per-chunk diagnostics) while preserving stable playback behavior and interrupt/session contracts.

## Changes
1. `integration/integrations/speech_playback_integration.py`
- Added runtime controls from speech playback config:
  - `audio_diag_verbose` (default false)
  - `audio_diag_log_every` (default 50)
- Gated per-chunk logs:
  - `AUDIO_RECV`
  - `RAW_AUDIO_DIAG`
- Passed diagnostics flags down to `AVFPlayerConfig`.

2. `modules/speech_playback/core/avf_player.py`
- Extended `AVFPlayerConfig` with:
  - `audio_diag_verbose`
  - `audio_diag_log_every`
- Gated noisy diagnostics in:
  - `add_audio_data`
  - `is_playing`
  - `_playback_loop` (`QUEUE_EXTRACT`, `Pre-copy`, `Test write`, `Scheduled chunk`)
- Added sparse progress debug log every `audio_diag_log_every` chunks when verbose is off.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py` -> OK
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py` -> 18 passed

## Result
- Runtime logs are much cleaner in default mode.
- Deep playback diagnostics remain available via config toggle without behavior changes in interrupt/mode/session flow.
