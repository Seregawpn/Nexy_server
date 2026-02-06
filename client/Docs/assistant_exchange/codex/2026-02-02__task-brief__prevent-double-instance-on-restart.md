# Prevent Double Instance on Restart

Date: 2026-02-02
Assistant: Codex

## Summary
Fixed restart handler logic to avoid launching the dev process when a packaged relaunch already succeeded, preventing double instances (two tray icons).

## Changes
- `modules/permission_restart/macos/permissions_restart_handler.py`: guarded dev fallback behind `restart_successful` check; unified sleep timing.

## Rationale
When a packaged Nexy.app is found during a dev run, the handler could launch the packaged app and then also launch the dev Python process, creating two instances and two tray icons. The fix enforces a single restart path.

## Verification
- Trigger restart in a dev run with a packaged app present; confirm only one instance/tray icon appears.
- Check logs: no dev restart log if packaged relaunch succeeded.

## Missing Required Docs
Required docs referenced by `AGENTS.md` are not present in this repo snapshot:
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
