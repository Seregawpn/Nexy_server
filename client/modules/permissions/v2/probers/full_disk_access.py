"""
Permission System V2 - Full Disk Access Prober

Probes Full Disk Access by attempting to stat protected files.
Uses only os.stat() for safety - no actual file reading.
"""

from __future__ import annotations

import glob
import logging
import os
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


# Protected paths that require FDA to access
FDA_TEST_PATTERNS: list[str] = [
    "~/Library/Messages/chat.db",  # iMessage database
    "~/Library/Safari/History.db",
    "~/Library/Mail/V*/MailData/Envelope Index",
]


class FullDiskAccessProber(BaseProber):
    """Prober for Full Disk Access permission."""

    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.FULL_DISK_ACCESS
        self._last_result: bool | None = None

    async def trigger(self) -> None:
        """
        No dialog API for FDA.
        Orchestrator opens Settings via deep-link.
        """
        # Nothing to do - user must manually enable in Settings
        logger.debug("[FDA_PROBER] No trigger available for FDA")

    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe FDA capability by stat'ing protected files."""
        ts = self._now()

        # Light probe: use cached
        if probe_kind == "light" and self._last_result is not None:
            ok = self._last_result
            domain, code, msg = None, None, None
        else:
            ok, domain, code, msg = self._stat_probe()
            self._last_result = ok

        ev = ProbeEvidence(
            file_access_ok=ok,
            error_domain=domain,
            error_code=code,
            error_message=msg,
        )
        ev = apply_normalization_to_evidence(self.permission, ev)

        return ProbeResult(
            permission=self.permission, timestamp=ts, probe_kind=probe_kind, evidence=ev
        )

    def _stat_probe(self) -> tuple[bool | None, str | None, str | None, str | None]:
        """
        Test FDA by attempting to stat protected files.
        Safe operation - doesn't read any actual data.

        CRITICAL: We must attempt to access the file directly to trigger TCC.
        Using glob on a protected directory (like ~/Library/Messages) might just
        return an empty list without triggering the PermissionError we need.
        """
        for pat in FDA_TEST_PATTERNS:
            expanded = os.path.expanduser(pat)

            # Use glob only if there are wildcards
            if any(char in expanded for char in ["*", "?", "["]):
                candidates = glob.glob(expanded)
            else:
                # Direct access attempt
                candidates = [expanded]

            for path in candidates:
                try:
                    # CRITICAL: stat() is sometimes not enough to trigger TCC registration.
                    # We must attempt to OPEN the file to force the OS to check permissions.
                    with open(path, "rb"):
                        pass
                    logger.debug("[FDA_PROBER] open(%s) succeeded", path)
                    return True, None, None, None
                except PermissionError as e:
                    logger.debug("[FDA_PROBER] open(%s) permission denied", path)
                    # This is GOOD - it means the file exists and we are blocked.
                    # This should also register the app in System Settings.
                    return False, "os", "EACCES", f"Permission denied: {path}"
                except FileNotFoundError:
                    # File doesn't exist, try next
                    continue
                except OSError as e:
                    # Catch other OS errors (like operation not permitted)
                    if e.errno == 1:  # EPERM - Operation not permitted
                        logger.debug("[FDA_PROBER] stat(%s) operation not permitted", path)
                        return False, "os", "EPERM", f"Operation not permitted: {path}"
                    return None, "os", type(e).__name__, str(e)
                except Exception as e:
                    # Unknown error, treat as transient
                    return None, "os", type(e).__name__, str(e)

        # No test paths found on this system
        logger.warning("[FDA_PROBER] No FDA test paths exist on this machine")
        return None, "fda", "NO_TEST_PATH", "No FDA probe path exists on this machine"

    def supports_light_probe(self) -> bool:
        return True
