# Server Scripts (Canonical)

Command context:
- This README assumes current directory is `server/server/`.
- If you run from workspace root, prepend paths with `server/server/` (for example: `python3 server/server/scripts/update_version.py X.Y.Z.W`).

## Core owner scripts

- Version source sync:
```bash
python3 scripts/update_version.py X.Y.Z.W
```

- Publish client artifacts (Nexy_production):
```bash
python3 scripts/publish_assets_and_sync.py                 # default publish -> beta
python3 scripts/publish_assets_and_sync.py publish --channel beta
python3 scripts/publish_assets_and_sync.py promote --source beta --target stable
python3 scripts/publish_assets_and_sync.py --dry-run
```
Guards:
- canonical inbox path only: `server/release_inbox/<channel>`
  - beta publish reads from: `server/release_inbox/beta`
  - stable publish (blocked) would read from: `server/release_inbox/stable`
- canonical manifest owner only: `server/updates/manifests/manifest*.json`
- direct publish to `stable` is blocked; production path is only `beta -> promote -> stable`
- promote is idempotent for identical source/target artifact fingerprint

- Update runtime version on Azure VM:
```bash
bash scripts/update_server_version.sh X.Y.Z.W
```

- One-VM fast runtime cutover (production ingress `:443`):
```bash
bash scripts/cutover_runtime_backend.sh --to staging
bash scripts/cutover_runtime_backend.sh --to prod
```
Guards:
- precheck target backend health before switch
- lock to prevent parallel cutover
- nginx test + reload
- auto rollback on failure

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
