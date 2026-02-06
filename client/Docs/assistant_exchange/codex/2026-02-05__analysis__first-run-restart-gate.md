# First-Run Restart Gate

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
Несинхронизированные точки принятия решения о рестарте и TOCTOU между проверкой и запуском ведут к параллельным инстансам. Дублирующиеся «мягкие» guard-ы (pgrep/lock/flag) не образуют единого gate.

## Root Cause
Децентрализация рестарт-логики между PermissionOrchestrator, PermissionsRestartHandler, helper-скриптом и InstanceManager → проверки выполняются в разное время и в разных местах → race между check и open, возможен дубль рестарта и запуск 2+ процессов.

## Optimal Fix
Сконцентрировать single-flight на уровне permission_restart (межпроцессный lock + idempotency flag), а проверку «другой инстанс» выполнять в helper прямо перед open, опираясь на lock-файл InstanceManager. Источник истины для first-run и рестартов — permission_ledger.json.

## Verification
Ручной запуск с очищенными флагами, один PID Nexy, один рестарт, после рестарта стабильная работа. Логи: один [PERMISSION_RESTART] Restart requested и отсутствие повторов.

## Запрос/цель
Проанализировать текущую логику first-run + restart и предложить архитектурно корректный fix для single-restart и single-instance.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py, modules/permissions/v2/orchestrator.py, modules/instance_manager/core/instance_manager.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/first_run_flow_spec.md
- Ограничения: без новых источников истины, решение через существующие модули/координаторы

## Решения/выводы
- Source of Truth: permission_ledger.json
- Рестарт-gate должен быть межпроцессным и жить в permission_restart
- TOCTOU устраняется переносом проверки «другой инстанс» в момент запуска

## Открытые вопросы
- Нужен ли отдельный restart_in_progress.lock или достаточно AtomicRestartFlag + instance lock?
- Требуется ли fsync/верификация записи ledger перед рестартом?

## Следующие шаги
- Согласовать primary fix и реализовать минимальные изменения
- Провести ручную проверку с параллельными стартами
