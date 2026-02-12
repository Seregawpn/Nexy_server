# Task Brief: PTT release stop-path unblocking

Date: 2026-02-11
Owner: Codex

## Context
Runtime logs showed:
- `combo callback dispatch: RELEASE scheduled`
- missing `RELEASE completed`
- prolonged `Listening...` after key release

This indicates RELEASE coroutine was not completing in time.

## Root cause
`InputProcessingIntegration._terminal_stop()` awaited mic-closure on release path.
If `voice.mic_closed` was delayed/missed, release coroutine remained in STOPPING and callback future did not complete.

## Change
File:
- `integration/integrations/input_processing_integration.py`

Changes:
- Added bounded wait for mic closure on terminal stop:
  - `self._terminal_stop_mic_wait_timeout_sec = 0.35`
  - `_terminal_stop()` now wraps mic wait with `asyncio.wait_for(..., timeout=0.35)`
  - on timeout logs warning and continues lifecycle

## Why architecture-safe
- Owner remains `InputProcessingIntegration`.
- No new feature flags.
- No new decision owner introduced.
- Existing stop semantics preserved, but blocking window is bounded.

## Verification
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py`
- Result: `11 passed`

## Expected runtime improvement
On release, callback should complete even if `voice.mic_closed` is late, preventing mode/mic stick due to STOPPING hang.
