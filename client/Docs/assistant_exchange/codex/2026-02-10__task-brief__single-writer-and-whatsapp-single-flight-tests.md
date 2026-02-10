# Task Brief: tests for single-writer restart_pending and WhatsApp single-flight reset

## Added tests
- `tests/test_centralization_regressions.py`
  - `test_permission_restart_does_not_write_restart_pending_state`
  - `test_whatsapp_reset_is_single_flight`

## What they enforce
- `PermissionRestartIntegration` no longer writes `restart_pending` state (coordinator single-writer ownership).
- WhatsApp reset/restart scheduling is single-flight under duplicate triggers.

## Test runs
- `PYTHONPATH=. pytest -q tests/test_centralization_regressions.py` -> `2 passed`
- `pytest -q tests/test_gateways.py tests/test_interrupt_playback.py tests/test_centralization_regressions.py ../tests/test_action_execution_failure_routing.py ../tests/test_grpc_client_action_compatibility.py ../tests/test_mode_management_listening_transition.py ../tests/test_mode_management_processing_action_guard.py ../tests/test_playback_full_interrupt.py` -> `41 passed`

## Verification scripts
- `python3 scripts/verify_no_direct_state_access.py` -> OK
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
