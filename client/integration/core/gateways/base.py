"""
Base types and utilities for decision gateways.

Provides DecisionCtx for structured decision context and log_decision for canonical logging.
"""
from __future__ import annotations

from dataclasses import dataclass
import logging
import time
from typing import Any

from integration.core.selectors import Snapshot

from .types import Decision

logger = logging.getLogger(__name__)


@dataclass
class DecisionCtx:
    """Structured context for decision logging."""

    mic: str
    screen: str
    accessibility: str
    device: str
    network: str
    firstRun: bool
    appMode: str
    update_in_progress: bool | None = None
    whatsapp: str | None = None
    extra: dict[str, Any] | None = None

    def to_log_string(self) -> str:
        """Generate canonical log context string."""
        parts = [
            f"mic={self.mic}",
            f"screen={self.screen}",
            f"accessibility={self.accessibility}",
            f"device={self.device}",
            f"network={self.network}",
            f"firstRun={self.firstRun}",
            f"appMode={self.appMode}",
        ]
        
        if self.update_in_progress is not None:
            parts.append(f"update_in_progress={self.update_in_progress}")

        if self.whatsapp is not None:
            parts.append(f"whatsapp={self.whatsapp}")
        
        return f"ctx={{{','.join(parts)}}}"


def create_ctx_from_snapshot(s: Snapshot) -> DecisionCtx:
    """Create DecisionCtx from Snapshot."""
    return DecisionCtx(
        mic=s.perm_mic.value,
        screen=s.perm_screen.value,
        accessibility=s.perm_accessibility.value,
        device=s.device_input.value,
        network=s.network.value,
        firstRun=s.first_run,
        appMode=s.app_mode.value,
        update_in_progress=getattr(s, "update_in_progress", None),
        whatsapp= getattr(s.whatsapp_status, "value", "disconnected") if hasattr(s, "whatsapp_status") else None,
    )


def log_decision(
    gateway_name: str,
    decision: Decision,
    ctx: DecisionCtx,
    *,
    source: str,
    started_at: float,
    reason: str | None = None,
) -> str:
    """
    Log decision in canonical format and return log string.
    
    Args:
        gateway_name: Name of the gateway making the decision
        decision: Decision outcome
        ctx: Decision context
        source: Source domain (e.g., "audio", "permission_restart")
        started_at: Timestamp when decision started (for duration calculation)
        reason: Optional reason for the decision
    
    Returns:
        Canonical log string for tests
    """
    duration_ms = int((time.time() - started_at) * 1000)
    
    reason_part = f" reason={reason}" if reason else ""
    ctx_str = ctx.to_log_string()
    log_msg = f"decision={decision.value}{reason_part} {ctx_str} source={source} duration_ms={duration_ms}"
    
    # Log through logger (for backward compatibility)
    level = "info" if decision == Decision.ABORT else "debug"
    log_fn = getattr(logger, level, logger.info)
    log_fn(log_msg)
    
    return log_msg
