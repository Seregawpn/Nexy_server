# Analysis: nexy.log check (first-run)

## What was checked
- `~/Library/Logs/Nexy/nexy.log`
- Flag file: `~/Library/Application Support/Nexy/permissions_first_run_completed.flag`

## Findings
- Latest first-run related entries are dated **2026-01-28**.
- Log contains a prior dev-bypass line on **2026-01-28 13:36:20**.
- No entries from **2026-01-29** were found in the log.
- Flag file `permissions_first_run_completed.flag` is **absent**.

## Implication
- Current “problem repeats” cannot be diagnosed from today’s app log; likely using an older build or log not updating.

## Next checks
- Provide fresh `nexy.log` lines from today’s run and confirm which build is launched.
