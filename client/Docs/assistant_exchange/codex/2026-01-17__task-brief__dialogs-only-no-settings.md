# Dialogs Only: No Settings Opens

## Goal
Ensure permission activation never opens System Settings; use only system dialogs or access attempts.

## Changes
- Removed Settings fallback for Contacts.
- Removed Settings opening for Full Disk Access (access attempt only).

## Touchpoints
- `modules/permissions/first_run/activator.py`
