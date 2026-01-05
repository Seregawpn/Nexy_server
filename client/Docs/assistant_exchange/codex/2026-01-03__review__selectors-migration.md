# Review: Selectors migration and state access cleanup

## Summary
Verified new selector helpers in `integration/core/selectors.py` and confirmed integration migrations are aligned with REQ-004 (no direct state access in integrations).

## Notes
- New selector helpers are simple wrappers around `state_manager.get_state_data`, which is permitted inside selectors.
- `get_current_session_id_as_float()` currently appears unused; session_id is generally UUID, so float conversion may not be meaningful if used later.

## Risk
- Remaining warnings in `verify_no_direct_state_access.py` should be periodically audited to avoid regressions.
