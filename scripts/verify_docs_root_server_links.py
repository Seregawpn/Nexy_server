#!/usr/bin/env python3
"""Verify backtick file-path refs in root Docs and server/server/Docs.

Scope:
- Docs/*.md
- server/server/Docs/*.md

The checker validates only path-like refs. Commands, HTTP paths, code ids,
method refs ("::"), and wildcards are ignored.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC_GLOBS = [
    ROOT / "Docs",
    ROOT / "server" / "server" / "Docs",
]

BACKTICK_RE = re.compile(r"`([^`]+)`")

PATH_PREFIXES = (
    "Docs/",
    "client/",
    "server/",
    "scripts/",
    "tests/",
    "config/",
    "modules/",
    "integration/",
    "packaging/",
    "monitoring/",
    "updates/",
    ".github/",
    "../../Docs/",
)

PATH_SINGLE = {
    "main.py",
    "pyproject.toml",
    "requirements.txt",
    "pytest.ini",
    "VERSION",
}


def is_path_like(ref: str) -> bool:
    if not ref:
        return False
    if ref in PATH_SINGLE:
        return True
    if ref.startswith(PATH_PREFIXES):
        return True
    return False


def should_skip(ref: str) -> bool:
    if any(tok in ref for tok in ("::", "*", "{", "}", "<", ">", "|")):
        return True
    if ref.startswith(("http://", "https://", "/")):
        return True
    if " " in ref:
        return True
    if ref in {"updates/health", "health", "status"}:
        return True
    return False


def resolve_ref(doc_file: Path, ref: str) -> Path:
    # For docs under server/server/Docs, relative refs are resolved from server/server.
    # Many server docs still use repo-root style aliases (server/Docs, server/scripts, etc.).
    if "server/server/Docs" in str(doc_file):
        server_root = ROOT / "server" / "server"
        root_server = ROOT / "server"
        if ref.startswith("../../Docs/"):
            return ROOT / ref.replace("../../", "", 1)
        if ref == "VERSION":
            # Server docs canonically refer to server/VERSION in repo-root layout.
            return root_server / "VERSION"
        if ref.startswith("Docs/"):
            return server_root / ref
        if ref.startswith("server/Docs/"):
            alt = server_root / ref.replace("server/", "", 1)
            return alt
        if ref.startswith("server/scripts/"):
            return server_root / ref.replace("server/", "", 1)
        if ref.startswith("server/config/"):
            return server_root / ref.replace("server/", "", 1)
        if ref.startswith("server/integrations/"):
            return server_root / ref.replace("server/", "", 1)
        if ref.startswith("server/modules/"):
            return server_root / ref.replace("server/", "", 1)
        if ref.startswith("server/updates/"):
            return server_root / ref.replace("server/", "", 1)
        if ref.startswith(("server/", "client/")):
            return ROOT / ref
        return server_root / ref

    # Root Docs refs resolve from repo root
    return ROOT / ref


def main() -> int:
    misses: list[tuple[Path, str, Path]] = []

    for base in DOC_GLOBS:
        for md in sorted(base.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            for ref in BACKTICK_RE.findall(text):
                if should_skip(ref) or not is_path_like(ref):
                    continue
                target = resolve_ref(md, ref)
                if not target.exists():
                    misses.append((md, ref, target))

    if not misses:
        print("Docs link check passed (root + server).")
        return 0

    print("Missing path refs:")
    for md, ref, target in misses:
        print(f"- {md.relative_to(ROOT)} :: `{ref}` -> {target}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
