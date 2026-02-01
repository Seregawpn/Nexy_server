# FDA: Non-Modal Dialog

## Goal
Avoid UI hangs by replacing blocking FDA modal alert with a non-modal sheet.

## Changes
- Use `beginSheetModalForWindow_completionHandler_` instead of `runModal()`.
- Open Settings + async access attempt in completion handler.
- Keep 15s hold for overall timing without blocking UI.

## Touchpoints
- `modules/permissions/first_run/activator.py`
