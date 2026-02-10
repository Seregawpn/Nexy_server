# Task Brief: interrupt preempt per-press dedup

## Context
- В рантайм-логах повторно публиковался `interrupt.request` в рамках одного физического нажатия (`press` -> `long_press`), что дублировало `grpc.request_cancel` и mode transitions.

## Changes
- Обновлен `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`:
  - Добавлен guard `self._preempt_sent_press_id` (один preempt на один `press_id`).
  - `interrupt.request` теперь получает явный `press_id` через параметр `_publish_interrupt_and_cancel(..., press_id=...)`.
  - В `_handle_press` preempt выполняется не более одного раза для текущего `press_id`.
  - В `_handle_long_press` повторный preempt пропускается, если уже отправлен для того же `press_id`.
  - В `_cancel_short_tap` добавлен такой же антидубль guard по `press_id`.
  - Guard сбрасывается в terminal reset-путях.

## Validation
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `pytest -q tests/test_speech_playback_session_id.py tests/test_user_quit_ack.py`
- Результат: `5 passed`.

## Expected Runtime Effect
- Для одного физического нажатия должен появляться максимум один `interrupt.request` preempt.
- Дубли `grpc.request_cancel` и повторные “processing -> sleeping -> listening” из-за второго preempt должны исчезнуть.
