# First-run permissions hang analysis

## Task
Analyze why the app appeared to hang after requesting microphone and screen capture permissions.

## Findings
- First-run permissions are a blocking gate in `integration/core/simple_module_coordinator.py` and the V2 pipeline waits for completion in `integration/integrations/first_run_permissions_integration.py`.
- When TCC prompts are shown, the orchestrator polls until the permission state changes; startup is intentionally halted until completion or timeout.
- This behavior makes the app look "hung" if the user delays the dialogs or a TCC prompt does not resolve.

## Evidence
- `integration/integrations/first_run_permissions_integration.py` waits on `wait_for_completion(timeout=300.0)` and returns `False` when not all hard permissions are granted.
- `integration/core/simple_module_coordinator.py` restricts startup to permissions flow on first run and stops further module loading when permissions are missing.
- Config order places `microphone` then `screen_capture` with inter-step pauses.

## Notes
- Required docs listed in AGENTS.md were not present in this repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

## Next checks (if needed)
- Inspect `~/Library/Application Support/Nexy/permission_ledger.json` for current step/state.
- Review app logs for `[FIRST_RUN_PERMISSIONS]` and `[ORCHESTRATOR]` transitions around the hang.
