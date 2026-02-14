# Activate updater in development environment

## What changed
- Enabled updater in `development` profile in:
  - `config/unified_config.yaml`

## Updated keys
- `updater.development.enabled: true`
- `updater.development.auto_check: true`
- `updater.development.check_on_startup: true`
- `updater.development.auto_install: true`

## Why
- Runtime logs show app running with `env=development`, while updater was disabled in that profile.
- This prevented update checks in sessions where environment resolves to development.

## Expected effect
- On next app start, `UpdaterIntegration` should no longer log "Пропускаю запуск ... отключен" for development runs.
- Startup update check will run automatically.
