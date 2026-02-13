# Task Brief

## Goal
Убрать дубли/конфликты в cancel-ветке `SpeechPlaybackIntegration` и сохранить один архитектурный owner cleanup.

## Changes
- Файл: `integration/integrations/speech_playback_integration.py`
- Вынесены общие операции cancel в единые приватные методы:
  - `_stop_player_locked()`
  - `_is_cancel_dedup(sid, now)`
  - `_arm_cancel_guard(sid, now)`
  - `_apply_cancel_state(sid, source=...)`
- Обновлены входные обработчики:
  - `_on_unified_interrupt(...)` теперь использует общий pipeline.
  - `_on_grpc_cancel(...)` теперь использует тот же общий pipeline + terminal publish.

## Architecture Fit
- Owner не изменён: `SpeechPlaybackIntegration`.
- Централизация достигнута в пределах текущего слоя интеграции.
- Второй источник истины для cancel-cleanup не добавлен.

## Risk/Conflict
- Убрано дублирование cleanup логики между двумя хендлерами.
- Сохранена сериализация через `_playback_op_lock`.
- Сохранена идемпотентность terminal событий через `_emit_terminal_playback_event`.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py`
- `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_grpc_audio_format.py` -> `2 passed`
- `PYTHONPATH=. python3 -m pytest -q tests/test_interrupt_playback.py -k "playback_started or signal"` -> `4 passed, 11 deselected`
