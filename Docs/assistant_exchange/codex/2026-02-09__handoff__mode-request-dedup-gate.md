# Handoff: mode.request dedup gate

Date: 2026-02-09  
Type: handoff  
Assistant: codex

## Change
- Added centralized short-window dedup for `mode.request` in:
  - `client/integration/integrations/mode_management_integration.py`

## Details
- New fields:
  - `_mode_request_dedup_window_sec = 0.5`
  - `_last_mode_request_ts: dict[(target_mode, session_id), ts]`
- In `_on_mode_request`:
  - normalize key `(target_mode, session_id or "__none__")`
  - skip repeated requests inside dedup window
  - lightweight stale-key cleanup to bound map size

## Why
- Prevent near-simultaneous duplicated `mode.request` from multiple sources from triggering repeated mode handling paths.
- Keep mode transition ownership centralized in `ModeManagementIntegration`.

## Validation
- `py_compile`: OK
- Targeted regression suite: `17 passed`
