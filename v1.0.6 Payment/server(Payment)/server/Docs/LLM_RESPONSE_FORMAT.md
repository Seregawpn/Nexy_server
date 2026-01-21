# Формат ответов LLM для Nexy Assistant

## Общий формат

LLM должен возвращать ответы в одном из двух форматов:

### 1. Обычный текстовый ответ (без действия)

```json
{
  "text": "Привет! Как дела? Чем могу помочь?"
}
```

Или просто строка:
```
Привет! Как дела? Чем могу помочь?
```

### 2. Ответ с действием (Action Response)

```json
{
  "session_id": "session_1764210832.530743",
  "command": "open_app",
  "args": {
    "app_name": "Safari"
  },
  "text": "Открываю Safari."
}
```

## Детали формата Action Response

### Обязательные поля:
- `session_id` (string) - ID сессии из запроса
- `command` (string) - тип команды (например, "open_app")
- `args` (object) - аргументы команды
- `text` (string) - текстовый ответ для TTS (может быть пустым)

### Поддерживаемые команды:

#### `open_app`
```json
{
  "session_id": "session_123",
  "command": "open_app",
  "args": {
    "app_name": "Safari"
  },
  "text": "Открываю Safari."
}
```

**Валидация:**
- `args.app_name` обязателен и не должен быть пустым
- Можно использовать `args.app_path` вместо `args.app_name`

#### `close_app`
```json
{
  "session_id": "session_123",
  "command": "close_app",
  "args": {
    "app_name": "Safari"
  },
  "text": "Закрываю Safari."
}
```

**Валидация:**
- `args.app_name` обязателен и не должен быть пустым
- Формат идентичен `open_app`

### Примеры полных ответов:

#### Пример 1: Открытие приложения
```json
{
  "session_id": "session_1764210832.530743",
  "command": "open_app",
  "args": {
    "app_name": "Calculator"
  },
  "text": "Открываю калькулятор."
}
```

#### Пример 1.1: Закрытие приложения
```json
{
  "session_id": "session_1764210832.530743",
  "command": "close_app",
  "args": {
    "app_name": "Safari"
  },
  "text": "Закрываю Safari."
}
```

#### Пример 2: Обычный ответ без действия
```json
{
  "text": "Калькулятор уже открыт. Что вы хотите вычислить?"
}
```

#### Пример 3: Ответ с пустым текстом (только действие)
```json
{
  "session_id": "session_1764210832.530743",
  "command": "open_app",
  "args": {
    "app_name": "Safari"
  },
  "text": ""
}
```

## Обработка на сервере

1. `AssistantResponseParser` парсит ответ
2. Если есть `command` → создаётся `command_payload` для MCP
3. `text` используется для генерации TTS
4. `command_payload` отправляется клиенту через `__MCP__` префикс

## Важно

- Если `command` указан, но отсутствует `session_id` или `args.app_name` → команда игнорируется, возвращается только `text`
- Если `command` не указан → обычный текстовый ответ
- `text` всегда должен быть строкой (может быть пустой)
- Для `open_app` можно использовать `args.app_path` вместо `args.app_name`
- Для `close_app` требуется только `args.app_name` (без `app_path`)

