# Server Release & Update Guide

**Status:** ✅ Active Strategy  
**Last Updated:** February 14, 2026

This document is the **Single Source of Truth** for the Nexy Server release and update process. It consolidates versioning rules, deployment steps, and troubleshooting procedures.

---

## 1. Versioning Architecture

The server determines its version from multiple sources. Understanding the priority order is critical for successful updates.

### ⚠️ Priority Order (Critical)

1.  **Environment Variables (`config.env`)** [HIGHEST PRIORITY]
    - Location: `/home/azureuser/voice-assistant/server/config.env` on Azure VM.
    - Variables: `SERVER_VERSION`, `SERVER_BUILD`.
    - **Effect**: If these are set, they **OVERRIDE** everything else.
    - **Action**: You **MUST** update these values during deployment.

2.  **Manifest File (`manifest.json`)**
    - Location: `server/updates/manifests/manifest.json`.
    - Usage: Used by the Update Provider to generate the `appcast.xml` for clients.
    - **Action**: Must be updated to match the release version.

3.  **Code File (`VERSION`)** [LOWEST PRIORITY]
    - Location: `VERSION` file in the project root.
    - Usage: Default fallback if `config.env` variables are missing.
    - **Action**: Should always be updated in the repo for consistency.

---

## 2. Release Process Checklist

### Phase 1: Local Preparation
1.  **Update Repository Version**:
    - Update `VERSION` file to `X.Y.Z.Build`.
    - Run `python3 server/scripts/update_version.py X.Y.Z.Build` (updates config examples).
    - Commit changes: `git commit -m "Release vX.Y.Z.Build"`.
2.  **Tag Release**:
    - `git tag vX.Y.Z.Build`
    - `git push origin vX.Y.Z.Build`

### Phase 2: Artifact Publication
1.  **Build Client**: Build the client application (`.dmg`).
2.  **GitHub Release**: Create a release for the tag and upload the `.dmg`.
3.  **Verify Direct Link**:
    - Ensure the download link is **HTTPS**.
    - Redirects are allowed, but the final destination must be HTTPS.
    - **Required**: `https://github.com/.../Nexy.dmg`

### Phase 3: Server Deployment (Azure)
This phase applies the update to the running server.

1.  **Connect to Server**:
    - Local: `az vm run-command invoke ...` or SSH.
2.  **Deploy Code**:
    - Fetch new tag/branch: `git fetch --all && git checkout vX.Y.Z.Build`.
    - Update dependencies: `pip install -r server/requirements.txt`.
3.  **Update Configuration (CRITICAL)**:
    - Update `server/config.env`:
      ```bash
      # MUST match new version
      SERVER_VERSION=X.Y.Z.Build
      SERVER_BUILD=X.Y.Z.Build
      ```
4.  **Update Manifest**:
    - Edit `server/updates/manifests/manifest.json`:
      - `version`: "X.Y.Z.Build"
      - `url`: "https://github.com/.../Nexy.dmg" (VALID HTTPS URL)
5.  **Restart Service**:
    - `sudo systemctl restart voice-assistant.service`

---

## 3. Verification

After restart, verify the upgrade was successful.

### A. Health Endpoint
Confirms the running server code knows its version.
```bash
curl -s https://nexy-server.canadacentral.cloudapp.azure.com/health | grep version
# Expected: "latest_version": "X.Y.Z.Build"
```

### B. Appcast (Update Feed)
Confirms the update is visible to clients.
```bash
curl -s https://nexy-server.canadacentral.cloudapp.azure.com/updates/appcast.xml
```
**Checklist:**
- [ ] `sparkle:version` matches new build.
- [ ] `sparkle:shortVersionString` matches new version.
- [ ] `url` is correct and starts with `https://`.

---

## 4. Troubleshooting Guide

| Issue | Root Cause | Fix |
| :--- | :--- | :--- |
| **Old Version in /health** | `config.env` still has old `SERVER_VERSION`. | Edit `config.env` on VM & restart. |
| **"HTTPS required" Error** | Manifest URL is `http://` or invalid. | Edit `manifest.json` with HTTPS URL & restart. |
| **Update Loop** | `SERVER_BUILD` is same/lower than client. | Increment `SERVER_BUILD` in `config.env`. |
| **Manifest Not Found** | Wrong path in `UpdateServiceConfig`. | Check `SERVER_ROOT` and paths in logs. |
