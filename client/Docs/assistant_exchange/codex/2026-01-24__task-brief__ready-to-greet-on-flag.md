# Task Brief: publish ready_to_greet when first-run flag exists

## Goal
Ensure WelcomeMessage plays even when first-run permissions pipeline is skipped due to existing flag.

## Change
- Publish `system.ready_to_greet` alongside `permissions.first_run_completed` when `permissions_first_run_completed.flag` exists.

## File touched
- `integration/integrations/first_run_permissions_integration.py`

## Notes
- `scripts/verify_feature_flags.py` is missing in repo; discovery step cannot be executed.
