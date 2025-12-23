#!/usr/bin/env python3
"""
Validate unified_config.yaml and interaction_matrix.yaml against JSON schemas.

Usage:
    python scripts/validate_schemas.py
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
    import yaml
except ImportError:
    print("ERROR: Required packages not installed. Run: pip install jsonschema pyyaml")
    sys.exit(1)


def load_yaml(filepath: Path) -> dict:
    """Load YAML file as dict."""
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


def load_schema(filepath: Path) -> dict:
    """Load JSON schema file."""
    with open(filepath, "r") as f:
        return json.load(f)


def validate_config():
    """Validate unified_config.yaml against schema."""
    config_path = Path(__file__).parent.parent / "config" / "unified_config.yaml"
    schema_path = Path(__file__).parent.parent / "client" / "config" / "schemas" / "unified_config.schema.json"
    
    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}")
        return False
    
    if not schema_path.exists():
        print(f"ERROR: Schema file not found: {schema_path}")
        return False
    
    try:
        config = load_yaml(config_path)
        schema = load_schema(schema_path)
        jsonschema.validate(instance=config, schema=schema)
        print(f"✅ {config_path} is valid")
        return True
    except jsonschema.ValidationError as e:
        print(f"❌ {config_path} validation failed:")
        print(f"  {e.message}")
        print(f"  Path: {'.'.join(str(p) for p in e.path)}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def validate_matrix():
    """Validate interaction_matrix.yaml against schema."""
    matrix_path = Path(__file__).parent.parent / "config" / "interaction_matrix.yaml"
    schema_path = Path(__file__).parent.parent / "client" / "config" / "schemas" / "interaction_matrix.schema.json"
    
    if not matrix_path.exists():
        print(f"ERROR: Matrix file not found: {matrix_path}")
        return False
    
    if not schema_path.exists():
        print(f"ERROR: Schema file not found: {schema_path}")
        return False
    
    try:
        matrix = load_yaml(matrix_path)
        schema = load_schema(schema_path)
        jsonschema.validate(instance=matrix, schema=schema)
        print(f"✅ {matrix_path} is valid")
        return True
    except jsonschema.ValidationError as e:
        print(f"❌ {matrix_path} validation failed:")
        print(f"  {e.message}")
        print(f"  Path: {'.'.join(str(p) for p in e.path)}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def main():
    """Main entry point."""
    config_ok = validate_config()
    matrix_ok = validate_matrix()
    
    if config_ok and matrix_ok:
        print("\n✅ All configs are valid")
        return 0
    else:
        print("\n❌ Validation failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())

