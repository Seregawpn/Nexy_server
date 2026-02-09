# Task Brief: Webhook Secret Alignment

## Goal
Align local webhook secret with Stripe endpoint to validate webhooks.

## Changes
- Updated `server/config.env` to include:
  - STRIPE_WEBHOOK_SECRET
  - STRIPE_TEST_WEBHOOK_SECRET
  - STRIPE_LIVE_WEBHOOK_SECRET
  all set to Stripe endpoint secret.

## Test
- Webhook POST returned 400 Invalid signature before restart (server likely loaded old env).

## Next Steps
- Restart server and re-run webhook test.
