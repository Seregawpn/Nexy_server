"""
Permission System V2 - Input Monitoring Prober

Probes Input Monitoring permission using CGEventTap creation test.
This is the only permission that commonly needs app restart to activate.
"""

from __future__ import annotations

import logging
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class InputMonitoringProber(BaseProber):
    """Prober for Input Monitoring permission (CGEventTap)."""
    
    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.INPUT_MONITORING
        self._last_tap_created: bool | None = None
        self._last_tap_enabled: bool | None = None
        self._consecutive_create_fail: int = 0
    
    async def trigger(self) -> None:
        """
        Trigger Input Monitoring permission request.
        Uses IOHIDRequestAccess if available.
        """
        try:
            import ctypes
            IOKit = ctypes.CDLL('/System/Library/Frameworks/IOKit.framework/IOKit')
            kIOHIDRequestTypeListenEvent = 1
            IOKit.IOHIDRequestAccess(kIOHIDRequestTypeListenEvent)
            logger.debug("[IM_PROBER] Called IOHIDRequestAccess()")
        except Exception as e:
            logger.warning("[IM_PROBER] IOHIDRequestAccess failed: %s", e)
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe Input Monitoring capability via CGEventTap test."""
        ts = self._now()
        
        # Light probe: use cached
        if probe_kind == "light" and self._last_tap_created is not None:
            tap_created = self._last_tap_created
            tap_enabled = self._last_tap_enabled
            domain, code, msg = None, None, None
        else:
            tap_created, tap_enabled, domain, code, msg = await self._capability_event_tap()
            self._last_tap_created = tap_created
            self._last_tap_enabled = tap_enabled
        
        ev = ProbeEvidence(
            tap_created=tap_created,
            tap_enabled=tap_enabled,
            error_domain=domain,
            error_code=code,
            error_message=msg,
        )
        ev = apply_normalization_to_evidence(self.permission, ev)
        
        # Track consecutive failures for needs_restart detection
        if tap_created is False:
            self._consecutive_create_fail += 1
        else:
            self._consecutive_create_fail = 0
        
        # Heuristic: if we've failed to create tap multiple times
        # but there's no explicit "denied" error, might need restart
        if (self._consecutive_create_fail >= 3 and 
            ev.permission_denied_hint is not True and 
            tap_created is False):
            ev = ProbeEvidence(
                tap_created=tap_created,
                tap_enabled=tap_enabled,
                error_domain=domain,
                error_code=code,
                error_message=msg,
                permission_denied_hint=ev.permission_denied_hint,
                transient_hint=ev.transient_hint,
                likely_needs_restart_hint=True,  # Signal to classifier
                misconfig_hint=ev.misconfig_hint,
            )
        
        return ProbeResult(
            permission=self.permission,
            timestamp=ts,
            probe_kind=probe_kind,
            evidence=ev
        )
    
    async def _capability_event_tap(self) -> tuple[bool | None, bool | None, str | None, str | None, str | None]:
        """
        Test CGEventTap creation capability.
        Returns (tap_created, tap_enabled, domain, code, message).
        """
        try:
            from Quartz import (  # type: ignore[reportMissingImports]
                CFMachPortIsValid,  # type: ignore[reportAttributeAccessIssue]
                CGEventTapCreate,  # type: ignore[reportAttributeAccessIssue]
                CGEventTapEnable,  # type: ignore[reportAttributeAccessIssue]
                kCGEventMaskForAllEvents,  # type: ignore[reportAttributeAccessIssue]
                kCGEventTapOptionListenOnly,  # type: ignore[reportAttributeAccessIssue]
                kCGHeadInsertEventTap,  # type: ignore[reportAttributeAccessIssue]
                kCGSessionEventTap,  # type: ignore[reportAttributeAccessIssue]
            )
            
            # Dummy callback
            def dummy_callback(proxy, event_type, event, refcon):
                return event
            
            # Try to create tap
            tap = CGEventTapCreate(
                kCGSessionEventTap,
                kCGHeadInsertEventTap,
                kCGEventTapOptionListenOnly,
                kCGEventMaskForAllEvents,
                dummy_callback,
                None
            )
            
            if tap is None:
                logger.debug("[IM_PROBER] CGEventTapCreate returned NULL")
                return False, False, "CGEventTap", None, "tap creation failed (not permitted)"
            
            # Check if valid
            if not CFMachPortIsValid(tap):
                logger.debug("[IM_PROBER] CGEventTap is invalid")
                return True, False, "CGEventTap", None, "tap created but invalid"
            
            # Enable the tap
            CGEventTapEnable(tap, True)
            
            # Clean up
            try:
                CGEventTapEnable(tap, False)
            except:
                pass
            
            logger.debug("[IM_PROBER] CGEventTap created and enabled successfully")
            return True, True, None, None, None
            
        except ImportError as e:
            logger.warning("[IM_PROBER] Quartz not available: %s", e)
            return None, None, "import", None, str(e)
        except Exception as e:
            logger.error("[IM_PROBER] CGEventTap test failed: %s", e)
            return False, False, "CGEventTap", type(e).__name__, str(e)
    
    def supports_light_probe(self) -> bool:
        return True
