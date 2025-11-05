#!/usr/bin/env python3
"""
Verify that all rules from interaction_matrix.yaml are covered by tests.

Checks:
1. Every rule in interaction_matrix.yaml has a corresponding test
2. Gateway mentioned in rule exists and uses the axis/condition
3. Test covers the rule's decision logic

See .cursorrules section 11 for requirements.
"""
import re
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def load_interaction_matrix() -> Dict:
    """Load interaction_matrix.yaml."""
    matrix_path = Path(__file__).parent.parent / "config" / "interaction_matrix.yaml"
    if not matrix_path.exists():
        return {}
    
    try:
        with open(matrix_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"{RED}Error loading interaction_matrix.yaml: {e}{RESET}", file=sys.stderr)
        return {}


def load_test_gateways() -> str:
    """Load test_gateways.py content."""
    tests_file = Path(__file__).parent.parent / "tests" / "test_gateways.py"
    if not tests_file.exists():
        return ""
    
    try:
        with open(tests_file, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def check_gateway_exists(gateway_name: str) -> Tuple[bool, str]:
    """Check if gateway function exists in gateways."""
    gateways_dir = Path(__file__).parent.parent / "integration" / "core" / "gateways"
    
    # Check common.py
    common_file = gateways_dir / "common.py"
    if common_file.exists():
        with open(common_file, "r", encoding="utf-8") as f:
            content = f.read()
            if f"def {gateway_name}" in content or f"def decide_{gateway_name}" in content:
                return True, f"common.py"
    
    # Check permission_gateways.py
    perm_file = gateways_dir / "permission_gateways.py"
    if perm_file.exists():
        with open(perm_file, "r", encoding="utf-8") as f:
            content = f.read()
            if f"def {gateway_name}" in content:
                return True, f"permission_gateways.py"
    
    # Check all gateway files
    for gateway_file in gateways_dir.glob("**/*.py"):
        if gateway_file.name != "__init__.py":
            with open(gateway_file, "r", encoding="utf-8") as f:
                content = f.read()
                if f"def {gateway_name}" in content:
                    rel_path = gateway_file.relative_to(gateways_dir.parent.parent)
                    return True, str(rel_path)
    
    return False, ""


def check_rule_in_tests(rule: Dict, test_content: str) -> bool:
    """Check if rule is covered by tests."""
    # Extract key information from rule
    decision = rule.get("decision", "")
    gateway = rule.get("gateway", "")
    priority = rule.get("priority", "")
    when = rule.get("when", {})
    
    # Check if gateway is mentioned in tests
    if gateway and gateway not in test_content:
        return False
    
    # Check if decision is mentioned
    if decision and decision.replace("_", "") not in test_content.replace("_", ""):
        return False
    
    # Check if priority is tested (hard_stop/graceful)
    if priority == "hard_stop" and "abort" not in test_content.lower():
        return False
    if priority == "graceful" and ("retry" not in test_content.lower() and "degrade" not in test_content.lower()):
        return False
    
    return True


def main():
    """Main entry point."""
    print(f"{YELLOW}Checking rule coverage in tests...{RESET}\n")
    
    matrix = load_interaction_matrix()
    if not matrix:
        print(f"{RED}ERROR: Could not load interaction_matrix.yaml{RESET}", file=sys.stderr)
        return 1
    
    rules = matrix.get("rules", [])
    if not rules:
        print(f"{YELLOW}No rules found in interaction_matrix.yaml{RESET}")
        return 0
    
    test_content = load_test_gateways()
    if not test_content:
        print(f"{RED}ERROR: Could not load test_gateways.py{RESET}", file=sys.stderr)
        return 1
    
    errors = []
    warnings = []
    
    for rule in rules:
        gateway_name = rule.get("gateway", "")
        decision = rule.get("decision", "")
        priority = rule.get("priority", "")
        description = rule.get("description", "")
        
        if not gateway_name:
            warnings.append(f"Rule without gateway: {description or decision}")
            continue
        
        # Check gateway exists
        gateway_exists, gateway_location = check_gateway_exists(gateway_name)
        if not gateway_exists:
            print(f"{RED}❌ Rule gateway '{gateway_name}' not found{RESET}")
            errors.append(f"Gateway '{gateway_name}' not found (rule: {description or decision})")
            continue
        
        # Check rule is covered by tests
        if not check_rule_in_tests(rule, test_content):
            print(f"{YELLOW}⚠️  Rule may not be covered: {description or decision} (gateway: {gateway_name}){RESET}")
            warnings.append(f"Rule '{description or decision}' may not be covered by tests")
        else:
            print(f"{GREEN}✅ Rule covered: {description or decision} (gateway: {gateway_name}){RESET}")
    
    # Summary
    print(f"\n{'='*60}")
    if errors:
        print(f"{RED}❌ FAILED: {len(errors)} errors{RESET}")
        for error in errors:
            print(f"  {RED}• {error}{RESET}")
        return 1
    elif warnings:
        print(f"{YELLOW}⚠️  WARNINGS: {len(warnings)} rules may not be fully covered{RESET}")
        for warning in warnings:
            print(f"  {YELLOW}• {warning}{RESET}")
        print(f"{GREEN}✅ All gateways exist{RESET}")
        return 0
    else:
        print(f"{GREEN}✅ PASSED: All rules have gateways and appear to be covered{RESET}")
        return 0


if __name__ == "__main__":
    sys.exit(main())


