# Permissions Double Prompts

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
Дублирование запроса разрешений Accessibility/Input Monitoring при старте клиента из-за параллельных инициаторов без общего гейта.

## Root Cause
FirstRunPermissionsIntegration и InputProcessingIntegration инициируют запросы независимо → конкурирующие системные промпты → повторные запросы/двойной UX.

## Optimal Fix
Централизовать запуск permission-зависимых интеграций через координатор и единую точку принятия решения (first_run + gateway), исключив локальные триггеры.

## Verification
Проверить, что при первом запуске выводится ровно один набор промптов, а input_processing не стартует до завершения first_run.

## Запрос/цель
Определить причину двойных запросов разрешений и предложить архитектурно корректный фикс.

## Контекст
- Файлы: integration/core/simple_module_coordinator.py, integration/integrations/first_run_permissions_integration.py, integration/integrations/input_processing_integration.py, modules/input_processing/keyboard/keyboard_monitor.py
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md, /Users/sergiyzasorin/Fix_new/Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без изменения архитектуры, централизовать решения

## Решения/выводы
- Два источника запроса прав нарушают принцип единого источника истины.
- Требуется гейт старта input_processing до завершения first_run и/или явного grant.

## Открытые вопросы
- Нужно ли полностью блокировать input_processing при missing permissions или запускать в degraded mode?

## Следующие шаги
- Ввести гейт на запуск permission-зависимых интеграций через gateway/координатор.
- Убрать локальные промпт-триггеры там, где они дублируют first_run.
