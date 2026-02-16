# Task Brief

## Context
User requested to finalize architecture alignment by centralizing logic contracts and adding safeguards against regressions.

## Scope
- Add contract-level tests for browser install voice flow and gRPC TTS readiness guard.
- Document owner-path and lifecycle contract in architecture docs.

## Changes

### 1) Tests added
File: `tests/test_browser_install_contracts.py`

Added 4 async tests:
1. `test_browser_install_started_tts_waits_for_welcome_completion`
   - Verifies install-start TTS is queued until welcome completion.
2. `test_browser_already_installed_tts_emits_when_welcome_done`
   - Verifies explicit "already installed" voice message when welcome gate is open.
3. `test_server_tts_skips_when_grpc_connection_unavailable`
   - Verifies `_play_server_tts` does not stream when gRPC remains disconnected (2 checks fail).
4. `test_server_tts_retries_connect_and_streams_on_second_attempt`
   - Verifies one retry path: first connect check fails, second succeeds, stream starts.

### 2) Architecture documentation updated
File: `Docs/ARCHITECTURE_OVERVIEW.md`

Added section `5.1) Browser Install Lifecycle Contract (owner-path)`:
- `BrowserUseModule` = state owner.
- `BrowserUseIntegration` = install UX/TTS owner.
- `WelcomeMessageIntegration` = welcome lifecycle owner.
- Startup ordering rule: welcome first, browser install voice second.
- Reliability rule: `GrpcClientIntegration._play_server_tts` must ensure connected transport before streaming.

## Verification
Command executed:
- `pytest -q tests/test_browser_install_contracts.py`

Result:
- `4 passed`.

## Architecture Gates
- Single Owner Gate: PASS (owners explicitly documented and tested)
- Zero Duplication Gate: PASS (no parallel UX owner path introduced)
- Anti-Race Gate: PASS (welcome gate + connect retry path covered)
- Flag Lifecycle Gate: PASS (no new flags introduced)
