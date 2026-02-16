# Task Brief: Fix false payment offer for grandfathered users

## Problem
Grandfathered users could still get payment offer in some error paths because client-side limit detection was too broad.

## Root Cause
`grpc_client_integration` treated almost any error containing words like `subscription`/`subscribe` as limit exceeded and triggered `buy_subscription`.

## Changes
1. `client/integration/integrations/grpc_client_integration.py`
- Added strict matcher `_is_subscription_limit_error()` for real quota markers only:
  - `daily/weekly/monthly limit exceeded`
  - `limited free tier`
  - `subscription_gate_denied`
  - `you have reached your daily limit`
- Replaced broad checks in both:
  - streaming `error_message` path
  - `AioRpcError` path

2. `client/integration/integrations/payment_integration.py`
- Added `grandfathered` to statuses treated as active paid-equivalent in:
  - success notification path
  - polling completion condition

## Verification
- `python3 -m py_compile` for both updated files passed.

## Expected Effect
- Grandfathered users no longer receive accidental payment prompts from unrelated permission/network errors.
- Payment integration correctly recognizes `grandfathered` as active unlimited status.
