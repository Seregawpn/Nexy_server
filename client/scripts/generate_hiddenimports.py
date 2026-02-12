#!/usr/bin/env python3
"""
Generate recommended hiddenimports for Nexy.spec based on transitive dependency analysis.

This script analyzes key packages (browser-use, langchain, pydantic) and their
full dependency trees to generate a comprehensive list of modules that need
to be in hiddenimports for PyInstaller to correctly bundle them.

Usage:
    python scripts/generate_hiddenimports.py [--diff] [--update]

Options:
    --diff    Compare generated list against current Nexy.spec and show differences
    --update  Automatically update Nexy.spec with new imports (requires confirmation)

Exit codes:
    0 = Success
    1 = Error or missing deps found with --diff
"""

import importlib.metadata
import importlib.util
from pathlib import Path
import re
import sys

# ANSI colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"

# Key packages to analyze for browser-use functionality
KEY_PACKAGES = [
    "browser-use",
    "langchain-core",
    "langchain-google-genai",
    "pydantic",
    "httpx",
    "playwright",
]

# Submodules that are commonly needed but not auto-detected
KNOWN_SUBMODULES = {
    "pydantic": [
        "pydantic",
        "pydantic_core",
        "pydantic._migration",
        "pydantic.warnings",
        "pydantic.version",
    ],
    "httpx": [
        "httpx",
        "httpx._config",
    ],
    "httpcore": [
        "httpcore",
        "httpcore._async",
        "httpcore._sync",
    ],
    "h11": [
        "h11",
        "h11._connection",
    ],
    "anyio": [
        "anyio",
        "anyio._backends",
        "anyio._backends._asyncio",
    ],
    "idna": [
        "idna",
        "idna.codec",
    ],
    "playwright": [
        "playwright",
        "playwright._impl",
        "playwright._impl.main",
        "playwright.async_api",
        "playwright.sync_api",
    ],
    "browser_use": [
        "browser_use",
        "browser_use.browser",
        "browser_use.browser.profile",
        "browser_use.agent",
        "browser_use.llm.views",
    ],
    "langchain_core": [
        "langchain_core",
        "langchain_core.messages",
        "langchain_core.language_models",
        "langchain_core.outputs",
    ],
}

# Packages to skip (stdlib, PyInstaller handles them, or not needed)
SKIP_PACKAGES = {
    "pip",
    "setuptools",
    "wheel",
    "pkg_resources",
    "pytest",
    "black",
    "flake8",
    "mypy",
    "ruff",
    "sphinx",
    "docutils",
}


def get_package_dependencies(
    package_name: str, visited: set[str] | None = None, depth: int = 0
) -> set[str]:
    """
    Recursively get all dependencies of a package.
    Returns set of package names (not module names).
    """
    if visited is None:
        visited = set()

    pkg_lower = package_name.lower()
    if pkg_lower in visited or depth > 5:
        return set()

    visited.add(pkg_lower)
    deps = set()

    try:
        requires = importlib.metadata.requires(package_name)
        if not requires:
            return deps

        for req in requires:
            # Skip extras and environment markers for now
            if "extra ==" in req or ";" in req:
                # Still parse the package name
                pass

            # Extract package name (before version specifier)
            match = re.match(r"^([a-zA-Z0-9_-]+)", req.split(";")[0])
            if match:
                dep_name = match.group(1).lower()
                if dep_name not in SKIP_PACKAGES and dep_name not in visited:
                    deps.add(dep_name)
                    # Recurse
                    deps.update(get_package_dependencies(dep_name, visited, depth + 1))
    except importlib.metadata.PackageNotFoundError:
        pass
    except Exception as e:
        print(f"  {YELLOW}⚠{NC} Error analyzing {package_name}: {e}")

    return deps


def package_to_module(package_name: str) -> str:
    """Convert package name to importable module name."""
    # Common mappings
    mappings = {
        "pillow": "PIL",
        "pyyaml": "yaml",
        "pyobjc-core": "objc",
        "google-generativeai": "google.generativeai",
        "google-api-core": "google.api_core",
        "google-auth": "google.auth",
        "protobuf": "google.protobuf",
        "speechrecognition": "speech_recognition",
        "browser-use": "browser_use",
    }

    pkg_lower = package_name.lower()
    if pkg_lower in mappings:
        return mappings[pkg_lower]

    # Default: replace dashes with underscores
    return package_name.replace("-", "_")


def is_module_available(module_name: str) -> bool:
    """Check if module is importable."""
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except Exception:
        return False


def generate_hiddenimports() -> list[str]:
    """Generate comprehensive hiddenimports list."""
    print(f"{YELLOW}📦 Analyzing package dependencies...{NC}")
    print()

    all_packages = set()

    for pkg in KEY_PACKAGES:
        print(f"  Analyzing {BLUE}{pkg}{NC}...")
        deps = get_package_dependencies(pkg)
        all_packages.add(pkg.lower())
        all_packages.update(deps)
        print(f"    Found {len(deps)} dependencies")

    print()
    print(f"Total unique packages: {len(all_packages)}")
    print()

    # Convert to modules and check availability
    hiddenimports: set[str] = set()

    for pkg in sorted(all_packages):
        module = package_to_module(pkg)

        # Add known submodules
        if module in KNOWN_SUBMODULES:
            for submod in KNOWN_SUBMODULES[module]:
                if is_module_available(submod.split(".")[0]):
                    hiddenimports.add(submod)
        elif is_module_available(module):
            hiddenimports.add(module)

    # Add critical modules that are always needed
    critical = [
        "jiter",
        "orjson",
        "sniffio",
        "certifi",
        "tenacity",
        "filetype",
        "attrs",
    ]
    for mod in critical:
        if is_module_available(mod):
            hiddenimports.add(mod)

    return sorted(hiddenimports)


def extract_current_hiddenimports(spec_path: Path) -> set[str]:
    """Extract hiddenimports from Nexy.spec."""
    content = spec_path.read_text()
    match = re.search(r"hiddenimports\s*=\s*\[([^\]]+)\]", content, re.DOTALL)
    if not match:
        return set()

    block = match.group(1)
    imports = re.findall(r'"([^"]+)"', block)
    return set(imports)


def main():
    show_diff = "--diff" in sys.argv
    do_update = "--update" in sys.argv

    # Find paths
    script_dir = Path(__file__).parent
    client_dir = script_dir.parent
    spec_path = client_dir / "packaging" / "Nexy.spec"

    # Generate recommended imports
    recommended = set(generate_hiddenimports())

    print(f"{GREEN}Generated {len(recommended)} recommended hiddenimports{NC}")
    print()

    if show_diff or do_update:
        if not spec_path.exists():
            print(f"{RED}❌ Nexy.spec not found{NC}")
            sys.exit(1)

        current = extract_current_hiddenimports(spec_path)

        # Filter: only show browser-use related modules (not project modules)
        browser_related = {m for m in recommended if not m.startswith(("integration.", "modules."))}

        missing_in_spec = browser_related - current

        if missing_in_spec:
            print(f"{YELLOW}Missing from Nexy.spec ({len(missing_in_spec)}):{NC}")
            for mod in sorted(missing_in_spec):
                print(f'  {RED}+{NC} "{mod}",')
            print()

        if not missing_in_spec:
            print(f"{GREEN}✅ Nexy.spec has all recommended browser-use imports{NC}")
        else:
            print(f"{YELLOW}Consider adding the above imports to hiddenimports in Nexy.spec{NC}")
            sys.exit(1)
    else:
        # Just print the list
        print("Recommended hiddenimports for browser-use:")
        print()
        for mod in sorted(recommended):
            if not mod.startswith(("integration.", "modules.")):
                print(f'        "{mod}",')


if __name__ == "__main__":
    main()
