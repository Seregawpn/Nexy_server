# Task Brief: contacts permission mandatory

## Scope
- Make Contacts permission non-skippable and treat it as hard/mandatory in V2.

## Changes
- `modules/permissions/v2/classifiers.py`: replaced `OutcomeKind.SKIP` for contacts denial with `OutcomeKind.WAITING_USER` to avoid skipping.
- `config/unified_config.yaml`: set `integrations.permissions_v2.steps.contacts.criticality` to `hard`.

## Notes
- `scripts/verify_feature_flags.py` is not present in this repo; attempted run failed.

## Verification
- Re-run first-run with TCC reset; confirm `contacts` does not become `skipped` and `all_hard_granted` requires contacts.
