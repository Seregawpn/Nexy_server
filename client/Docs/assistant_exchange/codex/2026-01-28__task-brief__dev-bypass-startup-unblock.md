# Task Brief: dev bypass unblocks startup

## Goal
Allow full startup (including speech_playback/welcome_message) when terminal dev-bypass is enabled.

## Change
- In `integration/core/simple_module_coordinator.py`, disable `restrict_to_permissions` when `NEXY_TEST_SKIP_PERMISSIONS=1`.
- Added log line indicating dev-bypass skipping restriction.

## Rationale
Prevents first-run gate from blocking speech playback in dev-bypass mode.

## Files
- `integration/core/simple_module_coordinator.py`
