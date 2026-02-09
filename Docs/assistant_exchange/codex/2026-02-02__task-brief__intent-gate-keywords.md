# Intent Gate Keywords

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-02
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
- Инструменты и скриншот подключались без явного intent‑gate, что увеличивало задержку.

## Root Cause
- Нет единой decision‑функции для включения screenshot/tools на уровне workflow.

## Optimal Fix
- Ввести keyword‑based intent‑gate в StreamingWorkflowIntegration.
- Добавить per‑request use_search в TextProcessingModule/Processor/Provider.

## Verification
- Проверить intent decision в логах и снижение TTFB для non‑vision запросов.

## Запрос/цель
- Реализовать EN‑only keyword‑gate для screenshot/tools и разделить web_search vs browser_use.

## Контекст
- Файлы: server/server/integrations/workflow_integrations/streaming_workflow_integration.py, server/server/modules/text_processing/module.py, server/server/modules/text_processing/core/text_processor.py, server/server/modules/text_processing/providers/langchain_gemini_provider.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без нового источника истины, без отдельного классификатора.

## Решения/выводы
- Keyword‑gate с приоритетами: system_action → vision → web_search → browser_use → messages → default.
- use_search проходит по цепочке в провайдер, чтобы отключать tools.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать ручные проверки intent‑decision по 3–4 фразам.
