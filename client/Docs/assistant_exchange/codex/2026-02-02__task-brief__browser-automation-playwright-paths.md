# Browser automation Playwright paths fix

## Changes
- Set deterministic `PLAYWRIGHT_BROWSERS_PATH` to `~/Library/Application Support/Nexy/ms-playwright`.
- Ensure driver executable bit in frozen mode.
- Log install stdout/stderr for diagnostics.

## Files touched
- modules/browser_automation/module.py

## Notes
- Required docs missing in repo: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md
