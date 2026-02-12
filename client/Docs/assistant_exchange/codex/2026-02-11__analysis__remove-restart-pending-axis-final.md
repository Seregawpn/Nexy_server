# Task
Final cleanup: remove legacy `restart_pending` axis from runtime snapshot/gateway infrastructure.

# Diagnosis
`restart_pending` remained as compatibility-only field in `Snapshot` and gateway context even though runtime decisions no longer used it.

# Changes
1. Removed `restart_pending` from `Snapshot`:
   - `integration/core/selectors.py`
   - Deleted dataclass field, compatibility selector, and snapshot population.

2. Removed `restart_pending` from gateway decision context/log formatting:
   - `integration/core/gateways/base.py`
   - Deleted `DecisionCtx.restart_pending` and related log serialization.

3. Updated tests to new contract:
   - `tests/test_gateways.py`: snapshot factory no longer accepts `restart_pending`.
   - `tests/test_restart_pending_selector_gateway.py`: verifies snapshot has no `restart_pending` attribute.

# Verification
- `python3 -m py_compile` on touched files: OK
- `PYTHONPATH=. pytest -q` on targeted suites:
  - `tests/test_gateways.py`
  - `tests/test_restart_pending_selector_gateway.py`
  - `tests/test_autostart_repair_policy.py`
  - `tests/test_restart_pending_state_keys.py`
  - `tests/test_permissions_v2_ready_to_greet_guard.py`
  - `tests/test_centralization_regressions.py`
  - `tests/test_coordinator_critical_subscriptions.py`
- Result: **39 passed**

# Remaining mentions
- `modules/permissions/v2/types.py::Phase.RESTART_PENDING` remains intentionally (FSM phase, not runtime axis).
- A few test names/comments still include the word `restart_pending` for historical context only.
