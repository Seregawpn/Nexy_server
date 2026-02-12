# Task Brief — Sync microphone tests with current InputProcessingIntegration API

## Context
После обновлений InputProcessingIntegration часть тестов использовала устаревшие внутренние методы (`_handle_key_release`, `_ensure_playback_idle`).

## Changes
- File: `tests/test_microphone_activation.py`
  - replaced `_handle_key_release(...)` -> `_handle_release(...)`
  - replaced `_ensure_playback_idle` mocks -> `_wait_for_playback_finished`
  - removed stale `_current_session_id` test writes

## Verification
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py` -> `5 passed`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "release_suppressed_when_combo_still_pressed_early_after_start or release_not_suppressed_when_combo_not_pressed"` -> `2 passed`

## Result
Тестовый контракт синхронизирован с текущим owner API InputProcessingIntegration; регрессионные кейсы по release/spurious release проходят.
