# Nexy Server

**Назначение:** Серверная часть Nexy — голосового ассистента для macOS
**Статус:** ✅ **Production Ready** (100% compliance)
**Версия:** 3.11.0

[![Compliance](https://img.shields.io/badge/Compliance-100%25-brightgreen.svg)](COMPLIANCE_REPORT.md)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen.svg)](Docs/)
[![Production](https://img.shields.io/badge/Production-Ready-brightgreen.svg)]()

---

## 🎯 Соответствие стандартам

**Общее соответствие:** [100% ✅](COMPLIANCE_REPORT.md)

| Компонент | Статус | Compliance |
|-----------|--------|------------|
| Модульная архитектура | ✅ Реализована | 100% |
| Документация | ✅ Полная | 100% |
| Конфигурация | ✅ Создана | 100% |
| ADR процесс | ✅ Настроен | 100% |
| Скрипты валидации | ✅ Присутствуют | 100% |
| gRPC протокол | ✅ Backward compatible | 100% |

**Детальный отчет:** [`COMPLIANCE_REPORT.md`](COMPLIANCE_REPORT.md)

---

## 🧭 Навигационная матрица документации

### 🔴 Критически важные документы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 📋 **Compliance** | [`COMPLIANCE_REPORT.md`](COMPLIANCE_REPORT.md) | **Отчет о соответствии стандартам (100%)** |
| 📋 **Правила** | [`Docs/SERVER_DEVELOPMENT_RULES.md`](Docs/SERVER_DEVELOPMENT_RULES.md) | **Канон правил разработки и релизов (v2.0)** |
| 🧱 **Архитектура** | [`Docs/ARCHITECTURE_OVERVIEW.md`](Docs/ARCHITECTURE_OVERVIEW.md) | Архитектура, FSM, backpressure, graceful shutdown |

### Основные документы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🔄 **Обновления** | [`Docs/GITHUB_UPDATE_SYSTEM.md`](Docs/GITHUB_UPDATE_SYSTEM.md) | Пайплайн деплоя, подписи, GitHub интеграция |
| 🧩 **FSM/States** | [`Docs/STATE_CATALOG.md`](Docs/STATE_CATALOG.md) | Оси состояний, метрики, владельцы |
| ⚙️ **Rollout** | [`Docs/RAMP_PLAN.md`](Docs/RAMP_PLAN.md) | План раскатки трафика, гвардрайлы, этапы |
| 🧪 **Тесты** | [`scripts/grpc_smoke.py`](scripts/grpc_smoke.py) | Smoke-тесты, контракт-тесты, chaos-тесты |

### Специализированные документы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 📦 **Backpressure** | [`Docs/BACKPRESSURE_README.md`](Docs/BACKPRESSURE_README.md) | Политика лимитов, конфиг, troubleshooting |
| 🔍 **CI Checks** | [`Docs/CI_GRPC_CHECKS.md`](Docs/CI_GRPC_CHECKS.md) | CI-workflow, проверки, валидация размеров |
| 📝 **ADR** | [`Docs/ADR_TEMPLATE.md`](Docs/ADR_TEMPLATE.md) | Шаблон решений (ADR) с полями для осей/guards |
| ✅ **Canary** | [`Docs/CANARY_CHECKLIST.md`](Docs/CANARY_CHECKLIST.md) | Чеклист для canary выкатки |
| 🚀 **Beta Gate** | [`Docs/BETA_GATE_CHECKLIST.md`](Docs/BETA_GATE_CHECKLIST.md) | Чеклист для beta gate |
| 📊 **gRPC Protocol** | [`Docs/GRPC_PROTOCOL_AUDIT.md`](Docs/GRPC_PROTOCOL_AUDIT.md) | Аудит протокола, контракт-таблицы |

### ADR (Architecture Decision Records)

| **ADR** | **Тема** | **Статус** |
|---------|----------|-----------|
| [`ADR-001`](Docs/decisions/ADR-001-modular-architecture.md) | Модульная архитектура с ModuleCoordinator | ✅ Accepted |

### Критические фиксы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🔴 **Версионирование** | [`Docs/VERSION_FORMAT_CRITICAL_FIX.md`](Docs/VERSION_FORMAT_CRITICAL_FIX.md) | Канон форматов версий (строки) |
| 🔧 **Update Fixes** | [`Docs/UPDATE_SYSTEM_FIXES.md`](Docs/UPDATE_SYSTEM_FIXES.md) | Фиксы системы обновлений, синхронизация размеров |

---

## 🚀 Быстрый старт

### Первоначальная настройка

1. **Создайте config.env:**
   ```bash
   cp config.env.example config.env
   nano config.env  # Заполните API ключи
   ```

   **Обязательные переменные:**
   - `GEMINI_API_KEY` - ключ Gemini API
   - `AZURE_SPEECH_KEY` - ключ Azure Speech
   - `DB_PASSWORD` - пароль PostgreSQL (если используется)

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

### Запуск сервера

```bash
# Загрузка переменных окружения
source config.env

# Запуск сервера
python main.py
```

**Ожидаемый вывод:**
- ✅ gRPC сервер запущен на порту 50051
- ✅ HTTP health/status сервер на порту 8080
- ✅ Update сервер на порту 8081
- ✅ Graceful shutdown handlers установлены

### Префлайт-проверки

```bash
# Общая проверка
./scripts/preflight_check.sh 20.151.51.172 443

# Проверка интерсепторов
python scripts/test_interceptor_errors.py 20.151.51.172 443

# Проверка backpressure
python scripts/test_backpressure.py 20.151.51.172 443
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

- `config/unified_config_example.yaml` — пример конфигурации
- `config.env.example` — пример переменных окружения
- `config/unified_config.py` — загрузчик конфигурации

### Backpressure конфигурация

```yaml
backpressure:
  max_concurrent_streams: 50      # Максимум одновременно открытых StreamAudio
  idle_timeout_seconds: 300        # Таймаут для неактивных стримов (5 минут)
  max_message_rate_per_second: 10 # Максимум сообщений в секунду на стрим
  grace_period_seconds: 30         # Период ожидания перед принудительным закрытием
```

**Окружения:** dev/stage/prod (автоматический выбор по `NEXY_ENV`)

---

## 🧪 Тестирование

### Smoke-тесты

```bash
# gRPC smoke test
python scripts/grpc_smoke.py 20.151.51.172 443

# Health check
python scripts/check_grpc_health.py 20.151.51.172 443

# Contract tests
python scripts/grpc_contract_tests.py 20.151.51.172 443

# Chaos test
python scripts/chaos_smoke.py 20.151.51.172 443
```

### Валидация обновлений

```bash
# Проверка версий и размеров
bash scripts/validate_updates.sh 20.151.51.172 443
```

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

