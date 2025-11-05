#!/usr/bin/env python3
"""
Verify feature flags and kill-switches are registered in FEATURE_FLAGS.md.

See .cursorrules section 6.1 and 19.1 for requirements.
"""
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Set

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Required flags for first-run/permission-restart
REQUIRED_FLAGS = {
    "NEXY_FEATURE_FIRST_RUN_V2",
    "NEXY_FEATURE_PERMISSION_RESTART_V2",
    "NEXY_KS_PERMISSION_RESTART_V2",
    "NEXY_DISABLE_AUTO_RESTART",
}


def load_feature_flags_md() -> Dict[str, Dict]:
    """Load feature flags from FEATURE_FLAGS.md."""
    flags_md = Path(__file__).parent.parent / "Docs" / "FEATURE_FLAGS.md"
    if not flags_md.exists():
        return {}
    
    flags = {}
    try:
        with open(flags_md, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Extract flag names from markdown table
            # Format: | `FLAG_NAME` | Type | ...
            pattern = r"\| `([^`]+)` \|"
            matches = re.findall(pattern, content)
            for match in matches:
                flags[match] = {"found": True, "source": "FEATURE_FLAGS.md"}
    except Exception as e:
        print(f"{YELLOW}Warning: Could not parse FEATURE_FLAGS.md: {e}{RESET}", file=sys.stderr)
    
    return flags


def load_unified_config() -> Dict:
    """Load unified_config.yaml to check for feature flags."""
    config_path = Path(__file__).parent.parent / "config" / "unified_config.yaml"
    if not config_path.exists():
        return {}
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def check_flag_in_code(flag_name: str) -> List[str]:
    """Check if flag is used in code."""
    root = Path(__file__).parent.parent
    locations = []
    
    # Search for flag usage
    for py_file in root.rglob("*.py"):
        if any(excluded in str(py_file) for excluded in [".git", ".venv", "build", "dist"]):
            continue
        
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()
                if flag_name in content:
                    rel_path = py_file.relative_to(root)
                    locations.append(str(rel_path))
        except Exception:
            pass
    
    return locations


def main():
    """Main entry point."""
    print(f"{YELLOW}Checking feature flags registration...{RESET}\n")
    
    flags_md = load_feature_flags_md()
    config = load_unified_config()
    
    errors = []
    warnings = []
    
    for flag_name in REQUIRED_FLAGS:
        print(f"\n{GREEN}Checking: {flag_name}{RESET}")
        
        # Check in FEATURE_FLAGS.md
        if flag_name in flags_md:
            print(f"  ✅ Registered in FEATURE_FLAGS.md")
        else:
            print(f"  {RED}❌ NOT registered in FEATURE_FLAGS.md{RESET}")
            errors.append(f"{flag_name}: Missing in FEATURE_FLAGS.md")
        
        # Check in code
        code_locations = check_flag_in_code(flag_name)
        if code_locations:
            print(f"  ✅ Found in code: {', '.join(code_locations[:3])}{'...' if len(code_locations) > 3 else ''}")
        else:
            print(f"  {YELLOW}⚠️  NOT found in code (may be OK if not yet implemented){RESET}")
            warnings.append(f"{flag_name}: Not found in code")
    
    # Summary
    print(f"\n{'='*60}")
    if errors:
        print(f"{RED}❌ FAILED: {len(errors)} missing registrations{RESET}")
        for error in errors:
            print(f"  {RED}• {error}{RESET}")
        return 1
    elif warnings:
        print(f"{YELLOW}⚠️  WARNINGS: {len(warnings)} flags not found in code{RESET}")
        print(f"{GREEN}✅ All required flags registered in FEATURE_FLAGS.md{RESET}")
        return 0
    else:
        print(f"{GREEN}✅ PASSED: All required flags registered and found{RESET}")
        return 0


if __name__ == "__main__":
    sys.exit(main())


