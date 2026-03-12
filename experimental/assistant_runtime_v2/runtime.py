from __future__ import annotations

import logging
from typing import Any, AsyncGenerator, Callable, Dict

from .active_context import ActiveContextStore
from .task_lifecycle import TaskLifecycleManager

logger = logging.getLogger(__name__)

LegacyHandler = Callable[[Dict[str, Any]], AsyncGenerator[Dict[str, Any], None]]


class AssistantRuntimeV2:
    """
    Experimental isolated runtime owner-path.

    Current phase is intentionally safe: v2 owns only routing/logging/context shell
    and delegates actual request execution to the existing workflow path.
    """

    def __init__(self) -> None:
        self._active_context_store = ActiveContextStore()
        self._task_lifecycle = TaskLifecycleManager()

    async def process_request_streaming(
        self,
        request_data: Dict[str, Any],
        *,
        legacy_handler: LegacyHandler,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        session_id = str(request_data.get("session_id") or "-")
        state = self._active_context_store.get_or_create(session_id)
        state.turn_version += 1
        self._task_lifecycle.begin_turn(request_data, state)

        logger.info(
            "REQUEST_PATH stage=workflow.route component=assistant_runtime_v2 session=%s runtime=v2 turn=%s",
            session_id,
            state.turn_version,
        )

        try:
            async for item in legacy_handler(request_data):
                self._task_lifecycle.observe_stream_item(item, state)
                yield item
        finally:
            self._task_lifecycle.finish_turn(state, request_data)
            self._active_context_store.clear(session_id)
