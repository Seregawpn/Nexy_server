# Web Search Diagnostics Script

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Нужен быстрый скрипт диагностики сети/доступа для Web Search.

## Root Cause
Поиск зависает из‑за внешнего вызова; нужно подтвердить DNS/HTTPS доступность.

## Optimal Fix
Добавить `web_search_diagnostics.py` с проверкой DNS/HTTPS и выводом текущих конфигов.

## Verification
Скрипт печатает статусы DNS/HTTPS и конфиг Web Search.

## Запрос/цель
Дать инструмент для диагностики зависания Web Search.

## Контекст
- Файлы: `server/server/scripts/web_search_diagnostics.py`

## Решения/выводы
- Добавлен диагностический скрипт.

## Открытые вопросы
- Где запускать диагностику (локально/staging/prod).

## Следующие шаги
- Запустить: `python3 server/server/scripts/web_search_diagnostics.py`.
