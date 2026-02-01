# Task Brief: packaging permissions smoke-check

## Goal
Add optional permissions smoke-check to `build_final.sh` to verify first-run events after install.

## Changes
- Added `--permissions-smoke` flag.
- Launches `/Applications/Nexy.app`, then scans `~/Library/Logs/Nexy/nexy.log` for `FIRST_RUN_PERMISSIONS` or `permissions.first_run_started` after launch.
- Fails build if expected events are not found.

## Files touched
- `packaging/build_final.sh`
