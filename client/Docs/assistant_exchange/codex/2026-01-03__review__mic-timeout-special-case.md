# Review: Mic timeout special-case

## Result
Confirmed in `integration/integrations/first_run_permissions_integration.py` that on unified timeout the microphone path assumes GRANTED and logs `microphone timeout_assumed_granted`, while other permissions are marked DENIED and proceed.

## Key lines
- Microphone timeout branch publishes `permissions.stale_cache_assumed` and `status_checked` with GRANTED.
- Non-microphone timeout branch publishes `permissions.timeout` with DENIED.

## Next step
Rebuild packaged artifacts to include the change.
