# Pre-release Server Go-live Checks

## Scope
Validation of new production server before final go-live.

## Endpoint
- `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com`

## Verified
- `health/status/updates` endpoints return `200`.
- gRPC smoke test over `443` passes end-to-end.
- Nginx TLS is domain-based (Let's Encrypt cert).
- Internal service ports are loopback-only on VM:
  - `127.0.0.1:50051`, `127.0.0.1:8080`, `127.0.0.1:8081`
- Direct public access attempts to `:50051/:8080/:8081` timeout.
- NSG inbound rules:
  - 22 from admin IP only
  - 80 public
  - 443 public

## Fixed during run
- Added explicit Nginx HTTP routes for:
  - `/webhook/stripe`
  - `/payment/success`
  - `/payment/cancel`
  - `/api/subscription/portal`
  - `/api/subscription/checkout`
  - `/api/subscription/status`
- Added port `80` server block with redirect to HTTPS.

## Remaining operational point
- Billing/webhook feature is currently disabled in runtime config:
  - `SUBSCRIPTION_ENABLED=false`
  - `PAYMENT_USE_ENABLED=false`
- Therefore `/webhook/stripe` currently returns `404` by application logic (route not mounted when module disabled).

## Go/No-Go
- Core assistant server: GO
- Billing/webhook flow: NO-GO until feature flags are enabled and Stripe endpoint updated.
