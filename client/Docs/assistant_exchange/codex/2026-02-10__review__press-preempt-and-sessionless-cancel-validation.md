# Validation: press-preempt + sessionless cancel

## Scope
- Проверка синтаксиса и целевых тестов после правок:
  - `integration/integrations/interrupt_management_integration.py`
  - `integration/integrations/input_processing_integration.py`

## Executed
- `python3 -m py_compile integration/integrations/interrupt_management_integration.py integration/integrations/input_processing_integration.py`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py`
- `PYTHONPATH=. pytest -q ../tests/test_playback_full_interrupt.py`
- `PYTHONPATH=. pytest -q ../tests/test_no_timeouts_no_duplicates.py`

## Results
- `py_compile`: OK
- `tests/test_interrupt_playback.py`: 5 passed, 1 failed
- `../tests/test_playback_full_interrupt.py`: 3 failed
- `../tests/test_no_timeouts_no_duplicates.py`: 3 passed

## Failure pattern
- Все падения связаны с ожиданием, что `SpeechPlaybackIntegration._cancelled_sessions`
  пополняется даже когда `had_audio=False`.
- Текущая реализация в `SpeechPlaybackIntegration` сознательно не добавляет sid в
  `cancelled_sessions`, если аудио еще не было (`skip cancelled_sessions ... no audio yet`).
- Это расхождение тестовых ожиданий и текущего контракта playback guard, не с правкой
  `press-preempt`/`sessionless grpc.request_cancel`.
