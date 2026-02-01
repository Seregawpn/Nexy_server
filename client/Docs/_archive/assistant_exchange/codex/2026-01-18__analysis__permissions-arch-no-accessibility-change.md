# Permissions Architecture (No Accessibility Changes)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Нужно закрепить архитектуру first-run без изменений в Accessibility, при этом сохранить правильный порядок и перезапуск без конфликтов с обновлениями.

## Root Cause
Отсутствие зафиксированного контракта “sequential activate + hold + optional settings-only для FDA” приводит к восприятию «пропусков» и неявным блокировкам.

## Optimal Fix
Сформировать архитектурный контракт: последовательные activator-вызовы, паузы, settings-only только для FDA, перезапуск через permission_restart.

## Verification
Очистить флаги и пройти first-run: порядок из required_permissions, видимые логи по каждому разрешению, restart через permission_restart.

## Запрос/цель
Сформировать идеальную архитектуру first-run, не трогая Accessibility.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/first_run/activator.py, integration/integrations/permission_restart_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-010/011)
- Ограничения: Accessibility не менять

## Решения/выводы
- Assumption: Accessibility уже соответствует требованиям и работает корректно.
- Settings-only применять только для Full Disk Access.

## Открытые вопросы
- Подтвердить, что Accessibility уже settings-only и не требует изменений.

## Следующие шаги
- Зафиксировать контракт в коде/логах и применить к остальным разрешениям.
