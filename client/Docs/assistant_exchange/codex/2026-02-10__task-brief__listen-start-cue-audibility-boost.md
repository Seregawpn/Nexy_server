# Task Brief: Listen-start cue audibility boost

## Context
По runtime-логам сигнал `listen_start` проходит весь pipeline (`signal.emit -> sink.publish -> playback.signal -> avf.render_start`), но пользователь не слышит его стабильно.

## Diagnosis
Проблема не в доставке события, а в субъективной слышимости на целевом output route (AirPods) при коротком/умеренно тихом профиле.

## Change
- `config/unified_config.yaml`
  - `signals.patterns.listen_start` усилен:
    - `tone_hz: 1200`
    - `duration_ms: 220`
    - `volume: 0.65`

## Architecture fit
- Source of truth сохранён: `SignalIntegration` + централизованный конфиг.
- Новых путей/состояний/локальных обходов не добавлено.

## Expected
Сигнал входа в `LISTENING` становится заметно слышимым даже при менее благоприятном аудио-маршруте.
