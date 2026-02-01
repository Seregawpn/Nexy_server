# Permissions Stale Flag Fix

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
Исправление добавляет сброс `_are_all_granted` в начале `start()`, что устраняет риск устаревшего состояния при отозванных разрешениях.

## Root Cause
`_are_all_granted` ранее сохранялся из флага и мог оставаться True даже при фактическом отзыве прав.

## Optimal Fix
Сбрасывать `_are_all_granted=False` перед проверкой системных статусов и выставлять True только при `all_granted`.

## Verification
Сценарий: флаг есть, права отозваны. Ожидаемо `are_all_granted` остается False до реального подтверждения.

## Запрос/цель
Проверить корректность фикса устаревшего статуса разрешений.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md, /Users/sergiyzasorin/Fix_new/Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Фикс корректен, устраняет главный риск stale состояния.

## Найденные проблемы (если review)
- Нет.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать ручную проверку отзыва разрешений.

## Итоговый статус
**СООТВЕТСТВУЕТ**
