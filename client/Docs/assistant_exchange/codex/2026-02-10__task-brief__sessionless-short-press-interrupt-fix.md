# Sessionless short-press interrupt fix

## Что сделано
- Исправлен owner cancel-цепочки в `InterruptManagementIntegration`:
  - `grpc.request_cancel` теперь публикуется всегда для `speech_stop`, включая кейс `session_id=None`.
  - Лог публикации приведен к фактическому payload (`session_id` включен в сообщение).

## Почему это исправляет проблему
- При short press после `grpc.request_completed` session может быть уже очищен.
- Ранее cancel-событие не публиковалось при `session_id=None`, поэтому `SpeechPlaybackIntegration` не останавливал плеер.
- Теперь единый поток прерывания сохраняется: `interrupt.request -> grpc.request_cancel -> playback.cancelled`.

## Архитектурное соответствие
- Владелец прерывания не менялся: `InterruptManagementIntegration`.
- Второй путь остановки не добавлялся.
- Централизация и single source of truth сохранены.

## Измененные файлы
- `integration/integrations/interrupt_management_integration.py`
