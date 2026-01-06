# Remove prepare_release.sh

## Summary
- Removed scripts/prepare_release.sh to eliminate non-canonical packaging path.

## Reasoning
- File could modify .app after signing; canonical workflow is packaging/build_final.sh.

## Files
- Deleted: scripts/prepare_release.sh

## Notes
- Required sources missing in repo: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md.
