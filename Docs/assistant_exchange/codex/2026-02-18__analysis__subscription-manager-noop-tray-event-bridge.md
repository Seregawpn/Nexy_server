# Analysis: subscription manager command/menu no-op in dev logs

## Symptom
User repeatedly asks to open Subscription Manager; nothing opens. Tray menu click also appears to do nothing.

## Findings
1. Voice path (nexy-dev.log): no `manage_subscription` action dispatch observed.
   - STT misrecognitions present (`play Joe subscription`, `could not understand audio`), so voice intent often never reaches payment action.
2. Tray path (code bug): `TrayController` emits local callbacks, but `TrayControllerIntegration` registered only `quit_clicked` callback.
   - `ui.action.manage_subscription` callback was never bridged to EventBus.
   - Result: menu item existed, but click was effectively dropped (no-op).

## Fix implemented
File: `client/integration/integrations/tray_controller_integration.py`

- Added event bridge registration on start for:
  - `ui.action.manage_subscription`
  - `updater.check_manual`
  - `settings_clicked`
  - `about_clicked`
  - `icon_clicked`
  - `icon_right_clicked`
- Added `_relay_tray_event(event_type, data)` to publish tray-originated events into EventBus with `source=tray`.

This keeps Integration layer as single owner for cross-module event routing.

## Validation
- `python3 -m py_compile` passed for:
  - `client/integration/integrations/tray_controller_integration.py`
  - `client/integration/integrations/payment_integration.py`
- Code check confirms callback registration and relay method are present.

## Expected runtime after restart
- Clicking Tray `Manage Subscription...` must emit `ui.action.manage_subscription` and trigger PaymentIntegration route (portal/checkout).
- Logs should show relay and payment handling instead of silent no-op.
