# Task Brief — FDA pre-probe to ensure TCC entry

## Goal
Make the app appear in Full Disk Access list before opening Settings by forcing a protected-file stat.

## Changes
- Added `~/Library/Application Support/com.apple.TCC/TCC.db` to FDA test paths.
- Added FDA pre-probe (heavy) before opening Settings when the step hasn’t been probed yet.

## Files
- modules/permissions/v2/probers/full_disk_access.py
- modules/permissions/v2/orchestrator.py

## Verification
- Launch app, reach FDA step, open Privacy → Full Disk Access.
- Expect app listed and `FDA_PROBER stat(...) permission denied` in logs.
