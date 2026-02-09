# Messages Prompt Missing

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-01
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
Сервер иногда использует статический промпт без блока Messages, из-за чего LLM отвечает «не умею отправлять сообщения» и не формирует action JSON.

## Root Cause
Динамический промпт включается только при whatsapp/browser/subscription → messages_enabled не учитывается → система падает на static prompt без инструкций → нет команды send_message.

## Optimal Fix
Сделать динамический промпт активным при messages_enabled или всегда (модульный промпт уже защищает включение/исключение блоков).

## Verification
Проверить, что при запросе «отправь сообщение…» сервер формирует action JSON send_message; клиент принимает команду и исполняет.

## Запрос/цель
Найти причину, почему ассистент говорит «не умею отправлять сообщения», и предложить минимальный архитектурный фикс.

## Контекст
- Файлы: `server/server/config/unified_config.py`, `server/server/config/prompts.py`, `client/integration/integrations/action_execution_integration.py`, `client/config/unified_config.yaml`
- Документы: `AGENTS.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, архивные `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/ANTIGRAVITY_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: Без реархитектуры, централизованная логика, один источник истины

## Решения/выводы
- Ключевая причина — условие выбора промпта в `get_provider_config`, не учитывающее messages.
- Клиентские фичи messages включены; проблема вероятнее на сервере (промпт).

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- Используется ли в окружении продакшена статический GEMINI_SYSTEM_PROMPT без Messages блока?

## Следующие шаги
- Правка условия выбора промпта.
- Лог в старте провайдера: источник промпта (dynamic/static) + наличие «MESSAGES ACTIONS».
