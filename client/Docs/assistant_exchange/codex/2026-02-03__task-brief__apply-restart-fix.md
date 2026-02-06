# Task Brief: Apply Restart Fix

## Scope
Applied two fixes to V2 permissions restart flow:
- Corrected restart sequence invocation in orchestrator.
- Added completion idempotency guard in integration when restart is scheduled.

## Changes
- `modules/permissions/v2/orchestrator.py`: `_enter_restart_pending()` → `_enter_restart_sequence()`.
- `modules/permissions/v2/integration.py`: Added `_completion_signaled` guard; ensure completion is signaled only once (on restart scheduled or final completion).

## Verification
Not run (no tests executed).

## Notes
This prevents `AttributeError` in V2 and avoids duplicate completion signaling across restart boundaries.
