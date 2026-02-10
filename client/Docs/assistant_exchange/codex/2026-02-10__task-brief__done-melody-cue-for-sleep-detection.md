# Task Brief: DONE melody cue for sleep detection

## Problem
По логам terminal `DONE` публикуется, но на слух сложно уверенно отличить его в реальном потоке.

## Change
- В `modules/signals/channels/audio_tone.py` добавлена генерация короткой мелодии для `SignalPattern.DONE`:
  - 2 тона подряд с короткой паузой (`gap_ms=18`)
  - частоты: `hz` и `hz * 1.32`
  - длительности: `55%` и `45%` от `duration_ms`

## Architecture
- Владелец политики сигнала не изменен: `SignalIntegration`.
- Канал `AudioToneChannel` отвечает только за форму PCM (реализация), без новых источников событий.

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- `22 passed`

