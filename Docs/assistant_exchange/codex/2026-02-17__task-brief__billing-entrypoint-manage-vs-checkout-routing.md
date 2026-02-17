# Task Brief: Unified billing entrypoint (manage vs checkout)

## Problem
Client always triggered buy flow from `ui.action.buy_subscription` / limit action, even when user already had an active Stripe subscription. This caused checkout to open for already-paid users.

## Fix Summary
- Added centralized routing entrypoint in `PaymentIntegration`:
  - fetch `/api/subscription/status` (server as source of truth)
  - route to `open_manage_subscription()` for known Stripe-linked statuses
  - otherwise route to `open_buy_subscription()`
- Switched `ui.action.buy_subscription` handler to use this entrypoint.
- Reused a single `_ensure_hardware_id()` helper for status check and checkout.

## Architecture Gates
- Single Owner: `PaymentIntegration.open_subscription_entrypoint()`
- Zero Duplication: removed duplicated hardware-id wait logic from checkout path
- Anti-Race: preserved checkout in-flight dedup guard
- Flag Lifecycle: no new flags introduced

## Validation
- `python3 -m py_compile client/integration/integrations/payment_integration.py` passed.
- Route logging added:
  - `Billing route=manage ...`
  - `Billing route=checkout ...`

## Expected Runtime Behavior
- Reinstalled app + same `hardware_id` with active Stripe subscription -> opens customer portal (manage).
- New user with no Stripe linkage -> opens checkout.
