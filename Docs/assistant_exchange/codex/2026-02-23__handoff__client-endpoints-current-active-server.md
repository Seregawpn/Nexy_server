# Client endpoints for current active server

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-23
- ID (INS-###): N/A

## Diagnosis
Клиенту нужен единый список корректных endpoint'ов активного сервера, но update-plane частично деградирован (appcast 500).

## Root Cause
Инфраструктура на новом сервере активна и доступна, однако update service не имеет валидного runtime-манифеста для appcast generation.

## Optimal Fix
Использовать единый production host и закрепить для клиента только рабочие API:
- Host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
- gRPC over TLS: `:443`
- Health/status API: `/health`, `/status`, `/updates/health`

## Verification
Live-check (2026-02-23):
- `GET /health` -> 200
- `GET /status` -> 200
- `GET /updates/health` -> 200
- `GET /updates/appcast.xml` -> 500
- gRPC smoke (`443`, TLS) -> success

## Информация об изменениях
- Что изменено:
  - Добавлен handoff-документ с текущим набором корректных API/линков для клиентской части.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-23__handoff__client-endpoints-current-active-server.md`
- Причина/цель:
  - Зафиксировать корректные endpoint’ы и текущее состояние update-plane для клиентской интеграции.
- Проверка:
  - Curl-check HTTP endpoints + запуск `server/scripts/grpc_smoke.py`.

## Запрос/цель
Выдать корректные API и ссылки текущего активного сервера для использования клиентом.

## Контекст
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/scripts/quick_server_ops.sh`
- `server/scripts/grpc_smoke.py`

## Решения/выводы
- Единственный production host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`.
- Для runtime клиент должен использовать TLS gRPC на `443`.
- Update appcast endpoint сейчас неготов для клиента (`500`) и требует remediation на сервере.

## Открытые вопросы
- Нужен ли немедленный server-side fix appcast до включения автoобновления в клиенте.

## Следующие шаги
1. Оставить в клиенте gRPC/health интеграцию на текущем host.
2. Не включать appcast-based update check до фикса `GET /updates/appcast.xml`.
3. После фикса update-plane повторить smoke+curl валидацию.
