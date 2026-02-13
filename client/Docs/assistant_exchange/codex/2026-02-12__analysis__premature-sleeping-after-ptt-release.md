# Premature sleeping after PTT release (voice no_speech race)

## Context
- User symptom: after voice request app immediately returns to `SLEEPING`.
- Evidence source: runtime logs around `2026-02-12 12:11:24` to `12:11:28`.

## Findings
1. `ProcessingWorkflow` treats early `voice.recognition_failed` as terminal and immediately completes chain:
   - `integration/workflows/processing_workflow.py:337-365`
2. `GoogleSRController` can emit `no_speech` on stop while a final audio chunk is still being recognized in a background thread:
   - `modules/voice_recognition/core/google_sr_controller.py:229-233`
   - final chunk path exists in `modules/voice_recognition/core/google_sr_controller.py:203-216`
3. `VoiceRecognitionIntegration` enforces first terminal STT event per session; later success is deduped:
   - `integration/integrations/voice_recognition_integration.py:741-754`
   - `integration/integrations/voice_recognition_integration.py:875-888`

## Causal chain
- `recording_stop` -> stop flag set.
- listener loop hits timeout branch with stop -> emits terminal `no_speech`.
- `ProcessingWorkflow` gets `voice.recognition_failed` before `grpc.request_started` and returns to `SLEEPING`.
- later background recognition completes with valid text, but terminal dedup drops it (`terminal STT dedup` in logs).

## Architecture-fit fix direction
- Keep terminal ownership in `VoiceRecognitionIntegration` (single source of truth for terminal STT event).
- In `GoogleSRController`, suppress immediate `no_speech` terminal on stop-path when final recognition may still arrive.
- Use delayed fallback `no_speech` (already exists in integration) as the only no-speech terminal for stop-path.

## Risk
- Current behavior causes false terminal fail and early mode rollback.
- Fix should reduce race without introducing a second mode owner.
