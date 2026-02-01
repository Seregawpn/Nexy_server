# Task Brief: first-run ledger gate

## Goal
Stop trusting `permissions_first_run_completed.flag` as a gate and rely on V2 ledger/orchestrator to decide whether the first-run pipeline runs.

## Changes
- Removed `_first_run_completed` checks from `FirstRunPermissionsIntegration.are_all_granted` and `start()`.
- Updated requirements/spec to state the flag is cache only; ledger controls eligibility.

## Files touched
- `integration/integrations/first_run_permissions_integration.py`
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/first_run_flow_spec.md`

## Notes
- `scripts/verify_feature_flags.py` not present in repo; discovery step not runnable.
