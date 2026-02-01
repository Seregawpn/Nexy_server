# Contacts — Disable Settings Fallback

## Date
2026-01-27

## Change Summary
Contacts should be dialog-only. Removed Settings fallback for contacts to prevent prompt suppression.

## Files
- `config/unified_config.yaml`
- `modules/permissions/v2/orchestrator.py`

## Verification Plan
- Clean first-run → запуск .app → confirm Contacts prompt appears.
- Ensure no `SETTINGS_NAV Opened Settings: contacts` in logs.
