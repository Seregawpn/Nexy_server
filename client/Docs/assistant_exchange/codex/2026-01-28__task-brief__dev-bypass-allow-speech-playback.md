# Task Brief: dev-bypass allow speech playback

## Goal
Allow speech_playback (and other permission-gated modules) to start in dev-bypass so welcome audio can play.

## Change
- In `integration/core/simple_module_coordinator.py`, bypass the per-module permission gate when `NEXY_TEST_SKIP_PERMISSIONS=1`.

## Rationale
Dev-bypass skips permission checks; blocking speech_playback prevents welcome audio completion.

## Files
- `integration/core/simple_module_coordinator.py`
