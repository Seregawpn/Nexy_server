#!/usr/bin/env python3
"""
Verify that all keys in interaction_matrix.yaml 'when' clauses are covered by predicates.

This ensures that DecisionEngine can properly evaluate all rules from the matrix.
"""
from __future__ import annotations

import sys
import yaml
from pathlib import Path
from typing import Set, Dict, Any

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from integration.core.gateways.predicates import REGISTRY
except ImportError as e:
    print(f"ERROR: Failed to import predicates registry: {e}")
    sys.exit(1)


def load_interaction_matrix() -> Dict[str, Any]:
    """Load interaction_matrix.yaml."""
    matrix_path = project_root / "config" / "interaction_matrix.yaml"
    if not matrix_path.exists():
        print(f"ERROR: interaction_matrix.yaml not found at {matrix_path}")
        sys.exit(1)
    
    with open(matrix_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def extract_predicate_keys(rules: list) -> Set[str]:
    """Extract all predicate keys from 'when' clauses."""
    keys = set()
    for rule in rules:
        when = rule.get("when", {})
        if isinstance(when, dict):
            keys.update(when.keys())
    return keys


def check_predicate_coverage(matrix: Dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Check that all predicate keys in rules are covered by REGISTRY.
    
    Returns:
        (is_valid, errors_list)
    """
    rules = matrix.get("rules", [])
    if not rules:
        return True, []
    
    predicate_keys = extract_predicate_keys(rules)
    registered_predicates = set(REGISTRY.keys())
    
    missing = predicate_keys - registered_predicates
    
    errors = []
    if missing:
        errors.append(f"Missing predicates in registry: {sorted(missing)}")
        errors.append(f"Registered predicates: {sorted(registered_predicates)}")
        errors.append(f"Keys found in rules: {sorted(predicate_keys)}")
    
    return len(missing) == 0, errors


def main():
    """Main entry point."""
    matrix = load_interaction_matrix()
    is_valid, errors = check_predicate_coverage(matrix)
    
    if not is_valid:
        print("ERROR: Some predicate keys in interaction_matrix.yaml are not registered")
        print("\n".join(errors))
        print("\nTo fix:")
        print("1. Add missing predicates to integration/core/gateways/predicates.py")
        print("2. Register them with @_register() decorator")
        sys.exit(1)
    
    print("✅ All predicate keys in interaction_matrix.yaml are covered by registry")
    sys.exit(0)


if __name__ == "__main__":
    main()



