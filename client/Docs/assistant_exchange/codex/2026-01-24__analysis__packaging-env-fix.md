# Analysis: packaging env/permissions issues

## Context
User reports missing permission prompts (Contacts) and inconsistent packaging; build logs show missing `pyobjc-framework-Contacts` and invalid entitlements in installed app/pkg.

## Findings
- `packaging/build_final.sh` uses `.venv` for arm64 build but system Python for x86_64, leading to inconsistent dependency sets.
- `packaging/Nexy.spec` includes `Contacts` hiddenimport, so missing module in build env causes it to be excluded from the bundled app.
- Entitlements validation is performed only on `CLEAN_APP` during signing; final artifacts (`dist/Nexy.app`, pkg payload) are not revalidated in-script.
- Required docs listed in AGENTS.md are missing in repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

## Proposed primary fix (plan)
- Standardize a single `BUILD_PYTHON` (universal `/Library/Frameworks/.../python3`) for all preflight checks and both arch PyInstaller builds.
- Remove `.venv` activation from build flow or ensure `.venv` matches the same dependency set for both arch builds.
- Add preflight checks for Contacts import using the same `BUILD_PYTHON` (and `arch -x86_64` for x86 path).
- Add post-copy entitlements validation for final artifacts (`dist/Nexy.app`, pkg payload) to catch signature regressions.

## Next checks
- Rebuild via `packaging/build_final.sh` and verify: `codesign -d --entitlements :- dist/Nexy.app`, `pkgutil --expand-full dist/Nexy.pkg` then check entitlements on payload app.
- Confirm Contacts prompt appears on first run after TCC reset.
