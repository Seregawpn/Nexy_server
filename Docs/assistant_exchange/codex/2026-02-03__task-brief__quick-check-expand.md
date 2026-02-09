# Quick check expand

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Быстрая проверка не покрывала контракт prompt/allowed_commands и dtype/codec.

## Root Cause
Отсутствовали sanity‑проверки на критичные расхождения.

## Optimal Fix
Расширен quick_check.sh проверками prompt‑команд и аудио dtype/codec.

## Verification
Запуск `server/scripts/quick_check.sh` завершает проверку без ошибок.

## Запрос/цель
Ускорить выявление конфигурационных конфликтов.

## Контекст
- Файлы: `server/scripts/quick_check.sh`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Добавлены проверки prompt payment commands и dtype/codec.

## Открытые вопросы
- Нет.

## Следующие шаги
- При необходимости добавить lint/format в quick_check.
