# Analysis: PROCESSING stuck after press/release with no recognized speech

## Summary
Observed symptom: after long-press + release with silence/no recognized speech, app can stay in `PROCESSING`.

## Root cause (verified in code)
1. `InputProcessingIntegration` always sends `mode.request -> PROCESSING` on release (`integration/integrations/input_processing_integration.py`).
2. `ProcessingWorkflow` starts chain and moves to `capturing -> sending_grpc`, then waits for terminal events (`grpc.request_completed/failed` or `voice.recognition_failed` + playback completion) (`integration/workflows/processing_workflow.py`).
3. In silence branch, `VoiceRecognitionIntegration` can stop listening without guaranteed publication of `voice.recognition_failed` for that session (`integration/integrations/voice_recognition_integration.py`, `modules/voice_recognition/core/google_sr_controller.py`).
4. No gRPC request starts without recognized text (`integration/integrations/grpc_client_integration.py`), so `grpc.request_*` terminal events are absent.
5. Result: no terminal trigger for `ProcessingWorkflow`, mode remains `PROCESSING` until global timeout.

## Architecture fit
- Source of truth for mode is correct (`ModeManagementIntegration`).
- Defect is missing terminal event contract in STT/processing chain, not mode manager logic.

## Fix direction
- Add guaranteed terminal publication for release+silence path: emit `voice.recognition_failed(session_id, reason=no_speech_after_release)` exactly once.
- In `ProcessingWorkflow`, if `recognition_failed` arrives and no session-scoped playback starts in short window, finalize to `SLEEPING` (no dependency on signal-only playback).

## Risks
- Duplicate terminal events/races between stop/cancel callbacks.
- Must enforce idempotency by `session_id` in VoiceRecognition and ProcessingWorkflow.
