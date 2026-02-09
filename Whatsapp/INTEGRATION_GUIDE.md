# Руководство по интеграции WhatsApp MCP Server

## 📋 Содержание

1. [Обзор интеграции](#обзор-интеграции)
2. [Формат подключения](#формат-подключения)
3. [Формат запросов](#формат-запросов)
4. [Формат ответов](#формат-ответов)
5. [Примеры интеграции](#примеры-интеграции)
6. [Обработка ошибок](#обработка-ошибок)
7. [Лучшие практики](#лучшие-практики)

---

## Обзор интеграции

### Что такое MCP?

**Model Context Protocol (MCP)** - открытый стандарт для подключения AI приложений к внешним системам через JSON-RPC 2.0.

### Как работает интеграция?

```
Ваше приложение → JSON-RPC 2.0 → Python MCP Server → WhatsApp
```

### Требования:

- Python 3.8+
- Установленный MCP сервер (`pip install mcp`)
- Настроенная конфигурация MCP

---

## Формат подключения

### 1. Через MCP протокол (рекомендуется)

**Конфигурация MCP клиента:**

```json
{
  "mcpServers": {
    "whatsapp-python": {
      "command": "python3",
      "args": [
        "/path/to/whatsapp-mcp-python/server.py"
      ],
      "timeout": 30
    }
  }
}
```

**Инициализация:**

```python
import subprocess
import json
import asyncio

# Запуск MCP сервера
process = subprocess.Popen(
    ["python3", "/path/to/server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Инициализация
init_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "your-app",
            "version": "1.0.0"
        }
    }
}

process.stdin.write(json.dumps(init_request) + "\n")
process.stdin.flush()
```

---

### 2. Прямое подключение к базе данных (только чтение)

**Для чтения данных можно подключаться напрямую к SQLite:**

```python
import sqlite3
from pathlib import Path

DB_PATH = Path("/path/to/whatsapp-mcp-ready/node_modules/@iflow-mcp/whatsapp-mcp-ts/data/whatsapp.db")

def get_chats(limit=20, page=0):
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    offset = page * limit
    cursor.execute("""
        SELECT jid, name, last_message_time
        FROM chats
        ORDER BY last_message_time DESC
        LIMIT ? OFFSET ?
    """, (limit, offset))
    
    chats = cursor.fetchall()
    conn.close()
    
    return chats
```

**⚠️ Внимание:** Прямое подключение только для чтения. Для отправки сообщений используйте MCP протокол.

---

## Формат запросов

### JSON-RPC 2.0 формат

Все запросы следуют стандарту JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "id": <уникальный_id>,
  "method": "<метод>",
  "params": {
    "<параметры>"
  }
}
```

### Доступные методы:

#### 1. `tools/list` - Получить список инструментов

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

#### 2. `tools/call` - Вызвать инструмент

**Поиск контактов:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "search_contacts",
    "arguments": {
      "query": "Sophia"
    }
  }
}
```

**Список чатов:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "list_chats",
    "arguments": {
      "limit": 5,
      "page": 0
    }
  }
}
```

**Сообщения из чата:**
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "list_messages",
    "arguments": {
      "chat_jid": "Sophia",
      "limit": 10,
      "page": 0
    }
  }
}
```

**Отправка сообщения:**
```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "tools/call",
  "params": {
    "name": "send_message",
    "arguments": {
      "recipient": "Sophia",
      "message": "Hello!"
    }
  }
}
```

**Информация о чате:**
```json
{
  "jsonrpc": "2.0",
  "id": 6,
  "method": "tools/call",
  "params": {
    "name": "get_chat",
    "arguments": {
      "chat_jid": "Sophia"
    }
  }
}
```

---

## Формат ответов

### Успешный ответ:

```json
{
  "jsonrpc": "2.0",
  "id": <id_запроса>,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "<текстовый_ответ>"
      }
    ]
  }
}
```

### Ошибка:

```json
{
  "jsonrpc": "2.0",
  "id": <id_запроса>,
  "error": {
    "code": <код_ошибки>,
    "message": "<сообщение_об_ошибке>"
  }
}
```

### Стандартизированный формат текстовых ответов:

#### Поиск контактов:
```
Найдено контактов: <количество>

<номер>. <Имя>
   JID: <jid>
   Телефон: <номер>
```

#### Список чатов:
```
Чаты (страница <номер>):

<номер>. <Имя>
   JID: <jid>
   Телефон: <номер>
   Последнее сообщение: <отправитель>: <текст>
   Время: <ISO timestamp>
```

#### Сообщения:
```
Сообщения из чата: <Имя> (<JID>)

[<ISO timestamp>] <Отправитель>: <Текст>
```

#### Отправка сообщения:
```
✅ Сообщение отправлено успешно
Получатель: <Имя> (<JID>)
ID сообщения: <id>
Время отправки: <ISO timestamp>
```

---

## Примеры интеграции

### Python

```python
import asyncio
import json
import subprocess
from pathlib import Path

class WhatsAppMCPClient:
    def __init__(self, server_path):
        self.server_path = server_path
        self.process = None
        self.request_id = 0
    
    async def start(self):
        """Запуск MCP сервера"""
        self.process = await asyncio.create_subprocess_exec(
            "python3", str(self.server_path),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        # Инициализация
        await self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "my-app", "version": "1.0.0"}
        })
    
    async def _send_request(self, method, params):
        """Отправка запроса и получение ответа"""
        self.request_id += 1
        req_id = self.request_id
        
        request = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params
        }
        
        req_json = json.dumps(request) + "\n"
        self.process.stdin.write(req_json.encode())
        await self.process.stdin.drain()
        
        # Читаем ответ
        while True:
            line = await self.process.stdout.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
            
            try:
                response = json.loads(line.decode().strip())
                if response.get("id") == req_id:
                    return response
            except json.JSONDecodeError:
                continue
    
    async def search_contacts(self, query):
        """Поиск контактов"""
        response = await self._send_request("tools/call", {
            "name": "search_contacts",
            "arguments": {"query": query}
        })
        
        if response.get("result"):
            return response["result"]["content"][0]["text"]
        return None
    
    async def list_chats(self, limit=20, page=0):
        """Получить список чатов"""
        response = await self._send_request("tools/call", {
            "name": "list_chats",
            "arguments": {"limit": limit, "page": page}
        })
        
        if response.get("result"):
            return response["result"]["content"][0]["text"]
        return None
    
    async def send_message(self, recipient, message):
        """Отправить сообщение"""
        response = await self._send_request("tools/call", {
            "name": "send_message",
            "arguments": {
                "recipient": recipient,
                "message": message
            }
        })
        
        if response.get("result"):
            return response["result"]["content"][0]["text"]
        return None
    
    async def stop(self):
        """Остановка сервера"""
        if self.process:
            self.process.terminate()
            await self.process.wait()

# Использование
async def main():
    client = WhatsAppMCPClient(Path("/path/to/server.py"))
    await client.start()
    
    # Поиск контактов
    contacts = await client.search_contacts("Sophia")
    print(contacts)
    
    # Список чатов
    chats = await client.list_chats(limit=5)
    print(chats)
    
    # Отправка сообщения
    result = await client.send_message("Sophia", "Hello!")
    print(result)
    
    await client.stop()

asyncio.run(main())
```

---

### JavaScript/Node.js

```javascript
const { spawn } = require('child_process');
const path = require('path');

class WhatsAppMCPClient {
    constructor(serverPath) {
        this.serverPath = serverPath;
        this.process = null;
        this.requestId = 0;
        this.pendingRequests = new Map();
    }
    
    async start() {
        return new Promise((resolve) => {
            this.process = spawn('python3', [this.serverPath], {
                stdio: ['pipe', 'pipe', 'pipe']
            });
            
            let buffer = '';
            this.process.stdout.on('data', (data) => {
                buffer += data.toString();
                const lines = buffer.split('\n');
                buffer = lines.pop() || '';
                
                for (const line of lines) {
                    if (line.trim()) {
                        try {
                            const response = JSON.parse(line);
                            const id = response.id;
                            if (this.pendingRequests.has(id)) {
                                const { resolve } = this.pendingRequests.get(id);
                                this.pendingRequests.delete(id);
                                resolve(response);
                            }
                        } catch (e) {
                            // Не JSON
                        }
                    }
                }
            });
            
            // Инициализация
            this.sendRequest('initialize', {
                protocolVersion: '2024-11-05',
                capabilities: {},
                clientInfo: { name: 'my-app', version: '1.0.0' }
            }).then(() => resolve());
        });
    }
    
    async sendRequest(method, params) {
        return new Promise((resolve) => {
            this.requestId++;
            const id = this.requestId;
            
            const request = {
                jsonrpc: '2.0',
                id: id,
                method: method,
                params: params
            };
            
            this.pendingRequests.set(id, { resolve });
            this.process.stdin.write(JSON.stringify(request) + '\n');
        });
    }
    
    async searchContacts(query) {
        const response = await this.sendRequest('tools/call', {
            name: 'search_contacts',
            arguments: { query }
        });
        
        if (response.result) {
            return response.result.content[0].text;
        }
        return null;
    }
    
    async listChats(limit = 20, page = 0) {
        const response = await this.sendRequest('tools/call', {
            name: 'list_chats',
            arguments: { limit, page }
        });
        
        if (response.result) {
            return response.result.content[0].text;
        }
        return null;
    }
    
    async sendMessage(recipient, message) {
        const response = await this.sendRequest('tools/call', {
            name: 'send_message',
            arguments: { recipient, message }
        });
        
        if (response.result) {
            return response.result.content[0].text;
        }
        return null;
    }
    
    stop() {
        if (this.process) {
            this.process.kill();
        }
    }
}

// Использование
(async () => {
    const client = new WhatsAppMCPClient('/path/to/server.py');
    await client.start();
    
    const contacts = await client.searchContacts('Sophia');
    console.log(contacts);
    
    const chats = await client.listChats(5);
    console.log(chats);
    
    const result = await client.sendMessage('Sophia', 'Hello!');
    console.log(result);
    
    client.stop();
})();
```

---

### HTTP API (обертка)

```python
from flask import Flask, request, jsonify
import asyncio
from whatsapp_mcp_client import WhatsAppMCPClient

app = Flask(__name__)
client = None

@app.before_first_request
def init_client():
    global client
    client = WhatsAppMCPClient(Path("/path/to/server.py"))
    asyncio.run(client.start())

@app.route('/api/search', methods=['POST'])
def search_contacts():
    data = request.json
    query = data.get('query')
    
    result = asyncio.run(client.search_contacts(query))
    return jsonify({"result": result})

@app.route('/api/chats', methods=['GET'])
def list_chats():
    limit = request.args.get('limit', 20, type=int)
    page = request.args.get('page', 0, type=int)
    
    result = asyncio.run(client.list_chats(limit, page))
    return jsonify({"result": result})

@app.route('/api/send', methods=['POST'])
def send_message():
    data = request.json
    recipient = data.get('recipient')
    message = data.get('message')
    
    result = asyncio.run(client.send_message(recipient, message))
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=5000)
```

---

## Обработка ошибок

### Типы ошибок:

1. **Ошибка подключения:**
```json
{
  "error": {
    "code": -32000,
    "message": "Connection not ready"
  }
}
```

2. **Ошибка валидации:**
```json
{
  "error": {
    "code": -32602,
    "message": "Параметр 'query' обязателен"
  }
}
```

3. **Ошибка отправки:**
```json
{
  "error": {
    "code": -32001,
    "message": "Failed to send message: Connection timeout"
  }
}
```

### Обработка в коде:

```python
async def safe_send_message(client, recipient, message):
    try:
        result = await client.send_message(recipient, message)
        if "успешно" in result.lower() or "successfully" in result.lower():
            return {"success": True, "message": result}
        else:
            return {"success": False, "error": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

---

## Лучшие практики

### 1. Управление соединением

- ✅ Переиспользуйте одно соединение для нескольких запросов
- ✅ Закрывайте соединение при завершении работы
- ✅ Обрабатывайте таймауты

### 2. Обработка ответов

- ✅ Всегда проверяйте наличие `result` или `error`
- ✅ Парсите текстовые ответы согласно стандартизированному формату
- ✅ Обрабатывайте ошибки gracefully

### 3. Производительность

- ✅ Используйте пагинацию для больших списков
- ✅ Кэшируйте результаты поиска контактов
- ✅ Не делайте слишком частые запросы

### 4. Безопасность

- ✅ Не храните авторизацию в коде
- ✅ Используйте переменные окружения для путей
- ✅ Валидируйте входные данные

---

## Формат данных для интеграции

### Входные данные (стандартизированные):

```python
# Поиск контактов
{
    "query": "Sophia"  # string, required
}

# Список чатов
{
    "limit": 20,  # integer, 1-100, default: 20
    "page": 0     # integer, >= 0, default: 0
}

# Сообщения
{
    "chat_jid": "Sophia",  # string, required (имя или JID)
    "limit": 20,           # integer, 1-100, default: 20
    "page": 0              # integer, >= 0, default: 0
}

# Отправка сообщения
{
    "recipient": "Sophia",  # string, required (имя или JID)
    "message": "Hello!"     # string, required, max: 4096
}
```

### Выходные данные (стандартизированные):

```python
# Успешный ответ
{
    "success": True,
    "data": "<текстовый_ответ_в_стандартизированном_формате>"
}

# Ошибка
{
    "success": False,
    "error": "<описание_ошибки>"
}
```

---

## Пример полной интеграции

```python
import asyncio
from whatsapp_mcp_client import WhatsAppMCPClient
from pathlib import Path

async def full_integration_example():
    # Инициализация
    client = WhatsAppMCPClient(Path("/path/to/server.py"))
    await client.start()
    
    try:
        # 1. Поиск контакта
        print("Поиск контакта...")
        contacts = await client.search_contacts("Sophia")
        print(contacts)
        
        # 2. Получение списка чатов
        print("\nПолучение списка чатов...")
        chats = await client.list_chats(limit=5)
        print(chats)
        
        # 3. Получение сообщений
        print("\nПолучение сообщений...")
        messages = await client.send_request("tools/call", {
            "name": "list_messages",
            "arguments": {"chat_jid": "Sophia", "limit": 10}
        })
        if messages.get("result"):
            print(messages["result"]["content"][0]["text"])
        
        # 4. Отправка сообщения
        print("\nОтправка сообщения...")
        result = await client.send_message("Sophia", "Hello from integration!")
        print(result)
        
    finally:
        await client.stop()

if __name__ == "__main__":
    asyncio.run(full_integration_example())
```

---

## ✅ Чеклист интеграции

- [ ] Установлен Python 3.8+
- [ ] Установлен MCP (`pip install mcp`)
- [ ] Настроен путь к `server.py`
- [ ] Реализована инициализация MCP
- [ ] Реализована обработка JSON-RPC запросов
- [ ] Реализована обработка ответов
- [ ] Реализована обработка ошибок
- [ ] Протестированы все функции
- [ ] Документирован код интеграции

---

**Дата создания:** 2025-12-01  
**Версия:** 1.0

