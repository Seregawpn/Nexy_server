# Task Brief: Instance lock race hardening

## Context
Observed duplicate-start loops and focus loss behavior were linked to instance lock instability under fallback/access-error paths.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/instance_manager/core/instance_manager.py`.
- `psutil.AccessDenied`/`psutil.ZombieProcess` now keep lock as valid (conservative duplicate protection).
- Removed unsafe unconditional deletion of fallback lock file in `_switch_to_fallback_lock()`.

## Architecture gates
- Single owner: `InstanceManager` remains owner of runtime single-instance lock decisions.
- Zero duplication: no new lock path/owner introduced.
- Anti-race: removed path that could delete active lock from another process.
- Flag lifecycle: no new flags.

## Verification
- `python3 -m py_compile modules/instance_manager/core/instance_manager.py integration/integrations/instance_manager_integration.py modules/browser_automation/module.py`
- Result: success.

## Expected runtime effect
- Reduced risk of false lock cleanup and concurrent launches.
- Lower chance of repeated startup/exit loop and focus steal side-effects.
