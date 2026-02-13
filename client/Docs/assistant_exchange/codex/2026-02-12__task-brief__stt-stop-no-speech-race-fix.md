# STT stop no_speech race fix

## What was fixed
- Removed immediate terminal `no_speech` emission from `GoogleSRController` stop-path.
- Kept terminal no-speech ownership in `VoiceRecognitionIntegration` delayed fallback.

## Why
- Immediate `no_speech` on stop raced with delayed successful final chunk recognition.
- This caused premature `recognition_failed` -> `ProcessingWorkflow` completion -> `mode.request(SLEEPING)`.

## Code changes
- `modules/voice_recognition/core/google_sr_controller.py`
  - stop-flag branch before `listen()` no longer emits terminal `no_speech`.
  - `WaitTimeoutError` + stop branch no longer emits terminal `no_speech`.
  - removed dead helper `_emit_no_speech_terminal()`.

## Expected effect
- For one `session_id`, terminal STT becomes single and stable (`completed` first when available; otherwise fallback `failed`).
- Eliminates false early `PROCESSING -> SLEEPING` transitions triggered by stop-race.

## Verification status
- Static diff reviewed.
- Runtime verification pending in live PTT scenario (recommended: repeated quick-release tests).
