# Fixing Server Tests to Green

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Провалы тестов были вызваны потерей `session_id` в парсере, порядком валидации gRPC, неполным маскированием секретов, отсутствием `pytest-asyncio` и отсутствием гарантированного `text_response` для action-ответов.

## Root Cause
Фрагментарная логика: session_id привязывался только к action‑командам; hardware_id валидировался после session_id; маскирование не учитывало строковые токены вне ключей; async‑плагин не был установлен; поток с command+text мог не форсировать emission.

## Optimal Fix
Сделать session_id обязательным для любого JSON‑ответа; поменять порядок проверок в gRPC; усилить маскирование (regex + рекурсия); добавить `pytest-asyncio` и `pytest.ini`; гарантировать очередь текста для action‑ответа.

## Verification
Запустить:
- `pytest server/tests/test_assistant_response_parser.py`
- `pytest server/tests/test_grpc_identifier_validation.py`
- `pytest server/tests/test_secret_masking.py`
- `pytest server/tests/test_streaming_workflow_mcp.py`
- `pytest server/tests/test_pr2_module_interface.py`

## Запрос/цель
Привести `pytest server/tests` к зеленому состоянию.

## Контекст
- Файлы: `server/integrations/core/assistant_response_parser.py`, `server/modules/grpc_service/core/grpc_server.py`, `server/utils/logging_formatter.py`, `server/integrations/workflow_integrations/streaming_workflow_integration.py`, `server/requirements.txt`, `pytest.ini`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- session_id теперь сохраняется и для text‑only JSON.
- gRPC проверяет hardware_id до session_id.
- Маскирование расширено и рекурсивно.
- Добавлен pytest‑asyncio и pytest.ini.
- Текст action‑ответа гарантированно попадает в буфер эмиссии.

## Открытые вопросы
- Требуется ли установка зависимостей локально для фактического прогона (pytest-asyncio)?

## Следующие шаги
- Установить зависимости и прогнать targeted‑tests.
