"""
Selectors: pure functions for checking state snapshots.

This module provides read-only selectors that extract boolean conditions
from Snapshot objects. All state access should go through selectors instead
of direct state inspection.

See .cursorrules section 21.x for architecture details.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal

from integration.core.state_manager import ApplicationStateManager, AppMode

class PermissionStatus(Enum):
    """Permission status values."""

    GRANTED = "granted"
    DENIED = "denied"
    PROMPT_BLOCKED = "prompt_blocked"


class DeviceStatus(Enum):
    """Device status values."""

    DEFAULT_OK = "default_ok"
    BUSY = "busy"


class NetworkStatus(Enum):
    """Network status values."""

    ONLINE = "online"
    OFFLINE = "offline"


# NOTE: AppMode is imported from state_manager to ensure a single source of truth.


@dataclass(frozen=True)
class Snapshot:
    """
    Immutable snapshot of system state axes.

    This is the single source of truth for decision-making. All selectors
    operate on Snapshot instances rather than accessing state directly.
    """

    # Permission axes
    perm_mic: PermissionStatus
    perm_screen: PermissionStatus
    perm_accessibility: PermissionStatus

    # Device axes
    device_input: DeviceStatus

    # Network axis
    network: NetworkStatus

    # Application state axes
    first_run: bool
    app_mode: AppMode

    # Restart state axis (Phase 2 - ADR-001)
    restart_pending: bool = False  # Default False for backward compatibility
    update_in_progress: bool = False  # Default False for backward compatibility


# Permission selectors


def mic_ready(s: Snapshot) -> bool:
    """Check if microphone permission is granted."""
    return s.perm_mic == PermissionStatus.GRANTED


def screen_ready(s: Snapshot) -> bool:
    """Check if screen capture permission is granted."""
    return s.perm_screen == PermissionStatus.GRANTED


def accessibility_ready(s: Snapshot) -> bool:
    """Check if accessibility permission is granted."""
    return s.perm_accessibility == PermissionStatus.GRANTED


def all_permissions_ready(s: Snapshot) -> bool:
    """Check if all critical permissions are granted."""
    return mic_ready(s) and screen_ready(s) and accessibility_ready(s)


# Device selectors


def device_idle(s: Snapshot) -> bool:
    """Check if input device is idle (not busy)."""
    return s.device_input == DeviceStatus.DEFAULT_OK


def device_busy(s: Snapshot) -> bool:
    """Check if input device is busy."""
    return s.device_input == DeviceStatus.BUSY


# Network selectors


def network_online(s: Snapshot) -> bool:
    """Check if network is online."""
    return s.network == NetworkStatus.ONLINE


def network_offline(s: Snapshot) -> bool:
    """Check if network is offline."""
    return s.network == NetworkStatus.OFFLINE


# Application state selectors


def is_first_run(s: Snapshot) -> bool:
    """Check if this is the first run of the application."""
    return s.first_run


def is_sleeping_mode(s: Snapshot) -> bool:
    """Check if application is in SLEEPING mode."""
    return s.app_mode == AppMode.SLEEPING


def is_listening_mode(s: Snapshot) -> bool:
    """Check if application is in LISTENING mode."""
    return s.app_mode == AppMode.LISTENING


def is_processing_mode(s: Snapshot) -> bool:
    """Check if application is in PROCESSING mode."""
    return s.app_mode == AppMode.PROCESSING


# Restart state selectors (Phase 2 - ADR-001)


def is_restart_pending(s: Snapshot) -> bool:
    """Check if application restart is pending after first-run permissions."""
    return s.restart_pending


def is_first_run_restart_pending(s: Snapshot) -> bool:
    """
    Check if this is first run AND restart is pending.

    This is the critical condition that blocks integration startup
    until the application restarts.
    """
    return s.first_run and s.restart_pending


# Composite selectors


def can_start_listening(s: Snapshot) -> bool:
    """
    Check if listening can be started (permissions + device + mode + not first_run).

    Блокирует активацию во время процедуры первого запуска (first_run).
    """
    return (
        not is_first_run(s)  # КРИТИЧНО: Блокируем активацию во время first_run
        and mic_ready(s)
        and device_idle(s)
        and (is_sleeping_mode(s) or is_listening_mode(s))
    )


def can_process_audio(s: Snapshot) -> bool:
    """Check if audio processing can proceed (permissions + network + mode)."""
    return (
        mic_ready(s)
        and network_online(s)
        and (is_listening_mode(s) or is_processing_mode(s))
    )


def should_degrade_offline(s: Snapshot) -> bool:
    """Check if processing should degrade due to offline network."""
    return network_offline(s) and is_processing_mode(s)



# Service flags (thin accessors; shadow-mode during migration)


def is_update_in_progress(state_manager: ApplicationStateManager) -> bool:
    """Check if an application update is currently in progress.

    Source of truth is UpdaterIntegration which mirrors its state to state_manager.
    This selector exists to prevent direct state access in integrations.
    """
    try:
        return bool(state_manager.get_state_data("update_in_progress", False))
    except Exception:
        return False


def create_snapshot_from_state(
    state_manager: ApplicationStateManager,
    *,
    default_permissions: bool = True,
    default_device: DeviceStatus = DeviceStatus.DEFAULT_OK,
    default_network: NetworkStatus = NetworkStatus.ONLINE,
) -> Snapshot:
    """
    Create a Snapshot from ApplicationStateManager state.
    
    This helper function is allowed to read state_manager directly because
    it's in selectors.py (allowed exception per architecture rules).
    
    Args:
        state_manager: ApplicationStateManager instance
        default_permissions: Whether to assume all permissions granted (default True)
        default_device: Default device status
        default_network: Default network status
        
    Returns:
        Snapshot with current system state
    """
    # Get app mode
    try:
        current_mode = state_manager.get_current_mode()
        if not isinstance(current_mode, AppMode):
            try:
                current_mode = AppMode(current_mode)  # type: ignore[arg-type]
            except Exception:
                current_mode = AppMode.SLEEPING
    except Exception:
        current_mode = AppMode.SLEEPING
    
    # Get first_run status
    first_run = bool(state_manager.get_state_data("permissions_restart_pending", False)) or False
    # TODO: Get actual first_run flag from FirstRunPermissionsIntegration if needed
    
    # Get restart_pending status
    restart_pending = bool(state_manager.get_state_data("permissions_restart_pending", False))
    
    # Permission statuses (default to GRANTED, can be overridden by actual checks)
    perm_mic = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    perm_screen = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    perm_accessibility = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    
    # TODO: Get actual permission statuses from PermissionsIntegration if available
    
    # Get update_in_progress status
    update_in_progress = is_update_in_progress(state_manager)
    
    return Snapshot(
        perm_mic=perm_mic,
        perm_screen=perm_screen,
        perm_accessibility=perm_accessibility,
        device_input=default_device,
        network=default_network,
        first_run=first_run,
        app_mode=current_mode,
        restart_pending=restart_pending,
        update_in_progress=update_in_progress,
    )


