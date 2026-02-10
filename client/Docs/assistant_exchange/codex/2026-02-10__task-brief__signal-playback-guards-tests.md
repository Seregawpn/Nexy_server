# Task Brief: tests for signal playback guards

Date: 2026-02-10
Assistant: codex

## Goal
Закрепить регрессионными тестами защиту от некорректного воспроизведения cue-сигналов.

## Changes
File:
- `tests/test_interrupt_playback.py`

Added tests:
1. `test_playback_signal_skips_stale_event`
2. `test_playback_signal_skips_when_user_quit_intent`
3. `test_playback_signal_skips_listen_start_outside_listening`
4. `test_playback_signal_skips_error_in_listening`

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Result:
- `22 passed`

## Effect
- Зафиксирован контракт: stale/quit/context-invalid `playback.signal` не приводит к воспроизведению.
- Снижена вероятность повторного появления проблемы в LISTENING и при shutdown.
