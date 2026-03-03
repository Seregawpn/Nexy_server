# Handoff: Deploy v1.6.1.42 to remote server

Date: 2026-02-18
Assistant: codex
Type: handoff

## Deployment target
- Azure VM: `Nexy`
- Resource group: `NETWORKWATCHERRG`
- Runtime path: `/home/azureuser/voice-assistant`

## Applied steps
1. Added git safe.directory on VM and fetched code branch:
   - `origin/codex/v1.6.1.42-code-only`
2. Checked out branch on VM:
   - branch: `codex/v1.6.1.42-code-only`
   - commit: `ee57d422`
3. Synced runtime version to `1.6.1.42`:
   - `/home/azureuser/voice-assistant/VERSION`
   - `/home/azureuser/voice-assistant/server/updates/manifests/manifest.json`
4. Resolved startup blocker for required text_processing:
   - updated `GEMINI_API_KEY` in `/home/azureuser/voice-assistant/config.env` to validated key
5. Restarted `voice-assistant` and verified endpoints.

## Verification
- `systemctl is-active voice-assistant` -> `active`
- `http://127.0.0.1:8080/health` -> `latest_version=1.6.1.42`, `latest_build=1.6.1.42`
- `http://127.0.0.1:8081/health` -> `version/latest_version/latest_build=1.6.1.42`
- No fresh `API_KEY_INVALID` / `API key expired` in tail logs after restart.
