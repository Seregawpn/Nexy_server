# Server Update Process (Redirect)

This file is kept for compatibility and points to active canonical guides.

## Two Independent Pipelines

1. Code + Deploy pipeline:
- Repository: `Seregawpn/Nexy_server`
- Canon: `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`

2. Client artifacts pipeline:
- Repository: `Seregawpn/Nexy_production/releases`
- Canon: `Docs/RELEASE_AND_UPDATE_GUIDE.md`

## Mandatory Rule

Do not mix these pipelines:
- Server source deployment must go only through `Nexy_server`.
- Client update artifacts (`Nexy.dmg`, `Nexy.pkg`) must go only through `Nexy_production/releases`.

## Versioning Priority

For runtime version behavior, use:
- `server/config/unified_config.py`
- `server/main.py`

If this file conflicts with canonical guides, canonical guides win.
