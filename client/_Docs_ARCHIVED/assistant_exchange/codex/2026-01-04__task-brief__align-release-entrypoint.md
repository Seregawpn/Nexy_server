# Task Brief

## Objective
Align release flow docs and scripts to use the canonical `scripts/release_build.sh` entrypoint.

## Changes
- `scripts/prepare_release.sh`: switched build invocation to `scripts/release_build.sh release`.
- `Docs/RELEASE_TESTING_GUIDE.md`: replaced `build_final.sh` references with `scripts/release_build.sh release`.

## Verification
- No remaining references to `build_final.sh` in updated files.
