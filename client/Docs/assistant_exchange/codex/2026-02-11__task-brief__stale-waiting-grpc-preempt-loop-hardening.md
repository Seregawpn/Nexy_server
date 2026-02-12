# Task Brief: stale waiting_grpc preempt-loop hardening

## Problem
User experienced combo hold producing normal key input instead of new mic cycle.
Logs showed repeated `PRESS_PREEMPT should=True ... state=waiting_grpc` while mode already `SLEEPING`.

## Root cause
`waiting_grpc` context could remain stale after terminal paths. Next PRESS/LONG_PRESS interpreted stale context as pending preempt and repeatedly emitted interrupt flow.

## Fix
- File: `integration/integrations/input_processing_integration.py`
- Added normalization guard:
  - `_normalize_stale_waiting_grpc_context(source)`
  - Clears stale grpc wait context when:
    - `_session_waiting_grpc=True`
    - mode != `PROCESSING`
    - no playback/recording/mic activity
- Guard called at start of `_handle_press` and `_handle_long_press`.

## Tests
- Added:
  - `tests/test_interrupt_playback.py::test_press_clears_stale_waiting_grpc_in_sleeping_without_interrupt`
- Validation passed:
  - targeted stale tests
  - full touched suite (37 passed, 1 deselected)

## Expected effect
- No repeated preempt loop from stale `waiting_grpc` in `SLEEPING`.
- New press cycles are accepted normally and can re-arm microphone flow.
