"""
Permission System V2 - Accessibility Prober

Probes Accessibility (AX) permission using AXIsProcessTrusted().
"""

from __future__ import annotations

from dataclasses import replace
import logging
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class AccessibilityProber(BaseProber):
    """Prober for Accessibility permission."""
    
    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.ACCESSIBILITY
        self._last_result: bool | None = None
    
    async def trigger(self) -> None:
        """
        Trigger the accessibility permission prompt using AXIsProcessTrustedWithOptions.
        This shows the native macOS dialog without opening System Settings.
        """
        try:
            from ApplicationServices import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt  # type: ignore[reportMissingImports]
            
            options = {kAXTrustedCheckOptionPrompt: True}
            result = AXIsProcessTrustedWithOptions(options)
            logger.debug("[AX_PROBER] Called AXIsProcessTrustedWithOptions(prompt=True) = %s", result)
            
        except ImportError:
            logger.debug("[AX_PROBER] ApplicationServices not available, skipping trigger")
        except Exception as e:
            logger.warning("[AX_PROBER] Trigger failed: %s", e)
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe AX capability."""
        ts = self._now()
        
        # Light probe: use cached result
        if probe_kind == "light" and self._last_result is not None:
            ax_ok = self._last_result
        else:
            ax_ok = await self._capability_ax_ok()
            self._last_result = ax_ok
        
        ev = ProbeEvidence(
            ax_action_ok=ax_ok,
            error_domain=None,
            error_code=None,
            error_message=None,
        )
        
        # If ax_ok is False, that means AXIsProcessTrusted() returned False
        # This is a "needs user action" state, not transient
        if ax_ok is False:
            ev = replace(ev, permission_denied_hint=True, transient_hint=False)
        
        ev = apply_normalization_to_evidence(self.permission, ev)
        return ProbeResult(
            permission=self.permission,
            timestamp=ts,
            probe_kind=probe_kind,
            evidence=ev
        )
    
    async def _capability_ax_ok(self) -> bool | None:
        """
        Check if Accessibility is enabled.
        Uses AXIsProcessTrusted() via PyObjC.
        """
        try:
            from ApplicationServices import AXIsProcessTrusted  # type: ignore[reportMissingImports]
            result = AXIsProcessTrusted()
            logger.debug("[AX_PROBER] AXIsProcessTrusted() = %s", result)
            return bool(result)
        except ImportError:
            logger.warning("[AX_PROBER] ApplicationServices not available")
            return None
        except Exception as e:
            logger.error("[AX_PROBER] AXIsProcessTrusted() failed: %s", e)
            return None
    
    def supports_light_probe(self) -> bool:
        return True
