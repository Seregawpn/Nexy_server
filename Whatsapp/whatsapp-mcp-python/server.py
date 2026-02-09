#!/usr/bin/env python3
"""
Python MCP сервер для WhatsApp через Baileys
Использует базу данных напрямую и Node.js только для отправки сообщений
QR код нужно сканировать только один раз - авторизация сохраняется в auth_info/
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional, List, Dict
import sqlite3
from datetime import datetime

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Пути
BASE_DIR = Path(__file__).parent.parent
BAILEYS_DIR = BASE_DIR / "whatsapp-mcp-ready" / "node_modules" / "@iflow-mcp" / "whatsapp-mcp-ts"
BAILEYS_SERVER = BAILEYS_DIR / "build" / "main.js"
AUTH_DIR = BAILEYS_DIR / "data" / "auth_info"
DB_PATH = BAILEYS_DIR / "data" / "whatsapp.db"
CONTACT_RESOLVER = Path("/Users/sergiyzasorin/Messages/contact_resolver.py")

# Инициализация MCP сервера
server = Server("whatsapp-python")

def get_contact_name(phone_number: str) -> str:
    """Получает имя контакта из macOS"""
    try:
        if CONTACT_RESOLVER.exists():
            import importlib.util
            spec = importlib.util.spec_from_file_location("contact_resolver", CONTACT_RESOLVER)
            if spec and spec.loader:
                contact_resolver = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(contact_resolver)
                contact = contact_resolver.resolve_contact(phone_number)
                return contact.get("display_label", phone_number)
    except Exception as e:
        print(f"Ошибка получения имени контакта: {e}", file=sys.stderr)
    return phone_number

def enrich_chat_name(jid: str, current_name: Optional[str] = None) -> str:
    """Обогащает имя чата из контактов macOS"""
    if current_name and current_name != jid.split("@")[0]:
        return current_name
    
    phone_number = jid.split("@")[0]
    return get_contact_name(phone_number)

def get_db_connection():
    """Получает соединение с базой данных"""
    if not DB_PATH.exists():
        return None
    return sqlite3.connect(str(DB_PATH))

def extract_phone_number(jid: str) -> str:
    """Извлекает номер телефона из JID"""
    return jid.split("@")[0]

def search_contacts_in_db(query: str) -> List[Dict]:
    """Поиск контактов в базе данных (стандартизированный формат)"""
    conn = get_db_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    # Ищем по имени или JID
    cursor.execute("""
        SELECT DISTINCT jid, name 
        FROM chats 
        WHERE name LIKE ? OR jid LIKE ?
        ORDER BY last_message_time DESC
        LIMIT 20
    """, (f"%{query}%", f"%{query}%"))
    
    results = []
    for jid, name in cursor.fetchall():
        enriched_name = enrich_chat_name(jid, name)
        phone = extract_phone_number(jid)
        results.append({
            "jid": jid,
            "name": enriched_name,
            "phone": phone
        })
    
    conn.close()
    return results

def list_chats_from_db(limit: int = 20, page: int = 0) -> List[Dict]:
    """Получает список чатов из базы данных (стандартизированный формат)"""
    # Валидация параметров
    limit = max(1, min(limit, 100))  # От 1 до 100
    page = max(0, page)  # Не меньше 0
    
    conn = get_db_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    offset = page * limit
    cursor.execute("""
        SELECT jid, name, last_message_time, 
               (SELECT content FROM messages WHERE chat_jid = chats.jid ORDER BY timestamp DESC LIMIT 1) as last_message,
               (SELECT sender FROM messages WHERE chat_jid = chats.jid ORDER BY timestamp DESC LIMIT 1) as last_sender,
               (SELECT is_from_me FROM messages WHERE chat_jid = chats.jid ORDER BY timestamp DESC LIMIT 1) as last_is_from_me
        FROM chats
        ORDER BY last_message_time DESC NULLS LAST
        LIMIT ? OFFSET ?
    """, (limit, offset))
    
    chats = []
    for row in cursor.fetchall():
        jid, name, last_time, last_msg, last_sender, last_is_from_me = row
        enriched_name = enrich_chat_name(jid, name)
        phone = extract_phone_number(jid)
        
        # Форматируем отправителя последнего сообщения
        if last_is_from_me:
            sender_display = "Вы"
        elif last_sender:
            sender_display = enrich_chat_name(last_sender, last_sender.split("@")[0])
        else:
            sender_display = "Unknown"
        
        chats.append({
            "jid": jid,
            "name": enriched_name,
            "phone": phone,
            "last_message_time": last_time or "",
            "last_message": last_msg or "",
            "last_sender": sender_display,
            "last_is_from_me": bool(last_is_from_me) if last_is_from_me is not None else None
        })
    
    conn.close()
    return chats

def list_messages_from_db(chat_jid: str, limit: int = 20, page: int = 0) -> List[Dict]:
    """Получает сообщения из чата (стандартизированный формат)"""
    # Валидация параметров
    limit = max(1, min(limit, 100))  # От 1 до 100
    page = max(0, page)  # Не меньше 0
    
    conn = get_db_connection()
    if not conn:
        return []
    
    cursor = conn.cursor()
    offset = page * limit
    cursor.execute("""
        SELECT id, sender, content, timestamp, is_from_me
        FROM messages
        WHERE chat_jid = ?
        ORDER BY timestamp DESC
        LIMIT ? OFFSET ?
    """, (chat_jid, limit, offset))
    
    messages = []
    for row in cursor.fetchall():
        msg_id, sender, content, timestamp, is_from_me = row
        if is_from_me:
            sender_name = "Вы"
        elif sender:
            sender_name = enrich_chat_name(sender, sender.split("@")[0])
        else:
            sender_name = "Unknown"
        
        messages.append({
            "id": msg_id,
            "sender": sender_name,
            "content": content or "",
            "timestamp": timestamp or "",
            "is_from_me": bool(is_from_me)
        })
    
    conn.close()
    return messages

async def send_message_via_node(recipient: str, message: str) -> str:
    """Отправляет сообщение через существующий Node.js Baileys MCP сервер"""
    # Используем существующий Node.js сервер через MCP протокол
    process = await asyncio.create_subprocess_exec(
        "node", str(BAILEYS_SERVER),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    request_id = 1
    
    # Инициализация
    init_request = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "whatsapp-python", "version": "1.0.0"}
        }
    }
    
    # Проверка подключения через list_chats
    check_request = {
        "jsonrpc": "2.0",
        "id": request_id + 1,
        "method": "tools/call",
        "params": {
            "name": "list_chats",
            "arguments": {"limit": 1}
        }
    }
    
    # Отправка сообщения
    send_request = {
        "jsonrpc": "2.0",
        "id": request_id + 2,
        "method": "tools/call",
        "params": {
            "name": "send_message",
            "arguments": {
                "recipient": recipient,
                "message": message
            }
        }
    }
    
    async def send_and_wait_response(req, timeout=30):
        """Отправляет запрос и ждет ответ"""
        req_json = json.dumps(req) + "\n"
        process.stdin.write(req_json.encode())
        await process.stdin.drain()
        
        # Читаем ответ
        start_time = asyncio.get_event_loop().time()
        buffer = b""
        
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            try:
                chunk = await asyncio.wait_for(process.stdout.read(1024), timeout=0.5)
                if not chunk:
                    await asyncio.sleep(0.1)
                    continue
                
                buffer += chunk
                lines = buffer.split(b"\n")
                buffer = lines.pop() if lines else b""
                
                for line in lines:
                    if not line.strip():
                        continue
                    try:
                        response = json.loads(line.decode().strip())
                        if response.get("id") == req["id"]:
                            return response
                    except (json.JSONDecodeError, UnicodeDecodeError):
                        continue
            except asyncio.TimeoutError:
                continue
        
        raise TimeoutError("Timeout waiting for response")
    
    try:
        # Инициализация
        await send_and_wait_response(init_request, timeout=5)
        
        # Ждем подключения (проверяем через list_chats)
        await asyncio.sleep(3)  # Даем время на подключение
        try:
            check_response = await send_and_wait_response(check_request, timeout=10)
            # Если проверка прошла, продолжаем
        except:
            pass  # Продолжаем даже если проверка не прошла
        
        # Отправка сообщения
        response = await send_and_wait_response(send_request, timeout=15)
        
        if response.get("result"):
            content = response["result"].get("content", [{}])[0].get("text", "")
            return content
        elif response.get("error"):
            return f"Failed to send message: {response['error']}"
        else:
            return "Unknown response format"
    
    except TimeoutError:
        return "Timeout: Connection not ready. Please ensure WhatsApp is connected and try again."
    except Exception as e:
        return f"Failed to send message: {str(e)}"
    finally:
        try:
            process.terminate()
            await asyncio.wait_for(process.wait(), timeout=2.0)
        except:
            try:
                process.kill()
            except:
                pass

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Список доступных инструментов"""
    return [
        Tool(
            name="search_contacts",
            description="Поиск контактов в WhatsApp по имени или номеру телефона",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Имя контакта или номер телефона для поиска"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_chats",
            description="Получить список чатов с последними сообщениями",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Максимальное количество чатов (по умолчанию 20)",
                        "default": 20
                    },
                    "page": {
                        "type": "integer",
                        "description": "Номер страницы (0-indexed)",
                        "default": 0
                    }
                }
            }
        ),
        Tool(
            name="list_messages",
            description="Получить сообщения из конкретного чата",
            inputSchema={
                "type": "object",
                "properties": {
                    "chat_jid": {
                        "type": "string",
                        "description": "JID чата (например, '123456@s.whatsapp.net') или имя контакта"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Максимальное количество сообщений",
                        "default": 20
                    },
                    "page": {
                        "type": "integer",
                        "description": "Номер страницы",
                        "default": 0
                    }
                },
                "required": ["chat_jid"]
            }
        ),
        Tool(
            name="send_message",
            description="Отправить сообщение контакту или группе",
            inputSchema={
                "type": "object",
                "properties": {
                    "recipient": {
                        "type": "string",
                        "description": "JID получателя (например, '123456@s.whatsapp.net') или имя контакта"
                    },
                    "message": {
                        "type": "string",
                        "description": "Текст сообщения для отправки"
                    }
                },
                "required": ["recipient", "message"]
            }
        ),
        Tool(
            name="get_chat",
            description="Получить информацию о конкретном чате",
            inputSchema={
                "type": "object",
                "properties": {
                    "chat_jid": {
                        "type": "string",
                        "description": "JID чата или имя контакта"
                    }
                },
                "required": ["chat_jid"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Обработка вызовов инструментов"""
    try:
        if name == "search_contacts":
            query = arguments.get("query", "").strip()
            if not query:
                return [TextContent(type="text", text="❌ Ошибка: Параметр 'query' обязателен и не может быть пустым")]
            
            results = search_contacts_in_db(query)
            
            if not results:
                return [TextContent(type="text", text=f"Контакты не найдены для запроса: {query}")]
            
            # Стандартизированный формат: имя, JID, телефон
            output = f"Найдено контактов: {len(results)}\n\n"
            for i, contact in enumerate(results, 1):
                output += f"{i}. {contact['name']}\n"
                output += f"   JID: {contact['jid']}\n"
                output += f"   Телефон: {contact['phone']}\n\n"
            
            return [TextContent(type="text", text=output)]
        
        elif name == "list_chats":
            limit = arguments.get("limit", 20)
            page = arguments.get("page", 0)
            
            # Валидация
            if not isinstance(limit, int) or limit < 1:
                limit = 20
            if not isinstance(page, int) or page < 0:
                page = 0
            
            chats = list_chats_from_db(limit, page)
            
            if not chats:
                return [TextContent(type="text", text="Чаты не найдены")]
            
            # Стандартизированный формат: имя, JID, телефон, последнее сообщение, время
            output = f"Чаты (страница {page + 1}):\n\n"
            for i, chat in enumerate(chats, 1):
                output += f"{i}. {chat['name']}\n"
                output += f"   JID: {chat['jid']}\n"
                output += f"   Телефон: {chat['phone']}\n"
                if chat['last_message']:
                    output += f"   Последнее сообщение: {chat['last_sender']}: {chat['last_message']}\n"
                if chat['last_message_time']:
                    output += f"   Время: {chat['last_message_time']}\n"
                output += "\n"
            
            return [TextContent(type="text", text=output)]
        
        elif name == "list_messages":
            chat_jid = arguments.get("chat_jid", "").strip()
            limit = arguments.get("limit", 20)
            page = arguments.get("page", 0)
            
            if not chat_jid:
                return [TextContent(type="text", text="❌ Ошибка: Параметр 'chat_jid' обязателен")]
            
            # Валидация
            if not isinstance(limit, int) or limit < 1:
                limit = 20
            if not isinstance(page, int) or page < 0:
                page = 0
            
            # Если это имя, ищем JID
            original_jid = chat_jid
            if not chat_jid.endswith("@s.whatsapp.net") and not chat_jid.endswith("@g.us"):
                results = search_contacts_in_db(chat_jid)
                if results:
                    chat_jid = results[0]["jid"]
                    chat_name = results[0]["name"]
                else:
                    return [TextContent(type="text", text=f"❌ Чат не найден: {original_jid}")]
            else:
                # Получаем имя для JID
                conn = get_db_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT name FROM chats WHERE jid = ?", (chat_jid,))
                    row = cursor.fetchone()
                    conn.close()
                    chat_name = enrich_chat_name(chat_jid, row[0] if row else None)
                else:
                    chat_name = chat_jid
            
            messages = list_messages_from_db(chat_jid, limit, page)
            
            if not messages:
                return [TextContent(type="text", text=f"Сообщения не найдены для чата: {chat_name} ({chat_jid})")]
            
            # Стандартизированный формат: имя чата, JID, сообщения с временными метками
            output = f"Сообщения из чата: {chat_name} ({chat_jid})\n\n"
            for msg in reversed(messages):  # Показываем в хронологическом порядке
                output += f"[{msg['timestamp']}] {msg['sender']}: {msg['content']}\n"
            
            return [TextContent(type="text", text=output)]
        
        elif name == "send_message":
            recipient = arguments.get("recipient", "").strip()
            message = arguments.get("message", "").strip()
            
            # Валидация
            if not recipient:
                return [TextContent(type="text", text="❌ Ошибка: Параметр 'recipient' обязателен")]
            if not message:
                return [TextContent(type="text", text="❌ Ошибка: Параметр 'message' обязателен и не может быть пустым")]
            if len(message) > 4096:
                return [TextContent(type="text", text="❌ Ошибка: Сообщение слишком длинное (максимум 4096 символов)")]
            
            original_recipient = recipient
            recipient_name = recipient
            
            # Если recipient - имя, ищем JID
            if not recipient.endswith("@s.whatsapp.net") and not recipient.endswith("@g.us"):
                results = search_contacts_in_db(recipient)
                if results:
                    recipient = results[0]["jid"]
                    recipient_name = results[0]["name"]
                else:
                    return [TextContent(type="text", text=f"❌ Контакт не найден: {original_recipient}")]
            
            result = await send_message_via_node(recipient, message)
            
            # Стандартизированный формат ответа
            if "successfully" in result.lower() or "успешно" in result.lower():
                # Извлекаем ID сообщения из ответа
                import re
                msg_id_match = re.search(r'ID:\s*([A-F0-9]+)', result)
                msg_id = msg_id_match.group(1) if msg_id_match else "unknown"
                
                from datetime import datetime
                timestamp = datetime.utcnow().isoformat() + "Z"
                
                formatted_result = f"✅ Сообщение отправлено успешно\n"
                formatted_result += f"Получатель: {recipient_name} ({recipient})\n"
                formatted_result += f"ID сообщения: {msg_id}\n"
                formatted_result += f"Время отправки: {timestamp}"
                return [TextContent(type="text", text=formatted_result)]
            else:
                return [TextContent(type="text", text=f"❌ Ошибка отправки сообщения\nПолучатель: {recipient_name} ({recipient})\nПричина: {result}")]
        
        elif name == "get_chat":
            chat_jid = arguments.get("chat_jid", "").strip()
            
            if not chat_jid:
                return [TextContent(type="text", text="❌ Ошибка: Параметр 'chat_jid' обязателен")]
            
            # Если это имя, ищем JID
            if not chat_jid.endswith("@s.whatsapp.net") and not chat_jid.endswith("@g.us"):
                results = search_contacts_in_db(chat_jid)
                if results:
                    chat_jid = results[0]["jid"]
                else:
                    return [TextContent(type="text", text=f"❌ Чат не найден: {chat_jid}")]
            
            conn = get_db_connection()
            if not conn:
                return [TextContent(type="text", text="❌ База данных не доступна")]
            
            cursor = conn.cursor()
            cursor.execute("SELECT jid, name, last_message_time FROM chats WHERE jid = ?", (chat_jid,))
            row = cursor.fetchone()
            
            if not row:
                conn.close()
                return [TextContent(type="text", text=f"❌ Чат не найден: {chat_jid}")]
            
            jid, name, last_time = row
            enriched_name = enrich_chat_name(jid, name)
            phone = extract_phone_number(jid)
            
            # Подсчитываем количество сообщений
            cursor.execute("SELECT COUNT(*) FROM messages WHERE chat_jid = ?", (chat_jid,))
            message_count = cursor.fetchone()[0]
            
            conn.close()
            
            # Стандартизированный формат: имя, JID, телефон, последнее сообщение, всего сообщений
            output = f"Информация о чате:\n"
            output += f"Имя: {enriched_name}\n"
            output += f"JID: {jid}\n"
            output += f"Телефон: {phone}\n"
            if last_time:
                output += f"Последнее сообщение: {last_time}\n"
            output += f"Всего сообщений: {message_count}\n"
            
            return [TextContent(type="text", text=output)]
        
        else:
            return [TextContent(type="text", text=f"Неизвестный инструмент: {name}")]
    
    except Exception as e:
        import traceback
        error_msg = f"Ошибка: {str(e)}\n{traceback.format_exc()}"
        return [TextContent(type="text", text=error_msg)]

async def main():
    """Главная функция"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
