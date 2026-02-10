# Analysis: ActionMessage contract and missing action execution

## Context
User reported intermittent behavior where assistant voice confirms an action (e.g. send message), but no action is executed.

## Verified contract
- Server gRPC proto defines action as `StreamResponse.action_message`.
- Server emits actions in `/Users/sergiyzasorin/Fix_new/server/server/modules/grpc_service/core/grpc_server.py` from `item['command_payload']`.
- Client accepts action only from `WhichOneof('content') == 'action_message'` in `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`.
- Executor runs only on `grpc.response.action` in `/Users/sergiyzasorin/Fix_new/client/integration/integrations/action_execution_integration.py`.

## Key finding
If server returns only text/audio confirmation and does not emit `action_message`, client correctly does not execute any action.

## Additional race/behavior observed from logs
- Some sessions were marked cancelled and playback integration ignored further audio chunks for that `sid` (`Ignoring audio chunk for cancelled sid=...`).
- In successful runs, playback path is healthy (`PLAYBACK_END ... exit_reason=queue_drained`, `had_audio=True`).

## Architecture-safe fix direction
1. Keep single source of truth: action execution trigger = `action_message` only.
2. Add server-side guard/telemetry when text indicates intent but `command_payload` missing (detect and fail fast/explicitly).
3. Add end-to-end assertion in tests: for actionable intents, stream must include exactly one `action_message`.
4. Do not add client-side text parsing fallback for actions (would create a second decision path).

## Files relevant for implementation
- `/Users/sergiyzasorin/Fix_new/server/server/modules/grpc_service/streaming.proto`
- `/Users/sergiyzasorin/Fix_new/server/server/modules/grpc_service/core/grpc_server.py`
- `/Users/sergiyzasorin/Fix_new/server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
- `/Users/sergiyzasorin/Fix_new/server/server/integrations/core/assistant_response_parser.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/action_execution_integration.py`
