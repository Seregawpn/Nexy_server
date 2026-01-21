# 📊 Отчет о настройках Azure OpenAI

**Дата проверки:** 2025-01-20  
**Метод проверки:** Azure CLI  
**Статус:** ✅ Ресурс найден и активен

---

## ✅ Найденные настройки

### Основная информация

| Параметр | Значение |
|----------|----------|
| **Ресурс** | `nexy-ai-core` |
| **Группа ресурсов** | `NetworkWatcherRG` |
| **Регион** | `canadacentral` (Canada Central) |
| **Статус** | `Succeeded` ✅ |
| **Тип** | `AIServices` (Cognitive Services) |

### Base URL (Endpoint)

**Полученный через Azure CLI:**
```
https://nexy-ai-core.cognitiveservices.azure.com/
```

**⚠️ ВАЖНО:** Этот URL отличается от указанного ранее:
```
https://nexy-ai-core.openai.azure.com/
```

**Рекомендация:** Используйте URL, полученный через Azure CLI, так как он является официальным endpoint ресурса.

### API Keys

- ✅ **KEY 1:** Существует и активен
- ✅ **KEY 2:** Существует и активен

**Действие:** Получите ключи вручную через Azure Portal:
1. Откройте [Azure Portal](https://portal.azure.com)
2. Найдите ресурс: `nexy-ai-core`
3. Перейдите в **"Keys and Endpoint"**
4. Скопируйте **KEY 1** или **KEY 2**

---

## ❓ Что нужно проверить вручную

### 1. Deployment Name (Имя развертывания)

**Где проверить:**
1. Azure Portal → `nexy-ai-core` → **"Model deployments"**
2. Или Azure OpenAI Studio: https://oai.azure.com/ → **"Deployments"**

**Что проверить:**
- [ ] Есть ли развертывание с именем: `OpenAICreate-2026011`
- [ ] Если нет, какое имя у существующих развертываний?
- [ ] Статус развертывания: должен быть **"Succeeded"**

**Текущее предположение:** `OpenAICreate-2026011` (нужно подтвердить в Azure Portal)

---

## 🔧 Настройки для Cursor

### Вариант 1: Используя найденный Base URL

**Base URL:**
```
https://nexy-ai-core.cognitiveservices.azure.com/
```

**Deployment Name:**
```
OpenAICreate-2026011
```
(подтвердите в Azure Portal)

**API Key:**
```
(получите из Azure Portal → Keys and Endpoint)
```

### Вариант 2: Если нужен формат openai.azure.com

Если Cursor требует формат `openai.azure.com`, попробуйте:

**Base URL:**
```
https://nexy-ai-core.openai.azure.com/
```

**Deployment Name:**
```
OpenAICreate-2026011
```

**API Key:**
```
(тот же ключ из Azure Portal)
```

---

## 🧪 Проверка правильности Base URL

Для проверки, какой URL правильный, запустите:

```bash
# Установите API ключ
export AZURE_OPENAI_API_KEY="ваш_ключ_здесь"

# Проверьте с cognitiveservices.azure.com
curl -X POST \
  "https://nexy-ai-core.cognitiveservices.azure.com/openai/deployments/OpenAICreate-2026011/chat/completions?api-version=2024-02-15-preview" \
  -H "api-key: ${AZURE_OPENAI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}],"max_tokens":10}'

# Проверьте с openai.azure.com
curl -X POST \
  "https://nexy-ai-core.openai.azure.com/openai/deployments/OpenAICreate-2026011/chat/completions?api-version=2024-02-15-preview" \
  -H "api-key: ${AZURE_OPENAI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}],"max_tokens":10}'
```

Тот URL, который вернет **200 OK**, и является правильным.

---

## 📋 Чек-лист для завершения настройки

- [ ] Получен API ключ из Azure Portal → Keys and Endpoint
- [ ] Проверен Deployment Name в Azure Portal → Model deployments
- [ ] Выбран правильный Base URL (cognitiveservices.azure.com или openai.azure.com)
- [ ] Все данные введены в Cursor
- [ ] Cursor перезапущен
- [ ] Тестовый запрос в Cursor работает

---

## 🔗 Полезные ссылки

- **Azure Portal:** https://portal.azure.com
- **Azure OpenAI Studio:** https://oai.azure.com/
- **Ресурс напрямую:** https://portal.azure.com/#@/resource/subscriptions/*/resourceGroups/NetworkWatcherRG/providers/Microsoft.CognitiveServices/accounts/nexy-ai-core

---

## 📝 Следующие шаги

1. **Откройте Azure Portal** и проверьте Deployment Name
2. **Скопируйте API ключ** из раздела Keys and Endpoint
3. **Обновите настройки в Cursor** с правильными данными
4. **Протестируйте подключение** через скрипт: `./scripts/test_azure_openai_key.sh`

---

**Создано автоматически скриптом:** `scripts/check_azure_openai_settings.sh`
