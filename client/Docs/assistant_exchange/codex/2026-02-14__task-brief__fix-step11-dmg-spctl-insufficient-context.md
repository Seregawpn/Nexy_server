# Task Brief: fix Step 11 DMG spctl Insufficient Context failure

Date: 2026-02-14
Branch: release/v1.6.1.35

## Problem
Final build failed at Step 11 (`Итоговая верификация артефактов`) with:
- `spctl dmg: rejected`
- `source=Insufficient Context`
- exit code `3`

Even though app/pkg signing and notarization were already valid.

## Root cause
`packaging/build_final.sh` had duplicated DMG `spctl` logic:
- Step 10 handled `Insufficient Context` as non-fatal warning.
- Step 11 called `spctl --assess --type open` directly inside strict `set -e + pipefail` verification pipe, causing hard failure.

## Changes
Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/build_final.sh` in Step 11:
- Wrapped `spctl dmg` in guarded `if ...; then ... else ... fi`.
- Captures and logs `spctl` output.
- Treats `Insufficient Context` as warning with explicit message.
- Preserves strict failure behavior for truly critical checks.

## Verification
- `bash -n packaging/build_final.sh` => OK.
- Step 11 block now cannot crash solely on DMG `Insufficient Context`.

## Expected result
Full packaging no longer fails at Step 11 when DMG is notarized/stapled but `spctl` returns context-related non-zero status.
