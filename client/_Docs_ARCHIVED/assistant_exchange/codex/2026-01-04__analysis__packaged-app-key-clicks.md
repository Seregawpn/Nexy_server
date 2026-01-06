# Analysis: packaged app key click sounds

- Context: system click/beep when holding Ctrl+N (PTT) in packaged .app.
- Primary hypothesis: Quartz backend fails in .app and input falls back to pynput, which cannot suppress key events, so AppKit emits NSBeep for unhandled key equivalent.
- Secondary hypothesis: app is activated (activateIgnoringOtherApps_) so unhandled keyDown reaches NSApplication and beeps even if partial suppression occurs.
- Architecture fit: input_processing keyboard backend is the owner of event suppression; avoid UI-level workarounds.
- Proposed direction: require Quartz for ctrl_n in .app, ensure full suppression of combo keyDown/Up (and optionally flagsChanged) when combo mode is active; surface permission errors instead of silent fallback.
- Quick checks: inspect logs for "QuartzKeyboardMonitor успешно запущен" vs "fallback на pynput"; verify Accessibility/Input Monitoring granted to .app bundle.
- Files inspected: modules/input_processing/keyboard/mac/quartz_monitor.py, modules/input_processing/keyboard/keyboard_monitor.py, integration/integrations/input_processing_integration.py, main.py, modules/tray_controller/macos/menu_handler.py, config/unified_config.yaml.
- Missing required docs in repo: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md.
