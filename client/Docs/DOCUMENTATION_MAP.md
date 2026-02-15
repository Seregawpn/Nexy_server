# Карта документации Nexy Client

Цель: быстрый навигатор только по актуальным документам в `Docs/`.

## 1. Канонические документы (Source of Truth)

- `Docs/README.md` — master-index документации (единая точка входа)
- `Docs/PROJECT_REQUIREMENTS.md` — snapshot требований
- `Docs/ARCHITECTURE_OVERVIEW.md` — архитектура и границы слоёв
- `Docs/FLOW_INTERACTION_SPEC.md` — канон EventBus контрактов
- `Docs/STATE_CATALOG.md` — оси состояния и ownership
- `config/interaction_matrix.yaml` — правила взаимодействия осей
- `integration/core/gateways/` — реализация decision-логики

## 2. Runtime и поведение

- `Docs/first_run_flow_spec.md` — first-run / permissions V2
- `Docs/FEATURE_FLAGS.md` — реестр feature flags и kill-switches
- `Docs/PRODUCT_CONCEPT.md` — продуктовые сценарии

## 3. Release / Packaging

- `Docs/PACKAGING_FINAL_GUIDE.md` — канонический pipeline упаковки
- `Docs/PRE_PACKAGING_VERIFICATION.md` — pre-packaging проверки
- `Docs/PACKAGING_READINESS_CHECKLIST.md` — итоговый readiness чеклист
- `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` — версионирование и publish-политика

## 4. Requirements Navigation

- `Docs/REQUIREMENTS_SOURCE_MAP.md` — карта источников требований и владельцев

## 5. Правило синхронизации

При изменении runtime-логики синхронизировать артефакты в порядке:

1. `Docs/STATE_CATALOG.md`
2. `config/interaction_matrix.yaml`
3. `integration/core/gateways/`
4. `tests/test_gateways.py` и профильные тесты
5. `Docs/PROJECT_REQUIREMENTS.md`

## 6. Deprecated / Historical

Исторические и удалённые документы не использовать как источники истины.
Для истории использовать только `Docs/_archive/` и `_Docs_ARCHIVED/`.

Архивировано в рамках cleanup (2026-02-15):
- `Docs/_archive/HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`
- `Docs/_archive/HOTKEY_IMPLEMENTATION_PLAN.md`
- `Docs/_archive/HOTKEY_SHORTCUT_INTERCEPTION_DIAGNOSIS.md`
- `Docs/_archive/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`
- `Docs/_archive/INPUT_ARCHITECTURE_V2.md`
- `Docs/_archive/TROUBLESHOOTING.md`

---

Последнее обновление: 2026-02-15
