# Web Search Smoke Test

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Нужно проверить Web Search на staging без запуска полного приложения.

## Root Cause
Локальная среда не подтверждает сетевой поиск, требуется smoke‑test в среде с доступом.

## Optimal Fix
Добавить скрипт smoke‑test для запуска на staging.

## Verification
Скрипт возвращает первый чанк ответа или явную ошибку/таймаут.

## Запрос/цель
Подготовить runnable скрипт проверки Web Search.

## Контекст
- Файлы: `server/server/scripts/web_search_smoke_test.py`

## Решения/выводы
- Добавлен скрипт для проверки поиска.

## Открытые вопросы
- В какой среде запускать (staging/production).

## Следующие шаги
- Запустить скрипт на staging с корректными env.
