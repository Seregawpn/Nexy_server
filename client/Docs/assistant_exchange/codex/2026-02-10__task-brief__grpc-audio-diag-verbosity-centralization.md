# Task Brief: Centralized gRPC audio diagnostics verbosity

Date: 2026-02-10
Assistant: codex
Type: task-brief

## Goal
Reduce runtime log flood from per-chunk audio diagnostics while preserving protocol summary and on-demand deep troubleshooting.

## Changes
- Updated `integration/integrations/grpc_client_integration.py`:
  - Added centralized controls:
    - `audio_diag_verbose` (default: `False`)
    - `audio_diag_log_every` (default: `50`)
  - Sources:
    - config: `integrations.grpc_client.audio_diag_verbose`, `audio_diag_log_every`
    - env override: `NEXY_AUDIO_DIAG_VERBOSE`
  - Gated per-chunk diagnostics (`GRPC_CHUNK_DIAG`, `GRPC_AUDIO_RAW`, silent/noise-floor skip logs, low-amplitude logs) behind `audio_diag_verbose`.
  - In non-verbose mode, keep only sparse progress debug log every `audio_diag_log_every` chunks.
  - Kept end-of-stream summary logs unchanged.

## Validation
- `python3 -m py_compile integration/integrations/grpc_client_integration.py integration/integrations/input_processing_integration.py` -> OK
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py` -> 15 passed

## Result
- Default runtime logs are significantly cleaner.
- Deep audio diagnostics remain available via config/env toggle without code changes.
