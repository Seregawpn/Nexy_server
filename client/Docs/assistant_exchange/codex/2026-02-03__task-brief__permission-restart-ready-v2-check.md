# Task Brief: fix V2 config check in permission restart readiness

## Context
Logs show: "Could not check V2 config: 'UnifiedConfigLoader' object has no attribute 'get'" during `_publish_ready_if_applicable`.

## Change
- Use the existing `_v2_enabled` flag instead of calling `UnifiedConfigLoader.get(...)`.
- Removes noisy exception path and keeps behavior consistent with initialization.

## Files Touched
- `integration/integrations/permission_restart_integration.py`

## Verification
- Expect log: "V2 enabled, deferring ready_to_greet" without config error.
