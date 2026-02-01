# Task Brief: unify build Python + entitlements validation

## Goal
Stabilize packaging by using a single build Python for all preflight/build steps and add entitlements validation on final artifacts.

## Changes
- Unified `BUILD_PYTHON` usage for preflight, PyInstaller builds (arm64/x86_64), and packaging scripts.
- Removed `.venv` activation during build to avoid dependency divergence.
- Added Contacts check for both native and x86_64 execution.
- Added entitlements validation for final `dist/Nexy.app` and PKG payload app.

## Files touched
- `packaging/build_final.sh`

## Notes
- `scripts/verify_feature_flags.py` is missing in repo; attempted run failed.

## Next steps
- Rebuild via `./packaging/build_final.sh`.
- Verify logs for Contacts availability and entitlements checks.
