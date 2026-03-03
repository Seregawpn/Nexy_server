# Handoff: Canonical deploy docs and rules sync

## Goal
Unify documentation/rules/settings for correct deploy and remote-server operations on new Azure account.

## Updated canonical docs
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`
- `Docs/REMOTE_SERVER_CONFIG.md`
- `Docs/CLIENT_CONNECTION_GUIDE.md`
- `Docs/CLIENT_QUICK_REFERENCE.md`
- `Docs/DOCUMENTATION_UPDATE_SUMMARY.md`

## Main synchronization points
1. Production target normalized to:
   - RG: `NexyNewRG`
   - VM: `NexyNew`
   - Host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
2. Canonical deploy command:
   - `bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W`
3. Canonical ops commands:
   - `bash server/scripts/quick_server_ops.sh check`
   - `bash server/scripts/quick_server_ops.sh monitor-once`
   - `bash server/scripts/quick_server_ops.sh monitor-start`
4. Monitoring immutability rule documented:
   - regular deploy must not alter monitoring artifacts;
   - deploy fails on monitor drift unless explicit `--allow-monitor-changes`.
5. Client connection docs corrected:
   - production `:443` requires TLS `secure_channel`;
   - `insecure_channel` marked non-canonical for production.

## Validation executed
- `python3 scripts/verify_docs_root_server_links.py` -> `[docs-gate] OK`
- `bash -n server/scripts/deploy_server_one_click.sh` -> OK
- `bash -n server/scripts/quick_server_ops.sh` -> OK
- `bash -n server/scripts/pull_remote_server_monitor_status.sh` -> OK

## Notes
- Historical documents may still mention older infra as archived context; canonical operation paths are now explicit in updated guides above.
