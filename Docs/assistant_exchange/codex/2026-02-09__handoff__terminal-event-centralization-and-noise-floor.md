# Handoff: terminal event centralization and ingress noise-floor

Date: 2026-02-09  
Type: handoff  
Assistant: codex

## Changes

1) `client/integration/integrations/speech_playback_integration.py`
- Added centralized terminal publisher helper:
  - `_emit_terminal_playback_event(event_name, session_id, payload, mark_finalized=True)`
- Added per-session terminal dedup map:
  - `_terminal_event_by_session`
- Switched terminal publishes to helper:
  - `playback.completed` (no-audio path and finalize-on-silence)
  - `playback.failed` (grpc failed)
  - `playback.cancelled` (grpc cancel path)
- Result: one terminal playback event per session (idempotent by owner).

2) `client/integration/integrations/grpc_client_integration.py`
- Added centralized ingress noise-floor gate:
  - `_noise_floor_peak_int16 = 3`
  - `_noise_floor_rms_int16 = 1.0`
- Audio chunk processing now drops:
  - all-zero chunks (existing behavior)
  - micro-noise floor chunks (new behavior)
- Result: reduced technical tail/noise entering playback queue.

## Validation
- `py_compile`: OK
- Targeted regression suite: `17 passed`

## Outcome
- Terminal playback lifecycle is centralized in one owner with session idempotency.
- Audio ingress policy remains centralized in grpc integration with explicit noise-floor rule.
