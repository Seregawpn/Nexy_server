# First-Run Wait-Loop 15s Cleanup

## Goal
Use a single 15s wait-loop per permission and remove duplicate holds/settings hints.

## Changes
- First-run now uses a short activation trigger hold (0.5s) and relies on wait-loop for timing.
- Microphone status polling uses no-prompt checker.
- Config: activation_hold_duration_sec set to 0.5s, settings_required_permissions cleared.

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
- `config/unified_config.yaml`
