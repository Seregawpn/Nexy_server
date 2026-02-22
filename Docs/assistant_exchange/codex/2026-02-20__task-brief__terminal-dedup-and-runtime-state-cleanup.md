# Task Brief — Terminal dedup hardening and runtime-state cleanup

## Context
User requested elimination of duplicate/unsafe paths and non-centralized runtime risks.

## Diagnosis
Two medium-risk areas remained:
1. `SpeechPlaybackIntegration` could re-schedule `finalize_on_silence` repeatedly for the same session.
2. Per-session volatile maps were cleaned inconsistently (manual scattered `pop`s), increasing duplication/leak risk.

## Changes
1. `client/integration/integrations/speech_playback_integration.py`
- Made silence-finalize scheduling idempotent:
  - `_schedule_silence_finalize(..., force_restart=False)` now no-ops if an active task already exists.
- Added centralized volatile-state cleanup helper:
  - `_clear_session_runtime_state(session_id)`.
- Replaced scattered manual cleanup with helper in terminal/cancel/failed paths.

2. `client/integration/workflows/processing_workflow.py`
- Added explicit `_completing` field in `__init__` and removed dynamic `getattr` check.
- Keeps terminal reentrancy guard single-owner and explicit.

## Architecture Fit
- Playback owner remains `SpeechPlaybackIntegration`.
- Workflow owner remains `ProcessingWorkflow`.
- No new owner path introduced.

## Validation
- `python3 -m py_compile client/integration/integrations/speech_playback_integration.py client/integration/workflows/processing_workflow.py`
- Grep validation confirmed new guard/helper usages.

## Expected Effect
- Less chance of terminal delays from repeated finalize task resets.
- Cleaner session lifecycle state handling and lower stale-state risk.
