# Disable status control in permissions V2

## Goal
Ensure permission flow advances by time only, without status-based control or probing.

## Changes
- In timeout mode, skip FDA pre-probe and all status polling/probing; advance steps only by deadline.

## Files touched
- `modules/permissions/v2/orchestrator.py`

## Notes
- Required docs referenced by AGENTS.md are missing in this repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
