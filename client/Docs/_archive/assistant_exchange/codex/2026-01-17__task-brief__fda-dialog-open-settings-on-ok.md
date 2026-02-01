# Full Disk Access: Dialog With Optional Settings

## Goal
Show a native dialog and open System Settings only when the user confirms.

## Changes
- Added NSAlert prompt for Full Disk Access.
- Open Settings only after user clicks OK; otherwise skip.

## Touchpoints
- `modules/permissions/first_run/activator.py`
