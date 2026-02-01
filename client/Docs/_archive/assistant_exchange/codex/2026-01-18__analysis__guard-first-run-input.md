# Guard Input During First-Run

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Ранний запуск input_processing во время first-run создавал параллельные TCC prompts, блокируя Mic/Screen до рестарта.

## Root Cause
Guard основывался на `permissions_first_run_completed.flag`, который создаётся до рестарта, поэтому input-monitoring стартовал слишком рано.

## Optimal Fix
Блокировать запуск input/voice_recognition/screenshot_capture при `first_run_in_progress` или `permissions_restart_pending` и добавить self-guard в InputProcessingIntegration.

## Verification
Обновлены guard-условия в coordinator и input_processing.

## Запрос/цель
Обеспечить последовательный показ разрешений в одном first-run.

## Контекст
- Файлы: integration/core/simple_module_coordinator.py, integration/integrations/input_processing_integration.py
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без изменения последовательности activator

## Решения/выводы
- input_processing больше не стартует при `first_run_in_progress`.
- coordinator пропускает зависимые интеграции при first_run/restart_pending.

## Открытые вопросы
- Нужен ли аналогичный guard для других интеграций, которые могут триггерить TCC?

## Следующие шаги
- Прогнать `scripts/test_first_run_integration.sh`.
