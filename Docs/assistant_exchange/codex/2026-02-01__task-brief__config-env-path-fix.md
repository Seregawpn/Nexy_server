# Task Brief: Config Env Path Fix

## Goal
Ensure server loads Stripe webhook secret from the correct config.env location.

## Changes
- Copied `server/config.env` to `server/server/config.env` (actual load path).

## Next Steps
- Restart server and re-run webhook test.
