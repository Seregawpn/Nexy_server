# Send Message Action Routing Diagnostics

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-09
- ID (INS-###): INS-N/A

## Diagnosis
Клиент получает аудио и текст, но action-канал не срабатывает (`action_chunks=0`), поэтому `send_message` не доходит до `ActionExecutionIntegration`.

## Root Cause
Узкий парсинг action payload на клиенте (`command/args` only) + отсутствие явной диагностики action-like текста -> команда теряется при легаси-обертках/нестандартном JSON и выглядит как "ничего не произошло".

## Optimal Fix
Расширить нормализацию action payload в единственной точке (GrpcClientIntegration) и добавить диагностику в той же точке ingestion.

Внедрено:
- Поддержка легаси-оберток: `command_payload`, `payload`, `action`, `data`, `result`.
- Поддержка альтернативных полей: `type` как команда, `params/arguments` как args.
- Предупреждение для action-like `text_chunk`, если action не извлечен.
- Более информативный warning при невалидном `ActionMessage`.
- Финальный `GRPC_END` summary дополнен флагом `action_like_text`.

## Verification
- `python3 -m py_compile client/integration/integrations/grpc_client_integration.py` — OK.
- Ожидаемые новые логи:
  - `text_chunk looks action-like but action payload was not extracted`
  - `ActionMessage invalid payload ... raw=...`
  - `summary={..., action_chunks=..., action_like_text=...}`

## Запрос/цель
Найти, почему команда "отправить сообщение" не исполняется на клиенте, и усилить диагностируемость пути парсинга/маршрутизации.

## Контекст
- Файлы: `client/integration/integrations/grpc_client_integration.py`
- Документы: `AGENTS.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/ANTIGRAVITY_PROMPT.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, через существующий EventBus путь.

## Решения/выводы
- Source of Truth для маршрутизации action сохранен в `GrpcClientIntegration`.
- Новый второй путь принятия решений не добавлен.
- На предоставленном логе первичный симптом: `action_chunks=0` при `text_chunks=1`.

## Открытые вопросы
- Какой точный `text_chunk` приходит в проблемной сессии до аудио (полный payload)?
- Приходит ли от сервера `action_message` в той же сессии, но с нестандартной структурой?

## Следующие шаги
- Запустить сценарий `send_message` и собрать новые логи `GRPC_END + text_chunk/action_message`.
- Если снова `action_chunks=0`, проверить серверный `assistant_response_parser` и условия генерации `command_payload` для `send_message`.
