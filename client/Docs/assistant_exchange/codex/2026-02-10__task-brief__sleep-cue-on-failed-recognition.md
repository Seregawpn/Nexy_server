# Task Brief: sleep cue on failed recognition

## Problem
При `PROCESSING -> SLEEPING` в частом кейсе `failed_recognition` пользователь не воспринимал сигнал перехода в сон как стабильный.

## Change
- В `SignalIntegration._on_processing_terminal` добавлен fallback:
  - `result=failed` + `reason=failed_recognition` -> `SignalPattern.DONE`
  - прочие `failed` остаются `SignalPattern.ERROR`

## Why
- Это выравнивает UX-контракт: при завершении processing-цикла в sleeping всегда есть "sleep cue", даже если STT дал `unknown_value`.
- Конфликты и дубли не добавлены: источник по-прежнему один (`processing.terminal`).

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- `22 passed`

