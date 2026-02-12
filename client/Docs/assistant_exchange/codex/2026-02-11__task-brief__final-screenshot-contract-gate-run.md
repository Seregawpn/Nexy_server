# Task Brief: Final Screenshot Contract Gate Run

Date: 2026-02-11  
Type: task-brief

## Scope
- Run final combined validation for screenshot/session/grpc contract changes.

## Commands

1) Combined pytest subset:
- `python3 -m pytest tests/test_screenshot_capture_regressions.py tests/test_client_server_flow_contracts.py tests/test_processing_workflow_session_guard.py tests/test_webp_screenshot.py -q`

2) Ruff on touched files:
- `.venv/bin/ruff check integration/integrations/screenshot_capture_integration.py modules/screenshot_capture/core/screenshot_capture.py integration/workflows/processing_workflow.py tests/test_screenshot_capture_regressions.py tests/test_client_server_flow_contracts.py`

## Results
- Pytest: `11 passed, 3 skipped`
- Ruff: `All checks passed!`
