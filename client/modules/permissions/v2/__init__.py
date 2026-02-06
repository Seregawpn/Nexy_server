"""
Permission System V2

A complete permission orchestration system for macOS with:
- Pipeline mode (sequential steps, no batches)
- Capability-based probing
- Error classification
- Restart management
"""

from .classifiers import (
    AccessibilityClassifier,
    BaseClassifier,
    ContactsClassifier,
    FullDiskAccessClassifier,
    InputMonitoringClassifier,
    MicrophoneClassifier,
    ScreenCaptureClassifier,
    get_classifier,
)
from .config_loader import load_v2_config
from .error_matrix import (
    DENY_CONFIRM_COUNT,
    RESTART_SUSPECT_COUNT,
    NormCategory,
    StepCounters,
    apply_normalization_to_evidence,
    normalize_error,
)
from .integration import PermissionOrchestratorIntegration
from .ledger import (
    LedgerRecord,
    LedgerStore,
    StepLedgerEntry,
)
from .orchestrator import (
    PermissionOrchestrator,
    UIEvent,
    UIEventType,
)
from .probers import BaseProber
from .settings_nav import (
    SETTINGS_URLS,
    SettingsNavigator,
)
from .types import (
    OutcomeKind,
    PermissionCriticality,
    PermissionId,
    Phase,
    ProbeEvidence,
    ProbeResult,
    RestartConfig,
    StepConfig,
    StepMode,
    StepOutcome,
    StepState,
    StepTiming,
)

__all__ = [
    # Types
    "Phase",
    "PermissionId",
    "StepMode",
    "StepState",
    "OutcomeKind",
    "PermissionCriticality",
    "StepTiming",
    "StepConfig",
    "RestartConfig",
    "ProbeEvidence",
    "ProbeResult",
    "StepOutcome",
    # Error matrix
    "NormCategory",
    "normalize_error",
    "apply_normalization_to_evidence",
    "StepCounters",
    "DENY_CONFIRM_COUNT",
    "RESTART_SUSPECT_COUNT",
    # Ledger
    "StepLedgerEntry",
    "LedgerRecord",
    "LedgerStore",
    # Settings
    "SettingsNavigator",
    "SETTINGS_URLS",
    # Orchestrator
    "PermissionOrchestrator",
    "UIEvent",
    "UIEventType",
    # Classifiers
    "BaseClassifier",
    "MicrophoneClassifier",
    "ScreenCaptureClassifier",
    "InputMonitoringClassifier",
    "AccessibilityClassifier",
    "ContactsClassifier",
    "FullDiskAccessClassifier",
    "get_classifier",
    # Probers
    "BaseProber",
    # Config
    "load_v2_config",
    # Integration
    "PermissionOrchestratorIntegration",
]
