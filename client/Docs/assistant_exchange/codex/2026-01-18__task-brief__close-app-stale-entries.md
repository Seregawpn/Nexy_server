# Close App Stale Entry Cleanup

## Goal
Avoid `already_running` after close_app completes by clearing stale entries.

## Change Summary
- Clear stale `_active_apps` entries when the previous task is missing or done.
- Keeps close_app idempotency while allowing new commands after completion.

## Files Touched
- `integration/integrations/action_execution_integration.py`

## Verification
- Trigger close_app twice; second should not hit `already_running` if prior task already finished.
