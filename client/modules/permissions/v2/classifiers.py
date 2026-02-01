"""
Permission System V2 - Classifiers

Classifies probe results into outcomes for each permission type.
Uses error_matrix for normalization and counter logic.
"""

from __future__ import annotations

import logging
from typing import Literal

from .types import (
    PermissionId,
    OutcomeKind,
    ProbeResult,
    StepOutcome,
)
from .error_matrix import (
    NormCategory,
    normalize_error,
    DENY_CONFIRM_COUNT,
    RESTART_SUSPECT_COUNT,
)
from .ledger import StepLedgerEntry

logger = logging.getLogger(__name__)


class BaseClassifier:
    """Base classifier with common logic."""
    
    def __init__(self, permission: PermissionId):
        self.permission = permission
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        """Override in subclass."""
        raise NotImplementedError
    
    def _update_counters(self, entry: StepLedgerEntry, cat: NormCategory) -> None:
        """Update entry counters based on category."""
        if cat == NormCategory.DENIED:
            entry.consecutive_denied += 1
            entry.consecutive_transient = 0
            entry.consecutive_needs_restart = 0
        elif cat in (NormCategory.TRANSIENT, NormCategory.UNKNOWN):
            entry.consecutive_transient += 1
            entry.consecutive_denied = 0
            entry.consecutive_needs_restart = 0
        elif cat == NormCategory.NEEDS_RESTART:
            entry.consecutive_needs_restart += 1
            entry.consecutive_denied = 0
            entry.consecutive_transient = 0
        else:
            entry.consecutive_denied = 0
            entry.consecutive_transient = 0
            entry.consecutive_needs_restart = 0


class MicrophoneClassifier(BaseClassifier):
    """Classifier for microphone permission."""
    
    def __init__(self):
        super().__init__(PermissionId.MICROPHONE)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        # PASS: frames received
        if e.frames_received is True:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Audio frames received.",
                reason_code="MIC_PASS"
            )
        
        # Normalize error
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        # Explicit denied hint or confirmed by counter
        if e.permission_denied_hint or entry.consecutive_denied >= DENY_CONFIRM_COUNT:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.FAIL,
                reason="Microphone access denied.",
                reason_code="MIC_DENIED"
            )
        
        # Still waiting
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING,
            reason="Waiting for microphone access.",
            reason_code="MIC_WAITING",
            is_transient=True
        )


class ScreenCaptureClassifier(BaseClassifier):
    """Classifier for screen capture permission."""
    
    def __init__(self):
        super().__init__(PermissionId.SCREEN_CAPTURE)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        # PASS: frame received
        if e.frames_received is True:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Screen frame captured.",
                reason_code="SC_PASS"
            )
        
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        if e.permission_denied_hint or entry.consecutive_denied >= DENY_CONFIRM_COUNT:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.FAIL,
                reason="Screen capture denied.",
                reason_code="SC_DENIED"
            )
        
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING,
            reason="Waiting for screen capture access.",
            reason_code="SC_WAITING",
            is_transient=True
        )


class InputMonitoringClassifier(BaseClassifier):
    """Classifier for input monitoring permission (CGEventTap).
    
    NEEDS_RESTART is only allowed when:
    - permission_denied_hint is NOT True (i.e., permission was granted)
    - We have evidence suggesting "granted but not active"
    
    This prevents false restarts when user simply hasn't granted permission.
    """
    
    def __init__(self):
        super().__init__(PermissionId.INPUT_MONITORING)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        # PASS: tap created and enabled
        if e.tap_created is True and e.tap_enabled is True:
            # Reset counters on success
            entry.consecutive_needs_restart = 0
            entry.consecutive_denied = 0
            entry.consecutive_transient = 0
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Event tap created and enabled.",
                reason_code="IM_PASS"
            )
        
        # Check for explicit denied hint first
        if e.permission_denied_hint:
            entry.consecutive_denied += 1
            entry.consecutive_needs_restart = 0
            entry.consecutive_transient = 0
            
            if entry.consecutive_denied >= DENY_CONFIRM_COUNT:
                return StepOutcome(
                    permission=self.permission,
                    kind=OutcomeKind.FAIL,
                    reason="Input Monitoring denied.",
                    reason_code="IM_DENIED"
                )
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING,
                reason="Waiting for Input Monitoring (appears denied).",
                reason_code="IM_WAITING_DENIED",
                is_transient=True
            )
        
        # Check for needs_restart hint - ONLY if NOT denied
        # This is the key safety: needs_restart only when permission granted but not active
        if e.likely_needs_restart_hint:
            entry.consecutive_needs_restart += 1
            entry.consecutive_denied = 0
            entry.consecutive_transient = 0
            
            if entry.consecutive_needs_restart >= RESTART_SUSPECT_COUNT:
                return StepOutcome(
                    permission=self.permission,
                    kind=OutcomeKind.NEEDS_RESTART,
                    reason="Input Monitoring granted but needs restart to activate.",
                    reason_code="IM_NEEDS_RESTART",
                    needs_restart=True
                )
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING,
                reason="Input Monitoring may need restart, confirming...",
                reason_code="IM_WAITING_RESTART",
                is_transient=True
            )
        
        # Normalize error for other cases
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        # Denied confirmed by error normalization
        if entry.consecutive_denied >= DENY_CONFIRM_COUNT:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.FAIL,
                reason="Input Monitoring denied.",
                reason_code="IM_DENIED"
            )
        
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING,
            reason="Waiting for Input Monitoring.",
            reason_code="IM_WAITING",
            is_transient=True
        )


class AccessibilityClassifier(BaseClassifier):
    """Classifier for accessibility permission."""
    
    def __init__(self):
        super().__init__(PermissionId.ACCESSIBILITY)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        # PASS: AX action succeeded
        if e.ax_action_ok is True:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Accessibility enabled.",
                reason_code="AX_PASS"
            )
        
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        # Misconfig (not in /Applications, wrong bundle)
        if e.misconfig_hint:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.FAIL,
                reason="App misconfigured (check app location).",
                reason_code="AX_MISCONFIG"
            )
        
        # For AX, denied means WAITING_USER (need to toggle in Settings)
        if e.permission_denied_hint or cat == NormCategory.DENIED:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING_USER,
                reason="Enable Accessibility in System Settings.",
                reason_code="AX_WAITING_USER"
            )
        
        # Transient after toggle
        if e.transient_hint:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING,
                reason="Accessibility transitioning.",
                reason_code="AX_TRANSIENT",
                is_transient=True
            )
        
        # Default to waiting user
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING_USER,
            reason="Enable Accessibility in System Settings.",
            reason_code="AX_WAITING_USER_DEFAULT"
        )


class ContactsClassifier(BaseClassifier):
    """Classifier for contacts permission."""
    
    def __init__(self):
        super().__init__(PermissionId.CONTACTS)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        if e.contacts_fetch_ok is True:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Contacts access granted.",
                reason_code="CONTACTS_PASS"
            )
        
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        if e.permission_denied_hint or entry.consecutive_denied >= DENY_CONFIRM_COUNT:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING_USER,
                reason="Enable Contacts in System Settings.",
                reason_code="CONTACTS_WAITING_USER"
            )
        
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING,
            reason="Waiting for Contacts access.",
            reason_code="CONTACTS_WAITING",
            is_transient=True
        )


class FullDiskAccessClassifier(BaseClassifier):
    """Classifier for Full Disk Access permission."""
    
    def __init__(self):
        super().__init__(PermissionId.FULL_DISK_ACCESS)
    
    def classify(self, probe: ProbeResult, entry: StepLedgerEntry) -> StepOutcome:
        e = probe.evidence
        
        if e.file_access_ok is True:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.PASS_,
                reason="Full Disk Access granted.",
                reason_code="FDA_PASS"
            )
        
        cat = normalize_error(
            permission=self.permission,
            domain=e.error_domain,
            code=e.error_code,
            message=e.error_message
        )
        self._update_counters(entry, cat)
        
        if e.permission_denied_hint or cat == NormCategory.DENIED:
            return StepOutcome(
                permission=self.permission,
                kind=OutcomeKind.WAITING_USER,
                reason="Enable Full Disk Access in System Settings.",
                reason_code="FDA_WAITING_USER"
            )
        
        return StepOutcome(
            permission=self.permission,
            kind=OutcomeKind.WAITING_USER,
            reason="Enable Full Disk Access in System Settings.",
            reason_code="FDA_WAITING_USER_DEFAULT"
        )


# Factory function
def get_classifier(permission: PermissionId) -> BaseClassifier:
    """Get classifier for a permission."""
    classifiers = {
        PermissionId.MICROPHONE: MicrophoneClassifier,
        PermissionId.SCREEN_CAPTURE: ScreenCaptureClassifier,
        PermissionId.INPUT_MONITORING: InputMonitoringClassifier,
        PermissionId.ACCESSIBILITY: AccessibilityClassifier,
        PermissionId.CONTACTS: ContactsClassifier,
        PermissionId.FULL_DISK_ACCESS: FullDiskAccessClassifier,
    }
    return classifiers[permission]()
