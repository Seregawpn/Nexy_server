"""
ActionExecutionIntegration — выполнение действий open_app и close_app на клиенте.

Подписывается на grpc.response.action и запускает McpActionExecutor для выполнения команд через MCP.
Feature ID: F-2025-016-mcp-app-opening-integration
"""

import asyncio
import json
import logging
from typing import Any, Dict, Optional, Set

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from config.unified_config_loader import UnifiedConfigLoader, OpenAppActionConfig
from modules.mcp_action import McpActionExecutor, McpActionConfig
from modules.action_errors.messages import resolver as action_error_resolver

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"

from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)


class ActionExecutionIntegration(BaseIntegration):
    """Подписывается на grpc.response.action и запускает McpActionExecutor для выполнения действий через MCP."""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="ActionExecutionIntegration",
        )
        
        # Загружаем конфигурацию из unified_config
        loader = UnifiedConfigLoader.get_instance()
        actions_cfg = loader.get_actions_config().get("open_app") or OpenAppActionConfig()
        
        # Сохраняем конфигурацию open_app для совместимости
        self._open_app_config = actions_cfg
        
        # McpActionExecutor для open_app и close_app (через MCP)
        # Загружаем конфигурацию MCP серверов из unified_config
        mcp_configs = loader.get_mcp_config()
        open_app_mcp = mcp_configs.get('open_app', {})
        close_app_mcp = mcp_configs.get('close_app', {})
        
        # Преобразуем относительные пути в абсолютные
        from pathlib import Path
        # Определяем корень проекта Nexy (client(prod) находится в Nexy/client(prod))
        # __file__ = client(prod)/integration/integrations/action_execution_integration.py
        # Нужно подняться на 4 уровня: integrations -> integration -> client(prod) -> Nexy
        # 0: action_execution_integration.py
        # 1: integrations
        # 2: integration
        # 3: client(prod)
        # 4: Nexy
        nexy_root = Path(__file__).parent.parent.parent.parent
        
        open_app_server_path = open_app_mcp.get('server_path', '')
        close_app_server_path = close_app_mcp.get('server_path', '')
        
        # Если путь относительный, делаем его абсолютным относительно корня Nexy
        if open_app_server_path and not Path(open_app_server_path).is_absolute():
            # Путь уже относительно Nexy root (без "../")
            open_app_server_path = str((nexy_root / open_app_server_path).resolve())
        if close_app_server_path and not Path(close_app_server_path).is_absolute():
            close_app_server_path = str((nexy_root / close_app_server_path).resolve())
        
        # Fallback на пути по умолчанию, если конфигурация не найдена
        if not open_app_server_path:
            open_app_server_path = str(nexy_root / "mcp_close_app_test" / "server" / "app_launcher_server.py")
        if not close_app_server_path:
            close_app_server_path = str(nexy_root / "mcp_close_app_test" / "server" / "close_app_server.py")
        
        mcp_config = McpActionConfig(
            open_app_server_path=open_app_server_path,
            close_app_server_path=close_app_server_path,
            timeout_sec=float(close_app_mcp.get('timeout_sec', actions_cfg.timeout_sec)),
            enabled=bool(close_app_mcp.get('enabled', actions_cfg.enabled)),
        )
        self._mcp_executor = McpActionExecutor(mcp_config)
        self._actions_lock = asyncio.Lock()
        self._active_actions: Dict[str, asyncio.Task] = {}  # session_id -> task
        self._active_apps: Dict[str, str] = {}  # app_name -> session_id (для идемпотентности close_app)
        self._spoken_error_sessions: Set[str] = set()
        
        logger.info(
            "[%s] ActionExecutionIntegration initialized: enabled=%s, timeout=%.1fs, open_app_server=%s, close_app_server=%s",
            FEATURE_ID,
            mcp_config.enabled,
            mcp_config.timeout_sec,
            open_app_server_path,
            close_app_server_path
        )

    async def _do_initialize(self) -> bool:
        """Инициализация интеграции."""
        return True

    async def _do_start(self) -> bool:
        """Запуск интеграции - подписка на события."""
        if not self._mcp_executor.config.enabled:
            logger.info("[%s] MCP action executor disabled, skipping start", FEATURE_ID)
            return True

        await self.event_bus.subscribe(
            "grpc.response.action",
            self._on_action_received,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "interrupt.request",
            self._on_interrupt,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "keyboard.short_press",
            self._on_keyboard_short_press,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "app.mode_changed",
            self._on_mode_changed,
            EventPriority.HIGH,
        )
        logger.info("[%s] ActionExecutionIntegration started", FEATURE_ID)
        return True

    async def _do_stop(self) -> bool:
        """Остановка интеграции - отмена всех действий и отписка от событий."""
        if not self._mcp_executor.config.enabled:
            return True
        
        await self._cancel_all_actions(reason="integration_stop")
        await self.event_bus.unsubscribe("grpc.response.action", self._on_action_received)
        await self.event_bus.unsubscribe("interrupt.request", self._on_interrupt)
        await self.event_bus.unsubscribe("keyboard.short_press", self._on_keyboard_short_press)
        await self.event_bus.unsubscribe("app.mode_changed", self._on_mode_changed)
        logger.info("[%s] ActionExecutionIntegration stopped", FEATURE_ID)
        return True

    async def _on_action_received(self, event: Dict[str, Any]):
        """
        Получает JSON действия из grpc.response.action.
        
        Ожидаемый формат события:
        {
            "session_id": "...",
            "action_json": "{...}",  # JSON строка с command_payload
            "feature_id": "F-2025-016-mcp-app-opening-integration"
        }
        """
        # Извлекаем данные из события
        data = event.get("data", event) if isinstance(event, dict) and "data" in event else event
        session_id = data.get("session_id")
        action_json = data.get("action_json")
        feature_id = data.get("feature_id") or FEATURE_ID

        if not self._mcp_executor.config.enabled:
            logger.info("[%s] MCP actions disabled, ignoring payload", feature_id)
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="disabled",
                message="MCP action executor disabled",
                app_name=None,
            )
            return

        if not session_id or not action_json:
            logger.error("[%s] Invalid grpc.response.action payload: %s", feature_id, data)
            return

        # Парсим JSON
        try:
            action_data = json.loads(action_json)
        except json.JSONDecodeError as exc:
            logger.error("[%s] Invalid action JSON: %s", feature_id, exc)
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="invalid_json",
                message=str(exc),
                app_name=None,
            )
            return

        # Определяем тип команды и feature_id
        command = action_data.get("command")
        action_type = command  # "open_app" или "close_app"
        
        # Расширяем валидацию типов для поддержки close_app
        valid_commands = ["open_app", "close_app"]
        if command not in valid_commands:
            logger.warning(
                "[%s] Unsupported command: %s",
                feature_id,
                command
            )
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="unsupported_command",
                message=f"Unsupported command: {command}",
                app_name=None,
            )
            return
        
        # Обновляем feature_id в зависимости от типа действия
        if command == "open_app":
            action_feature_id = "F-2025-013-open-app"
        elif command == "close_app":
            action_feature_id = "F-2025-014-close-app"
        else:
            action_feature_id = feature_id
        
        # Валидация параметров в зависимости от типа действия
        args = action_data.get("args", {})
        if command == "open_app":
            # Для open_app требуется app_name или app_path
            if not args.get("app_name") and not args.get("app_path"):
                logger.error(
                    "[%s] Missing app_name or app_path for open_app",
                    action_feature_id
                )
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing app_name or app_path for open_app",
                    app_name=None,
                )
                return
        elif command == "close_app":
            # Для close_app требуется только app_name
            if not args.get("app_name"):
                logger.error(
                    "[%s] Missing app_name for close_app",
                    action_feature_id
                )
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing app_name for close_app",
                    app_name=None,
                )
                return

        # Преобразуем формат для McpActionExecutor
        # McpActionExecutor ожидает: {"type": "open_app" или "close_app", "app_name": "...", "app_path": "..."}
        executor_action_data = {
            "type": action_type,
            "app_name": args.get("app_name"),
            "app_path": args.get("app_path"),
        }

        # Защита от дублирования: проверяем, не выполняется ли уже действие для этой сессии
        async with self._actions_lock:
            if session_id in self._active_actions:
                logger.info("[%s] Action already running for session=%s", feature_id, session_id)
                return
            
            # Идемпотентность для close_app: проверяем, не закрывается ли уже это приложение
            action_type = executor_action_data.get("type")
            app_name = executor_action_data.get("app_name")
            if action_type == "close_app" and app_name:
                if app_name in self._active_apps:
                    existing_session = self._active_apps[app_name]
                    logger.info(
                        "[%s] close_app already running for app=%s (session=%s, new_session=%s)",
                        feature_id,
                        app_name,
                        existing_session,
                        session_id
                    )
                    return
                # Регистрируем приложение как активное
                self._active_apps[app_name] = session_id
            
            # Создаем задачу для выполнения действия
            task = asyncio.create_task(
                self._execute_action(
                    session_id=session_id,
                    action_data=executor_action_data,
                    feature_id=action_feature_id
                )
            )
            self._active_actions[session_id] = task

    async def _execute_action(
        self,
        *,
        session_id: str,
        action_data: Dict[str, Any],
        feature_id: str
    ):
        """
        Выполняет действие через McpActionExecutor.
        
        Args:
            session_id: ID сессии
            action_data: Данные действия для McpActionExecutor
            feature_id: ID фичи для логирования
        """
        # Определяем тип действия для событий
        action_type = action_data.get("type", "open_app")
        event_prefix = f"actions.{action_type}"
        
        # Публикуем событие о начале выполнения
        await self.event_bus.publish(
            f"{event_prefix}.started",
            {
                "session_id": session_id,
                "feature_id": feature_id,
                "action": action_data,
            },
        )
        self._spoken_error_sessions.discard(session_id)
        
        try:
            # Выполняем действие в зависимости от типа
            if action_type == "open_app":
                # Используем McpActionExecutor для open_app (через MCP)
                result = await self._mcp_executor.execute_action(
                    action_data,
                    session_id=session_id
                )
            elif action_type == "close_app":
                # Используем McpActionExecutor для close_app (через MCP)
                result = await self._mcp_executor.execute_action(
                    action_data,
                    session_id=session_id
                )
            else:
                # Неизвестный тип действия
                from modules.mcp_action import McpActionResult
                result = McpActionResult(
                    success=False,
                    message=f"Unsupported action type: {action_type}",
                    error="unsupported_action",
                )
            
            if result.success:
                # Успешное выполнение
                await self.event_bus.publish(
                    f"{event_prefix}.completed",
                    {
                        "session_id": session_id,
                        "feature_id": feature_id,
                        "message": result.message,
                        "app_name": result.app_name,
                    },
                )
                logger.info(
                    "[%s] Action completed successfully: %s",
                    feature_id,
                    result.app_name or "unknown"
                )
            else:
                # Ошибка выполнения
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=feature_id,
                    error_code=result.error or "unknown",
                    message=result.message,
                    app_name=result.app_name or action_data.get("app_name"),
                )
                logger.warning(
                    "[%s] Action failed: %s - %s",
                    feature_id,
                    result.error,
                    result.message
                )
                
        except asyncio.CancelledError:
            # Действие было отменено
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="cancelled",
                message="Action cancelled",
                app_name=action_data.get("app_name"),
            )
            logger.info("[%s] Action cancelled for session=%s", feature_id, session_id)
            
        except Exception as exc:
            # Неожиданная ошибка
            await self._handle_error(exc, where="_execute_action")
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="unexpected",
                message=str(exc),
                app_name=action_data.get("app_name"),
            )
            logger.error(
                "[%s] Unexpected error executing action: %s",
                feature_id,
                exc
            )
        finally:
            # Удаляем задачу из активных
            async with self._actions_lock:
                task = self._active_actions.pop(session_id, None)
                if task and not task.done():
                    task.cancel()
                
                # Удаляем приложение из активных (для идемпотентности close_app)
                action_type = action_data.get("type")
                app_name = action_data.get("app_name")
                if action_type == "close_app" and app_name:
                    if self._active_apps.get(app_name) == session_id:
                        self._active_apps.pop(app_name, None)
                        logger.debug(
                            "[%s] Removed app from active_apps: %s (session=%s)",
                            feature_id,
                            app_name,
                            session_id
                        )

    async def _on_interrupt(self, event: Dict[str, Any]):
        """Обработка прерывания - отмена всех действий."""
        await self._cancel_all_actions(reason="interrupt")

    async def _on_keyboard_short_press(self, event: Dict[str, Any]):
        """Обработка короткого нажатия клавиши - отмена всех действий."""
        await self._cancel_all_actions(reason="keyboard_short_press")

    async def _on_mode_changed(self, event: Dict[str, Any]):
        """Обработка изменения режима приложения - отмена при переходе в спящий режим."""
        try:
            from modules.mode_management import AppMode
            data = event.get("data", event) if isinstance(event, dict) and "data" in event else event
            new_mode = data.get("mode")
            
            # Если передана строка, пытаемся конвертировать в AppMode для надежности
            if isinstance(new_mode, str):
                try:
                    new_mode = AppMode(new_mode)
                except ValueError:
                    pass
            
            if new_mode == AppMode.SLEEPING:
                logger.debug("[%s] Mode changed to SLEEPING, cancelling all actions", FEATURE_ID)
                await self._cancel_all_actions(reason="mode_change_to_sleeping")
        except Exception as e:
            logger.warning("[%s] Error in _on_mode_changed: %s", FEATURE_ID, e)

    async def _cancel_all_actions(self, *, reason: str):
        """
        Отменяет все активные действия.
        
        Args:
            reason: Причина отмены (для логирования)
        """
        async with self._actions_lock:
            tasks = list(self._active_actions.items())
            self._active_actions.clear()

        for session_id, task in tasks:
            if task.done():
                continue
            logger.info(
                "[%s] Cancelling action for session=%s reason=%s",
                FEATURE_ID,
                session_id,
                reason
            )
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    async def _publish_failure(
        self,
        *,
        session_id: Optional[str],
        feature_id: str,
        error_code: Optional[str],
        message: str,
        app_name: Optional[str],
    ) -> None:
        """Публикует событие failure и голосовой фидбек."""
        if session_id:
            payload = {
                "session_id": session_id,
                "feature_id": feature_id,
                "error": error_code or "unknown",
                "message": message,
            }
        else:
            payload = {
                "feature_id": feature_id,
                "error": error_code or "unknown",
                "message": message,
            }
        # Определяем префикс события в зависимости от feature_id
        if "close-app" in feature_id:
            event_name = "actions.close_app.failed"
        else:
            event_name = "actions.open_app.failed"
        await self.event_bus.publish(event_name, payload)
        await self._cancel_active_playback(session_id=session_id, reason=error_code or "action_failed")
        await self._publish_speech_feedback(
            session_id=session_id,
            error_code=error_code,
            app_name=app_name,
            error_message=message,
            feature_id=feature_id,
        )

    async def _cancel_active_playback(self, *, session_id: Optional[str], reason: str) -> None:
        """Останавливает текущее воспроизведение, чтобы не звучала старая реплика."""
        if not session_id:
            return
        try:
            await self.event_bus.publish(
                "playback.cancelled",
                {
                    "session_id": session_id,
                    "source": "actions.open_app",
                    "reason": reason or "action_failed",
                    "feature_id": FEATURE_ID,
                },
            )
        except Exception as exc:
            logger.warning("[%s] Failed to cancel playback: %s", FEATURE_ID, exc)

    async def _publish_speech_feedback(
        self,
        *,
        session_id: Optional[str],
        error_code: Optional[str],
        app_name: Optional[str],
        error_message: Optional[str] = None,
        feature_id: Optional[str] = None,
    ) -> None:
        """Публикует speech.playback.request с описанием ошибки."""
        if not self._open_app_config.speak_errors or not session_id:
            return
        if session_id in self._spoken_error_sessions:
            return

        # Используем переданный feature_id или FEATURE_ID по умолчанию
        used_feature_id = feature_id or FEATURE_ID
        
        # Определяем source в зависимости от feature_id
        if "close-app" in used_feature_id:
            source = "actions.close_app"
        else:
            source = "actions.open_app"

        speech_text = action_error_resolver.resolve(error_code, app_name, error_message)
        await self.event_bus.publish(
            "speech.playback.request",
            {
                "session_id": session_id,
                "feature_id": used_feature_id,
                "source": source,
                "category": "action_error",
                "priority": "high",
                "use_server_tts": self._open_app_config.use_server_tts,
                "voice": "en-US",
                "text": speech_text,
            },
        )
        self._spoken_error_sessions.add(session_id)
        logger.info(
            "[%s] Published speech feedback for session=%s code=%s",
            FEATURE_ID,
            session_id,
            error_code,
        )
