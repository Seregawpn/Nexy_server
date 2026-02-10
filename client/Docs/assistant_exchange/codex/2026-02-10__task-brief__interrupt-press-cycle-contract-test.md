# Task Brief: interrupt press-cycle contract test

## Context
- Нужно закрепить антидубль контракт: в одном физическом press-cycle (`PRESS -> LONG_PRESS` с одинаковым `press_id`) публикуется только один `interrupt.request`.

## Changes
- Обновлен файл `/Users/sergiyzasorin/Fix_new/client/tests/test_interrupt_playback.py`:
  - Добавлен тест `test_press_and_long_press_same_press_id_publish_single_interrupt_request`.
  - Тест проверяет:
    - ровно 1 событие `interrupt.request`;
    - `type == speech_stop`;
    - `press_id` совпадает с press-cycle.
  - Обновлен устаревший тест:
    - `test_press_publishes_interrupt_when_sleeping_but_session_still_present`
    - → `test_press_does_not_publish_interrupt_when_sleeping_with_stale_session`
    - теперь соответствует текущему контракту: в `SLEEPING` без pending grpc preempt не публикуется.

## Validation
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "single_interrupt_request"`
  - `1 passed, 6 deselected`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py tests/test_user_quit_ack.py`
  - `12 passed`

## Result
- Инвариант “1 preempt на 1 press_id” закреплен автотестом.
- Регрессионный набор по interrupt/playback/session/quit проходит.
