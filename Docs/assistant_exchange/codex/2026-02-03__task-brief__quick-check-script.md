# Quick check script

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Не было единых быстрых проверок для ускорения фиксов.

## Root Cause
Отсутствовал минимальный скрипт запуска тестов и sanity‑проверок конфигов.

## Optimal Fix
Добавлен `scripts/quick_check.sh` с быстрым набором проверок.

## Verification
Запуск скрипта `server/scripts/quick_check.sh` должен отработать без ошибок.

## Запрос/цель
Ускорить цикл фикса/проверки.

## Контекст
- Файлы: `server/scripts/quick_check.sh`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Добавлен скрипт быстрого прогона тестов и sanity‑проверки флагов.

## Открытые вопросы
- Нужно ли добавить lint/format в quick_check.

## Следующие шаги
- При необходимости расширить набор проверок.
