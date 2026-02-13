"""Runtime module version helpers."""

from __future__ import annotations

import os
from pathlib import Path


def get_module_version() -> str:
    """Resolve server version from VERSION file with env fallback."""
    version_file = Path(__file__).resolve().parents[2] / "VERSION"
    if version_file.exists():
        version = version_file.read_text(encoding="utf-8").strip()
        if version:
            return version

    env_version = os.getenv("SERVER_VERSION", "").strip()
    if env_version:
        return env_version

    return "0.0.0.0"

