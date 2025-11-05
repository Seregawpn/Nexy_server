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

def _activate_nsapplication():
    """
    CRITICAL: Activate NSApplication for LSUIElement applications.
    Without this, menu bar icon doesn't appear when launched from .app on macOS Sequoia.
    Must be called BEFORE creating rumps.App and NSStatusItem.
    """
    import sys
    try:
        sys.stderr.write("[NEXY_INIT] Activating NSApplication for menu bar app...\n")
        sys.stderr.flush()
        import AppKit
        app = AppKit.NSApplication.sharedApplication()
        # NSApplicationActivationPolicyAccessory (hide from Dock, show in menu bar)
        app.setActivationPolicy_(AppKit.NSApplicationActivationPolicyAccessory)
        # ADDITIONALLY: Force activate the app to ensure menu bar items are visible
        app.activateIgnoringOtherApps_(True)
        sys.stderr.write("[NEXY_INIT] SUCCESS: NSApplication activated for menu bar app\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"[NEXY_INIT] ERROR: NSApplication activation failed: {e}\n")
        sys.stderr.flush()

_apply_fix()
_activate_nsapplication()

