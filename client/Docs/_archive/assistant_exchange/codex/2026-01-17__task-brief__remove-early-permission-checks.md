# Remove Early Permission Checks

## Goal
Prevent early permission prompts before sequential first-run flow.

## Changes
- Removed pre-start checks for mic/accessibility/screen/input that could trigger prompts out of order.

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
