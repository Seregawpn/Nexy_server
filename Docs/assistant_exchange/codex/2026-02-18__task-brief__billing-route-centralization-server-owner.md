# Billing route centralization (server owner)

## Goal
Remove duplicated client/server billing-route decisions and make server the single owner for checkout vs manage routing.

## Implemented
1. Server (`SubscriptionModule`) now returns canonical route field:
   - `recommended_billing_route`: `manage` if Stripe customer exists, else `checkout`.
2. Client (`PaymentIntegration.open_subscription_entrypoint`) now uses:
   - primary: `recommended_billing_route` from server status API
   - fallback: legacy local heuristic (only for backward compatibility with old server)
3. Existing lazy Stripe sync and billing-active policy remain in server owner path.

## Files changed
- `server/server/modules/subscription/subscription_module.py`
- `client/integration/integrations/payment_integration.py`
- `server/server/modules/subscription/providers/stripe_service.py` (from previous step in same task chain)

## Verification run
- `python3 -m py_compile` for modified modules: OK.
- Runtime API still showed old payload until server restart (expected for hot process).

## Expected after restart
- `/api/subscription/status` includes `recommended_billing_route`.
- Client logs contain `recommended=manage|checkout` and no independent routing conflicts.
