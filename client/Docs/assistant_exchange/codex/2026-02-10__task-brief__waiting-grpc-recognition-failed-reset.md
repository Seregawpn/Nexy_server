# Task Brief: reset waiting_grpc on recognition_failed

Date: 2026-02-10
Assistant: codex

## Problem
После `voice.recognition_failed` input lifecycle мог остаться в `waiting_grpc` со старым `session_id`. Следующий `PRESS` ошибочно трактовался как preempt/interrupt в idle/sleeping контексте.

## Root cause
В `InputProcessingIntegration._on_recognition_failed` была инвертированная ветка: при `waiting_grpc=True` state не сбрасывался.

## Changes
File:
- `integration/integrations/input_processing_integration.py`

Implemented:
1. `_on_recognition_failed` теперь:
- при `waiting_grpc=True` выполняет owner-reset для совпадающей (или отсутствующей) session;
- при `sid mismatch` логирует skip;
- при `waiting_grpc=False` сохраняет прежнее поведение (mode.request sleeping + reset).

2. Added regression test:
- `tests/test_interrupt_playback.py::test_recognition_failed_resets_waiting_grpc_state`

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Result:
- `23 passed`

## Expected runtime effect
- После STT fail не остаётся stale `waiting_grpc`.
- `PRESS_PREEMPT decision` в sleeping/idle больше не должен срабатывать из-за старой сессии.
