# Task Brief: Reduce permissions timeout to 15s

## Change
- Updated `permissions.first_run.max_wait_sec` from 30 to 15 in `config/unified_config.yaml`.

## Reason
- Shorten first-run wait time per permission to reduce long startup delays.

## Files
- config/unified_config.yaml

## Verification
- Run first-run flow and confirm timeouts occur at ~15s per permission.
