
import asyncio
import json
import logging
import uuid
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class WhatsappMCPClient:
    """
    Client for interacting with the WhatsApp MCP Server (Node.js).
    Handles JSON-RPC communication and high-level command mapping.
    """
    
    def __init__(self, service_manager):
        self.service_manager = service_manager
        self.pending_requests: Dict[str, asyncio.Future] = {}
        self._listener_task: Optional[asyncio.Task] = None
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        
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
                    
                decoded_line = line.decode('utf-8').strip()
                if not decoded_line:
                    continue
                    
                try:
                    message = json.loads(decoded_line)
                    await self._handle_message(message)
                except json.JSONDecodeError:
                    logger.warning(f"Invalid JSON received from WhatsApp service: {decoded_line}")
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            logger.error(f"Error in MCP listener: {e}")
            
    async def _handle_message(self, message: Dict[str, Any]):
        """Handle incoming JSON-RPC message"""
        # Handle Response
        if 'id' in message and ('result' in message or 'error' in message):
            req_id = message['id']
            if req_id in self.pending_requests:
                future = self.pending_requests.pop(req_id)
                if 'error' in message:
                    future.set_exception(Exception(f"MCP Error: {message['error']}"))
                else:
                    future.set_result(message['result'])
        # Handle Notifications (optional)
        
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """Call an MCP tool"""
        if not self._writer:
            raise RuntimeError("MCP Client not connected")
            
        req_id = str(uuid.uuid4())
        request = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            },
            "id": req_id
        }
        
        future = asyncio.Future()
        self.pending_requests[req_id] = future
        
        # Send request
        data = json.dumps(request) + "\n"
        self._writer.write(data.encode('utf-8'))
        await self._writer.drain()
        
        # Wait for response with timeout
        try:
            return await asyncio.wait_for(future, timeout=30.0)
        except asyncio.TimeoutError:
            if req_id in self.pending_requests:
                del self.pending_requests[req_id]
            raise TimeoutError(f"Tool call '{name}' timed out")

    async def list_tools(self) -> Any:
        """List available tools"""
        if not self._writer:
            raise RuntimeError("MCP Client not connected")
            
        req_id = str(uuid.uuid4())
        request = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "params": {},
            "id": req_id
        }
        
        future = asyncio.Future()
        self.pending_requests[req_id] = future
        
        data = json.dumps(request) + "\n"
        self._writer.write(data.encode('utf-8'))
        await self._writer.drain()
        
        try:
            return await asyncio.wait_for(future, timeout=10.0)
        except asyncio.TimeoutError:
            if req_id in self.pending_requests:
                del self.pending_requests[req_id]
            raise TimeoutError("tools/list timed out")


    # High-Level Commands
    
    async def resolve_contact(self, contact_name: str) -> Optional[str]:
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
            if isinstance(result, dict) and 'content' in result:
                text_content = ""
                for item in result['content']:
                    if item.get('type') == 'text':
                         text_content += item.get('text', '')
                
                try:
                    contacts = json.loads(text_content)
                    if isinstance(contacts, list) and len(contacts) > 0:
                        logger.info(f"Contact found in WhatsApp (Internal): {contact_name}")
                        return contacts[0].get('jid')
                except json.JSONDecodeError:
                    pass

            # 2. Fallback: Try System Address Book (via Messages contact_resolver)
            logger.info(f"Contact not found in WhatsApp internal. Trying System Contacts for: {contact_name}")
            from modules.messages.contact_resolver import find_contacts_by_name
            
            # Note: This is a synchronous call, running in executor to avoid blocking
            loop = asyncio.get_running_loop()
            system_contacts = await loop.run_in_executor(None, find_contacts_by_name, contact_name)
            
            if system_contacts:
                logger.info(f"DEBUG: System contacts found: {system_contacts}")
                
                # Check for errors in response and filter valid contacts
                valid_contacts = [c for c in system_contacts if 'error' not in c]
                
                if isinstance(valid_contacts, list) and len(valid_contacts) > 1:
                     # Multiple system contacts found
                     names = [c.get('name', 'Unknown') for c in valid_contacts]
                     raise AmbiguousContactError(f"Multiple contacts found in System: {', '.join(names)}", choices=names)

                if valid_contacts:
                    # Take the first phone number from the first valid contact
                    first_contact = valid_contacts[0]
                    phones = first_contact.get('phones', [])
                    
                    if phones:
                        phone = phones[0]
                        # Clean number: remove non-digits
                        cleaned_phone = "".join(filter(str.isdigit, phone))
                        
                        # Format as WhatsApp JID
                        jid = f"{cleaned_phone}@s.whatsapp.net"
                        logger.info(f"Contact found in System: {contact_name} -> {jid}")
                        return jid
                else:
                    logger.warning("No valid contacts returned from System (likely permission denied).")

            # 3. Fallback: Raw Phone Number
            # If the user provided a phone number directly, use it.
            cleaned_input = "".join(filter(str.isdigit, contact_name))
            if len(cleaned_input) >= 7:  # Heuristic: at least 7 digits to be a phone number
                jid = f"{cleaned_input}@s.whatsapp.net"
                logger.info(f"Input looks like a phone number. Using direct JID: {jid}")
                return jid
            
            raise ContactNotFoundError(f"Contact '{contact_name}' not found", contact_name=contact_name)
        except AmbiguousContactError:
            raise # Propagate up
        except Exception as e:
            logger.error(f"Contact resolution failed: {e}")
            raise # Propagate unexpected errors too, or wrap them

    async def send_whatsapp_message(self, contact: str, message: str) -> str:
        """Send message"""
        jid = await self.resolve_contact(contact)
            
        try:
            await self.call_tool("send_message", {"recipient": jid, "message": message})
            return f"Message sent to {contact}"
        except Exception as e:
            return f"Failed to send message: {e}"

    async def read_whatsapp_messages(self, contact: Optional[str] = None) -> str:
        """Read messages"""
        if contact:
            jid = await self.resolve_contact(contact)
            
            res = await self.call_tool("list_messages", {"chat_id": jid, "limit": 5})
            return str(res)
        else:
            # List chats if no contact
            res = await self.call_tool("list_chats", {"limit": 5})
            return str(res)

class AmbiguousContactError(Exception):
    def __init__(self, message, choices):
        super().__init__(message)
        self.choices = choices

class ContactNotFoundError(Exception):
    def __init__(self, message, contact_name):
        super().__init__(message)
        self.contact_name = contact_name
