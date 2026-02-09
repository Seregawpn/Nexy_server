# MCP order + audio dtype fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Порядок ActionMessage относительно text/audio не был закреплён, а AUDIO_FORMAT мог содержать codec (pcm/mp3), что ломало dtype.

## Root Cause
ActionMessage отправлялся в середине цикла, а AUDIO_FORMAT использовался для двух смыслов.

## Optimal Fix
ActionMessage перенесён после text/audio в рамках item, добавлено предупреждение при некорректном dtype.

## Verification
`python3 -m pytest server/tests/test_grpc_mcp_integration.py -q` → 4 passed.

## Запрос/цель
Зафиксировать порядок MCP и защитить dtype от codec значений.

## Контекст
- Файлы: `server/modules/grpc_service/core/grpc_server.py`, `server/config/unified_config.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- ActionMessage отправляется после text/audio.
- При `AUDIO_FORMAT=pcm|mp3` пишется warning и dtype принудительно int16.

## Открытые вопросы
- Нужен ли тест на порядок MCP сообщений на клиенте.

## Следующие шаги
- При необходимости добавить интеграционный тест порядка сообщений.
