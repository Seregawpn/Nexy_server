# Task Brief — Remove gRPC StreamAudio Deadline

## Goal
Remove the hardcoded StreamAudio timeout and disable the client-side deadline for long-running browser automation.

## Changes
- Added optional timeout parameter to `GrpcClient.stream_audio` and removed the hardcoded 30s deadline.
- Wired `request_timeout_sec` from `GrpcClientIntegration` to the stream call (0 disables deadline).
- Set `integrations.grpc_client.request_timeout_sec` to `0.0` in `config/unified_config.yaml`.

## Files
- `modules/grpc_client/core/grpc_client.py`
- `integration/integrations/grpc_client_integration.py`
- `config/unified_config.yaml`

## Verification
- Run a long browser automation (1–2 minutes) and confirm no `DEADLINE_EXCEEDED` in logs.
