#!/usr/bin/env python3
"""Pre-flight dependency and binary verification for Nexy macOS packaging."""

from __future__ import annotations

import shutil
import subprocess
import sys
from importlib import metadata
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Distribution name -> expected version
REQUIRED_PACKAGES = {
    "aiohttp": "3.12.15",
    "grpcio": "1.75.1",
    "grpcio-tools": "1.75.1",
    "mss": "10.1.0",
    "numpy": "2.3.3",
    "Pillow": "11.3.0",
    "protobuf": "6.32.1",
    "psutil": "7.1.0",
    "PyAudio": "0.2.14",
    "pyinstaller": "6.16.0",
    "pyinstaller-hooks-contrib": "2025.9",
    "pyobjc-core": "12.1",
    "pyobjc-framework-AVFoundation": "11.1",
    "pyobjc-framework-Cocoa": "12.1",
    "pyobjc-framework-Quartz": "11.1",
    "pynput": "1.8.1",
    "pydub": "0.25.1",
    "PyYAML": "6.0.3",
    "rumps": "0.4.0",
    "SpeechRecognition": "3.14.4",
}

BINARY_REQUIREMENTS = [
    ("resources/ffmpeg/ffmpeg", ("arm64", "x86_64")),
    ("resources/audio/SwitchAudioSource", ("arm64", "x86_64")),
    ("resources/audio/flac", ("arm64", "x86_64")),
]


class CheckError(Exception):
    """Raised when the environment is not ready for packaging."""


def check_packages() -> list[str]:
    errors: list[str] = []
    for dist_name, expected_version in REQUIRED_PACKAGES.items():
        try:
            installed_version = metadata.version(dist_name)
        except metadata.PackageNotFoundError:
            errors.append(f"{dist_name}: not installed (expected {expected_version})")
            continue

        if installed_version != expected_version:
            errors.append(
                f"{dist_name}: {installed_version} (expected {expected_version})"
            )
    return errors


def check_binary_architectures() -> list[str]:
    errors: list[str] = []
    lipo_path = shutil.which("lipo")
    if not lipo_path:
        return ["lipo: command not found (install Xcode Command Line Tools)"]

    for rel_path, architectures in BINARY_REQUIREMENTS:
        absolute_path = PROJECT_ROOT / rel_path
        if not absolute_path.exists():
            errors.append(f"{rel_path}: file not found")
            continue

        result = subprocess.run(
            [lipo_path, "-info", str(absolute_path)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            errors.append(
                f"{rel_path}: lipo failed ({result.stderr.strip() or result.stdout.strip()})"
            )
            continue

        info = f"{result.stdout} {result.stderr}"
        missing = [arch for arch in architectures if arch not in info]
        if missing:
            errors.append(
                f"{rel_path}: missing architectures {', '.join(missing)}; got: {info.strip()}"
            )
    return errors


def main() -> int:
    errors = []
    package_errors = check_packages()
    binary_errors = check_binary_architectures()

    if package_errors:
        errors.extend(f"[python] {msg}" for msg in package_errors)
    if binary_errors:
        errors.extend(f"[binary] {msg}" for msg in binary_errors)

    if errors:
        print("❌ Pre-flight check failed:")
        for err in errors:
            print(f"   - {err}")
        return 1

    print("✅ All dependencies and binaries match packaging requirements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
