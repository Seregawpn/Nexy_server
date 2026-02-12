# PROJECT ASSISTANT RULES — CLIENT

Этот файл дополняет корневой `AGENTS.md` и применяется только для клиентской части.

## Контекст клиента
- Базовые правила проекта: `AGENTS.md` (в корне).
- Архитектура и текущие принципы: `client/Docs/ARCHITECTURE_OVERVIEW.md`.
- Требования: `client/Docs/PROJECT_REQUIREMENTS.md`.
- Клиентские правила и упаковка: см. `.cursorrules` (раздел 1.0.1).
- Документация: см. `client/Docs/README.md`, `client/Docs/DOCUMENTATION_MAP.md`, `client/Docs/DOCS_INDEX.md`.

## Pre-Change Gate (обязательно до любых правок кода)
- Сначала прочитай и зафиксируй релевантные разделы:
  - `AGENTS.md` (корень)
  - `Docs/DOCS_INDEX.md` и `Docs/PRE_CHANGE_CHECKLIST.md` (корневой процесс)
  - `client/Docs/DOCS_INDEX.md` и `client/Docs/PRE_CHANGE_CHECKLIST.md` (клиентский процесс)
  - `client/Docs/PROJECT_REQUIREMENTS.md`
  - `client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `client/Docs/FEATURE_FLAGS.md`
- Перед изменениями проверь дубликаты/параллельные пути (>=70% сходства) и зафиксируй единого владельца (Source of Truth).
- Любой новый локальный стейт/флаг допустим только при явном владельце, зоне действия и плане удаления.
- Если gate не пройден, изменения не вносить.

## Правило источников
- `client/Docs/_archive/*` — только historical reference, не Source of Truth.
- При конфликте использовать canonical-документы из `client/Docs/DOCS_INDEX.md`, затем корневой `Docs/DOCS_INDEX.md`.

## Отчетность ассистента (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `client/Docs/assistant_exchange/<assistant>/` или `Docs/assistant_exchange/<assistant>/` по контексту задачи.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.
- Перезапись запрещена: только новый файл.

## Фокус клиента
- Работай внутри текущих модулей и интеграций клиента.
- Не нарушай существующие границы модулей.
