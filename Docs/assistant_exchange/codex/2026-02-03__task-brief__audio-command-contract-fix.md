# Audio/command contract fixes

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Обнаружены потенциальные конфликты: смешение dtype/codec в AUDIO_FORMAT, fallback‑валидация команд без учета фич, и риск await на async‑generator.

## Root Cause
Один env использовался для разных смыслов, а fallback‑парсер не синхронизирован с allowed_commands.

## Optimal Fix
Введен AUDIO_CODEC для codec, fallback‑валидация теперь использует get_allowed_commands, а модульные результаты корректно обрабатывают awaitable и async‑iterator.

## Verification
`python3 -m pytest server/tests/test_assistant_response_parser.py server/tests/test_streaming_workflow_mcp.py -q` → 19 passed.

## Запрос/цель
Устранить потенциальные конфликты в аудио формате и командной валидации.

## Контекст
- Файлы: `server/config/unified_config.py`, `server/config.env`, `server/integrations/core/assistant_response_parser.py`, `server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- AUDIO_CODEC введен и используется для audio_format (codec), AUDIO_FORMAT остался dtype.
- Fallback‑валидация команд синхронизирована с allowed_commands.
- Обработка module.process поддерживает awaitable и async‑iterator.

## Открытые вопросы
- Нужна ли строгая фиксация порядка ActionMessage относительно text/audio на стороне клиента.

## Следующие шаги
- При необходимости добавить тесты на порядок MCP сообщений.
