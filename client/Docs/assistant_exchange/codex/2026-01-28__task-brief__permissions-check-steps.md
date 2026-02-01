# Task Brief: permissions check steps

## Goal
Provide minimal steps to verify why permission flow was skipped (bypass vs first-run flag vs packaging).

## Steps Suggested
- Check env bypass: run with `NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS=1`.
- Check first-run flags: `python scripts/clear_first_run_flags.py`.
- Check app logs for `FIRST_RUN_PERMISSIONS`.
- Inspect `.app/Contents/Resources/` if packaging suspicion.

## Notes
- Required docs referenced in AGENTS instructions are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
