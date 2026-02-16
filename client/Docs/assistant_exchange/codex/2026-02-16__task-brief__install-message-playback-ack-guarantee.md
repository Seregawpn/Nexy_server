# Task Brief

## Context
User repeatedly reported that browser was installed but install-complete audio message was not heard.

## Root Problem
One-shot startup TTS publish could occur, but delivery-to-playback was not acknowledged. Status could be true while user-facing audio delivery was false.

## Changes Applied

### 1) Ack-based install announcement delivery
File: `integration/integrations/browser_use_integration.py`

- Added playback terminal subscriptions:
  - `playback.completed`
  - `playback.failed`
  - `playback.cancelled`

- Introduced install announcement delivery tracking:
  - `_install_delivery_pending: dict[session_id -> {text, retries_left}]`
  - session_id for install announcements now unique: `browser_install_announce_<id>`

- For install statuses:
  - `completed` and `already_installed` now require delivery ack.
  - `started` remains informational without ack requirement.

- Behavior:
  - On `playback.completed` for tracked session -> mark delivered and clear pending.
  - On `playback.failed/cancelled` -> retry with new session_id (bounded retries).

### 2) Existing startup race hardening kept
- `grpc.tts_request` subscriber readiness wait before publish.
- gRPC connect retries in `GrpcClientIntegration._play_server_tts` (already added earlier).

## Tests Updated
File: `tests/test_browser_install_contracts.py`

Added/updated coverage:
1. already-installed announcement uses dedicated ack session_id.
2. install completion announcement retries on `playback.failed` and re-emits with new session_id.
3. existing transport readiness tests retained.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py tests/test_browser_install_contracts.py`
- `pytest -q tests/test_browser_install_contracts.py`
- Result: `5 passed`

## Architecture Gates
- Single Owner Gate: PASS (state vs UX owners preserved)
- Zero Duplication Gate: PASS (no second UX path introduced)
- Anti-Race Gate: PASS (ack + bounded retry for startup one-shot delivery)
- Flag Lifecycle Gate: PASS (no new feature flags)
