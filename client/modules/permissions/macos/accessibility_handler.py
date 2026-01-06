"""
Accessibility and Input Monitoring permissions helper for macOS.

UI-ONLY HELPER: Opens System Settings and provides instructions.
For permission CHECKS, use check_accessibility_status() from status_checker.py.
"""

import logging
import subprocess
from typing import Dict, Any

logger = logging.getLogger(__name__)


class AccessibilityHandler:
    """Accessibility permissions UI helper for macOS.
    
    NOTE: This class is for UI actions only (open_settings, get_instructions).
    For permission CHECKS, use check_accessibility_status() from 
    modules.permissions.first_run.status_checker.
    """
    
    def __init__(self):
        try:
            from Foundation import NSBundle
            self.bundle_id = NSBundle.mainBundle().bundleIdentifier() or "com.nexy.assistant"
            logger.debug(f"🔍 AccessibilityHandler detected bundle_id: {self.bundle_id}")
        except Exception:
            self.bundle_id = "com.nexy.assistant"
    
    def check_accessibility_permission(self) -> bool:
        """Check whether the app is trusted for Accessibility.
        
        ВАЖНО: Делегирует проверку в check_accessibility_status() — единственный
        источник истины для Accessibility проверок.
        """
        try:
            from modules.permissions.first_run.status_checker import (
                check_accessibility_status,
                PermissionStatus
            )
            status = check_accessibility_status()
            trusted = status == PermissionStatus.GRANTED
            
            if trusted:
                logger.info("✅ Accessibility permission granted")
            else:
                logger.warning("⚠️ Accessibility permission not granted")
            
            return trusted
            
        except Exception as e:
            logger.warning(f"⚠️ Error checking accessibility permission: {e}")
            return False
    
    def check_input_monitoring_permission(self) -> bool:
        """Check whether the app is trusted for Input Monitoring."""
        try:
            # Проверяем через tccutil
            result = subprocess.run(
                ['tccutil', 'check', 'ListenEvent', self.bundle_id],
                capture_output=True,
                text=True,
                timeout=5,
            )
            
            granted = result.returncode == 0
            
            if granted:
                logger.info("✅ Input Monitoring permission granted")
            else:
                logger.warning("⚠️ Input Monitoring permission not granted")
            
            return granted
            
        except Exception as e:
            logger.error(f"❌ Error checking input monitoring permission: {e}")
            return False
    
    def open_accessibility_settings(self) -> bool:
        """Open System Settings on the Accessibility pane."""
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'],
                check=True,
            )
            logger.info("✅ Accessibility settings opened")
            return True
        except Exception as e:
            logger.error(f"❌ Error opening Accessibility settings: {e}")
            return False
    
    def open_input_monitoring_settings(self) -> bool:
        """Open System Settings on the Input Monitoring pane."""
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent'],
                check=True,
            )
            logger.info("✅ Input Monitoring settings opened")
            return True
        except Exception as e:
            logger.error(f"❌ Error opening Input Monitoring settings: {e}")
            return False
    
    def get_permission_status(self) -> Dict[str, Any]:
        return {
            'accessibility': self.check_accessibility_permission(),
            'input_monitoring': self.check_input_monitoring_permission(),
            'bundle_id': self.bundle_id
        }
    
    def get_instructions(self) -> str:
        """Return human-readable instructions for granting permissions."""
        return (
            "🔧 ACCESSIBILITY & INPUT MONITORING PERMISSIONS\n\n"
            "1. Accessibility (required to monitor the keyboard):\n"
            "   - Open System Settings\n"
            "   - Go to Privacy & Security\n"
            "   - Select Accessibility\n"
            "   - Enable the toggle for Nexy AI Assistant\n\n"
            "2. Input Monitoring (required to capture key presses):\n"
            "   - Open System Settings\n"
            "   - Go to Privacy & Security\n"
            "   - Select Input Monitoring\n"
            "   - Enable the toggle for Nexy AI Assistant\n\n"
            "Quick links:\n"
            'open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"\n'
            'open "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"\n'
        )
