"""
Очередь запросов разрешений для последовательного отображения системных промптов.
"""

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

from integration.core.event_bus import EventPriority, EventBus
from .types import PermissionType

logger = logging.getLogger(__name__)


@dataclass
class _QueueItem:
    permission: PermissionType
    source: str
    future: asyncio.Future
    auto_open: bool


class PermissionsQueue:
    """
    Простой диспетчер, который гарантирует последовательность запросов разрешений.
    Пока активен один запрос — остальные ждут в очереди.
    """

    def __init__(
        self,
        event_bus: EventBus,
        *,
        sequential: bool = True,
        auto_open_settings: bool = False,
        pause_between_requests: float = 0.5,
        request_timeout: float = 300.0,
    ):
        self._event_bus = event_bus
        self._sequential = sequential
        self._auto_open_default = auto_open_settings
        self._pause = max(0.0, float(pause_between_requests))
        self._timeout = max(1.0, float(request_timeout))

        self._queue: asyncio.Queue[_QueueItem] = asyncio.Queue()
        self._current: Optional[_QueueItem] = None
        self._processing_task: Optional[asyncio.Task] = None
        self._subscriptions_attached = False

    async def initialize(self):
        """Подписываемся на события только в последовательном режиме."""
        if not self._sequential or self._subscriptions_attached:
            return

        await self._event_bus.subscribe(
            "permissions.status_checked",
            self._on_permission_event,
            EventPriority.CRITICAL,
        )
        await self._event_bus.subscribe(
            "permissions.changed",
            self._on_permission_event,
            EventPriority.CRITICAL,
        )
        self._subscriptions_attached = True
        logger.debug("PermissionsQueue: subscriptions attached")

    async def request(
        self,
        permission: PermissionType,
        *,
        source: str,
        auto_open: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Запросить разрешение. Возвращает dict со статусом {'status': 'granted'|'denied'|...}.
        В непоследовательном режиме просто публикует событие и возвращает пустой ответ.
        """
        if not self._sequential:
            await self._event_bus.publish(
                "permissions.request_required",
                {
                    "source": source,
                    "permissions": [permission.value],
                },
            )
            return {"status": None, "permission": permission.value}

        loop = asyncio.get_running_loop()
        future: asyncio.Future = loop.create_future()
        item = _QueueItem(
            permission=permission,
            source=source,
            future=future,
            auto_open=self._auto_open_default if auto_open is None else auto_open,
        )

        await self._queue.put(item)

        # Запускаем обработчик, если он ещё не запущен
        if not self._processing_task or self._processing_task.done():
            self._processing_task = asyncio.create_task(self._process_queue())

        return await future

    async def _process_queue(self):
        """Забирает элементы из очереди и обрабатывает их по очереди."""
        while True:
            item = await self._queue.get()
            self._current = item

            logger.debug(
                "PermissionsQueue: requesting %s (source=%s)",
                item.permission.value,
                item.source,
            )

            await self._event_bus.publish(
                "permissions.request_required",
                {
                    "source": item.source,
                    "permissions": [item.permission.value],
                    "auto_open": item.auto_open,
                },
            )

            try:
                await asyncio.wait_for(item.future, timeout=self._timeout)
            except asyncio.TimeoutError:
                if not item.future.done():
                    item.future.set_result(
                        {"status": "timeout", "permission": item.permission.value}
                    )
                logger.warning(
                    "PermissionsQueue: timeout waiting for %s",
                    item.permission.value,
                )
            finally:
                self._current = None
                self._queue.task_done()
                if self._pause:
                    await asyncio.sleep(self._pause)

    async def _on_permission_event(self, event: Dict[str, Any]):
        """Получает обновления статусов от системных интеграций."""
        if not self._current:
            return

        data = (event or {}).get("data") or {}

        # Обновление по одному разрешению
        permission = data.get("permission")
        status = data.get("status") or data.get("new_status")
        self._complete_if_matches(permission, status)

        # Пакетное обновление
        perms_map = data.get("permissions")
        if isinstance(perms_map, dict):
            for perm_key, value in perms_map.items():
                value_status = value
                if isinstance(value, dict):
                    value_status = value.get("status") or value.get("new_status")
                self._complete_if_matches(perm_key, value_status)

    def _complete_if_matches(self, permission_value: Any, status_value: Any):
        """Если событие относится к активному запросу — завершаем Future."""
        if not self._current:
            return

        permission = self._normalize_permission(permission_value)
        if permission is None or permission != self._current.permission:
            return

        status = self._normalize_status(status_value)
        if status is None:
            return

        if not self._current.future.done():
            self._current.future.set_result(
                {"status": status, "permission": permission.value}
            )
            logger.debug(
                "PermissionsQueue: %s completed with status %s",
                permission.value,
                status,
            )

    @staticmethod
    def _normalize_permission(value: Any) -> Optional[PermissionType]:
        if isinstance(value, PermissionType):
            return value
        if isinstance(value, str):
            lowered = value.lower()
            for perm in PermissionType:
                if perm.value == lowered:
                    return perm
        return None

    @staticmethod
    def _normalize_status(value: Any) -> Optional[str]:
        if value is None:
            return None
        if hasattr(value, "value"):
            return str(value.value).lower()
        return str(value).lower()

    @property
    def sequential(self) -> bool:
        return self._sequential
