# Task Brief: Screenshot Out-of-Order Replay Regression Test

Date: 2026-02-11  
Type: task-brief

## Goal
- Add explicit regression coverage for out-of-order replay scenario:
  - `voice.recording_start(A) -> voice.recording_start(B) -> app.mode_changed(PROCESSING, A)`

## Implemented

- Updated:
  - `tests/test_screenshot_capture_regressions.py`

- Added test:
  - `test_screenshot_integration_out_of_order_replay_keeps_mode_session`
  - Verifies capture routing follows `app.mode_changed.data.session_id` (`A`) even after later `recording_start(B)`.

## Verification

- `python3 -m pytest tests/test_screenshot_capture_regressions.py -q`  
  Result: `3 passed`

- `.venv/bin/ruff check tests/test_screenshot_capture_regressions.py`  
  Result: `All checks passed!`
