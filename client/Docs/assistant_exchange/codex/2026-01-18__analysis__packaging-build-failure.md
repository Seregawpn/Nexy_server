# Analysis: Packaging build failure

## Symptom
`packaging/build_final.sh` failed during PyInstaller COLLECT with `Failed to process binary` for `_sha2.cpython-313-darwin.so`. Log also shows missing hidden imports for `modules.permissions.macos.*` and missing `libFLAC.14.dylib`.

## Root Cause
Primary failure: corrupted/missing PyInstaller cache binary in `~/Library/Application Support/pyinstaller/.../_sha2.cpython-313-darwin.so`, causing `process_collected_binary` to abort. Additional risks: missing hidden imports and missing libFLAC dependency may cause runtime issues even if build succeeds.

## Recommended Fix
1. Clear PyInstaller cache and rebuild (`~/Library/Application Support/pyinstaller`), plus clean `build-*` and `dist-*` directories.
2. Ensure Python/venv consistency (use expected Python 3.13 universal or the venv used by build).
3. Address missing `libFLAC.14.dylib` (install or bundle), and resolve hidden imports if they are required.

## Evidence
Build log excerpt shows:
- `ERROR: Hidden import 'modules.permissions.macos.accessibility_handler' not found`
- `WARNING: Library not found: ... libFLAC.14.dylib`
- `SystemError: Failed to process binary ... _sha2.cpython-313-darwin.so`

## Files
- `build_logs/build_20260118_141847.log`
- `packaging/build_final.sh`
- `packaging/Nexy.spec`
