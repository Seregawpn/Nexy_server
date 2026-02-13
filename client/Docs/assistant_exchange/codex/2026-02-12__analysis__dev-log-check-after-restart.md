# Dev Log Check After Restart (2026-02-12)

## Scope
- Checked: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
- Checked: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`
- Goal: verify duplicates/conflicts/races after latest Dev restart and quit.

## Findings
1. TAL timeout:
- `TAL hold timeout (120s)` exists only in older session (`11:23`, line `15139` in `nexy-dev.log`).
- Latest session (`11:34`) has `Skip TAL hold: tray already ready and hold is inactive` and no new timeout.

2. Startup/bootstrap:
- One bootstrap in latest run: `ACTIVITY=begin reason=tray_bootstrap` at `11:34:14`.
- No evidence of extra process relaunch in the checked latest segment.

3. Quit path observability gap (still present):
- Present: `Quit requested via tray menu` and `quit() called`.
- Missing in latest segment after quit: `tray.quit_clicked` publish/dispatch, `app.shutdown` publish/dispatch, `[QUIT_ACK]`.
- Indicates quit may still bypass centralized EventBus shutdown path in this execution path.

4. Minor duplicate noise:
- Repeated `autostart.status_checked` and repeated `LaunchAgent автозапуск не найден` in startup sequence.
- Likely duplicate status checks from startup + startup-event handlers.

## Conclusion
- Hotkey/TAL startup regression looks fixed in latest run.
- Primary remaining risk is shutdown path centralization/ack visibility on tray quit.
