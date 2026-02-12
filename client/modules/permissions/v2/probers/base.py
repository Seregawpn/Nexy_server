"""
Permission System V2 - Base Prober

Abstract interface for permission probers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import time
from typing import Literal

from ..types import ProbeResult, StepConfig


class BaseProber(ABC):
    """
    Abstract base class for permission probers.

    Each permission has its own prober that:
    1. Checks capability (can we actually use the permission?)
    2. Returns evidence with hints for the classifier
    """

    def __init__(self, config: StepConfig):
        self.config = config
        self.permission = config.permission

    def _now(self) -> float:
        """Get current timestamp."""
        return time.time()

    @abstractmethod
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """
        Probe the permission capability.

        Args:
            probe_kind: "light" for quick cached check, "heavy" for full capability test

        Returns:
            ProbeResult with evidence and hints
        """
        pass

    @abstractmethod
    async def trigger(self) -> None:
        """
        Trigger the permission request (show dialog or open settings).
        Called once at the start of the permission step.
        """
        pass

    def supports_light_probe(self) -> bool:
        """
        Whether this prober supports light probes.
        Override in subclass if light probes are available.
        """
        return False
