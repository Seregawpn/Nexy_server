from __future__ import annotations

import logging
from typing import Any, Dict, Optional

from .active_context import ActiveContextState

logger = logging.getLogger(__name__)


class TaskLifecycleManager:
    """
    Thin passive lifecycle hook for v2.

    It reads only canonical current-pipeline signals and never performs its own
    semantic interpretation.
    """

    _COMMAND_DOMAIN_MAP = {
        "send_message": "messages",
        "read_messages": "messages",
        "find_contact": "messages",
        "send_whatsapp_message": "whatsapp",
        "read_whatsapp_messages": "whatsapp",
        "open_app": "system_control",
        "close_app": "system_control",
        "browser_use": "browser",
        "close_browser": "browser",
        "buy_subscription": "payment",
        "manage_subscription": "payment",
    }

    def begin_turn(self, request_data: Dict[str, Any], state: ActiveContextState) -> None:
        user_text = str(request_data.get("text") or "").strip()
        prepared_request = request_data.get("prepared_request")
        route = self._extract_route(prepared_request)

        state.last_user_text = user_text
        state.status = "turn_started"
        state.last_question = None
        state.awaiting_reply = False
        state.missing_slots = []

        logger.info(
            "REQUEST_PATH stage=v2.lifecycle.begin component=assistant_runtime_v2 session=%s route=%s has_text=%s",
            state.session_id,
            route or "-",
            bool(user_text),
        )

    def observe_stream_item(self, item: Dict[str, Any], state: ActiveContextState) -> None:
        if not isinstance(item, dict):
            return

        command_payload = item.get("command_payload")
        if isinstance(command_payload, dict):
            payload = command_payload.get("payload", {})
            command = str(payload.get("command") or "").strip().lower()
            if command:
                state.domain = self._COMMAND_DOMAIN_MAP.get(command)
                state.goal = command
                state.intent = command
                state.filled_slots = dict(payload.get("args") or {})
                state.status = "observed_command"
                logger.info(
                    "REQUEST_PATH stage=v2.lifecycle.command component=assistant_runtime_v2 session=%s command=%s domain=%s",
                    state.session_id,
                    command,
                    state.domain or "-",
                )

        if item.get("is_final"):
            logger.info(
                "REQUEST_PATH stage=v2.lifecycle.final component=assistant_runtime_v2 session=%s status=%s has_command=%s",
                state.session_id,
                state.status,
                bool(command_payload),
            )

    def finish_turn(self, state: ActiveContextState, request_data: Optional[Dict[str, Any]] = None) -> None:
        signal_route = None
        signal_goal_state = None
        signal_current_goal = None
        if isinstance(request_data, dict):
            signals = request_data.get("_assistant_runtime_v2_signals")
            if isinstance(signals, dict):
                signal_route = str(signals.get("route") or "").strip().lower() or None
                signal_goal_state = str(signals.get("goal_state") or "").strip().lower() or None
                signal_current_goal = str(signals.get("current_goal") or "").strip() or None

        lifecycle_event = self._map_goal_state_to_event(signal_goal_state)
        if signal_route and not state.domain:
            state.domain = signal_route
        if signal_current_goal and not state.goal:
            state.goal = signal_current_goal

        logger.info(
            "REQUEST_PATH stage=v2.lifecycle.finish component=assistant_runtime_v2 session=%s status=%s lifecycle=%s goal_state=%s goal=%s domain=%s",
            state.session_id,
            state.status,
            lifecycle_event,
            signal_goal_state or "-",
            state.goal or "-",
            state.domain or "-",
        )

        state.domain = None
        state.goal = None
        state.intent = None
        state.filled_slots.clear()
        state.missing_slots = []
        state.last_question = None
        state.awaiting_reply = False
        state.status = "idle"

    @staticmethod
    def _extract_route(prepared_request: Any) -> Optional[str]:
        if not isinstance(prepared_request, dict):
            return None
        route = str(prepared_request.get("route") or "").strip().lower()
        return route or None

    @staticmethod
    def _map_goal_state_to_event(goal_state: Optional[str]) -> str:
        mapping = {
            "set": "task_opened",
            "keep": "task_continued",
            "replace": "task_replaced",
            "clear": "task_closed",
            "empty": "task_inactive",
        }
        return mapping.get(str(goal_state or "").strip().lower(), "task_unknown")
