"""
McpActionExecutor — исполнитель действий через MCP серверы.

Поддерживает open_app и close_app через отдельные MCP серверы.
Feature ID: F-2025-014-close-app
"""

import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

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
            action_data: Данные действия с полем "command" или "type" 
                        ("open_app", "close_app", "read_messages", "send_message")
            session_id: ID сессии для логирования

        Returns:
            Результат выполнения действия
        """
        # ⚠️ КРИТИЧНО: Поддержка и "command", и "type" для обратной совместимости
        # Приоритет: command > type (command - новый формат, type - старый для open_app/close_app)
        action_type = action_data.get("command") or action_data.get("type")
        
        if not action_type:
            return McpActionResult(
                success=False,
                message="Missing 'command' or 'type' field in action_data",
                error="missing_command_or_type",
            )
        
        # Поддерживаемые команды: существующие (open_app, close_app) + новые (read_messages, send_message)
        supported_commands = ["open_app", "close_app", "read_messages", "send_message"]
        if action_type not in supported_commands:
            return McpActionResult(
                success=False,
                message=f"Unknown action type: {action_type}. Supported: {supported_commands}",
                error="unknown_action_type",
            )

        # Определяем путь к MCP серверу
        if action_type == "open_app":
            server_path = self.config.open_app_server_path
        elif action_type == "close_app":
            server_path = self.config.close_app_server_path
        elif action_type in ["read_messages", "send_message"]:
            # Messages команды используют messages_server_path
            server_path = getattr(self.config, 'messages_server_path', None)
            if not server_path:
                return McpActionResult(
                    success=False,
                    message="Messages MCP server path not configured",
                    error="missing_messages_server_path",
                )
        else:
            return McpActionResult(
                success=False,
                message=f"Unknown action type: {action_type}",
                error="unknown_action_type",
            )

        # Подготовка аргументов для инструмента
        tool_name = action_type  # "open_app", "close_app", "read_messages", или "send_message"
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
        elif action_type == "read_messages":
            # read_messages: contact (required), limit (optional, default 10, max 50)
            args = action_data.get("args", {})
            if not args.get("contact"):
                return McpActionResult(
                    success=False,
                    message="Missing 'contact' parameter for read_messages",
                    error="missing_parameter",
                )
            tool_args["contact"] = args["contact"]
            if "limit" in args:
                limit = args["limit"]
                if not isinstance(limit, int) or limit < 1 or limit > 50:
                    return McpActionResult(
                        success=False,
                        message="'limit' must be an integer between 1 and 50",
                        error="invalid_parameter",
                    )
                tool_args["limit"] = limit
        elif action_type == "send_message":
            # send_message: contact (required), message (required), phone_number (optional)
            args = action_data.get("args", {})
            if not args.get("contact"):
                return McpActionResult(
                    success=False,
                    message="Missing 'contact' parameter for send_message",
                    error="missing_parameter",
                )
            if not args.get("message"):
                return McpActionResult(
                    success=False,
                    message="Missing 'message' parameter for send_message",
                    error="missing_parameter",
                )
            tool_args["contact"] = args["contact"]
            tool_args["message"] = args["message"]
            if "phone_number" in args:
                tool_args["phone_number"] = args["phone_number"]

        # Выполнение через MCP
        try:
            server_params = StdioServerParameters(
                command="python3",
                args=[str(Path(server_path).absolute())],
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
                        result_text = result.content[0].text

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
            error_msg = f"MCP action error: {str(exc)}"
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