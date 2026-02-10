# Task Brief: Reject PROCESSING mode requests without session_id

Date: 2026-02-10
Assistant: codex

## Problem
Logs showed `mode.request -> AppMode.PROCESSING` with `session_id=None`, causing empty processing loops, redundant `app.mode_changed`, tray/screenshot churn, and workflow skip messages.

## Change
- Added centralized guard in `integration/integrations/mode_management_integration.py`:
  - Reject `target=AppMode.PROCESSING` when `session_id` is missing.
  - Log warning: `MODE_REQUEST rejected: target=PROCESSING requires session_id`.
- Added regression test:
  - `tests/test_mode_management_mode_request_dedup.py::test_mode_request_processing_without_session_id_rejected`

## Why architecture-safe
- Enforced in existing mode owner (`ModeManagementIntegration`), no local bypasses.
- Keeps `ApplicationStateManager` as single SoT while preventing invalid transitions.
- No new state introduced.

## Verification
- `python3 -m py_compile integration/integrations/mode_management_integration.py tests/test_mode_management_mode_request_dedup.py`
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_speech_playback_session_id.py`
- Result: `25 passed`

## Expected effect in logs
- No more `MODE_REQUEST: target=AppMode.PROCESSING ... session_id=None` being applied.
- No more `ProcessingWorkflow: mode=processing without session_id` noise.
