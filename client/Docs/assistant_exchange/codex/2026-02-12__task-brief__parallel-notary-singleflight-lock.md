# Task Brief: parallel packaging anti-race for notarytool keychain profile

## Problem
- After enabling parallel DMG/PKG packaging, build failed with:
  - `Error: No Keychain password item found for profile: nexy-notary`
  - DMG branch succeeded while PKG branch failed (exit 69).

## Root cause
- Concurrent `xcrun notarytool submit` calls from two background branches (`DMG` and `PKG`)
  against one shared keychain profile can race.

## Fix
- Added centralized single-flight guard in `packaging/build_final.sh`:
  - function `with_notary_lock()` with lock dir `/tmp/nexy_notarytool.lock`.
- Wrapped only parallel notary submits with this lock:
  - DMG submit
  - PKG submit

## Why this fits
- Keeps parallel build/sign flow as requested.
- Serializes only critical shared-resource operation (notarytool profile access).
- No architecture break and no extra state owners.

## Verification
- `bash -n packaging/build_final.sh` passes.
- `with_notary_lock` and wrapped submit calls present in script.
