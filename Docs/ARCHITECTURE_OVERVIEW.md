# 🧭 Nexy Server — Архитектурный обзор

Документ — канон для серверной части Nexy. Он закрепляет владельцев архитектурных осей, структуру каталогов, контракты модулей и обязательные проверки перед релизом. Любые изменения в этих разделах должны обновлять данный документ вместе с профильными канонами.

Исторические планы и отчеты перенесены в `Docs/_archive` и не используются как источник истины.

**Flow Interaction Spec (канон взаимодействий):** `Docs/FLOW_INTERACTION_SPEC.md`

---

## 0. Release/Deploy Boundaries

- `Seregawpn/Nexy` — source code и deploy pipeline.
- `Seregawpn/Nexy_production/releases` — клиентские артефакты (`Nexy.dmg`, `Nexy.pkg`) и update-канал.

Каноны:
- Deploy: `Docs/SERVER_DEPLOYMENT_GUIDE.md`
- Client release: `Docs/RELEASE_AND_UPDATE_GUIDE.md`
- Incident runbook: `Docs/DEPLOY_INCIDENT_RUNBOOK.md`

Запрещено смешивать эти пайплайны в одной инструкции.

---

## 1. Оси, владельцы и источники истины

| Ось | Canon | Ответственный |
| --- | --- | --- |
| gRPC и протокол | `Docs/GRPC_PROTOCOL_AUDIT.md` | @grpc-core |
| Обновления и AppCast | `Docs/RELEASE_AND_UPDATE_GUIDE.md` | @release-ops |
| Backpressure и лимиты | `Docs/BACKPRESSURE_README.md` | @reliability |
| Health/наблюдаемость | `Docs/CI_GRPC_CHECKS.md` | @sre-duty |
| Защита данных и DR | `Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md` | @server-platform |
| Конфигурация | `config/unified_config.py` + `config/unified_config.yaml` | @server-platform |
| State Catalog | `Docs/STATE_CATALOG.md` | Tech Lead клиента |
| Flow Interaction Spec | `Docs/FLOW_INTERACTION_SPEC.md` | Tech Lead клиента |

- Один документ-канон на ось, один владелец. Ссылки в PR должны указывать на обновление соответствующего канона.
- `Docs/ADR_TEMPLATE.md` используется для фиксации изменений модулей/матриц/протокола (микро-ADR ≥7 строк).

---

## 2. Структура и границы слоёв

```
server/server/
├── main.py                      # Точка входа сервера
├── modules/                     # Чистая бизнес-логика
│   ├── grpc_service/            # gRPC сервер, интерсепторы, streaming.proto
│   ├── audio_generation/
│   ├── text_processing/
│   ├── session_management/
│   ├── memory_management/
│   ├── interrupt_handling/
│   ├── text_filtering/
│   ├── database/                # Управление базой данных
│   └── update/                  # Система обновлений
├── integrations/                # Обвязка и orchestration
│   ├── core/
│   ├── service_integrations/
│   └── workflow_integrations/
├── monitoring/                  # Метрики и health-проверки
│   └── grpc_monitor.py          # Мониторинг gRPC запросов
├── scripts/                     # smoke/contract/гвардрайлы
├── tests/                       # unit/contract сценарии
├── config/                      # unified_config.yaml (единый источник истины)
├── utils/                       # Утилиты (логирование, метрики, текст)
├── updates/                     # Артефакты обновлений (manifests, downloads, keys)
├── nginx/                       # Конфигурация Nginx для ingress
└── Docs/                        # Канон документов
```

- Модули ≠ интеграции ≠ workflow: бизнес-логика живёт в `server/server/modules/*`. Оркестрация и сценарии находятся в интеграциях и workflow-интеграциях.
- Прямые импорты между модулями запрещены. Доступ идёт через `server/server/integrations/service_integrations/module_coordinator.py`.
- Каждый модуль реализует `UniversalModuleInterface`. 
  - **Прямая реализация:** `text_processing` использует `module.py` (напрямую реализует интерфейс)
  - **Адаптеры:** Остальные модули используют `adapter.py` (обёртка над существующими процессорами), предоставляющие единый `initialize/process/cleanup/status`
- gRPC слой не импортирует интеграции напрямую; связь через `GrpcServiceManager` → `ModuleCoordinator`, а создание модулей выполняет `ModuleFactory`.
- Workflow-интеграции (`streaming`, `memory`, `interrupt`) работают с capability через `module.process()`. Запрос внутренних `get_processor()` допускается только как временный workaround и фиксируется в ADR + `Docs/SERVER_DEVELOPMENT_RULES.md`.
- **Опциональные модули:** `database`, `audio_generation`, `text_filtering`, `interrupt_handling` - сервер может работать без них при ошибке инициализации (graceful degradation).
- Все порты/лимиты/таймауты читаются из `unified_config`; в коде отсутствуют «магические числа».

---

## 2.1 Database Durability & Protection (обязательный канон)

- **Source of Truth по DB policy:** `Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md` + `Docs/DATABASE_SETUP_GUIDE.md`.
- **Least-privilege для app-role:** `SELECT/INSERT/UPDATE`; запрещены `DELETE/TRUNCATE/CREATE` на уровне роли.
- **Hard-delete guard:** trigger-защита от физического удаления критичных записей (`users/sessions/commands/llm_answers/token_usage` и связанные таблицы).
- **Кодовая политика:** модуль `database` не выполняет `delete` операции в runtime.
- **Release/Deploy gate:** перед production-релизом обязателен backup; restore drill должен быть не старше 7 дней.
- **После restore:** обязательно повторно применить `scripts/harden_database_protection.sh`.

---

## 2.2 Как добавить новый функционал (Server Route)

**Единый источник истины**: `Docs/SERVER_DEVELOPMENT_RULES.md` (серверный маршрут).  
Здесь фиксируем только краткий путь:

1. **Module** → `server/server/modules/<feature>/`
   - Если модуль новый: создать `module.py` с классом, реализующим `UniversalModuleInterface`
   - Если обёртка над существующим процессором: создать `adapter.py` с адаптером
2. **ModuleFactory** → регистрация capability в `_MODULE_REGISTRY` (`integrations/core/module_factory.py`)
   - Формат: `'capability': 'modules.<feature>.module:ClassName'` или `'modules.<feature>.adapter:AdapterName'`
3. **ModuleCoordinator** → инициализация/доступ (автоматически через `GrpcServiceManager`)
4. **Config/Flags** → `server/server/config/unified_config.yaml` + `Docs/FEATURE_FLAGS.md`
5. **gRPC Contract** → `Docs/GRPC_PROTOCOL_AUDIT.md` (если требуется)

---

## 2.3 Принципы устойчивости стриминга

- **Request-scoped state**: состояние стрима не хранится на уровне экземпляра workflow.
- **Single-flight по session_id**: один активный StreamAudio на `session_id`, повторные отклоняются.
- **Source of Truth**: `session_id` и gRPC статусы формируются только в `grpc_server.py`.
- **Backpressure централизован**: acquire/check/release в `GrpcServiceIntegration`.
- **Политика ошибок**: ошибка до начала стрима → gRPC статус + `error_message`; после частичных данных → terminal `error_message` без изменения gRPC статуса.
- **Streaming semantics**: raw LLM stream приходит из `LangChainGeminiProvider.astream(...)`, но внешний semantic emit принадлежит только `StreamingWorkflowIntegration`; ранний `text_response` допустим как request-scoped preview, при этом `audio_chunk` остаётся sentence-based.

---

## 2.4 Session Management и Concurrency (обновлено 21 января 2026)

### Централизованное управление сессиями

Вся информация о сессиях хранится в единственном источнике истины:

| Компонент | Ответственность |
|-----------|-----------------|
| `SessionRegistry` | Единственный владелец session state (thread-safe с `threading.RLock`) |
| `SessionTracker` | Делегирует всё в `SessionRegistry`, управляет lifecycle |
| `InterruptManager` | Получает session data из `SessionRegistry`, не хранит копии |
| `InterruptWorkflowIntegration` | Использует `SessionRegistry` для session queries |

**Паттерн:** Все операции с сессиями идут через `SessionRegistry.register_session()`, `get_session()`, `interrupt_session()`, `unregister_session()`.

### Централизованные флаги прерывания

| Компонент | Роль |
|-----------|------|
| `GlobalFlagProvider` | Единственный владелец `global_interrupt_flag` |
| `InterruptManager` | Делегирует все flag-операции в `GlobalFlagProvider` |

**Паттерн:** `InterruptManager.should_interrupt(hardware_id)` запрашивает `GlobalFlagProvider.check_interrupt_flag()`.

### Thread-Safety и Lock Usage

| Компонент | Lock Type | Защищаемый ресурс |
|-----------|-----------|-------------------|
| `SessionRegistry` | `threading.RLock` | `_active_sessions` dict |
| `HardwareIDProvider` | `asyncio.Lock` | `received_ids` set |
| `StreamingWorkflowIntegration` | `asyncio.Lock` | `_hardware_id_to_sessions` (in-flight tracking) |
| `BackpressureManager` | `asyncio.Lock` | rate/stream counters |
| `SubscriptionModule` | `threading.Lock` | `_cache` TTL cache |
| `MemoryWorkflowIntegration` | `asyncio.Lock` | `memory_cache`, `_memory_tasks` |

**Правило:** Любой shared mutable state, доступный из нескольких async задач, должен быть защищён lock.

---

## 2.5 Current Runtime Owners and Helper-Only Layers

Ниже перечислены текущие owner-модули серверного runtime. Helper-файлы `*_bridge.py` допустимы только как internal decomposition и не являются вторым owner-path.

- `StreamingWorkflowIntegration`
  - Owner: semantic streaming emit (`text_chunk`, `audio_chunk`, terminal sequencing).
  - Runtime rule: raw LLM stream приходит из `LangChainGeminiProvider.astream(...)`, но внешний semantic emit принадлежит только workflow.
  - Helper-only split: ранний text preview и sentence-based audio остаются внутри одного owner-path.

- `GrpcServiceIntegration`
  - Owner: service-layer fallback policy, wrapper orchestration, backpressure acquire/release.
  - Runtime rule: direct fallback допустим только до первого yield wrapper-path; после partial data workflow restart запрещён.

- `MemoryWorkflowIntegration`
  - Owner: cache/task state, stale fallback, refresh scheduling, memory fetch/update orchestration.
  - Helper-only split: `memory_cache_bridge.py` — cache-policy helper; `_cache_lock`, `_memory_tasks`, `_refresh_tasks` остаются у owner.

- `LangChainGeminiProvider`
  - Owner: actual LLM execution lifecycle, streaming/non-streaming model call, retry/provider state.
  - Helper-only split: `langchain_gemini_bridge.py` — request/prompt shaping, runtime input normalization, usage recording.

- `AssistantResponseParser`
  - Owner: normalized assistant output contract (`ParsedResponse`, `command_payload`, text fallback).
  - Helper-only split: `assistant_response_parser_bridge.py` — markdown/json cleanup, action validation, command payload shaping.

- `AudioProcessor`
  - Owner: TTS orchestration, processor readiness, provider lifecycle.
  - Helper-only split: `audio_processor_bridge.py` — readiness/status/summary shaping, config/provider voice-settings propagation.

- `EdgeTTSProvider`
  - Owner: low-level TTS streaming path, ffmpeg/pydub conversion lifecycle, retry execution.
  - Helper-only split: `edge_tts_provider_bridge.py` — conversion mode, retry policy, byte chunk splitting, status/audio-info shaping.


---

## 3. Ответы ассистента и MCP команды

### 3.1 Формат ответа ассистента

Сервер поддерживает два типа ответов от ассистента (LLM):

**Обычный текстовый ответ:**
- Только поле `text` (строка для озвучки)
- Поведение: текст идёт на генерацию речи (TTS) и стриминг клиенту

**Action-ответ (комбинированный):**
```json
{
  "session_id": "<uuid>",
  "command": "open_app",
  "args": {
    "app_name": "Telegram"
  },
  "text": "Открываю Telegram, дайте знать, если понадобится что-то ещё."
}
```

- `text` — идёт на генерацию речи/стриминг (ожидается озвучка для пользователя)
- JSON (`command` + `args` + `session_id`) — без модификаций доходит до клиента, который публикует событие `mcp.command_request`
- При отсутствии `command` поведение совпадает с текущим: текст/аудио идут на клиента, MCP событие не формируется

**Парсинг и валидация:**
- Парсер: `integrations/core/assistant_response_parser.py`
- Толерантность к "кривым" данным: если пришёл обычный текст без JSON — возвращается `text_response`, `command_payload=None`
- Если JSON, но отсутствует `text` — логируется предупреждение, подставляется пустая строка (чтобы TTS не падал)
- Проверка обязательных полей (`session_id`, `app_name` для `open_app`) и генерация ошибок/логов при их отсутствии

**Передача через gRPC (Фаза 3):**
- `command_payload` отправляется клиенту как `text_chunk` с префиксом `__MCP__`
- Формат: `__MCP__{"event": "mcp.command_request", "payload": {...}}`
- Клиент должен отслеживать чанки с префиксом `__MCP__` и публиковать JSON в EventBus как событие `mcp.command_request`
- Текст и аудио продолжают передаваться параллельно в обычном формате
- Префикс выбран для backward compatibility (не требует изменения proto)

**Фича-флаг:**
- `features.forward_assistant_actions` — включает передачу JSON на клиента (по умолчанию `false`)
- Kill-switch: `kill_switches.disable_forward_assistant_actions` — немедленное отключение без релиза

**Документация:**
- Канон: `Docs/SERVER_DEVELOPMENT_RULES.md` (итоговый summary)
- Исторический план: `Docs/_archive/MCP_COMMAND_INTEGRATION_PLAN.md` (для справки, не канон)
- Решения об action принимает ассистент (LLM), сервер только транслирует

### 3.2 Browser Automation (`browser_use`)

Сервер поддерживает browser routing через модуль `browser_use` (Feature ID: F-2025-015).

**Возможности:**
- Принимать `browser_use` команду от LLM
- Форвардить browser task на клиент
- Держать единый routing gate для browser capability на сервере

**Конфигурация (`config.env` / shared runtime owner):**

| Переменная | По умолчанию | Описание |
|------------|--------------|----------|
| `BROWSER_USE_ENABLED` | `true` | Standalone fallback; в монорепо manual owner живёт в `client/config/unified_config.yaml -> features.browser_use/browser` |

**Runtime правило:**
Сервер не запускает браузер локально. Реальное browser execution, install lifecycle и model/runtime config принадлежат клиенту.

**Команды:**
- `browser_use` — Передать веб-задачу клиенту
- `close_browser` — Передать клиенту команду закрытия браузера

### 3.3 Messages Integration (`messages`) (Feature ID: F-2025-016)

Сервер поддерживает MCP интеграцию с Apple Messages для чтения и отправки сообщений через голосовые команды.

**Возможности:**
- Чтение входящих сообщений из iMessage/SMS
- Отправка сообщений контактам
- Поиск контактов в адресной книге

**Команды (выполняются на клиенте):**

| Команда | Описание |
|---------|----------|
| `read_messages` | Прочитать последние сообщения от контакта |
| `send_message` | Отправить сообщение контакту |
| `find_contact` | Найти контакт по имени |

**Требования:**
- Full Disk Access для доступа к `~/Library/Messages/chat.db`
- Права на Automation (Messages.app) для отправки

**Голосовая обратная связь:**
После успешной отправки клиент озвучивает: "Message to {recipient}: '{content}'. Sent successfully."

### 3.4 Token Usage Tracking (F-2025-019)

Сервер централизованно собирает статистику использования токенов LLM от всех источников для биллинга и мониторинга.

**Архитектура:**
- **Source of Truth**: Таблица `token_usage` в PostgreSQL.
- **Service**: `TokenUsageTracker` — единая точка входа для записи статистики.
- **Repository**: `TokenUsageRepository` — абстракция над БД.

**Источники данных:**
1. **Main LLM**: `LangChainGeminiProvider` (через `usage_metadata` ответа).
2. **Memory Analyzer**: `MemoryAnalyzer` (анализ памяти в фоне).
3. **Browser Agent**: Клиент отправляет статистику через gRPC `ReportUsage` после выполнения задач.

Канонический контракт памяти (short/medium/long, async flow, DB/cache, anti-race):
- `Docs/MEMORY_REQUIREMENTS.md`

**Отчетность:**
- Скрипт `../scripts/report_token_costs.py` генерирует отчет по расходам пользователей.

---

## 4. gRPC ось

### 4.1 Протокол и генерация

- Канонический proto-файл: `modules/grpc_service/streaming.proto` (не дублировать в других каталогах).
- Регенерация Python-стабов:
  ```bash
  cd server/server/modules/grpc_service
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
  ```
- Любое breaking-изменение → новый `StreamingServiceV2` + feature-flag + 2 релиза параллельной поддержки (описано в `Docs/GRPC_PROTOCOL_AUDIT.md`).

### 4.2 Стабильность API

- RPC: `StreamAudio` (bidirectional stream), `InterruptSession` (unary-unary).
- Контракт совместимости фиксируется в `Docs/GRPC_PROTOCOL_AUDIT.md`; CI (`Docs/CI_GRPC_CHECKS.md`) блокирует регресс по регенерации proto и smoke-тестам.
- Любое добавление поля требует обновления таблицы совместимости в каноне.

### 4.3 Error Taxonomy

| error_type | gRPC code | Клиентское действие |
| --- | --- | --- |
| `timeout` | `DEADLINE_EXCEEDED` | Retry with backoff |
| `unavailable` | `UNAVAILABLE` | Retry exponential |
| `cancelled_by_user` | `CANCELLED` | Stop UX, no retry |
| `stream_limit_exceeded` | `RESOURCE_EXHAUSTED` | Backoff 60s → retry |
| `rate_limit_exceeded` | `RESOURCE_EXHAUSTED` | Throttle locally → retry |
| `validation_failed` | `INVALID_ARGUMENT` | Fix payload, no retry |
| `internal` | `INTERNAL` | Surface error, retry once |

### 4.4 LoggingInterceptor

- Файл: `modules/grpc_service/core/grpc_interceptor.py`. Оборачивает callables через `_replace`, не модифицируя сериализаторы (`rpc_method_handler` — namedtuple).
- В логах обязателен контекст: `scope=grpc`, `method=/streaming.StreamingService/...`, `decision=start|abort|complete`, `ctx` со служебными полями.
- Ошибки классифицируются через `ErrorCodeMapper`; transient ошибки фиксируются как `decision=error`, `error_classified=transient`.
- Любой новый RPC обязан регистрироваться через LoggingInterceptor. В обходных сценариях требуется ADR + обновление `Docs/CI_GRPC_CHECKS.md`.

Таблица дублируется комментариями в `server/server/modules/grpc_service/core/grpc_interceptor.py`. Любое изменение — синхронное обновление двух мест.

---

## 5. Конфигурация и флаги

Единый источник — `server/server/config/unified_config.py`. Значения для окружений перечислены в `server/server/config/unified_config.yaml`.

| Ключ | Тип | dev | stage | prod | Env override |
| --- | --- | --- | --- | --- | --- |
| `grpc.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `GRPC_HOST` (`auto` = по `NEXY_ENV`) |
| `grpc.port` | int | 50051 | 50051 | 50051 | `GRPC_PORT` |
| `grpc.max_workers` | int | 10 | — (inherit prod) | 100 | `MAX_WORKERS` |
| `http.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `HTTP_HOST` (`auto` = по `NEXY_ENV`) |
| `http.port` | int | 8080 | 8080 | 8080 | `HTTP_PORT` |
| `backpressure.max_concurrent_streams` | int | 10 | 25 | 50 | `BACKPRESSURE_MAX_STREAMS` |
| `backpressure.max_message_rate_per_second` | int | 5 | 8 | 0 | `BACKPRESSURE_MAX_RATE` (0 = отключено) |
| `backpressure.idle_timeout_seconds` | int | 60 | 180 | 900 | `BACKPRESSURE_IDLE_TIMEOUT` (15 минут для длинных TTS) |
| `features.use_module_coordinator` | bool | true | true | true | `USE_MODULE_COORDINATOR` |
| `kill_switches.disable_module_coordinator` | bool | false | false | false | `NEXY_KS_DISABLE_MODULE_COORDINATOR` |
| `update.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `UPDATE_HOST` (`auto` = по `NEXY_ENV`) |
| `update.port` | int | 8081 | 8081 | 8081 | `UPDATE_PORT` |

> Stage наследует prod значения, если не указано иное. Значения по умолчанию для `grpc.host`/`http.host`/`update.host` определяются `NEXY_ENV`: dev → `0.0.0.0` для локальных тестов, stage/prod → `127.0.0.1` (все запросы идут через Nginx на 443). Значение `auto` в `config.env` означает «использовать дефолт по окружению». Все overrides проходят через unified_config + env, прямых setdefault в коде нет.

Backpressure лимиты, error-коды и рекомендации по отладке — в `Docs/BACKPRESSURE_README.md`.

### 5.1 Feature Flags Architecture (Server-Side)

Сервер агрессивно использует Feature Flags для защиты от галлюцинаций LLM и экономии ресурсов.

**1. Modular Prompt Engineering:**
- `unified_config.py` собирает системный промпт динамически.
- Если shared owner `features.messages=false` (или standalone fallback `MESSAGES_ENABLED=false`) → секция "Messages" вырезается из промпта.
- Если shared owner `features.payment=false` (или standalone fallback `SUBSCRIPTION_ENABLED=false`) → секция "Subscriptions" вырезается.

**2. Command Validator:**
- `ResponseValidator` проверяет каждую команду от LLM.
- `allowed_commands` формируются динамически на основе `FeaturesConfig`.
- Попытка выполнить `read_messages` при отключенном флаге вызывает `ValidationError` (защита от "взлома" промпта).

---

## 6. Наблюдаемость и fail-fast

- **Decision-логи**: формат `ts=<iso> level=<lvl> scope=<module> method=<rpc> decision=<event> ctx=<json> dur_ms=<int>`. Логи без `decision` считаются нарушением канона.
- **Структурированное логирование**:
  - Единый формат для всех модулей
  - Автоматическая маскировка секретов (API ключи, пароли, токены)
  - Реализация: `utils/logging_formatter.py`
- **Метрики (агрегация каждые 60s)**:
  - `p95_latency_ms{rpc}` — 95-й перцентиль задержки по RPC методам
  - `error_rate{rpc}` — частота ошибок по методам
  - `backpressure_refusal_rate` — частота отказов из-за backpressure
  - `decision_rate{type}` — частота решений (start/abort/retry/degrade/complete)
  - Реализация: `utils/metrics_collector.py`
  - Периодическое логирование каждые 60 секунд
  - Итоговые метрики при graceful shutdown
- **Гвардрайлы CI** (`Docs/CI_GRPC_CHECKS.md`):
  - regen proto → diff запретов
  - smoke-тесты (`python scripts/grpc_smoke.py --host 127.0.0.1 --port 50051`)
  - health/порт/версия (`python scripts/check_grpc_health.py`)
  - Cache-Control заголовки (`curl -I https://<host>/updates/appcast.xml | grep 'Cache-Control'`)
  - validate release size (`scripts/validate_updates.sh`)

---

## 7. Надёжность, ingress и shutdown

- **Ingress**: один публичный вход — HTTPS:443 через Nginx (`/etc/nginx/sites-available/nexy`). Внутренние адреса `127.0.0.1:50051`, `127.0.0.1:8080`, `127.0.0.1:8081` слушают только на localhost и недоступны извне.
- **Архитектура доступа:**
  - Публичная точка входа prod: `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com` (IP закреплён за Nexy Server в Azure)
  - Значение `NEXY_ENV=prod` или `stage` автоматически переводит все сервисы в режим `127.0.0.1`. Для локальных запусков (`NEXY_ENV=dev`) хосты по умолчанию `0.0.0.0`.
  - Внешний доступ: только через Nginx на порту 443 (HTTPS, HTTP/2)
  - Внутренние порты: 8080 (HTTP health/status), 50051 (gRPC), 8081 (Update Server) — только localhost (`127.0.0.1`)
  - Nginx проксирует: `https://<host>/health` → `http://127.0.0.1:8080/health`
  - Nginx проксирует: `https://<host>/status` → `http://127.0.0.1:8080/status`
  - Nginx проксирует: `https://<host>/` (gRPC) → `grpc://127.0.0.1:50051`
  - Nginx проксирует: `https://<host>/updates/*` → `http://127.0.0.1:8081/*`
- **Конфигурация Nginx (критично):**
  - `location /health` и `/status` должны быть **перед** `location /`
  - Иначе запросы попадут в gRPC прокси вместо HTTP прокси, что вызовет ошибку 502 Bad Gateway
  - Подробности: `Docs/SERVER_DEPLOYMENT_GUIDE.md`
- **Cache-Control**: `/updates/appcast.xml` — `max-age=60`, `/updates/health` — `max-age=30`, `/health` — `max-age=30`. Проверяется вручную (curl) и в smoke-checks CI.
- **Backpressure**: ошибки `stream_limit_exceeded`/`rate_limit_exceeded` мапятся на `RESOURCE_EXHAUSTED` (см. таблицу). Лимиты берутся из unified_config.
  - **Текущие настройки (prod):**
    - `max_concurrent_streams`: 50
    - `idle_timeout_seconds`: 900 (15 минут для длинных TTS ответов)
    - `max_message_rate_per_second`: 0 (отключено для аудио стримов)
    - `grace_period_seconds`: 30
- **Graceful shutdown**: перехватываем SIGTERM/SIGINT, останавливаем backpressure manager, логируем финальный агрегат метрик, корректно завершаем все активные стримы. Нарушение — блокер для релиза.
- **Структурированное логирование**: единый формат `ts=... level=INFO scope=grpc method=... decision=... ctx={...} dur_ms=...`. Автоматическая маскировка секретов (API ключи, пароли, токены).
- **Метрики производительности**: автоматический сбор P95 latency, error rate, decision rate каждые 60 секунд. Итоговые метрики при graceful shutdown.
- **Нет синхронных блокировок** в `StreamAudio`: IO через async-обёртки, CPU — threadpool с ограничением concurrency из unified_config.
- **Критические исправления (11 января 2026):**
  - Backpressure Manager: увеличен `idle_timeout_seconds` до 900 секунд (15 минут) для поддержки длинных TTS ответов
  - Backpressure Manager: отключен `max_message_rate_per_second` (0) для плавной передачи аудио стримов
  - Graceful Shutdown: добавлена остановка backpressure manager перед завершением
  - Структурированное логирование: автоматическая маскировка секретов в логах
  - Метрики: периодическое логирование каждые 60 секунд

---

## 8. Роллаут и «готовность»

- Feature-flag first: любое изменение >2 осей — под флаг + kill-switch + канареечный план (1% → 25% → 50% → 100%).
- SIMPLE-гейт ≤60 LOC/1 файл + 2 теста. Impact-гейт требует `change_impact.yaml`, обновления `STATE_CATALOG`, 8–14 pairwise сценариев и негативные тесты.
- «Готово» = чеклисты выполнены, SLO в норме (`p95_latency_ms(StreamAudio) ≤ 1000`, `error_rate(StreamAudio) ≤ 5%`), метрики в dashboards.
- Canary guardrails: jq one-liners из `scripts/` (ошибки/решения/latency) — обязательная часть проверки.

---

## 9. Ссылки

- `Docs/SERVER_DEVELOPMENT_RULES.md` — подробные гейты разработки
- `Docs/SERVER_DEPLOYMENT_GUIDE.md` — деплой, HTTPS ingress, smoke-проверки
- `Docs/BACKPRESSURE_README.md` — детальные лимиты и отладка
- `Docs/DATABASE_SETUP_GUIDE.md` — настройка PostgreSQL и hardening
- `Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md` — backup/restore/restore-drill канон
- `Docs/STATE_CATALOG.md` — карта состояний и владельцы
- `Docs/CI_GRPC_CHECKS.md` — обязательные CI-стадии
- `Docs/_archive/ARCHITECTURE_ALIGNMENT_CHECK.md` — историческая проверка соответствия архитектуры и кода
