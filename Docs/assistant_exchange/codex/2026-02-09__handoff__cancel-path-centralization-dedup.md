# Handoff: cancel path centralization and dedup

Date: 2026-02-09  
Type: handoff  
Assistant: codex

## What changed

1) `client/integration/workflows/processing_workflow.py`
- Removed direct subscription of `ProcessingWorkflow` to `keyboard.short_press`.
- Kept only `interrupt.request` as interrupt input.
- `_cancel_active_processes()` no longer publishes:
  - `grpc.request_cancel`
  - `playback.cancelled`
- Cancellation is now delegated to unified interrupt channel owner.

2) `client/integration/integrations/speech_playback_integration.py`
- Hardened `_on_grpc_cancel` dedup:
  - marks session as finalized on cancel path,
  - skips duplicate publish when `cancel_in_flight`,
  - updates cancel dedup window (`_last_cancel_sid/_last_cancel_ts`) for grpc-cancel path too.

## Why
- Removed duplicate cancel paths that produced repeated `playback.cancelled` / `grpc.request_cancel`.
- Preserved single source of truth for interruption orchestration.

## Validation
- `py_compile`: OK
- Targeted regression suite: `17 passed`
