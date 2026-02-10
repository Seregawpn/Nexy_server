# Analysis: User feedback on Command/Spotlight/menu collapse and auto-relaunch

## User feedback
- Command shortcuts feel broken.
- Cmd+Space opens Spotlight then it disappears.
- App/menu interactions disappear after a few seconds.
- Quit from status menu relaunches app.

## Findings
1. Input hotkey layer does not intentionally block Command key globally.
   - `modules/input_processing/keyboard/mac/quartz_monitor.py` suppresses `Ctrl+N` combo path only.
2. App explicitly re-activates itself on startup:
   - `main.py` calls `activateIgnoringOtherApps_(True)` in `activate_nsapplication_for_menu_bar()`.
   - `modules/tray_controller/core/tray_controller.py` also calls `nsapp.activateIgnoringOtherApps_(True)` before `app.run()`.
3. Quit→relaunch symptom is consistent with external autostart source.
   - Project has known legacy autostart history (`Docs/assistant_exchange/codex/2026-02-05__analysis__quit-relaunch.md`).
   - Current integration defaults to monitor mode; legacy cleanup is optional (`integration/integrations/autostart_manager_integration.py`).

## Local machine snapshot (now)
- `/Library/LaunchAgents` has no legacy Nexy plist currently; contains `nexy_launcher.sh`.
- No Nexy process was running at check time.

## Conclusion
- Feedback is plausible and likely true for affected environment.
- Most probable mechanism:
  1) app relaunch/focus activation steals foreground, collapsing Spotlight/menu;
  2) external autostart source relaunches after Quit.
