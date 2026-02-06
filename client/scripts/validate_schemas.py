#!/usr/bin/env python3
"""Validate YAML configs against JSON schemas."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def main() -> int:
    config_path = ROOT / "config" / "unified_config.yaml"
    schema_path = ROOT / "client" / "config" / "schemas" / "unified_config.schema.json"
    matrix_path = ROOT / "config" / "interaction_matrix.yaml"
    matrix_schema_path = ROOT / "client" / "config" / "schemas" / "interaction_matrix.schema.json"

    if not config_path.exists() or not schema_path.exists():
        print("Missing unified config or schema.")
        return 1
    if not matrix_path.exists() or not matrix_schema_path.exists():
        print("Missing interaction matrix or schema.")
        return 1

    config = load_yaml(config_path)
    schema = load_json(schema_path)
    matrix = load_yaml(matrix_path)
    matrix_schema = load_json(matrix_schema_path)

    jsonschema.validate(instance=config, schema=schema)
    jsonschema.validate(instance=matrix, schema=matrix_schema)

    print("Schema validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
