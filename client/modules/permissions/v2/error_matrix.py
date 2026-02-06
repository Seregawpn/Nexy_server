"""
Permission System V2 - Error Classification Matrix

Unified error normalization for all permission probers.
Maps error domains/codes/messages to categories: OK, TRANSIENT, DENIED, NEEDS_RESTART, MISCONFIG.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .types import PermissionId, ProbeEvidence


class NormCategory(str, Enum):
    """Normalized error categories."""
    OK = "ok"
    TRANSIENT = "transient"
    DENIED = "denied"
    NEEDS_RESTART = "needs_restart"
    MISCONFIG = "misconfig"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class MarkerSet:
    """Markers for error classification."""
    denied_markers: list[str]
    transient_markers: list[str]
    misconfig_markers: list[str]


# Global defaults
DEFAULT_MARKERS = MarkerSet(
    denied_markers=[
        "not authorized",
        "not permitted",
        "permission denied",
        "authorization denied",
        "tcc",
        "ktccservice",
        "denied",
    ],
    transient_markers=[
        "timeout",
        "timed out",
        "try again",
        "busy",
        "in use",
        "temporarily unavailable",
        "interrupted",
        "could not start",
        "cannot start",
    ],
    misconfig_markers=[
        "sandbox",
        "code signature",
        "bundle identifier",
        "not in /applications",
        "wrong process",
        "helper",
        "agent",
    ],
)


# Per-permission enrichments
PERMISSION_MARKERS: dict[PermissionId, MarkerSet] = {
    PermissionId.MICROPHONE: MarkerSet(
        denied_markers=["microphone", "ktccservicemicrophone", "avauthorizationstatusdenied"],
        transient_markers=["device", "sample rate", "format", "coreaudio", "overrun", "underrun"],
        misconfig_markers=[],
    ),
    PermissionId.SCREEN_CAPTURE: MarkerSet(
        denied_markers=["screen recording", "screen capture", "ktccservicescreencapture"],
        transient_markers=["stream", "start", "interrupted"],
        misconfig_markers=[],
    ),
    PermissionId.INPUT_MONITORING: MarkerSet(
        denied_markers=["input monitoring", "listen event", "ktccservicelistenevent"],
        transient_markers=["kcgeventtapdisabledbytimeout", "timeout", "disabled"],
        misconfig_markers=[],
    ),
    PermissionId.ACCESSIBILITY: MarkerSet(
        denied_markers=["accessibility", "trusted", "not trusted", "ax"],
        transient_markers=["transition", "not ready"],
        misconfig_markers=["tcc identity", "bundle", "applications"],
    ),
    PermissionId.FULL_DISK_ACCESS: MarkerSet(
        denied_markers=["full disk", "tcc", "ktccservicesystempolicyallfiles"],
        transient_markers=["busy", "try again"],
        misconfig_markers=["sandbox"],
    ),
    PermissionId.CONTACTS: MarkerSet(
        denied_markers=["contacts"],
        transient_markers=["busy", "try again"],
        misconfig_markers=["sandbox"],
    ),
}


# Counter thresholds
DENY_CONFIRM_COUNT = 3
RESTART_SUSPECT_COUNT = 2


def _lower(s: str | None) -> str:
    return (s or "").strip().lower()


def normalize_error(
    *,
    permission: PermissionId,
    domain: str | None,
    code: str | None,
    message: str | None,
) -> NormCategory:
    """Normalize an error to a category based on domain/code/message."""
    d = _lower(domain)
    c = _lower(code)
    m = _lower(message)

    ms = PERMISSION_MARKERS.get(permission)
    denied = DEFAULT_MARKERS.denied_markers + (ms.denied_markers if ms else [])
    transient = DEFAULT_MARKERS.transient_markers + (ms.transient_markers if ms else [])
    misconfig = DEFAULT_MARKERS.misconfig_markers + (ms.misconfig_markers if ms else [])

    # MISCONFIG first
    if any(x in m for x in misconfig) or "sandbox" in d:
        return NormCategory.MISCONFIG

    # Strong denied
    if any(x in m for x in denied) or "tcc" in d:
        return NormCategory.DENIED

    # Transient
    if any(x in m for x in transient):
        return NormCategory.TRANSIENT

    # Some domains commonly represent transient failures
    if any(x in d for x in ["coreaudio", "avfoundation", "screen", "iosurface"]):
        if "timeout" in m or "busy" in m:
            return NormCategory.TRANSIENT

    return NormCategory.UNKNOWN


def apply_normalization_to_evidence(permission: PermissionId, ev: ProbeEvidence) -> ProbeEvidence:
    """
    Returns a new ProbeEvidence with hints set based on normalized error text.
    Probers can still override hints if they know better.
    """
    if not (ev.error_domain or ev.error_code or ev.error_message):
        return ev

    cat = normalize_error(
        permission=permission,
        domain=ev.error_domain,
        code=ev.error_code,
        message=ev.error_message
    )

    denied_hint = ev.permission_denied_hint
    transient_hint = ev.transient_hint
    misconfig_hint = ev.misconfig_hint

    if cat == NormCategory.DENIED and denied_hint is None:
        denied_hint = True
    if cat in (NormCategory.TRANSIENT, NormCategory.UNKNOWN) and transient_hint is None:
        transient_hint = True
    if cat == NormCategory.MISCONFIG and misconfig_hint is None:
        misconfig_hint = True

    # Create new evidence with updated hints
    return ProbeEvidence(
        frames_received=ev.frames_received,
        tap_created=ev.tap_created,
        tap_enabled=ev.tap_enabled,
        ax_action_ok=ev.ax_action_ok,
        file_access_ok=ev.file_access_ok,
        contacts_fetch_ok=ev.contacts_fetch_ok,
        error_domain=ev.error_domain,
        error_code=ev.error_code,
        error_message=ev.error_message,
        permission_denied_hint=denied_hint,
        permission_not_determined_hint=ev.permission_not_determined_hint,
        transient_hint=transient_hint,
        likely_needs_restart_hint=ev.likely_needs_restart_hint,
        misconfig_hint=misconfig_hint,
    )


@dataclass
class StepCounters:
    """Counters for tracking consecutive error categories."""
    consecutive_denied: int = 0
    consecutive_transient: int = 0
    consecutive_needs_restart: int = 0

    def update(self, cat: NormCategory) -> None:
        """Update counters based on normalized category."""
        if cat == NormCategory.DENIED:
            self.consecutive_denied += 1
            self.consecutive_transient = 0
            self.consecutive_needs_restart = 0
        elif cat in (NormCategory.TRANSIENT, NormCategory.UNKNOWN):
            self.consecutive_transient += 1
            self.consecutive_denied = 0
            self.consecutive_needs_restart = 0
        elif cat == NormCategory.NEEDS_RESTART:
            self.consecutive_needs_restart += 1
            self.consecutive_denied = 0
            self.consecutive_transient = 0
        else:
            # OK or other - reset all
            self.consecutive_denied = 0
            self.consecutive_transient = 0
            self.consecutive_needs_restart = 0

    def is_denied_confirmed(self) -> bool:
        """Check if denied is confirmed by consecutive count."""
        return self.consecutive_denied >= DENY_CONFIRM_COUNT

    def is_restart_suspected(self) -> bool:
        """Check if restart is suspected by consecutive count."""
        return self.consecutive_needs_restart >= RESTART_SUSPECT_COUNT
