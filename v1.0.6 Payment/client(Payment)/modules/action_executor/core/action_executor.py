"""
ActionExecutor — локальный исполнитель действий (open_app) без MCP зависимостей.

Использует direct режим: /usr/bin/open для открытия приложений на macOS.
"""

import asyncio
import logging
import os
from typing import Any, Dict, Optional

from .types import ActionExecutorConfig, ActionResult

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"

logger = logging.getLogger(__name__)


class ActionExecutor:
    """Локальный исполнитель действий (open_app) без MCP зависимостей."""

    def __init__(self, config: ActionExecutorConfig):
        self._config = config
        self._binary = config.binary or "/usr/bin/open"
        self._allowed = {app.lower(): app for app in config.allowed_apps or []}
        logger.info(
            "[%s] ActionExecutor created enabled=%s timeout=%.1fs binary=%s",
            FEATURE_ID,
            config.enabled,
            config.timeout_sec,
            self._binary,
        )

    def is_enabled(self) -> bool:
        """Проверяет, включен ли executor."""
        return bool(self._config.enabled)

    async def execute(self, action_data: Dict[str, Any]) -> ActionResult:
        """
        Выполняет действие open_app.
        
        Args:
            action_data: Словарь с данными действия:
                - type: str - тип действия (должен быть "open_app")
                - app_name: str - имя приложения (например, "Safari")
                - app_path: str (опционально) - путь к приложению
        
        Returns:
            ActionResult с результатом выполнения
        """
        if not self._config.enabled:
            return ActionResult(
                success=False,
                message="Actions are disabled",
                error="disabled",
            )

        action_type = (action_data or {}).get("type")
        if action_type != "open_app":
            return ActionResult(
                success=False,
                message=f"Unsupported action type: {action_type}",
                error="unsupported_action",
            )

        app_name = self._normalize_app_name(action_data.get("app_name"))
        app_path = self._normalize_path(action_data.get("app_path"))

        if not app_name and not app_path:
            return ActionResult(
                success=False,
                message="Missing app_name or app_path",
                error="invalid_payload",
            )

        # Проверка whitelist (если список не пустой)
        if self._allowed and app_name:
            if app_name.lower() not in self._allowed:
                logger.warning(
                    "[%s] App '%s' is not in allowed list: %s",
                    FEATURE_ID,
                    app_name,
                    list(self._allowed.keys()),
                )
                return ActionResult(
                    success=False,
                    message=f"App '{app_name}' is not allowed",
                    error="not_allowed",
                    app_name=app_name,
                )

        cmd = await self._build_command(app_name=app_name, app_path=app_path)
        if cmd is None:
            return ActionResult(
                success=False,
                message="Executor binary not found",
                error="binary_missing",
                app_name=app_name,
            )

        logger.info("[%s] Running command: %s", FEATURE_ID, cmd)
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        except FileNotFoundError:
            logger.error("[%s] Binary not found: %s", FEATURE_ID, cmd[0])
            return ActionResult(
                success=False,
                message="Executor binary missing",
                error="binary_missing",
                app_name=app_name,
            )
        except Exception as exc:
            logger.error("[%s] Failed to spawn process: %s", FEATURE_ID, exc)
            return ActionResult(
                success=False,
                message=str(exc),
                error="spawn_failed",
                app_name=app_name,
            )

        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=self._config.timeout_sec,
            )
        except asyncio.TimeoutError:
            process.kill()
            await process.communicate()
            logger.error(
                "[%s] Command timed out (%.1fs)", FEATURE_ID, self._config.timeout_sec
            )
            return ActionResult(
                success=False,
                message="Action timed out",
                error="timeout",
                app_name=app_name,
            )

        if process.returncode != 0:
            err_text = (stderr or b"").decode("utf-8", errors="ignore").strip()
            logger.error(
                "[%s] Command failed rc=%s error=%s",
                FEATURE_ID,
                process.returncode,
                err_text,
            )
            return ActionResult(
                success=False,
                message=err_text or "Failed to open application",
                error="command_failed",
                app_name=app_name,
            )

        logger.info("[%s] Successfully opened app: %s", FEATURE_ID, app_name or app_path)
        return ActionResult(
            success=True,
            message=f"Opened {app_name or app_path}",
            app_name=app_name,
        )

    async def _build_command(
        self,
        *,
        app_name: Optional[str],
        app_path: Optional[str],
    ) -> Optional[list]:
        """
        Формирует команду запуска приложения.
        
        Args:
            app_name: Имя приложения (например, "Safari")
            app_path: Путь к приложению (например, "/Applications/Safari.app")
        
        Returns:
            Список аргументов для subprocess или None, если binary не найден
        """
        binary = self._binary
        if not binary or not os.path.exists(binary):
            return None

        if app_path:
            return [binary, app_path]

        if app_name:
            return [binary, "-a", app_name]

        return None

    def _normalize_app_name(self, value: Optional[str]) -> Optional[str]:
        """
        Нормализует имя приложения.
        
        Удаляет расширение .app, если оно есть.
        """
        if not value:
            return None
        normalized = value.strip()
        if normalized.lower().endswith(".app"):
            normalized = normalized[:-4]
        return normalized or None

    def _normalize_path(self, value: Optional[str]) -> Optional[str]:
        """Нормализует путь к приложению."""
        if not value:
            return None
        return value.strip() or None

