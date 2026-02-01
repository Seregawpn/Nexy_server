# FDA Settings Background Open

## Goal
Open Full Disk Access System Settings without stealing focus, so subsequent permission prompts (Contacts/Input) appear.

## Changes
- Added `background` flag to `_open_permission_settings` and used `open -g` for FDA.

## Notes
Required project docs referenced by AGENTS.md are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
