# Server Scripts (Canonical)

## Core owner scripts

- Version source sync:
```bash
python3 scripts/update_version.py X.Y.Z.W
```

- Publish client artifacts (Nexy_production):
```bash
python3 scripts/publish_assets_and_sync.py
python3 scripts/publish_assets_and_sync.py publish --channel beta
python3 scripts/publish_assets_and_sync.py promote --source beta --target stable
python3 scripts/publish_assets_and_sync.py --dry-run
```
Guards:
- canonical inbox path only: `server/release_inbox`
- canonical manifest owner only: `server/updates/manifests/manifest*.json`
- promote is idempotent for identical source/target artifact fingerprint

- Update runtime version on Azure VM:
```bash
bash scripts/update_server_version.sh X.Y.Z.W
```

- Remote manifest owner (locked):
```bash
bash scripts/update_manifest_remote_locked.sh [options]
bash scripts/update_manifest_remote_locked.sh --channel beta [options]
```

## Deprecated (blocked)

These scripts are intentionally disabled and must not be used:
- `scripts/deploy.sh`
- `scripts/sync_manifest.sh`
- `scripts/update_manifest_with_dmg.sh`
- `scripts/fix_version_mismatch.sh`
- `scripts/sync_version_centralization.sh`

Use only the core owner scripts listed above.
