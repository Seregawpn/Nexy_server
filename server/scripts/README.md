# Server Scripts (Canonical)

Канонические owner-скрипты:

- `python3 server/scripts/update_version.py X.Y.Z.W`
- `python3 server/scripts/publish_assets_and_sync.py`
- `bash server/scripts/update_server_version.sh X.Y.Z.W`

## Deprecated (blocked)

Следующие скрипты оставлены только как блокирующие заглушки, чтобы исключить конфликтные потоки:

- `server/scripts/deploy.sh`
- `server/scripts/sync_version_centralization.sh`
- `server/scripts/sync_manifest.sh`
- `server/scripts/update_manifest_with_dmg.sh`
- `server/scripts/fix_version_mismatch.sh`

Если нужен релиз, использовать только канонический flow выше.
