"""
Environment detection helpers.

Lightweight (no config loader) to avoid heavy imports in early/critical paths.
"""

from __future__ import annotations

import os
from pathlib import Path
import sys


def is_production_env() -> bool:
    """Return True when running in production environment."""
    env_candidate = os.getenv("NEXY_ENV") or os.getenv("NEXY_ENVIRONMENT")
    if env_candidate:
        normalized = env_candidate.strip().lower()
        if normalized in {"prod", "production"}:
            return True
        if normalized in {"dev", "development"}:
            return False
        # Unknown custom env: treat as non-production unless explicitly prod.
        return False

    if getattr(sys, "frozen", False):
        return True

    argv_path = Path(sys.argv[0]).resolve()
    if ".app/Contents/MacOS" in str(argv_path):
        return True

    return False
