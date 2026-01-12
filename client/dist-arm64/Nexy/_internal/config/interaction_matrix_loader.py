"""
Helpers for loading the interaction matrix in development/diagnostic modes.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from .unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

DEV_ENVIRONMENTS = {"development", "dev", "diagnostics", "diag"}


def load_interaction_matrix(dev_only: bool = True, *, path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load the interaction_matrix.yaml file. When `dev_only` is True (default),
    the matrix is only returned for development/diagnostic environments to
    avoid impacting production behaviour while the rules стабилизируются.
    """

    loader = UnifiedConfigLoader.get_instance()
    environment = loader.get_environment()
    if dev_only and environment not in DEV_ENVIRONMENTS:
        logger.debug("Interaction matrix skipped (environment=%s)", environment)
        return {}

    matrix_path = path or Path(__file__).resolve().parent / "interaction_matrix.yaml"
    if not matrix_path.exists():
        logger.debug("Interaction matrix file not found at %s", matrix_path)
        return {}

    try:
        with matrix_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
            if not isinstance(data, dict):
                logger.warning("Interaction matrix has unexpected structure (%s)", type(data))
                return {}
            return data
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.warning("Failed to load interaction matrix: %s", exc)
        return {}
