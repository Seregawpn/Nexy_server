#!/bin/bash

set -euo pipefail

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE_DIR="${NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR:-$CLIENT_DIR/.cache/playwright-browsers-bundle}"
BUNDLE_DIR="$(python3 - <<PY
from pathlib import Path
print(Path('$BUNDLE_DIR').expanduser().resolve())
PY
)"
VERIFY_ONLY=0
FORCE_REINSTALL=0
if [[ "${1:-}" == "--verify-only" ]]; then
    VERIFY_ONLY=1
fi
if [[ "${1:-}" == "--force" ]]; then
    FORCE_REINSTALL=1
fi

if [ -x "$CLIENT_DIR/.venv/bin/python" ]; then
    BUILD_PYTHON="$CLIENT_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    BUILD_PYTHON="$(command -v python3)"
else
    echo "❌ python3 not found"
    exit 1
fi

if [ -x "$CLIENT_DIR/.venv_x86/bin/python" ]; then
    BUILD_PYTHON_X86="$CLIENT_DIR/.venv_x86/bin/python"
else
    BUILD_PYTHON_X86=""
fi

export NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR="$BUNDLE_DIR"
X86_TMP_DIR="${BUNDLE_DIR}.x86_tmp"

verify_bundle() {
    "$BUILD_PYTHON" - <<'PY'
import os
import sys
from pathlib import Path

bundle = Path(os.environ["NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR"]).resolve()
if not bundle.is_dir():
    print(f"bundle dir missing: {bundle}", file=sys.stderr)
    sys.exit(2)

chromium_dirs = [p for p in bundle.iterdir() if p.is_dir() and p.name.startswith("chromium-")]
if not chromium_dirs:
    print(f"no chromium-* dirs in {bundle}", file=sys.stderr)
    sys.exit(3)

def has_any_executable(base: Path, arch_dir: str) -> bool:
    candidates = [
        base / arch_dir / "Chromium.app" / "Contents" / "MacOS" / "Chromium",
        base / arch_dir / "Google Chrome for Testing.app" / "Contents" / "MacOS" / "Google Chrome for Testing",
    ]
    return any(c.is_file() for c in candidates)

def is_universal_ready(base: Path) -> bool:
    return (
        (has_any_executable(base, "chrome-mac") or has_any_executable(base, "chrome-mac-x64"))
        and has_any_executable(base, "chrome-mac-arm64")
        and (base / "INSTALLATION_COMPLETE").is_file()
    )

if not any(is_universal_ready(d) for d in chromium_dirs):
    print("chromium installation markers/executables missing for both mac arches", file=sys.stderr)
    sys.exit(4)

print("✅ Playwright bundle is universal-ready:", bundle)
PY
}

if [ "$VERIFY_ONLY" -eq 1 ]; then
    verify_bundle
    exit 0
fi

if [ "$FORCE_REINSTALL" -eq 0 ] && verify_bundle >/dev/null 2>&1; then
    echo "✅ Reusing prebuilt Playwright bundle: $BUNDLE_DIR"
    exit 0
fi

if [ "$VERIFY_ONLY" -eq 0 ]; then
    rm -rf "$BUNDLE_DIR" "$X86_TMP_DIR"
    mkdir -p "$BUNDLE_DIR" "$X86_TMP_DIR"

    echo "🔧 Preparing Playwright bundle: $BUNDLE_DIR"

    PLAYWRIGHT_BROWSERS_PATH="$BUNDLE_DIR" "$BUILD_PYTHON" -m playwright install chromium

    if [ -n "$BUILD_PYTHON_X86" ]; then
        # Playwright currently supports mac up to 15 in host override table.
        PLAYWRIGHT_BROWSERS_PATH="$X86_TMP_DIR" PLAYWRIGHT_HOST_PLATFORM_OVERRIDE="mac15" \
            arch -x86_64 "$BUILD_PYTHON_X86" -m playwright install --force chromium

        "$BUILD_PYTHON" - <<'PY'
import os
import shutil
import sys
from pathlib import Path

bundle = Path(os.environ["NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR"]).resolve()
x86_tmp = Path(str(bundle) + ".x86_tmp").resolve()

target_candidates = sorted([p for p in bundle.iterdir() if p.is_dir() and p.name.startswith("chromium-")])
source_candidates = sorted([p for p in x86_tmp.iterdir() if p.is_dir() and p.name.startswith("chromium-")])
if not target_candidates or not source_candidates:
    print("missing chromium dirs for x86 merge", file=sys.stderr)
    sys.exit(2)

target = target_candidates[0]
source = source_candidates[0]

source_x86 = None
for name in ("chrome-mac-x64", "chrome-mac"):
    candidate = source / name
    if candidate.is_dir():
        source_x86 = candidate
        break
if source_x86 is None:
    print(f"x86 Chromium dir not found in {source}", file=sys.stderr)
    sys.exit(3)

dest_x86 = target / source_x86.name
if dest_x86.exists():
    shutil.rmtree(dest_x86)
shutil.copytree(source_x86, dest_x86)

marker = target / "INSTALLATION_COMPLETE"
if not marker.exists():
    marker.touch()
PY
    fi
fi

verify_bundle

if [ "$VERIFY_ONLY" -eq 0 ]; then
    rm -rf "$X86_TMP_DIR"
    echo "✅ Done: $BUNDLE_DIR"
fi
