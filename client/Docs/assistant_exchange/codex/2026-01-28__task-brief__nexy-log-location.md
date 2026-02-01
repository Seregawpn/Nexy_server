# Task Brief: nexy log location

## Goal
Point user to Nexy app log location and request log snippet.

## Findings
- unified_config.yaml sets log path to `~/Library/Logs/Nexy/nexy.log`.
- fallback path in main.py is `/tmp/nexy_debug.log` if config load fails.

## Next Step
- User should paste the log start or share the file path.
