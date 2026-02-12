# Analysis: microphone step skipped immediately on first-run

## Symptom
Log shows `microphone` became `skipped` with `reason_code=TIMEOUT` and pipeline moved to `screen_capture` immediately.

## Root cause
In timeout mode, step deadline was computed from `entry.grace_started_at` from ledger. On restart/relaunch this timestamp could be stale from a previous run, making deadline already expired.

## Fix
- File: `modules/permissions/v2/orchestrator.py`
- Deadline now uses current attempt start first:
  `step_start = entry.triggered_at or entry.grace_started_at or time.time()`

This keeps 15s timeout tied to the current attempt, not stale ledger state.

## Validation
- `python3 -m py_compile modules/permissions/v2/orchestrator.py modules/permissions/v2/integration.py`
