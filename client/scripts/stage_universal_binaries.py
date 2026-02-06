#!/usr/bin/env python3
"""
Stage Universal 2 binaries from vendor_binaries to resources.

This script creates Universal 2 (arm64 + x86_64) binaries by merging
architecture-specific binaries from vendor_binaries/ using lipo.

Required binaries:
- FFmpeg: vendor_binaries/ffmpeg/{arm64,x86_64}/ffmpeg -> resources/ffmpeg/ffmpeg
- FLAC: vendor_binaries/flac/{arm64,x86_64}/flac -> resources/audio/flac
- SwitchAudioSource: vendor_binaries/switchaudio/{arm64,x86_64}/SwitchAudioSource -> resources/audio/SwitchAudioSource
"""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Binary definitions: (name, vendor_path_template, output_path)
BINARY_DEFS = [
    (
        "FFmpeg",
        "vendor_binaries/ffmpeg/{arch}/ffmpeg",
        "resources/ffmpeg/ffmpeg",
    ),
    (
        "FLAC",
        "vendor_binaries/flac/{arch}/flac",
        "resources/audio/flac",
    ),
    (
        "SwitchAudioSource",
        "vendor_binaries/switchaudio/{arch}/SwitchAudioSource",
        "resources/audio/SwitchAudioSource",
    ),
]


def check_lipo() -> Path:
    """Check if lipo is available."""
    lipo_path = shutil.which("lipo")
    if not lipo_path:
        raise RuntimeError(
            "lipo command not found. Install Xcode Command Line Tools: xcode-select --install"
        )
    return Path(lipo_path)


def stage_binary(name: str, vendor_template: str, output_path: str) -> bool:
    """
    Stage a Universal 2 binary from vendor_binaries to resources.

    Args:
        name: Human-readable name of the binary
        vendor_template: Path template with {arch} placeholder (relative to PROJECT_ROOT)
        output_path: Output path (relative to PROJECT_ROOT)

    Returns:
        True if successful, False otherwise
    """
    arm64_path = PROJECT_ROOT / vendor_template.format(arch="arm64")
    x86_64_path = PROJECT_ROOT / vendor_template.format(arch="x86_64")
    output = PROJECT_ROOT / output_path

    # Check source binaries exist
    if not arm64_path.exists():
        print(f"❌ {name}: arm64 binary not found: {arm64_path}")
        return False

    if not x86_64_path.exists():
        print(f"❌ {name}: x86_64 binary not found: {x86_64_path}")
        return False

    # Create output directory
    output.parent.mkdir(parents=True, exist_ok=True)

    # Check if output already exists and is Universal 2
    if output.exists():
        lipo_path = check_lipo()
        result = subprocess.run(
            [str(lipo_path), "-info", str(output)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            info = result.stdout + result.stderr
            if "arm64" in info and "x86_64" in info:
                print(f"✅ {name}: Universal 2 binary already exists: {output}")
                return True

    # Create Universal 2 binary using lipo
    print(f"🔨 {name}: Creating Universal 2 binary...")
    print(f"   arm64: {arm64_path}")
    print(f"   x86_64: {x86_64_path}")
    print(f"   output: {output}")

    lipo_path = check_lipo()
    result = subprocess.run(
        [
            str(lipo_path),
            "-create",
            "-arch", "arm64", str(arm64_path),
            "-arch", "x86_64", str(x86_64_path),
            "-output", str(output),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"❌ {name}: lipo failed: {result.stderr}")
        return False

    # Make executable
    output.chmod(0o755)

    # Verify result
    verify_result = subprocess.run(
        [str(lipo_path), "-info", str(output)],
        capture_output=True,
        text=True,
    )

    if verify_result.returncode != 0:
        print(f"❌ {name}: Verification failed: {verify_result.stderr}")
        return False

    info = verify_result.stdout + verify_result.stderr
    if "arm64" not in info or "x86_64" not in info:
        print(f"❌ {name}: Verification failed - not Universal 2: {info}")
        return False

    print(f"✅ {name}: Universal 2 binary created successfully")
    print(f"   {info.strip()}")
    return True


def main() -> int:
    """Main entry point."""
    print("🚀 Staging Universal 2 binaries...")
    print(f"Project root: {PROJECT_ROOT}\n")

    success_count = 0
    for name, vendor_template, output_path in BINARY_DEFS:
        if stage_binary(name, vendor_template, output_path):
            success_count += 1
        else:
            print(f"❌ Failed to stage {name}")
            return 1
        print()

    print(f"✅ Successfully staged {success_count}/{len(BINARY_DEFS)} binaries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
