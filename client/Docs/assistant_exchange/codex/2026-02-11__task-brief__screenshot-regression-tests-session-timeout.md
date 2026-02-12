# Task Brief: Screenshot Regression Tests (Session Order + Timeout)

Date: 2026-02-11  
Type: task-brief

## Goal
- Add focused regressions for screenshot flow stability:
  1) Out-of-order/stale session guard in mode-driven capture routing.
  2) Hard timeout behavior in `ScreenshotCapture.capture_screenshot()`.

## Implemented

- Added test file:
  - `tests/test_screenshot_capture_regressions.py`

- Test 1:
  - `test_screenshot_integration_prefers_mode_event_session_id`
  - Verifies `ScreenshotCaptureIntegration._on_mode_changed` uses `event.data.session_id`
    instead of stale `_last_session_id`.

- Test 2:
  - `test_capture_screenshot_timeout_returns_error_result`
  - Verifies timeout path returns `ScreenshotResult(success=False, error="Таймаут захвата скриншота")`.

## Verification

- `python3 -m pytest tests/test_screenshot_capture_regressions.py -q`  
  Result: `2 passed`

- `python3 -m py_compile tests/test_screenshot_capture_regressions.py`  
  Result: success
