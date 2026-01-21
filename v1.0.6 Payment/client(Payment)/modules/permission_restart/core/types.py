"""
Type definitions used by the permission restart module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

from modules.permissions.core.types import PermissionStatus, PermissionType


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
    session_id: Optional[str] = None
    source: Optional[str] = None


@dataclass(frozen=True)
class RestartRequest:
    """
    Aggregated information about a planned application restart.
    """

    session_id: Optional[str]
    reason: str
    delay_sec: float
    critical_permissions: Tuple[PermissionType, ...]


@dataclass(frozen=True)
class RestartOutcome:
    """
    Result of a restart attempt.
    """

    success: bool
    attempts_used: int
    reason: str
    critical_permissions: Sequence[PermissionType]
