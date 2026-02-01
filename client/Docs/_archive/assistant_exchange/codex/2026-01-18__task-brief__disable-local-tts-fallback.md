# Task Brief: Disable local TTS fallback

## Goal
Disable local macOS `say` fallback for `grpc.tts_request` so only server TTS is used.

## Changes
- Removed fallback publish to `speech.playback.request` in `GrpcClientIntegration._on_tts_request`.
- Updated REQ-007 to document server-only TTS for `grpc.tts_request`.

## Files
- `integration/integrations/grpc_client_integration.py`
- `Docs/PROJECT_REQUIREMENTS.md`

## Tests
- Not run (logic change only).

## Notes
- Flags discovery run for `grpc_client_integration.py` (no flags found).
