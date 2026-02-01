"""
Shared gateway types.
"""

from __future__ import annotations

from enum import Enum


class Decision(Enum):
    """Decision outcomes for state transitions."""

    START = "start"
    RETRY = "retry"
    ABORT = "abort"
    DEGRADE = "degrade"
    NOTIFY_USER = "notify_user"


__all__ = ["Decision"]

