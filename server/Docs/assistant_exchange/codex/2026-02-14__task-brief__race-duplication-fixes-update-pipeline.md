# Task Brief: race/duplication fixes in update pipeline

## Scope
Fix current issues identified in update path audit:
- potential concurrent update race in client integration
- runtime manifest mutation in update server download path
- non-fail-fast git sync in publish script
- stale path usage in publish script docs

## Changes
1. `../client/integration/integrations/updater_integration.py`
- Added `self._update_lock = asyncio.Lock()`.
- Wrapped `_execute_update()` body in `async with self._update_lock`.
- Result: startup/scheduled/manual triggers cannot run update flow in parallel.

2. `server/modules/update/providers/update_server_provider.py`
- Removed runtime `manifest_provider.update_manifest(...)` from `download_handler` on size mismatch.
- Kept warning log only.
- Result: no second writer of manifest during artifact serving.

3. `server/scripts/publish_assets_and_sync.py`
- Updated docstring paths to canonical ones.
- Added `run_command_or_exit(...)` and fail-fast behavior for:
  - `git add`
  - `git commit`
  - `git push`
- Result: script no longer reports success when git sync actually failed.

## Validation
- AST parse passed for all changed files:
  - `server/modules/update/providers/update_server_provider.py`
  - `server/scripts/publish_assets_and_sync.py`
  - `../client/integration/integrations/updater_integration.py`

## Risk/impact
- No new state machines introduced.
- Update execution now serialized at integration boundary.
- Manifest source-of-truth no longer mutated by runtime download path.
