# Task Brief: disable payment and switch to production target

## Requested
- Disable payment flow.
- Enable production server target.

## Applied changes
1) Client routing to production gRPC:
- `client/config/unified_config.yaml`
  - `integrations.grpc_client.server: production`

2) Client payment feature off:
- `client/config/unified_config.yaml`
  - `feature_flags.payment.enabled: false`

3) Server subscription/payment off:
- `server/config.env`
  - `SUBSCRIPTION_ENABLED=false`
  - `PAYMENT_USE_ENABLED=false`

## Notes
- Server env already had production mode (`NEXY_ENV=prod`), no change required.
- Restart client/server processes to apply runtime config/env updates.
