"""
Utility that normalises permission events and spots meaningful transitions.
"""

from __future__ import annotations

import logging
from typing import Dict, Iterable, Iterator, List, Optional, Tuple

from modules.permissions.core.types import PermissionStatus, PermissionType

from .types import PermissionTransition

logger = logging.getLogger(__name__)


class PermissionChangeDetector:
    """
    Collects permission events from EventBus, keeps track of the latest known
    status for each permission and emits transitions for critical permissions.
    """

    def __init__(self, critical_permissions: Iterable[PermissionType]):
        self._critical: set[PermissionType] = set(critical_permissions)
        self._last_status: Dict[PermissionType, PermissionStatus] = {}

    def set_critical_permissions(self, permissions: Iterable[PermissionType]) -> None:
        """Update the set of permissions that should trigger a restart."""

        self._critical = set(permissions)

    def process_event(self, event_type: str, payload: Dict[str, object]) -> List[PermissionTransition]:
        """
        Normalise raw event data and return transitions that require attention.
        """

        transitions: List[PermissionTransition] = []

        for perm, old_status, new_status, session_id, source in self._extract_entries(
            event_type, payload
        ):
            if new_status is None:
                continue

            # Compute the baseline status before mutating the cache. This avoids
            # clobbering the previous state when events do not provide old_status.
            cached_status = self._last_status.get(perm)
            baseline_old = old_status or cached_status
            if baseline_old is None:
                baseline_old = new_status

            if perm in self._critical and new_status == PermissionStatus.GRANTED and baseline_old != PermissionStatus.GRANTED:
                transition = PermissionTransition(
                    permission=perm,
                    old_status=baseline_old,
                    new_status=new_status,
                    session_id=session_id,
                    source=source,
                )
                transitions.append(transition)
                logger.info(
                    "[PERMISSION_RESTART] Critical permission granted: %s (%s → %s)",
                    perm.value,
                    baseline_old.value if baseline_old else "unknown",
                    new_status.value,
                )

            # Persist the latest status after computing the transition, so future
            # events have the correct baseline even when old_status is omitted.
            self._last_status[perm] = new_status

        return transitions

    def _extract_entries(
        self, event_type: str, payload: Dict[str, object]
    ) -> Iterator[Tuple[PermissionType, Optional[PermissionStatus], Optional[PermissionStatus], Optional[str], Optional[str]]]:
        base_session_id = _safe_str(payload.get("session_id"))
        base_source = _safe_str(payload.get("source")) or event_type

        single_permission = _normalize_permission(payload.get("permission"))
        if single_permission:
            old_status = _normalize_status(payload.get("old_status"))
            raw_new = payload.get("new_status")
            if raw_new is None:
                raw_new = payload.get("status")
            new_status = _normalize_status(raw_new)
            yield single_permission, old_status, new_status, base_session_id, base_source

        permissions_map = payload.get("permissions")
        if isinstance(permissions_map, dict):
            for perm_key, details in permissions_map.items():
                perm = _normalize_permission(perm_key)
                if perm is None:
                    continue

                old_status = None
                new_status = None
                entry_session_id = base_session_id
                entry_source = base_source

                if isinstance(details, dict):
                    old_status = _normalize_status(
                        details.get("old_status") or details.get("previous_status")
                    )
                    new_status = _normalize_status(
                        details.get("new_status")
                        or details.get("status")
                        or details.get("current_status")
                    )
                    detail_session = _safe_str(details.get("session_id"))
                    detail_source = _safe_str(details.get("source"))
                    if detail_session:
                        entry_session_id = detail_session
                    if detail_source:
                        entry_source = detail_source
                else:
                    new_status = _normalize_status(details)

                yield perm, old_status, new_status, entry_session_id, entry_source


def _normalize_permission(value: object) -> Optional[PermissionType]:
    if isinstance(value, PermissionType):
        return value

    if isinstance(value, str):
        lowered = value.strip().lower()
        for perm in PermissionType:
            if perm.value == lowered:
                return perm
    return None


def _normalize_status(value: object) -> Optional[PermissionStatus]:
    if isinstance(value, PermissionStatus):
        return value

    if isinstance(value, str):
        lowered = value.strip().lower()
        for status in PermissionStatus:
            if status.value == lowered:
                return status
    return None


def _safe_str(value: object) -> Optional[str]:
    if value is None:
        return None
    return str(value)
