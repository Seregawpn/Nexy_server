# FDA Dialog Main-Thread Guard

## Goal
Avoid blocking or crashes by skipping NSAlert when not on the main thread.

## Changes
- Added main-thread guard before showing NSAlert in Full Disk Access activation.

## Touchpoints
- `modules/permissions/first_run/activator.py`
