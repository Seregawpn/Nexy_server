# Task Brief — Playback silence owner + gRPC collect config centralization

Date: 2026-02-18
Assistant: Codex
Type: task-brief

## Scope
- Убрать нецентрализованный глобальный `silence` task в `SpeechPlaybackIntegration`.
- Централизовать collect-phase лимиты/TTL сервера в `WorkflowConfig` (убрать хардкод из `grpc_server.py`).

## Changes

### 1) Client: per-session finalize-on-silence owner
- File: `client/integration/integrations/speech_playback_integration.py`
- Replaced:
  - `self._silence_task` -> `self._silence_tasks: dict[str, asyncio.Task[Any]]`
- Added centralized helpers:
  - `_cancel_silence_finalize(session_id: Any | None = None)`
  - `_schedule_silence_finalize(session_id: Any, timeout: float = 3.0)`
- Updated call sites:
  - `_queue_session_audio` (grpc done -> schedule per session)
  - `_on_raw_audio` (raw clip -> schedule per session)
  - `_on_grpc_completed` (had audio -> schedule per session)
  - `_apply_cancel_state` (cancel per sid or all)
  - `stop()` (cancel all pending finalize tasks)
- Added finalize cleanup:
  - `finally` in `_finalize_on_silence` removes current task from `_silence_tasks`.

### 2) Server: collect-phase limits moved to unified config
- File: `server/server/config/unified_config.py`
- `WorkflowConfig` extended with:
  - `collect_ttl_sec: float = 90.0`
  - `collect_max_chunks: int = 256`
  - `collect_max_text_chars: int = 20000`
- `WorkflowConfig.from_env()` now reads:
  - `STREAM_COLLECT_TTL_SEC`
  - `STREAM_COLLECT_MAX_CHUNKS`
  - `STREAM_COLLECT_MAX_TEXT_CHARS`

- File: `server/server/modules/grpc_service/core/grpc_server.py`
- `NewStreamingServicer.__init__` now sources collect settings from `get_config().workflow` with safety bounds.

### 3) Tests update
- File: `client/tests/test_voice_audio_owner_guards.py`
- Updated assertion from `_silence_task` to `_silence_tasks[sid]` in no-audio->first-audio recovery test.

## Architecture Gates
- Single Owner Gate:
  - Playback finalize owner = `SpeechPlaybackIntegration` per-session task map.
  - Collect limits owner = `WorkflowConfig` (`unified_config`).
- Zero Duplication Gate:
  - Removed repeated ad-hoc cancel/recreate patterns of one global task.
  - Removed hardcoded collect limits path in gRPC servicer.
- Anti-Race Gate:
  - Per-session task scheduling prevents cross-session cancel collisions.
  - Explicit task cleanup (`finally`) prevents stale references.
- Flag Lifecycle Gate:
  - New env keys are runtime-consumed in `WorkflowConfig.from_env()` and read in `grpc_server`.

## Validation
- `pytest -q tests/test_voice_audio_owner_guards.py tests/test_grpc_client_interim_commit_gate.py` (client): 14 passed
- `pytest -q server/tests/test_grpc_collect_commit_flow.py` (server): 5 passed
- `python3 -m py_compile ...` for touched files: OK

## Expected Effect
- Снижение риска stuck-in-PROCESSING из-за race глобального silence-task между сессиями.
- Единый источник истины для collect-phase лимитов/TTL без серверного хардкода.
