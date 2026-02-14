# Enable update voice announcements on startup

## Change
- Updated config:
  - `config/unified_config.yaml`
  - `update_notification.announce_on_startup: true`

## Why
- `UpdateNotificationIntegration` suppresses all startup update announcements when
  `announce_on_startup` is false.
- User requested voice playback during download/update startup flow.

## Expected behavior
- During startup-triggered update:
  - voice/signal notifications for update start/progress/error are no longer suppressed.
