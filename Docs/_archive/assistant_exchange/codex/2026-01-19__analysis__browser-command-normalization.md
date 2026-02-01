# Browser Command Normalization

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-19
- ID (INS-###): INS-005

## Diagnosis
Команды от LLM приходили в вариантах (`browser-use`, `browser.use`) и отбрасывались на валидации/клиенте как unsupported, из-за чего browser_use не исполнялся.

## Root Cause
Несогласованный контракт команды → разные варианты строки → Pydantic/парсер не принимает → клиент говорит “не могу выполнить”.

## Optimal Fix
Единая нормализация команд в серверном парсере + валидаторе, и явное требование формата в prompt.

## Verification
Отправить “Open YouTube” и подтвердить, что команда `browser_use` проходит валидацию, приходит в клиент как `grpc.response.action`, и ActionExecutionIntegration не логирует `unsupported_command`.

## Запрос/цель
Нормализовать формат команды и зафиксировать требование в prompt.

## Контекст
- Файлы: server/server/integrations/core/assistant_response_parser.py, server/server/integrations/core/response_models.py, server/server/config/unified_config.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения общей архитектуры

## Решения/выводы
- Нормализация команды добавлена в Pydantic валидатор и парсер.
- Prompt усилен: command для browser_use только в каноническом виде.

## Открытые вопросы
- Нужно ли расширять allowed commands в Pydantic для messaging команд.

## Следующие шаги
- Прогон end-to-end запроса “Open YouTube” и проверка логов.
