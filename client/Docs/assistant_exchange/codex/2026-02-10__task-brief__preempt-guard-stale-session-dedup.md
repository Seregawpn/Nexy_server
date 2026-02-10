# Task Brief: Preempt Guard Against Stale Session

Date: 2026-02-10
Type: task-brief
Assistant: codex

## Problem
After introducing contract dedup, runtime logs still showed a second `interrupt.request` in the same user cycle.
Root trigger: preempt checks in `InputProcessingIntegration` treated any non-null `session_id` as active work, including stale ids after cancel.

## Change
File:
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`

Updated preempt/interrupt guards in:
- `_handle_press`
- `_handle_long_press`
- `_cancel_short_tap`

Rule changed from:
- `session_id is not None`

To:
- `session_id is not None and _session_waiting_grpc`

So interrupt preempt now fires only when there is real active context:
- playback active, or
- mode is `PROCESSING`, or
- pending grpc wait state.

## Why This Fits Architecture
- Owner remains `InputProcessingIntegration` for input-cycle preempt decision.
- No new ownership paths introduced.
- No local bypass of `InterruptManagementIntegration`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` OK
- `pytest -q tests/test_user_quit_ack.py tests/test_speech_playback_session_id.py` → 5 passed
