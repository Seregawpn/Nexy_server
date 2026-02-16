# Task Brief: Immediate browser start feedback for first-step latency

## Problem
User observed ~5s pause after browser window opens and before first visible step, perceived as freeze.

## Root cause
`BROWSER_TASK_STARTED` had no immediate voice feedback; first feedback arrived only on first `BROWSER_STEP_COMPLETED`, which can be delayed by model planning/page readiness.

## Fix
- Added immediate TTS on `BROWSER_TASK_STARTED` in owner integration:
  - Text: `Browser opened. Starting search now.`
  - Source: `browser_start`
- Added one-shot guard per `_run_process` execution to avoid duplicate start announcements.

## Files
- `integration/integrations/browser_use_integration.py`
- `tests/test_browser_install_contracts.py`

## Verification
- Added test: `test_browser_task_started_emits_immediate_start_tts`
- Run:
  - `pytest -q tests/test_browser_install_contracts.py tests/test_browser_module_ready_bypass.py`
  - Result: `9 passed`

## Architecture gates
- Single owner: Browser UX feedback remains centralized in `BrowserUseIntegration`.
- Zero duplication: reused existing `grpc.tts_request` publish path.
- Anti-race: one-shot local guard avoids duplicate start TTS in the same run.
- New state axis: none.
