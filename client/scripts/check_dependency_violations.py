#!/usr/bin/env python3
"""Detect direct network client instantiations outside integration layer."""

from __future__ import annotations

import ast
from pathlib import Path
import sys
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_DIRS = {
    ROOT / "integration" / "integrations",
    ROOT / "modules" / "grpc_client",
}

ALLOWED_FILES = {
    ROOT / "scripts" / "check_dependency_violations.py",
}

TARGET_CALLS = {
    "GrpcClient",
}

HTTPX_CALL = ("httpx", "Client")


def is_allowed(path: Path) -> bool:
    if path in ALLOWED_FILES:
        return True
    for allowed in ALLOWED_DIRS:
        try:
            path.relative_to(allowed)
            return True
        except ValueError:
            continue
    return False


def iter_py_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        if "/.venv" in str(path) or "/.venv_x86" in str(path):
            continue
        if "/dist/" in str(path) or "/build/" in str(path):
            continue
        yield path


class ViolationVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.violations: list[tuple[int, str]] = []

    def visit_Call(self, node: ast.Call) -> None:
        name = None
        if isinstance(node.func, ast.Name):
            name = node.func.id
            if name in TARGET_CALLS:
                self.violations.append((node.lineno, name))
        elif isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                if (node.func.value.id, node.func.attr) == HTTPX_CALL:
                    self.violations.append((node.lineno, f"{node.func.value.id}.{node.func.attr}"))
        self.generic_visit(node)


def main() -> int:
    violations = []
    for path in iter_py_files(ROOT):
        if is_allowed(path):
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        visitor = ViolationVisitor()
        visitor.visit(tree)
        for lineno, name in visitor.violations:
            violations.append((path, lineno, name))

    if violations:
        print("Dependency violations detected:")
        for path, lineno, name in violations:
            rel = path.relative_to(ROOT)
            print(f"- {rel}:{lineno} -> {name}")
        return 1

    print("No dependency violations detected.")
    return 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--soft", action="store_true", help="Exit with 0 even if violations found")
    args = parser.parse_args()
    
    sys.exit(main() if not args.soft else (main() and 0))
