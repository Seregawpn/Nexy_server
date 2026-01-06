# Packaging Signature Analysis

## Context
- User asked why current packaging is incorrect and how to make it correct.
- Local verification shows invalid signature for dist/Nexy.app (arm64).

## Findings
- `codesign --verify --deep --strict` fails for dist/Nexy.app and its main binary (arm64), implying post-sign modification.
- `packaging/build_final.sh` already enforces post-sign integrity; if it succeeded, current invalid state indicates later modification.

## Hypotheses
1) Post-sign file injection (e.g., running scripts/prepare_release.sh or similar that writes into dist/Nexy.app after signing).
2) Manual modifications/copying of dist/Nexy.app after signing.

## Recommended Fix
- Rebuild via packaging/build_final.sh from clean state and avoid any post-sign modifications to dist/Nexy.app.
- If metadata must be added, do it before signing inside the canonical workflow.

## Evidence
- Command: codesign --verify --deep --strict --verbose=2 dist/Nexy.app
- Output: invalid signature (code or signature have been modified) for arm64.

## Missing Required Sources
- Docs/ASSISTANT_COORDINATION_PROTOCOL.md
- Docs/ANTIGRAVITY_PROMPT.md
- Docs/CODEX_PROMPT.md
- Docs/assistant_exchange/TEMPLATE.md
