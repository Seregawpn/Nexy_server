# Analysis: processing-stuck-fallback-race

## Context
Проверен лог от 2026-02-14 15:25:52–15:26:04 и связанные владельцы логики в `VoiceRecognitionIntegration`, `ProcessingWorkflow`, `ModeManagementIntegration`.

## Diagnosis
`PROCESSING` залипает, когда после `voice.recording_stop` не приходит terminal STT событие (`voice.recognition_completed`/`voice.recognition_failed`).

## Root Cause
- В `VoiceRecognitionIntegration` после `recording_stop` планируется fail-safe fallback (`_schedule_stop_terminal_fallback`) для no-speech.
- Но при переходе режима в `PROCESSING` выполняется `_on_app_mode_changed`, который отменяет этот fallback (`_cancel_stop_terminal_fallback`).
- Если в это окно GoogleSR не присылает terminal callback (типично: `Stop requested while waiting for speech`), terminal STT не публикуется.
- Без terminal STT `GrpcClientIntegration` не получает текст и не публикует `grpc.request_started`/`grpc.request_failed`, а `ProcessingWorkflow` остается в `sending_grpc` до `total_timeout=300s`.

## Evidence
- Fallback планируется: `integration/integrations/voice_recognition_integration.py:840`
- Fallback отменяется на `AppMode.PROCESSING`: `integration/integrations/voice_recognition_integration.py:467` и `integration/integrations/voice_recognition_integration.py:475`
- В workflow no-speech terminal ожидается до `grpc.request_started`: `integration/workflows/processing_workflow.py:366`
- Таймаут-заглушка только 300s: `integration/workflows/processing_workflow.py:48`

## Architecture Fit
- Где должна жить фиксация terminal STT: `VoiceRecognitionIntegration` (owner речевого terminal события).
- Source of Truth по режимам/сессии не меняется: `ModeManagementIntegration` + `ApplicationStateManager`.
- Centralization сохраняется: новый путь mode transition не добавляется.

## Recommended Fix (primary)
1. Не отменять `_stop_terminal_fallback` при `new_mode == AppMode.PROCESSING` в `_on_app_mode_changed`.
2. Отменять fallback только при фактическом terminal STT (`_publish_v2_completed`, `_publish_v2_failed`, snapshot terminal), как уже делается.
3. (Опционально) Логировать явный `VOICE: fallback cancelled by terminal`, чтобы видеть корректный owner-путь.

## Risk Check
- Duplication risk: low
- Race risk: low (уменьшается)
- New state introduced: no
- Centralized: yes
- Breaks architecture: no

## Verification
1. Удержание PTT без речи, отпускание в обычном сценарии.
2. Проверить, что в течение ~1.2s после `voice.recording_stop` приходит `voice.recognition_failed` с `reason=no_speech_after_release` при отсутствии Google callback.
3. Проверить, что `ProcessingWorkflow` уходит из `sending_grpc` в terminal path и публикует `mode.request -> SLEEPING` без ожидания 300s.
