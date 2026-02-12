# Task Brief: Listen-start cue audibility fix

## Context
Пользователь не слышит сигнал активации режима listening, хотя в логах есть `signal.emit`, `playback_signal.queued`, `avf.render_start`.

## Diagnosis
Источник проблемы — слишком тихий профиль cues (в коде жёстко `volume=0.22`) и отсутствие чтения конфиг-профилей для `listen_start/done/error/cancel`.

## Changes
- `integration/integrations/signal_integration.py`
  - Убрана жёсткая статическая громкость для всех паттернов.
  - Добавлен централизованный builder `_build_audio_profile()`:
    - берёт значения из `config.patterns` (если заданы),
    - иначе применяет слышимые дефолты.
  - Добавлен `_clamp_volume()` для безопасной нормализации 0..1.
- `config/unified_config.yaml`
  - Добавлены явные `signals.patterns` для:
    - `listen_start` (1046Hz, 160ms, 0.4)
    - `done` (880Hz, 140ms, 0.28)
    - `error` (740Hz, 180ms, 0.32)
    - `cancel` (660Hz, 140ms, 0.3)

## Why this fits architecture
- Единый владелец сигналов сохранён: `SignalIntegration`.
- Нет второго пути принятия решений; только централизованный конфиг + integration owner.

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`
- Result: `22 passed`.

## Expected result
Сигнал `listen_start` становится слышимым и предсказуемым без изменения маршрута событий и без локальных обходов в playback/input.
