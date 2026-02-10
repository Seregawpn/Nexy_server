# Task Brief: cleanup remaining duplication/race/centralization paths

## Implemented
- Removed duplicate `restart_pending` writer in PermissionRestartIntegration.
  - `restart_pending` state is now documented as coordinator-owned single writer path.
- Removed direct state-manager fallback in processing timeout guard.
  - Timeout path now remains controller-only (no bypass of mode centralization).
- Removed dead `mode.changed` subscription and handler from UpdaterIntegration.
  - Updater now tracks mode only via `app.mode_changed`.
- Added single-flight guard for WhatsApp reset/restart tasks.
  - New `_schedule_reset_session_and_restart()` prevents parallel reset tasks.
- Removed duplicate `node_path` assignment in WhatsApp config overlay.
- Synced architecture doc for TTS contract:
  - local `say` fallback marked disabled;
  - canonical path is server TTS via `grpc.tts_request` -> `grpc.response.audio`.

## Files updated
- `integration/integrations/permission_restart_integration.py`
- `integration/integrations/mode_management_integration.py`
- `integration/integrations/updater_integration.py`
- `integration/integrations/whatsapp_integration.py`
- `Docs/ARCHITECTURE_OVERVIEW.md`

## Verification
- `python3 scripts/verify_no_direct_state_access.py` -> OK
- `python3 scripts/verify_feature_flags.py` -> OK
- `python3 scripts/verify_4_artifacts_invariant.py` -> OK
- `python3 scripts/verify_rule_coverage.py` -> OK
- `pytest -q ...` targeted suite -> `39 passed`
