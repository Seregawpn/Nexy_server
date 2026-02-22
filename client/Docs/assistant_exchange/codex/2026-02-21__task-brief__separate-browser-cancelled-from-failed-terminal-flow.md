## Task
Разделить terminal-ветки `browser.cancelled` и `browser.failed` без усложнения архитектуры и без второго owner-path.

## Что сделано
- Добавлен явный `type=BROWSER_TASK_CANCELLED` в publish для cancel-ветки.
- В cancel terminal payload добавлены `cancel_reason` и `cancel_source`.
- В `ProcessingWorkflow` `browser.cancelled` переведен на отдельный обработчик `_on_browser_cancelled` (без изменения финальной owner-логики завершения цепочки).
- В `ActionExecutionIntegration` улучшено определение terminal-статуса browser lifecycle: учитываются и raw event type, и payload type.

## Verification
- `python3 -m py_compile` успешно для:
  - `integration/integrations/browser_use_integration.py`
  - `integration/workflows/processing_workflow.py`
  - `integration/integrations/action_execution_integration.py`

## Информация об изменениях
- Что изменено:
  - Разведены semantic paths для `cancelled` и `failed` на уровне workflow-обработчиков.
  - Устранен риск ошибочной классификации `browser.cancelled` как `success` в lifecycle.
  - Добавлена диагностика причины отмены (`cancel_reason`, `cancel_source`) в terminal payload.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/workflows/processing_workflow.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/action_execution_integration.py`
- Причина/цель изменений:
  - Сделать terminal-состояния browser ветки однозначными и диагностируемыми, без изменения центра принятия решений.
- Проверка:
  - Синтаксическая компиляция (`py_compile`) и контроль точек подписки/terminal publish.
