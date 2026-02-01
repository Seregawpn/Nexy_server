# Logging Path Fix (Nexy)

## Summary
- Updated logging path to a user-writable location and ensured `~` is expanded before creating file handlers.

## Changes
- Set `logging.file_path` to `~/Library/Logs/Nexy/nexy.log` in `config/unified_config.yaml`.
- Expanded `~` in `integration/utils/logging_setup.py` before `abspath`.

## Rationale
- App bundle launches cannot write to relative `logs/` path; using a stable user log directory avoids silent log loss.

## Verification
- Launch `/Applications/Nexy.app` and confirm `~/Library/Logs/Nexy/nexy.log` receives entries.
