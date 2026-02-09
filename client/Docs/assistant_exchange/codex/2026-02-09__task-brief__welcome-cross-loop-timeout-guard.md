# Task Brief: Welcome cross-loop timeout guard

## Context
Startup logs showed welcome flow reaches gRPC diagnostics (`[GRPC_DIAG] Финальный результат...`) but never continues to:
- `TRACE [WELCOME_GEN] client.generate_welcome_audio returned`
- sending `playback.raw_audio`

This indicated a potential await stall on the cross-loop bridge (`run_coroutine_threadsafe` -> `wrap_future`) or a delayed completion path.

## Changes

### 1) modules/grpc_client/core/grpc_client.py
- In `generate_welcome_audio(...)`:
  - Added bridge timeout (`call_timeout + 5s`) for cross-loop path.
  - Added explicit diagnostic log for cross-loop call with loop ids.
  - On timeout, cancel the thread-safe future and raise timeout error.

### 2) modules/welcome_message/core/audio_generator.py
- Added hard timeout wrapper around `client.generate_welcome_audio(...)` using `asyncio.wait_for`.
- Added explicit timeout handling/log and return `None` on timeout so `WelcomePlayer` can use fallback path.

## Why
- Prevent indefinite hangs between gRPC completion and welcome integration continuation.
- Ensure welcome pipeline degrades predictably instead of stalling silently.

## Validation
- `python3 -m py_compile modules/grpc_client/core/grpc_client.py` ✅
- `python3 -m py_compile modules/welcome_message/core/audio_generator.py` ✅

## Expected logs after fix
- If success path:
  - `TRACE [WELCOME_GEN] client.generate_welcome_audio returned`
  - `TRACE [WELCOME_PLAYER] _play_server_audio() returned: success=True`
  - `playback.raw_audio` publish
- If bridge stall persists:
  - `❌ [WELCOME_BRIDGE] timeout waiting cross-loop result ...`
  - `❌ [WELCOME_AUDIO] Таймаут ожидания generate_welcome_audio ...`
  - local fallback path from WelcomePlayer should be attempted.
