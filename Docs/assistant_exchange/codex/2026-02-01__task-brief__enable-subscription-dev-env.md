# Task Brief: Enable Subscription in Dev

## Goal
Align environment config to allow Stripe test webhooks and subscription flow.

## Changes
- Set `NEXY_ENV=dev`
- Set `SUBSCRIPTION_ENABLED=true`

## Files
- `server/server/config.env`

## Follow-ups
- Fill real `STRIPE_TEST_SECRET_KEY`, `STRIPE_TEST_PUBLISHABLE_KEY`, `STRIPE_TEST_PRICE_ID` (or STRIPE_* equivalents).
- Provide valid `GEMINI_API_KEY` to avoid gRPC init failure.
