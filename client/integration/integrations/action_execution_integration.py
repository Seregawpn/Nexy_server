"""
ActionExecutionIntegration — выполнение действий open_app и close_app на клиенте.

Подписывается на grpc.response.action и запускает McpActionExecutor для выполнения команд через MCP.
Feature ID: F-2025-016-mcp-app-opening-integration
"""

import asyncio
import hashlib
import json
from pathlib import Path
import subprocess
import time
from typing import Any

from config.unified_config_loader import OpenAppActionConfig, UnifiedConfigLoader
from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.utils.resource_path import get_user_data_dir
from modules.action_errors.messages import resolver as action_error_resolver
from modules.mcp_action import McpActionConfig, McpActionExecutor

# Messages integration
from modules.messages import (
    connect_db,
    find_contacts_by_name,
    format_message_date,
    get_last_message,
    get_messages_by_contact,
    resolve_contact,
    send_message_to_contact,
)
from modules.permissions.v2.ledger import LedgerStore
from modules.permissions.v2.types import PermissionId, StepState

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"

from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)
ACTION_PIPELINE_TAG = "ACTION_PIPELINE"


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
        open_app_mcp = mcp_configs.get("open_app", {})
        close_app_mcp = mcp_configs.get("close_app", {})

        open_app_server_path = open_app_mcp.get("server_path", "")
        close_app_server_path = close_app_mcp.get("server_path", "")

        # Fallback на канонические пути, если конфигурация не найдена
        if not open_app_server_path:
            open_app_server_path = "mcp_servers/open_app/server.py"
        if not close_app_server_path:
            close_app_server_path = "mcp_servers/close_app/server.py"

        mcp_config = McpActionConfig(
            open_app_server_path=open_app_server_path,
            close_app_server_path=close_app_server_path,
            timeout_sec=float(close_app_mcp.get("timeout_sec", actions_cfg.timeout_sec)),
            enabled=bool(close_app_mcp.get("enabled", actions_cfg.enabled)),
        )
        self._mcp_executor = McpActionExecutor(mcp_config)
        self._actions_lock = asyncio.Lock()
        self._active_actions: dict[str, asyncio.Task[Any]] = {}  # session_id -> task
        self._active_apps: dict[
            str, str
        ] = {}  # app_name -> session_id (для идемпотентности close_app)
        self._spoken_error_sessions: set[str] = set()
        self._action_dedupe: dict[str, float] = {}
        self._action_dedupe_ttl_sec = 90.0

        logger.info(
            "[%s] ActionExecutionIntegration initialized: enabled=%s, timeout=%.1fs, open_app_server=%s, close_app_server=%s",
            FEATURE_ID,
            mcp_config.enabled,
            mcp_config.timeout_sec,
            open_app_server_path,
            close_app_server_path,
        )

    async def _do_initialize(self) -> bool:
        """Инициализация интеграции."""
        return True

    async def _do_start(self) -> bool:
        """Запуск интеграции - подписка на события."""
        if not self._mcp_executor.config.enabled:
            logger.info("[%s] MCP action executor disabled, skipping start", FEATURE_ID)
            return True

        logger.info(
            "[%s] Starting ActionExecutionIntegration (subscribing to grpc.response.action)",
            FEATURE_ID,
        )
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
        await self.event_bus.subscribe(
            "browser.completed",
            self._on_browser_use_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "browser.failed",
            self._on_browser_use_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "browser.cancelled",
            self._on_browser_use_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "actions.send_whatsapp_message.completed",
            self._on_whatsapp_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "actions.send_whatsapp_message.failed",
            self._on_whatsapp_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "actions.read_whatsapp_messages.completed",
            self._on_whatsapp_terminal_event,
            EventPriority.HIGH,
        )
        await self.event_bus.subscribe(
            "actions.read_whatsapp_messages.failed",
            self._on_whatsapp_terminal_event,
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
        await self.event_bus.unsubscribe("browser.completed", self._on_browser_use_terminal_event)
        await self.event_bus.unsubscribe("browser.failed", self._on_browser_use_terminal_event)
        await self.event_bus.unsubscribe("browser.cancelled", self._on_browser_use_terminal_event)
        await self.event_bus.unsubscribe(
            "actions.send_whatsapp_message.completed", self._on_whatsapp_terminal_event
        )
        await self.event_bus.unsubscribe(
            "actions.send_whatsapp_message.failed", self._on_whatsapp_terminal_event
        )
        await self.event_bus.unsubscribe(
            "actions.read_whatsapp_messages.completed", self._on_whatsapp_terminal_event
        )
        await self.event_bus.unsubscribe(
            "actions.read_whatsapp_messages.failed", self._on_whatsapp_terminal_event
        )
        logger.info("[%s] ActionExecutionIntegration stopped", FEATURE_ID)
        return True

    async def _on_action_received(self, event: dict[str, Any]):
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
        source = data.get("source")

        logger.info(
            "[%s] stage=received session=%s source=%s has_action_json=%s feature=%s",
            ACTION_PIPELINE_TAG,
            session_id,
            source,
            bool(action_json),
            feature_id,
        )

        if not self._mcp_executor.config.enabled:
            logger.info("[%s] MCP actions disabled, ignoring payload", feature_id)
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="disabled",
                message="MCP action executor disabled",
                app_name=None,
                command=None,
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
            logger.warning(
                "[%s] stage=invalid_json session=%s source=%s error=%s raw=%s",
                ACTION_PIPELINE_TAG,
                session_id,
                source,
                exc,
                str(action_json)[:220],
            )
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="invalid_json",
                message=str(exc),
                app_name=None,
                command=None,
            )
            return

        logger.info(
            "🔍 [F-2025-016] Action received: session_id=%s, command=%s",
            session_id,
            action_data.get("command"),
        )

        logger.info("[%s] _on_action_received: event=%s", FEATURE_ID, action_data)

        # Определяем тип команды и feature_id
        command = action_data.get("command")
        action_type = command  # "open_app" или "close_app"
        args = action_data.get("args", {})
        logger.info(
            "[%s] stage=parsed session=%s command=%s args_keys=%s source=%s",
            ACTION_PIPELINE_TAG,
            session_id,
            command,
            sorted(args.keys()) if isinstance(args, dict) else [],
            source,
        )

        # Строим список допустимых команд динамически на основе feature flags
        loader = UnifiedConfigLoader.get_instance()
        valid_commands = ["open_app", "close_app"]  # Всегда доступны

        if loader.is_feature_enabled("messages", default=False):
            valid_commands.extend(["read_messages", "send_message", "find_contact"])
        if loader.is_feature_enabled("browser", default=False):
            valid_commands.extend(["browser_use", "close_browser"])
        if loader.is_feature_enabled("payment", default=False):
            valid_commands.extend(["buy_subscription", "manage_subscription"])
        if loader.is_feature_enabled("whatsapp", default=False):
            valid_commands.extend(["send_whatsapp_message", "read_whatsapp_messages"])
        if command not in valid_commands:
            logger.warning("[%s] Unsupported command: %s", feature_id, command)
            logger.warning(
                "[%s] stage=rejected session=%s reason=unsupported_command command=%s source=%s",
                ACTION_PIPELINE_TAG,
                session_id,
                command,
                source,
            )
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="unsupported_command",
                message=f"Unsupported command: {command}",
                app_name=None,
                command=command,
            )
            return

        # Обновляем feature_id в зависимости от типа действия
        if command == "open_app":
            action_feature_id = "F-2025-013-open-app"
        elif command == "close_app":
            action_feature_id = "F-2025-014-close-app"
        elif command in ["read_messages", "send_message", "find_contact"]:
            action_feature_id = "F-2025-016-messages"
        elif command == "browser_use":
            action_feature_id = "F-2025-015-browser-use"
        elif command == "close_browser":
            action_feature_id = "F-2025-015-browser-use"
        elif command in ["buy_subscription", "manage_subscription"]:
            action_feature_id = "F-2025-017-stripe-payment"
        elif command in ["send_whatsapp_message", "read_whatsapp_messages"]:
            action_feature_id = "F-2025-019-whatsapp"
        else:
            action_feature_id = feature_id

        # [Feature Flags] Check if feature is enabled
        loader = UnifiedConfigLoader.get_instance()
        feature_check_map = {
            "read_messages": "messages",
            "send_message": "messages",
            "find_contact": "messages",
            "browser_use": "browser",
            "close_browser": "browser",
            "buy_subscription": "payment",
            "manage_subscription": "payment",
            "send_whatsapp_message": "whatsapp",
            "read_whatsapp_messages": "whatsapp",
        }

        feature_name = feature_check_map.get(command)
        if feature_name:
            if not loader.is_feature_enabled(feature_name, default=False):
                msg = f"Feature '{feature_name}' is disabled in configuration."
                logger.warning("[%s] %s Ignoring command: %s", action_feature_id, msg, command)
                logger.warning(
                    "[%s] stage=rejected session=%s reason=feature_disabled feature=%s command=%s",
                    ACTION_PIPELINE_TAG,
                    session_id,
                    feature_name,
                    command,
                )

                # Strict check: if feature is disabled, return failure
                # This ensures "silent" commands are avoided as requested in diagnosis
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="feature_disabled",
                    message=f"Feature '{feature_name}' is currently disabled.",
                    app_name=None,
                    command=command,
                )

                # Speak the error for WhatsApp specifically (as per diagnosis)
                if feature_name == "whatsapp":
                    await self.event_bus.publish(
                        "grpc.tts_request",
                        {
                            "session_id": session_id,
                            "text": "WhatsApp integration is currently disabled.",
                            "source": "whatsapp",
                        },
                    )

                return

        # Валидация параметров в зависимости от типа действия
        if command == "open_app":
            # Для open_app требуется app_name или app_path
            if not args.get("app_name") and not args.get("app_path"):
                logger.error("[%s] Missing app_name or app_path for open_app", action_feature_id)
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing app_name or app_path for open_app",
                    app_name=None,
                    command=command,
                )
                return
        elif command == "close_app":
            # Для close_app требуется только app_name
            if not args.get("app_name"):
                logger.error("[%s] Missing app_name for close_app", action_feature_id)
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing app_name for close_app",
                    app_name=None,
                    command=command,
                )
                return
        elif command == "read_messages":
            # contact is optional ('all' by default), limit optional
            pass
        elif command == "send_message":
            # contact and message required
            if not args.get("contact") or not args.get("message"):
                logger.warning(
                    "[%s] stage=rejected session=%s reason=missing_parameter command=send_message contact=%s message_len=%s",
                    ACTION_PIPELINE_TAG,
                    session_id,
                    bool(args.get("contact")),
                    len(str(args.get("message", ""))),
                )
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing contact or message for send_message",
                    app_name=None,
                    command=command,
                )
                return
        elif command == "find_contact":
            # query required
            if not args.get("query"):
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=action_feature_id,
                    error_code="missing_parameter",
                    message="Missing query for find_contact",
                    app_name=None,
                    command=command,
                )
                return
        elif command == "browser_use":
            # browser_use may have optional args like task, url, model
            pass

        # Специальная обработка для Messages
        if command in ["read_messages", "send_message", "find_contact"]:
            dedupe_key = self._make_action_dedupe_key(session_id, command, args)
            logger.info(
                "[%s] stage=dispatch session=%s target=messages command=%s dedupe_key=%s",
                ACTION_PIPELINE_TAG,
                session_id,
                command,
                dedupe_key,
            )
            if not await self._register_action_dedupe(dedupe_key, session_id, command):
                return
            await self._execute_messages_action(
                session_id=session_id,
                command=command,
                args=args,
                feature_id=action_feature_id,
                dedupe_key=dedupe_key,
            )
            return

        # Специальная обработка для Browser Use
        if command == "browser_use":
            dedupe_key = self._make_action_dedupe_key(session_id, command, args)
            logger.info(
                "[%s] stage=dispatch session=%s target=browser_use command=%s dedupe_key=%s",
                ACTION_PIPELINE_TAG,
                session_id,
                command,
                dedupe_key,
            )
            if not await self._register_action_dedupe(dedupe_key, session_id, command):
                logger.info(
                    "[%s] Duplicate browser_use action ignored (session=%s)",
                    action_feature_id,
                    session_id,
                )
                return
            await self._execute_browser_use_action(
                session_id=session_id, args=args, feature_id=action_feature_id
            )
            return

        if command == "close_browser":
            logger.info(
                "[%s] stage=dispatch session=%s target=browser command=close_browser",
                ACTION_PIPELINE_TAG,
                session_id,
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="started",
                source="dispatch",
            )
            await self.event_bus.publish("browser.close.request", {"session_id": session_id})
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="dispatch",
                status="success",
            )
            return

        # Специальная обработка для Payment commands
        if command == "buy_subscription":
            logger.info(
                "[%s] stage=dispatch session=%s target=payment command=buy_subscription",
                ACTION_PIPELINE_TAG,
                session_id,
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="started",
                source="dispatch",
            )
            logger.info(
                "[%s] Dispatching buy_subscription to PaymentIntegration", action_feature_id
            )
            await self.event_bus.publish(
                "ui.action.buy_subscription",
                {
                    "session_id": session_id,
                    "source": "llm_command",
                    "feature_id": action_feature_id,
                },
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="dispatch",
                status="success",
            )
            return

        if command == "manage_subscription":
            logger.info(
                "[%s] stage=dispatch session=%s target=payment command=manage_subscription",
                ACTION_PIPELINE_TAG,
                session_id,
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="started",
                source="dispatch",
            )
            logger.info(
                "[%s] Dispatching manage_subscription to PaymentIntegration", action_feature_id
            )
            await self.event_bus.publish(
                "ui.action.manage_subscription",
                {
                    "session_id": session_id,
                    "source": "llm_command",
                    "feature_id": action_feature_id,
                },
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="dispatch",
                status="success",
            )
            return

        # Специальная обработка для Whatsapp commands
        if command in ["send_whatsapp_message", "read_whatsapp_messages"]:
            logger.info(
                "[%s] stage=dispatch session=%s target=whatsapp command=%s",
                ACTION_PIPELINE_TAG,
                session_id,
                command,
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="started",
                source="dispatch",
            )
            logger.info("[%s] Dispatching %s to WhatsappIntegration", action_feature_id, command)
            await self.event_bus.publish(
                "whatsapp.request",
                {
                    "session_id": session_id,
                    "command": command,
                    "args": args,
                    "feature_id": action_feature_id,
                },
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
                # Нормализуем app_name для проверки (регистронезависимо, без пробелов)
                app_name_normalized = app_name.strip().lower()
                if app_name_normalized in self._active_apps:
                    existing_session = self._active_apps[app_name_normalized]
                    existing_task = self._active_actions.get(existing_session)
                    if existing_task is None or existing_task.done():
                        # Снимаем залипшие записи, чтобы не блокировать новые close_app
                        self._active_apps.pop(app_name_normalized, None)
                        if existing_task and existing_task.done():
                            self._active_actions.pop(existing_session, None)
                        logger.info(
                            "[%s] close_app stale entry cleared for app=%s (session=%s)",
                            feature_id,
                            app_name,
                            existing_session,
                        )
                    else:
                        logger.info(
                            "[%s] close_app already running for app=%s (session=%s, new_session=%s)",
                            feature_id,
                            app_name,
                            existing_session,
                            session_id,
                        )
                        # Публикуем событие failure для второй сессии, чтобы клиент/сервер получили ответ
                        await self._publish_failure(
                            session_id=session_id,
                            feature_id=action_feature_id,
                            error_code="already_running",
                            message=f"close_app already running for {app_name} (session={existing_session})",
                            app_name=app_name,
                            command=action_type,
                        )
                        return
                # Регистрируем приложение как активное (используем нормализованный ключ)
                self._active_apps[app_name_normalized] = session_id

            # Создаем задачу для выполнения действия
            task = asyncio.create_task(
                self._execute_action(
                    session_id=session_id,
                    action_data=executor_action_data,
                    feature_id=action_feature_id,
                )
            )
            self._active_actions[session_id] = task

    async def _execute_action(
        self, *, session_id: str, action_data: dict[str, Any], feature_id: str
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
        await self._publish_action_lifecycle(
            session_id=session_id,
            command=action_type,
            phase="started",
            source="executor",
        )
        self._spoken_error_sessions.discard(session_id)

        try:
            # Выполняем действие в зависимости от типа
            if action_type == "open_app":
                server_path = Path(self._mcp_executor.config.open_app_server_path)
                if not server_path.exists():
                    logger.warning(
                        "[%s] MCP open_app server not found: %s. Falling back to system open.",
                        feature_id,
                        server_path,
                    )
                    result = await self._execute_open_app_fallback(
                        action_data=action_data,
                        session_id=session_id,
                    )
                else:
                    # Используем McpActionExecutor для open_app (через MCP)
                    result = await self._mcp_executor.execute_action(
                        action_data, session_id=session_id
                    )
            elif action_type == "close_app":
                # Check server existence first
                server_path = Path(self._mcp_executor.config.close_app_server_path)
                use_fallback = not server_path.exists()

                result = None
                if not use_fallback:
                    # Try MCP first
                    try:
                        result = await self._mcp_executor.execute_action(
                            action_data, session_id=session_id
                        )
                        if not result.success:
                            logger.warning(
                                "[%s] MCP close_app failed, trying fallback. Error: %s",
                                feature_id,
                                result.error,
                            )
                            use_fallback = True
                    except Exception as e:
                        logger.warning(
                            "[%s] MCP close_app exception: %s, trying fallback", feature_id, e
                        )
                        use_fallback = True

                if use_fallback:
                    logger.info("[%s] Using fallback for close_app", feature_id)
                    result = await self._execute_close_app_fallback(
                        action_data=action_data, session_id=session_id
                    )
            else:
                # Неизвестный тип действия
                from modules.mcp_action import McpActionResult

                result = McpActionResult(
                    success=False,
                    message=f"Unsupported action type: {action_type}",
                    error="unsupported_action",
                )

            if result is None:
                # Should not happen given logic above, but satisfies type checker
                from modules.mcp_action import McpActionResult

                result = McpActionResult(
                    success=False, error="internal_error", message="Result is None"
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
                    result.app_name or "unknown",
                )
                await self._publish_action_lifecycle(
                    session_id=session_id,
                    command=action_type,
                    phase="finished",
                    source="executor",
                    status="success",
                )
            else:
                # Ошибка выполнения
                await self._publish_failure(
                    session_id=session_id,
                    feature_id=feature_id,
                    error_code=result.error or "unknown",
                    message=result.message,
                    app_name=result.app_name or action_data.get("app_name"),
                    command=action_type,
                )
                logger.warning(
                    "[%s] Action failed: %s - %s", feature_id, result.error, result.message
                )
                await self._publish_action_lifecycle(
                    session_id=session_id,
                    command=action_type,
                    phase="finished",
                    source="executor",
                    status="failed",
                )

        except asyncio.CancelledError:
            # Действие было отменено
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="cancelled",
                message="Action cancelled",
                app_name=action_data.get("app_name"),
                command=action_type,
            )
            logger.info("[%s] Action cancelled for session=%s", feature_id, session_id)
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=action_type,
                phase="finished",
                source="executor",
                status="cancelled",
            )

        except Exception as exc:
            # Неожиданная ошибка
            await self._handle_error(exc, where="_execute_action")
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=action_type,
                phase="finished",
                source="executor",
                status="failed",
            )

    async def _execute_open_app_fallback(
        self,
        *,
        action_data: dict[str, Any],
        session_id: str | None,
    ):
        """Fallback: open app via system `open` when MCP server is missing."""
        from modules.mcp_action import McpActionResult

        app_name = action_data.get("app_name")
        app_path = action_data.get("app_path")
        binary = self._open_app_config.binary or "/usr/bin/open"

        if not Path(binary).exists():
            binary = "/usr/bin/open"

        if not app_name and not app_path:
            return McpActionResult(
                success=False,
                message="Missing app_name or app_path for open_app",
                error="missing_parameter",
            )

        try:
            if app_path:
                subprocess.run([binary, str(app_path)], check=True)
            else:
                # app_name гарантированно не None здесь (проверено выше)
                if not app_name:
                    return McpActionResult(
                        success=False,
                        message="Missing app_name for open_app",
                        error="missing_parameter",
                    )
                subprocess.run([binary, "-a", str(app_name)], check=True)
            return McpActionResult(
                success=True,
                message=f"Opened {app_path or app_name}",
                app_name=app_name,
            )
        except Exception as exc:
            logger.error(
                "[%s] open_app fallback failed: %s, session=%s",
                FEATURE_ID,
                exc,
                session_id or "unknown",
            )
            return McpActionResult(
                success=False,
                message=str(exc),
                error="open_app_fallback_failed",
                app_name=app_name,
            )
        finally:
            # Удаляем задачу из активных
            async with self._actions_lock:
                if session_id:
                    action_type = action_data.get("type")
                    app_name = action_data.get("app_name")
                    if action_type == "close_app" and app_name:
                        # Нормализуем app_name для поиска (регистронезависимо, без пробелов)
                        app_name_normalized = app_name.strip().lower()
                        if self._active_apps.get(app_name_normalized) == session_id:
                            self._active_apps.pop(app_name_normalized, None)
                            logger.debug(
                                "[%s] Removed app from active_apps: %s (session=%s)",
                                FEATURE_ID,
                                app_name,
                                session_id,
                            )

    async def _execute_close_app_fallback(
        self,
        *,
        action_data: dict[str, Any],
        session_id: str | None,
    ):
        """Fallback: close app via system `osascript` when MCP server is missing or fails."""
        from modules.mcp_action import McpActionResult

        app_name = action_data.get("app_name")
        if not app_name:
            return McpActionResult(
                success=False,
                message="Missing app_name for close_app",
                error="missing_parameter",
            )

        try:
            # Special handling for closing "Nexy" (self)
            if app_name.lower().strip() in ["nexy", "nexy app", "nexy.app"]:
                logger.info("[%s] Self-close requested (fallback)", FEATURE_ID)
                # Centralized shutdown path:
                # publish quit intent, coordinator emits app.shutdown.
                await self.event_bus.publish("tray.quit_clicked", {"source": "action_execution"})

                # Use osascript to quit gently
                script = 'tell application "Nexy" to quit'
                subprocess.run(["/usr/bin/osascript", "-e", script], check=False)

                return McpActionResult(
                    success=True,
                    message="Nexy is shutting down...",
                    app_name=app_name,
                )

            # Normal app closing via AppleScript
            script = f'tell application "{app_name}" to quit'
            subprocess.run(["/usr/bin/osascript", "-e", script], check=True, capture_output=True)

            return McpActionResult(
                success=True,
                message=f"Closed {app_name}",
                app_name=app_name,
            )

        except subprocess.CalledProcessError as e:
            # Try force kill if quit fails? No, keep it simple for now as per constraints.
            error_msg = e.stderr.decode().strip() if e.stderr else str(e)
            logger.error(
                "[%s] close_app fallback failed: %s, session=%s",
                FEATURE_ID,
                error_msg,
                session_id or "unknown",
            )
            return McpActionResult(
                success=False,
                message=f"Failed to close {app_name}: {error_msg}",
                error="close_app_fallback_failed",
                app_name=app_name,
            )
        except Exception as exc:
            logger.error(
                "[%s] close_app fallback unexpected error: %s, session=%s",
                FEATURE_ID,
                exc,
                session_id or "unknown",
            )
            return McpActionResult(
                success=False,
                message=str(exc),
                error="close_app_fallback_failed",
                app_name=app_name,
            )
        finally:
            # Cleanup active actions
            async with self._actions_lock:
                if session_id:
                    # Remove task
                    task = self._active_actions.pop(session_id, None)
                    if task and not task.done():
                        task.cancel()

                    # Remove from active apps
                    app_name_normalized = app_name.strip().lower()
                    if self._active_apps.get(app_name_normalized) == session_id:
                        self._active_apps.pop(app_name_normalized, None)

    async def _on_interrupt(self, event: dict[str, Any]):
        """Обработка прерывания - отмена всех действий."""
        await self._cancel_all_actions(reason="interrupt")

    async def _on_keyboard_short_press(self, event: dict[str, Any]):
        """Обработка короткого нажатия клавиши - отмена всех действий."""
        await self._cancel_all_actions(reason="keyboard_short_press")

    async def _on_mode_changed(self, event: dict[str, Any]):
        """Обработка изменения режима приложения - отмена при переходе в спящий режим."""
        try:
            from modules.mode_management import AppMode

            data = (
                event.get("data", event) if isinstance(event, dict) and "data" in event else event
            )
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

    async def _on_browser_use_terminal_event(self, event: dict[str, Any]):
        """Завершает lifecycle browser_use только по фактическому завершению browser task."""
        try:
            data = (
                event.get("data", event) if isinstance(event, dict) and "data" in event else event
            )
            session_id = data.get("session_id")
            if not session_id:
                return

            event_type = data.get("type", "")
            if "FAILED" in str(event_type):
                status = "failed"
            elif "CANCELLED" in str(event_type):
                status = "cancelled"
            else:
                status = "success"

            await self._publish_action_lifecycle(
                session_id=session_id,
                command="browser_use",
                phase="finished",
                source="browser",
                status=status,
            )
        except Exception as e:
            logger.debug("[%s] _on_browser_use_terminal_event failed: %s", FEATURE_ID, e)

    async def _on_whatsapp_terminal_event(self, event: dict[str, Any]):
        """Завершает lifecycle WhatsApp-команд только по фактическим terminal-событиям."""
        try:
            data = (
                event.get("data", event) if isinstance(event, dict) and "data" in event else event
            )
            session_id = data.get("session_id")
            if not session_id:
                return

            command = data.get("command")
            if not command:
                event_type = str(data.get("type", ""))
                if "send_whatsapp_message" in event_type:
                    command = "send_whatsapp_message"
                elif "read_whatsapp_messages" in event_type:
                    command = "read_whatsapp_messages"
                else:
                    return

            event_type = str(data.get("type", ""))
            status = "failed" if "failed" in event_type.lower() else "success"
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="whatsapp",
                status=status,
            )
        except Exception as e:
            logger.debug("[%s] _on_whatsapp_terminal_event failed: %s", FEATURE_ID, e)

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
                "[%s] Cancelling action for session=%s reason=%s", FEATURE_ID, session_id, reason
            )
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    async def _publish_failure(
        self,
        *,
        session_id: str | None,
        feature_id: str,
        error_code: str | None,
        message: str,
        app_name: str | None,
        command: str | None = None,
        suppress_playback_cancel: bool = False,
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
        event_name = self._resolve_failure_event_name(command=command, feature_id=feature_id)
        await self.event_bus.publish(event_name, payload)
        if not suppress_playback_cancel:
            await self._cancel_active_playback(
                session_id=session_id,
                reason=error_code or "action_failed",
                command=command,
            )
        await self._publish_speech_feedback(
            session_id=session_id,
            error_code=error_code,
            app_name=app_name,
            error_message=message,
            feature_id=feature_id,
            command=command,
        )

    @staticmethod
    def _resolve_failure_event_name(*, command: str | None, feature_id: str) -> str:
        if command:
            return f"actions.{command}.failed"
        if "close-app" in feature_id:
            return "actions.close_app.failed"
        return "actions.open_app.failed"

    async def _cancel_active_playback(
        self,
        *,
        session_id: str | None,
        reason: str,
        command: str | None = None,
    ) -> None:
        """Останавливает текущее воспроизведение, чтобы не звучала старая реплика."""
        if not session_id:
            return
        source = f"actions.{command}" if command else "actions.open_app"
        try:
            await self.event_bus.publish(
                "interrupt.request",
                {
                    "type": "speech_stop",
                    "session_id": session_id,
                    "source": source,
                    "reason": reason or "action_failed",
                    "feature_id": FEATURE_ID,
                },
            )
        except Exception as exc:
            logger.warning("[%s] Failed to cancel playback: %s", FEATURE_ID, exc)

    async def _publish_speech_feedback(
        self,
        *,
        session_id: str | None,
        error_code: str | None,
        app_name: str | None,
        error_message: str | None = None,
        feature_id: str = FEATURE_ID,
        command: str | None = None,
    ) -> None:
        """Публикует speech.playback.request с описанием ошибки."""
        if not self._open_app_config.speak_errors or not session_id:
            return
        if session_id in self._spoken_error_sessions:
            return

        if command:
            source = f"actions.{command}"
        # Используем переданный feature_id или FEATURE_ID по умолчанию
        elif feature_id and "close-app" in feature_id:
            source = "actions.close_app"
        # Используем переданный feature_id или FEATURE_ID по умолчанию
        else:
            source = "actions.open_app"

        speech_text = action_error_resolver.resolve(error_code, app_name, error_message)
        # Use server EdgeTTS via grpc.tts_request (with local fallback)
        await self.event_bus.publish(
            "grpc.tts_request",
            {
                "session_id": session_id,
                "text": speech_text,
                "source": source,
            },
        )
        self._spoken_error_sessions.add(session_id)
        logger.info(
            "[%s] Published speech feedback for session=%s code=%s",
            FEATURE_ID,
            session_id,
            error_code,
        )

    async def _execute_messages_action(
        self,
        *,
        session_id: str,
        command: str,
        args: dict[str, Any],
        feature_id: str,
        dedupe_key: str | None = None,
    ):
        """
        Выполняет команду Messages (read_messages, send_message, find_contact).
        Запускает синхронный код в отдельном потоке.
        """
        event_prefix = f"actions.{command}"

        # 1. Публикуем событие о начале
        await self.event_bus.publish(
            f"{event_prefix}.started",
            {
                "session_id": session_id,
                "feature_id": feature_id,
                "command": command,
                "args": args,
            },
        )
        await self._publish_action_lifecycle(
            session_id=session_id,
            command=command,
            phase="started",
            source="messages",
        )
        self._spoken_error_sessions.discard(session_id)

        try:
            # 2. Выполняем в потоке
            if command == "read_messages":
                result = await asyncio.to_thread(self._handle_read_messages, args)
            elif command == "send_message":
                result = await asyncio.to_thread(self._handle_send_message, args)
            elif command == "find_contact":
                result = await asyncio.to_thread(self._handle_find_contact, args)
            else:
                result = {"success": False, "message": f"Unknown command: {command}"}

            # 3. Обрабатываем результат
            if result.get("success", False):
                await self.event_bus.publish(
                    f"{event_prefix}.completed",
                    {
                        "session_id": session_id,
                        "feature_id": feature_id,
                        "result": result,
                    },
                )
                logger.info("[%s] %s completed successfully", feature_id, command)
                await self._publish_action_lifecycle(
                    session_id=session_id,
                    command=command,
                    phase="finished",
                    source="messages",
                    status="success",
                )

                # 4. Озвучиваем результат пользователю
                await self._handle_messages_success_feedback(session_id, command, result)
            else:
                if dedupe_key:
                    await self._clear_action_dedupe(dedupe_key)
                error_code_res = result.get("error_code")
                error_msg = result.get("message", "Unknown error")

                if error_code_res == "ambiguous_contact":
                    choices = result.get("choices", [])
                    choices_str = ", ".join(choices[:3])
                    text_to_speak = (
                        f"I found multiple contacts: {choices_str}. Please say the full name."
                    )

                    # Speak specific feedback
                    await self.event_bus.publish(
                        "grpc.tts_request",
                        {
                            "session_id": session_id,
                            "text": text_to_speak,
                            "source": f"actions.{command}",
                        },
                    )
                    self._spoken_error_sessions.add(session_id)  # Prevent generic error speech

                elif error_code_res == "similar_contacts_found":
                    suggestions = result.get("suggestions", [])
                    if suggestions:
                        suggestions_str = ", ".join(suggestions[:3])
                        text_to_speak = f"Contact not found. Did you mean: {suggestions_str}?"
                    else:
                        text_to_speak = "Contact not found. Please check the name and try again."

                    # Speak specific feedback
                    await self.event_bus.publish(
                        "grpc.tts_request",
                        {
                            "session_id": session_id,
                            "text": text_to_speak,
                            "source": f"actions.{command}",
                        },
                    )
                    self._spoken_error_sessions.add(session_id)  # Prevent generic error speech

                await self._publish_failure(
                    session_id=session_id,
                    feature_id=feature_id,
                    error_code=error_code_res or "execution_failed",
                    message=error_msg,
                    app_name="Messages",
                    command=command,
                    suppress_playback_cancel=error_code_res
                    in {"ambiguous_contact", "similar_contacts_found"},
                )
                logger.warning("[%s] %s failed: %s", feature_id, command, error_msg)
                await self._publish_action_lifecycle(
                    session_id=session_id,
                    command=command,
                    phase="finished",
                    source="messages",
                    status="failed",
                )

        except Exception as exc:
            if dedupe_key:
                await self._clear_action_dedupe(dedupe_key)
            await self._handle_error(exc, where=f"_execute_messages_action({command})")
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="exception",
                message=str(exc),
                app_name="Messages",
                command=command,
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="messages",
                status="failed",
            )

    async def _handle_messages_success_feedback(
        self, session_id: str, command: str, result: dict[str, Any]
    ):
        """Формирует и озвучивает результат успешного выполнения команды Messages."""
        text_to_speak = ""

        if command == "read_messages":
            count = result.get("count", 0)
            target = result.get("target", "Unknown")
            messages = result.get("messages", [])

            if count == 0:
                text_to_speak = f"No messages found from {target}."
            elif count == 1:
                msg = messages[0]
                text = msg.get("text", "")
                # Убираем лишние метаданные из текста для озвучки если они есть
                text_to_speak = f"Last message from {target}: {text}"
            else:
                text_to_speak = f"Last {count} messages from {target}. "
                for i, msg in enumerate(messages):
                    text = msg.get("text", "")
                    if i > 0:
                        text_to_speak += " Next message: "
                    text_to_speak += text

        elif command == "send_message":
            # Include message content and recipient in the feedback
            contact_name = result.get("contact_name", "recipient")
            message_content = result.get("message_content", "")
            if message_content:
                text_to_speak = (
                    f"Message to {contact_name}: '{message_content}'. Sent successfully."
                )

            else:
                text_to_speak = f"Message to {contact_name} sent successfully."

        elif command == "find_contact":
            count = result.get("count", 0)
            contacts = result.get("contacts", [])
            if count == 0:
                text_to_speak = "No contacts found."
            elif count == 1:
                c = contacts[0]
                name = c.get("display_label") or c.get("first_name") or "Unknown"
                phones = ", ".join(c.get("phones", []))
                text_to_speak = f"Found contact {name}, phone {phones}."
            else:
                text_to_speak = f"Found {count} contacts."

        if text_to_speak:
            # Use server EdgeTTS via grpc.tts_request (not local macOS say)
            await self.event_bus.publish(
                "grpc.tts_request",
                {
                    "session_id": session_id,
                    "text": text_to_speak,
                    "source": f"actions.{command}",
                },
            )

    def _make_action_dedupe_key(self, session_id: str, command: str, args: dict[str, Any]) -> str:
        stable_args = json.dumps(
            args or {}, sort_keys=True, ensure_ascii=False, separators=(",", ":")
        )
        raw = f"{session_id}|{command}|{stable_args}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    async def _register_action_dedupe(self, key: str, session_id: str, command: str) -> bool:
        now = time.monotonic()
        async with self._actions_lock:
            self._prune_action_dedupe(now)
            if key in self._action_dedupe:
                logger.info(
                    "[%s] Duplicate action dropped: session=%s command=%s",
                    FEATURE_ID,
                    session_id,
                    command,
                )
                return False
            self._action_dedupe[key] = now
        return True

    async def _clear_action_dedupe(self, key: str):
        async with self._actions_lock:
            self._action_dedupe.pop(key, None)

    def _prune_action_dedupe(self, now: float):
        if not self._action_dedupe:
            return
        ttl = self._action_dedupe_ttl_sec
        expired = [k for k, ts in self._action_dedupe.items() if now - ts > ttl]
        for k in expired:
            self._action_dedupe.pop(k, None)

    async def _execute_browser_use_action(
        self, *, session_id: str, args: dict[str, Any], feature_id: str
    ):
        """
        Перенаправляет команду browser_use в BrowserUseIntegration через событие browser.use.request.
        """
        # 1. Публикуем событие о начале
        await self.event_bus.publish(
            "actions.browser_use.started",
            {
                "session_id": session_id,
                "feature_id": feature_id,
                "command": "browser_use",
                "args": args,
            },
        )
        await self._publish_action_lifecycle(
            session_id=session_id,
            command="browser_use",
            phase="started",
            source="dispatch",
        )
        self._spoken_error_sessions.discard(session_id)

        # 2. Перенаправляем запрос в BrowserUseIntegration
        # BrowserUseIntegration ожидает событие "browser.use.request" с данными в поле 'data' или напрямую
        # Параметры: task, url (опционально), model (опционально)
        payload = {
            "session_id": session_id,
            "task": args.get("task", ""),
            "url": args.get("url"),
            "model": args.get("model"),
            # Можно передать исходные args полностью
            **args,
        }

        logger.info(
            "[%s] Routing browser_use command to BrowserUseIntegration (session=%s)",
            feature_id,
            session_id,
        )

        await self.event_bus.publish("browser.use.request", payload)

        # Мы не ждем завершения здесь, так как BrowserUseIntegration асинхронен и сам публикует прогресс
        # Но мы можем сразу подтвердить перенаправление
        await self.event_bus.publish(
            "actions.browser_use.dispatched",
            {"session_id": session_id, "feature_id": feature_id, "status": "dispatched"},
        )

    async def _publish_action_lifecycle(
        self,
        *,
        session_id: str | None,
        command: str,
        phase: str,
        source: str,
        status: str | None = None,
    ) -> None:
        if not session_id:
            return
        payload: dict[str, Any] = {
            "session_id": session_id,
            "command": command,
            "phase": phase,
            "source": source,
        }
        if status is not None:
            payload["status"] = status
        await self.event_bus.publish(f"actions.lifecycle.{phase}", payload)

    def _handle_read_messages(self, args: dict[str, Any]) -> dict[str, Any]:
        """Обработчик read_messages (синхронный)."""
        contact_id = args.get("contact")
        limit = int(args.get("limit", 10))

        # Single owner gate: Messages DB access is allowed only after FDA PASS in Permission V2 ledger.
        # This prevents repeated protected-file probes that produce kernel deny noise.
        if not self._is_full_disk_access_granted():
            return {
                "success": False,
                "message": (
                    "Full Disk Access is not granted yet. "
                    "Please allow Nexy in Privacy & Security > Full Disk Access."
                ),
            }

        # Подключаемся к БД
        conn = connect_db()
        if not conn:
            return {
                "success": False,
                "message": "Failed to connect to Messages DB (Check Full Disk Access)",
            }

        try:
            messages = []
            target_name = "Unknown"

            if not contact_id or contact_id.lower() == "all":
                # Получаем последнее сообщение вообще
                last_msg = get_last_message(conn)
                if last_msg:
                    messages = [last_msg]
                    raw_target = last_msg.get("display_name") or last_msg.get("contact_id")
                    if raw_target:
                        resolved = resolve_contact(raw_target, messages_conn=conn)
                        target_name = resolved.get("display_label") or raw_target
                    else:
                        target_name = "Unknown"
            else:
                # Резолвим контакт
                resolved = resolve_contact(contact_id, messages_conn=conn)
                resolved_id = resolved.get("raw_identifier") or contact_id
                target_name = resolved.get("display_label") or contact_id

                # Если это имя, ищем номера
                if not any(c.isdigit() for c in resolved_id):
                    contacts_found = find_contacts_by_name(contact_id)
                    if contacts_found:
                        # Берем первый номер первого найденного
                        phones = contacts_found[0].get("phones", [])
                        if phones:
                            resolved_id = phones[0]

                messages = get_messages_by_contact(conn, resolved_id, limit=limit)

            # Форматируем для ответа
            formatted_messages = []
            for msg in messages:
                sender_label = msg.get("display_name") or msg.get("contact_id") or "Unknown"
                if not msg.get("is_from_me") and sender_label:
                    resolved_sender = resolve_contact(sender_label, messages_conn=conn)
                    sender_label = resolved_sender.get("display_label") or sender_label
                formatted_messages.append(
                    {
                        "text": msg.get("text", "[No text]"),
                        "from_me": msg.get("is_from_me", False),
                        "date": format_message_date(msg.get("date", 0)),
                        "sender": "Me" if msg.get("is_from_me") else sender_label,
                    }
                )

            return {
                "success": True,
                "messages": formatted_messages,
                "count": len(formatted_messages),
                "target": target_name,
            }
        finally:
            conn.close()

    def _is_full_disk_access_granted(self) -> bool:
        """Check FDA state from Permission V2 ledger (single source of truth)."""
        try:
            ledger_path = get_user_data_dir() / "permission_ledger.json"
            ledger = LedgerStore(str(ledger_path)).load()
            if not ledger:
                # Preserve legacy behavior if ledger is unavailable.
                return True
            entry = ledger.steps.get(PermissionId.FULL_DISK_ACCESS)
            return bool(entry and entry.state == StepState.PASS_)
        except Exception as exc:
            logger.warning("[MESSAGES] Failed to check FDA ledger state: %s", exc)
            # Fail-open to avoid blocking due to transient ledger read issues.
            return True

    def _handle_send_message(self, args: dict[str, Any]) -> dict[str, Any]:
        """Обработчик send_message (синхронный)."""
        contact = args.get("contact")
        message = args.get("message")

        if not contact or not message:
            return {"success": False, "message": "Missing contact or message"}

        result = send_message_to_contact(contact, message)
        # Add message content to result for TTS feedback
        result["message_content"] = message
        return result

    def _handle_find_contact(self, args: dict[str, Any]) -> dict[str, Any]:
        """Обработчик find_contact (синхронный)."""
        query = args.get("query")
        if not query:
            return {"success": False, "message": "Missing query"}

        contacts = find_contacts_by_name(query)

        if not contacts and any(c.isdigit() for c in query):
            resolved = resolve_contact(query)
            if resolved and resolved.get("source") != "fallback":
                contacts = [resolved]

        return {"success": True, "contacts": contacts, "count": len(contacts)}
