# Task brief: finalize centralization by removing secondary cancel path

Date: 2026-02-10
Assistant: Codex
Type: task-brief

## Implemented
1. `VoiceRecognitionIntegration`
   - Removed direct subscription to `keyboard.short_press`.
   - Removed secondary local cancel handler path (`_on_cancel_request`).
   - Kept cancel/stop decisions through owner-driven lifecycle paths.
   - Added dedup counter `self._dedup_start_skips` for runtime observability.
   - Kept serialized start/stop transitions via `_audio_transition_lock`.

2. `GoogleSRController`
   - Added public `is_listening()` accessor.
   - Integration now prefers this public API (with backward-compatible fallback).

## Validation
- `python3 -m py_compile` passed:
  - `integration/integrations/voice_recognition_integration.py`
  - `modules/voice_recognition/core/google_sr_controller.py`
- Grep confirms no remaining `keyboard.short_press` / `_on_cancel_request` usage in `VoiceRecognitionIntegration`.
