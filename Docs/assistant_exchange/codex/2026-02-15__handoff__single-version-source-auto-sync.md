# Handoff: Single Version Source Auto Sync

## Goal
Убрать ручные правки версии в разных местах и оставить один источник истины.

## Source of Truth
- `VERSION` (корень workspace)

## Implemented Owner
- `server/scripts/update_version.py`

## What Script Syncs
- `VERSION`
- `server/config.env.example` (`SERVER_VERSION`, `SERVER_BUILD`)
- `server/config/unified_config.yaml` (`default_version`, `default_build`, `server.version`, `server.build`)
- `server/config/unified_config.py` (fallback значение `SERVER_VERSION`)
- `server/updates/manifests/manifest.json` (`version`, `build`, `release_date`)
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (doc release marker)
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (doc release marker)
- `client/config/unified_config.yaml` + авто-синк client производных файлов через `client/config/auto_sync.py` (если client доступен)

## Docs Updated
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`

## Verified
- `python3 server/scripts/update_version.py --read`
- `python3 server/scripts/update_version.py 1.6.1.38 --check`
- Скрипт успешно синхронизировал drift до `1.6.1.38`.
