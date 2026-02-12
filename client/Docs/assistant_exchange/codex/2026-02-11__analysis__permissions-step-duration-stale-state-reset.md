# Analysis: steps advanced every ~2s instead of 15s

## Symptom
After fix, pipeline moved through `screen_capture -> network -> contacts...` every ~2s.

## Root cause
`advance_on_timeout` path reused persisted terminal/stale per-step state from ledger. `_wait_until_deadline` returned early for terminal states, leaving only grace delay.

## Fix
- File: `modules/permissions/v2/orchestrator.py`
- At the start of each step in timeout mode, reset runtime step markers/state:
  - `state=UNKNOWN`
  - `triggered_at/grace_started_at/polling_started_at/waiting_long_entered_at=None`
  - `last_reason_code/last_reason=None`

This enforces fresh 15s budget per step on each run.

## Validation
- `python3 -m py_compile modules/permissions/v2/orchestrator.py`
