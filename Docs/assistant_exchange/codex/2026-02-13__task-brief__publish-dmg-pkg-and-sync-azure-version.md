# Task Brief: Publish DMG/PKG and Sync Azure Version in One Run

## Goal
- При получении от пользователя новых `DMG/PKG` файлов:
  - загрузить `DMG` в release tag `Update`
  - загрузить `PKG` в release tag `App`
  - параллельно синхронизировать версию на Azure

## Added Script
- `server/scripts/publish_assets_and_sync.sh`

## Behavior
- Inputs:
  - `--dmg /abs/path/Nexy.dmg` (optional)
  - `--pkg /abs/path/Nexy.pkg` (optional)
  - `--version X.Y.Z.W` (optional; default from `VERSION`)
  - `--repo OWNER/REPO` (optional; default `Seregawpn/Nexy_production`)
- Parallelism:
  - запускает `update_server_version.sh` в фоне
  - загружает assets в GitHub release (`Update`/`App`)
  - ждёт завершение sync версии
- Post-steps:
  - если есть DMG, обновляет remote manifest JSON (current + versioned)
  - валидирует `/updates/health` и `/updates/appcast.xml` на совпадение версии

## Expected Stable URLs
- DMG: `https://github.com/Seregawpn/Nexy_production/releases/download/Update/<file>.dmg`
- PKG: `https://github.com/Seregawpn/Nexy_production/releases/download/App/<file>.pkg`

