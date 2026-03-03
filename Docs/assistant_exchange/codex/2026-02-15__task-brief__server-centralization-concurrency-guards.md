# Server centralization: init-path, inflight SoT, import path hardening

Date: 2026-02-15
Type: task-brief

## Done
- Switched `GrpcServiceManager` bootstrap to coordinator-first by default.
- Kept legacy bootstrap only behind explicit emergency env flag: `NEXY_FORCE_LEGACY_GRPC_INIT=true`.
- Moved in-flight session/hardware tracking ownership into `SessionRegistry` (`try_acquire_inflight`, `release_inflight`, inflight queries).
- Updated `StreamingWorkflowIntegration` to use `SessionRegistry` for atomic acquire/release and removed local duplicated inflight maps.
- Removed `sys.path` mutations from core/import-sensitive layers:
  - `grpc_server.py`
  - `grpc_service_integration.py`
- Added protobuf import compatibility without path hacks via `sys.modules.setdefault("streaming_pb2", streaming_pb2)`.
- Added race tests:
  - concurrent same `session_id` -> reject
  - concurrent same `hardware_id` when guard enabled -> reject
- Updated coordinator tests for new emergency-only legacy behavior.

## Files changed
- `server/modules/grpc_service/core/grpc_service_manager.py`
- `server/modules/session_management/core/session_registry.py`
- `server/integrations/workflow_integrations/streaming_workflow_integration.py`
- `server/modules/grpc_service/core/grpc_server.py`
- `server/integrations/service_integrations/grpc_service_integration.py`
- `server/tests/test_pr2_1_coordinator.py`
- `server/tests/test_streaming_workflow_concurrency_guards.py` (new)

## Verification
- `PYTHONPATH=server .venv/bin/pytest -q server/tests/test_pr2_1_coordinator.py server/tests/test_streaming_workflow_concurrency_guards.py`
  - result: 18 passed
- `PYTHONPATH=server .venv/bin/pytest -q server/tests/test_grpc_mcp_integration.py server/tests/test_streaming_workflow_mcp.py`
  - result: 11 passed

## Notes
- `use_module_coordinator` and `disable_module_coordinator` are now non-routing hints unless emergency override is explicitly enabled.
- Remaining config-doc alignment for inactive flags can be handled in a separate docs/cleanup pass.
