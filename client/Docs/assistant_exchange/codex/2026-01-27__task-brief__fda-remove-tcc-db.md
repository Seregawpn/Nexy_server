# Task Brief — Remove TCC.db from FDA probe

## Goal
Avoid false PASS for Full Disk Access caused by probing TCC.db.

## Change
- Removed `~/Library/Application Support/com.apple.TCC/TCC.db` from `FDA_TEST_PATTERNS`.

## File
- modules/permissions/v2/probers/full_disk_access.py
