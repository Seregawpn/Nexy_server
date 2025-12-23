#!/usr/bin/env python3
"""Merge .so files from x86_64 installation into main site-packages."""

import subprocess
import sys
import tempfile
from pathlib import Path

MAIN_SITE = Path("/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages")
X86_SITE = Path("/tmp/x86_64_site_packages")

def find_so_files(root):
    """Find all .so files recursively."""
    return list(root.rglob("*.so"))

def get_relative_path(full_path, base):
    """Get relative path from base."""
    try:
        return full_path.relative_to(base)
    except ValueError:
        return None

def merge_so(main_so, x86_so):
    """Merge two .so files into universal binary."""
    # Check if main_so already has both architectures
    result = subprocess.run(
        ["lipo", "-info", str(main_so)],
        capture_output=True,
        text=True
    )
    if result.returncode == 0 and "x86_64" in result.stdout and "arm64" in result.stdout:
        return True, "already universal"
    
    # Create universal binary
    with tempfile.NamedTemporaryFile(delete=False, suffix=".so") as tmp:
        tmp_path = tmp.name
    
    result = subprocess.run(
        ["lipo", "-create", str(main_so), str(x86_so), "-output", tmp_path],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        return False, f"lipo failed: {result.stderr}"
    
    # Backup original
    backup = main_so.with_suffix(main_so.suffix + ".backup")
    subprocess.run(["cp", str(main_so), str(backup)], check=False)
    
    # Replace with universal
    subprocess.run(["cp", str(tmp_path), str(main_so)], check=True)
    subprocess.run(["rm", tmp_path], check=False)
    
    return True, "merged"

def main():
    print("Finding .so files in x86_64 installation...")
    x86_so_files = {get_relative_path(f, X86_SITE): f for f in find_so_files(X86_SITE)}
    print(f"Found {len(x86_so_files)} .so files in x86_64 installation\n")
    
    print("Merging with main site-packages...")
    merged = 0
    skipped = 0
    errors = 0
    
    for rel_path, x86_so in x86_so_files.items():
        if rel_path is None:
            continue
        
        main_so = MAIN_SITE / rel_path
        if not main_so.exists():
            continue
        
        success, msg = merge_so(main_so, x86_so)
        if success:
            if "already" in msg:
                skipped += 1
            else:
                merged += 1
                print(f"✓ {rel_path}")
        else:
            errors += 1
            print(f"✗ {rel_path}: {msg}")
    
    print(f"\n✅ Merged: {merged}, Already universal: {skipped}, Errors: {errors}")
    return 0 if errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

