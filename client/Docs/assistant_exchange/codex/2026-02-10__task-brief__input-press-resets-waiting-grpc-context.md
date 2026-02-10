# Task Brief: Reset stale waiting_grpc on new press

Date: 2026-02-10
Type: task-brief
Assistant: codex

## Problem
Runtime logs still showed duplicate `interrupt.request` in one user cycle:
- first on `press_preempt`
- second on `long_press`

Root reason: stale `_session_waiting_grpc` and `_active_grpc_session_id` survived into the new press cycle, so `long_press` treated stale context as active preempt target.

## Fix
File:
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`

In `_handle_press` after optional preempt publish and before arming:
- `_session_waiting_grpc = False`
- `_active_grpc_session_id = None`

This ensures a new press always starts a fresh input lifecycle and prevents duplicate preempt on subsequent `long_press`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `pytest -q tests/test_user_quit_ack.py tests/test_speech_playback_session_id.py` → 5 passed
