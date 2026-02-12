# Full Markdown Reference Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Не вся документация актуальна относительно текущего кода и структуры репозитория. Есть системные битые ссылки, особенно в старых requirement-картах и исторических описаниях.

## Root Cause
Реорганизация структуры (`server/server`, переносы в `_archive`, удаление временных скриптов/доков) не была полностью синхронизирована во всех markdown-файлах.

## Optimal Fix
Выполнен полный аудит ссылок по всем markdown, затем отдельный аудит активных документов (`Docs`, `client/Docs`, `server/server/Docs`, `AGENTS`).

## Verification
- Полный аудит (включая архивы/downloads):
  - `MISS_TOTAL=2540`
  - `MISS_UNIQUE_REFS=377`
  - `MISS_SOURCE_FILES=599`
- Аудит активных документов:
  - `MISS_TOTAL=164`
  - `MISS_UNIQUE_REFS=59`
  - `MISS_SOURCE_FILES=39`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `client/Docs/DOCS_INDEX.md`, `server/server/Docs/DOCS_INDEX.md`
- Source of Truth: root/client/server DOCS_INDEX + AGENTS
- Дублирование: исключены дубли в уже исправленных AGENTS/README/rules
- Feature Flags check: ссылки на FEATURE_FLAGS сохранены на существующие canonical файлы
- Race check: N/A (документационный аудит)

## Запрос/цель
Проверить, все ли документы актуальны с учетом реального кода.

## Контекст
- Проверены все `*.md` в репозитории.
- Отдельно выделены активные документы без `_archive` и `downloads`.

## Решения/выводы
1. Полный массив markdown содержит много исторического шума (ожидаемо).
2. Даже среди активных документов есть 59 уникальных невалидных ссылок.
3. Главные источники проблем: `client/Docs/REQUIREMENTS_SOURCE_MAP.md`, `client/Docs/PROJECT_REQUIREMENTS.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`.

## Топ отсутствующих ссылок (active audit)
- `Docs/TAL_TESTING_CHECKLIST.md` (17)
- `Docs/CRM_INSTRUCTION_REGISTRY.md` (16)
- `Docs/GLOBAL_DELIVERY_PLAN.md` (13)
- `scripts/check_tal_after_restart.py` (9)
- `scripts/test_tray_termination.py` (8)
- `Docs/CURRENT_STATUS_REPORT.md` (7)
- `Docs/TRAY_TERMINATION_FIX.md` (5)
- `Docs/TERMINAL_VS_APP_BUNDLE_DIFFERENCES.md` (4)
- `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md` (4)
- `Docs/UPDATE_SYSTEM_FIXES.md` (2)
- `Docs/MCP_INTEGRATION_SUMMARY.md` (2)
- `Docs/CRM_ASSISTANT_INSTRUCTIONS.md` (3)
- `Docs/CRM_CONSOLIDATED_RULES.md` (2)

## Открытые вопросы
- Восстанавливать отсутствующие документы (канон) или переводить ссылки на архив/новые замены точечно?

## Следующие шаги
1. Починить Top-20 ссылок в 4 главных источниках (`PROJECT_REQUIREMENTS*`, `ARCHITECTURE_OVERVIEW*`).
2. Для legacy-ссылок ввести явный маркер `(reference, archived)` и новый canonical путь.
3. Повторно прогнать active-audit как quality gate перед merge.
