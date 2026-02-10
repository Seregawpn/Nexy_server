# Analysis: conflicts / duplicates / races / centralization / flags

## Scope
- Project docs checked: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/STATE_CATALOG.md`, `Docs/FEATURE_FLAGS.md`
- Verification scripts: `scripts/verify_feature_flags.py`, `scripts/verify_no_direct_state_access.py`, `scripts/verify_4_artifacts_invariant.py`, `scripts/verify_rule_coverage.py`

## Key findings

1. **Startup order has two owners (duplication/conflict)**
- `integration/core/simple_module_coordinator.py:413` defines hardcoded `startup_order`.
- `integration/core/integration_factory.py:66` also defines `STARTUP_ORDER`.
- Orders diverge (e.g. tray position differs), so REQ-006 can silently drift.

2. **Real race in mode/session bridge**
- `integration/integrations/mode_management_integration.py:642` writes shared `_pending_session_id_for_callback` before awaiting controller lock.
- `integration/integrations/mode_management_integration.py:137` callback reads this shared field later.
- Concurrent `mode.request` can overwrite session id before first callback executes.

3. **Feature flags are formally “OK” but semantically inconsistent**
- `scripts/verify_feature_flags.py` checks only presence in registry, not defaults/owner semantics.
- `Docs/FEATURE_FLAGS.md:49` says `features.payment` default=true.
- `config/unified_config.yaml:592` has no `features.payment` key.
- `integration/core/integration_factory.py:375` treats missing payment feature as disabled (`get(..., False)`).
- `integration/integrations/action_execution_integration.py:288` treats missing payment feature as enabled (`get(..., True)`).
- Result: command path and integration registration disagree.

4. **State access centralization still partially bypassed (known debt)**
- `scripts/verify_no_direct_state_access.py:17` keeps allowlist for critical integrations.
- Direct reads/writes remain in `input_processing`, `mode_management`, `permission_restart`, `updater`, `voice_recognition`.
- This contradicts strict REQ-004 target and keeps mixed SoT access patterns.

5. **First-run/restart axes have multiple writers**
- Coordinator writes first-run and restart-pending (`integration/core/simple_module_coordinator.py:895`, `:919`, `:1415`).
- PermissionRestartIntegration also writes restart-pending (`integration/integrations/permission_restart_integration.py:247`).
- Even with same boolean value, this is not single-writer ownership.

6. **Dead/legacy event path still subscribed**
- Updater subscribes to `mode.changed` (`integration/integrations/updater_integration.py:219`), but publishers are `app.mode_changed`.
- Increases cognitive load and suggests unfinished migration.

## Script results
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_no_direct_state_access.py` -> OK with allowlisted exceptions
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
- `python3 scripts/verify_architecture.py` -> missing file (doc/process drift)

## Recommended centralization direction
1. Keep **single owner of startup order** in `IntegrationFactory`, remove coordinator-local order.
2. Replace shared `_pending_session_id_for_callback` with request-scoped transfer (payload/data on transition callback).
3. Unify feature-gate semantics via one helper (`is_feature_enabled`) with one default policy.
4. Remove allowlist by migrating remaining direct state access to selectors/gateways.
5. Assign exactly one writer for `first_run` and `restart_pending` (prefer V2 ledger adapter).
