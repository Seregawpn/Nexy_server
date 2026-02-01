# Task Brief: build_final permissions preflight

## Goal
Ensure packaging script resets permission state and blocks packaging when permission-related bypass/config issues are present.

## Changes
- Remove `permission_ledger.json` during cleanup (normal + clean install).
- Add permissions preflight:
  - fail on dev-bypass env vars
  - validate `permissions_v2.enabled`, `advance_on_timeout=false`, non-empty `permissions_v2.order`, non-empty `permission_restart.critical_permissions`.

## Files touched
- `packaging/build_final.sh`

## Notes
- `scripts/verify_feature_flags.py` not present in repo; discovery step not runnable.
