# Task Brief: Centralize startup order, feature gates, and mode-session bridge

## Done
- Centralized startup order ownership in `IntegrationFactory` and switched coordinator startup path to `IntegrationFactory.get_startup_order(...)`.
- Added `UnifiedConfigLoader.is_feature_enabled()` as single gate helper with aliases and kill-switch handling.
- Migrated action command availability checks to `is_feature_enabled()` (messages/browser/payment/whatsapp).
- Removed shared mutable `session_id` bridge in mode management and switched to request-scoped payload via `ModeController.switch_mode(..., data={session_id})`.

## Files changed
- `integration/core/integration_factory.py`
- `integration/core/simple_module_coordinator.py`
- `config/unified_config_loader.py`
- `integration/integrations/action_execution_integration.py`
- `integration/integrations/mode_management_integration.py`

## Verification
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_no_direct_state_access.py` -> OK (allowlist warnings unchanged)
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
