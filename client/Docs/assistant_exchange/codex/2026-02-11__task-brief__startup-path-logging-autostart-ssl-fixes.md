# Task Brief: startup path logging, autostart dedup, updater SSLContext fix

Date: 2026-02-11
Assistant: Codex
Type: task-brief

## Context
User reported remaining startup log issues after previous cleanup:
- wrong log file path rendering with `.../client/~/Library/...`
- duplicate startup noise around tray/autostart
- updater SSLContext warning (`'str' object cannot be interpreted as an integer`)

## Changes

1. Fixed log path normalization in main entrypoint
- File: `main.py`
- Changed:
  - from `os.path.abspath(log_file)`
  - to `Path(log_file).expanduser().resolve()`
- Also fixed typo in boot log line:
  - `BOOT: tempr log file` -> `BOOT: temp log file`

2. Removed remaining duplicate tray init log
- File: `integration/integrations/tray_controller_integration.py`
- Removed second duplicate `tray.will_init` log line.

3. Reduced duplicate autostart status emissions at startup
- File: `integration/integrations/autostart_manager_integration.py`
- `start()` no longer performs immediate `_check_autostart_status()` (startup handler already checks).
- Monitoring loop now sleeps first, then checks status (prevents instant duplicate check on start).

4. Fixed updater SSLContext configuration type
- File: `modules/updater/net.py`
- Added `import ssl`.
- Changed `create_urllib3_context(cert_reqs='CERT_NONE')` to `create_urllib3_context(cert_reqs=ssl.CERT_NONE)`.

## Validation
- `pytest -q tests/test_welcome_startup_sequence.py tests/test_restart_pending_state_keys.py tests/test_event_ownership_contract.py tests/test_gateways.py`
  - Result: `27 passed`
- `python3 -m py_compile main.py integration/integrations/tray_controller_integration.py integration/integrations/autostart_manager_integration.py modules/updater/net.py`
  - Result: OK

## Expected runtime effect
- Log path prints as a valid absolute path in user log directory (without literal `~/` segment).
- One `tray.will_init` line (no duplicate).
- `autostart.status_checked` should not be emitted twice immediately at startup.
- Updater should not log SSLContext type warning anymore.
