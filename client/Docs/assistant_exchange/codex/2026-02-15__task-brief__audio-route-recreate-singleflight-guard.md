# Audio route recreate single-flight guard (VoiceOver conflict hardening)

## Context
При одновременной работе Nexy + VoiceOver в unified log наблюдались:
- `Found 2 different sessions`
- `HALC_ProxyIOContext::_StartIO(): ... error 35`

Это указывает на конкуренцию/дребезг route-change и повторные рестарты audio graph.

## Root cause
В `AVFoundationPlayer._on_route_change()` каждый route-change запускал новый background `recreate` поток.
При серии быстрых событий это могло запускать overlapping recreate/start циклы.

## Change
Файл: `modules/speech_playback/core/avf_player.py`

1. Добавлен guard-состояние:
- `_route_recreate_in_flight`
- `_last_route_recreate_ts`
- `_route_recreate_min_interval_sec=1.0`

2. В `_on_route_change()`:
- если recreate уже в полете -> событие игнорируется;
- если событие пришло слишком рано (debounce) -> игнорируется;
- recreate запускается через обертку `_recreate_with_guard()` с `finally`-сбросом in-flight флага.

## Architecture fit
- Owner логики остается `AVFoundationPlayer`.
- Новых внешних флагов/источников истины не добавлено.
- Убран race-path на уровне owner-компонента.

## Verification
- `PYTHONPATH=. .venv/bin/python -m py_compile modules/speech_playback/core/avf_player.py` -> OK
- `PYTHONPATH=. .venv/bin/python -m unittest discover -s tests -p 'test_quartz_monitor_chord_logic.py'` -> OK

## Expected impact
- Меньше recreate-штормов при дергании аудиомаршрутов/VoiceOver.
- Ниже вероятность StartIO ошибок из-за overlapping restart sequence.
