# Task Brief: done cue amplification for sleep transition

## Problem
Даже после централизации terminal-сигналов `DONE` при `PROCESSING -> SLEEPING` оставался слабо различим в реальном потоке.

## Change
- Усилен профиль `SignalPattern.DONE` в `SignalIntegration`:
  - `tone_hz`: `1040 -> 1240`
  - `duration_ms`: `220 -> 360`
  - `volume`: `0.36 -> 0.52`

## Why
- `DONE` является ключевым sleep-cue и должен быть заметно отличим от `LISTEN_START`.
- Изменение локализовано в одном владельце аудио-политики (`SignalIntegration`), без новых путей или флагов.

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- `22 passed`

