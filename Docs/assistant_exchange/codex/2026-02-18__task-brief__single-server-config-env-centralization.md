# Task Brief — Single server config.env centralization

Date: 2026-02-18
Assistant: Codex
Type: task-brief

## Goal
Убрать путаницу от двух server config.env и оставить один Source of Truth.

## Changes

1) Unified config loader centralized
- File: `server/server/config/unified_config.py`
- Changed env load path to only: `server/config.env`
- Removed implicit internal path usage (`server/server/config.env`)
- Added warning if unified path missing.

2) Main startup loader centralized
- File: `server/server/main.py`
- Removed primary/fallback dual-path logic.
- Now loads only `server/config.env`.
- Added warning if file missing.

3) Duplicate config removed
- Deleted file: `server/server/config.env`

## Verification
- `python3 -m py_compile server/server/config/unified_config.py server/server/main.py` -> OK
- `pytest -q server/server/tests/test_config_validation.py server/server/tests/test_config_drift.py` -> 9 passed
- Runtime check:
  - `subscription.enabled=True`
  - `gemini_api_key_fallback` present in loaded config

## Architecture gates
- Single Owner: env source = `server/config.env`
- Zero Duplication: removed duplicate `server/server/config.env`
- Anti-Race: no parallel env-source branch at startup
- Flag Lifecycle: existing flags continue to resolve from one file
