# Task Brief: Playback Cancel Single-Owner Path

Date: 2026-02-11

## Context
В `SpeechPlaybackIntegration` существовали два параллельных пути обработки cancel:
- `_on_grpc_cancel` (остановка/guard/публикация)
- `_on_unified_interrupt` (остановка/guard/очистка)

Это увеличивало сложность и риск race/duplication при почти одновременных `grpc.request_cancel` и `playback.cancelled`.

## Change
Файл:
- `integration/integrations/speech_playback_integration.py`

Сделано:
- `_on_grpc_cancel` оставлен только как publisher канонического terminal-события `playback.cancelled`.
- Вся фактическая обработка cancel (остановка плеера, очистка очереди, guard-механика, session cleanup) оставлена в одном owner-обработчике: `_on_unified_interrupt`.

Итог:
- единый runtime-owner cancel side effects;
- меньше параллельных мутаций одного и того же состояния.

## Verification
Команды:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py::TestInterruptPlayback::test_grpc_cancel_publishes_playback_cancelled_with_source_payload tests/test_interrupt_playback.py::TestInterruptPlayback::test_speech_playback_handles_interrupt_idempotently`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "grpc_cancel or interrupt_idempotently"`

Результат:
- `2 passed`
- `2 passed, 19 deselected`

## Risk Notes
- Изменение точечное, ограничено cancel-path в одном файле.
- Контракт `playback.cancelled` сохранен.
