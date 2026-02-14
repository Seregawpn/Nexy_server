# Server Release & Update Guide

**Status:** Active Rulebook  
**Last Updated:** February 14, 2026

This document is the Single Source of Truth for Nexy release publication and update synchronization.

---

## 0. Two Pipelines (Mandatory)

- Pipeline A (Code + Deploy): `Seregawpn/Nexy_server`
  - Purpose: store server code and deploy to Azure VM.
- Pipeline B (Client Artifacts): `Seregawpn/Nexy_production/releases`
  - Purpose: publish `Nexy.dmg`/`Nexy.pkg` for client update channel.

These pipelines have different owners and must not be mixed.

---

## 1. Release Infrastructure Rules (Golden Rules)

### 1.1 Critical Infrastructure
- `release_inbox` MUST exist at repo root.
- Core automation script: `server/scripts/publish_assets_and_sync.py`.
- Manifest path: `server/updates/manifests/manifest.json`.

### 1.2 Repository Separation
- Code Repo (source + deploy): `Seregawpn/Nexy_server`.
- Release Repo (binary assets): `Seregawpn/Nexy_production`.
- Never upload artifacts to the code repo release page.

### 1.3 Fixed Production Tags
- `Nexy.dmg` -> tag `Update`.
- `Nexy.pkg` -> tag `App`.
- Do not create version-specific release tags for production binary delivery.

---

## 2. Versioning Architecture

### Priority Order (Critical)
1. Environment Variables in VM `config.env` (highest):
   - `SERVER_VERSION`
   - `SERVER_BUILD`
2. Manifest file:
   - `server/updates/manifests/manifest.json`
3. Repo file `VERSION` (fallback only).

If `SERVER_VERSION` / `SERVER_BUILD` on VM are stale, `/health` can show old version even after release publication.

---

## 3. Release Process Checklist

### Phase 1: Local Preparation
1. Update `VERSION` to `X.Y.Z.Build`.
2. Run:
   ```bash
   python3 server/scripts/update_version.py X.Y.Z.Build
   ```
3. Commit and tag:
   ```bash
   git commit -m "Release vX.Y.Z.Build"
   git tag vX.Y.Z.Build
   git push origin vX.Y.Z.Build
   ```

### Phase 2: Artifact Publication & Sync (Detailed)

1. Build artifacts:
   - Required: `Nexy.dmg`
   - Optional (if part of release): `Nexy.pkg`

2. Pre-check infrastructure:
   ```bash
   test -d release_inbox && echo "OK: release_inbox exists" || echo "MISSING: release_inbox"
   ls -la release_inbox
   ```
   Expected:
   - `release_inbox` directory exists.
   - It contains `Nexy.dmg` (and optionally `Nexy.pkg`).

3. Place artifacts into `release_inbox` (repo root).

4. Run publisher script from repo root:
   ```bash
   python3 server/scripts/publish_assets_and_sync.py
   ```
   Expected log markers:
   - `Current Version: ...`
   - `Target Repo: Seregawpn/Nexy_production`
   - `Uploaded. URL: https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`
   - `Manifest updated at .../server/updates/manifests/manifest.json`
   - `Manifest changes pushed to remote`
   - `RELEASE COMPLETE`
   - In `--dry-run` mode, `Manifest updated at ...` and `Manifest changes pushed to remote` are not expected.

5. Verify publication:
   - `https://github.com/Seregawpn/Nexy_production/releases/tag/Update`
   - `https://github.com/Seregawpn/Nexy_production/releases/tag/App`
   - DMG direct URL is reachable:
     `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`

6. Verify manifest in code repo (`Seregawpn/Nexy_server`):
   - `server/updates/manifests/manifest.json` contains:
     - correct `version` / `build`
     - updated `artifact.url`
     - updated `artifact.size`
     - updated `artifact.sha256`

### Phase 3: Server Deployment (Azure)

```bash
# Replace with actual release tag, e.g. vX.Y.Z.Build
TAG_NAME="vX.Y.Z.Build"

az vm run-command invoke \
  --resource-group "NetworkWatcherRG" \
  --name "Nexy" \
  --command-id RunShellScript \
  --scripts "
    set -e
    export HOME=/home/azureuser
    cd /home/azureuser/voice-assistant
    git config --global --add safe.directory /home/azureuser/voice-assistant
    git fetch --all --tags
    git checkout -f $TAG_NAME
    source venv/bin/activate
    pip install --upgrade -r server/requirements.txt
    chmod +x server/scripts/update_server_version.sh
    VERSION=\${TAG_NAME#v}
    ./server/scripts/update_server_version.sh \$VERSION
  "
```

---

## 4. Troubleshooting & Maintenance

### 4.1 Inbox not found
Symptom:
- Script fails with `Inbox directory not found`.

Fix:
```bash
mkdir -p release_inbox
ls -la release_inbox
```
Then place artifacts again and rerun script.

### 4.2 Script not found
Symptom:
- `python3: can't open file ... publish_assets_and_sync.py`.

Fix:
- Correct command from repo root:
  ```bash
  python3 server/scripts/publish_assets_and_sync.py
  ```
- Incorrect (do not use):
  ```bash
  python3 server/server/scripts/publish_assets_and_sync.py
  ```

### 4.3 GH CLI error
Symptom examples:
- `gh: command not found`
- `authentication required`
- `HTTP 401/403` on upload.

Fix:
```bash
gh --version
gh auth status
gh auth login
```
After successful auth, rerun publication script.

### 4.4 Wrong target repository
Symptom:
- Assets published to unexpected repo or URL.

Fix:
1. Open `server/scripts/publish_assets_and_sync.py`.
2. Verify:
   - `TARGET_REPO = "Seregawpn/Nexy_production"`
   - `ARTIFACT_MAPPING["Nexy.dmg"]["tag"] == "Update"`
   - `ARTIFACT_MAPPING["Nexy.pkg"]["tag"] == "App"`
3. Re-run publication.

### 4.5 Manifest pushed to wrong code repo
Symptom:
- Script completed, but manifest commit appeared in wrong GitHub repository.

Fix:
1. Check current git remote before running publication:
   ```bash
   git remote -v
   ```
2. Confirm `origin` points to `Seregawpn/Nexy_server`.
3. If not, switch remote and re-run publication.

---

## 5. Search / Logs (Поиск)

- Build artifacts:
  - `release_inbox/`
- Release manifest:
  - `server/updates/manifests/manifest.json`
- Script runtime logs:
  - stdout/stderr of:
    `python3 server/scripts/publish_assets_and_sync.py`
- Remote verification:
  - `https://github.com/Seregawpn/Nexy_production/releases/tag/Update`
  - `https://github.com/Seregawpn/Nexy_production/releases/tag/App`

---

## 6. Final Verification Checklist

1. `release_inbox` exists and contains expected artifacts.
2. Script completed with `RELEASE COMPLETE`.
3. DMG/PKG visible in `Seregawpn/Nexy_production` fixed tags.
4. `manifest.json` updated and pushed in `Seregawpn/Nexy_server`.
5. Post-deploy `/health` and appcast show new version/build.
