# Server Runtime Docs Index (Canonical)

Purpose: one canonical map for server runtime analysis and code changes.

## Canonical (Source of Truth)
- `server/server/AGENTS.md` — assistant rules for server runtime workspace.
- `server/server/Docs/ARCHITECTURE_OVERVIEW.md` — server architecture and boundaries.
- `server/server/Docs/SERVER_DEVELOPMENT_RULES.md` — mandatory server engineering gates.
- `server/server/Docs/SERVER_PROTOBUF_SPECIFICATION.md` — protocol behavior and field expectations.
- `server/server/Docs/GRPC_PROTOCOL_AUDIT.md` — compatibility and gRPC contract checks.
- `server/server/Docs/FEATURE_FLAGS.md` — server runtime flag registry/behavior.
- `server/server/Docs/PRE_CHANGE_CHECKLIST.md` — mandatory gate before code edits.

## Global Canonical References
- `AGENTS.md`
- `Docs/DOCS_INDEX.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`

## Archived / Reference-only (Non-authoritative)
- `server/server/Docs/_archive/*`

Rules:
1. `server/server/Docs/_archive/*` must not be used as Source of Truth.
2. API changes must start from `server/modules/grpc_service/streaming.proto`.
3. If server runtime docs conflict with root process docs, root docs define workflow and server docs define runtime implementation.
