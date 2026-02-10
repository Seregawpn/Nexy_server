# Task Brief: Event ownership centralization (shutdown + STT failure)

## Goal
Reduce duplicate publishers for critical intents and keep one source of truth for shutdown/failure paths.

## Implemented

1. `app.shutdown` publishing path centralized:
- Updated `integration/integrations/action_execution_integration.py`
- Self-close fallback (`close_app` for Nexy) no longer publishes `app.shutdown` directly.
- It now publishes `tray.quit_clicked` (`source=action_execution`), so `SimpleModuleCoordinator` remains shutdown publisher.

2. `voice.recognition_failed` publishing centralized in one helper:
- Updated `integration/integrations/voice_recognition_integration.py`
- Added `_publish_recognition_failed(session_id, error, reason)`.
- Replaced all direct `event_bus.publish("voice.recognition_failed", ...)` calls with helper usage.

## Verification
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_user_quit_ack.py` -> 13 passed.
- `python3 -m py_compile` for modified integrations -> OK.

## Effect
- One less duplicate shutdown publisher.
- STT failure publication path is structurally unified, easier to enforce idempotency in one place.
