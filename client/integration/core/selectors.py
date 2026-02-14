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
from typing import Any

from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)

from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager

# Import AppMode with fallback mechanism (same as state_manager.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception as e:
    # Fallback: explicit modules path if repository layout is used
    logger.debug(f"Failed to import AppMode from mode_management, using modules.mode_management: {e}")
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

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


class WhatsappStatus(Enum):
    """Whatsapp status values."""
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    QR_REQUIRED = "qr_required"


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
    
    # Whatsapp status axis
    whatsapp_status: WhatsappStatus = WhatsappStatus.DISCONNECTED


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


def missing_any_permissions(s: Snapshot) -> bool:
    """Check if any critical permissions are missing."""
    return not all_permissions_ready(s)


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


# Whatsapp selectors

def is_whatsapp_qr_required(s: Snapshot) -> bool:
    """Check if WhatsApp requires QR scan."""
    return s.whatsapp_status == WhatsappStatus.QR_REQUIRED


# Restart state selectors (DEPRECATED - Phase 2 cleanup)


def is_restart_pending(s: Snapshot) -> bool:
    """
    DEPRECATED: Перезапуск теперь происходит автоматически в FirstRunPermissionsIntegration.
    Используйте is_first_run_in_progress() вместо этого.
    """
    import warnings
    warnings.warn(
        "is_restart_pending is deprecated. Use is_first_run_in_progress() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return s.restart_pending


def is_first_run_restart_pending(s: Snapshot) -> bool:
    """
    DEPRECATED: Перезапуск теперь происходит автоматически в FirstRunPermissionsIntegration.
    Используйте is_first_run_in_progress() вместо этого.
    """
    import warnings
    warnings.warn(
        "is_first_run_restart_pending is deprecated. Use is_first_run_in_progress() instead.",
        DeprecationWarning,
        stacklevel=2
    )
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
        return bool(state_manager.get_state_data(StateKeys.UPDATE_IN_PROGRESS, False))
    except Exception as e:
        logger.debug(f"Failed to get update_in_progress state: {e}")
        return False


def is_restart_completed_fallback(state_manager: ApplicationStateManager) -> bool:
    """
    DEPRECATED: Больше не используется — перезапуск происходит автоматически.
    Всегда возвращает False.
    """
    import warnings
    warnings.warn(
        "is_restart_completed_fallback is deprecated and always returns False.",
        DeprecationWarning,
        stacklevel=2
    )
    return False


# ==============================================================================
# Direct State Accessors (REQ-004 compliant)
# ==============================================================================
# These functions provide centralized access to frequently-used state values.
# All integrations should use these instead of direct state_manager.get_* calls.


def is_valid_session_id(session_id: object) -> bool:
    """Validate session_id is a uuid4 string."""
    if not isinstance(session_id, str):
        return False
    try:
        import uuid
        parsed = uuid.UUID(session_id, version=4)
        return str(parsed) == session_id
    except Exception as e:
        logger.debug(f"Session ID validation failed for '{session_id}': {e}")
        return False


def get_current_session_id(state_manager: ApplicationStateManager) -> str | None:
    """Get current session ID.
    
    Returns the active session ID or None if no session is active.
    This is the single source of truth for session tracking.
    """
    try:
        session_id = state_manager.get_current_session_id()
        return session_id if is_valid_session_id(session_id) else None
    except Exception as e:
        logger.debug(f"Failed to get current session ID: {e}")
        return None


def get_current_mode(state_manager: ApplicationStateManager) -> AppMode:
    """Get current application mode.
    
    Returns the current AppMode, defaulting to SLEEPING if unavailable.
    """
    try:
        mode = state_manager.get_current_mode()
        if isinstance(mode, AppMode):
            return mode
        return AppMode(mode)  # type: ignore[arg-type]
    except Exception as e:
        logger.debug(f"Failed to get current mode, defaulting to SLEEPING: {e}")
        return AppMode.SLEEPING


def get_state_value(state_manager: ApplicationStateManager, key: str, default: Any = None) -> Any:
    """Read state_data via centralized selector access."""
    return state_manager.get_state_data(key, default)


def is_ptt_pressed(state_manager: ApplicationStateManager) -> bool:
    """Check if PTT (Push-To-Talk) button is currently pressed.
    
    Used by input processing and voice recognition integrations.
    """
    try:
        return bool(state_manager.get_state_data(StateKeys.PTT_PRESSED, False))
    except Exception:
        # High frequency check, keep silent unless debugging needed
        return False


def is_first_run_in_progress(state_manager: ApplicationStateManager) -> bool:
    """Check if first-run flow is currently in progress.
    
    Used to block certain operations during the permission grant flow.
    """
    try:
        return bool(state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, False))
    except Exception as e:
        logger.debug(f"Failed to get first_run_in_progress state: {e}")
        return False


def has_active_session(state_manager: ApplicationStateManager) -> bool:
    """Check if there is an active session.
    
    Returns True if session_id is not None.
    """
    return get_current_session_id(state_manager) is not None


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
    except Exception as e:
        logger.debug(f"Snapshot creation: failed to get app mode: {e}")
        current_mode = AppMode.SLEEPING
    
    # Get first_run status (explicit state only; SoT synced from ledger)
    try:
        first_run_required = state_manager.get_state_data(StateKeys.FIRST_RUN_REQUIRED, None)
    except Exception as e:
        logger.debug(f"Snapshot creation: failed to get first_run_required: {e}")
        first_run_required = None
    first_run = bool(first_run_required) if first_run_required is not None else False

    # Get restart_pending status
    restart_pending = bool(state_manager.get_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, False))
    
    # Permission statuses (default to GRANTED, can be overridden by actual checks)
    perm_mic = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    perm_screen = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    perm_accessibility = PermissionStatus.GRANTED if default_permissions else PermissionStatus.DENIED
    
    # TODO: Get actual permission statuses from PermissionsIntegration if available
    
    # Get network status (single state axis owned by NetworkManagerIntegration).
    try:
        raw_network = state_manager.get_state_data(StateKeys.NETWORK_STATUS, None)
        if raw_network is None:
            network_status = default_network
        else:
            value = str(raw_network).lower()
            if value in ("online", "connected"):
                network_status = NetworkStatus.ONLINE
            elif value in ("offline", "disconnected", "failed"):
                network_status = NetworkStatus.OFFLINE
            else:
                network_status = default_network
    except Exception:
        network_status = default_network

    # Get update_in_progress status
    update_in_progress = is_update_in_progress(state_manager)
    
    # Get whatsapp status
    try:
        ws_val = state_manager.get_state_data(StateKeys.WHATSAPP_STATUS, "disconnected")
        whatsapp_status = WhatsappStatus(ws_val)
    except Exception:
        whatsapp_status = WhatsappStatus.DISCONNECTED
    
    return Snapshot(
        perm_mic=perm_mic,
        perm_screen=perm_screen,
        perm_accessibility=perm_accessibility,
        device_input=default_device,
        network=network_status,
        first_run=first_run,
        app_mode=current_mode,
        restart_pending=restart_pending,
        update_in_progress=update_in_progress,
        whatsapp_status=whatsapp_status,
    )
