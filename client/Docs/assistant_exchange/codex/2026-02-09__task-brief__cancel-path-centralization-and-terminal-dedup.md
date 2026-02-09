# Task Brief: cancel-path centralization and terminal dedup

## Summary
Сделаны два архитектурных шага для снижения дублей/гонок:
1) Убран конфликт terminal-событий в cancel-ветке playback.
2) Централизована публикация `interrupt.request + grpc.request_cancel` в input.

## Changes

### 1) SpeechPlaybackIntegration terminal dedup
- Файл: `integration/integrations/speech_playback_integration.py`
- В `_on_unified_interrupt`:
  - cancel теперь помечает сессию как `finalized`.
  - на cancel больше **не** публикуется `playback.completed`.
  - terminal-событие cancel-ветки остаётся `playback.cancelled`.

### 2) InputProcessingIntegration cancel centralization
- Файл: `integration/integrations/input_processing_integration.py`
- Добавлен единый метод:
  - `_publish_interrupt_and_cancel(session_id, timestamp, source)`
- Заменены дублирующие куски публикации в:
  - `_handle_press`
  - `_handle_short_tap_cancel`
  - `_handle_short_press` (ветка с активной записью)
  - `_handle_long_press`

## Why it helps
- Убирает двойной terminal path `cancelled + completed` на одной сессии.
- Уменьшает дубли и расхождения в cancel-логике, оставляя один владелец публикации cancel-команд.

## Validation
- `python3 -m py_compile integration/integrations/input_processing_integration.py integration/integrations/speech_playback_integration.py` — успешно.

