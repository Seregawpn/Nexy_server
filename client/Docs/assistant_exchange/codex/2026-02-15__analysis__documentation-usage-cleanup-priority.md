# Documentation Usage Audit and Cleanup Priority

Дата: 2026-02-15

## Метод

- Просканированы ссылки `Docs/*.md` по репозиторию (код + скрипты + активные docs, без архивов).
- Разделены категории:
  - активно используется (есть регулярные входящие ссылки, включая code/scripts/governance)
  - слабо используется (есть 1 ссылка, в основном из другого дока)
  - не используется (0 ссылок)
  - конфликтует (описывает устаревший owner/path или дублирует канон)

## 1) Активно используется (оставить)

- `Docs/STATE_CATALOG.md` (13 refs)
- `Docs/PACKAGING_FINAL_GUIDE.md` (11 refs)
- `Docs/PRE_PACKAGING_VERIFICATION.md` (10 refs)
- `Docs/ARCHITECTURE_OVERVIEW.md` (9 refs)
- `Docs/FEATURE_FLAGS.md` (9 refs)
- `Docs/first_run_flow_spec.md` (9 refs)
- `Docs/PACKAGING_READINESS_CHECKLIST.md` (8 refs)
- `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` (8 refs)
- `Docs/PROJECT_REQUIREMENTS.md` (7 refs)
- `Docs/README.md` (6 refs)
- `Docs/FLOW_INTERACTION_SPEC.md` (5 refs)

## 2) Слабо используется (кандидаты на merge/архив)

- `Docs/PRODUCT_CONCEPT.md` (4 refs)
- `Docs/DOCUMENTATION_MAP.md` (3 refs)
- `Docs/REQUIREMENTS_SOURCE_MAP.md` (3 refs)
- `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md` (1 ref)
- `Docs/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md` (1 ref)
- `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md` (1 ref)
- `Docs/INPUT_ARCHITECTURE_V2.md` (1 ref)

## 3) Не используется (0 refs, first-remove candidates)

- `Docs/HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`
- `Docs/HOTKEY_IMPLEMENTATION_PLAN.md`
- `Docs/HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`
- `Docs/TROUBLESHOOTING.md`

## 4) Конфликтует с текущей реальностью (убирать/править в первую очередь)

1. `Docs/FLOW_INTERACTION_SPEC.md`
- Конфликт: указан SoT `SimpleModuleCoordinator.startup_order`, фактически runtime использует `IntegrationFactory.STARTUP_ORDER`.
- Риск: неверные изменения init-order, дубли owner-path.

2. Hotkey cluster (конфликт дублирования канона)
- Документы: `HOTKEY_COMBINATION_REQUIREMENTS.md`, `HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`, `HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`, `HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`, `HOTKEY_IMPLEMENTATION_PLAN.md`, `HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`.
- Проблема: 6 документов про один домен с пересечением REQ/плана/диагноза; часть не реферится вообще.
- Риск: множественные “локальные каноны” и конфликт требований при правках hotkey.

3. `Docs/INPUT_ARCHITECTURE_V2.md` vs основной канон
- Проблема: отдельный SoT для input домена, в то время как общий event/owner канон уже в `FLOW_INTERACTION_SPEC` + `ARCHITECTURE_OVERVIEW`.
- Риск: параллельный owner-документ без governance.

## 5) Рекомендуемая стратегия очистки

### Шаг A (сразу, low-risk)
- Архивировать 0-ref документы:
  - `HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`
  - `HOTKEY_IMPLEMENTATION_PLAN.md`
  - `HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`
  - `TROUBLESHOOTING.md`

### Шаг B (разрулить конфликт)
- В `FLOW_INTERACTION_SPEC.md` заменить startup SoT на `IntegrationFactory.STARTUP_ORDER`.

### Шаг C (дедуп hotkey)
- Оставить 2 файла max:
  - 1 requirements: `HOTKEY_COMBINATION_REQUIREMENTS.md`
  - 1 implementation plan: `HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`
- Остальные hotkey docs архивировать.

### Шаг D (упростить навигацию)
- Оставить один индекс (`Docs/README.md`) + одну карту (`Docs/DOCUMENTATION_MAP.md`).
- `REQUIREMENTS_SOURCE_MAP.md` либо генерировать автоматически, либо сузить до ownership-only таблицы.

## 6) Приоритет удаления (по порядку)

P1:
- `Docs/HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`
- `Docs/HOTKEY_IMPLEMENTATION_PLAN.md`
- `Docs/HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`
- `Docs/TROUBLESHOOTING.md`

P2:
- `Docs/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md` (после merge в `HOTKEY_COMBINATION_REQUIREMENTS.md`)
- `Docs/INPUT_ARCHITECTURE_V2.md` (после выноса уникальных инвариантов в `FLOW_INTERACTION_SPEC.md`)

P3:
- `Docs/REQUIREMENTS_SOURCE_MAP.md` (если оставить auto-generated ownership реестр)

## Вывод

Самый безопасный и эффективный cleanup: удалить 0-ref документы, затем убрать конфликт SoT в `FLOW_INTERACTION_SPEC.md`, затем схлопнуть hotkey-дубли до 2 документов.
