# Analysis: shutdown/restart logic audit and implementation plan

## Scope
- Audited current shutdown and restart flow in code + runtime logs.
- Focus: manual quit path vs delayed permission restart helper relaunch.

## Confirmed runtime facts
- `log.md` shows normal process exit (`Entering exit handler`, process death).
- Same log shows external relaunch command after quit window:
  - `logger launching: /usr/bin/open -a /Applications/Nexy.app`
- Command source is restart helper in:
  - `modules/permission_restart/macos/permissions_restart_handler.py::_spawn_delayed_launch_helper`.

## Current architecture observations
1. Restart owners
   - V2 orchestrator (`modules/permissions/v2/orchestrator.py`) triggers restart via `restart_handler.trigger_restart(...)`.
   - Legacy permission restart integration also has scheduling/guards but is frozen in V2 mode for transition events.
2. Quit intent ownership is currently split
   - `integration/core/simple_module_coordinator.py::_on_user_quit` sets `StateKeys.USER_QUIT_INTENT`.
   - `integration/integrations/tray_controller_integration.py::_on_tray_quit` also sets the same flag.
3. Detached helper gap
   - Existing guards abort restart before `trigger_restart`.
   - Already spawned detached helper is not cancelled by user quit and may still call `open -a`.

## Flags and interaction points mapped
- State keys:
  - `user_quit_intent`
  - `permissions_restart_pending`
  - `update_in_progress`
- Files/signals:
  - `restart_in_progress.lock`
  - `restart_completed.flag`
  - `permission_ledger.json`
- Env flags:
  - `NEXY_DISABLE_AUTO_RESTART`
  - `NEXY_KS_FIRST_RUN_RESTART`
  - `NEXY_FIRST_RUN_RESTARTED`
  - `NEXY_BYPASS_PERMISSION_READY`
- Events:
  - `tray.quit_clicked`
  - `app.shutdown`
  - V2 permission phase events and restart-related UI events
- Alternate quit source:
  - `action_execution_integration` publishes `tray.quit_clicked` for self-close.

## Primary plan (architecture-safe)
1. Keep restart decision centralized in permission restart owner path.
2. Introduce single persistent abort marker for helper launch check (owner: permission restart handler).
3. On all user-quit entry points set abort marker before UI/process quit.
4. In delayed helper script check abort marker immediately before `open -a`; skip launch if set.
5. On clean startup clear stale abort marker once owner initialized.
6. Remove duplicate writer behavior for `user_quit_intent` (single writer in coordinator).

## Risks
- Medium duplication risk if both coordinator and tray integration continue writing quit-intent independently.
- High race risk without helper-level abort check.

