# Server Update Process & Requirements

This document outlines the strict requirements and process for deploying updates to the Nexy server to ensure consistent versioning and successful client updates.

## 1. Versioning Source of Truth

The server relies on multiple sources for version information. It is critical that **ALL** sources are synchronized.

### Priority Order (Highest to Lowest)
1.  **Environment Variables (`config.env`)**: `SERVER_VERSION` and `SERVER_BUILD` in `/home/azureuser/voice-assistant/server/config.env` override everything.
2.  **Manifest File**: `updates/manifests/manifest.json`.
3.  **Code File**: `VERSION` file in the repository root.

> [!IMPORTANT]
> **Common Failure Mode**: Updating the `VERSION` file in git but failing to update `config.env` on the server will cause the server to report the **OLD** version, blocking client updates.

## 2. Deployment Checklist

Before announcing a release, ensure the following steps are completed:

### A. Local Preparation
1.  **Update Repository Version**:
    - Update `server/VERSION` file.
    - Commit with message: `Update server to vX.Y.Z.Build`.
2.  **Git Tag**:
    - Create a git tag matching the version (e.g., `v1.6.1.35`).
    - Push the tag to origin.

### B. Artifact Publication (GitHub Releases)
1.  **Upload Artifact**: Upload the client `.dmg` (or other artifacts) to the GitHub Release.
2.  **HTTPS URL**: Ensure the download URL is **HTTPS**.
    - **Valid**: `https://github.com/.../Nexy.dmg`
    - **Invalid**: `http://...`, IP addresses, or redirects to non-secure endpoints.

### C. Server Deployment (Azure)
1.  **Deploy Code**: Pull the latest code/tag to `/home/azureuser/voice-assistant`.
2.  **Update Server Config (CRITICAL)**:
    - Edit `server/config.env` on the VM.
    - Set `SERVER_VERSION=X.Y.Z.Build`.
    - Set `SERVER_BUILD=X.Y.Z.Build`.
3.  **Update Manifest**:
    - Ensure `updates/manifests/manifest.json` reflects the new version and the correct HTTPS artifact URL.
4.  **Restart Service**:
    - `sudo systemctl restart voice-assistant.service`

## 3. Verification Steps

After deployment, verify the update server status **before** notifying clients.

### Check Health Endpoint
Returns the active server version.
```bash
curl -s https://nexy-server.canadacentral.cloudapp.azure.com/health | grep version
# Expected: "latest_version": "1.6.1.35"
```

### Check Appcast (Sparkle Feed)
Returns the XML used by the client updater.
```bash
curl -s https://nexy-server.canadacentral.cloudapp.azure.com/updates/appcast.xml
```
**Verify:**
- `sparkle:version` matches the new build number.
- `sparkle:shortVersionString` matches the new version string.
- `url` is the correct HTTPS link to the artifact.

## 4. Troubleshooting

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| Client sees old version | `config.env` has old `SERVER_VERSION` | Update `config.env` on VM & restart service. |
| Client gets "HTTPS required" error | Artifact URL in manifest/appcast is HTTP | Update `manifest.json` with HTTPS URL & restart service. |
| Update loop (keeps re-downloading) | `SERVER_BUILD` < Client Build | Ensure `SERVER_BUILD` is incremented. |
