# Analysis: Remaining duplicates/conflicts in audio and cancel flows

## Context
После фикса Quartz autorepeat был выполнен дополнительный анализ на оставшиеся дубли/конфликты по логам Dev.

## Diagnosis
Найдены 2 конфликтные точки:
1) В AVF profile apply была несовместимая распаковка результата `setActive_error_`.
2) В cancel-цепочке была двойная остановка плеера при `grpc_cancel -> playback.cancelled`.

## Root Cause
- `setActive_error_` в разных PyObjC окружениях может вернуть `bool` вместо tuple.
- В `_on_unified_interrupt` dedup-проверка стояла после `stop_player`, поэтому stop вызывался повторно.

## Architecture Fit
- Owner audio-session: `AVFoundationPlayer._ensure_playback_audio_session`.
- Owner cancel lifecycle: `SpeechPlaybackIntegration`.
- Source of Truth не изменен, второй путь не добавлен.

## Changes
1) `modules/speech_playback/core/avf_player.py`
- Нормализован результат `session.setActive_error_(True, None)`:
  - поддержка tuple и bool return.

2) `integration/integrations/speech_playback_integration.py`
- `_is_cancel_dedup`: dedup теперь работает и для `session_id=None`.
- `_on_unified_interrupt`: dedup-проверка перенесена до `_stop_player_locked()`.

3) (ранее в этой же сессии) `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Guard `combo_active_hold` для suppress autorepeat без повторного PRESS.

## Verification
- `python3 -m py_compile` для измененных файлов — OK.
- Кодовая проверка наличия guards/branches:
  - `combo_active_hold`
  - safe handling `setActive_error_`
  - dedup-before-stop в `_on_unified_interrupt`

## Информация об изменениях
- Что изменено:
  - Устранен runtime-конфликт AVAudioSession API возврата (bool/tuple).
  - Устранена двойная остановка плеера в cancel-цепочке.
  - Устранен дубль PRESS на autorepeat удержании Ctrl+N.
- Список файлов:
  - `modules/speech_playback/core/avf_player.py`
  - `integration/integrations/speech_playback_integration.py`
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Причина/цель изменений:
  - Стабилизировать runtime audio/cancel, убрать циклы/дубли и ложные warning/error.
- Проверка:
  - Выполнена синтаксическая проверка `py_compile`.
