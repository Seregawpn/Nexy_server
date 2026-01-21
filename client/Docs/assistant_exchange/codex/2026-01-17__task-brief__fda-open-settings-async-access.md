# FDA: Async Access Attempt After Open Settings

## Goal
Open Settings without blocking and still register the app in the FDA list.

## Changes
- After "Open Settings", fire-and-forget a background access attempt to `chat.db`.

## Touchpoints
- `modules/permissions/first_run/activator.py`
