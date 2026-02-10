# Task Brief: processing terminal cue single-owner (DONE over ERROR overlap)

Date: 2026-02-10
Assistant: codex

## Goal
Убрать ситуацию, когда при завершении PROCESSING пользователь не слышит сигнал перехода в SLEEPING из-за наложения `ERROR` и `DONE`.

## Root cause
В fail-сценарии публиковались два terminal-cue подряд:
- `ERROR` на `voice.recognition_failed`
- `DONE` на `PROCESSING -> SLEEPING`

Из-за back-to-back воспроизведения создавался эффект "sleep-сигнал не сработал".

## Changes
Files:
- `integration/integrations/signal_integration.py`
- `tests/test_signal_integration_cancel_done_suppression.py`

Implemented:
1. В `SignalIntegration._on_error_like` добавлен processing-guard:
   - если текущий режим `PROCESSING`, `ERROR` не воспроизводится (`deferred`), чтобы terminal cue оставался один.
2. `DONE` по `PROCESSING -> SLEEPING` остается активным.
3. Добавлен тест `test_error_deferred_while_processing`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`

Result:
- `23 passed`

## Expected runtime effect
- При завершении PROCESSING слышен один стабильный terminal-cue (DONE на переходе в SLEEPING).
- Исчезает эффект “сигнал не активируется” из-за перекрытия ERROR+DONE.
