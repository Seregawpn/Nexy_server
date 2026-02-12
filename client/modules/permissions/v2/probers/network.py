"""
Permission System V2 - Network Prober

Probes Network permission by attempting to create socket connections.
This triggers the macOS Firewall or "Local Network" permission dialogs.
"""

from __future__ import annotations

import logging
import socket
from typing import Literal

from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class NetworkProber(BaseProber):
    """Prober for Network permission (Firewall/Local Network)."""

    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.NETWORK

    async def trigger(self) -> None:
        """
        Trigger Network permission request.
        Attempts both outgoing connection and incoming bind to trigger relevant dialogs.
        Also shows a simulated dialog to provide a consistent UX.
        """
        logger.debug("[NETWORK_PROBER] Triggering network requests...")

        # 0. Trigger Local Network Permission (Native System Dialog)
        # Attempting to access a local network address triggers the "Local Network" privacy prompt on macOS.
        try:
            # Creating a UDP socket and sending data to a local broadcast address
            # is a reliable way to trigger the permission prompt.
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0.1)
            try:
                # 255.255.255.255 is the global broadcast address, but often local broadcast
                # or a specific local IP is needed to trigger the specific prompt.
                # We try a common local IP pattern.
                s.connect(("192.168.1.1", 80))
                s.send(b"trigger_permission")
            except Exception:
                # Connection might fail if the IP doesn't exist, which is fine.
                # The attempt itself registers the intent.
                pass
            finally:
                s.close()
            logger.debug("[NETWORK_PROBER] Local Network trigger attempted")
        except Exception as e:
            logger.warning("[NETWORK_PROBER] Failed to trigger Local Network prompt: %s", e)

        # 1. Trigger Outgoing Connection (DNS usually safe)
        # This might trigger "Nexy would like to access the local network" or similar check
        try:
            # Connect to valid public DNS
            s = socket.create_connection(("8.8.8.8", 53), timeout=1.0)
            s.close()
            logger.debug("[NETWORK_PROBER] Outgoing connection triggered")
        except Exception as e:
            logger.debug("[NETWORK_PROBER] Outgoing connection failed (expected if offline): %s", e)

        # 2. Trigger Incoming Connection (Bind)
        # This triggers the macOS Firewall "Do you want the application... to accept incoming..." dialog
        try:
            s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind to random port on all interfaces
            s_in.bind(("", 0))
            s_in.listen(1)
            port = s_in.getsockname()[1]
            logger.debug("[NETWORK_PROBER] Bound to port %d for firewall trigger", port)
            s_in.close()
        except Exception as e:
            logger.warning("[NETWORK_PROBER] Bind failed: %s", e)

    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe Network capability."""
        ts = self._now()

        # We can't easily check if "permission is granted" because network access
        # is usually allowed by default unless blocked by Firewall/Little Snitch.
        # So we assume it works if we can make a call, OR we just assume pass
        # because we only want to show the dialog during first run.

        is_connected = False
        try:
            # Simple check
            socket.create_connection(("8.8.8.8", 53), timeout=0.5).close()
            is_connected = True
        except:
            pass

        # We always return "Ok" because failure to connect might just mean offline,
        # not permission denied. And we don't want to block the wizard for offline users.
        # The goal is to ensure the DIALOG was triggered if applicable.

        ev = ProbeEvidence(
            network_conn_ok=True,  # Always consider "ok" to pass the step
            misconfig_hint=False,
        )

        return ProbeResult(
            permission=self.permission, timestamp=ts, probe_kind=probe_kind, evidence=ev
        )
