# Client-Server Flow Analysis (Contracts, Duplicates, Races, Centralization)

Date: 2026-02-11
Assistant: codex
Type: analysis

## Scope
- Reviewed runtime contracts and tests around:
  - gRPC response mapping and cancel routing
  - mode request dedup/session guard behavior
  - signal emission dedup/suppression behavior
  - MCP action response type contract
- Verified with full test suite.

## Pre-Change Gate Notes
- Read in current workspace (`/Users/sergiyzasorin/Fix_new/client`):
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FEATURE_FLAGS.md`
- Assumption: references to `client/Docs/*` in process rules map to `Docs/*` in this workspace layout (no `client/Docs/*` subtree exists from this cwd).
- Source of Truth for flow ownership:
  - mode transitions: `ModeManagementIntegration` + `ApplicationStateManager`
  - cancel orchestration: `InterruptManagementIntegration` publishes intent; playback side effects owned by playback integration path
  - gRPC transport contract mapping: `GrpcClientIntegration`

## Findings (before fixes)
1. Duplicate cancel trigger path in action execution integration (`interrupt.request` and `keyboard.short_press` both mapped to cancel).
2. Loose/legacy action extraction from `text_chunk` in gRPC response mapping (contract drift risk against explicit `action_message`).
3. Non-deterministic event ordering due to EventBus fast-path for selected events.
4. Test-contract drift after strict MCP `TextContent` validation and strict mode payload handling.
5. Script-like async files collected by pytest as tests, causing collection/runtime errors.

## Changes Applied
- Runtime hardening:
  - `integration/integrations/grpc_client_integration.py`
    - removed legacy action extraction from `text_chunk`
    - `grpc.request_cancel` requires `session_id`
  - `integration/integrations/action_execution_integration.py`
    - removed duplicate cancel trigger via `keyboard.short_press`
  - `integration/integrations/interrupt_management_integration.py`
    - fixed app-state payload access via `event.data`
  - `integration/core/event_bus.py`
    - disabled fast-path list to enforce deterministic ordering
- Tests:
  - added `tests/test_client_server_flow_contracts.py` (3 regression tests)
  - updated:
    - `modules/mcp_action/tests/test_executor.py` to use `mcp.types.TextContent`
    - `tests/test_mode_management_mode_request_dedup.py` for current mode contract
    - `tests/test_signal_integration_cancel_done_suppression.py` for current mode payload contract
  - marked manual script files as skipped in pytest:
    - `test_first_run_centralization.py`
    - `test_messages_real.py`
    - `tests/test_token_reporting.py`

## Duplication/Race/Centralization Status
- Duplicate cancel path: removed (single cancel intent path remains).
- Race risk (ordering): reduced by removing EventBus fast-path bypass.
- Contract ambiguity in gRPC action extraction: removed (`action_message` only).
- Source of Truth preserved:
  - mode changes through mode-management/state-manager contract
  - cancel orchestration via dedicated integration path
- New feature flags/state: none introduced.

## Verification
- Targeted subset: pass
  - `18 passed, 4 skipped`
- Full suite: pass
  - `242 passed, 16 skipped, 4 warnings`

## Residual Risks
- Pytest warnings remain (unknown `integration` marker, one async mock warning) but do not fail suite.
- Manual scripts retained in repo; now explicitly excluded from automated suite.

## Outcome
- Client-server data transfer/processing contracts are aligned to explicit owners.
- Duplicate and ambiguous paths removed.
- Determinism and anti-race behavior improved without introducing parallel state sources.
