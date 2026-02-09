# Task Brief: Fix PROCESSING stuck on release + no speech

## Goal
Устранить зависание режима `PROCESSING` в ветке: long-press -> release -> речи нет/не распознано.

## Implemented
1. `integration/integrations/voice_recognition_integration.py`
- Добавлен idempotent terminal guard по `session_id` (`_try_mark_terminal_recognition`).
- На `recording_stop` теперь:
  - вызывается `stop_listening()` и читается snapshot результата;
  - при наличии snapshot сразу публикуется terminal STT (`voice.recognition_completed` или `voice.recognition_failed`);
  - если snapshot пустой — запускается fallback-задача (`1.2s`) и публикуется `voice.recognition_failed(reason=no_speech_after_release)`.
- Добавлен cancel fallback-задачи при cancel/mode switch/успешном terminal callback.

2. `integration/workflows/processing_workflow.py`
- Добавлен флаг `grpc_started`.
- В `_on_recognition_failed` добавлена ветка:
  - если `current_stage == SENDING_GRPC` и `grpc_started == False`, цепочка завершается сразу (без ожидания playback).
- Сброс `grpc_started` в start/cleanup.

## Architecture Fit
- Владелец режима не менялся: только `mode.request` -> `ModeManagementIntegration`.
- Source of Truth сохранен.
- Убрана зависимость от несессионного `playback.signal` в ветке no-speech.

## Verification
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py integration/workflows/processing_workflow.py` — OK.

## Expected runtime result
- При release без распознанной речи теперь гарантирован terminal исход по `session_id`.
- `ProcessingWorkflow` не остается в `PROCESSING` из-за отсутствия gRPC/playback terminal-событий.

## Update (2026-02-09, follow-up)
- Расширен guard в `ProcessingWorkflow._on_recognition_failed`:
  - завершение chain выполняется при `grpc_started == False` на pre-gRPC этапах `STARTING/CAPTURING/SENDING_GRPC`.
- Причина: в реальном логе `recognition_failed` может приходить, пока workflow еще не успел перейти в `SENDING_GRPC` (гонка порядка событий), что оставляло режим в `PROCESSING`.
