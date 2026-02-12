# Task Brief

- Date: 2026-02-11
- Type: task-brief
- Title: minimal-recognition-failed-stopping-guard

## Context

Проблема: при long-hold после release система могла остаться в `PROCESSING`, если `voice.recognition_failed` приходил в фазе `STOPPING`.

## Minimal Fix Applied

1. В `InputProcessingIntegration._on_recognition_failed` убран ранний `return` для `PTTState.STOPPING` (оставлен только для `PTTState.RECORDING`).
2. В `InputProcessingIntegration._handle_release` добавлен guard:
   - после `_request_terminal_stop(...)`, если состояние уже не `STOPPING`, переход в `PROCESSING` не публикуется.
3. В `InputProcessingIntegration._handle_short_press` добавлен такой же guard.

## Why This Is Minimal

- Без новых флагов/состояний.
- Без новых владельцев логики.
- Только защита от гонки между terminal STT-fail и последующей публикацией `mode.request(PROCESSING)`.

## Verification

- Команда: `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "recognition_failed_resets_waiting_grpc_state"`
- Result: `1 passed, 16 deselected`

