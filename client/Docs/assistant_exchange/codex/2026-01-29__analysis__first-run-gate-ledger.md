# Analysis: first-run gate uses ledger

## Summary
Updated startup gating to rely on `FirstRunPermissionsIntegration.are_all_granted` (ledger-driven) instead of `permissions_first_run_completed.flag`.

## Files touched
- `integration/core/simple_module_coordinator.py`

## Rationale
Removes flag as a decision source; aligns with ledger-driven first-run eligibility.
