"""
PyInstaller runtime hook ensuring AppKit symbols are available in Foundation
before any PyObjC-based modules (e.g. rumps) are imported.
"""

import logging

logger = logging.getLogger(__name__)


def _apply_fix():
    try:
        from integration.utils.macos_pyobjc_fix import fix_pyobjc_foundation
    except Exception as import_error:  # pragma: no cover - defensive, should not happen
        logger.warning("⚠️ Unable to import macOS PyObjC fix module: %s", import_error)
        return

    try:
        fix_pyobjc_foundation()
    except Exception as exc:  # pragma: no cover - guard against unexpected runtime issues
        logger.warning("⚠️ Failed to apply PyObjC Foundation fix: %s", exc)


_apply_fix()

