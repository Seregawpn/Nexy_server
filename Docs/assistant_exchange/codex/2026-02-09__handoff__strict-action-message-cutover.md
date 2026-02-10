# Handoff: strict action_message cutover

## Implemented now

1. Strict action dispatch path in gRPC integration
- Removed text-based command extraction from `text_chunk` and combined text.
- Removed fallback publish of `grpc.response.action` from text.
- Action is now accepted only from protobuf `action_message`.

2. Strict action payload format
- Removed legacy adapter (`type -> command`).
- `action_message.action_json` must be canonical JSON:
  - `{ "command": "...", "args": { ... } }`
- Invalid payloads are ignored with warning.

3. Existing dedup cleanups kept
- Mode manager action accounting uses lifecycle events only.
- Playback finalize idempotency remains active.

## Files touched in this step
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`

## Validation
- `python3 -m py_compile` passed for:
  - `grpc_client_integration.py`
  - `mode_management_integration.py`
  - `speech_playback_integration.py`

## Expected behavior after cutover
- `grpc.response.action` source should be only `action_message`.
- Text chunks no longer trigger action execution.
- Legacy action payload shape (`type/...`) is no longer accepted.
