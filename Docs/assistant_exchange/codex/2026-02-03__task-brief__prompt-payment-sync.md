# Prompt payment command sync

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Система промпта разрешала только `manage_subscription`, тогда как логика/валидатор поддерживают и `buy_subscription`.

## Root Cause
Prompt‑builder не синхронизирован с payment‑командами backend.

## Optimal Fix
Добавить `buy_subscription` в allowed_commands при `payment_enabled=True`.

## Verification
Вызов `build_system_prompt(payment_enabled=True)` включает `buy_subscription` в список разрешённых команд.

## Запрос/цель
Синхронизировать prompt и валидатор для payment‑команд.

## Контекст
- Файлы: `server/config/prompts.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- `buy_subscription` добавлен в allowed_commands при payment_enabled.

## Открытые вопросы
- Нет.

## Следующие шаги
- При необходимости добавить тест на allowed_commands в prompt.
