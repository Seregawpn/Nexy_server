# FDA Non-Modal: No Hold If Dialog Hidden

## Goal
Avoid blocking when FDA dialog cannot be shown, while keeping Settings flow and list registration.

## Changes
- Keep non-modal FDA dialog; return immediately when dialog is shown.
- Skip 15s hold if dialog is not shown; continue flow.
- Retain alert+window references to avoid GC.

## Touchpoints
- `modules/permissions/first_run/activator.py`
