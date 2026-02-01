# Tray Notification Subscription Fix

## Date
2026-01-27

## Change Summary
Fixed invalid EventPriority used for system notification subscription in tray integration.

## Files
- `integration/integrations/tray_controller_integration.py`

## Verification Plan
- Launch app and confirm `system.notification` has a subscriber.
- Verify FDA notification shows.
