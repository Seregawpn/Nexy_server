"""
Accessibility and Input Monitoring permissions helper for macOS.
Checks current status and opens System Settings when needed.
"""

import logging
import subprocess
from typing import Dict, Any

logger = logging.getLogger(__name__)

class AccessibilityHandler:
    """Accessibility permissions helper for macOS."""
    
    def __init__(self):
        self.bundle_id = "com.nexy.assistant"
    
    def _ax_trusted_public_check(self, *, prompt: bool = False) -> bool:
        """
        Invoke the public Quartz API (AXIsProcessTrustedWithOptions).
        `prompt` controls whether macOS should show the system dialog.
        """
        try:
            from ApplicationServices import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
            from Foundation import NSDictionary, NSNumber
        except ImportError as import_err:
            # Явный WARN лог при ImportError
            logger.warning(f"⚠️ Quartz/AX API недоступен: {import_err}")
            logger.warning(f"⚠️ Проверьте, что PyObjC-framework-Quartz установлен")
            logger.warning("⚠️ Считаем, что разрешение не выдано")
            return False

        try:
            options = NSDictionary.dictionaryWithObject_forKey_(
            NSNumber.numberWithBool_(bool(prompt)),
            kAXTrustedCheckOptionPrompt,
            )
            return bool(AXIsProcessTrustedWithOptions(options))
        except Exception as e:
            logger.error(f"❌ Ошибка вызова AXIsProcessTrustedWithOptions: {e}")
            return False
        except ImportError as import_err:
            logger.warning(f"⚠️ Quartz/AX API недоступен: {import_err}")
            logger.warning(f"⚠️ Проверьте, что PyObjC-framework-Quartz установлен")
            logger.warning("⚠️ Считаем, что разрешение не выдано")
            return False

    def check_accessibility_permission(self) -> bool:
        """Check whether the app is trusted for Accessibility using only public APIs."""
        try:
            trusted = self._ax_trusted_public_check(prompt=False)

            if trusted:
                logger.info("✅ Accessibility permission granted (public API)")
            else:
                logger.warning("⚠️ Accessibility permission not granted (public API)")

            return trusted

        except Exception as e:
            logger.error(f"❌ Error checking accessibility permission: {e}")
            # Возвращаем False, чтобы другие компоненты попытались запросить доступ
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
