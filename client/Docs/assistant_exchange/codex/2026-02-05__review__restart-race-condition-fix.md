# Restart Race Condition Fix Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
План исправлений реализован корректно: устранён TOCTOU, добавлен межпроцессный lock и проверка перед запуском.

## Root Cause
Децентрализованные guard‑проверки и окно между check→launch вызывали параллельные инстансы.

## Optimal Fix
Фикс выполнен архитектурно правильно: inter‑process lock + helper‑check перед `open -a`, без нового SoT.

## Verification
Рекомендованы ручные проверки: single restart, single PID, отсутствие дублей в логах.

## Запрос/цель
Проверить корректность реализации fix для restart race condition.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины

## Решения/выводы
- Lock TTL обработан после `flock`
- Lock release выполняется при неуспехе
- Проверка инстанса перенесена в helper

## Найденные проблемы (если review)
- Нет

## Открытые вопросы
- Нужно ли удалять lock‑файл на успешном рестарте (не требуется функционально)

## Следующие шаги
- Ручная проверка на двух быстрых стартах
