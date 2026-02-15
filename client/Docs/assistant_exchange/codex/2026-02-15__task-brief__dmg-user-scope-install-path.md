# Task Brief: DMG install path switched to user scope (no /Applications replace)

Date: 2026-02-15
Owner: Codex

## What changed
File: `modules/updater/updater.py`

1. Added `self._last_installed_app_path` to remember where update was installed.
2. `get_current_build()` now reads version from the currently running app bundle (`get_current_app_path()`), fallback to configured app path.
3. In `install_update()` for DMG:
   - If target resolves to `/Applications/...`, installer switches target to `~/Applications/Nexy.app` via `self.config.get_user_app_path()`.
   - Performs atomic replace in user scope path.
   - Stores installed path in `_last_installed_app_path`.
4. `relaunch_app()` now relaunches from `_last_installed_app_path` when available.

## Why
- Prevent permission-denied failures from replacing `/Applications/Nexy.app` using DMG path.
- Avoid repeated update loops caused by failed system-scope replacement.

## Validation
- `python3 -m py_compile modules/updater/updater.py modules/updater/migrate.py modules/updater/replace.py` passed.

## Expected behavior
- DMG update installs to `~/Applications/Nexy.app`.
- Relaunch opens updated app from user scope.
- Next update check reads current build from running app path.
