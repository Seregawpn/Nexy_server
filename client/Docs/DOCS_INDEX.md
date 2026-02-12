# Client Docs Index (Canonical)

Purpose: one canonical map for client-side analysis and code changes.

## Canonical (Source of Truth)
- `client/AGENTS.md` — assistant rules for client workspace.
- `client/Docs/README.md` — high-level documentation index.
- `client/Docs/DOCUMENTATION_MAP.md` — navigation and document relationships.
- `client/Docs/PROJECT_REQUIREMENTS.md` — product/client requirements.
- `client/Docs/ARCHITECTURE_OVERVIEW.md` — client architecture and boundaries.
- `client/Docs/FLOW_INTERACTION_SPEC.md` — canonical interaction contracts.
- `client/Docs/STATE_CATALOG.md` — state axes and ownership.
- `client/Docs/FEATURE_FLAGS.md` — client flag behavior and controls.
- `client/Docs/PRE_CHANGE_CHECKLIST.md` — mandatory gate before code edits.

## Global Canonical References
- `AGENTS.md`
- `Docs/DOCS_INDEX.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`

## Archived / Reference-only (Non-authoritative)
- `client/Docs/_archive/*`

Rules:
1. `client/Docs/_archive/*` must not be used as Source of Truth.
2. If client docs conflict with root process docs, root process docs define workflow and client docs define implementation details.
