# Analysis: first-run missing prompts (log review)

## Inputs
- User log: `log.md` (system log)
- Code: `integration/integrations/first_run_permissions_integration.py`
- Config: `config/unified_config.yaml`
- Requirements: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/first_run_flow_spec.md`

## Key findings
- Provided log is macOS system log; no Nexy app first-run markers observed.
- First-run flow is skipped when `permissions_first_run_completed.flag` exists.
- V2 first-run is driven by `integrations.permissions_v2.enabled` and can be overridden by env/config.

## Likely causes to verify
- Existing flag `~/Library/Application Support/Nexy/permissions_first_run_completed.flag`.
- V2 disabled at runtime (config override / env flags).
- User inspected OS log instead of app log (`~/Library/Logs/Nexy/nexy.log`).

## Suggested verification
1) Check `~/Library/Logs/Nexy/nexy.log` for `[FIRST_RUN_PERMISSIONS]` events.
2) Remove first-run flag using `scripts/clear_first_run_flags.py` and retry.
3) Confirm `permissions_v2.enabled=true` and no kill-switches enabled.
