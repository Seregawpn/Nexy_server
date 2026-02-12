# Pre-Change Checklist (Mandatory)

Use this checklist before any code edits. If any item is not satisfied, do not change code.

## 1) Required Reads
- `Docs/PROJECT_REQUIREMENTS.md` (relevant sections)
- `Docs/ARCHITECTURE_OVERVIEW.md` (relevant modules/layers)
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/FEATURE_FLAGS.md`
- `Docs/DOCS_INDEX.md`

## 2) Architecture Fit
- Target module/layer/workflow owner identified.
- Single Source of Truth identified.
- No bypass of coordinator/state manager/workflow owner.

## 3) Duplication Check
- Existing similar logic searched (`>=70%` similarity check).
- Duplicate paths identified and planned for merge/remove.

## 4) Race/Ordering Check
- Parallel/retry/out-of-order scenarios reviewed.
- Guard selected if needed: `single-flight` / `mutex` / `state-guard` / `idempotency` / `coordinator`.

## 5) Feature Flag Check
- Any touched flag exists in `Docs/FEATURE_FLAGS.md`.
- For new/changed flag: owner, scope, default, remove-condition, conflicts documented first.
- No conflicting or shadow flag introduced.

## 6) Change Boundary
- Minimal touchpoints listed (module/file/function).
- No extra local states/flags without owner.

## 7) Evidence in Output/Report
- Mention which docs/sections were used.
- Explicitly state Source of Truth.
- Explicitly state what duplicate was merged/removed (or `none`).
