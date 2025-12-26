#!/usr/bin/env python3
"""
Architecture Verification Script
--------------------------------
Ensures code adheres to architectural rules:
1. No direct access to StateManager (use selectors/gateways).
2. No direct instantiation of UnifiedConfigLoader (use singleton).
3. No direct logging.getLogger(__name__) (use get_logger).

See .cursorrules for details.
"""
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple

print("DEBUG: STARTING NEW ARCHITECTURE VERIFICATION SCRIPT")

# -----------------------------------------------------------------------------
# RULES CONFIGURATION
# -----------------------------------------------------------------------------

RULES = [
    {
        "name": "Direct State Access",
        "description": "Accessing StateManager directly instead of using selectors/gateways",
        "severity": "ERROR",
        "patterns": [
            r"\bstate\.get_state_data",
            r"\bstate\.set_state_data",
            r"\bstate_manager\.get_state_data",
            r"\bstate_manager\.set_state_data",
            r"\bApplicationStateManager\(\)\.get",
            r"\.get_state_data\(",        ],
        "allowed_files": [
            r".*[/\\]selectors\.py$",
            r".*[/\\]gateways\.py$",
            r".*[/\\]gateways[/\\].*\.py$",
            r".*[/\\]state_manager\.py$",
            r".*[/\\]test.*\.py$",
            r".*[/\\]tests[/\\].*\.py$",
            r".*[/\\]base_integration\.py$",  # BaseIntegration needs state access
        ]
    },
    {
        "name": "Config Instantiation",
        "description": "Direct instantiation of UnifiedConfigLoader (must use .get_instance())",
        "severity": "ERROR",
        "patterns": [
            r"UnifiedConfigLoader\(\)",
        ],
        "allowed_files": [
            r".*[/\\]unified_config_loader\.py$",
            r".*[/\\]test.*\.py$",
            r".*[/\\]tests[/\\].*\.py$",
        ]
    },
    {
        "name": "Logger Instantiation",
        "description": "Direct use of logging.getLogger(__name__) (should use integration.utils.get_logger)",
        "severity": "WARNING",  # Warning for now, will upgrade to ERROR later
        "patterns": [
            r"logging\.getLogger\(__name__\)",
        ],
        "allowed_files": [
            r".*[/\\]logging_setup\.py$",
            r".*[/\\]unified_config_loader\.py$",  # Before integration init
        ]
    }
]

# -----------------------------------------------------------------------------
# IGNORE LIST (Legacy violations whitelist)
# -----------------------------------------------------------------------------
IGNORED_FILES = {
    # Legacy Modules (scheduled for future refactoring or removal)
    # None - All legacy modules handled or refactored.
    
    # Utility scripts (dev tools) that may violate architecture for convenience
    "check_first_run_state.py",
    "verify_4_artifacts_invariant.py",
    "verify_audio_migration_compliance.py",
    "analyze_audio_migration_readiness_detailed.py",
    "clear_first_run_flags.py",
    "run_release_suite.py",
    
    # Other legacy files with known issues (add as needed)
    "legacy_module_example.py", 
}

def is_allowed(filepath: str, allowed_patterns: List[str]) -> bool:
    """Check if file matches any allowed pattern."""
    for pattern in allowed_patterns:
        if re.match(pattern, filepath):
            return True
    return False

def check_file(filepath: Path) -> List[Dict[str, Any]]:
    """Check file for violations of all rules."""
    violations = []
    
    # Whitelist check
    if filepath.name in IGNORED_FILES:
        return violations

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        lines = content.split("\n")
        
        for rule in RULES:
            if is_allowed(str(filepath), rule["allowed_files"]):
                continue
                
            for line_num, line in enumerate(lines, 1):
                # Skip comments
                if line.strip().startswith("#"):
                    continue
                    
                for pattern in rule["patterns"]:
                    if re.search(pattern, line):
                        violations.append({
                            "rule": rule["name"],
                            "severity": rule["severity"],
                            "file": str(filepath),
                            "line": line_num,
                            "pattern": pattern,
                            "content": line.strip(),
                        })
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
    
    return violations

def main():
    root = Path(__file__).parent.parent
    
    # Collect Python files
    python_files = []
    for pattern in ["**/*.py"]:
        python_files.extend(root.glob(pattern))
    
    # Exclude system directories
    excluded_dirs = {".git", ".venv", "build", "dist", "resources", "__pycache__"}
    python_files = [
        f for f in python_files
        if not any(excluded in str(f) for excluded in excluded_dirs)
    ]
    
    all_violations = []
    for filepath in python_files:
        violations = check_file(filepath)
        all_violations.extend(violations)
    
    error_count = 0
    warning_count = 0
    
    if all_violations:
        print("\n🔍 ARCHITECTURE VERIFICATION REPORT\n" + "="*40)
        
        for v in all_violations:
            icon = "❌" if v["severity"] == "ERROR" else "⚠️ "
            print(f"{icon} [{v['severity']}] {v['rule']}")
            print(f"   File: {v['file']}:{v['line']}")
            print(f"   Code: {v['content']}")
            print("-" * 40)
            
            if v["severity"] == "ERROR":
                error_count += 1
            else:
                warning_count += 1

    print(f"\nSummary: {error_count} Errors, {warning_count} Warnings")
    
    if error_count > 0:
        print("\n❌ FAILED: Architectural violations found.")
        return 1
    
    print("\n✅ PASSED: No critical architectural violations.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
