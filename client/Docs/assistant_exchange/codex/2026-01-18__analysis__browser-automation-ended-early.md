# Browser Automation Ended Early — Analysis

## Context
- User reports browser automation should run multiple cycles but stops after a single action.
- Provided logs earlier show `grpc.response.audio` stream followed by `StatusCode.DEADLINE_EXCEEDED` and mode transition to SLEEPING.

## Findings
- gRPC audio stream is terminated by deadline, triggering `grpc.request_failed` and `playback.failed`.
- Mode changes to SLEEPING after failure; ActionExecutionIntegration cancels active actions on SLEEPING.
- No `browser.progress` events are visible in the provided log excerpt, so long-running browser task is not confirmed on the client side.

## Likely Cause
- Fixed gRPC `StreamAudio` timeout (30s) ends the stream before additional MCP commands are sent.
- After stream failure, workflow transitions to SLEEPING, cancelling pending actions.

## Fix Direction
- Remove/raise StreamAudio timeout via config and pass it through GrpcClientIntegration.
- Optionally keep PROCESSING alive while browser progress events are active (needs workflow integration).

## References
- `modules/grpc_client/core/grpc_client.py`
- `integration/integrations/grpc_client_integration.py`
- `integration/integrations/action_execution_integration.py`
- `integration/integrations/browser_progress_integration.py`
