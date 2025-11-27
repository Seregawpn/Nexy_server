"""
ActionExecutionIntegration — выполнение действий open_app на клиенте.

Подписывается на grpc.response.action и запускает ActionExecutor для выполнения команд.
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
from modules.action_executor import ActionExecutor, ActionExecutorConfig
from modules.action_errors.messages import resolver as action_error_resolver

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"

logger = logging.getLogger(__name__)


class ActionExecutionIntegration(BaseIntegration):
    """Подписывается на grpc.response.action и запускает ActionExecutor."""

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
        loader = UnifiedConfigLoader()
        actions_cfg = loader.get_actions_config().get("open_app") or OpenAppActionConfig()
        
        executor_config = ActionExecutorConfig(
            enabled=actions_cfg.enabled,
            timeout_sec=actions_cfg.timeout_sec,
            allowed_apps=actions_cfg.allowed_apps or [],
            binary=actions_cfg.binary,
        )
        
        self._executor = ActionExecutor(executor_config)
        self._open_app_config = actions_cfg
        self._config = executor_config
        self._actions_lock = asyncio.Lock()
        self._active_actions: Dict[str, asyncio.Task] = {}
        self._spoken_error_sessions: Set[str] = set()
        
        logger.info(
            "[%s] ActionExecutionIntegration initialized: enabled=%s, timeout=%.1fs, allowed_apps=%s",
            FEATURE_ID,
            executor_config.enabled,
            executor_config.timeout_sec,
            len(executor_config.allowed_apps) if executor_config.allowed_apps else "all"
        )

    async def _do_initialize(self) -> bool:
        """Инициализация интеграции."""
        return True

    async def _do_start(self) -> bool:
        """Запуск интеграции - подписка на события."""
        if not self._executor.is_enabled():
            logger.info("[%s] Action executor disabled, skipping start", FEATURE_ID)
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
        logger.info("[%s] ActionExecutionIntegration started", FEATURE_ID)
        return True

    async def _do_stop(self) -> bool:
        """Остановка интеграции - отмена всех действий и отписка от событий."""
        if not self._executor.is_enabled():
            return True
        
        await self._cancel_all_actions(reason="integration_stop")
        await self.event_bus.unsubscribe("grpc.response.action", self._on_action_received)
        await self.event_bus.unsubscribe("interrupt.request", self._on_interrupt)
        await self.event_bus.unsubscribe("keyboard.short_press", self._on_keyboard_short_press)
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

        if not self._executor.is_enabled():
            logger.info("[%s] Actions disabled, ignoring payload", feature_id)
            await self._publish_failure(
                session_id=session_id,
                feature_id=feature_id,
                error_code="disabled",
                message="Action executor disabled",
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

        # Проверяем, что это команда open_app
        if action_data.get("command") != "open_app":
            logger.warning(
                "[%s] Unsupported command: %s",
                feature_id,
                action_data.get("command")
            )
            return

        # Преобразуем формат для ActionExecutor
        # ActionExecutor ожидает: {"type": "open_app", "app_name": "...", "app_path": "..."}
        executor_action_data = {
            "type": "open_app",
            "app_name": action_data.get("args", {}).get("app_name"),
            "app_path": action_data.get("args", {}).get("app_path"),
        }

        # Защита от дублирования: проверяем, не выполняется ли уже действие для этой сессии
        async with self._actions_lock:
            if session_id in self._active_actions:
                logger.info("[%s] Action already running for session=%s", feature_id, session_id)
                return
            
            # Создаем задачу для выполнения действия
            task = asyncio.create_task(
                self._execute_action(
                    session_id=session_id,
                    action_data=executor_action_data,
                    feature_id=feature_id
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
        Выполняет действие через ActionExecutor.
        
        Args:
            session_id: ID сессии
            action_data: Данные действия для ActionExecutor
            feature_id: ID фичи для логирования
        """
        # Публикуем событие о начале выполнения
        await self.event_bus.publish(
            "actions.open_app.started",
            {
                "session_id": session_id,
                "feature_id": feature_id,
                "action": action_data,
            },
        )
        self._spoken_error_sessions.discard(session_id)
        
        try:
            # Выполняем действие
            result = await self._executor.execute(action_data)
            
            if result.success:
                # Успешное выполнение
                await self.event_bus.publish(
                    "actions.open_app.completed",
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

    async def _on_interrupt(self, event: Dict[str, Any]):
        """Обработка прерывания - отмена всех действий."""
        await self._cancel_all_actions(reason="interrupt")

    async def _on_keyboard_short_press(self, event: Dict[str, Any]):
        """Обработка короткого нажатия клавиши - отмена всех действий."""
        await self._cancel_all_actions(reason="keyboard_short_press")

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
        await self.event_bus.publish("actions.open_app.failed", payload)
        await self._cancel_active_playback(session_id=session_id, reason=error_code or "action_failed")
        await self._publish_speech_feedback(
            session_id=session_id,
            error_code=error_code,
            app_name=app_name,
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
    ) -> None:
        """Публикует speech.playback.request с описанием ошибки."""
        if not self._open_app_config.speak_errors or not session_id:
            return
        if session_id in self._spoken_error_sessions:
            return

        speech_text = action_error_resolver.resolve(error_code, app_name)
        await self.event_bus.publish(
            "speech.playback.request",
            {
                "session_id": session_id,
                "feature_id": FEATURE_ID,
                "source": "actions.open_app",
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
