#!/usr/bin/env python3
"""
Verify that all hiddenimports in Nexy.spec are available in the current Python environment.

Usage:
    python scripts/verify_spec_dependencies.py [--fix] [--verbose]

Options:
    --fix      Show pip install commands for missing packages
    --verbose  Show all checked modules, not just missing ones

Exit codes:
    0 = All dependencies present
    1 = Missing dependencies found
"""

import importlib.util
from pathlib import Path
import re
import sys

# ANSI colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
NC = "\033[0m"

# Known package name mappings (module name -> pip package name)
MODULE_TO_PACKAGE = {
    "PIL": "Pillow",
    "cv2": "opencv-python",
    "sklearn": "scikit-learn",
    "yaml": "PyYAML",
    "Quartz": "pyobjc-framework-Quartz",
    "AppKit": "pyobjc-framework-Cocoa",
    "Foundation": "pyobjc-framework-Cocoa",
    "Contacts": "pyobjc-framework-Contacts",
    "AVFoundation": "pyobjc-framework-AVFoundation",
    "objc": "pyobjc-core",
    "google.protobuf": "protobuf",
    "google.generativeai": "google-generativeai",
    "pydantic_core": "pydantic",
    "rumps": "rumps",
    "speech_recognition": "SpeechRecognition",
    "langchain_core": "langchain-core",
    "langchain_google_genai": "langchain-google-genai",
    "browser_use": "browser-use",
}

# Modules that are built-in or part of the project (skip checking)
SKIP_MODULES = {
    "asyncio", "asyncio.events", "asyncio.futures", "asyncio.tasks",
    "logging", "time", "sys", "pathlib", "uuid", "queue", "threading",
    "mimetypes",
    # Project modules
    "integration", "modules", "config",
}

# Prefixes for dynamically loaded modules (check parent only)
DYNAMIC_PREFIXES = [
    "AppKit.",      # pyobjc - submodules loaded dynamically
    "Foundation.",  # pyobjc - submodules loaded dynamically
    "Quartz.",      # pyobjc - submodules loaded dynamically
    "Contacts.",    # pyobjc - submodules loaded dynamically
    "AVFoundation.", # pyobjc - submodules loaded dynamically
    "playwright._impl.", # playwright - internal submodules
    "integration.", # Project modules
    "modules.",     # Project modules
]


def extract_hiddenimports(spec_path: Path) -> list[str]:
    """Extract hiddenimports list from Nexy.spec file."""
    content = spec_path.read_text()
    
    # Find hiddenimports=[ ... ] block
    match = re.search(r'hiddenimports\s*=\s*\[([^\]]+)\]', content, re.DOTALL)
    if not match:
        print(f"{RED}❌ Could not find hiddenimports in {spec_path}{NC}")
        return []
    
    block = match.group(1)
    
    # Extract quoted strings
    imports = re.findall(r'"([^"]+)"', block)
    return imports


def check_module(module_name: str) -> tuple[bool, str | None]:
    """
    Check if a module is importable.
    Returns (is_available, error_message)
    """
    # Skip built-in or project modules
    base_module = module_name.split(".", maxsplit=1)[0]
    if base_module in SKIP_MODULES or module_name in SKIP_MODULES:
        return True, None
    
    # Skip dynamic submodules (check parent availability instead)
    for prefix in DYNAMIC_PREFIXES:
        if module_name.startswith(prefix):
            # Check if parent module is available
            parent = prefix.rstrip(".")
            try:
                spec = importlib.util.find_spec(parent)
                return spec is not None, None
            except Exception:
                return False, f"Parent module {parent} not found"
    
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None, None
    except ModuleNotFoundError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def get_pip_package(module_name: str) -> str:
    """Get pip package name for a module."""
    # Check exact match
    if module_name in MODULE_TO_PACKAGE:
        return MODULE_TO_PACKAGE[module_name]
    
    # Check base module
    base = module_name.split(".", maxsplit=1)[0]
    if base in MODULE_TO_PACKAGE:
        return MODULE_TO_PACKAGE[base]
    
    # Default: assume package name = base module name with underscores replaced
    return base.replace("_", "-")


def main():
    verbose = "--verbose" in sys.argv
    show_fix = "--fix" in sys.argv
    
    # Find Nexy.spec
    script_dir = Path(__file__).parent
    client_dir = script_dir.parent
    spec_path = client_dir / "packaging" / "Nexy.spec"
    
    if not spec_path.exists():
        print(f"{RED}❌ Nexy.spec not found at {spec_path}{NC}")
        sys.exit(1)
    
    print(f"{YELLOW}📦 Checking dependencies from {spec_path.name}...{NC}")
    print()
    
    imports = extract_hiddenimports(spec_path)
    if not imports:
        sys.exit(1)
    
    missing = []
    available = []
    
    for module in imports:
        is_ok, error = check_module(module)
        if is_ok:
            available.append(module)
            if verbose:
                print(f"  {GREEN}✓{NC} {module}")
        else:
            missing.append((module, error))
            print(f"  {RED}✗{NC} {module}")
    
    print()
    print(f"Checked: {len(imports)} modules")
    print(f"  {GREEN}Available:{NC} {len(available)}")
    print(f"  {RED}Missing:{NC}   {len(missing)}")
    
    if missing:
        print()
        print(f"{RED}❌ Missing dependencies will cause runtime errors in packaged app!{NC}")
        
        if show_fix:
            print()
            print(f"{YELLOW}Suggested fix:{NC}")
            packages = set(get_pip_package(m) for m, _ in missing)
            print(f"  pip install {' '.join(sorted(packages))}")
        
        sys.exit(1)
    else:
        print()
        print(f"{GREEN}✅ All dependencies available{NC}")
        sys.exit(0)


if __name__ == "__main__":
    main()
