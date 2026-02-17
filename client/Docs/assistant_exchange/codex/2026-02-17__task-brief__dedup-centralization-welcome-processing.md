# Task Brief: Dedup + centralization cleanup (welcome/processing)

## Context
Нужно продолжить системную зачистку дублей/конфликтов/гонок и усилить централизацию owner-путей.

## Diagnosis
Оставались локальные дубли:
1) `WelcomeMessageIntegration`: дублированный legacy метод возврата в sleep + повторяющийся код `mode.request`.
2) `ProcessingWorkflow`: явный дубль `completed_stages.clear()`.

## Architecture Fit
- Owner mode transitions сохранен через `mode.request` -> ModeManagementIntegration.
- Owner processing lifecycle сохранен в `ProcessingWorkflow`.
- Второй путь решений не добавлен.

## Changes
### 1) welcome_message_integration.py
- Удалено мертвое legacy API:
  - `_return_to_sleeping_after_playback` (не использовался).
- Убран неиспользуемый state:
  - `_welcome_playback_session_id`.
- Централизован mode-request publishing:
  - добавлен helper `_request_mode(target, reason, session_id)`;
  - все вызовы `mode.request` в welcome flow переведены на helper.

### 2) processing_workflow.py
- Удален явный duplicate call `self.completed_stages.clear()` (оставлен один).
- (ранее в этой ветке) сохранен race-fix по buffered `recognition_failed`.

## Concurrency / Race Guard
- Не добавлены новые owner-пути; behavior сохранен детерминированным.
- Существующий buffered fail guard в `ProcessingWorkflow` остается активным.

## Verification
- `python3 -m py_compile integration/integrations/welcome_message_integration.py integration/workflows/processing_workflow.py` — OK.
- Проверка grep:
  - `_return_to_sleeping_after_playback` отсутствует;
  - `_welcome_playback_session_id` отсутствует;
  - mode path идет через `_request_mode(...)`.

## Информация об изменениях
- Что изменено:
  - Удалены дублирующие/неиспользуемые ветки welcome sleep flow.
  - Упрощена и централизована публикация `mode.request` в welcome интеграции.
  - Удален явный дубль clear в processing workflow.
- Список файлов:
  - `integration/integrations/welcome_message_integration.py`
  - `integration/workflows/processing_workflow.py`
- Причина/цель изменений:
  - Снизить кодовую сложность, убрать дубли и уменьшить риск конфликтов порядка событий.
- Проверка:
  - Выполнен `py_compile`; поиском подтверждено удаление дублей.
