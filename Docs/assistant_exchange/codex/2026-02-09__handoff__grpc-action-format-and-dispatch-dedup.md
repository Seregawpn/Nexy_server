# Handoff: gRPC action format contract and dispatch dedup

## Implemented
- gRPC action payload canonicalization in client stream handler:
  - canonical shape: `{"command": "...", "args": {...}}`
  - legacy adapter: `{"type": "..."}` -> canonical with warning.
- Action dispatch dedup in stream processing:
  - `action_message` is primary and immediate.
  - text command extraction is deferred fallback only when no `action_message` was received/dispatched.
- Removed dead variable `action_message_sessions` from stream loop.
- Updated protobuf comments (client/server) for `ActionMessage.action_json` to canonical format.

## Files changed
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/modules/grpc_client/proto/streaming.proto`
- `/Users/sergiyzasorin/Fix_new/server/server/modules/grpc_service/streaming.proto`

## Validation
- `python3 -m py_compile` passed for:
  - `grpc_client_integration.py`
  - `speech_playback_integration.py`

## Follow-up cleanup (next)
- Remove legacy adapter branch after server fully emits canonical `command/args`.
- Remove text command fallback entirely once `action_message` is guaranteed for actionable commands.
