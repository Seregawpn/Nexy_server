# Filter Status Checked in Offline Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Offline check counted all `permissions.status_checked` mentions, including subscriptions and debug logs, which mismatched the updated test expectations.

## Root Cause
Regex was too broad and did not scope to published events.

## Optimal Fix
Filter `permissions.status_checked` to published events only (`📢 Событие опубликовано: permissions.status_checked`).

## Verification
Updated `scripts/check_first_run_state.py` to use the narrowed regex.

## Запрос/цель
Align offline check with test script criteria.

## Контекст
- Файлы: scripts/check_first_run_state.py
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без изменения приложения

## Решения/выводы
- Offline check now matches published-only criteria.

## Открытые вопросы
- Нужно ли повторно прогнать offline check после изменения?

## Следующие шаги
- При необходимости запустить `python3 scripts/check_first_run_state.py`.
