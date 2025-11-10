# 🧭 Nexy Server — Архитектурный обзор

Документ — канон для серверной части Nexy. Он закрепляет владельцев архитектурных осей, структуру каталогов, контракты модулей и обязательные проверки перед релизом. Любые изменения в этих разделах должны обновлять данный документ вместе с профильными канонами.

---

## 1. Оси, владельцы и источники истины

| Ось | Canon | Ответственный |
| --- | --- | --- |
| gRPC и протокол | `server/Docs/GRPC_PROTOCOL_AUDIT.md` | @grpc-core |
| Обновления и AppCast | `server/Docs/UPDATE_SYSTEM_FIXES.md` | @release-ops |
| Backpressure и лимиты | `server/Docs/BACKPRESSURE_README.md` | @reliability |
| Health/наблюдаемость | `server/Docs/CI_GRPC_CHECKS.md` | @sre-duty |
| Конфигурация | `server/config/unified_config.py` + `server/config/unified_config_example.yaml` | @server-platform |
| State Catalog | `server/Docs/STATE_CATALOG.md` | Tech Lead клиента |

- Один документ-канон на ось, один владелец. Ссылки в PR должны указывать на обновление соответствующего канона.
- `.github/CODEOWNERS` мапит эти оси на ответственных и используется CI для блокировки несогласованных изменений.
- `Docs/ADR_TEMPLATE.md` используется для фиксации изменений модулей/матриц/протокола (микро-ADR ≥7 строк).

---

## 2. Структура и границы слоёв

```
server/
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
├── scripts/                     # smoke/contract/гвардрайлы
├── tests/                       # unit/contract сценарии
├── config/                      # unified_config + пример
├── utils/                       # Утилиты (логирование, метрики, текст)
├── updates/                     # Артефакты обновлений (manifests, downloads, keys)
├── nginx/                       # Конфигурация Nginx для ingress
└── Docs/                        # Канон документов
```

- Модули ≠ интеграции ≠ workflow: бизнес-логика живёт в `server/modules/*`. Оркестрация и сценарии находятся в интеграциях и workflow-интеграциях.
- Прямые импорты между модулями запрещены. Доступ идёт через `server/integrations/service_integrations/module_coordinator.py`.
- gRPC слой не импортирует интеграции напрямую; связь через `GrpcServiceManager` → `ModuleCoordinator`.
- Все порты/лимиты/таймауты читаются из `unified_config`; в коде отсутствуют «магические числа».

---

## 3. gRPC ось

### 3.1 Протокол и генерация

- Канонический proto-файл: `server/modules/grpc_service/streaming.proto` (не дублировать в других каталогах).
- Регенерация Python-стабов:
  ```bash
  cd server/modules/grpc_service
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
  ```
- Любое breaking-изменение → новый `StreamingServiceV2` + feature-flag + 2 релиза параллельной поддержки (описано в `GRPC_PROTOCOL_AUDIT.md`).

### 3.2 Стабильность API

- RPC: `StreamAudio` (bidirectional stream), `InterruptSession` (unary-unary).
- Контракт совместимости фиксируется в `Docs/GRPC_PROTOCOL_AUDIT.md`; CI (`Docs/CI_GRPC_CHECKS.md`) блокирует регресс по регенерации proto и smoke-тестам.
- Любое добавление поля требует обновления таблицы совместимости в каноне.

### 3.3 Error Taxonomy

| error_type | gRPC code | Клиентское действие |
| --- | --- | --- |
| `timeout` | `DEADLINE_EXCEEDED` | Retry with backoff |
| `unavailable` | `UNAVAILABLE` | Retry exponential |
| `cancelled_by_user` | `CANCELLED` | Stop UX, no retry |
| `stream_limit_exceeded` | `RESOURCE_EXHAUSTED` | Backoff 60s → retry |
| `rate_limit_exceeded` | `RESOURCE_EXHAUSTED` | Throttle locally → retry |
| `validation_failed` | `INVALID_ARGUMENT` | Fix payload, no retry |
| `internal` | `INTERNAL` | Surface error, retry once |

Таблица дублируется комментариями в `server/modules/grpc_service/core/grpc_interceptor.py`. Любое изменение — синхронное обновление двух мест.

---

## 4. Конфигурация и флаги

Единый источник — `server/config/unified_config.py`. Значения для окружений перечислены в примере `unified_config_example.yaml`.

| Ключ | Тип | dev | stage | prod | Env override |
| --- | --- | --- | --- | --- | --- |
| `grpc.port` | int | 50051 | 50051 | 50051 | `GRPC_PORT` |
| `grpc.max_workers` | int | 10 | — (inherit prod) | 100 | `MAX_WORKERS` |
| `backpressure.max_concurrent_streams` | int | 10 | 25 | 50 | `BACKPRESSURE_MAX_STREAMS` |
| `backpressure.max_message_rate_per_second` | int | 5 | 8 | 10 | `BACKPRESSURE_MAX_RATE` |
| `backpressure.idle_timeout_seconds` | int | 60 | 180 | 300 | `BACKPRESSURE_IDLE_TIMEOUT` |
| `features.use_module_coordinator` | bool | true | true | true | `USE_MODULE_COORDINATOR` |
| `kill_switches.disable_module_coordinator` | bool | false | false | false | `NEXY_KS_DISABLE_MODULE_COORDINATOR` |
| `update.port` | int | 8081 | 8081 | 8081 | `UPDATE_PORT` |

> Stage наследует prod значения, если не указано иное. Все overrides проходят через unified_config + env, прямых setdefault в коде нет.

Backpressure лимиты, error-коды и рекомендации по отладке — в `Docs/BACKPRESSURE_README.md`.

---

## 5. Наблюдаемость и fail-fast

- **Decision-логи**: формат `ts=<iso> level=<lvl> scope=<module> method=<rpc> decision=<event> ctx=<json> dur_ms=<int>`. Логи без `decision` считаются нарушением канона.
- **Метрики (агрегация каждые 60s)**:
  - `p95_latency_ms{rpc}`
  - `error_rate{rpc}`
  - `backpressure_refusal_rate`
  - `decision_rate{type}`
- **Гвардрайлы CI** (`Docs/CI_GRPC_CHECKS.md`):
  - regen proto → diff запретов
  - smoke-тесты (`python scripts/grpc_smoke.py --host 127.0.0.1 --port 50051`)
  - health/порт/версия (`python scripts/check_grpc_health.py`)
  - Cache-Control заголовки (`curl -I https://<host>/appcast.xml | grep 'Cache-Control'`)
  - validate release size (`scripts/validate_updates.sh`)

---

## 6. Надёжность, ingress и shutdown

- **Ingress**: один публичный вход — HTTPS:443 через Nginx (`/etc/nginx/sites-available/nexy`). Внутренние адреса `127.0.0.1:50051`, `127.0.0.1:8080`, `127.0.0.1:8081` слушают только на localhost и недоступны извне.
- **Архитектура доступа:**
  - Внешний доступ: только через Nginx на порту 443 (HTTPS, HTTP/2)
  - Внутренние порты: 8080 (HTTP health/status), 50051 (gRPC), 8081 (Update Server) — только localhost
  - Nginx проксирует: `https://<host>/health` → `http://127.0.0.1:8080/health`
  - Nginx проксирует: `https://<host>/status` → `http://127.0.0.1:8080/status`
  - Nginx проксирует: `https://<host>/` (gRPC) → `grpc://127.0.0.1:50051`
- **Конфигурация Nginx (критично):**
  - `location /health` и `/status` должны быть **перед** `location /`
  - Иначе запросы попадут в gRPC прокси вместо HTTP прокси, что вызовет ошибку 502 Bad Gateway
  - Подробности: `Docs/SERVER_DEPLOYMENT_GUIDE.md` и `Docs/TROUBLESHOOTING_502.md`
- **Cache-Control**: `/appcast.xml` — `max-age=60`, `/updates/health` — `max-age=30`, `/health` — `max-age=30`. Проверяется вручную (curl) и автоматически `server/scripts/verify_cache_control_headers.py`.
- **Backpressure**: ошибки `stream_limit_exceeded`/`rate_limit_exceeded` мапятся на `RESOURCE_EXHAUSTED` (см. таблицу). Лимиты берутся из unified_config.
- **Graceful shutdown**: перехватываем SIGTERM/SIGINT, ждём завершения активных RPC ≤5s, печатаем финальный агрегат метрик. Нарушение — блокер для релиза.
- **Нет синхронных блокировок** в `StreamAudio`: IO через async-обёртки, CPU — threadpool с ограничением concurrency из unified_config.
- **Критические исправления (2 октября 2025):**
  - Импорт `get_config` в `grpc_server.py`: добавлен `from config.unified_config import get_config`
  - Обработка `PermissionError` в `update/config.py`: Update Server не критичен для работы основного сервера
  - Подробности: `Docs/CHANGELOG_SERVER_FIXES.md` и `Docs/REMOTE_SERVER_SPECIFICS.md`

---

## 7. Роллаут и «готовность»

- Feature-flag first: любое изменение >2 осей — под флаг + kill-switch + канареечный план (1% → 25% → 50% → 100%).
- SIMPLE-гейт ≤60 LOC/1 файл + 2 теста. Impact-гейт требует `change_impact.yaml`, обновления `STATE_CATALOG`, 8–14 pairwise сценариев и негативные тесты.
- «Готово» = чеклисты выполнены, SLO в норме (`p95_latency_ms(StreamAudio) ≤ 1000`, `error_rate(StreamAudio) ≤ 5%`), метрики в dashboards.
- Canary guardrails: jq one-liners из `scripts/` (ошибки/решения/latency) — обязательная часть проверки.

---

## 8. Ссылки

- `Docs/SERVER_DEVELOPMENT_RULES.md` — подробные гейты разработки
- `Docs/SERVER_DEPLOYMENT_GUIDE.md` — деплой, HTTPS ingress, smoke-проверки
- `Docs/BACKPRESSURE_README.md` — детальные лимиты и отладка
- `Docs/STATE_CATALOG.md` — карта состояний и владельцы
- `Docs/CI_GRPC_CHECKS.md` — обязательные CI-стадии
- `Docs/TROUBLESHOOTING_502.md` — диагностика проблемы 502 Bad Gateway и критические исправления
