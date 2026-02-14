# Handoff: Docs Two-Pipeline Alignment

## Objective
Align server documentation with the confirmed operating model:
- `Seregawpn/Nexy_server` for server code storage and deploy
- `Seregawpn/Nexy_production/releases` for DMG/PKG publication

## Updated Files
- `Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `server/Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/update_process_guide.md`

## What Changed
- Added explicit "Two Pipelines" rules to release/deploy docs.
- Standardized code repo references to `Seregawpn/Nexy_server` in release instructions.
- Added guardrail for wrong git remote before manifest push.
- Removed conflicting default guidance to force-push in deployment flow.
- Replaced outdated client-artifact section in deploy guide with redirect to release canon.
- Fixed multiple broken canonical links in architecture overview.
- Converted `Docs/update_process_guide.md` into a compatibility redirect to canonical guides.

## Notes
- The current runtime code still has historical duality around manifest naming (`manifest.json` vs `manifest_*.json` in some providers/scripts). This handoff only aligns docs and flow ownership.
