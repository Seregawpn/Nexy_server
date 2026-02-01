# Accessibility fallback to Settings (task brief)

## Goal
Add explicit fallback to System Settings when prompt helper fails or errors.

## Changes
- Introduced local helper to open Accessibility settings.
- Triggered immediate fallback when helper returns error/timeout.
- Reused fallback after status check for non-granted status.

## Files
- modules/permissions/first_run/activator.py
