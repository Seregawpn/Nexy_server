# Task Brief: playback.signal context guard (LISTENING + shutdown)

Date: 2026-02-10
Assistant: codex

## Goal
Стабилизировать проигрывание UX-сигналов, чтобы:
- не проигрывались поздние/stale сигналы в новом контексте (особенно `error/done/cancel` в `LISTENING`),
- сигналы не воспроизводились во время user quit / app shutdown.

## Changes
File:
- `integration/integrations/speech_playback_integration.py`

Implemented:
1. Added shutdown guard in playback integration:
- `self._shutdown_requested: bool = False`
- set to `True` in `_on_app_shutdown` before `stop()`.

2. Added quit-intent guard for signals:
- in `_on_playback_signal`, skip if `StateKeys.USER_QUIT_INTENT == True`.

3. Added context guard by current app mode (SoT via `selectors.get_current_mode(state_manager)`):
- skip `listen_start` if current mode is not `AppMode.LISTENING`;
- skip `error|done|cancel` if current mode is already `AppMode.LISTENING`.

4. Kept existing cancel in-flight dedup window unchanged.

## Why this fits architecture
- Source of truth remains centralized in `state_manager` + `mode_management`.
- No new parallel state machine introduced.
- Guard is localized at a single playback ingress point (`playback.signal` consumer), reducing race surface.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Result:
- `18 passed`

## Expected runtime effect
- No delayed `pattern=error/done/cancel` beeps over a fresh listening start.
- No cue playback once quit intent/shutdown begins.
