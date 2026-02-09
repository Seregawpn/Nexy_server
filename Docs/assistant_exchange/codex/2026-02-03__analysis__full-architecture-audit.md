# Full architecture audit — parsing/audio/MCP/gRPC

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Критичных гонок не обнаружено, но есть 5 потенциальных конфликтов/дублей, которые могут дать нестабильность: конфликт аудио формата, двойная логика валидации команд, риск некорректного async‑итератора модулей, неоднозначная эмиссия текста в JSON‑потоке, и порядок/момент доставки MCP команд.

## Root Cause
Часть логики дублируется на разных слоях (Pydantic vs fallback‑валидация, JSON‑stream vs финальный парсинг), а в аудио‑конфигурации один env используется для двух разных смыслов.

## Optimal Fix
Зафиксировать контракт аудио‑формата, убрать дублирующую валидацию или синхронизировать правила, и явно стандартизировать модульный async‑интерфейс.

## Verification
- Синхронизировать аудио формат (dtype vs codec) и проверить соответствие в grpc_server и audio_generation.
- Проверить, что отключенные команды не проходят fallback‑валидацию.
- Добавить тест на async generator в module.process.

## Запрос/цель
Полный аудит на дубли/конфликты/гонки в парсинге, аудио, MCP и gRPC.

## Контекст
- Файлы: `server/integrations/core/assistant_response_parser.py`, `server/integrations/core/response_models.py`, `server/integrations/core/json_stream_extractor.py`, `server/integrations/workflow_integrations/streaming_workflow_integration.py`, `server/modules/grpc_service/core/grpc_server.py`, `server/integrations/service_integrations/grpc_service_integration.py`, `server/modules/audio_generation/*`, `server/config/unified_config.py`.
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: аудит без изменений архитектуры

## Решения/выводы
- Конфликт формата аудио: `AudioConfig.from_env()` берет `AUDIO_FORMAT` и для `format` (dtype) и для `audio_format` (codec/pcm), что может сломать ожидания между TTS и gRPC.
- Дублирующая валидация команд: Pydantic запрещает отключенные команды, но fallback‑валидация в парсере может пропустить их, если Pydantic валидатор не сработал (например, ImportError).
- Риск в `streaming_workflow_integration._stream_module_results`: всегда `await module.process(...)`, что ломается, если `process` — async generator функция (не awaitable). Возможен скрытый конфликт интерфейса.
- JSON streaming vs финальный парсинг: есть несколько путей добавления текста в буфер, риск двойной эмиссии или разных разбиений (частично mitigated хеш‑дедупом).
- MCP action delivery: gRPC отправляет ActionMessage внутри основного цикла, до/после text/audio в зависимости от item. Это может быть неожиданно для клиента, если требуется строгий order.

## Найденные проблемы (если review)
- Потенциальный конфликт аудио формата (dtype vs codec) — high.
- Дублирующая валидация команд — medium.
- Async‑интерфейс модулей — medium.
- JSON‑stream двойная эмиссия — low/medium.
- Порядок MCP сообщений — low/medium.

## Открытые вопросы
- Требуется ли строгий порядок ActionMessage относительно text/audio?
- Должен ли fallback‑парсер уважать feature flags даже без Pydantic?
- Нужен ли отдельный env для codec (например `AUDIO_CODEC`) вместо `AUDIO_FORMAT`?

## Следующие шаги
- Принять контракт для аудио формата и синхронизировать env/конфиг.
- Синхронизировать fallback‑валидацию с allowed_commands.
- Зафиксировать контракт async‑интерфейса модулей.
