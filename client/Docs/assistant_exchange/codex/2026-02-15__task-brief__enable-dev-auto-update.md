# Task Brief: enable dev auto update

## Goal
Enable automatic update installation in the development updater profile.

## Changes
- Updated `/config/unified_config.yaml`:
  - `updater.development.auto_install: false -> true`

## Validation
- Loaded runtime updater config via `UpdaterManager`:
  - `enabled=True`
  - `check_on_startup=True`
  - `auto_install=True`
  - `manifest_url=https://nexy-server.canadacentral.cloudapp.azure.com/updates/appcast.xml`
  - `channel=fix`

## Notes
- This enables update attempts/install flow in dev profile.
- If logs still show `UpdaterIntegration disabled`, the running app is using a different runtime config (packaged resources), not this workspace file.
