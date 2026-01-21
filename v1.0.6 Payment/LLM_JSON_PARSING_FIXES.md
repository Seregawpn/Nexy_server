# 🔧 Исправления парсинга JSON-команд от LLM

> **Дата:** 2025-12-13  
> **Проблемы:** Несостыковка формата, хрупкий regex, отсутствие guardrails

---

## ✅ Исправленные проблемы

### 1. Унифицирован канонический формат

**Было:** Разные форматы (`payload` vs `args`, `command` string vs object)

**Стало:** Единственный канонический формат:
```json
{
  "command": "create_subscription",
  "args": {},
  "text": "Opening subscription page..."
}
```

**Правила:**
- ✅ `command` - строка (название команды)
- ✅ `args` - объект (параметры команды, НЕ содержит `hardware_id`)
- ✅ `text` - строка (текстовый ответ для TTS)
- ❌ НЕ поддерживается: `{"command": {"type": "...", "payload": {}}}`
- ❌ НЕ поддерживается: `{"command": "...", "payload": {}}`

---

### 2. Заменен хрупкий regex на balanced braces extraction

**Было:**
```python
# Хрупкий regex - не работает с вложенными объектами
json_match = re.search(r'\{[^{}]*"command"[^{}]*\}', response, re.DOTALL)
```

**Проблемы:**
- ❌ Не работает с вложенными объектами в `args`
- ❌ Не работает с многострочным JSON
- ❌ Не работает если в тексте есть фигурные скобки

**Стало:**
```python
def _extract_json_with_balanced_braces(self, text: str) -> Optional[str]:
    """
    Извлекает JSON объект с помощью balanced braces (поддержка вложенных объектов)
    
    Ищет первый объект, содержащий "command", используя счетчик скобок.
    """
    # Ищем позицию "command" в тексте
    command_pos = text.find('"command"')
    if command_pos == -1:
        return None
    
    # Ищем начало объекта (первая { перед "command")
    start_pos = text.rfind('{', 0, command_pos)
    if start_pos == -1:
        return None
    
    # Проходимся с счетчиком скобок до закрывающей }
    brace_count = 0
    i = start_pos
    
    while i < len(text):
        if text[i] == '{':
            brace_count += 1
        elif text[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                # Нашли закрывающую скобку
                return text[start_pos:i+1]
        i += 1
    
    return None
```

**Преимущества:**
- ✅ Работает с вложенными объектами
- ✅ Работает с многострочным JSON
- ✅ Устойчив к фигурным скобкам в тексте

---

### 3. Добавлены guardrails

#### 3.1. Лимит размера JSON

```python
MAX_JSON_SIZE = 16 * 1024  # 16KB лимит

# Проверка размера ответа
if len(response) > MAX_JSON_SIZE:
    logger.warning(f"[PARSER] Response too large: {len(response)} bytes")
    return None

# Проверка размера извлеченного JSON
if len(json_str) > MAX_JSON_SIZE:
    logger.warning(f"[PARSER] JSON too large: {len(json_str)} bytes")
    return None
```

#### 3.2. Строгая схема валидации

```python
def _validate_json_schema(self, data: dict) -> bool:
    """
    Валидация схемы JSON: разрешены только command/args/text
    
    ⚠️ КРИТИЧНО: Строгая схема - все лишние поля удаляются
    """
    if not isinstance(data, dict):
        return False
    
    # Обязательное поле: command
    if "command" not in data:
        return False
    
    # Разрешенные поля: command, args, text
    allowed_keys = {"command", "args", "text"}
    extra_keys = set(data.keys()) - allowed_keys
    
    if extra_keys:
        logger.warning(
            f"[PARSER] Extra keys in JSON (ignoring): {extra_keys}. "
            f"Allowed: {allowed_keys}"
        )
        # Удаляем лишние ключи
        for key in extra_keys:
            data.pop(key)
    
    # Проверка типов
    if not isinstance(data.get("command"), str):
        return False
    
    if "args" in data and not isinstance(data.get("args"), dict):
        return False
    
    if "text" in data and not isinstance(data.get("text"), str):
        return False
    
    return True
```

#### 3.3. Лимит размера args

```python
# В validate_command
MAX_ARGS_SIZE = 8 * 1024  # 8KB
args_size = len(json.dumps(args))
if args_size > MAX_ARGS_SIZE:
    return False, f"args too large: {args_size} bytes (max {MAX_ARGS_SIZE})"
```

---

### 4. Приоритет парсинга

**Порядок попыток извлечения JSON:**

1. **Code fence с языком:** ` ```json {...} ``` `
2. **Code fence без языка:** ` ``` {...} ``` `
3. **Весь ответ - JSON:** `{...}`
4. **Balanced braces extraction:** извлечение из текста с помощью счетчика скобок

**Правило:** Если парсинг/валидация не прошли → возвращаем только текст, команду игнорируем

---

### 5. Исправлены все места с несостыковкой формата

**Было:**
```python
# Несостыковка: payload вместо args
payload = command_payload.get('payload', {})
command = payload.get('command')
```

**Стало:**
```python
# Унифицировано: везде args
payload = command_payload.get('payload', {})
command = payload.get('command')
args = payload.get('args', {})  # ✅ args, не payload
```

**Исправлено в:**
- `_execute_subscription_command` - везде используется `args`
- `parse_response` - формирование `command_payload` с `args`
- Все примеры в документации

---

## 📋 Чеклист правильного парсинга

### Обязательные проверки:

- [ ] **Верификация формата:** только `command/args/text`
- [ ] **Лимит размера:** 16KB для JSON, 8KB для args
- [ ] **Строгая схема:** лишние поля удаляются
- [ ] **Balanced braces:** для inline JSON (не regex)
- [ ] **hardware_id:** только из gRPC, никогда из JSON
- [ ] **Валидация типов:** command=str, args=dict, text=str
- [ ] **Обработка ошибок:** при ошибке парсинга → только текст

### Рекомендуемые практики:

- [ ] Логирование всех ошибок парсинга
- [ ] Метрики для мониторинга (parse_failure_rate)
- [ ] Fallback на текстовый ответ при любой ошибке
- [ ] Тестирование на разных форматах ответов LLM

---

## 🎯 Итоговый формат

### Канонический формат от LLM:

```json
{
  "command": "create_subscription",
  "args": {},
  "text": "Opening subscription page..."
}
```

### Формат command_payload для выполнения:

```json
{
  "event": "subscription.command_request",
  "payload": {
    "session_id": "session_123",
    "command": "create_subscription",
    "args": {},
    "hardware_id": "hw_xxx",  // ⭐ Из gRPC
    "feature_id": "F-2025-017-stripe-payment"
  }
}
```

---

**Статус:** ✅ Все проблемы исправлены в `COMPLETE_SYSTEM_LOGIC.md`

**Следующий шаг:** Интегрировать исправленный парсер в реальный код






























