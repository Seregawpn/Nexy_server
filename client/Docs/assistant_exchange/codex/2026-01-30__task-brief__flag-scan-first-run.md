# Scan For First-Run Flag Usage

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
Нужно проверить, где ещё используется `permissions_first_run_completed.flag` как gate.

## Root Cause
Потенциальные локальные проверки флага могли создавать второй SoT.

## Optimal Fix
Провести поиск и оставить флаг только как кэш (создание), без чтения в логике принятия решений.

## Verification
- `rg "permissions_first_run_completed.flag"` не находит чтения флага вне создания.

## Запрос/цель
Найти и убрать все остаточные флаг‑гейты.

## Контекст
- Файлы: `integration/`, `modules/`

## Решения/выводы
- Осталось единственное упоминание в `integration/integrations/first_run_permissions_integration.py` как путь для создания кэша.

## Открытые вопросы
- Нет.

## Следующие шаги
- Не требуется.
