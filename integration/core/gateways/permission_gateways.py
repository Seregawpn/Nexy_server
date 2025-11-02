"""
Permission-centric gateway helpers shared between integrations.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Tuple

from integration.core.state_manager import ApplicationStateManager

try:  # pragma: no cover - defensive fallback for tooling contexts
    from integration.core.state_manager import AppMode  # type: ignore
except Exception:  # pragma: no cover
    from enum import Enum

    class AppMode(Enum):
        SLEEPING = "sleeping"
        LISTENING = "listening"
        PROCESSING = "processing"

from modules.permission_restart.core.config import PermissionRestartConfig
from modules.permissions.core.types import PermissionType

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PermissionRestartDecision:
    """
    Normalised response from the permission restart gateway.
    """

    allowed: bool
    reason: str
    blocked_by: Optional[str] = None
    requires_idle: bool = False


class PermissionRestartGateway:
    """
    Centralises decision making for permission-driven restarts so integrations
    do not duplicate business rules.
    """

    def __init__(
        self,
        state_manager: ApplicationStateManager,
        *,
        updater_integration: Optional[object] = None,
    ) -> None:
        self._state_manager = state_manager
        self._updater_integration = updater_integration

    def evaluate(
        self,
        *,
        pending_permissions: Iterable[PermissionType],
        config: PermissionRestartConfig,
        attempts: int,
        is_first_run: bool,
    ) -> PermissionRestartDecision:
        """
        Decide whether we are allowed to schedule a restart right now and, if
        not, provide context for the caller.
        """

        normalised = self._normalise_permissions(pending_permissions)
        reason = self.build_reason(normalised)

        if attempts >= config.max_restart_attempts:
            return PermissionRestartDecision(
                allowed=False,
                reason=reason,
                blocked_by="max_attempts",
            )

        if config.respect_updates and self.is_update_available():
            return PermissionRestartDecision(
                allowed=False,
                reason=reason,
                blocked_by="update_available",
            )

        requires_idle = False
        if config.respect_active_sessions and not is_first_run and not self.is_idle_mode():
            requires_idle = True

        return PermissionRestartDecision(
            allowed=True,
            reason=reason,
            requires_idle=requires_idle,
        )

    @staticmethod
    def build_reason(pending_permissions: Sequence[PermissionType]) -> str:
        """
        Provide a canonical reason string for downstream logging/metrics.
        """

        if len(pending_permissions) == 1:
            return f"{pending_permissions[0].value}_granted"
        return "critical_permissions_granted"

    @staticmethod
    def _normalise_permissions(
        pending_permissions: Iterable[PermissionType],
    ) -> Tuple[PermissionType, ...]:
        seen = set()
        ordered: List[PermissionType] = []
        for permission in pending_permissions:
            if permission in seen:
                continue
            ordered.append(permission)
            seen.add(permission)
        ordered.sort(key=lambda perm: perm.value)
        return tuple(ordered)

    def is_idle_mode(self) -> bool:
        """
        Return True when the app is currently idle (SLEEPING mode).
        """

        try:
            current_mode = self._state_manager.get_current_mode()
        except Exception:  # pragma: no cover - defensive
            return True

        try:
            if current_mode == AppMode.SLEEPING:
                return True
        except Exception:  # pragma: no cover - defensive
            pass

        value = getattr(current_mode, "value", str(current_mode)).lower()
        return value == getattr(AppMode.SLEEPING, "value", "sleeping")

    def is_update_in_progress(self) -> bool:
        """
        Inspect updater integration or shared state to detect an ongoing update.
        """

        updater = self._updater_integration
        if updater is not None:
            try:
                accessor = getattr(updater, "is_update_in_progress", None)
                if callable(accessor):
                    return bool(accessor())
                if isinstance(accessor, bool):
                    return accessor
            except Exception:  # pragma: no cover - defensive
                logger.debug("PermissionRestartGateway: updater status check failed", exc_info=True)

        try:
            state_flag = self._state_manager.get_state_data("update_in_progress", False)
            return bool(state_flag)
        except Exception:  # pragma: no cover - defensive
            return False

    def is_update_available(self) -> bool:
        """
        Check whether a Sparkle update is waiting to be installed.
        """

        updater = self._updater_integration
        if updater is not None:
            try:
                accessor = getattr(updater, "is_update_available", None)
                if callable(accessor):
                    return bool(accessor())
                if isinstance(accessor, bool):
                    return accessor
            except Exception:  # pragma: no cover - defensive
                logger.debug("PermissionRestartGateway: update availability check failed", exc_info=True)

        return False
