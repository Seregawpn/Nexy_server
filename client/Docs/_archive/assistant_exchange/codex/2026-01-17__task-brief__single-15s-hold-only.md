# First-Run: Single 15s Hold Only

## Goal
Use a single 15s window per permission for trigger + user response; remove extra waits between requests.

## Changes
- First-run uses only `activation_hold_duration_sec` and a single post-check (no wait-loop).
- Removed inter-permission pause (set to 0.0).
- Activation hold set back to 15.0 seconds.

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
- `config/unified_config.yaml`
