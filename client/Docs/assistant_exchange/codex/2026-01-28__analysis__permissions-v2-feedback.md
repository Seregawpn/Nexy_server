# Permissions V2 feedback

## Task
Review permissions V2 pipeline and provide feedback.

## Observations
- V2 pipeline is strictly sequential; AUTO_DIALOG steps block on polling until PASS/FAIL/NEEDS_RESTART.
- “Timed cell” behavior (auto-advance without status) is not implemented; grace/poll only control waiting cadence.
- first-run integration hard-blocks startup via `wait_for_completion()` and coordinator restricts modules until permissions are granted.

## Strengths
- Centralized FSM in `PermissionOrchestrator` with ledger persistence.
- Clear classifier separation and normalization via error_matrix.
- Restart safety for Input Monitoring with needs-restart confirmation.

## Risks / Issues
- Perceived app hang during TCC prompts due to blocking startup.
- FDA probe can return `NO_TEST_PATH`, which may leave status ambiguous on some systems.
- Contacts classifier returns WAITING_USER on denied, but contacts step is `auto_dialog` (no Settings navigation); may require UX consistency check.

## Missing required docs
The following required sources were not present in repo:
- Docs/ASSISTANT_COORDINATION_PROTOCOL.md
- Docs/ANTIGRAVITY_PROMPT.md
- Docs/CODEX_PROMPT.md
- Docs/assistant_exchange/TEMPLATE.md

## Next checks (cheap)
- Inspect permission ledger in `~/Library/Application Support/Nexy/permission_ledger.json` to see stuck step state.
- Confirm actual behavior of contacts dialog vs. settings workflow.
