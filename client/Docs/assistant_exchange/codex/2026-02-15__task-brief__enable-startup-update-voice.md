# Task Brief: enable startup update voice

## Context
Startup update announcements were suppressed by configuration:
`[UPDATE_NOTIFY] Suppressing startup update announcements`.

## Change
- Updated `/config/unified_config.yaml`:
  - `integrations.update_notification.announce_on_startup: true`

## Expected Result
- During startup-triggered updates, UpdateNotificationIntegration will speak update start/progress/error messages instead of suppressing them.

## Verification
- Config check confirms:
  - `announce_on_startup=True`
