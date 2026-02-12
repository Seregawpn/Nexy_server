from __future__ import annotations

import ast
import os
import sys
from pathlib import Path

sys.path.insert(0, os.getcwd())


REPO_ROOT = Path(os.getcwd())
OWNERSHIP_SCAN_ROOTS = (
    REPO_ROOT / "integration",
    REPO_ROOT / "modules",
)


def _iter_python_files() -> list[Path]:
    files: list[Path] = []
    for root in OWNERSHIP_SCAN_ROOTS:
        if not root.exists():
            continue
        files.extend(root.rglob("*.py"))
    return files


def _is_publish_ready_to_greet_call(node: ast.Call) -> bool:
    if not isinstance(node.func, ast.Attribute) or node.func.attr != "publish":
        return False
    if not node.args:
        return False
    arg0 = node.args[0]
    return isinstance(arg0, ast.Constant) and arg0.value == "system.ready_to_greet"


def _is_set_restart_pending_call(node: ast.Call) -> bool:
    return isinstance(node.func, ast.Attribute) and node.func.attr == "set_restart_pending"


def test_only_v2_integration_publishes_system_ready_to_greet() -> None:
    found: list[Path] = []
    for path in _iter_python_files():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and _is_publish_ready_to_greet_call(node):
                found.append(path)
                break

    rel = sorted(str(p.relative_to(REPO_ROOT)) for p in found)
    assert rel == ["modules/permissions/v2/integration.py"]


def test_restart_pending_state_setter_removed() -> None:
    found: list[Path] = []
    for path in _iter_python_files():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and _is_set_restart_pending_call(node):
                found.append(path)
                break

    rel = sorted(str(p.relative_to(REPO_ROOT)) for p in found)
    assert rel == []
