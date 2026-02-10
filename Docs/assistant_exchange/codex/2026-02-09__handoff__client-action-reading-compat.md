# Handoff: Client action-reading compatibility without server changes

## Scope
- Only client-side changes (no server edits).
- Goal: read actions robustly and avoid duplicates/conflicts.

## Implemented
- Updated `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`.
- Added compatibility parser for legacy action payloads in `text_chunk`:
  - `__MCP__{...}`
  - fenced JSON payloads
  - plain JSON object payloads
- Kept single execution path: still publishes `grpc.response.action` only.
- Added dedup guard per stream/session:
  - If action already dispatched, ignore duplicates from `action_message` or legacy text.
- Prevented control payload leakage into TTS/text path:
  - legacy action text is not forwarded as `grpc.response.text`.
- Extended stream summary logs with `action_chunks` counter.

## Why this fixes user symptom
- If server intermittently sends legacy action in text instead of `action_message`, client now still dispatches the action.
- If both formats appear, only one action is dispatched (no duplicate execution).

## Validation run
- `python3 -m py_compile client/integration/integrations/grpc_client_integration.py` ✅
- `pytest` run blocked by local env/config path issues (`config/unified_config.yaml` resolution) ⚠️

## Notes
- Architecture preserved: no text-to-action executor path added; only input compatibility in reader.
