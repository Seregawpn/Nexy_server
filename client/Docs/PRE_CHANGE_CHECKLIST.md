# Client Pre-Change Checklist (Mandatory)

Use before any client code edits. If any item is not satisfied, do not change code.

## 1) Required Reads
- `AGENTS.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `client/AGENTS.md`
- `client/Docs/DOCS_INDEX.md`
- `client/Docs/PROJECT_REQUIREMENTS.md` (relevant sections)
- `client/Docs/ARCHITECTURE_OVERVIEW.md` (relevant modules)
- `client/Docs/FLOW_INTERACTION_SPEC.md` (event/payload contracts)
- `client/Docs/STATE_CATALOG.md` (state ownership)
- `client/Docs/FEATURE_FLAGS.md`

## 2) Architecture Fit
- Target integration/module owner identified.
- Single Source of Truth identified.
- No local bypass around coordinator/state manager/workflow owner.

## 3) Duplication and Race Check
- Existing similar logic searched (`>=70%` similarity threshold).
- Duplicate path marked for merge/remove.
- Parallel/out-of-order/retry scenarios reviewed; guard selected if needed.

## 4) Flags and State Check
- Touched flags are documented in `client/Docs/FEATURE_FLAGS.md`.
- New state/flag has owner, scope, and removal condition.
- No shadow flags or duplicated state axes introduced.

## 5) Evidence
- Mention docs/sections used.
- Mention Source of Truth.
- Mention what duplicate was merged/removed (or `none`).
