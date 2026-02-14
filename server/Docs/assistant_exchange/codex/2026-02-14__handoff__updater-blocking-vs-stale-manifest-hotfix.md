# Handoff: updater blocking vs stale manifest hotfix

## What user reported
Client still shows updater problems and asks whether blocking is client-side and whether it can be removed.

## Findings
1. Client-side blocking exists in `client/modules/updater/net.py`:
   - non-HTTPS artifact URL is rejected by policy guard (`_is_artifact_url_allowed`).
2. Fresh runtime failures on `2026-02-14` were mostly not HTTPS-policy, but stale appcast URL with 404:
   - appcast pointed to `.../releases/download/v1.6.1.34/Nexy.dmg`.
3. Azure runtime used manifest directory under `server/server/updates/manifests`.
   - stale `manifest_1.6.1.34.json` caused old URL/size in appcast.

## Code changes (repo)
- `server/modules/update/providers/manifest_provider.py`
  - prefer canonical `manifest.json` in `get_latest_manifest()`;
  - include canonical manifest in `get_all_manifests()`;
  - normalize 4-part version sorting;
  - allow string build in `validate_manifest()`.
- `server/modules/update/providers/update_server_provider.py`
  - appcast now uses manifest as source of truth for version/build (fallback only if fields missing).
- `server/scripts/publish_assets_and_sync.py`
  - now writes both `manifest.json` and `manifest_<version>.json`;
  - git-add includes both files.
- `Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - manifest verification updated to check both canonical + versioned files.

## Azure hotfix applied
- Updated active runtime manifests in:
  - `/home/azureuser/voice-assistant/server/server/updates/manifests/manifest.json`
  - `/home/azureuser/voice-assistant/server/server/updates/manifests/manifest_1.6.1.36.json`
- Set artifact URL/size/sha256 to current Update artifact.
- Restarted `voice-assistant.service`.

## Post-hotfix verification
- `systemctl is-active voice-assistant.service` -> `active`
- `/updates/appcast.xml` now returns:
  - `url="https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg"`
  - `length="315718837"`
  - `sparkle:shortVersionString="1.6.1.36"`

## Security policy decision
- Keep HTTPS guard enabled in production.
- Optional dev-only relaxation remains possible via `allow_insecure_artifact_url`, but must not be enabled for production feeds.
