# Task Brief: Targeted validation (mode/action/interrupt)

## Commands
- `python3 scripts/verify_feature_flags.py`
- `python3 scripts/verify_no_direct_state_access.py`
- `python3 scripts/verify_4_artifacts_invariant.py`
- `python3 scripts/verify_rule_coverage.py`
- `pytest -q tests/test_gateways.py tests/test_interrupt_playback.py ../tests/test_action_execution_failure_routing.py ../tests/test_grpc_client_action_compatibility.py ../tests/test_mode_management_listening_transition.py ../tests/test_mode_management_processing_action_guard.py ../tests/test_playback_full_interrupt.py`

## Results
- Feature flags registry: OK
- Direct state access check: OK (1 expected allowlist warning for input_processing)
- 4-artifacts invariant: OK
- Gateway coverage: OK
- Pytest: `39 passed in 2.01s`
