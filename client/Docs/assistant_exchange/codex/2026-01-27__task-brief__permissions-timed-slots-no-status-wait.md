# Task Brief — Timed slots without waiting status

## Goal
Run permission steps by fixed time slots without waiting for final status.

## Change
- Switched pipeline back to `_probe_once` (no blocking wait) for all steps.

## File
- modules/permissions/v2/orchestrator.py
