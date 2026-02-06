# Task Brief: prefer dev restart when running from terminal

## Goal
Ensure that when running from source (non-frozen), the restart stays in the dev process and does not relaunch the packaged .app.

## Changes
- `PermissionsRestartHandler` now immediately chooses dev restart when `sys.frozen` is False.
- Packaged relaunch is skipped for non-frozen runs.

## Files Touched
- `modules/permission_restart/macos/permissions_restart_handler.py`

## Verification
- Run `python main.py` and trigger permissions restart.
- Expected: log "Dev restart preferred (non-frozen build), skipping packaged relaunch" and new dev process starts.
