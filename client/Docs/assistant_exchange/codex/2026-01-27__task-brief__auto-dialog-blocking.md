# Task Brief — Block AUTO_DIALOG steps until completion

## Goal
Prevent overlapping system dialogs by waiting for AUTO_DIALOG permissions to complete before moving to the next step.

## Changes
- AUTO_DIALOG steps now use `_poll_until_done` instead of `_probe_once` in the pipeline.

## Files
- modules/permissions/v2/orchestrator.py

## Verification
- Run first‑run flow; ensure Screen Capture dialog completes before Contacts appears.
