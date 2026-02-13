# Task Brief: Version Single-Source Follow-up Cleanup

## Goal
- Закрыть оставшиеся legacy fallback версии в рабочих server scripts.
- Убрать риск возврата к `1.0.0/1.0.1` при создании новых манифестов.

## Changes
- Updated `server/scripts/update_server_version.sh`:
  - fallback-манифест создается с `new_version/new_build`, не с `1.0.0`.

- Updated `server/scripts/sync_version_to_server.sh`:
  - fallback-манифест создается с `new_version/new_build`.

- Updated `server/scripts/update_version.py`:
  - удален hardcoded fallback `1.0.0` в remote manifest update snippet.

- Updated `server/scripts/sync_version_centralization.sh`:
  - проверка версии в remote `unified_config.py` больше не привязана к `1.0.1`.

- Updated `server/scripts/sync_manifest.sh`:
  - tag релиза теперь по умолчанию строится из `VERSION` (`v<version>`), если не задан `RELEASE_TAG`.
  - `MANIFEST_FILE` по умолчанию `manifest.json` (с override через env).

## Verification
- Shell syntax checks passed:
  - `update_server_version.sh`
  - `sync_version_to_server.sh`
  - `sync_version_centralization.sh`
  - `sync_manifest.sh`
- Python compile check passed:
  - `update_version.py`

