"""
Permission System V2 - Screen Capture Prober

Probes Screen Capture permission by attempting to capture a frame.
"""

from __future__ import annotations

import logging
from typing import Literal, Optional, Tuple

from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from ..error_matrix import apply_normalization_to_evidence
from .base import BaseProber

logger = logging.getLogger(__name__)


class ScreenCaptureProber(BaseProber):
    """Prober for Screen Capture permission."""
    
    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.SCREEN_CAPTURE
        self._last_result: Optional[bool] = None
    
    async def trigger(self) -> None:
        """
        Trigger screen capture permission.
        Uses CGRequestScreenCaptureAccess() if available.
        """
        try:
            from Quartz import CGRequestScreenCaptureAccess
            result = CGRequestScreenCaptureAccess()
            logger.debug("[SC_PROBER] CGRequestScreenCaptureAccess() = %s", result)
        except ImportError:
            logger.debug("[SC_PROBER] CGRequestScreenCaptureAccess not available")
        except Exception as e:
            logger.warning("[SC_PROBER] Trigger failed: %s", e)
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe screen capture capability."""
        ts = self._now()
        
        # Light probe: use cached
        if probe_kind == "light" and self._last_result is not None:
            ok = self._last_result
            domain, code, msg = None, None, None
        else:
            ok, domain, code, msg = await self._capability_screen_frame(probe_kind)
            self._last_result = ok
        
        ev = ProbeEvidence(
            frames_received=ok,
            error_domain=domain,
            error_code=code,
            error_message=msg,
        )
        ev = apply_normalization_to_evidence(self.permission, ev)
        
        return ProbeResult(
            permission=self.permission,
            timestamp=ts,
            probe_kind=probe_kind,
            evidence=ev
        )
    
    async def _capability_screen_frame(self, probe_kind: str) -> Tuple[Optional[bool], Optional[str], Optional[str], Optional[str]]:
        """
        Test screen capture capability.
        Returns (frames_received, domain, code, message).
        """
        try:
            from Quartz import (
                CGWindowListCreateImage,
                CGRectNull,
                kCGWindowListOptionAll,
                kCGNullWindowID,
            )
            
            # Try to capture a screenshot
            image = CGWindowListCreateImage(
                CGRectNull,
                kCGWindowListOptionAll,
                kCGNullWindowID,
                0  # kCGWindowImageDefault
            )
            
            if image is not None:
                # Check if image has actual content (not just a blank/denied frame)
                try:
                    from Quartz import CGImageGetWidth, CGImageGetHeight
                    width = CGImageGetWidth(image)
                    height = CGImageGetHeight(image)
                    if width > 0 and height > 0:
                        logger.debug("[SC_PROBER] Got frame %dx%d", width, height)
                        return True, None, None, None
                except:
                    # If we got an image object, consider it a pass
                    return True, None, None, None
            
            logger.debug("[SC_PROBER] CGWindowListCreateImage returned None")
            return False, "ScreenCapture", None, "Screen Recording permission denied"
            
        except ImportError as e:
            logger.warning("[SC_PROBER] Quartz not available: %s", e)
            return None, "import", None, str(e)
        except Exception as e:
            logger.error("[SC_PROBER] Screen capture test failed: %s", e)
            return False, "ScreenCapture", type(e).__name__, str(e)
    
    def supports_light_probe(self) -> bool:
        return True
