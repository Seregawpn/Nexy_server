# Handoff: docs full alignment for update pipeline

## Goal
Bring documentation to full alignment with current update/deploy reality and anti-drift safeguards.

## Updated docs
- `Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - clarified dual runtime manifest paths
  - clarified versioning priority for synchronized manifests
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - added mandatory `Update Manifest Consistency Gate` section
  - commands: sync + check + validate before deploy
- `server/scripts/README.md`
  - replaced outdated process with canonical index/redirect
  - added anti-drift rules and canonical commands only
- `Docs/update_process_guide.md`
  - added mandatory consistency gate section

## Process now documented as mandatory
1. `python3 server/scripts/sync_update_manifests.py`
2. `python3 server/scripts/sync_update_manifests.py --check`
3. `bash server/scripts/validate_updates.sh nexy-server.canadacentral.cloudapp.azure.com 443`
4. Block deploy if any check fails.

## Why this prevents recurrence
- Prevents manifest path drift (`server/updates/...` vs `server/server/updates/...`).
- Prevents stale appcast URL/size due to unsynced manifests.
- Forces HTTPS + fixed `Update` tag URL policy in documented gate flow.
