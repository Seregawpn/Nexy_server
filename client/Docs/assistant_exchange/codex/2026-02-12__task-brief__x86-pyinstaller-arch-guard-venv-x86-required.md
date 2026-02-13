# Task Brief: Guard x86_64 PyInstaller against arm64 wheel contamination

## Problem
Full build failed at x86_64 PyInstaller stage with:

- `IncompatibleBinaryArchError: ... zstandard/_cffi.cpython-313-darwin.so ... has arch arm64, need x86_64`

Root cause: x86 stage was allowed to run via `arch -x86_64 "$BUILD_PYTHON"` from `.venv`, which still contains arm64-only binary wheels.

## Changes
1. `packaging/build_final.sh`
   - Removed fallback path that ran x86 build from `.venv` (`arch -x86_64 "$BUILD_PYTHON"`).
   - Added hard guard: x86 stage now requires `BUILD_PYTHON_X86` (`./.venv_x86/bin/python`).
   - Added validation that `BUILD_PYTHON_X86` can run under `arch -x86_64`.
   - x86 PyInstaller now always runs as:
     - `PYI_TARGET_ARCH=x86_64 arch -x86_64 "$BUILD_PYTHON_X86" -m PyInstaller ...`

2. `Docs/PACKAGING_FINAL_GUIDE.md`
   - Updated environment section: `.venv_x86` is mandatory for x86 build stage.

## Why this is architecture-safe
- Keeps a single owner (`build_final.sh`) for architecture routing.
- Prevents mixed-arch interpreter/site-packages usage in x86 phase.
- Fails early with explicit guidance instead of failing late during COLLECT.

## Verification
- `bash -n packaging/build_final.sh` passed.
- Guard and x86 run-path confirmed in script.
