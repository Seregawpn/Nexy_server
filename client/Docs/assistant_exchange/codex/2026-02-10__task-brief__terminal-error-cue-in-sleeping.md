# Terminal ERROR cue in SLEEPING

## What was fixed
- `SignalIntegration` now emits `ERROR` cue for session-scoped failures even when app mode is already `SLEEPING`.
- Added dedup for repeated `ERROR` on the same `session_id` within short window.

## Files
- `integration/integrations/signal_integration.py`
- `tests/test_signal_integration_cancel_done_suppression.py`

## Why
Previously `voice.recognition_failed` could arrive after mode switched to sleeping, and ERROR cue was skipped (`already sleeping`), causing silent terminal state.

## Result
- Terminal failure now has audible confirmation.
- No duplicate ERROR cues for same session.

## Validation
- `python3 -m py_compile ...` OK
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py`
- Result: 10 passed.
