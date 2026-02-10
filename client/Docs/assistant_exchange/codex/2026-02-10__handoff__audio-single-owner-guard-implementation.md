# Handoff: audio single-owner + idempotent start implementation

Date: 2026-02-10
Assistant: Codex
Type: handoff

## Implemented
1. `integration/integrations/voice_recognition_integration.py`
   - Added `self._audio_transition_lock` to serialize start/stop transitions.
   - Added idempotent guard in `_on_recording_start` for same active session.
   - Removed unconditional pre-start cancel behavior; now skip duplicate start when already listening.
   - Added best-effort `_controller_is_listening()` helper.
   - Wrapped `_on_recording_stop` with the same transition lock.

2. `integration/integrations/input_processing_integration.py`
   - Subscribed to `interrupt.request`.
   - Added `_on_interrupt_request` owner handler for external `speech_stop` requests.
   - External stop now goes through owner terminal path (`_terminal_stop` + mode request to sleeping).
   - Keyboard/self-originated interrupts are ignored in this new handler to avoid duplicate terminal stop.

3. `integration/workflows/listening_workflow.py`
   - Timeout monitor no longer publishes `voice.recording_stop` directly.
   - Timeout now publishes `interrupt.request` with `type=speech_stop`.

## Validation
- `python3 -m py_compile` passed for all three changed files.
- Grep check confirms timeout path in `ListeningWorkflow` no longer emits direct terminal `voice.recording_stop`.

## Risk notes
- Runtime behavior should be validated with real PTT flow:
  - long press -> release
  - timeout during listening
  - rapid repeated start/stop events
