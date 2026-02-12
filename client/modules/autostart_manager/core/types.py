"""
Типы данных для модуля автозапуска.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Literal


class AutostartStatus(Enum):
    """Статус автозапуска."""
    ENABLED = "enabled"
    DISABLED = "disabled"
    ERROR = "error"

@dataclass
class AutostartConfig:
    """Конфигурация модуля автозапуска."""
    enabled: bool = False
    delay_seconds: int = 5
    method: Literal["launch_agent"] = "launch_agent"
    launch_agent_path: str = "~/Library/LaunchAgents/com.nexy.assistant.plist"
    bundle_id: str = "com.nexy.assistant"
