# Server Audit: init-path, session SoT, import-path, race tests

Date: 2026-02-15
Type: analysis

## Scope
- gRPC init-path consistency
- Session state source-of-truth consistency
- sys.path usage in core server layers
- Concurrent/single-flight test coverage

## Findings (validated)
1. Dual init-path in `grpc_service_manager.py` exists:
   - coordinator path and legacy path are both active runtime branches.
2. Local inflight tracking in `streaming_workflow_integration.py` duplicates session/hardware activity tracking conceptually with `SessionRegistry`.
3. `sys.path` mutations exist in core files (`grpc_server.py`, `grpc_service_integration.py`).
4. No dedicated tests for concurrent same `session_id` / same `hardware_id` rejection in `server/tests`.

## Architectural fit
- Existing docs declare central control via `GrpcServiceManager -> ModuleCoordinator` and `SessionRegistry` as session state owner.
- Current state keeps transitional/legacy and local guard paths that increase semantic drift risk.

## Recommended primary direction
- Make coordinator path canonical (legacy behind explicit emergency flag only).
- Keep streaming single-flight as concurrency guard, but centralize active session ownership in `SessionRegistry` and remove duplicate lifecycle maps where possible.
- Replace `sys.path` hacks with package-safe imports.
- Add race-focused async tests for concurrent requests.

