# Review: payment centralization race/dup check

## Scope
- Post-restart audit for payment/subscription flow: duplication, race risks, conflict points, centralization.

## Findings addressed
1. Removed duplicate allowed fields entry in repository update whitelist.
   - File: server/server/modules/subscription/repository/subscription_repository.py
2. Added single-flight guard for checkout reconcile by `session_id`.
   - File: server/server/modules/subscription/subscription_module.py
   - Mechanism: per-session `asyncio.Lock` + lock map cleanup.

## Current owner model
- Source of truth for subscription status: `SubscriptionModule` + repository idempotency/ordering guards.
- Webhook and payment success page both route through `reconcile_checkout_success` for fallback sync.

## Risk status
- Duplication risk: low
- Race risk: low (reconcile path guarded)
- Centralization: yes (single reconciliation owner)

## Validation
- `python3 -m py_compile` passed for touched files.
