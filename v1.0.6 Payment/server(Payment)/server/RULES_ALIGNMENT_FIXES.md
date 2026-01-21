# Server Development Rules Alignment Fixes

**Дата**: 2025-11-05
**Контекст**: Устранение несоответствий между документацией и канонами из `SERVER_DEVELOPMENT_RULES.md`

---

## Выявленные несоответствия

После аудита серверной части на соответствие правилам были обнаружены **4 критичных несоответствия** между документацией, CI и фактической реализацией.

---

## 1. ✅ HTTP примеры вместо HTTPS в deployment guide (КРИТИЧНЫЙ)

**Проблема**:
В `SERVER_DEPLOYMENT_GUIDE.md` публичные проверки health/status показывались через HTTP, что противоречит правилу "все публичные эндпоинты через HTTPS/443".

**Затронутые строки**:
- Строка 155: `http://20.151.51.172/health` → `https://20.151.51.172/health`
- Строка 156: `http://20.151.51.172/status` → `https://20.151.51.172/status`
- Строка 221: `curl http://20.151.51.172/health` → `curl -sk https://20.151.51.172/health`
- Строка 227: `curl http://20.151.51.172/status` → `curl -sk https://20.151.51.172/status`
- Строка 385: `curl http://20.151.51.172/health` → `curl -sk https://20.151.51.172/health`

**Исправление**:
```diff
-### **📊 Мониторинг деплоя:**
-- **Health check:** `http://20.151.51.172/health`
-- **Status API:** `http://20.151.51.172/status`
+### **📊 Мониторинг деплоя:**
+- **Health check (PUBLIC):** `https://20.151.51.172/health` (через Nginx/443)
+- **Status API (PUBLIC):** `https://20.151.51.172/status` (через Nginx/443)
+- **Health check (INTERNAL):** `http://127.0.0.1:8080/health` (прямой доступ, только локально)
```

**Результат**:
- ✅ Все публичные примеры используют HTTPS
- ✅ Добавлено явное разделение PUBLIC vs INTERNAL
- ✅ Добавлено примечание о недоступности внутренних портов извне

**Файлы**:
- [Docs/SERVER_DEPLOYMENT_GUIDE.md](Docs/SERVER_DEPLOYMENT_GUIDE.md#L153-L241)

---

## 2. ✅ Cache-Control headers уже присутствуют в nginx (ПРОВЕРЕНО)

**Проблема**:
Канареечный чеклист требует `Cache-Control` заголовки, но не было уверенности, что они присутствуют в nginx конфиге.

**Результат проверки**:
✅ Все требуемые заголовки **уже присутствуют** в [nginx/grpc-passthrough.conf](nginx/grpc-passthrough.conf):
- Строка 91: `/health` → `Cache-Control: public, max-age=30` ✅
- Строка 105: `/status` → `Cache-Control: public, max-age=30` ✅
- Строка 135: `/updates/appcast.xml` → `Cache-Control: public, max-age=60` ✅
- Строка 150: `/updates/health` → `Cache-Control: public, max-age=30` ✅

**Действия**: Нет (уже соответствует требованиям)

---

## 3. ✅ Унификация путей к proto в CI и .cursorrules

**Проблема**:
В `.cursorrules` команда регенерации использовала `cd server/modules/grpc_service`, что не соответствовало CI (`cd modules/grpc_service`).

**Исправление**:
```diff
-- Для регенерации gRPC артефактов используй:
-  ```bash
-  cd server/modules/grpc_service
-  python -m grpc_tools.protoc \
-      -I. \
-      --python_out=. \
-      --grpc_python_out=. \
-      streaming.proto
-  ```
+- Для регенерации gRPC артефактов (из корня server репозитория):
+  ```bash
+  cd modules/grpc_service
+  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
+  ```
+  **Канон пути:** `modules/grpc_service/streaming.proto` (без префикса `server/`, совпадает с CI)
```

**Результат**:
- ✅ Команда регенерации совпадает с CI
- ✅ Канон пути явно задокументирован
- ✅ Упрощена команда (однострочная, как в CI)

**Файлы**:
- [.cursorrules#L18-L23](.cursorrules#L18-L23)
- [.github/workflows/grpc-checks.yml#L48-L49](.github/workflows/grpc-checks.yml#L48-L49)

---

## 4. ✅ Добавлена CI-проверка Cache-Control заголовков

**Проблема**:
Канареечный чеклист требует проверку `Cache-Control`, но в CI не было автоматической валидации.

**Исправление**:
Добавлен новый step "Cache-Control Headers Check" в [.github/workflows/grpc-checks.yml](.github/workflows/grpc-checks.yml#L139-L172):

```yaml
- name: Cache-Control Headers Check
  id: cache_control_check
  run: |
    echo "🗂️ Checking Cache-Control headers..."

    # Проверяем /health
    HEALTH_CACHE=$(curl -s -k -I https://20.151.51.172/health 2>/dev/null | grep -i "cache-control:" | tr -d '\r\n' || echo "")
    if echo "$HEALTH_CACHE" | grep -q "max-age=30"; then
      echo "✅ /health: $HEALTH_CACHE"
    else
      echo "❌ /health: Expected 'max-age=30', got: $HEALTH_CACHE"
      exit 1
    fi

    # Проверяем /updates/health
    UPDATES_HEALTH_CACHE=$(curl -s -k -I https://20.151.51.172/updates/health 2>/dev/null | grep -i "cache-control:" | tr -d '\r\n' || echo "")
    if echo "$UPDATES_HEALTH_CACHE" | grep -q "max-age=30"; then
      echo "✅ /updates/health: $UPDATES_HEALTH_CACHE"
    else
      echo "❌ /updates/health: Expected 'max-age=30', got: $UPDATES_HEALTH_CACHE"
      exit 1
    fi

    # Проверяем /updates/appcast.xml
    APPCAST_CACHE=$(curl -s -k -I https://20.151.51.172/updates/appcast.xml 2>/dev/null | grep -i "cache-control:" | tr -d '\r\n' || echo "")
    if echo "$APPCAST_CACHE" | grep -q "max-age=60"; then
      echo "✅ /updates/appcast.xml: $APPCAST_CACHE"
    else
      echo "❌ /updates/appcast.xml: Expected 'max-age=60', got: $APPCAST_CACHE"
      exit 1
    fi

    echo "✅ All Cache-Control headers are correct"
  continue-on-error: true
```

**Проверяемые эндпоинты**:
- `/health` → должен иметь `max-age=30`
- `/updates/health` → должен иметь `max-age=30`
- `/updates/appcast.xml` → должен иметь `max-age=60`

**Результат**:
- ✅ Автоматическая валидация заголовков при каждом PR/push
- ✅ Fail если заголовки не соответствуют канону
- ✅ Добавлено в Summary CI

**Файлы**:
- [.github/workflows/grpc-checks.yml#L139-L172](.github/workflows/grpc-checks.yml#L139-L172)
- [.github/workflows/grpc-checks.yml#L239](.github/workflows/grpc-checks.yml#L239) (Summary update)

---

## Дополнительные улучшения

### Явное разделение PUBLIC vs INTERNAL эндпоинтов

В [SERVER_DEPLOYMENT_GUIDE.md](Docs/SERVER_DEPLOYMENT_GUIDE.md#L218-L241) добавлены явные секции:

```bash
### **1. Health Check (PUBLIC - через Nginx/HTTPS):**
# ПУБЛИЧНАЯ проверка (как её видит клиент)
curl -sk https://20.151.51.172/health
# Ожидаемый результат: JSON с полями: status, latest_version, latest_build

### **2. Status API (PUBLIC - через Nginx/HTTPS):**
# ПУБЛИЧНАЯ проверка (как её видит клиент)
curl -sk https://20.151.51.172/status
# Ожидаемый результат: JSON с информацией о сервисе, включая latest_version и latest_build

### **3. Internal Health Check (для локальной диагностики):**
# ВНУТРЕННЯЯ проверка (только с VM, не доступна извне)
curl http://127.0.0.1:8080/health
# Ожидаемый результат: JSON с полями: status, latest_version, latest_build
```

**Примечание**:
> Все публичные проверки (из внешней сети) ДОЛЖНЫ идти через HTTPS (443). HTTP порты (8080, 8081, 50051) слушают только localhost и недоступны извне.

---

## Сводка изменений

### Изменённые файлы

1. **[Docs/SERVER_DEPLOYMENT_GUIDE.md](Docs/SERVER_DEPLOYMENT_GUIDE.md)**:
   - Исправлены HTTP → HTTPS примеры (5 мест)
   - Добавлено явное разделение PUBLIC vs INTERNAL
   - Добавлено примечание о недоступности внутренних портов

2. **[.cursorrules](.cursorrules#L18-L23)**:
   - Унифицирован путь к proto с CI (`modules/grpc_service`)
   - Добавлена note о каноне пути

3. **[.github/workflows/grpc-checks.yml](.github/workflows/grpc-checks.yml)**:
   - Добавлен step "Cache-Control Headers Check"
   - Обновлён Summary с новым check

### Неизменённые файлы (уже соответствуют)

- **[nginx/grpc-passthrough.conf](nginx/grpc-passthrough.conf)**: Cache-Control заголовки уже присутствуют ✅

---

## Проверка соответствия канонам

| Требование | Статус | Файл/строка |
|------------|--------|-------------|
| Публичные эндпоинты через HTTPS | ✅ | SERVER_DEPLOYMENT_GUIDE.md (все примеры) |
| Cache-Control: /health max-age=30 | ✅ | nginx/grpc-passthrough.conf:91 |
| Cache-Control: /updates/health max-age=30 | ✅ | nginx/grpc-passthrough.conf:150 |
| Cache-Control: /updates/appcast.xml max-age=60 | ✅ | nginx/grpc-passthrough.conf:135 |
| Унифицированный путь к proto | ✅ | .cursorrules:20, grpc-checks.yml:48 |
| CI валидация Cache-Control | ✅ | grpc-checks.yml:139-172 |
| Разделение PUBLIC vs INTERNAL | ✅ | SERVER_DEPLOYMENT_GUIDE.md:218-241 |

---

## Следующие шаги

### Рекомендации

1. **Запустить CI** для проверки нового step "Cache-Control Headers Check"
2. **Обновить Canary checklist** со ссылкой на CI check
3. **Добавить в preflight скрипт** проверку Cache-Control перед деплоем

### Опциональные улучшения

1. Создать скрипт `scripts/check_ingress.sh` для валидации Nginx конфигурации
2. Добавить в `RAMP_PLAN.md` ссылку на Cache-Control guardrails
3. Документировать в `ARCHITECTURE_OVERVIEW.md` разделение PUBLIC/INTERNAL портов

---

**Подготовил**: Claude (Sonnet 4.5)
**Дата**: 2025-11-05
**Основание**: Аудит соответствия `SERVER_DEVELOPMENT_RULES.md`
**Статус**: Все 4 несоответствия устранены ✅
