# Tray billing entrypoint + subscription facts context

## Scope
- Ensure tray menu billing item always opens billing entrypoint.
- Improve assistant answer quality for "when subscription ends / how many days left".

## Changes
1) Tray menu billing action
- File: `client/modules/tray_controller/core/tray_controller.py`
- Renamed menu item to `Subscription & Billing...`.
- Changed callback publish event from `ui.action.manage_subscription` to `ui.action.buy_subscription`.
- Rationale: one stable entrypoint for billing flow from tray.

2) Subscription facts for assistant responses
- File: `server/server/modules/subscription/subscription_module.py`
- `get_context_for_prompt()` now emits deterministic facts block:
  - `status`, `active`, `access_tier`, `billing_active`, `period_end_utc`, `days_left`.
- Added explicit instruction for assistant to answer subscription date questions strictly from these facts.

## Validation
- `python3 -m py_compile client/modules/tray_controller/core/tray_controller.py server/server/modules/subscription/subscription_module.py` -> OK.

## Operational note
- Restart client + server required to apply runtime behavior.
