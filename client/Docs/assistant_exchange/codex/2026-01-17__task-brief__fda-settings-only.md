# FDA Settings Only

## Goal
Disable the Full Disk Access dialog and open System Settings directly while still attempting access so the app appears in the FDA list.

## Changes
- Replaced FDA dialog flow with settings-only flow in `modules/permissions/first_run/activator.py`.
- Kept async access attempt to register the app in the FDA list.

## Notes
Required project docs referenced by AGENTS.md are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
