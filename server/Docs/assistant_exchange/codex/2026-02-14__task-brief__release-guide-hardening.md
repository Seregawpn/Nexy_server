# Task Brief: Release Guide Hardening

## Context
- Requested to harden release documentation and prevent recurring publication failures (missing inbox, wrong script path, repo/tag confusion).
- Target file: `Docs/RELEASE_AND_UPDATE_GUIDE.md`.

## What Was Updated
- Added "Release Infrastructure Rules (Golden Rules)" with fixed infra requirements:
  - inbox presence
  - canonical script path
  - code repo vs release repo split
  - fixed production tags (`Update`, `App`)
- Expanded Phase 2 with:
  - pre-check commands
  - execution command
  - expected log markers
  - URL-based verification steps
- Added "Troubleshooting & Maintenance":
  - inbox missing
  - script path mismatch
  - GH CLI auth errors
  - wrong `TARGET_REPO`/tag mapping
- Added "Search / Logs (Поиск)" section:
  - artifacts location
  - manifest location
  - script output logs
  - remote release URLs

## Outcome
- Documentation now acts as a strict operational rulebook + practical troubleshooting playbook.
- The previous high-risk ambiguity (`server/server/scripts/...` vs `server/scripts/...`) is explicitly documented and resolved.
