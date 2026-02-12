from __future__ import annotations

import ast
import os
import sys
from pathlib import Path

sys.path.insert(0, os.getcwd())


REPO_ROOT = Path(os.getcwd())
CANONICAL_APPMODE_FILE = REPO_ROOT / "modules" / "mode_management" / "core" / "types.py"
INTEGRATIONS_ROOT = REPO_ROOT / "integration" / "integrations"
SCAN_ROOTS = (
    REPO_ROOT / "integration",
    REPO_ROOT / "modules",
)


def _iter_python_files(roots: tuple[Path, ...]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(root.rglob("*.py"))
    return files


def test_no_local_appmode_enum_fallbacks() -> None:
    found: list[Path] = []
    for path in _iter_python_files(SCAN_ROOTS):
        if path.resolve() == CANONICAL_APPMODE_FILE.resolve():
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "AppMode":
                found.append(path)
                break

    rel = sorted(str(p.relative_to(REPO_ROOT)) for p in found)
    assert rel == []


def test_no_direct_state_manager_get_state_data_in_integrations() -> None:
    found: list[Path] = []
    for path in _iter_python_files((INTEGRATIONS_ROOT,)):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr != "get_state_data":
                continue
            found.append(path)
            break

    rel = sorted(str(p.relative_to(REPO_ROOT)) for p in found)
    assert rel == []
