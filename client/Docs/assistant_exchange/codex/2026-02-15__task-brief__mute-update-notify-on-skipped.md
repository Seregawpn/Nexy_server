# Task Brief: Disable update announcements on skipped update events

Date: 2026-02-15
Owner: Codex

## Context
User requested no update announcements when updater decides to skip update checks/install.

## Changes
File: `integration/integrations/update_notification_integration.py`

1. Added subscription in initialize:
- `updater.update_skipped` -> `_on_update_skipped`

2. Added handler `_on_update_skipped(event)`:
- resets progress counters
- sets `_update_in_progress = False`
- sets `_update_completed = False`
- clears `_suppress_announcements`
- does not call `_speak()` and does not call `_play_signal()`
- logs explicit informational line that announcements are disabled for skipped updates

## Architecture Fit
- Owner remains `UpdateNotificationIntegration` for notification policy.
- No duplicate notification path introduced.

## Validation
- `python3 -m py_compile integration/integrations/update_notification_integration.py` passed.

## Expected Behavior
When `updater.update_skipped` is published, user hears no update-related voice/signal announcement.
