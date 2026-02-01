# Task Brief: dev vs packaged permissions separation

## Goal
Ensure packaged app prompts for permissions while terminal/dev runs bypass and do not contaminate packaged app state.

## Changes
- Added app name override hooks (`NEXY_APP_NAME` / `NEXY_APP_DATA_SUFFIX`) in `integration/utils/resource_path.py` for data/log/cache dir isolation.
- When terminal bypass is enabled in `main.py`, set:
  - `NEXY_APP_NAME=Nexy-Dev`
  - `NEXY_APP_DATA_SUFFIX=Dev`
  - `APP_BUNDLE_ID=com.nexy.assistant.dev`

## Rationale
- Prevents dev/terminal runs from writing `permission_ledger.json` and first-run flags to the same directory used by packaged `.app`.

## Files
- `integration/utils/resource_path.py`
- `main.py`
