# Analysis: no-skip permissions

## Summary
User requirement: permissions must not be skipped. Ledger shows `contacts` marked SKIP and `accessibility` waiting_user, so flow can finish without all hard permissions.

## Evidence
- `~/Library/Application Support/Nexy/permission_ledger.json`:
  - `contacts.state=skipped` with reason `CONTACTS_SKIPPED`.
  - `accessibility.state=waiting_user`.
- `~/Library/Logs/Nexy/nexy.log` shows V2 pipeline ran and completed with `all_hard_granted=False`.

## Root Cause
Contacts classifier treats denied/permission_denied_hint as `SKIP` (feature disabled), which allows flow completion without a required permission.

## Proposed Direction
- In `modules/permissions/v2/classifiers.py` (ContactsClassifier), replace `OutcomeKind.SKIP` on denial with `OutcomeKind.FAIL` or `OutcomeKind.WAITING_USER` when contacts are required.
- Ensure the requirement for contacts is driven by config (`messages.require_contacts_permission` or `permissions.contacts.required`).

## Risks
- Changing to FAIL may block startup if user refuses Contacts. Use feature gate or requirement flag to decide WAITING vs FAIL.

## Next Checks
- Confirm which config flag is the true SoT for “contacts required”.
- Decide UX: block app vs degraded mode.
