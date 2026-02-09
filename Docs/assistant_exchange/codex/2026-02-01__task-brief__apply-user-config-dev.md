# Task Brief: Apply User Config (Dev)

## Goal
Stabilize server startup and Stripe webhooks using provided credentials.

## Changes
- `NEXY_ENV=dev`
- `SUBSCRIPTION_ENABLED=true`
- Applied provided Gemini API key and DB credentials
- Applied Stripe test keys + webhook secret (endpoint secret)

## Files
- `server/server/config.env`

## Next Steps
- Set real `STRIPE_TEST_PRICE_ID` (monthly price)
- Restart server and re-run webhook test
