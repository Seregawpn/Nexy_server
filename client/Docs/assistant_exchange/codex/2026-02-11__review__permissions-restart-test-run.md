# Scope
Runtime and policy verification for first-run permissions/restart flow after centralization changes.

# Executed
- `PYTHONPATH=. pytest -q tests/test_restart_pending_state_keys.py tests/test_permissions_v2_ready_to_greet_guard.py tests/test_permissions_completed_state.py tests/test_coordinator_critical_subscriptions.py tests/test_welcome_startup_sequence.py`
- `PYTHONPATH=. pytest -q tests/test_permissions_v2_restart_policy.py tests/test_permission_v2_simulation.py`

# Result
- Initial run: one failure in `tests/test_permissions_v2_restart_policy.py` due to outdated expectation (`advance_on_timeout` expected restart).
- Updated test to current policy: timeout mode completes without restart.
- Re-run: all green.

# Final Status
- `15 passed` in focused policy/restart suite.
- No new runtime regressions detected in tested scope.
