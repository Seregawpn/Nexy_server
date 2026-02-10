# Task Brief: allowlist reduction + feature default sync

## Done
- Reduced direct-state-access allowlist to only one remaining legacy file:
  - `integration/integrations/input_processing_integration.py`
- Synced feature defaults in config/features with runtime usage:
  - Added explicit `features.browser.enabled=true`
  - Added explicit `features.messages.enabled=true`
  - Added explicit `features.payment.enabled=false`
- Synced registry default for payment:
  - `Docs/FEATURE_FLAGS.md`: `features.payment` default changed `true -> false`
- Fixed false positive in updater docstring that matched direct-access regex.

## Files changed
- `scripts/verify_no_direct_state_access.py`
- `config/unified_config.yaml`
- `Docs/FEATURE_FLAGS.md`
- `integration/integrations/updater_integration.py`

## Verification
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_no_direct_state_access.py` -> OK (only input_processing in allowlist)
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
