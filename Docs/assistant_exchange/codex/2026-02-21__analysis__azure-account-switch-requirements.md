# Azure Account Switch Requirements (Server)

## Context
- Request: migrate server deployment to another Azure account with possible public IP change.
- Scope: server deployment pipeline and runtime availability.

## Source Documents
- AGENTS.md
- server/Docs/SERVER_DEPLOYMENT_GUIDE.md
- server/Docs/RELEASE_AND_UPDATE_GUIDE.md
- server/Docs/DEPLOY_INCIDENT_RUNBOOK.md
- monitor_inbox/2026-02-19__05-49-43__incident__server-monitor.remote.md

## Key Constraints
- Code deploy source of truth: `Seregawpn/Nexy_server`.
- Runtime config source of truth on VM: `/home/azureuser/voice-assistant/config.env`.
- No parallel `az vm run-command invoke` during deploy.
- Internal ports remain localhost-only; external access only through nginx 443.

## Migration Preconditions
1. Access to new Azure subscription with role Contributor/Owner.
2. Confirm target region, VM SKU, and static public IP policy.
3. Prepare secrets: GEMINI_API_KEY (+ optional AZURE_SPEECH_*), Stripe/webhook, DB creds if used.
4. DNS/endpoint migration plan (A record cutover and TTL reduction).
5. Validate SSH key and NSG source IP allow-list.

## DoD
- VM healthy (`/health`, `/status`, `/updates/health`).
- `voice-assistant` active.
- Version/build synchronized with target release.
- Clients switched to new endpoint without second owner-path.
