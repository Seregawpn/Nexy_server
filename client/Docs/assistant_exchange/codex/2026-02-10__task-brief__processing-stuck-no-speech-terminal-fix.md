# Processing Stuck Fix for No-Speech Stop Path

## Симптом
Иногда после `LISTENING -> PROCESSING` режим зависал в `PROCESSING`, если отпускание PTT происходило в ветке `Stop requested while waiting for speech`.

## Корень
В `GoogleSRController` в ветке `WaitTimeoutError + stop` цикл завершался без terminal callback (`on_failed/on_completed`), поэтому downstream не всегда получал `voice.recognition_failed`.

## Изменение
Файл: `modules/voice_recognition/core/google_sr_controller.py`
- В ветках раннего выхода по stop добавлен terminal emit:
  - при `Stop flag detected, breaking loop`
  - при `Stop requested while waiting for speech`
- Добавлен метод `_emit_no_speech_terminal()`:
  - выставляет `last_error = "no_speech"`
  - увеличивает `failed`
  - вызывает `self._on_failed("no_speech")`

## Ожидаемый эффект
Даже если ни один аудиочанк не был распознан, pipeline получает terminal failure и корректно завершает `PROCESSING -> SLEEPING`.

## Проверка
```bash
PYTHONPATH=. pytest -q \
  tests/test_signal_integration_cancel_done_suppression.py \
  tests/test_interrupt_playback.py \
  tests/test_processing_workflow_session_guard.py
```

Результат: `22 passed`.
