# Analysis — Defer restart until first-run complete

Date: 2026-02-03
Assistant: Codex

## Goal
Ensure the app does not restart until the first-run permissions flow is fully finished.

## Findings
- V2 permissions orchestrator triggers restart after all steps complete but before phase `COMPLETED`.
- StateManager treats `Phase.RESTART_PENDING` as `first_run_in_progress=True`.
- V1 first-run batching can restart mid-flow via `permissions.first_run_restart_pending` events.

## Likely Causes
- V1 batching restarts (if V2 is disabled or unavailable).
- V2 restart happens before first-run completion event, which may be perceived as “restart before end”.

## Candidate Fixes
- Prefer V2: ensure `permissions_v2.enabled=true` and V2 integration initializes successfully.
- If V1 path is used: change handling of `permissions.first_run_restart_pending` to schedule restart only after last batch, or disable batching.
- Consider redefining `first_run_in_progress` mapping to exclude `Phase.RESTART_PENDING` if the product definition considers first-run complete at that point.

## Files Touched
None.

## Missing Required Docs
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
