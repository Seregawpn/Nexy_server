# Handoff: GitHub code push v1.6.1.43

Date: 2026-02-19
Assistant: codex
Type: handoff

## Summary
Выполнен code-only push версии `v1.6.1.43` без asset-pipeline.

## Commit
- Branch: `codex/v1.6.1.43-code-only`
- Commit: `79036956`
- Message: `release(server): bump code version to v1.6.1.43`

## Files in commit
- `server/VERSION`
- `server/server/config.env.example`
- `server/server/config/unified_config.yaml`
- `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/server/Docs/SERVER_DEPLOYMENT_GUIDE.md`

## Push targets
1. `Seregawpn/Nexy`:
   - branch pushed: `codex/v1.6.1.43-code-only`
   - tag pushed: `v1.6.1.43`
2. `Seregawpn/Nexy_server` (subtree from `server`):
   - branch pushed: `codex/v1.6.1.43-code-only`

## Notes
- Asset repositories and release assets were not touched.
