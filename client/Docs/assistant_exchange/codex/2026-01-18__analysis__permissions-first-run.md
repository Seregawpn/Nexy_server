# Permissions First-Run Analysis

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
First-run запрашивает разрешения без проверки статусов и без обязательного открытия System Settings для непроемптируемых разрешений; часть запросов может не показываться, а UX воспринимается как «не все разрешения».

## Root Cause
Активаторы вызываются последовательно без статуса/фолбэков → при недоступном API/неpromptable разрешениях диалог не появляется → пользователь не видит часть запросов и считает flow неполным.

## Optimal Fix
Добавить статус‑проверки и settings‑fallback в FirstRunPermissionsIntegration перед перезапуском; логировать и публиковать события по каждому разрешению.

## Verification
Очистить флаги first-run, запустить приложение, убедиться в логах активации всех требуемых разрешений и в открытии System Settings для accessibility/input_monitoring/full_disk_access при отсутствии доступа.

## Запрос/цель
Выявить причину отсутствия некоторых разрешений при первом запуске и предложить архитектурно корректный способ диагностики/исправления.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/first_run/activator.py, config/unified_config.yaml
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-010), Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без реархитектуры, внутри текущего permission flow

## Решения/выводы
- Причина вероятнее всего в отсутствии status‑check и settings‑fallback на часть разрешений.
- Текущий hold/timeouts дают ощущение «зависания» (≈ 6 * (13s + pause)).

## Открытые вопросы
- Есть ли в логах события активации screen_capture/input_monitoring/full_disk_access для проблемного запуска?
- Был ли уже создан permissions_first_run_completed.flag перед запуском?

## Следующие шаги
- Добавить status‑check и settings‑fallback и логирование по каждому разрешению.
- Провести повторный запуск после очистки флагов и проверить tccd logs.
