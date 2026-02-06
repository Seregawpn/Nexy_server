"""
Permission System V2 - Settings Navigator

Opens System Settings to the appropriate privacy page.
"""

from __future__ import annotations

import logging
import subprocess

logger = logging.getLogger(__name__)

SETTINGS_URLS: dict[str, str] = {
    "accessibility": "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility",
    "input_monitoring": "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent",
    "screen_capture": "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture",
    "microphone": "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone",
    "full_disk_access": "x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles",
    "contacts": "x-apple.systempreferences:com.apple.preference.security?Privacy_Contacts",
    "privacy_and_security": "x-apple.systempreferences:com.apple.preference.security",
}


class SettingsNavigator:
    """Opens System Settings to the requested privacy page."""

    def open(self, target: str) -> bool:
        """
        Open System Settings to the specified target page.
        
        Args:
            target: One of the SETTINGS_URLS keys
            
        Returns:
            True if the open command succeeded
        """
        url = SETTINGS_URLS.get(target, SETTINGS_URLS["privacy_and_security"])
        
        try:
            result = subprocess.run(
                ["open", url],
                check=False,
                capture_output=True,
                timeout=5.0,
            )
            if result.returncode == 0:
                logger.info("[SETTINGS_NAV] Opened Settings: %s", target)
                return True
            else:
                logger.warning(
                    "[SETTINGS_NAV] Failed to open Settings: %s (returncode=%d)",
                    target,
                    result.returncode,
                )
                return False
        except subprocess.TimeoutExpired:
            logger.warning("[SETTINGS_NAV] Timeout opening Settings: %s", target)
            return False
        except Exception as e:
            logger.error("[SETTINGS_NAV] Error opening Settings: %s - %s", target, e)
            return False
