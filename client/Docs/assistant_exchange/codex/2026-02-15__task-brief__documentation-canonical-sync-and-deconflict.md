# Task Brief: Documentation Canonical Sync and Deconflict

Дата: 2026-02-15

## Что сделано

Синхронизирована каноническая документация клиента с текущим состоянием репозитория и runtime-реализацией.

Изменённые документы:
- `Docs/README.md`
- `Docs/DOCUMENTATION_MAP.md`
- `Docs/REQUIREMENTS_SOURCE_MAP.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/STATE_CATALOG.md`
- `Docs/first_run_flow_spec.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/PRODUCT_CONCEPT.md`
- `Docs/PACKAGING_FINAL_GUIDE.md`

## Ключевые исправления

1. Удалены/заменены несуществующие ссылки и пути в канонических документах.
2. Устранён конфликт first-run политики:
   - зафиксирован V2 owner path (`integrations.permissions_v2.order` + ledger),
   - убраны legacy-ссылки на удалённые implementation/verification артефакты.
3. Устранён конфликт Source of Truth по `firstRun` в `STATE_CATALOG.md` (ledger как SoT, flag как cache).
4. Обновлены verification refs в `PROJECT_REQUIREMENTS.md` на реально существующие тесты.
5. Исправлены архитектурные пути: `integration/core/gateways/` вместо несуществующего `integration/core/gateways.py`.
6. Обновлён `PACKAGING_FINAL_GUIDE.md` с удалением ссылок на отсутствующие TAL/utility scripts.

## Результат

Канонические документы больше не содержат обнаруженных ссылок на удалённые файлы из предыдущего аудита, а критичный блок first-run/permissions приведён к единой V2-модели.
