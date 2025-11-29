"""
MCP Action Module — модуль для выполнения действий через MCP серверы.

Поддерживает open_app и close_app через отдельные MCP серверы.
Feature ID: F-2025-014-close-app
"""

from .core.mcp_action_executor import McpActionExecutor, McpActionResult
from .core.types import McpActionConfig

__all__ = ["McpActionExecutor", "McpActionResult", "McpActionConfig"]

