# Analysis: Assistant Prompt Path Alignment

## Scope
- Validate assistant-governing files and mandatory source references.
- Align server-level AGENTS files with real repository paths.

## Findings
- Separate `agent.md`, `antigravity.md`, `codex.md` files are not present in this workspace.
- Governance is currently defined by:
  - `AGENTS.md`
  - `server/AGENTS.md`
- Multiple mandatory links previously pointed to missing paths.

## Changes Applied
- Updated `AGENTS.md` (server root) to use existing mandatory document paths.
- Updated `server/AGENTS.md` (nested server scope) to use existing relative paths from that directory.
- Fixed invalid release guide path reference and CRM instruction path.
- Added a quick source-validation note in server root AGENTS.

## Validation
- All mandatory paths referenced in both updated files now resolve successfully.
- API contract path and release guide path resolve from both working directories.
