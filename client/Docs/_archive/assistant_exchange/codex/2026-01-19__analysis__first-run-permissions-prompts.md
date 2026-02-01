# First-Run Permission Prompts (Analysis)

## Context
- User reports simultaneous permission prompts and missing prompts during first run.
- Reviewed first-run flow, activators, and unified config.

## Key Findings
- First-run activation is sequential with fixed hold/pause, but it does not wait for user response.
- macOS TCC is known to rate-limit prompts when requesting 4+ permissions in one session (not handled in code).
- Batch settings exist in `config/unified_config.yaml` (`permissions.first_run.enable_batching`), but no batching logic is implemented in `FirstRunPermissionsIntegration`.
- Required docs `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, and `Docs/assistant_exchange/TEMPLATE.md` are missing in the repo snapshot.

## Proposed Direction
- Implement config-driven batching in `integration/integrations/first_run_permissions_integration.py` to request N permissions per session, trigger restart, and continue on next launch.
- Persist batch progress in a single owned state file under `~/Library/Application Support/Nexy/` (owned by FirstRunPermissionsIntegration).
- Keep activation order sourced from `config/unified_config.yaml` (`integrations.permissions.required_permissions`).

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/activator.py`
- `config/unified_config.yaml`

## Risks
- New persisted progress state must be treated as the single source of truth to avoid duplication.
- Behavior change requires test coverage for multi-restart flows.
