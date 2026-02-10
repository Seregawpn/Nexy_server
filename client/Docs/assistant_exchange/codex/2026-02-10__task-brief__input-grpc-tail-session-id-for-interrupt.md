# Task Brief: Keep session id during playback tail after grpc.completed

Date: 2026-02-10
Assistant: codex
Type: task-brief

## Context
In runtime logs, `interrupt.request` could be emitted during playback tail right after `grpc.request_completed`, but `session_id` became `None` too early due to input reset on grpc completion.

## Changes
1. Updated `integration/integrations/input_processing_integration.py`:
- `_on_grpc_completed`:
  - if playback is active, do not call full `_reset`.
  - move state to idle-like terminal state and keep `_active_grpc_session_id = sid`.
  - keep session context for immediate interrupt/preempt.
- `_on_playback_finished`:
  - for terminal playback event with matching `session_id`, clear `_active_grpc_session_id`.
  - clear state-manager session id only for matching active session.

2. Added tests in `tests/test_interrupt_playback.py`:
- `test_grpc_completed_keeps_session_during_playback_tail`
- `test_playback_terminal_clears_tail_session_context`

## Validation
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py` -> 9 passed
- `python3 -m py_compile integration/integrations/input_processing_integration.py` -> ok

## Expected Result
Interrupt during playback tail keeps non-null session context for cancel routing, and session context is removed on terminal playback event.
