# Review

## Scope
Review timestamp-mode changes in:
- `packaging/build_final.sh`
- `scripts/sign_all_binaries.sh`

## Findings
- `TIMESTAMP_MODE`/`TIMESTAMP_FLAG` applied consistently to codesign/productsign calls.
- Duplicate `TIMESTAMP_MODE` block exists in `build_final.sh` for PKG signing; acceptable but should be kept consistent.
- No guard to prevent notarization when `TIMESTAMP_MODE=none`; use `NEXY_SKIP_NOTARIZATION=1` for local builds.

## Outcome
Changes are technically correct for toggling timestamp behavior. Ensure build instructions mention the notarization constraint when timestamp is disabled.
