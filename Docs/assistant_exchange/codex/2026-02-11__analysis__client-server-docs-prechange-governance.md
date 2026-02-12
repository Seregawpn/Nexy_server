# Client Server Docs Pre-Change Governance

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Клиентская и серверная зоны имели неполный/несинхронизированный pre-change процесс, включая устаревшие ссылки и отсутствие локальных canonical-index/checklist.

## Root Cause
Разные AGENTS на workspace-уровне + отсутствие обязательного gate в client/server docs -> ассистент может вносить изменения без единого SoT и проверки дубликатов/флагов.

## Optimal Fix
Синхронизированы `client/AGENTS.md`, `server/AGENTS.md`, `server/server/AGENTS.md`; добавлены локальные `DOCS_INDEX.md` и `PRE_CHANGE_CHECKLIST.md` для client и server runtime.

## Verification
Проверены ссылки и наличие обязательных блоков (`Pre-Change Gate`, `Rule of sources`, `DOCS_INDEX`, `PRE_CHANGE_CHECKLIST`) через `rg` и `ls`.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `client/AGENTS.md`, `server/AGENTS.md`, `server/server/AGENTS.md`, `client/Docs/README.md`, `client/Docs/DOCUMENTATION_MAP.md`, `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`
- Source of Truth: root `AGENTS.md` + workspace AGENTS + new workspace `DOCS_INDEX.md`
- Дублирование: унифицированы правила pre-change между client/server
- Feature Flags check: client/server AGENTS теперь явно требуют `FEATURE_FLAGS` перед изменениями
- Race check: N/A (документационные изменения)

## Запрос/цель
Улучшить документацию клиентской и серверной части, чтобы ассистент корректно анализировал и вносил изменения.

## Контекст
- Файлы: `client/AGENTS.md`, `server/AGENTS.md`, `server/server/AGENTS.md`
- Новые файлы: `client/Docs/DOCS_INDEX.md`, `client/Docs/PRE_CHANGE_CHECKLIST.md`, `server/server/Docs/DOCS_INDEX.md`, `server/server/Docs/PRE_CHANGE_CHECKLIST.md`
- Ограничения: без изменения runtime-кода

## Решения/выводы
- Убраны неактуальные ссылки в server AGENTS.
- Добавлен обязательный pre-change gate в client/server workspace.
- Добавлен запрет использования `_archive` как Source of Truth.

## Открытые вопросы
- Нужна ли дополнительная синхронизация с `.cursorrules` в `client/` для явного упоминания новых checklist-файлов.

## Следующие шаги
- Использовать новые checklist перед любыми изменениями в `client/` и `server/server/`.
