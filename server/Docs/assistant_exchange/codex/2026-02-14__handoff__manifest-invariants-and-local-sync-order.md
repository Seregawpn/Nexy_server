# Handoff: manifest invariants and local sync order

## Task
Harden current rules and local server workflow to prevent updater failures caused by manifest/appcast drift.

## Implemented
1. Added mandatory update-manifest invariants in rules:
   - `AGENTS.md`
   - `server/AGENTS.md`

2. Hardened release/update guide:
   - `Docs/RELEASE_AND_UPDATE_GUIDE.md`
   - explicit dual runtime manifest paths
   - mandatory post-publish sync and consistency gate
   - stale appcast troubleshooting section

3. Hardened publish script:
   - `server/scripts/publish_assets_and_sync.py`
   - remote artifact verification already present
   - now writes/syncs manifest files into both runtime paths:
     - `server/updates/manifests`
     - `updates/manifests`

4. Added dedicated sync guard script:
   - `server/scripts/sync_update_manifests.py`
   - validates: HTTPS URL, fixed `Update` tag URL, positive size, SHA256 format
   - syncs canonical+versioned manifests to both runtime paths
   - `--check` mode for CI/pre-deploy gate

5. Strengthened consistency validator:
   - `server/scripts/validate_updates.sh`
   - validates AppCast artifact URL policy (HTTPS + fixed Update tag)
   - validates local manifest URL/size/sha256
   - validates manifest parity between both local runtime paths
   - supports 4-part version format (`1.6.1.36`)

6. Deploy guard hookup:
   - `server/scripts/deploy_azure_guarded.sh`
   - runs `sync_update_manifests.py` on VM before restart (best-effort)

## Local order performed now
- Ran `python3 server/scripts/sync_update_manifests.py`
- Ran `python3 server/scripts/sync_update_manifests.py --check` -> OK
- Result: local manifest trees synchronized.

## Notes
- Current workspace had mixed path conventions; sync script now prevents stale appcast caused by path drift.
- `validate_updates.sh` remote endpoint checks may fail when endpoint is not reachable from current environment; local manifest checks still run.
