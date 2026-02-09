# Архитектура системы WhatsApp MCP Server

## 📐 Общая схема системы

```
┌─────────────────────────────────────────────────────────────────┐
│                         Cursor IDE                               │
│                    (MCP Client)                                  │
└────────────────────────────┬──────────────────────────────────────┘
                             │ JSON-RPC 2.0
                             │ (stdio)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              Python MCP Server                                   │
│              (server.py)                                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  MCP Tools:                                              │  │
│  │  - search_contacts                                       │  │
│  │  - list_chats                                            │  │
│  │  - list_messages                                         │  │
│  │  - send_message                                          │  │
│  │  - get_chat                                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────┐         ┌──────────────────────────┐    │
│  │  SQLite Database │◄────────┤  Direct Read Operations │    │
│  │  (whatsapp.db)   │         │  - list_chats_from_db()  │    │
│  └──────────────────┘         │  - list_messages_from_db()│    │
│                                │  - search_contacts_in_db()│    │
│                                └──────────────────────────┘    │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Contact Resolver                                        │  │
│  │  (from Messages project)                                 │  │
│  │  - get_contact_name()                                    │  │
│  │  - enrich_chat_name()                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Send Message Handler                                    │  │
│  │  - send_message_via_node()                              │  │
│  │    └─► Calls Node.js Baileys Server                     │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬──────────────────────────────────────┘
                             │ JSON-RPC 2.0
                             │ (subprocess)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│         Node.js Baileys Server                                  │
│         (main.js)                                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Baileys Library                                         │  │
│  │  (@whiskeysockets/baileys)                               │  │
│  │  - makeWASocket()                                        │  │
│  │  - useMultiFileAuthState()                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────┐         ┌──────────────────────────┐    │
│  │  Auth Info       │         │  WhatsApp Web API        │    │
│  │  (auth_info/)    │         │  Connection              │    │
│  │  - creds.json    │         │  - WebSocket             │    │
│  │  - keys/         │         │  - Message Sending       │    │
│  └──────────────────┘         └──────────────────────────┘    │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Database Operations                                     │  │
│  │  - storeChat()                                           │  │
│  │  - storeMessage()                                        │  │
│  │  - getChats()                                            │  │
│  │  - getMessages()                                         │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬──────────────────────────────────────┘
                             │ WhatsApp Web API
                             │ (WebSocket)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    WhatsApp Servers                             │
│                    (Meta/Facebook)                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Потоки данных

### 1. Получение списка чатов

```
Cursor → Python MCP Server
         │
         ├─► list_chats_from_db()
         │   └─► SQLite Database (whatsapp.db)
         │       └─► SELECT chats ORDER BY last_message_time
         │
         ├─► enrich_chat_name() для каждого чата
         │   └─► contact_resolver.py
         │       └─► macOS Contacts/Messages DB
         │
         └─► Форматирование ответа (стандартизированный формат)
             └─► Cursor (JSON-RPC response)
```

**Код:**
```python
# server.py: list_chats_from_db()
conn = sqlite3.connect(DB_PATH)
cursor.execute("SELECT jid, name, last_message_time, ... FROM chats ...")
chats = cursor.fetchall()
for chat in chats:
    enriched_name = enrich_chat_name(chat['jid'], chat['name'])
    # Форматирование в стандартизированный формат
```

---

### 2. Получение сообщений

```
Cursor → Python MCP Server
         │
         ├─► list_messages_from_db(chat_jid)
         │   └─► SQLite Database
         │       └─► SELECT messages WHERE chat_jid = ?
         │
         ├─► enrich_chat_name() для отправителя
         │   └─► contact_resolver.py
         │
         └─► Форматирование ответа
             └─► Cursor
```

**Код:**
```python
# server.py: list_messages_from_db()
cursor.execute("""
    SELECT id, sender, content, timestamp, is_from_me
    FROM messages
    WHERE chat_jid = ?
    ORDER BY timestamp DESC
""", (chat_jid,))
```

---

### 3. Поиск контактов

```
Cursor → Python MCP Server
         │
         ├─► search_contacts_in_db(query)
         │   └─► SQLite Database
         │       └─► SELECT chats WHERE name LIKE ? OR jid LIKE ?
         │
         ├─► enrich_chat_name() для каждого результата
         │   └─► contact_resolver.py
         │
         └─► Форматирование ответа
             └─► Cursor
```

**Код:**
```python
# server.py: search_contacts_in_db()
cursor.execute("""
    SELECT DISTINCT jid, name 
    FROM chats 
    WHERE name LIKE ? OR jid LIKE ?
    ORDER BY last_message_time DESC
    LIMIT 20
""", (f"%{query}%", f"%{query}%"))
```

---

### 4. Отправка сообщения

```
Cursor → Python MCP Server
         │
         ├─► send_message_via_node(recipient, message)
         │   │
         │   ├─► Запуск Node.js процесса
         │   │   └─► subprocess.Popen("node", BAILEYS_SERVER)
         │   │
         │   ├─► Инициализация MCP
         │   │   └─► JSON-RPC: initialize
         │   │
         │   ├─► Вызов инструмента
         │   │   └─► JSON-RPC: tools/call {name: "send_message"}
         │   │
         │   └─► Получение ответа
         │       └─► JSON-RPC response
         │
         └─► Форматирование ответа
             └─► Cursor
```

**Node.js Baileys Server:**
```
JSON-RPC Request → Node.js Baileys Server
                    │
                    ├─► makeWASocket()
                    │   └─► useMultiFileAuthState(auth_info/)
                    │       └─► Загрузка сохраненной авторизации
                    │
                    ├─► sock.sendMessage(jid, {text: message})
                    │   └─► WhatsApp Web API (WebSocket)
                    │       └─► WhatsApp Servers
                    │
                    └─► JSON-RPC Response
                        └─► Python MCP Server
```

**Код:**
```python
# server.py: send_message_via_node()
process = await asyncio.create_subprocess_exec(
    "node", str(BAILEYS_SERVER),
    stdin=asyncio.subprocess.PIPE,
    stdout=asyncio.subprocess.PIPE
)

# Инициализация
await send_and_wait_response(init_request)

# Отправка сообщения
response = await send_and_wait_response(send_request)
```

---

### 5. Получение информации о чате

```
Cursor → Python MCP Server
         │
         ├─► get_chat(chat_jid)
         │   │
         │   ├─► SQLite Database
         │   │   └─► SELECT jid, name, last_message_time FROM chats
         │   │
         │   ├─► COUNT(*) FROM messages WHERE chat_jid = ?
         │   │
         │   └─► enrich_chat_name()
         │       └─► contact_resolver.py
         │
         └─► Форматирование ответа
             └─► Cursor
```

---

## 📦 Компоненты системы

### 1. Python MCP Server (`server.py`)

**Ответственность:**
- Обработка MCP запросов от Cursor
- Прямое чтение из SQLite базы данных
- Обогащение имен контактов из macOS
- Вызов Node.js сервера для отправки сообщений
- Форматирование ответов в стандартизированном формате

**Основные функции:**
- `list_chats_from_db()` - получение чатов из БД
- `list_messages_from_db()` - получение сообщений из БД
- `search_contacts_in_db()` - поиск контактов в БД
- `enrich_chat_name()` - обогащение имен из macOS
- `send_message_via_node()` - отправка через Node.js

**Зависимости:**
- `mcp` - MCP протокол
- `sqlite3` - база данных
- `asyncio` - асинхронность
- `subprocess` - запуск Node.js

---

### 2. Node.js Baileys Server (`main.js`)

**Ответственность:**
- Подключение к WhatsApp через Baileys
- Отправка сообщений через WhatsApp Web API
- Сохранение авторизации
- Синхронизация чатов и сообщений в БД

**Основные компоненты:**
- `startWhatsAppConnection()` - установка подключения
- `useMultiFileAuthState()` - управление авторизацией
- `makeWASocket()` - создание WebSocket соединения
- `storeChat()` / `storeMessage()` - сохранение в БД

**Зависимости:**
- `@whiskeysockets/baileys` - WhatsApp Web API клиент
- `@modelcontextprotocol/sdk` - MCP протокол
- `better-sqlite3` - база данных

---

### 3. База данных SQLite (`whatsapp.db`)

**Структура:**

```sql
-- Таблица чатов
CREATE TABLE chats (
    jid TEXT PRIMARY KEY,
    name TEXT,
    last_message_time TEXT
);

-- Таблица сообщений
CREATE TABLE messages (
    id TEXT,
    chat_jid TEXT,
    sender TEXT,
    content TEXT,
    timestamp TEXT,
    is_from_me INTEGER,
    PRIMARY KEY (id, chat_jid),
    FOREIGN KEY (chat_jid) REFERENCES chats(jid)
);
```

**Операции:**
- **Чтение:** Python сервер читает напрямую
- **Запись:** Node.js сервер записывает при получении сообщений

---

### 4. Авторизация (`auth_info/`)

**Структура:**
```
auth_info/
├── creds.json          # Учетные данные
└── keys/               # Ключи шифрования
    ├── app-state-sync-key-*.json
    └── ...
```

**Процесс:**
1. При первом запуске генерируется QR код
2. Пользователь сканирует QR код через WhatsApp
3. Авторизация сохраняется в `auth_info/`
4. При следующих запусках авторизация загружается автоматически

**Код:**
```javascript
// whatsapp.js
const { state, saveCreds } = await useMultiFileAuthState(AUTH_DIR);
sock.ev.on("creds.update", saveCreds);
```

---

### 5. Contact Resolver (`contact_resolver.py`)

**Источники имен (в порядке приоритета):**
1. Messages.display_name - имя из Messages приложения
2. AddressBook SQLite - локальная база контактов macOS
3. Contacts.framework - системные контакты (iCloud/Google)
4. Fallback - номер телефона, если имя не найдено

**Использование:**
```python
# server.py
def enrich_chat_name(jid: str, current_name: Optional[str] = None) -> str:
    phone_number = jid.split("@")[0]
    return get_contact_name(phone_number)
```

---

## 🔐 Безопасность и авторизация

### Процесс авторизации:

1. **Первый запуск:**
   ```
   Node.js Baileys Server → useMultiFileAuthState()
                          → QR код генерируется
                          → Пользователь сканирует
                          → Авторизация сохраняется в auth_info/
   ```

2. **Последующие запуски:**
   ```
   Node.js Baileys Server → useMultiFileAuthState()
                          → Загрузка из auth_info/
                          → Автоматическое подключение
   ```

3. **Обновление авторизации:**
   ```
   WhatsApp → creds.update event
           → saveCreds()
           → Обновление auth_info/
   ```

---

## 📊 Формат данных

### Стандартизированный формат ответов:

**Список чатов:**
```
Чаты (страница 1):

1. <Имя>
   JID: <jid>
   Телефон: <номер>
   Последнее сообщение: <отправитель>: <текст>
   Время: <ISO timestamp>
```

**Сообщения:**
```
Сообщения из чата: <Имя> (<JID>)

[<ISO timestamp>] <Отправитель>: <Текст>
```

**Отправка:**
```
✅ Сообщение отправлено успешно
Получатель: <Имя> (<JID>)
ID сообщения: <id>
Время отправки: <ISO timestamp>
```

---

## 🚀 Производительность

### Оптимизации:

1. **Прямое чтение из БД:**
   - Python сервер читает напрямую из SQLite
   - Не требует Node.js для чтения
   - Быстрый доступ к данным

2. **Кэширование имен:**
   - Имена контактов обогащаются при запросе
   - Можно добавить кэш для часто используемых контактов

3. **Асинхронность:**
   - Все операции асинхронные
   - Не блокирует выполнение

---

## 🔄 Синхронизация данных

### Как данные попадают в БД:

1. **При подключении:**
   ```
   Node.js Baileys → messaging-history.set event
                  → storeChat() / storeMessage()
                  → SQLite Database
   ```

2. **При получении новых сообщений:**
   ```
   WhatsApp → messages.upsert event
          → parseMessageForDb()
          → storeMessage()
          → SQLite Database
   ```

3. **При отправке:**
   ```
   Python Server → Node.js Baileys
                → sock.sendMessage()
                → WhatsApp
                → messages.upsert event (своё сообщение)
                → storeMessage()
                → SQLite Database
   ```

---

## 📝 Логирование

### Уровни логирования:

- **Python MCP Server:** stdout/stderr (через MCP протокол)
- **Node.js Baileys Server:** 
  - `wa-logs.txt` - логи WhatsApp подключения
  - `mcp-logs.txt` - логи MCP сервера

---

## 🎯 Итоговая схема взаимодействия

```
┌──────────┐
│  Cursor  │
└────┬─────┘
     │ JSON-RPC
     ▼
┌─────────────────┐     ┌──────────────┐
│ Python MCP      │────►│ SQLite DB    │ (чтение)
│ Server          │     │ (whatsapp.db)│
└────┬────────────┘     └──────────────┘
     │
     │ JSON-RPC (для отправки)
     ▼
┌─────────────────┐     ┌──────────────┐
│ Node.js Baileys │────►│ Auth Info    │
│ Server          │     │ (auth_info/) │
└────┬────────────┘     └──────────────┘
     │
     │ WhatsApp Web API
     ▼
┌─────────────────┐
│ WhatsApp        │
│ Servers         │
└─────────────────┘
```

---

## ✅ Преимущества архитектуры

1. **Разделение ответственности:**
   - Python для обработки запросов и чтения
   - Node.js для подключения к WhatsApp

2. **Производительность:**
   - Прямое чтение из БД (быстро)
   - Асинхронные операции

3. **Надежность:**
   - Автоматическое сохранение авторизации
   - Обработка ошибок

4. **Расширяемость:**
   - Легко добавить новые инструменты
   - Модульная структура

---

**Дата создания:** 2025-12-01  
**Версия:** 1.0

