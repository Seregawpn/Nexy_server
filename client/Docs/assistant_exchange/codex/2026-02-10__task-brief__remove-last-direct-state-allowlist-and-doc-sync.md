# Task Brief: Remove last direct-state allowlist and sync architecture docs

## Implemented
- Replaced last direct state read in InputProcessing with selector:
  - `selectors.is_first_run_in_progress(self.state_manager)`
- Removed runtime allowlist entries completely in direct-state access verifier.
- Synced architecture docs:
  - startup-order owner is `IntegrationFactory.STARTUP_ORDER`
  - feature gating uses `UnifiedConfigLoader.is_feature_enabled(...)`
  - feature key naming/docs aligned (`features.browser/messages/payment` + aliases)
- Synced STATE_CATALOG machine-check text with actual verifier status (allowlist=0).

## Files updated
- `integration/integrations/input_processing_integration.py`
- `scripts/verify_no_direct_state_access.py`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/STATE_CATALOG.md`

## Verification
- `python3 scripts/verify_no_direct_state_access.py` -> OK (no violations)
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
- `pytest -q ...` targeted suite -> `39 passed`
- `scripts/pre_build_gate.sh` -> PASSED (`Пройдено: 20`, `Пропущено: 1`)
