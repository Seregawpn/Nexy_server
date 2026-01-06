# Review: Mic permission stale status fix

## Scope
Checked implementation of microphone stale-cache fix and timeout changes.

## Files reviewed
- integration/integrations/first_run_permissions_integration.py
- modules/permissions/first_run/status_checker.py

## Findings
- Mic stale-timeout (20s) is implemented in _activate_and_wait_for_permission(), with explicit logging and synthetic GRANTED event publication.
- sounddevice fallback now treats device/host/busy/timeouts as GRANTED, reducing false NOT_DETERMINED states.
- Diagnostic logs are present for stale cache and sounddevice fallback outcomes.

## Risks
- The mic timeout assumes GRANTED after 20s even if user did not grant; this is intentional but should be validated via runtime logs.

## Next verification
- Reset mic permission and run packaged app; confirm first-run proceeds to Accessibility/Input/Screen after mic grant.
