# Analysis: Subscription manager route not opening

## Context
User reported that voice/menu requests to open Subscription Manager did not open anything.

## Diagnosis
`PaymentIntegration` mixed routing and transport assumptions:
- `ui.action.manage_subscription` called `open_manage_subscription()` directly.
- Billing HTTP endpoints were hardcoded as `http://<host>:8080/...`.
- Host resolution did not reliably follow active server profile behavior for billing transport.

This caused silent failures when profile/runtime expected different billing base URL behavior.

## Implemented change
File: `client/integration/integrations/payment_integration.py`

1. Centralized manage button flow through `open_subscription_entrypoint()`.
2. Added billing URL resolver:
   - `_resolve_billing_base_url()`
   - `_build_billing_api_url(path)`
3. Replaced all hardcoded payment URLs with centralized builder for:
   - `/api/subscription/status`
   - `/api/subscription/checkout`
   - `/api/subscription/portal`

## Architecture gates
- Single Owner Gate: kept in `PaymentIntegration` (client-side billing routing owner).
- Zero Duplication Gate: removed repeated URL construction logic.
- Anti-Race Gate: no new mutable shared state added.
- Flag Lifecycle Gate: no new flags introduced.

## Verification
- `python3 -m py_compile client/integration/integrations/payment_integration.py` passed.
- Direct portal API check returned 200 with `portal_url` on local server.

## Expected runtime result
- Menu action "Manage Subscription" now follows the same route decision as buy flow:
  - existing subscriber -> portal
  - no subscription -> checkout
- Billing API URL is resolved consistently via one function.
