# Nexy Server

**Назначение:** Серверная часть Nexy — голосового ассистента для macOS  
**Статус:** ✅ Готов к canary выкатке (PR-7 завершён)

---

## 🧭 Навигационная матрица документации

### Основные документы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🧱 **Архитектура** | `Docs/ARCHITECTURE_OVERVIEW.md` | Архитектура, FSM, таблицы исключений, backpressure, graceful shutdown |
| 🔄 **Обновления** | `Docs/GITHUB_UPDATE_SYSTEM.md` | Пайплайн деплоя, подписи, GitHub интеграция |
| 🧩 **FSM/States** | `Docs/STATE_CATALOG.md` | Оси состояний, метрики, владельцы |
| ⚙️ **Rollout** | `Docs/RAMP_PLAN.md` | План раскатки трафика, гвардрайлы, этапы |
| 📋 **Правила** | `Docs/SERVER_DEVELOPMENT_RULES.md` | Единая точка входа — правила разработки и релизов |
| 🧪 **Тесты** | `scripts/grpc_smoke.py` | Smoke-тесты, контракт-тесты, chaos-тесты |

### Специализированные документы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 📦 **Backpressure** | `Docs/BACKPRESSURE_README.md` | Политика лимитов, конфиг, troubleshooting |
| 🔍 **CI Checks** | `Docs/CI_GRPC_CHECKS.md` | CI-workflow, проверки, валидация размеров |
| 📝 **ADR** | `Docs/ADR_TEMPLATE.md` | Шаблон решений (ADR) с полями для осей/guards |
| ✅ **Canary** | `Docs/CANARY_CHECKLIST.md` | Чеклист для canary выкатки |
| 🚀 **Beta Gate** | `Docs/BETA_GATE_CHECKLIST.md` | Чеклист для beta gate |
| 📊 **gRPC Protocol** | `Docs/GRPC_PROTOCOL_AUDIT.md` | Аудит протокола, контракт-таблицы |

### Критические фиксы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🔴 **Версионирование** | `Docs/VERSION_FORMAT_CRITICAL_FIX.md` | Канон форматов версий (строки) |
| 🔧 **Update Fixes** | `Docs/UPDATE_SYSTEM_FIXES.md` | Фиксы системы обновлений, синхронизация размеров |

---

## 🚀 Быстрый старт

### Запуск сервера

```bash
# Активируем виртуальное окружение (если требуется)
source venv/bin/activate

# Загружаем переменные окружения
source server/config.env

# Запускаем сервер gRPC + HTTP + Update
python server/main.py
```

### Префлайт-проверки

```bash
# Общая проверка
./scripts/preflight_check.sh nexy-server.canadacentral.cloudapp.azure.com 443

# Проверка интерсепторов
python scripts/test_interceptor_errors.py nexy-server.canadacentral.cloudapp.azure.com 443

# Проверка backpressure
python scripts/test_backpressure.py nexy-server.canadacentral.cloudapp.azure.com 443
```

### Мониторинг

```bash
# Проверка гвардрайлов
./scripts/check_ramp_guardrails.sh server.log 100

# JQ-выражения для метрик
./scripts/monitoring_jq.sh server.log

# Настройка алёртов
./scripts/setup_alerts.sh server.log
```

### Локальное тестирование

```bash
# Юнит/интеграционные тесты координатора и адаптеров
pytest server/tests/test_pr2_1_coordinator.py

# Smoke-тест gRPC (локальный инстанс)
python server/scripts/grpc_smoke.py localhost 50051

# Smoke-тест продового инстанса
python scripts/grpc_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443
```

---

## 📚 Структура документации

```
Docs/
├── SERVER_DEVELOPMENT_RULES.md      # Единая точка входа — правила разработки
├── ARCHITECTURE_OVERVIEW.md         # Архитектура, FSM, таблицы исключений
├── STATE_CATALOG.md                 # Оси состояний и метрики
├── BACKPRESSURE_README.md           # Политика лимитов и конфиг
├── RAMP_PLAN.md                     # План раскатки трафика и гвардрайлы
├── CI_GRPC_CHECKS.md                # CI-workflow и проверки
├── VERSION_FORMAT_CRITICAL_FIX.md   # Канон форматов версий
├── UPDATE_SYSTEM_FIXES.md           # Фиксы системы обновлений
├── GITHUB_UPDATE_SYSTEM.md          # Пайплайн деплоя и подписи
├── ADR_TEMPLATE.md                  # Шаблон решений (ADR)
├── CANARY_CHECKLIST.md              # Чеклист для canary выкатки
├── BETA_GATE_CHECKLIST.md           # Чеклист для beta gate
└── GRPC_PROTOCOL_AUDIT.md           # Аудит протокола, контракт-таблицы
```

---

## ⚙️ Конфигурация

### Основные файлы

- `config/unified_config.yaml` — конфигурация
- `config.env.example` — пример переменных окружения
- `config/unified_config.py` — загрузчик конфигурации

### Сетевые биндинги

- `NEXY_ENV` управляет значениями по умолчанию для `grpc.host`, `http.host` и `update.host`: в `dev` слушаем `0.0.0.0` для локальных тестов, в `stage/prod` автоматически переключаемся на `127.0.0.1`, а наружный трафик идёт через Nginx.
- Значение `auto` в `GRPC_HOST`/`HTTP_HOST`/`UPDATE_HOST` означает «использовать дефолт для текущего окружения».
- Публичная точка входа продакшена — `https://nexy-server.canadacentral.cloudapp.azure.com` (443/HTTP2). Внутренние сервисы (`50051`, `8080`, `8081`) не слушают внешние интерфейсы в проде.

### Backpressure конфигурация

```yaml
backpressure:
  max_concurrent_streams: 50      # Максимум одновременно открытых StreamAudio
  idle_timeout_seconds: 300        # Таймаут для неактивных стримов (5 минут)
  max_message_rate_per_second: 20 # Максимум сообщений в секунду на стрим (увеличено для аудио)
  grace_period_seconds: 30         # Период ожидания перед принудительным закрытием
```

**Окружения:** dev/stage/prod (автоматический выбор по `NEXY_ENV`)

---

## 🧩 Архитектура модулей (универсальная схема)

- Вся бизнес-логика реализует `UniversalModuleInterface`. Существующие процессоры обернуты адаптерами (`modules/*/adapter.py`), которые предоставляют единый контракт `initialize/process/cleanup/status`.
- gRPC слой использует `ModuleCoordinator` + `ModuleFactory` (см. `server/integrations/service_integrations`). `GrpcServiceManager` не импортирует модули напрямую, а запрашивает capability через координатор.
- Workflow-интеграции (`integrations/workflow_integrations/*`) взаимодействуют с capability через `module.process()` и не зависят от внутренних классов модулей. Это документировано в `Docs/ARCHITECTURE_OVERVIEW.md`.
- gRPC interceptor (`modules/grpc_service/core/grpc_interceptor.py`) реализует единый контроль ошибок/метрик. Он совместим с grpcio 1.76.0: handler оборачивается через `_replace`, сериализаторы сохраняются автоматически.
- UpdateManager также реализует `UniversalModuleInterface` и управляется из `main.py` вместе с gRPC и HTTP health-слоем.

Дополнительные детали — в `server/Docs/ARCHITECTURE_OVERVIEW.md` и `server/Docs/SERVER_DEVELOPMENT_RULES.md`.

---

## 🧪 Тестирование

### Smoke-тесты

```bash
# gRPC smoke test
python scripts/grpc_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443

# Health check
python scripts/check_grpc_health.py nexy-server.canadacentral.cloudapp.azure.com 443

# Contract tests
python scripts/grpc_contract_tests.py nexy-server.canadacentral.cloudapp.azure.com 443

# Chaos test
python scripts/chaos_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443
```

### Валидация обновлений

```bash
# Проверка версий и размеров
bash scripts/validate_updates.sh nexy-server.canadacentral.cloudapp.azure.com 443
```

### Финальный smoke перед релизом

`SMOKE_TEST_QUICK_START.md` и `READY_FOR_SMOKE_TEST.md` содержат актуальный чеклист:

1. Поднять сервер (`python server/main.py` в активированном venv).
2. Выполнить `python server/scripts/grpc_smoke.py <host> <port>`.
3. Проверить `/health`, `/status`, `/appcast.xml`, а также Update Server (`http://127.0.0.1:8081`).

---

## 🔧 Разработка

### Правила разработки

См. `Docs/SERVER_DEVELOPMENT_RULES.md` для:
- Гейты перед мерджем (SIMPLE/Impact)
- Правила версионирования
- gRPC Compatibility Policy
- Rollout Policy
- Runbook отката

### ADR (Architecture Decision Records)

При изменении модульной логики, FSM, guards или осей:
1. Создать ADR по шаблону `Docs/ADR_TEMPLATE.md`
2. Заполнить раздел "Affected Axes / Guards"
3. Обновить `Docs/STATE_CATALOG.md` и `Docs/ARCHITECTURE_OVERVIEW.md`

---

## 📊 Мониторинг

### Метрики

- p95 latency по RPC методам
- error-rate по методам
- decision_rate (start/abort/retry/degrade/complete/error)

### Алёрты

- p95 > 1000ms (warn), >1500ms (page)
- error-rate > 5% (warn), >10% (page)
- рост unavailable/retry/abort ×2 от медианы за 24ч

**Настройка:** см. `scripts/setup_alerts.sh`

---

## 🚀 Canary выкатка

### План раскатки

1. **Этап A — 1%** (30–60 мин)
2. **Этап B — 25%** (2–4 часа)
3. **Этап C — 50%** (полдня)
4. **Этап D — 100%** (следующий день)

**Детали:** см. `Docs/RAMP_PLAN.md` и `Docs/CANARY_CHECKLIST.md`

---

## 🔗 Быстрые ссылки

- **Правила разработки:** `Docs/SERVER_DEVELOPMENT_RULES.md`
- **Архитектура:** `Docs/ARCHITECTURE_OVERVIEW.md`
- **Обновления:** `Docs/GITHUB_UPDATE_SYSTEM.md`
- **FSM/States:** `Docs/STATE_CATALOG.md`
- **Rollout:** `Docs/RAMP_PLAN.md`
- **Backpressure:** `Docs/BACKPRESSURE_README.md`
- **CI Checks:** `Docs/CI_GRPC_CHECKS.md`
- **Canary:** `Docs/CANARY_CHECKLIST.md`

---

**Последнее обновление:** 3 октября 2025  
**Статус:** ✅ Готов к canary выкатке
