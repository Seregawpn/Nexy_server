# Task Brief: Restore Missing Pre-Build Gate Scripts

## Scope
Восстановлены отсутствующие проверки и повторно включены в `pre_build_gate.sh`.

## Changes
- Added scripts:
  - `scripts/verify_no_direct_state_access.py`
  - `scripts/validate_schemas.py`
  - `scripts/verify_4_artifacts_invariant.py`
  - `scripts/verify_rule_coverage.py`
  - `scripts/verify_predicate_coverage.py`
  - `scripts/verify_feature_flags.py`
  - `scripts/update_requirements_snapshot.py`
- Re-enabled checks in `scripts/pre_build_gate.sh` (removed temporary skips).

## Notes
- `verify_no_direct_state_access.py` uses a small allowlist for current legacy direct accesses.
- `update_requirements_snapshot.py` performs minimal metadata validation.

## Verification
Not run.
