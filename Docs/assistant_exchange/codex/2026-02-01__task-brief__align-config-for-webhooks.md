# Task Brief: Align Config for Webhooks

## Goal
Align server config to dev/test Stripe setup and enable subscriptions.

## Changes
- Set `NEXY_ENV=dev`
- Set `SUBSCRIPTION_ENABLED=true`
- Set `STRIPE_WEBHOOK_SECRET` and `STRIPE_TEST_WEBHOOK_SECRET` to Stripe endpoint secret

## Files
- `server/server/config.env`

## Next Steps
- Restart server to load new config
- Re-run webhook test and verify `Webhook received` in logs
