# Root Docs Reality Alignment

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
Root-документация расходилась с фактической структурой проекта: устаревшие пути, старые значения startup/first-run, конфликтующие источники истины между root и client/server канонами.

## Root Cause
Исторические копии документов в root не синхронизировались после миграции на `client/*` и `server/server/*`, из-за чего появились неисполняемые ссылки и дубли архитектурного описания.

## Optimal Fix
- Root `Docs/ARCHITECTURE_OVERVIEW.md` переведён в index-only документ.
- `Docs/PROJECT_REQUIREMENTS.md` синхронизирован с реальными путями и артефактами.
- Убраны ссылки на несуществующие документы/скрипты, обновлены verification refs.
- REQ-006 выровнен с `IntegrationFactory.STARTUP_ORDER`.
- First-run требования выровнены с V2 (`client/modules/permissions/v2/*`, `permissions_v2.*`).

## Verification
- Проверена существуемость документируемых путей (кроме заведомо runtime-путей типа `dist/Nexy.app/Contents/Resources/`).
- Проверено отсутствие старых ссылок (`integration/*`, `modules/permissions/first_run/*`, `Docs/TAL_TESTING_CHECKLIST.md` и др.) в обновлённых sections.
- Проверено изменение diff только в целевых файлах root-документации.

## Запрос/цель
Привести root-документацию в соответствие с текущей реализацией проекта.

## Контекст
- Файлы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
- Каноны:
  - `client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `client/Docs/FLOW_INTERACTION_SPEC.md`
  - `server/server/Docs/ARCHITECTURE_OVERVIEW.md`

## Решения/выводы
- Root должен быть навигационным слоем, а не дублирующим runtime-каноном.
- Детали исполнения остаются у владельцев осей: `client/Docs/*` и `server/server/Docs/*`.

## Открытые вопросы
- Нужен ли отдельный CI скрипт, который валидирует все backtick-пути в `Docs/PROJECT_REQUIREMENTS.md` (рекомендуется).

## Следующие шаги
1. Добавить автоматическую проверку существования путей в CI.
2. Синхронизировать при необходимости `Docs/SYSTEM_CONCEPT.md` с новой ролью root-index.
