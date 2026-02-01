# Reset First-Run Flags + TCC (Contacts)

## Date
2026-01-26

## Actions
- Removed first-run flags and ledger:
  - `~/Library/Application Support/Nexy/permissions_first_run_completed.flag`
  - `~/Library/Application Support/Nexy/permission_ledger.json`
- Attempted TCC reset for Contacts:
  - `tccutil reset Contacts com.nexy.assistant` → failed (exit 70)
  - `tccutil reset Contacts` → failed (exit 70)

## Result
Flags/ledger removed. Contacts TCC reset failed (permissions/OS restriction).

## Next Step
User needs to reset Contacts permission manually in System Settings (Privacy & Security → Contacts) or run `tccutil` in an environment that allows it (macOS restriction may require Full Disk Access for Terminal or admin action).
