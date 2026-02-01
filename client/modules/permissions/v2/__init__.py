"""
Permission System V2

A complete permission orchestration system for macOS with:
- Pipeline mode (sequential steps, no batches)
- Capability-based probing
- Error classification
- Restart management
"""

from .types import (
    Phase,
    PermissionId,
    StepMode,
    StepState,
    OutcomeKind,
    PermissionCriticality,
    StepTiming,
    StepConfig,
    RestartConfig,
    ProbeEvidence,
    ProbeResult,
    StepOutcome,
)
from .error_matrix import (
    NormCategory,
    normalize_error,
    apply_normalization_to_evidence,
    StepCounters,
    DENY_CONFIRM_COUNT,
    RESTART_SUSPECT_COUNT,
)
from .ledger import (
    StepLedgerEntry,
    LedgerRecord,
    LedgerStore,
)
from .settings_nav import (
    SettingsNavigator,
    SETTINGS_URLS,
)
from .orchestrator import (
    PermissionOrchestrator,
    UIEvent,
    UIEventType,
)
from .classifiers import (
    BaseClassifier,
    MicrophoneClassifier,
    ScreenCaptureClassifier,
    InputMonitoringClassifier,
    AccessibilityClassifier,
    ContactsClassifier,
    FullDiskAccessClassifier,
    get_classifier,
)
from .probers import BaseProber
from .config_loader import load_v2_config
from .integration import PermissionOrchestratorIntegration

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
