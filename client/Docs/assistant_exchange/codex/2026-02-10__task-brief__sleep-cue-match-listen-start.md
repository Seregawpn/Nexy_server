# Sleep Cue Match Listen Start

## Что сделано
- В `integration/integrations/signal_integration.py` профиль `SignalPattern.DONE` приведен к тем же параметрам, что `SignalPattern.LISTEN_START`:
  - `tone_hz=880`
  - `duration_ms=120`
  - `volume=0.22`
- В `modules/signals/channels/audio_tone.py` удалена специальная ветка генерации двухтоновой мелодии для `done`.
- Теперь `done` и `listen_start` проходят через одинаковую генерацию `_generate_tone_bytes(...)`.

## Почему
- Нужен абсолютно одинаковый звук при:
  - активации режима listening,
  - переходе processing -> sleeping (done).
- Ранее `done` имел отдельный тоновый профиль и отдельную мелодию, из-за чего звучал иначе.

## Проверка
Запущены целевые тесты:

```bash
PYTHONPATH=. pytest -q \
  tests/test_signal_integration_cancel_done_suppression.py \
  tests/test_interrupt_playback.py \
  tests/test_processing_workflow_session_guard.py
```

Результат: `22 passed`.

## Риск
- Минимальный: изменение локализовано в профиле и генерации аудио-сигналов.
