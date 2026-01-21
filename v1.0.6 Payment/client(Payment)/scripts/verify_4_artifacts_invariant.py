#!/usr/bin/env python3
"""
Verify the "4 artifacts invariant" for state axis changes.

Any change to state behavior MUST update:
1. Docs/STATE_CATALOG.md
2. config/interaction_matrix.yaml
3. integration/core/gateways.py (or gateways/**/*.py)
4. Gateway tests (≥8–14 pairwise + 2 negative)

See .cursorrules section 11 "Чеклист изменений" for details.
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Colors for output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def find_axis_mentions(filepath: Path, axis_name: str) -> List[int]:
    """Find line numbers where axis is mentioned."""
    mentions = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                # Check for axis mention (case-insensitive, word boundary)
                pattern = rf"\b{re.escape(axis_name)}\b"
                if re.search(pattern, line, re.IGNORECASE):
                    mentions.append(line_num)
    except Exception:
        pass
    return mentions


def check_state_catalog(axis_name: str) -> Tuple[bool, List[str]]:
    """Check if axis is documented in STATE_CATALOG.md."""
    catalog_path = Path(__file__).parent.parent / "Docs" / "STATE_CATALOG.md"
    if not catalog_path.exists():
        return False, [f"STATE_CATALOG.md not found at {catalog_path}"]
    
    mentions = find_axis_mentions(catalog_path, axis_name)
    if mentions:
        return True, [f"Found in STATE_CATALOG.md at lines: {', '.join(map(str, mentions))}"]
    return False, [f"NOT found in STATE_CATALOG.md"]


def check_interaction_matrix(axis_name: str) -> Tuple[bool, List[str]]:
    """Check if axis/rules are in interaction_matrix.yaml."""
    matrix_path = Path(__file__).parent.parent / "config" / "interaction_matrix.yaml"
    if not matrix_path.exists():
        return False, [f"interaction_matrix.yaml not found at {matrix_path}"]
    
    mentions = find_axis_mentions(matrix_path, axis_name)
    if mentions:
        return True, [f"Found in interaction_matrix.yaml at lines: {', '.join(map(str, mentions))}"]
    return False, [f"NOT found in interaction_matrix.yaml"]


def check_gateways(axis_name: str) -> Tuple[bool, List[str]]:
    """Check if axis is used in gateways."""
    gateways_dir = Path(__file__).parent.parent / "integration" / "core" / "gateways"
    found = []
    
    # Check main gateways.py
    gateways_file = gateways_dir / "common.py"
    if gateways_file.exists():
        mentions = find_axis_mentions(gateways_file, axis_name)
        if mentions:
            found.append(f"common.py:{', '.join(map(str, mentions))}")
    
    # Check permission_gateways.py
    perm_gateways = gateways_dir / "permission_gateways.py"
    if perm_gateways.exists():
        mentions = find_axis_mentions(perm_gateways, axis_name)
        if mentions:
            found.append(f"permission_gateways.py:{', '.join(map(str, mentions))}")
    
    # Check all gateway files
    for gateway_file in gateways_dir.glob("**/*.py"):
        if gateway_file.name != "__init__.py":
            mentions = find_axis_mentions(gateway_file, axis_name)
            if mentions:
                file_rel = gateway_file.relative_to(gateways_dir.parent.parent)
                found.append(f"{file_rel}:{', '.join(map(str, mentions))}")
    
    if found:
        return True, found
    return False, [f"NOT found in any gateway file"]


def check_tests(axis_name: str) -> Tuple[bool, List[str]]:
    """Check if axis is tested in gateway tests."""
    tests_file = Path(__file__).parent.parent / "tests" / "test_gateways.py"
    if not tests_file.exists():
        return False, [f"test_gateways.py not found"]
    
    mentions = find_axis_mentions(tests_file, axis_name)
    if mentions:
        return True, [f"Found in test_gateways.py at lines: {', '.join(map(str, mentions))}"]
    return False, [f"NOT found in test_gateways.py"]


def extract_axes_from_changes() -> Set[str]:
    """Extract axis names from git diff (if available)."""
    axes = set()
    
    # Common axis names to check
    known_axes = [
        "update_in_progress",
        "restart_pending",
        "first_run",
        "perm_mic",
        "perm_screen",
        "perm_accessibility",
        "device_input",
        "network",
        "app_mode",
    ]
    
    # Try to detect from git diff
    try:
        import subprocess
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            changed_files = result.stdout.splitlines()
            for file in changed_files:
                # Check if any known axis is in changed files
                for axis in known_axes:
                    if axis in file.lower():
                        axes.add(axis)
    except Exception:
        pass
    
    return axes or set(known_axes)


def main():
    """Main entry point."""
    root = Path(__file__).parent.parent
    
    # Get axes to check (from args or detect from changes)
    if len(sys.argv) > 1:
        axes_to_check = sys.argv[1:]
    else:
        axes_to_check = ["update_in_progress", "restart_pending"]  # Default check
    
    print(f"{YELLOW}Checking 4-artifacts invariant for axes: {', '.join(axes_to_check)}{RESET}\n")
    
    all_errors = []
    all_warnings = []
    
    for axis_name in axes_to_check:
        print(f"\n{GREEN}Checking axis: {axis_name}{RESET}")
        
        # 1. STATE_CATALOG.md
        catalog_ok, catalog_msgs = check_state_catalog(axis_name)
        if catalog_ok:
            print(f"  ✅ STATE_CATALOG.md: {catalog_msgs[0]}")
        else:
            print(f"  {RED}❌ STATE_CATALOG.md: {catalog_msgs[0]}{RESET}")
            all_errors.append(f"{axis_name}: Missing in STATE_CATALOG.md")
        
        # 2. interaction_matrix.yaml
        matrix_ok, matrix_msgs = check_interaction_matrix(axis_name)
        if matrix_ok:
            print(f"  ✅ interaction_matrix.yaml: {matrix_msgs[0]}")
        else:
            print(f"  {YELLOW}⚠️  interaction_matrix.yaml: {matrix_msgs[0]}{RESET}")
            all_warnings.append(f"{axis_name}: Missing in interaction_matrix.yaml (may be OK if axis doesn't affect decisions)")
        
        # 3. gateways.py
        gateways_ok, gateways_msgs = check_gateways(axis_name)
        if gateways_ok:
            print(f"  ✅ gateways: Found in {', '.join(gateways_msgs)}")
        else:
            print(f"  {RED}❌ gateways: {gateways_msgs[0]}{RESET}")
            all_errors.append(f"{axis_name}: Missing in gateways")
        
        # 4. tests
        tests_ok, tests_msgs = check_tests(axis_name)
        if tests_ok:
            print(f"  ✅ tests: {tests_msgs[0]}")
        else:
            print(f"  {RED}❌ tests: {tests_msgs[0]}{RESET}")
            all_errors.append(f"{axis_name}: Missing in test_gateways.py")
    
    # Summary
    print(f"\n{'='*60}")
    if all_errors:
        print(f"{RED}❌ FAILED: {len(all_errors)} errors found{RESET}")
        for error in all_errors:
            print(f"  {RED}• {error}{RESET}")
        return 1
    elif all_warnings:
        print(f"{YELLOW}⚠️  WARNINGS: {len(all_warnings)} warnings{RESET}")
        for warning in all_warnings:
            print(f"  {YELLOW}• {warning}{RESET}")
        print(f"{GREEN}✅ All required artifacts present{RESET}")
        return 0
    else:
        print(f"{GREEN}✅ PASSED: All 4 artifacts present for checked axes{RESET}")
        return 0


if __name__ == "__main__":
    sys.exit(main())




