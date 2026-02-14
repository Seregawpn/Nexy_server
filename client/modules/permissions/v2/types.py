"""
Permission System V2 - Core Types

All enums, dataclasses, and type definitions for the permission orchestration system.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Literal


class Phase(StrEnum):
    """Lifecycle phases of the permission wizard."""
    FIRST_RUN = "first_run"
    RESTART_PENDING = "restart_pending"
    POST_RESTART_VERIFY = "post_restart_verify"
    COMPLETED = "completed"
    LIMITED_MODE = "limited_mode"


class PermissionId(StrEnum):
    """Identifiers for all supported permissions."""
    MICROPHONE = "microphone"
    SCREEN_CAPTURE = "screen_capture"
    CONTACTS = "contacts"
    INPUT_MONITORING = "input_monitoring"
    ACCESSIBILITY = "accessibility"
    MESSAGES = "messages"
    FULL_DISK_ACCESS = "full_disk_access"
    NETWORK = "network"


class StepMode(StrEnum):
    """How a permission is requested."""
    AUTO_DIALOG = "auto_dialog"      # System TCC dialog
    OPEN_SETTINGS = "open_settings"  # Manual toggle in System Settings


class StepState(StrEnum):
    """States a permission step can be in."""
    UNKNOWN = "unknown"
    TRIGGERED = "triggered"
    GRACE = "grace"
    POLLING = "polling"
    WAITING_USER = "waiting_user"
    WAITING_LONG = "waiting_long"
    PASS_ = "pass"
    FAIL = "fail"
    NEEDS_RESTART = "needs_restart"
    FAIL_AFTER_RESTART = "fail_after_restart"
    SKIPPED = "skipped"


class OutcomeKind(StrEnum):
    """Classification outcomes from probers."""
    PASS_ = "pass"
    FAIL = "fail"
    WAITING = "waiting"
    WAITING_USER = "waiting_user"
    NEEDS_RESTART = "needs_restart"
    FAIL_AFTER_RESTART = "fail_after_restart"
    SKIP = "skip"


class PermissionCriticality(StrEnum):
    """How critical a permission is to app functionality."""
    HARD = "hard"      # App won't work without it
    SOFT = "soft"      # Degraded but usable
    FEATURE = "feature"  # Nice to have


@dataclass(frozen=True)
class StepTiming:
    """Timing configuration for a permission step."""
    grace_s: float
    poll_s: float

    heavy_cooldown_s: float = 10.0

    waiting_long_after_s: float = 300.0
    waiting_long_poll_s: float = 15.0

    post_restart_verify_window_s: float = 20.0
    post_restart_verify_tick_s: float = 2.0
    step_timeout_s: float | None = None


@dataclass(frozen=True)
class StepConfig:
    """Configuration for a single permission step."""
    permission: PermissionId
    mode: StepMode
    timing: StepTiming

    supports_needs_restart: bool = False
    settings_target: str | None = None
    criticality: PermissionCriticality = PermissionCriticality.FEATURE


@dataclass(frozen=True)
class RestartConfig:
    """Configuration for restart behavior."""
    delay_sec: float = 1.0
    settings_safety_window_sec: float = 30.0
    require_all_hard_pass: bool = True
    require_needs_restart: bool = True


@dataclass(frozen=True)
class ProbeEvidence:
    """
    Observations from a capability probe.
    Hints are set by error_matrix normalization or stack-specific logic.
    """
    # Capability signals
    frames_received: bool | None = None     # mic/screen
    tap_created: bool | None = None         # input monitoring
    tap_enabled: bool | None = None
    ax_action_ok: bool | None = None        # accessibility
    file_access_ok: bool | None = None      # FDA
    messages_access_ok: bool | None = None
    contacts_fetch_ok: bool | None = None
    network_conn_ok: bool | None = None

    # Error normalization inputs
    error_domain: str | None = None
    error_code: str | None = None
    error_message: str | None = None

    # Prober hints
    permission_denied_hint: bool | None = None
    permission_not_determined_hint: bool | None = None
    transient_hint: bool | None = None
    likely_needs_restart_hint: bool | None = None
    misconfig_hint: bool | None = None


@dataclass(frozen=True)
class ProbeResult:
    """Result of a probe operation."""
    permission: PermissionId
    timestamp: float
    probe_kind: Literal["light", "heavy"]
    evidence: ProbeEvidence
    suggested_next_heavy_after_s: float | None = None


@dataclass(frozen=True)
class StepOutcome:
    """Classification outcome from a classifier."""
    permission: PermissionId
    kind: OutcomeKind
    reason: str
    reason_code: str

    needs_restart: bool = False
    is_transient: bool = False

    debug: dict[str, Any] = field(default_factory=dict)
