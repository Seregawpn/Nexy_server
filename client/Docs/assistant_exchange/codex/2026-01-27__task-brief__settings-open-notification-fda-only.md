# Settings Notification — FDA Only

## Date
2026-01-27

## Change Summary
Limit permissions Settings notification to Full Disk Access only (no notification for Accessibility).

## Files
- `modules/permissions/v2/integration.py`

## Verification Plan
- Trigger Accessibility step: no notification.
- Trigger Full Disk Access step: notification appears.
