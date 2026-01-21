"""
McpActionExecutor — исполнитель действий через MCP серверы.

Поддерживает open_app и close_app через отдельные MCP серверы.
Feature ID: F-2025-014-close-app
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

from integration.utils.resource_path import get_resource_path

from .types import McpActionConfig, McpActionResult

FEATURE_ID = "F-2025-014-close-app"

logger = logging.getLogger(__name__)


class McpActionExecutor:
    """Исполнитель действий через MCP серверы."""

    def __init__(self, config: McpActionConfig):
        """
        Инициализация исполнителя.

        Args:
            config: Конфигурация исполнителя
        """
        self.config = config
        logger.info(
            "[%s] McpActionExecutor initialized: open_app_server=%s, close_app_server=%s, timeout=%.1fs",
            FEATURE_ID,
            config.open_app_server_path,
            config.close_app_server_path,
            config.timeout_sec,
        )

    async def execute_action(
        self,
        action_data: Dict[str, Any],
        session_id: Optional[str] = None,
    ) -> McpActionResult:
        """
        Выполняет действие через MCP сервер.

        Args:
            action_data: Данные действия с полем "type" ("open_app" или "close_app")
            session_id: ID сессии для логирования

        Returns:
            Результат выполнения действия
        """
        # Определяем тип действия
        action_type = action_data.get("type")
        if action_type not in ["open_app", "close_app"]:
            return McpActionResult(
                success=False,
                message=f"Unknown action type: {action_type}",
                error="unknown_action_type",
            )

        # Определяем путь к MCP серверу
        if action_type == "open_app":
            server_path = self.config.open_app_server_path
        elif action_type == "close_app":
            server_path = self.config.close_app_server_path
        else:
            return McpActionResult(
                success=False,
                message=f"Unknown action type: {action_type}",
                error="unknown_action_type",
            )

        # Подготовка аргументов для инструмента
        tool_name = action_type  # "open_app" или "close_app"
        tool_args = {}

        if action_type == "open_app":
            if action_data.get("app_name"):
                tool_args["app_name"] = action_data["app_name"]
            elif action_data.get("app_path"):
                tool_args["app_path"] = action_data["app_path"]
            else:
                return McpActionResult(
                    success=False,
                    message="Missing app_name or app_path for open_app",
                    error="missing_parameter",
                )
        elif action_type == "close_app":
            if action_data.get("app_name"):
                tool_args["app_name"] = action_data["app_name"]
            else:
                return McpActionResult(
                    success=False,
                    message="Missing app_name for close_app",
                    error="missing_parameter",
                )

        # Resolve MCP server path before execution
        resolved_server_path = self._resolve_server_path(server_path, action_type)
        if not resolved_server_path:
            error_msg = f"MCP server not found for {action_type}: {server_path}"
            logger.error(
                "[%s] %s, session=%s",
                FEATURE_ID,
                error_msg,
                session_id or "unknown",
            )
            return McpActionResult(
                success=False,
                message=error_msg,
                error="server_not_found",
                app_name=action_data.get("app_name"),
            )

        # Выполнение через MCP
        try:
            server_params = StdioServerParameters(
                command=sys.executable,
                args=[str(resolved_server_path)],
            )

            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()

                    logger.info(
                        "[%s] Calling MCP tool '%s' with args: %s, session=%s",
                        FEATURE_ID,
                        tool_name,
                        tool_args,
                        session_id or "unknown",
                    )

                    result = await asyncio.wait_for(
                        session.call_tool(tool_name, tool_args),
                        timeout=self.config.timeout_sec,
                    )

                    # Обработка результата
                    if result.content and len(result.content) > 0:
                        # Проверяем тип контента - только TextContent имеет атрибут text
                        first_content = result.content[0]
                        if isinstance(first_content, TextContent):
                            result_text = first_content.text
                        else:
                            # Для других типов контента (ImageContent, AudioContent и т.д.)
                            # используем строковое представление или пропускаем
                            logger.warning(
                                "[%s] MCP action returned non-text content: %s, session=%s",
                                FEATURE_ID,
                                type(first_content).__name__,
                                session_id or "unknown",
                            )
                            return McpActionResult(
                                success=False,
                                message="MCP action returned non-text content",
                                error="unsupported_content_type",
                                app_name=action_data.get("app_name"),
                            )

                        if result_text.startswith("❌"):
                            # Ошибка
                            error_msg = result_text.replace("❌", "").strip()
                            logger.error(
                                "[%s] MCP action failed: %s, session=%s",
                                FEATURE_ID,
                                error_msg,
                                session_id or "unknown",
                            )
                            return McpActionResult(
                                success=False,
                                message=error_msg,
                                error="mcp_error",
                                app_name=action_data.get("app_name"),
                            )
                        else:
                            # Успех
                            logger.info(
                                "[%s] MCP action completed: %s, session=%s",
                                FEATURE_ID,
                                result_text,
                                session_id or "unknown",
                            )
                            return McpActionResult(
                                success=True,
                                message=result_text,
                                app_name=action_data.get("app_name"),
                            )
                    else:
                        # Нет содержимого
                        logger.warning(
                            "[%s] MCP action returned no content, session=%s",
                            FEATURE_ID,
                            session_id or "unknown",
                        )
                        return McpActionResult(
                            success=True,
                            message="Action completed (no response)",
                            app_name=action_data.get("app_name"),
                        )

        except asyncio.TimeoutError:
            error_msg = f"MCP action timeout after {self.config.timeout_sec}s"
            logger.error(
                "[%s] %s, session=%s",
                FEATURE_ID,
                error_msg,
                session_id or "unknown",
            )
            return McpActionResult(
                success=False,
                message=error_msg,
                error="timeout",
                app_name=action_data.get("app_name"),
            )

        except Exception as exc:
            error_msg = f"MCP action error: {self._format_exception(exc)}"
            logger.error(
                "[%s] %s, session=%s",
                FEATURE_ID,
                error_msg,
                session_id or "unknown",
                exc_info=True,
            )
            return McpActionResult(
                success=False,
                message=error_msg,
                error="execution_error",
                app_name=action_data.get("app_name"),
            )

    @staticmethod
    def _resolve_server_path(server_path: str, action_type: str) -> Optional[Path]:
        if not server_path:
            logger.error(
                "[%s] Empty MCP server path for action=%s",
                FEATURE_ID,
                action_type,
            )
            return None

        direct_path = Path(server_path)
        if direct_path.exists():
            return direct_path.resolve()

        resolved = get_resource_path(server_path)
        if resolved.exists():
            logger.info(
                "[%s] Resolved MCP server path for %s: %s -> %s",
                FEATURE_ID,
                action_type,
                server_path,
                resolved,
            )
            return resolved.resolve()

        logger.error(
            "[%s] MCP server path does not exist for %s: %s (resolved: %s)",
            FEATURE_ID,
            action_type,
            server_path,
            resolved,
        )
        return None

    @staticmethod
    def _format_exception(exc: Exception) -> str:
        if isinstance(exc, BaseExceptionGroup) and getattr(exc, "exceptions", None):
            parts = []
            for sub_exc in exc.exceptions:
                parts.append(f"{type(sub_exc).__name__}: {sub_exc}")
            return f"{type(exc).__name__}({len(parts)}): " + "; ".join(parts)
        return f"{type(exc).__name__}: {exc}"
