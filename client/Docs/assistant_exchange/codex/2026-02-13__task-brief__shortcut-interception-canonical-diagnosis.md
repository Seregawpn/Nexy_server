# Task Brief — shortcut interception canonical diagnosis

## Context
Пользователь уточнил, что проблема в перекладке/перехвате комбинации, а не в "возврате фокуса" как первичной причине.

## Deliverable
Создан документ:
- `Docs/HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`

## Что зафиксировано
- Каноничная формулировка инцидента: `shortcut interception / misrouting`.
- Разделение primary root-cause и secondary focus effects.
- Source of Truth по owner-слоям.
- Инвариант: interception только для strict `Ctrl+N`.
- KPI и порядок верификации (сначала interception, затем focus).

## Architecture fit
- Архитектура не меняется.
- Централизация сохранена: suppression owner в Quartz path, PTT owner в InputProcessing.
