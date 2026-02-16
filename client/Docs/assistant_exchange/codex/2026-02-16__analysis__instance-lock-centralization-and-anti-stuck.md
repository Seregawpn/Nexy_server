# Analysis: instance lock centralization and anti-stuck

## Summary
Implemented next-stage hardening for PM lock behavior and centralized read-only instance probe config.

## Changes
- Added `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/instance_manager/core/runtime_helpers.py`:
  - `resolve_lock_file_path()`
  - `make_probe_config()`
- Exported helpers from `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/instance_manager/__init__.py`.
- Refactored duplicate probe config in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/updater/updater.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/updater/migrate.py`
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/instance_manager/core/instance_manager.py`:
  - `AccessDenied/ZombieProcess` keeps lock valid only within `timeout_seconds`.
  - After timeout, lock treated stale to prevent permanent startup block.

## Architecture gates
- Single owner: `InstanceManager` remains lock decision owner.
- Zero duplication: updater/migrate probe config merged into single helper.
- Anti-race: conservative AccessDenied handling + anti-stuck TTL.
- Flag lifecycle: no new runtime flags.

## Validation
- `python3 -m py_compile modules/instance_manager/core/runtime_helpers.py modules/instance_manager/core/instance_manager.py modules/updater/updater.py modules/updater/migrate.py modules/browser_automation/module.py`
- Result: success.
