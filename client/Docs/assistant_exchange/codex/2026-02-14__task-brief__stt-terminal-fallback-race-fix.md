# Task Brief: stt-terminal-fallback-race-fix

## Goal
Убрать race, из-за которого `PROCESSING` мог зависать без terminal STT события после `voice.recording_stop`.

## Changes
- В `VoiceRecognitionIntegration._on_app_mode_changed` отмена stop-terminal fallback больше не выполняется при `AppMode.PROCESSING`.
- Отмена fallback оставлена только для `AppMode.SLEEPING`.
- `_cancel_stop_terminal_fallback` переведён на явный параметр `reason` и логирует причину отмены.
- Обновлены все вызовы отмены fallback в terminal-точках (`v2_completed`, `failed_empty`, `v2_failed`).

## Files
- `integration/integrations/voice_recognition_integration.py`

## Why This Fits Architecture
- Владелец terminal STT остаётся `VoiceRecognitionIntegration`.
- `ModeManagementIntegration` и `ApplicationStateManager` остаются единственным owner смены режимов.
- Новых путей смены режима не добавлено.

## Validation
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py` — passed.

## Expected Runtime Effect
- При stop-while-waiting terminal no-speech fallback не теряется.
- `ProcessingWorkflow` получает terminal событие и не зависает в `sending_grpc`.
