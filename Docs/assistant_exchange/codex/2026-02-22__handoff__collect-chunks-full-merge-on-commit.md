# Handoff: COLLECT chunks full merge before COMMIT generation

## What changed
- Centralized full-request merge in server gRPC owner-path (`COLLECT/COMMIT`).
- Server now merges all incoming collect chunks into one canonical text, instead of keeping only last chunk.
- COMMIT now always merges buffered COLLECT text with COMMIT prompt, then sends final merged text to workflow/LLM.

## Files
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/core/grpc_server.py`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/tests/test_grpc_phase_collect_commit.py`

## Behavioral impact
- Prevents loss of prior chunks when COMMIT prompt is short/stale.
- Supports both chunk formats:
  - snapshot chunks (growing full text),
  - delta chunks (text fragments).
- Preserves whitespace in merged prompt (lossless merge for speech text).

## Added diagnostics
- COMMIT merge log with lengths and chunk count:
  - `collect_chunks`, `collect_text_len`, `commit_prompt_len`, `final_prompt_len`.

## Verification
- `pytest -q tests/test_grpc_phase_collect_commit.py`
- Result: `5 passed`.

## Notes
- Existing anti-race path preserved (`chunk_seq` ordering + collect lock).
- No new ownership path introduced; merge remains centralized in `grpc_server.py`.
