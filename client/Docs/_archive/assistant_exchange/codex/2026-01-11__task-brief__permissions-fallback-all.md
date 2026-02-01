# Permissions fallback for all prompts (task brief)

## Goal
Ensure every permission activation falls back to System Settings when prompt/activation fails or remains not granted.

## Changes
- Added centralized System Settings opener using unified_config `permissions.system_preferences` URLs.
- Microphone: re-check status after activation; open Settings when not granted or when sounddevice is missing.
- Input Monitoring: open Settings if IOHID API unavailable or status remains not granted.
- Screen Capture: open Settings if API unavailable or status remains not granted.
- Accessibility: reuse centralized Settings opener for fallback.

## Files
- modules/permissions/first_run/activator.py
