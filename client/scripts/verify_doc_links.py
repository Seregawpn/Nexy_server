#!/usr/bin/env python3
"""Verify that repository-path references in canonical documentation exist."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_DOCS = [
    "Docs/README.md",
    "Docs/DOCUMENTATION_MAP.md",
    "Docs/REQUIREMENTS_SOURCE_MAP.md",
    "Docs/PROJECT_REQUIREMENTS.md",
    "Docs/STATE_CATALOG.md",
    "Docs/first_run_flow_spec.md",
    "Docs/ARCHITECTURE_OVERVIEW.md",
    "Docs/PRODUCT_CONCEPT.md",
    "Docs/PACKAGING_FINAL_GUIDE.md",
    "Docs/FEATURE_FLAGS.md",
    "Docs/RELEASE_VERSIONING_AND_PUBLISHING.md",
    "Docs/PRE_PACKAGING_VERIFICATION.md",
    "Docs/PACKAGING_READINESS_CHECKLIST.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")

ALLOWED_PREFIXES = (
    "Docs/",
    "scripts/",
    "config/",
    "integration/",
    "modules/",
    "tests/",
    "packaging/",
    "resources/",
    "assets/",
    "client/",
    ".github/",
)
ALLOWED_ROOT_FILES = {
    "main.py",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "PERMISSIONS_REPORT.md",
    "AGENTS.md",
    ".cursorrules",
    "log.md",
}
IGNORE_PREFIXES = (
    "_Docs_ARCHIVED/",
    "Docs/_archive/",
    "dist/",
    "build/",
    "build_logs/",
    "tmp/",
)


def _iter_candidates(line: str) -> list[str]:
    out: list[str] = []
    for m in LINK_RE.finditer(line):
        out.append(m.group(1).strip())
    for m in CODE_RE.finditer(line):
        out.append(m.group(1).strip())
    return out


def _normalize(raw: str, doc_rel: str) -> str | None:
    candidate = raw.strip().strip(".,:;)")
    if not candidate:
        return None
    if "://" in candidate or candidate.startswith("mailto:"):
        return None
    if candidate.startswith("#"):
        return None
    if " " in candidate or "\t" in candidate:
        return None
    if candidate.startswith("/") or candidate.startswith("~/"):
        return None

    candidate = candidate.split("#", 1)[0]
    if candidate.startswith("./"):
        candidate = candidate[2:]
    if candidate.startswith("server/"):
        return None
    if candidate.startswith(IGNORE_PREFIXES):
        return None
    if any(ch in candidate for ch in ("<", ">", "{", "}", "(", ")", "::", "=")):
        return None

    if candidate in ALLOWED_ROOT_FILES:
        return candidate
    if any(candidate.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        return candidate

    # Relative markdown links in the same folder, e.g. [x](FLOW_INTERACTION_SPEC.md)
    if "/" not in candidate and candidate.endswith(".md"):
        doc_parent = Path(doc_rel).parent
        return str((doc_parent / candidate).as_posix())

    return None


def _exists(path_str: str) -> bool:
    if path_str in ALLOWED_ROOT_FILES:
        return (ROOT / path_str).exists()
    if "*" in path_str:
        base = path_str.split("*", 1)[0].rstrip("/")
        return True if not base else (ROOT / base).exists()
    if path_str.endswith("/"):
        return (ROOT / path_str.rstrip("/")).is_dir()
    return (ROOT / path_str).exists()


def _skip_line(doc_rel: str, line: str, in_missing_section: bool) -> bool:
    if doc_rel != "Docs/README.md":
        return False
    if line.startswith("## "):
        return False
    # README intentionally contains non-existing examples in this section.
    return in_missing_section


def main() -> int:
    missing: list[tuple[str, int, str]] = []

    for doc_rel in CANONICAL_DOCS:
        doc_path = ROOT / doc_rel
        if not doc_path.exists():
            missing.append((doc_rel, 0, doc_rel))
            continue

        in_missing_section = False
        for idx, line in enumerate(doc_path.read_text(encoding="utf-8").splitlines(), start=1):
            if doc_rel == "Docs/README.md" and line.startswith("## "):
                in_missing_section = line.strip() == "## Отсутствующие документы"
            if _skip_line(doc_rel, line, in_missing_section):
                continue

            for raw in _iter_candidates(line):
                candidate = _normalize(raw, doc_rel)
                if not candidate:
                    continue
                if not _exists(candidate):
                    missing.append((doc_rel, idx, candidate))

    if missing:
        print("Broken documentation references detected:")
        for doc_rel, line_no, ref in missing:
            print(f"- {doc_rel}:{line_no} -> {ref}")
        return 1

    print("Documentation link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
