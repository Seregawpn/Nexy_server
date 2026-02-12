"""
Types for MCP Action Executor.
"""

from dataclasses import dataclass


@dataclass
class McpActionConfig:
    """Конфигурация MCP Action Executor."""

    open_app_server_path: str
    close_app_server_path: str
    timeout_sec: float = 10.0
    enabled: bool = True


@dataclass
class McpActionResult:
    """Результат выполнения MCP действия."""

    success: bool
    message: str
    error: str | None = None
    app_name: str | None = None
