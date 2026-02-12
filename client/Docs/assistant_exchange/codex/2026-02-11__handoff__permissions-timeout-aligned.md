# Handoff: permissions timeout aligned to config

## Task
Align first-run permissions behavior with configured per-step timeout policy:
- no extra waits beyond configured budget,
- step must not hang on microphone trigger,
- timeout should be treated as granted in timeout-policy mode.

## Changes made
1. `modules/permissions/v2/probers/microphone.py`
- `trigger()` is now hard-bounded by timeout via `asyncio.wait_for(asyncio.to_thread(...))`.
- Timeout budget is derived from step timeout (capped to 1.0s, floor 0.2s).
- On trigger timeout/failure, flow continues (no pipeline stall).

2. `modules/permissions/v2/orchestrator.py`
- In `_mark_timeout(...)`, when `advance_on_timeout=true`, timeout now sets step state to `PASS_` with reason `ASSUMED_BY_TIMEOUT`.
- This matches policy: "if user gave or not gave within step window, treat as granted".

## Validation
- `python3 -m py_compile modules/permissions/v2/probers/microphone.py modules/permissions/v2/orchestrator.py` passed.

## Expected runtime effect
- First step (`microphone`) can no longer block first-run pipeline indefinitely.
- Each permission step completes within configured timeout window.
- In timeout-policy mode, all timed-out steps are considered granted and pipeline proceeds deterministically.
