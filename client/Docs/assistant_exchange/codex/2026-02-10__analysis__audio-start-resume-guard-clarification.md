# Clarification: single owner for audio start/resume

Date: 2026-02-10
Assistant: Codex
Type: analysis

## Request
Пояснить, что означает:
- идемпотентный guard на start/resume;
- сведение триггеров старта/остановки аудио в один вход.

## Concrete mapping in current code
- Owner PTT lifecycle already exists: `integration/integrations/input_processing_integration.py`.
- Audio start currently happens in `integration/integrations/voice_recognition_integration.py` via `_on_recording_start -> start_listening()`.
- Parallel path detected: `integration/workflows/listening_workflow.py` publishes `voice.recording_stop` from `_timeout_monitor`, i.e. second control path for recording lifecycle.

## Meaning of the proposal
1. Guard:
   - Before `start_listening()` check state and skip repeated calls if already in `starting/running`.
   - Prevent duplicate starts when close-timed events overlap.

2. Single entry:
   - Keep only one publisher/owner for `voice.recording_start/stop` decisions.
   - `ListeningWorkflow` should not directly publish `voice.recording_stop`; it should request stop via owner event, and owner emits terminal recording event.

## Expected effect
- Fewer duplicate StartIO attempts.
- No competing start/stop control branches.
- Cleaner logs and deterministic audio lifecycle.
