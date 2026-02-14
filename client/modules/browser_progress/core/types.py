"""
Browser Progress Types
Types for browser automation progress events.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Any


class BrowserProgressType(StrEnum):
    """Browser progress event types from server"""
    TASK_STARTED = "BROWSER_TASK_STARTED"
    STEP_COMPLETED = "BROWSER_STEP_COMPLETED"
    TASK_COMPLETED = "BROWSER_TASK_COMPLETED"
    TASK_FAILED = "BROWSER_TASK_FAILED"
    TASK_CANCELLED = "BROWSER_TASK_CANCELLED"


@dataclass
class BrowserProgressEvent:
    """Browser progress event data"""
    type: BrowserProgressType
    task_id: str
    session_id: str
    step_number: int = 0
    description: str = ""
    url: str | None = None
    action: str | None = None
    error: str | None = None
    timestamp: datetime | None = None
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BrowserProgressEvent":
        """Create event from dict (from gRPC)"""
        return cls(
            type=BrowserProgressType(data.get("type", "BROWSER_TASK_STARTED")),
            task_id=data.get("task_id", ""),
            session_id=data.get("session_id", ""),
            step_number=data.get("step_number", 0),
            description=data.get("description", ""),
            url=data.get("url"),
            action=data.get("action"),
            error=data.get("error"),
        )
    
    def is_terminal(self) -> bool:
        """Check if this is a terminal event"""
        return self.type in (
            BrowserProgressType.TASK_COMPLETED,
            BrowserProgressType.TASK_FAILED,
            BrowserProgressType.TASK_CANCELLED,
        )
