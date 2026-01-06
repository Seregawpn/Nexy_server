# Review: First-run restart guard

## Scope
Validated guard to block permission restarts during first-run before restart_pending is set.

## Findings
- Guard present in `PermissionRestartIntegration._handle_transition`.
- Condition: `snapshot.first_run == True` and `snapshot.restart_pending == False`.
- Logs: `Restart blocked during first_run` with permission name.

## Risk
- None; guard reduces race risk without adding new state.

## Next
Rebuild packaged artifacts to include the change and verify in logs.
