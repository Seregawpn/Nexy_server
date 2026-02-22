# Tray billing click drop bridge fix

## Issue
Tray menu item click did not open billing page.

## Root cause
`TrayController` published `ui.action.buy_subscription`, but `TrayControllerIntegration` relay bridge forwarded only `ui.action.manage_subscription` and other events.
As a result, the event was dropped before reaching EventBus subscribers.

## Fix
Added `ui.action.buy_subscription` to relay event bridge list in:
- `client/integration/integrations/tray_controller_integration.py`

## Validation
- `python3 -m py_compile` passed for tray controller + integration files.

## Runtime note
Client restart required for tray integration reload.
