"""
Configuration helpers for the permission restart module.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .types import PermissionType

DEFAULT_CRITICAL_PERMISSIONS: list[PermissionType] = [
    PermissionType.MICROPHONE,
    PermissionType.ACCESSIBILITY,
    PermissionType.INPUT_MONITORING,
    PermissionType.SCREEN_CAPTURE,
]


@dataclass
class PermissionRestartConfig:
    """
    Declarative configuration for restart orchestration.
    """

    enabled: bool = True
    allow_dev_fallback: bool = True
    critical_permissions: list[PermissionType] = field(
        default_factory=lambda: list(DEFAULT_CRITICAL_PERMISSIONS)
    )
    restart_delay_sec: float = 5.0
    max_restart_attempts: int = 3
    respect_active_sessions: bool = True
    respect_updates: bool = True
    handler_launch_delay_ms: float = 1000.0  # Delay after dev process launch (default: 1.0 sec)
    packaged_launch_grace_ms: float = 3000.0  # Delay after process exit before launching packaged app
    graceful_shutdown_timeout_sec: float = 10.0  # Max wait before relaunch helper gives up
    graceful_shutdown_poll_interval_sec: float = 0.25  # Poll step while waiting for PID to exit

    @classmethod
    def from_dict(cls, raw: dict[str, object] | None) -> "PermissionRestartConfig":
        """
        Build configuration from raw dictionary data (usually unified_config).
        """

        if raw is None:
            return cls()

        enabled = bool(raw.get("enabled", True))
        allow_dev_fallback = bool(raw.get("allow_dev_fallback", True))
        restart_delay_sec = float(str(raw.get("restart_delay_sec", 5.0)))
        max_attempts = int(str(raw.get("max_restart_attempts", 3)))
        respect_sessions = bool(raw.get("respect_active_sessions", True))
        respect_updates = bool(raw.get("respect_updates", True))
        handler_launch_delay_ms = float(str(raw.get("handler_launch_delay_ms", 1000.0)))
        packaged_launch_grace_ms = float(str(raw.get("packaged_launch_grace_ms", 3000.0)))
        graceful_shutdown_timeout_sec = float(str(raw.get("graceful_shutdown_timeout_sec", 10.0)))
        graceful_shutdown_poll_interval_sec = float(str(raw.get("graceful_shutdown_poll_interval_sec", 0.25)))

        critical_raw: Iterable[object] | None = raw.get("critical_permissions")  # type: ignore[assignment]
        critical_permissions = _parse_permission_list(critical_raw)

        return cls(
            enabled=enabled,
            allow_dev_fallback=allow_dev_fallback,
            critical_permissions=critical_permissions or list(DEFAULT_CRITICAL_PERMISSIONS),
            restart_delay_sec=restart_delay_sec,
            max_restart_attempts=max_attempts,
            respect_active_sessions=respect_sessions,
            respect_updates=respect_updates,
            handler_launch_delay_ms=handler_launch_delay_ms,
            packaged_launch_grace_ms=packaged_launch_grace_ms,
            graceful_shutdown_timeout_sec=graceful_shutdown_timeout_sec,
            graceful_shutdown_poll_interval_sec=graceful_shutdown_poll_interval_sec,
        )


def load_permission_restart_config(section: dict[str, object] | None) -> PermissionRestartConfig:
    """
    Adapter used by integrations to obtain a fully parsed configuration object.
    """

    return PermissionRestartConfig.from_dict(section)


def _parse_permission_list(values: Iterable[object] | None) -> list[PermissionType]:
    if not values:
        return []

    resolved: list[PermissionType] = []
    for value in values:
        perm = _normalize_permission(value)
        if perm is not None and perm not in resolved:
            resolved.append(perm)
    return resolved


def _normalize_permission(value: object) -> PermissionType | None:
    if isinstance(value, PermissionType):
        return value

    if isinstance(value, str):
        lowered = value.strip().lower()
        for perm in PermissionType:
            if perm.value == lowered:
                return perm
    return None
