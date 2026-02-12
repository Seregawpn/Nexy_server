# Task Brief: Screenshot Capture Centralization and Race Hardening

Date: 2026-02-11  
Type: task-brief

## Goal
- Reduce screenshot flow race/conflict risk.
- Remove duplicate capture path.
- Improve timeout behavior and event-contract consistency.

## Implemented

1) Session binding hardening in screenshot integration
- File: `integration/integrations/screenshot_capture_integration.py`
- `app.mode_changed` now prefers `event.data.session_id` as primary source.
- `_last_session_id` kept only as compatibility fallback with warning logs.

2) Duplicate screenshot path removed
- File: `integration/integrations/screenshot_capture_integration.py`
- Removed integration-local `_fallback_capture_cli` path.
- Runtime capture now goes through module `ScreenshotCapture` only.
- If module unavailable, integration emits `screenshot.error(module_unavailable)`.

3) Dead legacy mode handler removed
- File: `integration/integrations/screenshot_capture_integration.py`
- Removed unused `_on_state_changed` (not subscribed).

4) Capture timeout enforcement
- File: `modules/screenshot_capture/core/screenshot_capture.py`
- Added `asyncio.wait_for(...)` around executor capture in:
  - `capture_screenshot(...)`
  - `capture_region(...)`
- Timeout now actually enforced from `ScreenshotConfig.timeout`.

5) Contract key alignment in processing workflow
- File: `integration/workflows/processing_workflow.py`
- Read `image_path` (canonical contract), keep `path` as compatibility fallback.

6) Minor latency cleanup
- File: `integration/integrations/screenshot_capture_integration.py`
- Removed fixed pre-capture delay `await asyncio.sleep(0.05)`.

## Verification

- `python3 -m pytest tests/test_gateways.py -q`  
  Result: `13 passed`

- `python3 -m pytest tests/test_webp_screenshot.py -q`  
  Result: `3 skipped` (expected environment-dependent skip)

- `python3 -m py_compile integration/integrations/screenshot_capture_integration.py modules/screenshot_capture/core/screenshot_capture.py integration/workflows/processing_workflow.py`  
  Result: success

## Notes
- No new feature flags/states introduced.
- Source of Truth for screenshot capture remains `ScreenshotCaptureIntegration` orchestration + module capture API.
