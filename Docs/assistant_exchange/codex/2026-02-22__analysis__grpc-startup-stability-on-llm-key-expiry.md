# gRPC startup stability on LLM key expiry

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-22
- ID (INS-###): N/A

## Diagnosis
При просроченном Gemini API key падала инициализация `text_processing`, что валило весь gRPC bootstrap. Дополнительно в `main.py` исключение фоновой task не считывалось и давало шум `Task exception was never retrieved`.

## Root Cause
Жёсткий startup network-probe в `LangChainGeminiProvider.initialize()` → внешняя ошибка провайдера становилась критичной для регистрации обязательного модуля → полный shutdown сервера + неаккуратный lifecycle фоновой task в `main.py`.

## Optimal Fix
- Убрана внешняя startup-проверка LLM из `initialize()`; оставлена локальная инициализация клиента, runtime-проверка выполняется на реальном запросе.
- В `main.py` добавлено явное `await serve_task` после `asyncio.wait(...)` и корректное закрытие второй task, чтобы не терять исключения.

## Verification
- `python -m py_compile server/main.py server/modules/text_processing/providers/langchain_gemini_provider.py`
- Локальный smoke-run `./.venv/bin/python server/main.py`:
  - gRPC инициализируется и не падает на bootstrap при том же окружении.
  - Нет `Task exception was never retrieved`.

## Информация об изменениях
- Что изменено:
  - Удалён startup stream-probe (`Hello`) из инициализации LangChain-провайдера.
  - Добавлено корректное считывание результата `serve_task` в main lifecycle.
- Файлы:
  - `server/main.py`
  - `server/modules/text_processing/providers/langchain_gemini_provider.py`
- Причина/цель:
  - Повысить устойчивость запуска сервера и убрать неуправляемые async-исключения.
- Проверка:
  - Компиляция py-файлов и локальный запуск/остановка сервера.

## Запрос/цель
Стабилизировать запуск сервера по логам инцидента: исключить падение на инициализации LLM и убрать unhandled task exception.

## Контекст
- Файлы: `server/main.py`, `server/modules/text_processing/providers/langchain_gemini_provider.py`
- Документы: `AGENTS.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, без второго owner-path.

## Решения/выводы
- Source of Truth для старта модулей сохранён в `ModuleCoordinator`.
- Убран хрупкий внешний check на startup; поведение упрощено и устойчивее к проблемам внешнего LLM сервиса.

## Открытые вопросы
- Нужен ли отдельный health-сигнал "LLM degraded" для observability (без блокировки startup).

## Следующие шаги
- Добавить integration test: startup при ошибке внешнего LLM не должен завершать gRPC bootstrap.
