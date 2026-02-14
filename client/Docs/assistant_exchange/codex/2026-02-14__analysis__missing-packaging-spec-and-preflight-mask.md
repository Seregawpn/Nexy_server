# Analysis: missing packaging spec and masked preflight failures

Date: 2026-02-14
Scope: client packaging pipeline

## What happened
`./packaging/build_final.sh` reports successful preflight checks even when critical checks print missing file errors for `packaging/Nexy.spec`.

## Findings
1. `packaging/Nexy.spec` is physically absent in current workspace.
   - Verified: no `*.spec` files in client tree.
   - Packaging scripts hardcode this path:
     - `packaging/build_final.sh` (PyInstaller invocations)
     - `scripts/verify_packaging_readiness.py`
     - `scripts/verify_imports.py`
     - `scripts/verify_pyinstaller.py`
     - `scripts/verify_spec_dependencies.py`

2. Preflight failure masking exists in `packaging/build_final.sh`.
   - Current pattern: `if cmd 2>&1 | tee -a "$PREFLIGHT_LOG"; then ...`
   - Without `set -o pipefail`, `if` checks exit code of `tee` (usually 0), not `cmd`.
   - Result: false positive success lines like `✅ verify_pyinstaller.py - все проверки пройдены` even when script prints fatal missing spec error.

3. Architectural mismatch:
   - Source-of-truth for packaging is `packaging/Nexy.spec` (documented in `Docs/PACKAGING_FINAL_GUIDE.md` and referenced by all packaging validators).
   - Current tree violates this contract by missing the owner artifact.

## Why build progressed
Build moved past preflight due to masked non-zero exits and then reached signing/keychain stage. It will still fail later when actual PyInstaller command tries to consume `packaging/Nexy.spec`.

## Recommended primary fix
1. Restore canonical file `packaging/Nexy.spec` (from valid commit/artifact baseline).
2. In `packaging/build_final.sh`, add `set -o pipefail` near existing `set -e`.
3. Keep existing centralized validators; do not add local bypass flags.

## Quick verification
- Run: `./packaging/build_final.sh --speed-check`
- Expected:
  - If spec missing: preflight stops with non-zero and explicit failure block.
  - If spec restored: readiness checks and pyinstaller validation pass.
