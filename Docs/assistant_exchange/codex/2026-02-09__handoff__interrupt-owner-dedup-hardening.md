# Handoff: interrupt-owner dedup hardening

Date: 2026-02-09  
Type: handoff  
Assistant: codex

## Scope
- Final step of cancel-path centralization: dedup at the interrupt owner level.

## Changes
1) `client/integration/integrations/interrupt_management_integration.py`
- Added dedup window state:
  - `_interrupt_dedup_window_sec = 0.5`
  - `_last_interrupt_publish_ts: dict[(interrupt_type, session_key), ts]`
- In `_on_interrupt_request`, for `speech_stop`:
  - dedup repeated publishes within window,
  - publish `grpc.request_cancel` only once per `(speech_stop, session)` window.

2) Existing prior centralization remains:
- `ProcessingWorkflow` no longer directly publishes `grpc.request_cancel` / `playback.cancelled`.
- `SpeechPlaybackIntegration` keeps terminal cancel dedup.

## Validation
- `py_compile` for modified modules: OK
- Targeted regression suite: `17 passed`

## Expected runtime effect
- Reduced duplicated `grpc.request_cancel` and `playback.cancelled` cascades.
- Cleaner interrupt logs and lower race surface during rapid short-press/cancel sequences.
