# Task Brief: cancel-cue-dedup-centralization

## Goal
Стабилизировать воспроизведение cancel-сигнала без дублей и без конфликтов с cancel-guard.

## Changes
- Удалено подавление `playback.signal` с `pattern=cancel` по правилу `cancel_in_flight`.
- Добавлен централизованный дедуп cancel-cue в `SpeechPlaybackIntegration`:
  - dedup по `cue_id`;
  - dedup по короткому окну `0.30s`.
- Первый валидный cancel-cue теперь принимается даже в `cancel_in_flight` окне.
- Добавлены диагностические причины `drop_reason` для dedup.

## File
- `integration/integrations/speech_playback_integration.py`

## Architecture
- Owner принятия/дедупа playback cue остается `SpeechPlaybackIntegration`.
- Owner эмиссии cue остается `SignalIntegration`.
- Новых путей событий не добавлено.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` — passed.
