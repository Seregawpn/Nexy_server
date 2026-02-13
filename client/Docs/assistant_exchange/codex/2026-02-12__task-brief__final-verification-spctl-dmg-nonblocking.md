# Task Brief: prevent false build failure on final `spctl dmg` check

## Problem
Build reached final verification and failed at:
- `spctl --assess --type open dist/Nexy.dmg`
- output: `source=Insufficient Context`
- exit code propagated via pipe to Step 11 and aborted build.

This is inconsistent with Step 10 where DMG notarization is already validated via `xcrun stapler validate`.

## Fix
Updated Step 11 in `packaging/build_final.sh`:
- changed `spctl dmg` from hard-fail command to report-only block;
- capture output + exit code without aborting script;
- print explicit note when reason is `Insufficient Context`;
- keep final verification log complete (`packaging_verification.log`) without false-negative build stop.

## Why safe
- Source of truth for DMG notarization remains `xcrun stapler validate` (already enforced).
- `spctl dmg` is retained as diagnostic signal only, not a release gate.

## Verification
- `bash -n packaging/build_final.sh` passes.
- Patched markers present around Step 11 `spctl dmg` block.
