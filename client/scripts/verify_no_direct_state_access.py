#!/usr/bin/env python3
"""
Script to verify no direct state access outside selectors/gateways.

See .cursorrules section 21.3 for architecture details.
"""
import re
import sys
from pathlib import Path

# Patterns that should only be accessed through selectors/gateways
PATTERNS = [
    r"\bperm_mic\b",
    r"\bperm_screen\b",
    r"\bperm_accessibility\b",
    r"\bnetwork_online\b",
    r"\bfirst_run\b",
    r"\bdevice_input\b",
    r"\bapp_mode\b",
    r"\bstate\.get",
    r"\bstate\.set",
    r"\bstate_manager\.get",
    r"\bstate_manager\.set",
    r"\bApplicationStateManager\(\)\.get",
]

# Files allowed to access state directly
ALLOWED_PATTERNS = [
    r".*[/\\]selectors\.py$",
    r".*[/\\]gateways\.py$",
    r".*[/\\]gateways[/\\].*\.py$",
    r".*[/\\]test.*\.py$",
    r".*[/\\]tests[/\\].*\.py$",
]


def is_allowed_file(filepath: str) -> bool:
    """Check if file is allowed to access state directly."""
    for pattern in ALLOWED_PATTERNS:
        if re.match(pattern, filepath):
            return True
    return False


def check_file(filepath: Path) -> list:
    """Check file for direct state access violations."""
    violations = []
    
    if is_allowed_file(str(filepath)):
        return violations
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        for line_num, line in enumerate(content.split("\n"), 1):
            # Skip comments
            if line.strip().startswith("#"):
                continue
                
            for pattern in PATTERNS:
                if re.search(pattern, line):
                    violations.append({
                        "file": str(filepath),
                        "line": line_num,
                        "pattern": pattern,
                        "content": line.strip(),
                    })
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
    
    return violations


def main():
    """Main entry point."""
    root = Path(__file__).parent.parent
    
    # Python files to check
    python_files = []
    for pattern in ["**/*.py"]:
        python_files.extend(root.glob(pattern))
    
    # Exclude certain directories
    excluded_dirs = {".git", ".venv", "build", "dist", "resources", "__pycache__"}
    python_files = [
        f for f in python_files
        if not any(excluded in str(f) for excluded in excluded_dirs)
    ]
    
    all_violations = []
    for filepath in python_files:
        violations = check_file(filepath)
        all_violations.extend(violations)
    
    if all_violations:
        print("ERROR: Direct state access violations found:", file=sys.stderr)
        for violation in all_violations:
            print(
                f"  {violation['file']}:{violation['line']}: "
                f"Pattern '{violation['pattern']}' found",
                file=sys.stderr,
            )
            print(f"    {violation['content']}", file=sys.stderr)
        return 1
    
    print("OK: No direct state access violations found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
