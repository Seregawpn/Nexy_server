# FDA: Open Settings Without Blocking

## Goal
Avoid perceived hang after user clicks "Open Settings" in the FDA dialog.

## Changes
- When user chooses Open Settings, return immediately and skip access attempt/hold.

## Touchpoints
- `modules/permissions/first_run/activator.py`
