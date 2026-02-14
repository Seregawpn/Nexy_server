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

### 0.1 GitHub Routing Guard (Mandatory)
- Server repository only: all server `git push` and server version `git tag vX.Y.Z.BUILD` go to `Seregawpn/Nexy_server`.
- Production artifacts only: all binary release publication (`Nexy.dmg`/`Nexy.pkg`) goes to `Seregawpn/Nexy_production`.
- Never create GitHub Release in `Seregawpn/Nexy_server`.
- Before any publish step, verify remotes:
  ```bash
  git remote -v
  ```
  Expected:
  - server code remote points to `https://github.com/Seregawpn/Nexy_server.git`
  - artifact release target remains `Seregawpn/Nexy_production`

---

## 1. Release Infrastructure Rules (Golden Rules)

### 1.1 Critical Infrastructure
- `release_inbox` MUST exist at repo root.
- Core automation script: `server/scripts/publish_assets_and_sync.py`.
- Manifest runtime paths (must stay synchronized):
  - `server/updates/manifests/manifest.json`
  - `server/server/updates/manifests/manifest.json`

### 1.2 Repository Separation
- Code Repo (source + deploy): `Seregawpn/Nexy_server`.
- Release Repo (binary assets): `Seregawpn/Nexy_production`.
- Never upload artifacts to the code repo release page.
- Never create GitHub Release in `Seregawpn/Nexy_server`.

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
2. Manifest files (runtime-synchronized pair):
   - `server/updates/manifests/manifest.json`
   - `server/server/updates/manifests/manifest.json`
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
   git push server_repo vX.Y.Z.Build
   ```

### Phase 1.1: DB Durability Gate (Mandatory Before Publish/Deploy)

1. Create pre-release backup:
   ```bash
   ./server/scripts/db_backup.sh
   ```
2. Ensure restore drill is recent (<= 7 days). If uncertain, run:
   ```bash
   ./server/scripts/db_restore_drill.sh
   ```
3. If any restore was performed during validation, re-apply DB hardening:
   ```bash
   ./server/scripts/harden_database_protection.sh
   ```
4. Canon for DB operations:
   - `server/Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md`
   - `server/Docs/DATABASE_SETUP_GUIDE.md`

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
   - `Verifying uploaded artifact from release URL...`
   - `Remote size: ... bytes`
   - `Remote SHA256: ...`
   - `Manifest updated at .../server/updates/manifests/manifest.json`
   - `Manifest changes pushed to remote`
   - `RELEASE COMPLETE`
   - In `--dry-run` mode, `Manifest updated at ...` and `Manifest changes pushed to remote` are not expected.

4.1 Update-only Integrity Rule (Mandatory):
- For update publication (without server code release), manifest values must be derived from the uploaded artifact URL, not only local file stats.
- Publisher flow is fixed:
  1) upload artifact to `Nexy_production`,
  2) download artifact from release URL,
  3) compute factual `size` and `sha256`,
  4) write these values to `server/updates/manifests/manifest.json`.
- If local and remote metadata differ, script must abort and not push manifest.
- After publish, run manifest sync to prevent runtime path drift:
  ```bash
  python3 server/scripts/sync_update_manifests.py
  ```

5. Verify publication:
   - `https://github.com/Seregawpn/Nexy_production/releases/tag/Update`
   - `https://github.com/Seregawpn/Nexy_production/releases/tag/App`
   - DMG direct URL is reachable:
     `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`

6. Verify manifest in code repo (`Seregawpn/Nexy_server`):
   - Both runtime paths contain synchronized files:
     - `server/updates/manifests/manifest.json`
     - `server/server/updates/manifests/manifest.json`
     - `server/updates/manifests/manifest_<version>.json`
     - `server/server/updates/manifests/manifest_<version>.json`
   - Files contain:
     - correct `version` / `build`
     - updated `artifact.url`
     - updated `artifact.size`
     - updated `artifact.sha256`

7. Run consistency gate (mandatory):
   ```bash
   bash server/scripts/validate_updates.sh nexy-server.canadacentral.cloudapp.azure.com 443
   ```
   Gate must pass before deploy.

### Phase 3: Server Deployment (Azure)

Recommended (single-command guarded deploy):

```bash
bash server/scripts/deploy_azure_guarded.sh vX.Y.Z.Build
```

Manual fallback:

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
    . venv/bin/activate
    if [ -f server/server/requirements.txt ]; then
      REQ_FILE=server/server/requirements.txt
    elif [ -f server/requirements.txt ]; then
      REQ_FILE=server/requirements.txt
    else
      REQ_FILE=requirements.txt
    fi
    pip install --upgrade -r $REQ_FILE
    if [ -f server/server/scripts/update_server_version.sh ]; then
      UPDATE_SCRIPT=server/server/scripts/update_server_version.sh
    else
      UPDATE_SCRIPT=server/scripts/update_server_version.sh
    fi
    chmod +x $UPDATE_SCRIPT
    VERSION=\${TAG_NAME#v}
    $UPDATE_SCRIPT \$VERSION || true
    if [ -f server/server/config.env ]; then
      sed -i \"s/^SERVER_VERSION=.*/SERVER_VERSION=\$VERSION/\" server/server/config.env || true
      sed -i \"s/^SERVER_BUILD=.*/SERVER_BUILD=\$VERSION/\" server/server/config.env || true
    fi
    if [ -f server/config.env ]; then
      sed -i \"s/^SERVER_VERSION=.*/SERVER_VERSION=\$VERSION/\" server/config.env || true
      sed -i \"s/^SERVER_BUILD=.*/SERVER_BUILD=\$VERSION/\" server/config.env || true
    fi
    sudo systemctl restart voice-assistant.service
    sleep 10
    sudo systemctl is-active voice-assistant.service
    curl -s http://127.0.0.1:8080/health
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

### 4.6 Azure run-command conflict
Symptom:
- `Run command extension execution is in progress`.

Fix:
1. Wait for previous command to finish.
2. Retry the same `az vm run-command invoke` once.

### 4.7 Gemini key invalid/expired
Symptom:
- `API_KEY_INVALID` / `API key expired`.
- `TextProcessor` initialization fails.

Fix:
1. Update `GEMINI_API_KEY` in VM config files:
   - `server/config.env`
   - `server/server/config.env`
2. Restart service:
   ```bash
   sudo systemctl restart voice-assistant.service
   ```

### 4.8 config.env parse crash
Symptom:
- `ValueError: illegal environment variable name` from `unified_config.py`.

Fix:
1. Ensure config parser uses `split('=', 1)` (not `rsplit`).
2. Restart service and verify `/health`.

### 4.9 AppCast serves stale artifact URL/version
Symptom:
- `/updates/appcast.xml` returns old artifact URL or outdated size.
- Client update fails with `HTTP 404` or size mismatch.

Fix:
1. Sync runtime manifests:
   ```bash
   python3 server/scripts/sync_update_manifests.py
   ```
2. Re-check gate:
   ```bash
   bash server/scripts/validate_updates.sh nexy-server.canadacentral.cloudapp.azure.com 443
   ```
3. Restart update service (or whole server service) and verify appcast again.

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
6. Pre-release DB backup was created successfully.
7. Last restore drill is not older than 7 days.
