# Task Brief: Event Contract Dedup + Welcome Session Binding

Date: 2026-02-10
Type: task-brief
Assistant: codex

## Scope
- Harden integration contract for:
  - `interrupt.request` publish/consume path
  - interrupt dedup/idempotency in owner integration
  - welcome playback terminal wait by concrete `session_id`

## Changes

### 1) InputProcessingIntegration
File: `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`

- `interrupt.request` payload now includes:
  - `event_id` (UUID)
  - `contract_version=1`
  - existing `session_id`, `press_id`, `source`, `type`

Goal: make each interrupt command uniquely identifiable and traceable.

### 2) InterruptManagementIntegration
File: `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py`

- Source/priority extraction aligned to payload-first:
  - read from `event.data` first, then fallback to top-level
- Added strict dedup by `event_id` with TTL cache.
- Strengthened fallback dedup for `speech_stop` by tuple:
  - `(interrupt_type, session_id, press_id)` in short window.
- `grpc.request_cancel` now carries through:
  - `session_id`, `press_id`, `event_id`.

Goal: avoid duplicate cancel cascades for same press-cycle/session.

### 3) WelcomeMessageIntegration
File: `/Users/sergiyzasorin/Fix_new/client/integration/integrations/welcome_message_integration.py`

- Welcome playback now publishes `playback.raw_audio` with explicit UUID `session_id`.
- `_send_audio_to_playback` returns that session id.
- `_wait_for_playback_completion(session_id)` now waits by exact session match.
- Wait listens to terminal playback events:
  - `playback.completed`
  - `playback.cancelled`
  - `playback.failed`

Goal: remove false timeout when terminal event exists but old string matcher misses it.

## Verification
- `python3 -m py_compile` on modified files: OK.
- `pytest -q tests/test_speech_playback_session_id.py tests/test_user_quit_ack.py`: 5 passed.

## Expected Runtime Effect
- Fewer duplicate `interrupt.request` side effects.
- Deterministic cancel path in `InterruptManagementIntegration`.
- Welcome wait no longer depends on `"welcome"` substring in session id.
