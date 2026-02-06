# Task Brief: restart guards + ledger mkdir verification

## Context
User reported repeated restarts. Need to ensure V2 owns restart and legacy restart_pending does not trigger duplicates; also fix ledger save crash on missing directory.

## Verification
- `modules/permissions/v2/integration.py`: RESTART_SCHEDULED mapping removed (returns None).
- `integration/integrations/permission_restart_integration.py`: guard for source=v2_integration with Decision: ABORT log; idempotency guard via restart flag.
- `modules/permissions/v2/ledger.py`: mkdir before tmp write added.

## Outcome
Changes are present on disk. Next step is rebuild and log check for:
- "Skipping legacy restart_pending from v2" and absence of duplicate restarts.
- No "permission_ledger.json.tmp -> permission_ledger.json" errors.
