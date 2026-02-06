# Task Execution Not Running (App)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-008

## Diagnosis
При запуске .app при активном экземпляре из Terminal новый процесс определяется как дубликат и завершает работу, поэтому действия (MCP/task execution) не обрабатываются.

## Root Cause
Single-instance политика (InstanceManagerIntegration) → детект дубликата по lock/pid → ранний exit → отсутствует активный обработчик action запросов в .app.

## Optimal Fix
Использовать только один активный экземпляр; если нужен .app — выключить Terminal‑процесс. При необходимости поддержки двух entrypoint — добавить передачу управления существующему экземпляру (IPC) вместо запуска нового.

## Verification
- Проверить `~/Library/Logs/Nexy/nexy.log` на отсутствие `InstanceStatus.DUPLICATE`.
- Убедиться, что при запросе действий есть лог `Action received`.

## Запрос/цель
Разобрать, почему команды действий не выполняются при запуске .app.

## Контекст
- Файлы: `integration/integrations/instance_manager_integration.py`, `integration/integrations/action_execution_integration.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения: единый экземпляр процесса

## Решения/выводы
- На текущих логах причина — детект дубликата экземпляра и завершение .app.

## Открытые вопросы
- Нужна ли поддержка передачи управления существующему экземпляру вместо exit?

## Следующие шаги
- Подтвердить, что параллельно запущен Terminal‑экземпляр.
- Проверить логи в момент команды, определить, доходит ли `grpc.response.action`.
