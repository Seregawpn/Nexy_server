"""
Type definitions used by the permission restart module.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence


class PermissionType(Enum):
    """Типы разрешений"""

    MICROPHONE = "microphone"
    SCREEN_CAPTURE = "screen_capture"
    CAMERA = "camera"
    NETWORK = "network"
    NOTIFICATIONS = "notifications"
    ACCESSIBILITY = "accessibility"
    INPUT_MONITORING = "input_monitoring"
    CONTACTS = "contacts"
    FULL_DISK_ACCESS = "full_disk_access"


class PermissionStatus(Enum):
    """Статусы разрешений"""

    GRANTED = "granted"
    DENIED = "denied"
    NOT_DETERMINED = "not_determined"
    ERROR = "error"


@dataclass(frozen=True)
class PermissionTransition:
    """
    Represents a single permission status transition.

    Only transitions that change the effective permission state are emitted by
    the detector, with particular focus on DENIED/NOT_DETERMINED → GRANTED.
    """

    permission: PermissionType
    old_status: PermissionStatus
    new_status: PermissionStatus
    session_id: str | None = None
    source: str | None = None


@dataclass(frozen=True)
class RestartRequest:
    """
    Aggregated information about a planned application restart.
    """

    session_id: str | None
    reason: str
    delay_sec: float
    critical_permissions: tuple[PermissionType, ...]


@dataclass(frozen=True)
class RestartOutcome:
    """
    Result of a restart attempt.
    """

    success: bool
    attempts_used: int
    reason: str
    critical_permissions: Sequence[PermissionType]
