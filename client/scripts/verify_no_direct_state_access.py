#!/usr/bin/env python3
"""
Verify No Direct State Access (REQ-004)

Проверяет, что интеграции не обращаются напрямую к state_manager.get_*
вне контекста selectors/gateways.

Допустимые исключения:
- initialize() - первоначальный setup
- комментарии с TODO
- fallback с пометкой в комментариях
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Violation:
    file: str
    line_num: int
    line: str
    pattern: str
    severity: str  # "error" | "warning"

# Patterns that indicate direct state access (potential violations)
VIOLATION_PATTERNS = [
    (r"state_manager\.get_current_mode\(\)", "get_current_mode"),
    (r"state_manager\.get_current_session_id\(\)", "get_current_session_id"),
    (r"state_manager\.get_state_data\(", "get_state_data"),
    (r"state_manager\.get_restart_completed", "get_restart_completed"),
]

# Patterns that indicate legitimate usage (exceptions)
EXCEPTION_PATTERNS = [
    r"# TODO:",
    r"# Fallback:",
    r"# fallback:",
    r"# One-time read",
    r"# Initialize",
    r"def initialize\(",
    r"async def initialize\(",
    r"# Shadow-mode",
    r"# tracked via events",
    # Helper methods that encapsulate state access
    r"def _get_active_session_id\(",
    r"def _has_active_session\(",
    r"def _set_session_id\(",
    r"def get_current_session_id\(",
    r"def get_current_mode\(",
    r"def is_ptt_pressed\(",
    r"def is_first_run_in_progress\(",
    r"def has_active_session\(",
    # selectors.py internal use is allowed
    r"def create_snapshot_from_state\(",
    r"def is_update_in_progress\(",
    r"def is_restart_completed_fallback\(",
    # Comments about architecture
    r"КРИТИЧНО:",
    r"единый источник истины",
    r"single source of truth",
    # Comments mentioning "instead of" direct access (explains WHY gateway is used)
    r"Используется вместо прямого",
    r"вместо прямого чтения",
]

# Files to scan
INTEGRATION_DIRS = [
    "integration/integrations",
]

# Files that are allowed to access state directly (source of truth or realtime)
EXCEPTION_FILES = {
    # mode_management_integration is THE source of truth for mode changes
    "mode_management_integration.py",
}

def check_file(filepath: str) -> List[Violation]:
    """Check single file for violations."""
    violations = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Track current function context
    in_initialize = False
    current_function = None
    
    # Helper methods that are allowed to access state directly
    HELPER_METHODS = {
        "_get_active_session_id",
        "_has_active_session", 
        "_set_session_id",
        "_can_update",  # UpdaterIntegration fallback
        "create_snapshot_from_state",
        "is_update_in_progress",
        "is_restart_completed_fallback",
        "get_current_session_id",
        "get_current_mode",
        "is_ptt_pressed",
        "is_first_run_in_progress",
        "has_active_session",
    }
    
    for line_num, line in enumerate(lines, 1):
        # Track current function
        func_match = re.search(r"(?:async\s+)?def\s+(\w+)\s*\(", line)
        if func_match:
            current_function = func_match.group(1)
            in_initialize = current_function == "initialize"
        
        # Check for violations
        for pattern, name in VIOLATION_PATTERNS:
            if re.search(pattern, line):
                # Check if any exception pattern applies
                is_exception = False
                
                # Check if in initialize method
                if in_initialize:
                    is_exception = True
                
                # Check if in a helper method
                if current_function in HELPER_METHODS:
                    is_exception = True
                
                # Check previous 3 lines for exception comments
                context_start = max(0, line_num - 4)
                for context_line in lines[context_start:line_num]:
                    for exception_pattern in EXCEPTION_PATTERNS:
                        if re.search(exception_pattern, context_line, re.IGNORECASE):
                            is_exception = True
                            break
                    if is_exception:
                        break
                
                # Check current line for exception patterns
                for exception_pattern in EXCEPTION_PATTERNS:
                    if re.search(exception_pattern, line, re.IGNORECASE):
                        is_exception = True
                        break
                
                severity = "warning" if is_exception else "error"
                
                violations.append(Violation(
                    file=filepath,
                    line_num=line_num,
                    line=line.strip(),
                    pattern=name,
                    severity=severity
                ))
    
    return violations

def main():
    print("=" * 70)
    print("  VERIFY NO DIRECT STATE ACCESS (REQ-004)")
    print("=" * 70)
    print()
    
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    all_violations: List[Violation] = []
    
    for integration_dir in INTEGRATION_DIRS:
        dir_path = project_root / integration_dir
        if not dir_path.exists():
            print(f"⚠️  Directory not found: {dir_path}")
            continue
        
        for py_file in dir_path.glob("*.py"):
            if py_file.name.startswith("__"):
                continue
            
            # Skip files that are allowed to access state directly
            if py_file.name in EXCEPTION_FILES:
                continue
            
            violations = check_file(str(py_file))
            all_violations.extend(violations)
    
    # Categorize violations
    errors = [v for v in all_violations if v.severity == "error"]
    warnings = [v for v in all_violations if v.severity == "warning"]
    
    # Print results
    if errors:
        print("❌ ERRORS (require refactoring):")
        print("-" * 70)
        for v in errors:
            rel_path = Path(v.file).name
            print(f"  {rel_path}:{v.line_num} - {v.pattern}")
            print(f"    {v.line[:80]}...")
        print()
    
    if warnings:
        print("⚠️  WARNINGS (exceptions/fallbacks):")
        print("-" * 70)
        for v in warnings:
            rel_path = Path(v.file).name
            print(f"  {rel_path}:{v.line_num} - {v.pattern}")
            print(f"    {v.line[:80]}...")
        print()
    
    # Summary
    print("=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print(f"  Errors:   {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Total:    {len(all_violations)}")
    print()
    
    if errors:
        print("❌ Direct state access found! Consider migrating to selectors/gateways.")
        return 1
    elif warnings:
        print("⚠️  Some warnings found, but they appear to be legitimate exceptions.")
        return 0
    else:
        print("✅ No direct state access violations found!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
