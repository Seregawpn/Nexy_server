# Documentation Index (Canonical Sources)

Purpose: one authoritative map for project documentation used for analysis and code changes.

## Canonical (Source of Truth)
- `AGENTS.md` — global assistant rules and required response/process format.
- `Docs/CODEX_PROMPT.md` — Codex-specific operational rules.
- `Docs/ANTIGRAVITY_PROMPT.md` — Antigravity-specific operational rules.
- `Docs/PROJECT_REQUIREMENTS.md` — product and functional requirements.
- `Docs/ARCHITECTURE_OVERVIEW.md` — architecture boundaries, layers, ownership.
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md` — cross-assistant workflow and document exchange.
- `Docs/FEATURE_FLAGS.md` — feature-flag ownership, scope, conflicts, and rollout constraints.
- `Docs/PRE_CHANGE_CHECKLIST.md` — mandatory gate before any code edits.
- `Docs/assistant_exchange/TEMPLATE.md` — mandatory report template.

## Archived / Reference-only (Non-authoritative)
- `Docs/_archive/*` — historical snapshots and references.

Rules:
1. Files under `Docs/_archive/` must not be used as Source of Truth.
2. If canonical and archived documents conflict, canonical always wins.
3. If a canonical document is missing, restore it first, then proceed with analysis/changes.
