# 🎤 Nexy Server

**Серверная часть Nexy: gRPC-потоки, модульная обработка команд и инфраструктура обновлений**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Основные возможности

- 📡 **gRPC streaming** — двусторонние аудио-стримы через `StreamingService`.
- 🧠 **Модульная обработка** — бизнес-логика живёт в `server/modules/*`, оркестрация разнесена по интеграциям.
- 🛡️ **Backpressure** — лимиты и коды отказов описаны в `Docs/BACKPRESSURE_README.md`.
- 📊 **Наблюдаемость** — структурированные decision-логи и метрики p95/error-rate/backpressure.
- ♻️ **Обновления** — подписанные манифесты и проверка размеров артефактов с GitHub CDN.

## 📚 Канонические документы

| Ось | Canon | Owner |
| --- | --- | --- |
| gRPC и протокол | `server/Docs/GRPC_PROTOCOL_AUDIT.md` | @grpc-core |
| Обновления | `server/Docs/UPDATE_SYSTEM_FIXES.md` | @release-ops |
| Backpressure | `server/Docs/BACKPRESSURE_README.md` | @reliability |
| Health & наблюдаемость | `server/Docs/CI_GRPC_CHECKS.md` | @sre-duty |
| Конфигурация | `server/config/unified_config.py` + `server/config/unified_config_example.yaml` | @server-platform |

Каждая ось имеет один источник истины и назначенного владельца. Изменения требуют обновления соответствующего документа.

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8+
- Доступ к API-ключам Gemini и Azure Speech
- Возможность открыть порт `50051` локально (только для INTERNAL тестов)

### Установка

```bash
git clone https://github.com/Seregawpn/Nexy_server.git
cd Nexy_server/server
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp config.env.example config.env  # заполните секреты и порты под окружение
```

### Запуск (INTERNAL)

```bash
python main.py  # gRPC поднимается на 0.0.0.0:50051
```

Публичный доступ всегда идёт через Nginx на 443/HTTPS; внутренние порты 8080/8081/50051 не публикуются вовне.

## ⚙️ Конфигурация (единый источник — `unified_config`)

| Ключ | Тип | dev | stage | prod | Env override |
| --- | --- | --- | --- | --- | --- |
| `grpc.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `GRPC_HOST` (`auto` → по `NEXY_ENV`) |
| `grpc.port` | int | 50051 | 50051 | 50051 | `GRPC_PORT` |
| `grpc.max_workers` | int | 10 | — (inherit prod) | 100 | `MAX_WORKERS` |
| `http.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `HTTP_HOST` (`auto` → по `NEXY_ENV`) |
| `http.port` | int | 8080 | 8080 | 8080 | `HTTP_PORT` |
| `backpressure.max_concurrent_streams` | int | 10 | 25 | 50 | `BACKPRESSURE_MAX_STREAMS` |
| `backpressure.max_message_rate_per_second` | int | 5 | 8 | 10 | `BACKPRESSURE_MAX_RATE` |
| `features.use_module_coordinator` | bool | true | true | true | `USE_MODULE_COORDINATOR` |
| `kill_switches.disable_module_coordinator` | bool | false | false | false | `NEXY_KS_DISABLE_MODULE_COORDINATOR` |
| `update.host` | string | `0.0.0.0` | `127.0.0.1` | `127.0.0.1` | `UPDATE_HOST` (`auto` → по `NEXY_ENV`) |
| `update.port` | int | 8081 | 8081 | 8081 | `UPDATE_PORT` |

> Stage наследует prod значения, если не указано иное в `unified_config_example.yaml`. `NEXY_ENV=prod/stage` автоматически переключает gRPC/HTTP/Update на `127.0.0.1`, весь внешний трафик обслуживает Nginx на `https://20.151.51.172`. В dev по умолчанию используем `0.0.0.0`, чтобы подключаться напрямую. Указание `auto` в env соответствует поведению по окружению.

## 🏗️ Архитектура и границы

- **Слои не протекают:** бизнес-логика живёт в `server/modules/*`, интеграции — в `server/integrations/{core,service_integrations,workflow_integrations}`. Прямых импортов между модулями нет; доступ идёт через `ModuleCoordinator`.
- **gRPC сервер:** канонический протокол описан в `server/modules/grpc_service/streaming.proto`. Регенирация — `python -m grpc_tools.protoc -I server/modules/grpc_service --python_out=server/modules/grpc_service --grpc_python_out=server/modules/grpc_service server/modules/grpc_service/streaming.proto` (см. `Docs/SERVER_DEVELOPMENT_RULES.md`).
- **Конфигурация:** все флаги, таймауты и лимиты берутся из `server/config/unified_config.py`. Код не держит хардкоды.
- **Наблюдаемость:** обязательны decision-логи (`ts`, `level`, `scope`, `method`, `decision`, `ctx`, `dur_ms`) и метрики `p95_latency_ms`, `error_rate`, `backpressure_refusal_rate`.
- **Ingress:** наружный трафик проходит через Nginx (HTTPS:443, IP продакшна `20.151.51.172`). `NEXY_ENV=prod/stage` автоматически заставляет службы слушать `127.0.0.1`, локально (`dev`) можно открыть `0.0.0.0`.

Подробный обзор — в `server/Docs/ARCHITECTURE_OVERVIEW.md`.

## 🐛 Известные проблемы

- **Self-signed сертификат для 443 (prod):** пока не установлен публичный сертификат. Клиентам требуется доверить сертификат вручную.
- **`config.env` не входит в git:** создайте его из `config.env.example` и заполните секреты.
- **Конфликты порта 50051:** перед локальным запуском убедитесь, что порт свободен или задайте `GRPC_PORT` в `config.env`.

## 🤝 Вклад

1. Форкните репозиторий и создайте ветку (`git checkout -b feature/<name>`).
2. Выполните Impact/SIMPLE-гейты из `server/Docs/SERVER_DEVELOPMENT_RULES.md`.
3. Запустите smoke и contract проверки (`python -m pytest`, `python scripts/grpc_smoke.py`) — результаты приложите в PR.
4. Откройте Pull Request с ссылками на обновлённые канонические документы.

## 📄 Лицензия

Проект распространяется под лицензией MIT — см. [LICENSE](LICENSE).
