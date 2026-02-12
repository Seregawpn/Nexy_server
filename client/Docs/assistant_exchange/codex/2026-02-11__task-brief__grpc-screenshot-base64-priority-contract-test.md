# Task Brief: gRPC Screenshot Base64 Priority Contract Test

Date: 2026-02-11  
Type: task-brief

## Goal
- Add integration-level contract coverage:
  - When `screenshot_base64` exists in session data, `GrpcClientIntegration` must use it directly.
  - File fallback (`screenshot_path` + `Path.read_bytes`) must not be used.

## Implemented

- Updated:
  - `tests/test_client_server_flow_contracts.py`

- Added:
  - `_FakeGrpcClientCaptureArgs` to capture `stream_audio(...)` request kwargs.
  - `test_grpc_prefers_screenshot_base64_over_file_read`
    - Seeds session with both `screenshot_base64` and `screenshot_path`.
    - Monkeypatches `Path.read_bytes` to fail test if called.
    - Verifies `stream_audio(..., screenshot_base64=<event_value>)` and correct `screen_info`.

- Cleanup:
  - Removed unused import `SimpleNamespace` to satisfy Ruff.

## Verification

- `python3 -m pytest tests/test_client_server_flow_contracts.py -q`  
  Result: `4 passed`

- `.venv/bin/ruff check tests/test_client_server_flow_contracts.py`  
  Result: `All checks passed!`
