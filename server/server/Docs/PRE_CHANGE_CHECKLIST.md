# Server Runtime Pre-Change Checklist (Mandatory)

Use before any server runtime code edits. If any item is not satisfied, do not change code.

## 1) Required Reads
- `AGENTS.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `server/server/AGENTS.md`
- `server/server/Docs/DOCS_INDEX.md`
- `server/server/Docs/ARCHITECTURE_OVERVIEW.md` (relevant sections)
- `server/server/Docs/SERVER_DEVELOPMENT_RULES.md` (gates/rules)
- `server/server/Docs/FEATURE_FLAGS.md`
- `server/server/Docs/GRPC_PROTOCOL_AUDIT.md` (for API changes)

## 2) Architecture Fit
- Target module/integration owner identified.
- Single Source of Truth identified.
- No direct cross-module shortcuts that bypass coordinator/integration boundaries.

## 3) API Contract Check (if touched)
- `server/modules/grpc_service/streaming.proto` updated first.
- Backward compatibility validated.
- Protobuf regeneration and dependent updates planned.

## 4) Duplication and Race Check
- Existing similar logic searched (`>=70%` similarity threshold).
- Duplicate path marked for merge/remove.
- Parallel/retry/out-of-order scenarios reviewed; guard selected if needed.

## 5) Flags and State Check
- Touched flags documented in `server/server/Docs/FEATURE_FLAGS.md`.
- New state/flag has owner, scope, and removal condition.
- No shadow flags or duplicated decision paths introduced.

## 6) Evidence
- Mention docs/sections used.
- Mention Source of Truth.
- Mention what duplicate was merged/removed (or `none`).
