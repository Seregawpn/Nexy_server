# Task Brief: Replace Legacy Update IP with Domain

## Context
- Request: replace legacy public IP `20.151.51.172` with canonical domain `nexy-server.canadacentral.cloudapp.azure.com`.
- Goal: remove mixed endpoint usage (IP + domain) in active server scripts/config/docs.

## What Was Changed
- Replaced legacy IP with domain in active server paths:
  - `server/updates/manifests/manifest.json`
  - `server/nginx/grpc-passthrough.conf`
  - `server/scripts/*` (defaults, curl targets, prompts)
  - `server/tests/*`
  - `server/README.md`
  - `server/Docs/CI_GRPC_CHECKS.md`
  - `server/Docs/GRPC_PROTOCOL_AUDIT.md`
  - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - `Docs/COMPREHENSIVE_TESTING_GUIDE.md`
  - `Docs/TESTING_RESULTS.md`

## Architecture Note
- Public endpoint is now consistently domain-first in operational artifacts and validation scripts.
- Historical/archived docs under `_archive` were intentionally not rewritten.

## Verification
- Grep over active paths shows no remaining `20.151.51.172` references.
- Remaining references exist only in `server/Docs/_archive/*` and historical incident docs.

