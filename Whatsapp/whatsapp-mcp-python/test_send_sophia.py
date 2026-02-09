#!/usr/bin/env python3
"""
Тест отправки сообщения Sophia через Python MCP сервер
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SERVER_PATH = BASE_DIR / "whatsapp-mcp-python" / "server.py"

async def test_send_message():
    """Тестирует отправку сообщения через MCP"""
    print("📤 Тест отправки сообщения Sophia через Python MCP\n")
    print("=" * 60)
    
    # Запускаем сервер
    process = await asyncio.create_subprocess_exec(
        "python3", str(SERVER_PATH),
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
            "clientInfo": {"name": "test-client", "version": "1.0.0"}
        }
    }
    
    # Поиск контакта
    search_request = {
        "jsonrpc": "2.0",
        "id": request_id + 1,
        "method": "tools/call",
        "params": {
            "name": "search_contacts",
            "arguments": {"query": "Sophia"}
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
                "recipient": "Sophia",
                "message": "How are you?"
            }
        }
    }
    
    async def send_request_and_wait(req):
        """Отправляет запрос и ждет ответ"""
        req_json = json.dumps(req) + "\n"
        process.stdin.write(req_json.encode())
        await process.stdin.drain()
        
        # Читаем ответ
        while True:
            line = await process.stdout.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
            
            try:
                response = json.loads(line.decode().strip())
                if response.get("id") == req["id"]:
                    return response
            except json.JSONDecodeError:
                continue
    
    try:
        print("⏳ Инициализация...")
        init_response = await send_request_and_wait(init_request)
        print("✅ Инициализация завершена\n")
        
        print("🔍 Поиск контакта Sophia...")
        search_response = await send_request_and_wait(search_request)
        if search_response.get("result"):
            content = search_response["result"].get("content", [{}])[0].get("text", "")
            print(content)
        
        print("\n📤 Отправка сообщения...")
        send_response = await send_request_and_wait(send_request)
        if send_response.get("result"):
            content = send_response["result"].get("content", [{}])[0].get("text", "")
            print(content)
            if "successfully" in content.lower():
                print("\n✅ Сообщение отправлено успешно!")
            else:
                print("\n⚠️  Возможна ошибка при отправке")
        elif send_response.get("error"):
            print(f"❌ Ошибка: {send_response['error']}")
    
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    finally:
        process.terminate()
        await process.wait()

if __name__ == "__main__":
    asyncio.run(test_send_message())

