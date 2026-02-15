# STT fallback vs late completion race (2026-02-15)

## Context
User reported: after speaking, system resets to sleeping and request is not accepted.

## Evidence from logs
- `voice.recording_stop` at `13:42:34.561`.
- Fallback terminal published as failed at `13:42:35.764`: `reason=no_speech_after_release`.
- Processing finalized failed and requested sleeping immediately after.
- Real STT success arrived later at `13:42:36.104`: `STT: how are you doing today`.
- Late success was dropped by terminal dedup: `VOICE: terminal STT dedup (... source=completed)`.

## Architecture fit
- Owner of terminal STT decision: `integration/integrations/voice_recognition_integration.py`.
- Owner of mode transition: `integration/integrations/mode_management_integration.py` via `mode.request`.
- ProcessingWorkflow correctly delegates terminal mode decision through `processing.terminal`.

## Root cause
Too short fixed fallback window (`_stop_terminal_fallback_sec = 1.2`) races with delayed final Google recognition callback. Fallback emits terminal failure first; dedup then blocks later valid completion.

## Primary fix
1. Keep single terminal owner in `VoiceRecognitionIntegration`.
2. Guard fallback with controller in-flight finalization state (or minimum adaptive grace) so fallback cannot fire while final chunk recognition is still running.
3. Allow terminal override only from `pending_fallback_no_speech -> completed` for same session within grace (or postpone failure publication until controller confirms no in-flight recognition).
4. Keep downstream centralized path unchanged (`voice.recognition_*` -> `ProcessingWorkflow` -> `processing.terminal` -> `ModeManagementIntegration`).

## Concurrency guard
- Mechanism: per-session state guard (`terminal_pending`, `terminal_finalized`) with idempotent finalize.
- Rule: only one terminal event is emitted, but fallback may wait until final recognizer state settles.

## Verification targets
- Release with short trailing speech: must end in `voice.recognition_completed`, not `failed_recognition`.
- No duplicate terminal events for same session.
- `mode.request SLEEPING` occurs only after true terminal outcome.
