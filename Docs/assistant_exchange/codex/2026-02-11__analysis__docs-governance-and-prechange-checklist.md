# Docs Governance And Pre-Change Checklist

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В документации не было единого canonical-индекса и обязательного evidence-блока по Pre-Change Gate, из-за чего возникал риск дублирования и конфликтов флагов/владельцев.

## Root Cause
Разрозненные требования -> неполный pre-change процесс -> локальные решения и конфликтующие источники правил.

## Optimal Fix
Создана централизованная документационная обвязка: `Docs/DOCS_INDEX.md` + `Docs/PRE_CHANGE_CHECKLIST.md`; синхронизированы `AGENTS.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`; усилен `Docs/FEATURE_FLAGS.md` правилами ownership/conflicts.

## Verification
Проверить наличие новых файлов и обязательных ссылок на них в `AGENTS.md` и `Docs/CODEX_PROMPT.md`; убедиться, что шаблон отчета требует Pre-Change Gate Evidence.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/FEATURE_FLAGS.md`, `Docs/assistant_exchange/TEMPLATE.md`, `AGENTS.md`
- Source of Truth: `AGENTS.md` + `Docs/CODEX_PROMPT.md` + `Docs/DOCS_INDEX.md`
- Дублирование: устранена неоднозначность canonical vs archive
- Feature Flags check: добавлен реестр и governance-контракт
- Race check: N/A (документационные изменения)

## Запрос/цель
Доработать документацию для точного анализа и безопасного внесения изменений без дублирования/децентрализации.

## Контекст
- Файлы: `AGENTS.md`, `Docs/CODEX_PROMPT.md`, `Docs/FEATURE_FLAGS.md`, `Docs/assistant_exchange/TEMPLATE.md`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- Ограничения: без изменения runtime-архитектуры

## Решения/выводы
- Введен единый canonical-индекс и запрет `_archive` как SoT.
- Введен обязательный pre-change checklist.
- Шаблон отчетности теперь требует доказательство прохождения gate.

## Открытые вопросы
- Нужно ли зеркально добавить эти же пункты в `Docs/ANTIGRAVITY_PROMPT.md` для полной симметрии ассистентов.

## Следующие шаги
- Применять checklist перед каждым новым изменением.
