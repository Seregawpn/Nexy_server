import asyncio
import json
import logging
from typing import Any
import uuid

logger = logging.getLogger(__name__)


class WhatsappMCPClient:
    """
    Client for interacting with the WhatsApp MCP Server (Node.js).
    Handles JSON-RPC communication and high-level command mapping.
    """

    def __init__(self, service_manager):
        self.service_manager = service_manager
        self.pending_requests: dict[str, asyncio.Future[Any]] = {}
        self._listener_task: asyncio.Task[Any] | None = None
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None

    async def start(self):
        """Start the client, hooking into the service manager's process streams"""
        if not self.service_manager.process:
            raise RuntimeError("Service manager process is not running")

        self._reader = self.service_manager.process.stdout
        self._writer = self.service_manager.process.stdin

        self._listener_task = asyncio.create_task(self._listen_loop())

        # Initialize MCP session if needed (MCP SDK usually expects an 'initialize' request)
        # But generic MCP tools might just work.
        # Let's assume standard MCP initialization flow might be needed future-wise,
        # but for now we'll just try to call tools.

    async def stop(self):
        """Stop the client"""
        if self._listener_task:
            self._listener_task.cancel()
            try:
                await self._listener_task
            except asyncio.CancelledError:
                pass

    async def _listen_loop(self):
        """Read responses from stdout line-by-line using JSON-RPC"""
        if not self._reader:
            return

        try:
            while True:
                line = await self._reader.readline()
                if not line:
                    break

                decoded_line = line.decode("utf-8").strip()
                if not decoded_line:
                    continue

                # Pass to ServiceManager for Logs/QR detection
                if hasattr(self.service_manager, "handle_output_line"):
                    try:
                        self.service_manager.handle_output_line(decoded_line)
                    except Exception as e:
                        logger.error(f"Error handling log line: {e}")

                try:
                    message = json.loads(decoded_line)
                    # Check if it's a valid JSON-RPC message or result
                    if isinstance(message, dict) and (
                        "jsonrpc" in message
                        or "id" in message
                        or "result" in message
                        or "error" in message
                    ):
                        await self._handle_message(message)
                except json.JSONDecodeError:
                    # Valid JSON logs are handled by service_manager, but invalid JSON is just logged here
                    logger.debug(f"Non-JSON output from WhatsApp service: {decoded_line}")

        except asyncio.CancelledError:
            pass
        except Exception as e:
            logger.error(f"Error in MCP listener: {e}")

    async def _handle_message(self, message: dict[str, Any]):
        """Handle incoming JSON-RPC message"""
        # Handle Response
        if "id" in message and ("result" in message or "error" in message):
            req_id = message["id"]
            if req_id in self.pending_requests:
                future = self.pending_requests.pop(req_id)
                if "error" in message:
                    future.set_exception(Exception(f"MCP Error: {message['error']}"))
                else:
                    future.set_result(message["result"])
        # Handle Notifications (optional)

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        """Call an MCP tool"""
        if not self._writer:
            raise RuntimeError("MCP Client not connected")

        req_id = str(uuid.uuid4())
        request = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
            "id": req_id,
        }

        future = asyncio.Future()
        self.pending_requests[req_id] = future

        # Send request
        data = json.dumps(request) + "\n"
        self._writer.write(data.encode("utf-8"))
        await self._writer.drain()

        # Wait for response with timeout
        try:
            result = await asyncio.wait_for(future, timeout=30.0)

            # Check for tool error (MCP protocol)
            if isinstance(result, dict) and result.get("isError"):
                content = result.get("content", [])
                error_msg = "Unknown tool error"
                if content and isinstance(content, list) and len(content) > 0:
                    # Check if content item is text
                    item = content[0]
                    if isinstance(item, dict) and item.get("type") == "text":
                        error_msg = item.get("text", error_msg)

                raise Exception(f"Tool execution failed: {error_msg}")

            return result
        except asyncio.TimeoutError as e:
            if req_id in self.pending_requests:
                del self.pending_requests[req_id]
            raise TimeoutError(f"Tool call '{name}' timed out") from e

    async def list_tools(self) -> Any:
        """List available tools"""
        if not self._writer:
            raise RuntimeError("MCP Client not connected")

        req_id = str(uuid.uuid4())
        request = {"jsonrpc": "2.0", "method": "tools/list", "params": {}, "id": req_id}

        future = asyncio.Future()
        self.pending_requests[req_id] = future

        data = json.dumps(request) + "\n"
        self._writer.write(data.encode("utf-8"))
        await self._writer.drain()

        try:
            result = await asyncio.wait_for(future, timeout=10.0)

            # Check for tool error (MCP protocol)
            if isinstance(result, dict) and result.get("isError"):
                content = result.get("content", [])
                error_msg = "Unknown tool error"
                if content and isinstance(content, list) and len(content) > 0:
                    # Check if content item is text
                    item = content[0]
                    if isinstance(item, dict) and item.get("type") == "text":
                        error_msg = item.get("text", error_msg)

                raise Exception(f"Tool execution failed: {error_msg}")

            return result

        except asyncio.TimeoutError as e:
            if req_id in self.pending_requests:
                del self.pending_requests[req_id]
            raise TimeoutError("Tool list timed out") from e

    # High-Level Commands

    async def resolve_contact(self, contact_name: str) -> str | None:
        """
        Resolve contact name to JID.
        Priority:
        1. WhatsApp internal search (cached/exact match)
        2. System Contacts (via Messages contact_resolver)
        """
        try:
            # 1. Try WhatsApp Internal Search
            result = await self.call_tool("search_contacts", {"query": contact_name})

            # Simple parsing for WhatsApp internal results
            if isinstance(result, dict) and "content" in result:
                text_content = ""
                for item in result["content"]:
                    if item.get("type") == "text":
                        text_content += item.get("text", "")

                try:
                    contacts = json.loads(text_content)
                    if isinstance(contacts, list) and len(contacts) > 0:
                        logger.info(f"Contact found in WhatsApp (Internal): {contact_name}")
                        return contacts[0].get("jid")
                except json.JSONDecodeError:
                    pass

            # 2. Fallback: Try System Address Book (via Messages contact_resolver)
            logger.info(
                f"Contact not found in WhatsApp internal. Trying System Contacts for: {contact_name}"
            )
            from modules.messages.contact_resolver import find_contacts_by_name

            # Note: This is a synchronous call, running in executor to avoid blocking
            loop = asyncio.get_running_loop()
            system_contacts = await loop.run_in_executor(None, find_contacts_by_name, contact_name)

            if system_contacts:
                logger.info(f"DEBUG: System contacts found: {system_contacts}")

                # Check for errors in response and filter valid contacts
                valid_contacts = [c for c in system_contacts if "error" not in c]

                if isinstance(valid_contacts, list) and len(valid_contacts) > 1:
                    # Multiple system contacts found
                    names = [c.get("name", "Unknown") for c in valid_contacts]
                    raise AmbiguousContactError(
                        f"Multiple contacts found in System: {', '.join(names)}", choices=names
                    )

                if valid_contacts:
                    # Take the first phone number from the first valid contact
                    first_contact = valid_contacts[0]
                    phones = first_contact.get("phones", [])

                    if phones:
                        phone = phones[0]
                        # Clean number: remove non-digits
                        cleaned_phone = "".join(filter(str.isdigit, phone))

                        # Format as WhatsApp JID
                        jid = f"{cleaned_phone}@s.whatsapp.net"
                        logger.info(f"Contact found in System: {contact_name} -> {jid}")
                        return jid
                else:
                    logger.warning(
                        "No valid contacts returned from System (likely permission denied)."
                    )

            # 3. Fallback: Raw Phone Number
            # If the user provided a phone number directly, use it.
            cleaned_input = "".join(filter(str.isdigit, contact_name))
            if len(cleaned_input) >= 7:  # Heuristic: at least 7 digits to be a phone number
                jid = f"{cleaned_input}@s.whatsapp.net"
                logger.info(f"Input looks like a phone number. Using direct JID: {jid}")
                return jid

            # 4. Try fuzzy search for similar contacts
            similar_contacts = await self._find_similar_contacts(contact_name)
            if similar_contacts:
                suggestions = [
                    c.get("display_label", c.get("first_name", c.get("name", "Unknown")))
                    for c in similar_contacts[:5]
                ]
                raise SimilarContactsFoundError(
                    f"Contact '{contact_name}' not found. Did you mean: {', '.join(suggestions)}?",
                    contact_name=contact_name,
                    suggestions=suggestions,
                )

            raise ContactNotFoundError(
                f"Contact '{contact_name}' not found", contact_name=contact_name
            )
        except (AmbiguousContactError, SimilarContactsFoundError):
            raise  # Propagate up
        except Exception as e:
            logger.error(f"Contact resolution failed: {e}")
            raise  # Propagate unexpected errors too, or wrap them

    async def send_whatsapp_message(self, contact: str, message: str) -> str:
        """
        Send a WhatsApp message to a contact.
        1. Resolve contact name to JID.
        2. Send message via MCP.
        """

        # 1. Resolve Contact to JID
        try:
            jid = await self.resolve_contact(contact)
            logger.info(f"Sending WhatsApp message to '{contact}' ({jid}): '{message}'")

            # 2. Send message via MCP
            await self.call_tool("send_message", {"recipient": jid, "message": message})
            return f"Message sent to {contact}"
        except Exception as e:
            return f"Failed to send message: {e}"

    async def read_whatsapp_messages(self, contact: str | None = None) -> str:
        """Read messages"""
        if contact:
            jid = await self.resolve_contact(contact)

            res = await self.call_tool("list_messages", {"chat_id": jid, "limit": 5})
            return str(res)
        else:
            # List chats if no contact
            res = await self.call_tool("list_chats", {"limit": 5})
            return str(res)

    async def _find_similar_contacts(self, query: str) -> list[dict[str, Any]]:
        """
        Поиск похожих контактов по частичному совпадению имени.

        Args:
            query: Искомое имя (частичное)

        Returns:
            Список похожих контактов
        """
        from modules.messages.contact_resolver import find_contacts_by_name

        query_lower = query.lower().strip()
        if len(query_lower) < 2:
            return []

        similar = []
        loop = asyncio.get_running_loop()

        # Стратегия 1: Поиск по первым 2-3 буквам
        for prefix_len in [3, 2]:
            if len(query_lower) >= prefix_len:
                prefix = query_lower[:prefix_len]
                matches = await loop.run_in_executor(None, find_contacts_by_name, prefix)
                for m in matches:
                    label = (
                        m.get("display_label") or m.get("first_name") or m.get("name") or ""
                    ).lower()
                    if label.startswith(prefix) or query_lower in label or prefix in label:
                        if m not in similar:
                            similar.append(m)
                if similar:
                    break

        # Стратегия 2: Убираем последнюю букву
        if not similar and len(query_lower) >= 3:
            alt_query = query_lower[:-1]
            matches = await loop.run_in_executor(None, find_contacts_by_name, alt_query)
            for m in matches:
                if m not in similar:
                    similar.append(m)

        return similar[:5]


class AmbiguousContactError(Exception):
    def __init__(self, message, choices):
        super().__init__(message)
        self.choices = choices


class ContactNotFoundError(Exception):
    """Contact was not found in WhatsApp or system contacts"""

    def __init__(self, message, contact_name):
        super().__init__(message)
        self.contact_name = contact_name


class SimilarContactsFoundError(Exception):
    """Contact not found, but similar contacts were found"""

    def __init__(self, message, contact_name, suggestions):
        super().__init__(message)
        self.contact_name = contact_name
        self.suggestions = suggestions


class WhatsAppConnectionError(Exception):
    """WhatsApp service is not running or connection failed"""

    pass


class WhatsAppNotAuthenticatedError(Exception):
    """Session expired or not established, QR code required"""

    pass


class WhatsAppTimeoutError(Exception):
    """WhatsApp operation timed out"""

    pass
