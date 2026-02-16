# Analysis: Startup duplicate-instance loop and focus loss

Date: 2026-02-16

## Summary
Observed repeated launch/exit loop of Nexy around `01:21:16`-`01:22:05`, with frequent focus-steal behavior in macOS system log.

## Evidence

### 1) Repeated duplicate-instance shutdown loop
File: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`

- Repeating sequence every ~1s:
  - `NEXY APPLICATION START`
  - `InstanceStatus.DUPLICATE`
  - `SAFE_EXIT: duplicate_instance ... nexy.lock`
  - `NEXY APPLICATION STOP`

Examples:
- `nexy.log:20027` (`InstanceStatus.DUPLICATE`)
- `nexy.log:20029` (`SAFE_EXIT: duplicate_instance ... pid=21722`)
- `nexy.log:20067` (`NEXY APPLICATION STOP`)
- `nexy.log:20078` (`NEXY APPLICATION START`)

### 2) Browser installer spawns Nexy binary as installer command
File: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`

- Repeated command:
  - `Executing install command: [/Applications/Nexy.app/Contents/MacOS/Nexy, -m, playwright, install, chromium]`

Examples:
- `nexy.log:17071`
- `nexy.log:20054`
- `nexy.log:32380`
- `nexy.log:33126`

This command uses Nexy executable itself, which can spawn another Nexy app process instead of standalone playwright CLI flow, feeding duplicate-instance loop.

### 3) Focus-steal symptom in system log
File: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/log.md`

- `WindowServer ... StealKeyFocusReturningID ... key thief updated ... (Nexy)`

Examples:
- `log.md:4208`
- `log.md:4212`
- `log.md:4213`

Also app self-terminates (not crash):
- `log.md:4240` (`terminate:`)
- `log.md:4262` (`Process death ... Nexy`)

## Root cause conclusion
Primary issue is not updater loop itself but process lifecycle loop:
- Browser-use install path triggers command through Nexy binary.
- New process is detected as duplicate by InstanceManager and exits.
- Repeated relaunch attempts cause visible "constant updating/restarting" effect and intermittent focus steals.

## Code location likely responsible
File: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`

- `module.py:495` builds default command as `[sys.executable, "-m", "playwright", "install", "chromium"]`.
- In packaged app, `sys.executable` resolves to Nexy binary (`/Applications/Nexy.app/Contents/MacOS/Nexy`).
- Command execution is logged at `module.py:591` and run at `module.py:593`.

## Additional note
`force_activate_on_startup` is `false` in config (`config/unified_config.yaml:35`), so direct forced activation is not primary trigger here; focus loss appears as side-effect of repeated launch attempts.
