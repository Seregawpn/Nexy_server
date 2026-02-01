# Task Brief — AUTO_DIALOG timed slot (no waiting)

## Goal
Do not wait for user response on AUTO_DIALOG; proceed after the timed slot.

## Change
- Use `_probe_once` for all steps in the pipeline (AUTO_DIALOG no longer blocks).

## File
- modules/permissions/v2/orchestrator.py

## Verification
- Dialogs can overlap if OS shows late; next step starts after grace+probe.
