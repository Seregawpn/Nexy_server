# Task Brief — Restart require_needs_restart logic

Date: 2026-02-03
Assistant: Codex

## Summary
Reviewed restart decision logic and configuration for permissions v2. Confirmed behavior when `require_needs_restart=false` and how it interacts with `require_all_hard_pass` and the safety guard.

## Sources Checked
- `modules/permissions/v2/orchestrator.py`
- `modules/permissions/v2/types.py`
- `config/unified_config.yaml`

## Key Findings
- `require_needs_restart` default is `true` in `RestartConfig` and currently set to `true` in `config/unified_config.yaml`.
- If `require_needs_restart=false`, restart can become unconditional **after** all HARD permissions are PASS/NEEDS_RESTART because the function returns `bool(hard_permissions)`.
- Independent safety guard: any HARD in `NEEDS_RESTART` triggers restart regardless of `require_needs_restart`.

## Missing Required Docs
The following required docs referenced by AGENTS instructions were not present in the repo:
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
