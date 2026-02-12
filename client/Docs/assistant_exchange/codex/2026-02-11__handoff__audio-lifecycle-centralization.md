# Audio Lifecycle Centralization Handoff

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-11
- ID (INS-###): INS-N/A

## Diagnosis
В TTS и signal-ветках были нецентрализованные публикации lifecycle/cue событий, что создавало риск дублей и orphan-контрактов.

## Root Cause
Частичная миграция на server-TTS и Signals owner оставила legacy-публикации без единого владельца terminal/start семантики.

## Optimal Fix
- Убрана ручная публикация `playback.started` из `GrpcClientIntegration._play_server_tts`.
- Для `grpc.tts_request` добавлен явный terminal upstream: `grpc.request_completed` (успех) / `grpc.request_failed` (ошибка).
- В `SignalIntegration` добавлен owner-handler `signal.play` с маппингом в канонические `SignalPattern`.
- Исправлен misleading docstring в ActionExecution (`speech.playback.request` -> `grpc.tts_request`).

## Verification
- `python3 -m py_compile integration/integrations/grpc_client_integration.py integration/integrations/signal_integration.py integration/integrations/update_notification_integration.py`
- `python3 -m py_compile integration/integrations/action_execution_integration.py`

## Запрос/цель
Централизация аудио-управления: убрать конфликты/дубли/гонки в playback и signal lifecycle.

## Контекст
- Файлы: 
  - `integration/integrations/grpc_client_integration.py`
  - `integration/integrations/signal_integration.py`
  - `integration/integrations/action_execution_integration.py`
- Документы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`

## Решения/выводы
- Playback lifecycle owner сохранен в `SpeechPlaybackIntegration`.
- TTS path теперь всегда завершает gRPC lifecycle-событиями.
- Update cue path больше не orphan: routed through `SignalIntegration`.

## Открытые вопросы
- Нужна ли формальная фиксация `signal.play` как поддерживаемого контракта в `Docs/FLOW_INTERACTION_SPEC.md`.

## Следующие шаги
- Прогнать runtime сценарии: `grpc.tts_request`, interrupt во время TTS, update start/success/error cues.
