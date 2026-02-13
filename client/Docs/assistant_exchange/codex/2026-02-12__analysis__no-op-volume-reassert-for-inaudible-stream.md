# Analysis: no-op playback volume reassert for inaudible stream

## Diagnosis
Пайплайн аудио и schedule здоровые (ненулевые peak/rms, engine/player running), но звук иногда неслышим.

## Root cause hypothesis
На fast no-op ветке `start_playback()` раньше не было принудительного восстановления `player_node`/`mainMixer` volume. При route/mic churn состояние могло остаться "логически playing, но фактически тихо/нулевой gain".

## Change
- File: `modules/speech_playback/core/avf_player.py`
- In `start_playback()` no-op path (already playing):
  - add `player_node.setVolume_(1.0)`
  - add `engine.mainMixerNode().setOutputVolume_(1.0)`

## Why architecture-safe
- Owner не менялся: recovery внутри AVF playback owner.
- Новых state-owners/flags не добавлено.

## Validation
Command:
`PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_pipeline_diagnostic.py tests/test_microphone_activation.py tests/test_interrupt_playback.py`

Result:
`21 passed`
