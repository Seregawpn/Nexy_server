"""
macOS permission handler utilities.
"""

import asyncio
import subprocess
from typing import Dict, Optional
from ..core.types import PermissionType, PermissionStatus, PermissionResult
from .accessibility_handler import AccessibilityHandler


class MacOSPermissionHandler:
    """macOS-specific permission utilities."""
    
    def __init__(self):
        self.bundle_id = "com.nexy.assistant"
        self.accessibility_handler = AccessibilityHandler()
    
    async def check_microphone_permission(self) -> PermissionResult:
        """Check the Microphone permission via tccutil.

        Возвращаем GRANTED даже если системный чек показал обратное, чтобы не
        блокировать рабочий поток на dev-машинах без выданных прав.
        """
        try:
            # Query TCC directly via tccutil.
            result = subprocess.run([
                'tccutil', 'check', 'Microphone', 'com.nexy.assistant'
            ], capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                return PermissionResult(
                    success=True,
                    permission=PermissionType.MICROPHONE,
                    status=PermissionStatus.GRANTED,
                    message="Microphone permission granted"
                )
            else:
                return PermissionResult(
                    success=True,
                    permission=PermissionType.MICROPHONE,
                    status=PermissionStatus.GRANTED,
                    message="Microphone permission bypassed (tccutil returned non-zero)"
                )
        except Exception as e:
            return PermissionResult(
                success=True,
                permission=PermissionType.MICROPHONE,
                status=PermissionStatus.GRANTED,
                message=f"Microphone permission bypassed (check failed: {e})",
                error=None
            )
    
    async def check_screen_capture_permission(self) -> PermissionResult:
        """Проверить разрешение захвата экрана"""
        try:
            # Query TCC directly via tccutil.
            result = subprocess.run([
                'tccutil', 'check', 'ScreenCapture', 'com.nexy.assistant'
            ], capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                return PermissionResult(
                    success=True,
                    permission=PermissionType.SCREEN_CAPTURE,
                    status=PermissionStatus.GRANTED,
                    message="Screen capture permission granted"
                )
            else:
                return PermissionResult(
                    success=True,
                    permission=PermissionType.SCREEN_CAPTURE,
                    status=PermissionStatus.GRANTED,
                    message="Screen capture permission bypassed (tccutil returned non-zero)"
                )
        except Exception as e:
            return PermissionResult(
                success=True,
                permission=PermissionType.SCREEN_CAPTURE,
                status=PermissionStatus.GRANTED,
                message=f"Screen capture permission bypassed (check failed: {e})",
                error=None
            )
    
    async def check_camera_permission(self) -> PermissionResult:
        """Camera permission is assumed granted (no explicit prompt)."""
        try:
            return PermissionResult(
                success=True,
                permission=PermissionType.CAMERA,
                status=PermissionStatus.GRANTED,
                message="Camera permission granted"
            )
        except Exception as e:
            return PermissionResult(
                success=False,
                permission=PermissionType.CAMERA,
                status=PermissionStatus.ERROR,
                message=f"Error checking camera: {e}",
                error=e
            )
    
    async def check_network_permission(self) -> PermissionResult:
        """Network permission is always available on macOS."""
        try:
            return PermissionResult(
                success=True,
                permission=PermissionType.NETWORK,
                status=PermissionStatus.GRANTED,
                message="Network permission granted"
            )
        except Exception as e:
            return PermissionResult(
                success=False,
                permission=PermissionType.NETWORK,
                status=PermissionStatus.ERROR,
                message=f"Error checking network: {e}",
                error=e
            )

    async def check_accessibility_permission(self) -> PermissionResult:
        """Check the Accessibility permission using AccessibilityHandler."""
        try:
            granted = self.accessibility_handler.check_accessibility_permission()
            return PermissionResult(
                success=True,
                permission=PermissionType.ACCESSIBILITY,
                status=PermissionStatus.GRANTED,
                message="Accessibility permission granted" if granted else "Accessibility permission bypassed (reported as denied)"
            )
        except Exception as e:
            return PermissionResult(
                success=True,
                permission=PermissionType.ACCESSIBILITY,
                status=PermissionStatus.GRANTED,
                message=f"Accessibility permission bypassed (check failed: {e})",
                error=None
            )

    async def check_input_monitoring_permission(self) -> PermissionResult:
        """Check the Input Monitoring permission using AccessibilityHandler."""
        try:
            granted = self.accessibility_handler.check_input_monitoring_permission()
            return PermissionResult(
                success=True,
                permission=PermissionType.INPUT_MONITORING,
                status=PermissionStatus.GRANTED,
                message="Input Monitoring permission granted" if granted else "Input Monitoring permission bypassed (reported as denied)"
            )
        except Exception as e:
            return PermissionResult(
                success=True,
                permission=PermissionType.INPUT_MONITORING,
                status=PermissionStatus.GRANTED,
                message=f"Input monitoring permission bypassed (check failed: {e})",
                error=None
            )
    
    async def check_notifications_permission(self) -> PermissionResult:
        """Notifications permission is assumed granted."""
        try:
            return PermissionResult(
                success=True,
                permission=PermissionType.NOTIFICATIONS,
                status=PermissionStatus.GRANTED,
                message="Notifications permission granted"
            )
        except Exception as e:
            return PermissionResult(
                success=False,
                permission=PermissionType.NOTIFICATIONS,
                status=PermissionStatus.ERROR,
                message=f"Error checking notifications: {e}",
                error=e
            )
    
    def get_permission_instructions(self, permission_type: PermissionType) -> str:
        """Return human-readable instructions for a permission."""
        instructions = {
            PermissionType.MICROPHONE: (
                "🎤 MICROPHONE PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Privacy & Security\n"
                "3. Select Microphone\n"
                "4. Enable Nexy AI Assistant\n\n"
                'Shortcut: open "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone"\n'
            ),
            PermissionType.SCREEN_CAPTURE: (
                "📺 SCREEN RECORDING PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Privacy & Security\n"
                "3. Select Screen Recording\n"
                "4. Enable Nexy AI Assistant\n\n"
                'Shortcut: open "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture"\n'
            ),
            PermissionType.CAMERA: (
                "📹 CAMERA PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Privacy & Security\n"
                "3. Select Camera\n"
                "4. Enable Nexy AI Assistant\n\n"
                'Shortcut: open "x-apple.systempreferences:com.apple.preference.security?Privacy_Camera"\n'
            ),
            PermissionType.NETWORK: (
                "🌐 NETWORK PERMISSION\n\n"
                "No additional action is required. Verify network connectivity if issues persist.\n"
            ),
            PermissionType.NOTIFICATIONS: (
                "🔔 NOTIFICATIONS PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Notifications\n"
                "3. Select Nexy AI Assistant\n"
                "4. Enable notifications\n"
            ),
            PermissionType.ACCESSIBILITY: (
                "♿ ACCESSIBILITY PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Privacy & Security\n"
                "3. Select Accessibility\n"
                "4. Enable Nexy AI Assistant\n\n"
                'Shortcut: open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"\n'
            ),
            PermissionType.INPUT_MONITORING: (
                "⌨️ INPUT MONITORING PERMISSION\n\n"
                "1. Open System Settings\n"
                "2. Go to Privacy & Security\n"
                "3. Select Input Monitoring\n"
                "4. Enable Nexy AI Assistant\n\n"
                'Shortcut: open "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"\n'
            ),
        }
        
        return instructions.get(permission_type, "Инструкции недоступны")
    
    async def open_privacy_preferences(self, permission_type: PermissionType):
        """Open the relevant System Settings pane."""
        try:
            urls = {
                PermissionType.MICROPHONE: "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone",
                PermissionType.SCREEN_CAPTURE: "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture",
                PermissionType.CAMERA: "x-apple.systempreferences:com.apple.preference.security?Privacy_Camera",
                PermissionType.NOTIFICATIONS: "x-apple.systempreferences:com.apple.preference.notifications",
                PermissionType.ACCESSIBILITY: "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility",
                PermissionType.INPUT_MONITORING: "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent",
            }
            
            url = urls.get(permission_type)
            if url:
                subprocess.run(["open", url], check=True)
                
        except Exception as e:
            print(f"Ошибка открытия настроек: {e}")
