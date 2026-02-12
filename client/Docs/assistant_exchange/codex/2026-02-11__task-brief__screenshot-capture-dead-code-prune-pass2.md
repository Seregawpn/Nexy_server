# Task Brief: Screenshot Capture Dead Code Prune (Pass 2)

Date: 2026-02-11  
Type: task-brief

## Scope
- Follow-up cleanup after screenshot centralization changes.

## Implemented

1) Removed dead methods in screenshot integration
- File: `integration/integrations/screenshot_capture_integration.py`
- Removed:
  - `_request_initial_permission_status`
  - `_check_screen_capture_permissions`
- Both had no call sites in runtime path.

2) Kept centralized permission source
- No local preflight permission probe reintroduced.
- Permission status remains sourced from permissions integration events.

## Verification

- `python3 -m py_compile integration/integrations/screenshot_capture_integration.py modules/screenshot_capture/core/screenshot_capture.py integration/workflows/processing_workflow.py`  
  Result: success

- `python3 -m pytest tests/test_gateways.py -q`  
  Result: `13 passed`

- `python3 -m pytest tests/test_webp_screenshot.py -q`  
  Result: `3 skipped`

## Notes
- `python3 -m ruff ...` could not run in this environment (`No module named ruff`).
