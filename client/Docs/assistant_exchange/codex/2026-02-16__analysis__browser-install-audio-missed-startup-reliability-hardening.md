# Analysis

## User issue
User repeatedly does not hear browser-install completion audio message despite Chromium being installed.

## Confirmed signals
- Chromium folder appears (`chromium-1208`) but `browser_install_pending.flag` remained present in at least one cycle.
- This indicates install-start happened, but completion-audio delivery was not reliably observed by user.

## Root cause hypothesis (runtime)
Two startup timing windows could still drop/skip perceived audio:
1. `grpc.tts_request` published before subscriber readiness (early startup race).
2. gRPC transport not yet connected when server TTS starts; short retry window could miss startup connect readiness.

## Hardening changes applied

1) `integration/integrations/browser_use_integration.py`
- `_publish_tts(...)` now waits for `grpc.tts_request` subscriber availability (up to ~3s) before publish.
- Prevents one-shot startup install messages from being dropped by early publish race.

2) `integration/integrations/grpc_client_integration.py`
- `_play_server_tts(...)` connection retry window expanded:
  - before: 1 retry after 0.5s
  - now: up to 8 retries with 1.0s delay (9 checks total including first)
- Reduces startup delivery loss when gRPC connect is slightly delayed.

## Validation
- `python3 -m py_compile integration/integrations/browser_use_integration.py integration/integrations/grpc_client_integration.py` -> OK
- `pytest -q tests/test_browser_install_contracts.py` -> 4 passed

## Expected result
Install completion voice message should be reliably delivered after startup even under slow connect/subscriber timing.
