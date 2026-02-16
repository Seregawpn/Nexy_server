# Analysis

## User Issue
Browser install completed but user did not hear install status voice messages.

## Root Cause
Two startup timing gaps could drop audible feedback:
1. Browser startup/install TTS waiting gate depended on welcome lifecycle; if welcome event did not arrive quickly, messages were delayed.
2. `grpc.tts_request` could be processed before gRPC transport was connected; `_play_server_tts` attempted stream without explicit `ensure_connected`, so startup TTS could fail silently from user perspective.

## Fixes Applied

1. `integration/integrations/grpc_client_integration.py`
- In `_play_server_tts(...)` added mandatory connection guard:
  - `await self._ensure_connected()` before streaming.
  - One retry after 0.5s if first connect check fails.
  - Explicit error log and skip only after failed retry.

2. `integration/integrations/browser_use_integration.py`
- Subscribed to both `welcome.completed` and `welcome.failed` to release queued startup browser TTS.
- Reduced welcome wait timeout from 20s to 8s to avoid long silent delays.

## Validation
- `python3 -m py_compile integration/integrations/browser_use_integration.py integration/integrations/grpc_client_integration.py`
- Result: success.

## Expected Outcome
- Browser install/start/completed/already-installed TTS is no longer dropped due to gRPC startup readiness.
- Startup install TTS queue is released faster and also on `welcome.failed` path.
