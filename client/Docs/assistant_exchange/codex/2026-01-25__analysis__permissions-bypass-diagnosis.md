# Analysis: permissions bypass diagnosis

## Findings
- Logs show multiple `terminal_launch: permissions bypass enabled` entries, meaning many runs were from terminal with bypass enabled.
- `permissions_first_run_completed.flag` is currently missing.
- `permission_ledger.json` contains entries for `contacts`, `accessibility`, and `full_disk_access` with `current_step` set to `full_disk_access`.

## Conclusion
The observed missing prompts are most likely due to terminal launch bypass; ledger indicates steps exist but bypass prevents real dialogs. Running from `/Applications/Nexy.app` without bypass is required for full prompt flow.
