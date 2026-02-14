# Task Brief: remove interactive keychain password prompt in build

Date: 2026-02-14
Branch: release/v1.6.1.35

## Problem
`packaging/build_final.sh` could trigger a password prompt via `security unlock-keychain login.keychain` without `-p`.

## Fix
Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/build_final.sh` to use non-interactive keychain handling:
- Removed unlock call without password.
- Added env-based non-interactive unlock:
  - `NEXY_KEYCHAIN_PASSWORD` (preferred)
  - `APPLE_KEYCHAIN_PASSWORD` (fallback)
- Added optional keychain name override:
  - `NEXY_KEYCHAIN_NAME` (default: `login.keychain-db`)
- If password env is present, script runs:
  - `security unlock-keychain -p ...`
  - `security set-key-partition-list ...`
- If password env is absent, script explicitly skips unlock (no prompt).

## Verification
- `bash -n packaging/build_final.sh` => OK.
- Keychain section now has no interactive `security unlock-keychain` call.
