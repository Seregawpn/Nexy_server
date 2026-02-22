# Analysis: client/server collect-commit trace for early-send symptom

## Scope
- Investigated client-side dev logs and server-side local logging entrypoints.
- Correlated provided runtime logs with collect/commit protocol semantics.

## Key findings
1. In provided server trace, LLM starts only after `REQUEST_PHASE_COMMIT`.
2. `REQUEST_PHASE_COLLECT` chunks are acknowledged (`collect_ack`) before commit.
3. Server merge logic currently prefers COMMIT prompt whenever non-empty:
   - `grpc_server.py::_consume_collect_for_commit`
   - buffered collect text is used only when commit prompt is empty.
4. This creates a truncation risk when commit carries short/stale text while collect had fuller text.

## Architecture owner-paths
- Client gate owner: `client/integration/integrations/grpc_client_integration.py`
  - commit allowed only after terminal STT + `voice.recording_stop`.
- Server merge owner: `server/server/modules/grpc_service/core/grpc_server.py`
  - `_handle_collect_phase`, `_consume_collect_for_commit`.

## Log locations
- Client dev logs:
  - `~/Library/Logs/Nexy/nexy-dev.log`
  - `~/Library/Logs/Nexy/nexy.log`
  - early bootstrap fallback: `/tmp/nexy_debug.log`
- Server local logs:
  - by default structured logger writes to stdout (console); persist with shell redirection.

## Practical command set
```bash
# Client
rg -n "PTT_STATE|voice\.recording_stop|Defer commit send|REQUEST_PHASE_COMMIT|collect send" ~/Library/Logs/Nexy/nexy-dev.log

# Server (if started in terminal with tee)
cd server/server
python main.py 2>&1 | tee server_runtime.log
rg -n "collect_ack|REQUEST_PHASE_COMMIT|Prompt для обработки|Начало LLM обработки" server_runtime.log
```

## Recommended next fix
- Server-side merge hardening in `_consume_collect_for_commit`:
  - avoid unconditional preference of non-empty commit prompt;
  - choose canonical merged text by recency/length policy and log merge metrics.
- Add regression test for: `collect(full) + commit(short)`.
