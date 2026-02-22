# Stripe period lazy-sync for missed webhooks

## Problem
User had paid subscription period expected active until 2026-02-17, but runtime returned limit exceeded.

## Findings
- DB row had:
  - status=grandfathered
  - stripe_status=active
  - stripe_subscription_id present
  - current_period_end=NULL
- Config had `SUBSCRIPTION_GRANDFATHERED_ENABLED=false`, so fallback to limited happened.
- Existing flow depended on webhook `customer.subscription.updated` for `current_period_end`; if webhook is missed/delayed, period remained NULL.

## Fix
- Added Stripe on-demand subscription fetch in provider:
  - `StripeService.get_subscription(subscription_id)`
- Added lazy sync in subscription module before decisions:
  - `create_portal_session(..., force=True)`
  - `get_subscription_status(...)`
  - `can_process(...)`
- Added mapping from Stripe status -> local status during sync.
- Updated prompt context to use effective tier (`access_tier` + `billing_active`) to avoid false "Paid Active" text.

## Files
- `server/server/modules/subscription/providers/stripe_service.py`
- `server/server/modules/subscription/subscription_module.py`

## Validation
- `python3 -m py_compile` on modified files: OK.

## Note
Running server instance must be restarted to load new code.
