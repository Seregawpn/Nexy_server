# Analysis: centralization status and next improvements

Date: 2026-02-10
Assistant: Codex
Type: analysis

## Current status
- Main target is achieved: timeout path no longer emits direct `voice.recording_stop`; it goes through `interrupt.request` and owner path.
- `VoiceRecognitionIntegration` start/stop now serialized with single-flight and has idempotent start guard.

## Remaining gaps (non-blocking but recommended)
1. `VoiceRecognitionIntegration` still subscribes `keyboard.short_press` and performs direct cancel.
   - This is a secondary cancel path outside owner lifecycle decisions.
2. `VoiceRecognitionIntegration` checks controller private field `_listening` indirectly.
   - Better replace with public `is_listening()` API in controller.

## Recommended follow-ups
1. Remove direct `keyboard.short_press` subscription from `VoiceRecognitionIntegration` and rely on owner/interrupt path.
2. Add `GoogleSRController.is_listening()` and use it in integration instead of private field access.
3. Add metric/counter for idempotent start skips to prove guard effectiveness in runtime.
