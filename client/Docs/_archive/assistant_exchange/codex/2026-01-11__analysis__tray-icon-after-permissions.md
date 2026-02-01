Title: Tray icon missing after permissions
Date: 2026-01-11
Type: analysis

Context:
- Checked app log at /var/folders/.../nexy_debug.log.
- Focused on tray startup around permissions flow.

Findings:
- Tray startup sequence executed: NSApplication activated, app.run called, status item created.
- Icon updates succeeded and tray creation attempt 1 succeeded.
- Input Monitoring permission is denied; tray briefly switched to LOCKED then back to SLEEPING.

Implication:
- Tray icon should be present; issue likely not in tray startup.
- If icon not visible, investigate OS-level menubar behavior or app bundle context.
