# Task Brief: Docs Cleanup by Usage and Conflict Priority

Дата: 2026-02-15

## Что выполнено

Сделан практический cleanup документации по результатам usage/conflict аудита.

### 1) Архивированы документы с нулевым/конфликтным использованием

Перенесены из `Docs/` в `Docs/_archive/`:
- `HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`
- `HOTKEY_IMPLEMENTATION_PLAN.md`
- `HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`
- `HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`
- `INPUT_ARCHITECTURE_V2.md`
- `TROUBLESHOOTING.md`

### 2) Исправлен конфликт Source of Truth

В `Docs/FLOW_INTERACTION_SPEC.md`:
- `Startup Flow` SoT изменён с `SimpleModuleCoordinator.startup_order` на `IntegrationFactory.STARTUP_ORDER` (через `get_startup_order(...)`), чтобы совпадать с реальным runtime.

### 3) Устранён конфликт по first-run verification модели

В `Docs/FLOW_INTERACTION_SPEC.md`:
- убрана формулировка `single post-trigger probe` как единственный механизм;
- зафиксировано, что verification в V2 может использовать polling (`AUTO_DIALOG`/`OPEN_SETTINGS`).

### 4) Обновлён навигатор

В `Docs/DOCUMENTATION_MAP.md`:
- удалён `Docs/INPUT_ARCHITECTURE_V2.md` из активного списка;
- добавлен блок архивированных документов cleanup-сессии.

## Результат

- Активный набор документации стал меньше и чище.
- Убраны конфликтующие/дублирующие hotkey и input документы.
- Канон startup owner-path и first-run verification синхронизирован с текущим кодом.
- Проверка ссылок `scripts/verify_doc_links.py` проходит без ошибок.
