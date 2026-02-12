# Analysis: Gateway restart_pending cleanup + subscription dedupe (pass 2)

## Scope
- Remove legacy `restart_pending` decision path remnants from gateway/rule layer.
- Remove duplicate `system.permissions_ready` subscription in VoiceOver ducking integration.
- Align tests/contracts with centralized first-run restart flow.

## Changes
- `integration/core/gateways/predicates.py`
  - Removed predicates: `app.restart_pending`, `app.first_run_restart_pending`.
- `integration/core/gateways/common.py`
  - Removed `restart_pending` from fallback routing logic.
  - `decide_continue_integration_startup` fallback now blocks on `first_run` only.
  - Simplified decision log context (no restart_pending axis).
- `integration/core/gateways/permission_gateways.py`
  - Removed fallback abort branch `first_run && restart_pending`.
- `integration/core/selectors.py`
  - `is_restart_pending()` changed to legacy compatibility stub returning `False`.
  - Snapshot now hard-sets `restart_pending=False`.
- `config/interaction_matrix.yaml`
  - Removed rules referencing `app.restart_pending` / `app.first_run_restart_pending`.
  - Kept centralized startup block rule based on `app.first_run=true`.
- `integration/integrations/voiceover_ducking_integration.py`
  - Removed duplicated `system.permissions_ready` subscription in non-first-run initialize branch.
- Tests updated:
  - `tests/test_gateways.py`
  - `tests/test_event_ownership_contract.py`
  - `tests/test_restart_pending_selector_gateway.py`

## Validation
- `python3 -m py_compile ...` (changed files): OK
- `PYTHONPATH=. pytest -q tests/test_gateways.py tests/test_event_ownership_contract.py tests/test_restart_pending_selector_gateway.py tests/test_coordinator_critical_subscriptions.py tests/test_centralization_regressions.py`
  - Result: `24 passed`

## Result
- Legacy restart_pending axis no longer participates in runtime decisions.
- One centralized restart path remains: coordinator -> permission_restart integration.
- Duplicate VoiceOver event subscription removed.
