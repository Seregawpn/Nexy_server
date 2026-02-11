"""
MessagesIntegration - centralized owner for Messages domain actions.
"""

import asyncio
import hashlib
import json
import time
from typing import Any

from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.utils.logging_setup import get_logger
from modules.messages import (
    connect_db,
    find_contacts_by_name,
    format_message_date,
    get_last_message,
    get_messages_by_contact,
    resolve_contact,
    send_message_to_contact,
)

logger = get_logger(__name__)
FEATURE_ID = "F-2025-016-messages"


class MessagesIntegration(BaseIntegration):
    """Single owner for Messages action execution."""

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
            name="MessagesIntegration",
        )
        self._dedupe_lock = asyncio.Lock()
        self._dedupe: dict[str, float] = {}
        self._dedupe_ttl_sec = 90.0

    async def _do_initialize(self) -> bool:
        return True

    async def _do_start(self) -> bool:
        await self.event_bus.subscribe("messages.read_request", self._on_read_request, EventPriority.HIGH)
        await self.event_bus.subscribe("messages.send_request", self._on_send_request, EventPriority.HIGH)
        await self.event_bus.subscribe("messages.contact_search", self._on_contact_search, EventPriority.HIGH)
        return True

    async def _do_stop(self) -> bool:
        await self.event_bus.unsubscribe("messages.read_request", self._on_read_request)
        await self.event_bus.unsubscribe("messages.send_request", self._on_send_request)
        await self.event_bus.unsubscribe("messages.contact_search", self._on_contact_search)
        return True

    async def _on_read_request(self, event: dict[str, Any]) -> None:
        data = event.get("data", event) if isinstance(event, dict) else {}
        args = dict(data.get("args") or {})
        if "contact" not in args:
            args["contact"] = data.get("contact_name")
        if "limit" not in args and data.get("limit") is not None:
            args["limit"] = data.get("limit")
        await self._execute_command(
            session_id=self._normalize_session_id(data.get("session_id")),
            command="read_messages",
            args=args,
            feature_id=str(data.get("feature_id") or FEATURE_ID),
        )

    async def _on_send_request(self, event: dict[str, Any]) -> None:
        data = event.get("data", event) if isinstance(event, dict) else {}
        args = dict(data.get("args") or {})
        if "contact" not in args:
            args["contact"] = data.get("contact_name")
        if "message" not in args:
            args["message"] = data.get("message_content")
        await self._execute_command(
            session_id=self._normalize_session_id(data.get("session_id")),
            command="send_message",
            args=args,
            feature_id=str(data.get("feature_id") or FEATURE_ID),
        )

    async def _on_contact_search(self, event: dict[str, Any]) -> None:
        data = event.get("data", event) if isinstance(event, dict) else {}
        args = dict(data.get("args") or {})
        if "query" not in args:
            args["query"] = data.get("query")
        await self._execute_command(
            session_id=self._normalize_session_id(data.get("session_id")),
            command="find_contact",
            args=args,
            feature_id=str(data.get("feature_id") or FEATURE_ID),
        )

    async def _execute_command(
        self,
        *,
        session_id: str | None,
        command: str,
        args: dict[str, Any],
        feature_id: str,
    ) -> None:
        if not session_id:
            logger.warning("[%s] Missing session_id for %s", FEATURE_ID, command)
            return

        dedupe_key = self._make_dedupe_key(session_id, command, args)
        if not await self._register_dedupe(dedupe_key):
            logger.info("[%s] Duplicate message command dropped: session=%s command=%s", FEATURE_ID, session_id, command)
            return

        event_prefix = f"actions.{command}"
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

        try:
            if command == "read_messages":
                result = await asyncio.to_thread(self._handle_read_messages, args)
            elif command == "send_message":
                result = await asyncio.to_thread(self._handle_send_message, args)
            else:
                result = await asyncio.to_thread(self._handle_find_contact, args)

            if result.get("success", False):
                await self.event_bus.publish(
                    f"{event_prefix}.completed",
                    {
                        "session_id": session_id,
                        "feature_id": feature_id,
                        "result": result,
                    },
                )
                await self._publish_action_lifecycle(
                    session_id=session_id,
                    command=command,
                    phase="finished",
                    source="messages",
                    status="success",
                )
                await self._handle_messages_success_feedback(session_id, command, result)
                return

            await self._emit_error_feedback(session_id, command, result)
            await self.event_bus.publish(
                f"{event_prefix}.failed",
                {
                    "session_id": session_id,
                    "feature_id": feature_id,
                    "error_code": result.get("error_code", "execution_failed"),
                    "message": result.get("message", "Unknown error"),
                    "command": command,
                },
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="messages",
                status="failed",
            )
        except Exception as exc:
            await self._handle_error(exc, where=f"_execute_command({command})")
            await self.event_bus.publish(
                f"{event_prefix}.failed",
                {
                    "session_id": session_id,
                    "feature_id": feature_id,
                    "error_code": "exception",
                    "message": str(exc),
                    "command": command,
                },
            )
            await self._publish_action_lifecycle(
                session_id=session_id,
                command=command,
                phase="finished",
                source="messages",
                status="failed",
            )

    async def _emit_error_feedback(self, session_id: str, command: str, result: dict[str, Any]) -> None:
        error_code = result.get("error_code")
        if error_code == "ambiguous_contact":
            choices = result.get("choices", [])
            choices_str = ", ".join(choices[:3])
            text = f"I found multiple contacts: {choices_str}. Please say the full name."
        elif error_code == "similar_contacts_found":
            suggestions = result.get("suggestions", [])
            if suggestions:
                suggestions_str = ", ".join(suggestions[:3])
                text = f"Contact not found. Did you mean: {suggestions_str}?"
            else:
                text = "Contact not found. Please check the name and try again."
        else:
            message = result.get("message", "Unknown error")
            text = f"Messages action failed: {message}"
        await self.event_bus.publish(
            "grpc.tts_request",
            {
                "session_id": session_id,
                "text": text,
                "source": f"actions.{command}",
            },
        )

    async def _handle_messages_success_feedback(self, session_id: str, command: str, result: dict[str, Any]) -> None:
        text_to_speak = ""
        if command == "read_messages":
            count = result.get("count", 0)
            target = result.get("target", "Unknown")
            messages = result.get("messages", [])
            if count == 0:
                text_to_speak = f"No messages found from {target}."
            elif count == 1:
                msg = messages[0]
                text_to_speak = f"Last message from {target}: {msg.get('text', '')}"
            else:
                text_to_speak = f"Last {count} messages from {target}. "
                for i, msg in enumerate(messages):
                    if i > 0:
                        text_to_speak += " Next message: "
                    text_to_speak += msg.get("text", "")
        elif command == "send_message":
            contact_name = result.get("contact_name", "recipient")
            message_content = result.get("message_content", "")
            if message_content:
                text_to_speak = f"Message to {contact_name}: '{message_content}'. Sent successfully."
            else:
                text_to_speak = f"Message to {contact_name} sent successfully."
        else:
            count = result.get("count", 0)
            contacts = result.get("contacts", [])
            if count == 0:
                text_to_speak = "No contacts found."
            elif count == 1:
                contact = contacts[0]
                name = contact.get("display_label") or contact.get("first_name") or "Unknown"
                phones = ", ".join(contact.get("phones", []))
                text_to_speak = f"Found contact {name}, phone {phones}."
            else:
                text_to_speak = f"Found {count} contacts."

        if text_to_speak:
            await self.event_bus.publish(
                "grpc.tts_request",
                {
                    "session_id": session_id,
                    "text": text_to_speak,
                    "source": f"actions.{command}",
                },
            )

    async def _publish_action_lifecycle(
        self,
        *,
        session_id: str,
        command: str,
        phase: str,
        source: str,
        status: str | None = None,
    ) -> None:
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
        contact_id = args.get("contact")
        limit = int(args.get("limit", 10))
        conn = connect_db()
        if not conn:
            return {"success": False, "message": "Failed to connect to Messages DB (Check Full Disk Access)"}
        try:
            messages = []
            target_name = "Unknown"
            if not contact_id or str(contact_id).lower() == "all":
                last_msg = get_last_message(conn)
                if last_msg:
                    messages = [last_msg]
                    raw_target = last_msg.get("display_name") or last_msg.get("contact_id")
                    if raw_target:
                        resolved = resolve_contact(raw_target, messages_conn=conn)
                        target_name = resolved.get("display_label") or raw_target
            else:
                resolved = resolve_contact(str(contact_id), messages_conn=conn)
                resolved_id = resolved.get("raw_identifier") or contact_id
                target_name = resolved.get("display_label") or str(contact_id)
                if not any(ch.isdigit() for ch in str(resolved_id)):
                    contacts_found = find_contacts_by_name(str(contact_id))
                    if contacts_found:
                        phones = contacts_found[0].get("phones", [])
                        if phones:
                            resolved_id = phones[0]
                messages = get_messages_by_contact(conn, str(resolved_id), limit=limit)

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

    def _handle_send_message(self, args: dict[str, Any]) -> dict[str, Any]:
        contact = args.get("contact")
        message = args.get("message")
        if not contact or not message:
            return {"success": False, "message": "Missing contact or message"}
        result = send_message_to_contact(str(contact), str(message))
        result["message_content"] = str(message)
        return result

    def _handle_find_contact(self, args: dict[str, Any]) -> dict[str, Any]:
        query = args.get("query")
        if not query:
            return {"success": False, "message": "Missing query"}
        contacts = find_contacts_by_name(str(query))
        if not contacts and any(ch.isdigit() for ch in str(query)):
            resolved = resolve_contact(str(query))
            if resolved and resolved.get("source") != "fallback":
                contacts = [resolved]
        return {
            "success": True,
            "contacts": contacts,
            "count": len(contacts),
        }

    def _make_dedupe_key(self, session_id: str, command: str, args: dict[str, Any]) -> str:
        stable_args = json.dumps(args or {}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(f"{session_id}|{command}|{stable_args}".encode("utf-8")).hexdigest()

    async def _register_dedupe(self, key: str) -> bool:
        now = time.monotonic()
        async with self._dedupe_lock:
            self._prune_dedupe(now)
            if key in self._dedupe:
                return False
            self._dedupe[key] = now
        return True

    def _prune_dedupe(self, now: float) -> None:
        expired = [k for k, ts in self._dedupe.items() if (now - ts) > self._dedupe_ttl_sec]
        for key in expired:
            self._dedupe.pop(key, None)

    @staticmethod
    def _normalize_session_id(session_id: Any) -> str | None:
        if session_id is None:
            return None
        value = str(session_id).strip()
        return value or None
