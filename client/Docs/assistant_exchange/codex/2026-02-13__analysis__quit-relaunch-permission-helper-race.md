# Analysis: quit -> relaunch via permission restart helper

## Context
- User symptom: after manual Quit from status menu, app exits and then appears again.
- Checked logs: `log.md` and `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`.

## Key timeline (confirmed)
- `2026-02-12 20:25:24` in `log.md`: app exits normally (`Entering exit handler`, process death).
- `2026-02-12 20:23:47` in `log.md`: external launch appears as:
  - `logger launching: /usr/bin/open -a /Applications/Nexy.app`
  - followed by new `CHECKIN` with new PID.
- The exact `logger launching: ...` message is produced by restart helper code in:
  - `modules/permission_restart/macos/permissions_restart_handler.py` (`_spawn_delayed_launch_helper`).

## Root cause
- Relaunch is coming from detached permission-restart helper (shell helper started earlier).
- Helper survives parent process shutdown and can still call `open -a` after manual Quit.
- Current abort guards (`user_quit_intent`) exist in orchestrator/integration runtime checks, but they do not cancel an already spawned detached helper.

## Architecture fit
- Restart ownership is centralized in permissions pipeline (`permissions v2 orchestrator` + `permission_restart handler`) and must stay there.
- Fix should be in restart owner path only, not in tray/VoiceOver paths.

## Primary fix direction
1. Add persistent abort marker owned by restart owner (e.g., `restart_abort.flag` in Nexy user data dir).
2. On manual quit (`tray.quit_clicked` path), set abort marker before UI quit.
3. In `_spawn_delayed_launch_helper`, check abort marker immediately before `open -a`; if set, skip launch.
4. Clear marker on clean app startup after ownership is re-established.

## Risk notes
- Without this guard, restart helper can relaunch after any late user quit.
- This is a race between detached helper and explicit quit intent.

