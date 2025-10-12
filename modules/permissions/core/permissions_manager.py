"""
Core permission manager for macOS.
"""

import asyncio
import logging
import time
from typing import Dict, Optional, Callable

from .types import (
    PermissionType,
    PermissionStatus,
    PermissionInfo,
    PermissionResult,
    PermissionEvent,
    PermissionConfig,
    PermissionManagerState,
    PermissionState,
)
from .config import PermissionConfigManager
from ..macos.permission_handler import MacOSPermissionHandler

logger = logging.getLogger(__name__)


class PermissionManager:
    """Coordinates permission checks and requests on macOS."""

    def __init__(self, config_path: str = "config/permissions_config.yaml"):
        self.config_manager = PermissionConfigManager(config_path)
        self.config: Optional[PermissionConfig] = None
        self.state = PermissionManagerState()
        self.macos_handler = MacOSPermissionHandler()
        self.is_initialized = False
        self.is_monitoring = False
        self._monitoring_task: Optional[asyncio.Task] = None

    async def initialize(self) -> bool:
        """Initialise configuration and cached permission state."""
        try:
            logger.info("🔧 Initialising PermissionManager")

            self.config = self.config_manager.get_config()
            self.state.config = self.config

            await self._initialise_permission_state()

            self.is_initialized = True
            logger.info("✅ PermissionManager initialised")
            return True

        except Exception as exc:
            logger.error("❌ Failed to initialise PermissionManager: %s", exc)
            return False

    async def _initialise_permission_state(self):
        """Create PermissionInfo entries for every known permission type."""
        descriptions = {
            PermissionType.MICROPHONE: "Microphone access is required for speech recognition.",
            PermissionType.SCREEN_CAPTURE: "Screen recording is required for screenshot capture.",
            PermissionType.CAMERA: "Camera access is required for video capture.",
            PermissionType.NETWORK: "Network access is required for service communication.",
            PermissionType.NOTIFICATIONS: "Notifications keep the user informed about events.",
            PermissionType.ACCESSIBILITY: "Accessibility access allows keyboard monitoring.",
            PermissionType.INPUT_MONITORING: "Input monitoring is required to detect key presses.",
        }

        timestamp = time.time()
        for perm_type in PermissionType:
            info = PermissionInfo(
                permission_type=perm_type,
                status=PermissionStatus.NOT_DETERMINED,
                granted=False,
                message=descriptions.get(perm_type, ""),
                last_checked=timestamp,
            )
            self.state.set_permission(perm_type, info)

    async def check_permission(self, permission_type: PermissionType) -> PermissionResult:
        """Check a single permission by delegating to the macOS handler."""
        try:
            logger.info("🔍 Checking permission: %s", permission_type.value)

            if permission_type == PermissionType.MICROPHONE:
                result = await self.macos_handler.check_microphone_permission()
            elif permission_type == PermissionType.SCREEN_CAPTURE:
                result = await self.macos_handler.check_screen_capture_permission()
            elif permission_type == PermissionType.CAMERA:
                result = await self.macos_handler.check_camera_permission()
            elif permission_type == PermissionType.NETWORK:
                result = await self.macos_handler.check_network_permission()
            elif permission_type == PermissionType.NOTIFICATIONS:
                result = await self.macos_handler.check_notifications_permission()
            elif permission_type == PermissionType.ACCESSIBILITY:
                result = await self.macos_handler.check_accessibility_permission()
            elif permission_type == PermissionType.INPUT_MONITORING:
                result = await self.macos_handler.check_input_monitoring_permission()
            else:
                result = PermissionResult(
                    success=False,
                    permission=permission_type,
                    status=PermissionStatus.ERROR,
                    message=f"Unknown permission type: {permission_type}",
                )

            if result.success:
                await self._update_permission_status(permission_type, result.status)

            logger.info("✅ Permission %s: %s", permission_type.value, result.status.value)
            return result

        except Exception as exc:
            logger.error("❌ Failed to check permission %s: %s", permission_type.value, exc)
            return PermissionResult(
                success=False,
                permission=permission_type,
                status=PermissionStatus.ERROR,
                message=f"Error checking permission: {exc}",
                error=exc,
            )

    async def check_all_permissions(self) -> Dict[PermissionType, PermissionResult]:
        """Check every permission type in parallel."""
        logger.info("🔍 Checking all permissions")

        results: Dict[PermissionType, PermissionResult] = {}
        tasks = {perm: asyncio.create_task(self.check_permission(perm)) for perm in PermissionType}

        for perm_type, task in tasks.items():
            try:
                results[perm_type] = await task
            except Exception as exc:
                logger.error("❌ Failed to check %s: %s", perm_type.value, exc)
                results[perm_type] = PermissionResult(
                    success=False,
                    permission=perm_type,
                    status=PermissionStatus.ERROR,
                    message=f"Error: {exc}",
                    error=exc,
                )

        logger.info("✅ Permission check completed")
        return results

    async def request_permission(self, permission_type: PermissionType) -> PermissionResult:
        """Request a permission if the operating system allows prompting."""
        try:
            logger.info("📝 Requesting permission: %s", permission_type.value)

            current_result = await self.check_permission(permission_type)

            if current_result.status == PermissionStatus.GRANTED:
                logger.info("✅ Permission %s already granted", permission_type.value)
                return current_result

            if current_result.status == PermissionStatus.DENIED:
                await self._show_permission_instructions(permission_type)
                return current_result

            if current_result.status == PermissionStatus.NOT_DETERMINED:
                await self._show_permission_dialog(permission_type)
                await asyncio.sleep(2)
                return await self.check_permission(permission_type)

            return current_result

        except Exception as exc:
            logger.error("❌ Failed to request permission %s: %s", permission_type.value, exc)
            return PermissionResult(
                success=False,
                permission=permission_type,
                status=PermissionStatus.ERROR,
                message=f"Error requesting permission: {exc}",
                error=exc,
            )

    async def request_required_permissions(self) -> Dict[PermissionType, PermissionResult]:
        """Request all permissions marked as required in the configuration."""
        logger.info("📝 Requesting required permissions")

        results: Dict[PermissionType, PermissionResult] = {}
        for perm_type in self.config.required_permissions:
            result = await self.request_permission(perm_type)
            results[perm_type] = result

            if result.status != PermissionStatus.GRANTED:
                await self._show_permission_instructions(perm_type)

        return results

    async def _update_permission_status(self, permission_type: PermissionType, new_status: PermissionStatus):
        """Update cached state and propagate an event."""
        try:
            info = self.state.get_permission(permission_type)
            if info is None:
                return

            old_status = info.status
            info.status = new_status
            info.last_checked = time.time()

            event = PermissionEvent(
                event_type="status_changed",
                permission=permission_type,
                status=new_status,
                message=f"Status changed from {old_status.value} to {new_status.value}",
                timestamp=time.time(),
            )

            await self.state.notify_callbacks(event)
            logger.info("🔄 Permission %s: %s → %s", permission_type.value, old_status.value, new_status.value)

        except Exception as exc:
            logger.error("❌ Failed to update status for %s: %s", permission_type.value, exc)

    async def _show_permission_instructions(self, permission_type: PermissionType):
        """Print instructions explaining how to grant the specified permission."""
        try:
            instructions = self.macos_handler.get_permission_instructions(permission_type)

            print(f"\n{'=' * 60}")
            print(f"🔐 PERMISSION: {permission_type.value.upper()}")
            print(f"{'=' * 60}")
            print(instructions)
            print(f"{'=' * 60}\n")

        except Exception as exc:
            logger.error("❌ Failed to show instructions for %s: %s", permission_type.value, exc)

    async def _show_permission_dialog(self, permission_type: PermissionType):
        """Fallback that reuses instructions—macOS does not allow custom prompts."""
        try:
            await self._show_permission_instructions(permission_type)
        except Exception as exc:
            logger.error("❌ Failed to show permission dialog for %s: %s", permission_type.value, exc)

    async def start_monitoring(self):
        """Begin periodic permission checks."""
        if self.is_monitoring:
            logger.warning("Permission monitoring already running")
            return

        if not self.is_initialized:
            logger.error("PermissionManager not initialised")
            return

        logger.info("🔄 Starting permission monitoring")
        self.is_monitoring = True
        self._monitoring_task = asyncio.create_task(self._monitoring_loop())

    async def stop_monitoring(self):
        """Stop periodic permission checks."""
        if not self.is_monitoring:
            return

        logger.info("⏹️ Stopping permission monitoring")
        self.is_monitoring = False

        if self._monitoring_task:
            self._monitoring_task.cancel()
            try:
                await self._monitoring_task
            except asyncio.CancelledError:
                pass

    async def _monitoring_loop(self):
        """Background loop that polls permissions according to the config."""
        try:
            while self.is_monitoring:
                await self.check_all_permissions()
                await asyncio.sleep(self.config.check_interval)

            logger.info("Permission monitoring stopped")

        except asyncio.CancelledError:
            logger.info("Permission monitoring cancelled")
        except Exception as exc:
            logger.error("❌ Permission monitoring failed: %s", exc)

    def add_callback(self, callback: Callable[[PermissionEvent], None]):
        """Compatibility placeholder (callbacks are not yet supported)."""
        logger.warning("add_callback is not implemented")

    async def get_permission_status(self, permission_type: PermissionType) -> Optional[PermissionInfo]:
        """Return cached information for a single permission."""
        return self.state.get_permission(permission_type)

    async def get_all_permissions_status(self) -> PermissionState:
        """Return the full permission state."""
        return self.state

    async def are_required_permissions_granted(self) -> bool:
        """Check whether all required permissions are currently granted."""
        return all(self.state.is_granted(perm) for perm in self.config.required_permissions)

    async def cleanup(self):
        """Stop monitoring and reset internal state."""
        try:
            await self.stop_monitoring()
            self.is_initialized = False
            logger.info("✅ PermissionManager cleaned up")
        except Exception as exc:
            logger.error("❌ Failed to clean up PermissionManager: %s", exc)
