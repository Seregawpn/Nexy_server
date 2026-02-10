# Handoff: audio scheduled but not audible

Date: 2026-02-09
Assistant: codex
Type: handoff

## Context
- Symptom: logs show continuous `ADD_AUDIO`/`Scheduled chunk`, but user does not hear speech.
- Scope: gRPC audio chunk intake + AVF playback route diagnostics.

## Changes
1) `client/integration/integrations/grpc_client_integration.py`
- Kept skip for fully silent chunks.
- Added skip for low-amplitude *inaudible* chunks (`not is_audible`) before publishing `grpc.response.audio`.
- Effect: removes queue tail/noise chunks that were previously scheduled and prolonged near-silence playback.

2) `client/modules/speech_playback/core/avf_player.py`
- Added `_log_output_route_snapshot()` helper.
- Call route snapshot on every `start_playback()` (not only first engine start).
- Effect: runtime evidence of real output device/port when playback starts, for diagnosing “scheduled but unheard” state.

## Validation
- `python3 -m py_compile` for modified files: OK.
- Targeted regression suite:
  - `test_mode_management_processing_action_guard.py`
  - `test_interrupt_playback.py`
  - `test_playback_full_interrupt.py`
  - `test_mode_management_listening_transition.py`
  - `test_no_timeouts_no_duplicates.py`
- Result: `17 passed`.

## Architectural note
- Source of truth remains:
  - audible classification in gRPC integration (ingress gate),
  - playback lifecycle in speech playback integration,
  - mode transitions in mode management integration.
- No new parallel decision path introduced.
