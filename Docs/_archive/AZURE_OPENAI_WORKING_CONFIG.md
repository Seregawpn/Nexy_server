# ✅ Рабочая конфигурация Azure OpenAI

**Дата:** 2025-01-20  
**Статус:** ✅ Протестировано и работает

---

## 🎯 Рабочие настройки

### Данные подключения

**Base URL:**
```
https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com/
```

**Deployment Name:**
```
gpt-5.2-chat
```

**API Key:**
```
Fjm2jiYGOJcVXft7stWQhg7SyBL20MH4azc07lDcdjGokwkrSSzgJQQJ99CAACHYHv6XJ3w3AAAAACOGjoz2
```

**API Version:**
```
2024-12-01-preview
```

---

## 🔧 Настройка в Cursor

### Шаг 1: Откройте настройки Cursor

1. Нажмите `Cmd + ,` (macOS) или `Ctrl + ,` (Windows/Linux)
2. Или через меню: `Cursor → Settings`

### Шаг 2: Найдите раздел AI/Model Settings

1. В поиске настроек введите: `model` или `ai provider`
2. Найдите раздел **"Model"** или **"AI Provider"**
3. Выберите провайдера: **"Azure OpenAI"**

### Шаг 3: Заполните данные

**Base URL:**
```
https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com/
```

**Deployment Name:**
```
gpt-5.2-chat
```

**API Key:**
```
Fjm2jiYGOJcVXft7stWQhg7SyBL20MH4azc07lDcdjGokwkrSSzgJQQJ99CAACHYHv6XJ3w3AAAAACOGjoz2
```

### Шаг 4: Сохраните и проверьте

1. Сохраните настройки
2. Перезапустите Cursor (если требуется)
3. Откройте чат и задайте тестовый вопрос
4. Проверьте, что ответ приходит от Azure OpenAI

---

## 🧪 Тестирование

### Через SDK (Python)

```bash
source client/.venv/bin/activate
python3 scripts/test_azure_openai_sdk.py \
    "https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com/" \
    "gpt-5.2-chat" \
    "Fjm2jiYGOJcVXft7stWQhg7SyBL20MH4azc07lDcdjGokwkrSSzgJQQJ99CAACHYHv6XJ3w3AAAAACOGjoz2"
```

### Через REST API

```bash
python3 scripts/test_azure_openai_config.py \
    "https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com" \
    "gpt-5.2-chat" \
    "Fjm2jiYGOJcVXft7stWQhg7SyBL20MH4azc07lDcdjGokwkrSSzgJQQJ99CAACHYHv6XJ3w3AAAAACOGjoz2"
```

---

## 📊 Результаты тестирования

✅ **Подключение:** Успешно  
✅ **Развертывание:** `gpt-5.2-chat` работает  
✅ **Модель:** `gpt-5.2-chat-2025-12-11`  
✅ **API Version:** `2024-12-01-preview`  
✅ **Тестовый запрос:** Выполнен успешно

**Пример ответа:**
```
Hello, Azure OpenAI is working!
```

---

## 💻 Пример кода (Python)

```python
from openai import AzureOpenAI

endpoint = "https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com/"
deployment = "gpt-5.2-chat"
api_key = "Fjm2jiYGOJcVXft7stWQhg7SyBL20MH4azc07lDcdjGokwkrSSzgJQQJ99CAACHYHv6XJ3w3AAAAACOGjoz2"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=16384,
    model=deployment
)

print(response.choices[0].message.content)
```

---

## ✅ Чек-лист

- [x] Библиотека `openai` установлена
- [x] Тест через SDK выполнен успешно
- [ ] Настройки Cursor обновлены
- [ ] Тестовый запрос в Cursor выполнен
- [ ] Все работает корректно

---

## 🔗 Связанные документы

- `scripts/test_azure_openai_sdk.py` — тестирование через SDK
- `scripts/test_azure_openai_config.py` — тестирование через REST API
- `Docs/AZURE_OPENAI_TOOLS_SUMMARY.md` — сводка всех инструментов

---

**Конфигурация протестирована и готова к использованию!**
