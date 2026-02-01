# Remove Dev Bypass For Permissions V2

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
Dev‑bypass отключал реальный first‑run и мешал штатному запросу разрешений.

## Root Cause
В V2 integration существовал Terminal Dev Mode bypass, который завершал wizard без реальных диалогов.

## Optimal Fix
Полностью удалить bypass‑ветку и проверку dev‑флага.

## Verification
- При запуске всегда стартует wizard.
- Нет логов "Bypassing permission wizard".

## Запрос/цель
Не обходить first‑run, выполнять как должно.

## Контекст
- Файлы: `modules/permissions/v2/integration.py`

## Решения/выводы
- Удалён dev‑bypass.

## Открытые вопросы
- Нет.

## Следующие шаги
- Очистить ledger/flags и проверить первый запуск.
