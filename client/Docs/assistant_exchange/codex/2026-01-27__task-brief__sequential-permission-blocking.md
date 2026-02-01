# Task Brief — Strict sequential permissions

## Goal
Do not start the next permission until the current one finishes.

## Change
- Use `_poll_until_done` for all steps in the pipeline.

## File
- modules/permissions/v2/orchestrator.py
