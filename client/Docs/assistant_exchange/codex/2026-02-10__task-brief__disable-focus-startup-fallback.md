# Task brief: disable focus startup fallback

## Request
Снизить риск потери/переключения фокуса (в т.ч. на зажатии hotkey) за счёт устранения потенциального focus-grab пути.

## Change
1. `config/unified_config.yaml`
- `focus.allow_tray_startup_fallback: true -> false`

2. `integration/core/simple_module_coordinator.py`
- Default для `allow_tray_startup_fallback` изменён `True -> False` в `_get_focus_config()`.

## Why
- One-shot fallback использует `activateIgnoringOtherApps_(True)`, что может давать фокусный прыжок.
- Отключение fallback убирает этот путь без вмешательства в PTT/interrupt/update логику.

## Validation
- Regression suite:
  - `tests/test_user_quit_ack.py`
  - `tests/test_interrupt_playback.py`
  - `tests/test_signal_integration_cancel_done_suppression.py`
  - `tests/test_mode_management_mode_request_dedup.py`
  - `tests/test_speech_playback_session_id.py`
- Result: `28 passed`.
