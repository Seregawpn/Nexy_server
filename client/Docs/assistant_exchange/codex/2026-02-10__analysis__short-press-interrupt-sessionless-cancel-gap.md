# Short Press Interrupt: sessionless cancel gap

## Context
- Симптом: короткое нажатие во время хвоста воспроизведения не останавливает аудио.
- Лог подтверждает: `interrupt.request` приходит, но `speech.stop_requested` имеет `subscribers=0`, а `grpc.request_cancel` не приводит к остановке, когда `session_id=None`.

## Diagnosis
- В `InputProcessingIntegration` short tap может легально публиковать `interrupt.request` с `session_id=None` (после `grpc_completed` и reset state).
- В `InterruptManagementIntegration` публикация `grpc.request_cancel` условная: только если `session_id is not None`.
- В результате единый cancel-канал (`grpc.request_cancel -> SpeechPlaybackIntegration -> playback.cancelled`) не активируется в sessionless-окне.

## Root cause chain
1. `grpc.request_completed` сбрасывает session в input (`_reset(...)->_set_session_id(None)`).
2. Пользователь делает short press в хвосте playback.
3. `interrupt.request(type=speech_stop, session_id=None)` публикуется корректно.
4. `InterruptManagementIntegration` логирует `grpc.request_cancel опубликован`, но реально не публикует событие из-за guard `if session_id is not None`.
5. `SpeechPlaybackIntegration` не получает `grpc.request_cancel`, плеер не останавливается.

## Architecture fit
- Owner interrupt orchestration: `InterruptManagementIntegration`.
- Source of truth cancel path: `interrupt.request -> grpc.request_cancel -> playback.cancelled` (см. `Docs/FLOW_INTERACTION_SPEC.md` 4.6).
- Исправление должно быть в owner-слое interrupt, не в локальном обходе input/speech.

## Primary fix
- В `InterruptManagementIntegration._on_interrupt_request` для `speech_stop` публиковать `grpc.request_cancel` всегда, даже при `session_id=None`.
- Payload оставлять с `session_id` (включая `None`), чтобы подписчики применяли собственный fallback:
  - `GrpcClientIntegration._on_request_cancel`: умеет отменять последний inflight при отсутствии session.
  - `SpeechPlaybackIntegration._on_grpc_cancel`: синхронно очищает queue/stop независимо от session.

## Anti-race / dedup
- Существующий dedup по `(interrupt_type, sid_key)` оставить.
- Дополнительно не вводить новые флаги в input/speech, чтобы не создавать второй путь cancel.

## Verification checklist
1. Запустить сценарий: дождаться `grpc.request_completed`, во время хвоста audio сделать short press.
2. Убедиться в логах:
   - есть `interrupt.request ... final.session_id=None`;
   - есть `grpc.request_cancel` dispatch;
   - в `SpeechPlaybackIntegration` сработал `_on_grpc_cancel` и `stop_playback`;
   - опубликован `playback.cancelled`.
3. Проверить отсутствие регрессии:
   - обычный interrupt с валидным session_id;
   - двойной short press (dedup окно);
   - mode transition остается централизованным через InterruptManagement.

## Code touchpoints
- `integration/integrations/interrupt_management_integration.py`
- (без изменений логики в) `integration/integrations/input_processing_integration.py`
- (без изменений логики в) `integration/integrations/speech_playback_integration.py`
