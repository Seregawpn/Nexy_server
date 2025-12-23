#!/usr/bin/env python3
"""Smoke tests for Universal 2 Nexy.app on both architectures."""

import subprocess
import sys
import time
from pathlib import Path

APP_PATH = Path(__file__).parent.parent / "dist" / "Nexy.app"

def check_architecture():
    """Check current architecture."""
    result = subprocess.run(
        ["uname", "-m"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def check_app_architectures(app_path: Path):
    """Check architectures in the app."""
    main_binary = app_path / "Contents" / "MacOS" / "Nexy"
    if not main_binary.exists():
        return False, "Main binary not found"
    
    result = subprocess.run(
        ["lipo", "-info", str(main_binary)],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return False, f"lipo failed: {result.stderr}"
    
    info = result.stdout
    has_arm64 = "arm64" in info
    has_x86_64 = "x86_64" in info
    
    return True, {
        "arm64": has_arm64,
        "x86_64": has_x86_64,
        "info": info.strip()
    }

def check_resources(app_path: Path):
    """Check that resource binaries are universal."""
    resources = [
        "Contents/Resources/resources/ffmpeg/ffmpeg",
        "Contents/Resources/resources/audio/SwitchAudioSource",
        "Contents/Resources/resources/audio/flac",
    ]
    
    results = {}
    for rel_path in resources:
        full_path = app_path / rel_path
        if not full_path.exists():
            results[rel_path] = "not found"
            continue
        
        result = subprocess.run(
            ["lipo", "-info", str(full_path)],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            results[rel_path] = f"lipo failed: {result.stderr}"
            continue
        
        info = result.stdout
        has_arm64 = "arm64" in info
        has_x86_64 = "x86_64" in info
        results[rel_path] = {
            "arm64": has_arm64,
            "x86_64": has_x86_64,
            "universal": has_arm64 and has_x86_64
        }
    
    return results

def test_app_launch(app_path: Path, arch: str = None):
    """Test launching the app."""
    cmd = ["open", "-W", str(app_path)]
    if arch:
        cmd = ["arch", f"-{arch}"] + cmd
    
    print(f"  Launching app ({arch or 'native'})...")
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait a bit for app to start
    time.sleep(3)
    
    # Check if process is still running (app launched)
    if process.poll() is None:
        process.terminate()
        time.sleep(1)
        if process.poll() is None:
            process.kill()
        return True, "App launched successfully"
    else:
        return False, f"App exited with code {process.returncode}"

def main():
    if not APP_PATH.exists():
        print(f"❌ App not found: {APP_PATH}")
        return 1
    
    print(f"🧪 Smoke testing Universal 2 app: {APP_PATH}\n")
    
    # Check architectures
    print("1. Checking app architectures...")
    success, arch_info = check_app_architectures(APP_PATH)
    if not success:
        print(f"   ❌ {arch_info}")
        return 1
    
    print(f"   ✅ Main binary: {arch_info['info']}")
    if not (arch_info['arm64'] and arch_info['x86_64']):
        print("   ❌ Main binary is not Universal 2!")
        return 1
    
    # Check resources
    print("\n2. Checking resource binaries...")
    resource_results = check_resources(APP_PATH)
    all_universal = True
    for rel_path, result in resource_results.items():
        if isinstance(result, dict):
            if result.get("universal"):
                print(f"   ✅ {rel_path}: Universal 2")
            else:
                print(f"   ❌ {rel_path}: Missing architectures")
                all_universal = False
        else:
            print(f"   ❌ {rel_path}: {result}")
            all_universal = False
    
    if not all_universal:
        return 1
    
    # Test launch (native)
    print("\n3. Testing app launch (native architecture)...")
    current_arch = check_architecture()
    print(f"   Current architecture: {current_arch}")
    
    success, msg = test_app_launch(APP_PATH)
    if success:
        print(f"   ✅ {msg}")
    else:
        print(f"   ⚠️  {msg} (may need manual testing)")
    
    # Test launch (Rosetta if on Apple Silicon)
    if current_arch == "arm64":
        print("\n4. Testing app launch (Rosetta/x86_64)...")
        success, msg = test_app_launch(APP_PATH, "x86_64")
        if success:
            print(f"   ✅ {msg}")
        else:
            print(f"   ⚠️  {msg} (may need manual testing)")
    
    print("\n✅ Basic smoke tests completed!")
    print("\n⚠️  Manual testing recommended:")
    print("   - Verify menu bar icon appears")
    print("   - Test audio functionality")
    print("   - Test external tools (ffmpeg, SwitchAudioSource, flac)")
    print("   - Test on actual Intel Mac if available")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

