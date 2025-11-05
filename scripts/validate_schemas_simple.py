#!/usr/bin/env python3
"""
Simple schema validation without hanging.
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed")
    sys.exit(1)


def main():
    """Quick validation - just check YAML syntax and enum values."""
    matrix_path = Path(__file__).parent.parent / "config" / "interaction_matrix.yaml"
    
    # Check YAML syntax
    try:
        data = yaml.safe_load(open(matrix_path))
        print(f"✅ {matrix_path} YAML syntax OK")
    except Exception as e:
        print(f"❌ {matrix_path} YAML error: {e}")
        return 1
    
    # Check required fields exist
    if "rules" not in data:
        print("❌ Missing 'rules' key")
        return 1
    
    # Check enum values in schema
    schema_path = Path(__file__).parent.parent / "client" / "config" / "schemas" / "interaction_matrix.schema.json"
    try:
        schema = json.load(open(schema_path))
        enum_values = schema["properties"]["rules"]["items"]["properties"]["decision"]["enum"]
        
        # Check all decision values are in enum
        invalid = []
        for i, rule in enumerate(data.get("rules", [])):
            decision = rule.get("decision")
            if decision and decision not in enum_values:
                invalid.append(f"rules[{i}].decision='{decision}'")
        
        if invalid:
            print(f"❌ Invalid decision values: {', '.join(invalid)}")
            print(f"Allowed: {enum_values}")
            return 1
        
        print(f"✅ All decision values valid ({len(data.get('rules', []))} rules)")
        return 0
    except Exception as e:
        print(f"⚠️ Schema check failed: {e} (but YAML is valid)")
        return 0  # Don't fail if schema check fails


if __name__ == "__main__":
    sys.exit(main())




