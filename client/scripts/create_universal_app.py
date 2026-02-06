#!/usr/bin/env python3
"""Merge arm64 and x86_64 PyInstaller bundles into a Universal 2 app."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm64", required=True, type=Path, help="Path to arm64 Nexy.app")
    parser.add_argument("--x86", required=True, type=Path, help="Path to x86_64 Nexy.app")
    parser.add_argument("--output", required=True, type=Path, help="Destination for Universal Nexy.app")
    parser.add_argument("--verbose", action="store_true", help="Print each merged file")
    return parser.parse_args()


def ensure_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"{label} not found: {path}")
    if path.suffix != ".app":
        raise SystemExit(f"{label} must point to Nexy.app bundle: {path}")


def is_macho(path: Path) -> bool:
    if path.is_symlink() or not path.is_file():
        return False
    result = subprocess.run(
        ["file", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return False
    return "Mach-O" in result.stdout


def get_architectures(path: Path) -> list[str]:
    """Get architectures in a Mach-O file."""
    result = subprocess.run(
        ["lipo", "-info", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    info = result.stdout
    archs = []
    if "arm64" in info:
        archs.append("arm64")
    if "x86_64" in info:
        archs.append("x86_64")
    return archs


def merge_binary(
    arm_src: Path,
    x86_src: Path,
    dest: Path,
    display_path: str,
    verbose: bool = False,
) -> None:
    # Check architectures
    arm_archs = get_architectures(arm_src)
    x86_archs = get_architectures(x86_src)
    
    # If both have same architectures, just copy one
    if set(arm_archs) == set(x86_archs):
        if verbose:
            print(f"⏭️  {display_path} (same arch: {', '.join(arm_archs)})")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(arm_src, dest)
        return
    
    # If one is already universal, use it
    if "arm64" in arm_archs and "x86_64" in arm_archs:
        if verbose:
            print(f"✓ {display_path} (arm64 already universal)")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(arm_src, dest)
        return
    
    if "arm64" in x86_archs and "x86_64" in x86_archs:
        if verbose:
            print(f"✓ {display_path} (x86_64 already universal)")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(x86_src, dest)
        return
    
    # Merge different architectures
    if verbose:
        print(f"🔄 lipo {display_path}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix="nexy-universal-", suffix=".bin")
    os.close(fd)
    Path(tmp_path).unlink(missing_ok=True)  # We'll let lipo create the file
    result = subprocess.run(
        [
            "lipo",
            "-create",
            str(arm_src),
            str(x86_src),
            "-output",
            tmp_path,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        # If merge fails, try to use the one that's more complete
        if "arm64" in arm_archs and "x86_64" not in x86_archs:
            if verbose:
                print(f"⚠️  {display_path} (merge failed, using arm64)")
            shutil.copy2(arm_src, dest)
            return
        raise SystemExit(
            f"lipo failed for {dest}:\nstdout: {result.stdout}\nstderr: {result.stderr}"
        )
    shutil.copymode(arm_src, tmp_path)
    Path(tmp_path).replace(dest)


def main() -> int:
    args = parse_args()
    arm_app = args.arm64.resolve()
    x86_app = args.x86.resolve()
    out_app = args.output.resolve()

    ensure_exists(arm_app, "arm64 bundle")
    ensure_exists(x86_app, "x86_64 bundle")

    if out_app.exists():
        shutil.rmtree(out_app)
    shutil.copytree(arm_app, out_app, symlinks=True)

    binaries_merged = 0
    missing = []
    for arm_file in arm_app.rglob("*"):
        if not is_macho(arm_file):
            continue
        rel_path = arm_file.relative_to(arm_app)
        x86_file = x86_app / rel_path
        if not x86_file.exists():
            missing.append(rel_path)
            continue
        if not is_macho(x86_file):
            continue
        dest_file = out_app / rel_path
        merge_binary(
            arm_file,
            x86_file,
            dest_file,
            str(rel_path),
            verbose=args.verbose,
        )
        binaries_merged += 1

    if missing:
        print("⚠️  Missing counterparts detected:")
        for rel in missing:
            print(f"   - {rel}")

    print(f"✅ Universal merge completed. Binaries merged: {binaries_merged}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

