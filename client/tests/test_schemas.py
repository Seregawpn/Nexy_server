"""
Schema validation tests for unified_config.yaml and interaction_matrix.yaml
"""
import json
import os
import pytest
from pathlib import Path

try:
    import jsonschema
except ImportError:
    pytest.skip("jsonschema not installed", allow_module_level=True)


def load_yaml(filepath: Path) -> dict:
    """Load YAML file as dict."""
    import yaml
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


def load_schema(filepath: Path) -> dict:
    """Load JSON schema file."""
    with open(filepath, "r") as f:
        return json.load(f)


def test_unified_config_schema():
    """Test unified_config.yaml against schema."""
    config_path = Path(__file__).parent.parent / "config" / "unified_config.yaml"
    schema_path = Path(__file__).parent.parent / "client" / "config" / "schemas" / "unified_config.schema.json"
    
    if not config_path.exists() or not schema_path.exists():
        pytest.skip("Config or schema files not found")
    
    config = load_yaml(config_path)
    schema = load_schema(schema_path)
    
    jsonschema.validate(instance=config, schema=schema)


def test_interaction_matrix_schema():
    """Test interaction_matrix.yaml against schema."""
    matrix_path = Path(__file__).parent.parent / "config" / "interaction_matrix.yaml"
    schema_path = Path(__file__).parent.parent / "client" / "config" / "schemas" / "interaction_matrix.schema.json"
    
    if not matrix_path.exists() or not schema_path.exists():
        pytest.skip("Matrix or schema files not found")
    
    matrix = load_yaml(matrix_path)
    schema = load_schema(schema_path)
    
    jsonschema.validate(instance=matrix, schema=schema)

