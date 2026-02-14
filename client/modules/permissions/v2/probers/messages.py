"""
Permission System V2 - Messages Prober

Probes Messages permission (Automation) using AppleScript.
"""

from __future__ import annotations

import asyncio
import logging
import subprocess
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class MessagesProber(BaseProber):
    """
    Prober for Messages permission (AppleEvents/Automation).
    
    Uses `osascript` to send a harmless event to Messages.app.
    This triggers the "App wants to control Messages" TCC prompt.
    """
    
    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.MESSAGES
        self._last_result: bool | None = None
    
    async def trigger(self) -> None:
        """
        Trigger Messages permission via AppleScript.
        
        Note: 'get name' doesn't require Automation permission.
        We need to access actual data (chats/services) to trigger TCC prompt.
        """
        logger.debug("[MESSAGES_PROBER] Triggering request...")
        try:
            # We run it in background so we don't block
            # IMPORTANT: 'get name' doesn't require Automation permission!
            # 'count of every service' actually accesses Messages data and triggers TCC
            cmd = ["osascript", "-e", 'tell application "Messages" to count of every service']
            subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            logger.debug("[MESSAGES_PROBER] Triggered messages permission request via AppleScript")
            
        except Exception as e:
            logger.warning("[MESSAGES_PROBER] Trigger failed: %s", e)
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe messages capability."""
        ts = self._now()
        
        # Light probe: use cached
        if probe_kind == "light" and self._last_result is not None:
            ok = self._last_result
            domain, code, msg = None, None, None
        else:
            ok, domain, code, msg = await self._capability_messages()
            self._last_result = ok
        
        ev = ProbeEvidence(
            # We map this to messages_access_ok
            messages_access_ok=ok,
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
    
    async def _capability_messages(self) -> tuple[bool | None, str | None, str | None, str | None]:
        """
        Test Messages capability by running a simple AppleScript.
        Returns (ok, domain, code, message).
        
        Note: 'get name' doesn't require Automation permission!
        We use 'count of every service' which accesses Messages data and requires TCC.
        """
        try:
            # IMPORTANT: 'get name' doesn't require Automation permission!
            # 'count of every service' actually accesses Messages data and requires TCC
            
            # Use asyncio.create_subprocess_exec for async execution
            proc = await asyncio.create_subprocess_exec(
                "osascript", "-e", 'tell application "Messages" to count of every service',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            try:
                stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=2.0)
                rc = proc.returncode
            except asyncio.TimeoutError:
                try:
                    proc.kill()
                except ProcessLookupError:
                    pass
                return None, "AppleScript", "TIMEOUT", "Command timed out (prompt likely open)"

            if rc == 0:
                logger.debug("[MESSAGES_PROBER] Success (AppleScript returned 0)")
                return True, None, None, None
            
            err_str = stderr.decode().strip()
            # -1743: Not authorized to send AppleEvents to System Events (or target app)
            # "User canceled" might also appear if they click Don't Allow
            if "1743" in err_str or "not authorized" in err_str.lower():
                 return False, "AppleScript", "DENIED", err_str
            
            # Other errors
            return None, "AppleScript", "ERROR", f"Code {rc}: {err_str}"
                
        except Exception as e:
            logger.error("[MESSAGES_PROBER] Test failed: %s", e)
            return None, "Execution", type(e).__name__, str(e)
    
    def supports_light_probe(self) -> bool:
        return True
